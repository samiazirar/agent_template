#!/usr/bin/env python3
"""Keep Herdr control roles out of project implementation and raw launches."""

from __future__ import annotations

import json
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
        if role in CONTROL_ROLES:
            deny(f"{role} may not edit project files; dispatch the package to Luna.")
            return 0

    if tool != "Bash" or role not in CONTROL_ROLES:
        return 0

    command = str(tool_input.get("command") or tool_input.get("cmd") or "")
    if role == "Human Orchestrator":
        allowed = re.match(
            r"^\s*(?:herdr-role-message\s+operations\b|"
            r"herdr-project-save-close\s+--close\b)",
            command,
        )
        if not allowed:
            deny("Human Orchestrator may only message Operations or perform the guarded project close.")
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
