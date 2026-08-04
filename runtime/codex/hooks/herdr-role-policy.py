#!/usr/bin/env python3
"""Keep Herdr control roles out of project implementation and raw launches."""

from __future__ import annotations

import json
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path


CONTROL_ROLES = {
    "Human Orchestrator",
    "Operations Lead",
    "Operations Collaborator",
    "Plan Orchestrator",
    "Suborchestrator",
}
TASK_CARD_ROOT = (
    Path(os.environ.get("XDG_STATE_HOME", Path.home() / ".local/state"))
    / "herdr" / "task-cards"
).resolve()
TECHNICAL_COMMAND = re.compile(
    r"(?:^|[;&|()]\s*)"
    r"(?:ssh|scp|rsync|sbatch|srun|docker|podman|apptainer|pytest|ctest|"
    r"make|cmake|ninja|cargo|npm|pnpm|yarn|pip|python(?:3)?\s+(?!.*validate_task_card\.py)|"
    r"bash\s+[^-]|sh\s+[^-]|\./[^\s]+)",
    re.IGNORECASE,
)
MUTATING_COMMAND = re.compile(
    r"\b(?:sed\s+-i|perl\s+-pi|git\s+apply|patch\s+-p\d*|tee|truncate|"
    r"touch|install|cp|mv|rm)\b|(?:^|\s)(?:>|>>)(?:\s|$)",
    re.IGNORECASE,
)
RAW_AGENT_LAUNCH = re.compile(
    r"\bherdr\s+(?:agent\s+start|pane\s+run)\b|"
    r"(?:^|[;&|()]\s*)(?:codex|claude|claudex|opencode)\b",
    re.IGNORECASE,
)


def current_role() -> str:
    if os.environ.get("HERDR_ENV") != "1" or not os.environ.get("HERDR_PANE_ID"):
        return ""
    try:
        raw = subprocess.run(
            ["herdr", "pane", "get", os.environ["HERDR_PANE_ID"]],
            check=True,
            text=True,
            capture_output=True,
            timeout=2,
        ).stdout
        label = json.loads(raw)["result"]["pane"].get("label", "")
    except (OSError, KeyError, json.JSONDecodeError, subprocess.SubprocessError):
        return ""
    return label.split(" · ", 1)[0]


def deny(reason: str) -> None:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))


def plan_context(cwd: str, role: str) -> str:
    if role not in CONTROL_ROLES:
        return ""
    path = Path(cwd) / "HUMAN_PLAN.md"
    if not path.is_file():
        return (
            f"Herdr role guard: you are {role}. Keep the assigned role boundary; "
            "do not perform a technical package yourself."
        )
    lines = [line.strip() for line in path.read_text(errors="replace").splitlines()]
    useful = [line for line in lines if line and not line.startswith("<!--")][:12]
    excerpt = "\n".join(useful)[:1600]
    return (
        f"Herdr role guard: you are {role}. The current Human Plan begins:\n"
        f"{excerpt}\n"
        "Only take actions causally tied to this plan. Control roles dispatch and "
        "integrate; they do not perform the technical package."
    )


def task_state_path(suffix: str) -> Path | None:
    workspace = os.environ.get("HERDR_WORKSPACE_ID")
    pane = os.environ.get("HERDR_PANE_ID")
    if not workspace or not pane:
        return None
    root = Path(os.environ.get("XDG_STATE_HOME", Path.home() / ".local/state"))
    return root / "herdr" / "task-cards" / workspace / f"{pane}.{suffix}"


def git_text(cwd: str, *args: str) -> str:
    try:
        return subprocess.run(
            ["git", "-C", cwd, *args],
            check=True,
            text=True,
            capture_output=True,
            timeout=3,
        ).stdout
    except (OSError, subprocess.SubprocessError):
        return ""


def stop_risks(payload: dict[str, object], role: str) -> list[str]:
    risks: list[str] = []
    message = str(payload.get("last_assistant_message") or "")
    lowered_message = message.casefold()
    continuing_job = re.search(
        r"\b(?:submitted|queued|running|sbatch|job(?:\s+id)?\s*[:#=]?\s*\d+)\b",
        lowered_message,
    )
    continuity = re.search(
        r"\b(?:watch(?:er|ing)?|wake|terminal event|completion event|"
        r"terminal owner|event-driven|next action owner)\b",
        lowered_message,
    )
    terminal = re.search(
        r"\b(?:completed|finished|failed|cancelled|canceled|timed out|timeout|"
        r"stopped|exited|terminal)\b",
        lowered_message,
    )
    if (
        role in {"Worker", "Suborchestrator", "Operations Lead"}
        and continuing_job
        and not continuity
        and not terminal
    ):
        risks.append(
            "A continuing job is reported without a named terminal wake path. "
            "Arrange one event-driven wake owner before stopping; do not poll."
        )

    if role != "Worker":
        return risks

    card_path = task_state_path("card")
    base_path = task_state_path("base")
    if not card_path or not base_path or not card_path.is_file() or not base_path.is_file():
        return risks

    card = card_path.read_text(encoding="utf-8", errors="replace").casefold()
    base = base_path.read_text(encoding="utf-8", errors="replace").strip()
    cwd = str(payload.get("cwd") or ".")
    head = git_text(cwd, "rev-parse", "HEAD").strip()
    if not base or not head:
        return risks

    changed = set(git_text(cwd, "diff", "--name-only", f"{base}..{head}").splitlines())
    status = git_text(cwd, "status", "--porcelain")
    changed.update(line[3:] for line in status.splitlines() if len(line) > 3)
    changed.discard("")
    if not changed:
        return risks

    example_surface = re.compile(
        r"(?:^|/)(?:examples?|fixtures?|samples?|tests?)(?:/|$)|"
        r"(?:^|/)(?:example|fixture|sample|test)[^/]*\.[^/]+$",
        re.IGNORECASE,
    )
    task_targets_example = re.search(
        r"\b(?:example|fixture|sample|test|documentation|docs)\b", card
    )
    if not task_targets_example and all(example_surface.search(path) for path in changed):
        risks.append(
            "Only example, fixture, sample, or test surfaces changed although the task asks "
            "for general behavior. Recheck the shared execution path behind the example."
        )

    dependency_files = {
        "package.json", "pyproject.toml", "requirements.txt", "cargo.toml",
        "go.mod", "environment.yml", "environment.yaml",
    }
    if any(Path(path).name.casefold() in dependency_files for path in changed) and not re.search(
        r"\b(?:dependency|package|environment)\b", card
    ):
        risks.append(
            "The change adds or alters dependency configuration although the task does not "
            "require a dependency. Prefer the existing implementation path."
        )

    name_status = git_text(cwd, "diff", "--name-status", f"{base}..{head}")
    added_files = [line for line in name_status.splitlines() if line.startswith("A\t")]
    if len(added_files) > 3:
        risks.append(
            f"The task added {len(added_files)} files. Confirm they are all necessary for the "
            "single requested result; remove scaffolding or parallel paths that are not."
        )

    added_diff = git_text(cwd, "diff", "--unified=0", f"{base}..{head}")
    added_lines = "\n".join(
        line[1:] for line in added_diff.splitlines()
        if line.startswith("+") and not line.startswith("+++")
    ).casefold()
    if re.search(r"\b(?:workaround|special[ -]?case|temporary fix|hotfix|hack)\b", added_lines):
        risks.append(
            "The patch describes a workaround or special case. Reproduce the original failure "
            "and confirm the change repairs its shared causal source rather than that one input."
        )
    return risks


def guard_stop(payload: dict[str, object], role: str) -> int:
    risks = stop_risks(payload, role)
    if not risks:
        return 0
    head = git_text(str(payload.get("cwd") or "."), "rev-parse", "HEAD").strip()
    signature = hashlib.sha256((role + head + "\n".join(risks)).encode()).hexdigest()[:20]
    seen = task_state_path(f"stop-{signature}")
    if seen and seen.exists():
        return 0
    if seen:
        seen.parent.mkdir(parents=True, exist_ok=True)
        seen.touch(mode=0o600)
    prompt = (
        "Before stopping, resolve this bounded completion risk:\n- "
        + "\n- ".join(risks)
        + "\nIf the signal is false, state the concrete reason once. Otherwise make the "
        "smallest root-level correction and rerun only the assigned done check. "
        "Do not broaden the task, add a review round, or create support artifacts."
    )
    print(prompt, file=sys.stderr)
    return 2


def main() -> int:
    payload = json.load(sys.stdin)
    event = payload.get("hook_event_name", "")
    role = current_role()

    if event == "SessionStart":
        context = plan_context(payload.get("cwd", "."), role)
        if context:
            print(json.dumps({
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": context,
                }
            }))
        return 0

    if event == "Stop":
        return guard_stop(payload, role)

    if event != "PreToolUse" or not role:
        return 0

    tool = payload.get("tool_name", "")
    tool_input = payload.get("tool_input") or {}
    if not isinstance(tool_input, dict):
        tool_input = {"command": str(tool_input)}

    if tool == "apply_patch":
        patch = str(tool_input.get("command", ""))
        if role == "Plan Orchestrator":
            paths = re.findall(r"^\*\*\* (?:Add|Update|Delete) File: (.+)$", patch, re.MULTILINE)
            if paths and all(Path(path).name == "HUMAN_PLAN.md" for path in paths):
                return 0
            deny("Plan Orchestrator may edit only HUMAN_PLAN.md.")
            return 0
        if role in {"Operations Lead", "Suborchestrator"}:
            paths = re.findall(r"^\*\*\* (?:Add|Update|Delete) File: (.+)$", patch, re.MULTILINE)
            resolved = [Path(path).resolve() for path in paths]
            relative = []
            for path in resolved:
                try:
                    relative.append(path.relative_to(TASK_CARD_ROOT))
                except ValueError:
                    break
            if paths and len(relative) == len(paths) and all(
                len(path.parts) == 2 and path.suffix == ".card"
                for path in relative
            ):
                return 0
        if role in CONTROL_ROLES:
            deny(f"{role} may not edit project files; dispatch the package to Luna.")
            return 0

    if tool != "Bash" or role not in CONTROL_ROLES:
        return 0

    command = str(tool_input.get("command") or tool_input.get("cmd") or "")
    if role == "Human Orchestrator":
        allowed = re.match(
            r"^\s*(?:herdr-role-message\s+operations\b|"
            r"herdr-project-save-close\s+--close\b|"
            r"herdr-restore-operations\s*$)",
            command,
        )
        if not allowed:
            deny("Human Orchestrator may only message Operations, run the guarded Operations restore, or perform the guarded project close.")
        return 0

    if RAW_AGENT_LAUNCH.search(command):
        deny("Raw agent launch is disabled for control roles; use herdr-agent so role and model policy are checked.")
        return 0
    if TECHNICAL_COMMAND.search(command):
        deny(f"{role} may not execute project, cluster, container, test, or debugging commands; dispatch Luna.")
        return 0
    if MUTATING_COMMAND.search(command):
        deny(f"{role} may not write project files from the shell; dispatch Luna or use the bounded plan writer.")
        return 0
    if role == "Suborchestrator" and re.search(r"\bgit\s+(?!show\b|log\b|status\b|diff\b|rev-parse\b)", command):
        deny("Suborchestrator may inspect supplied Git state only; Operations integrates worker commits.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
