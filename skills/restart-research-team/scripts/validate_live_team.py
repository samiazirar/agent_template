#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path


EXPECTED_TABS = [
    "00 Human Plan",
    "01 Orchestrators",
    "02 Strategic Council",
    "03 Suborchestrators",
    "04 Workers",
    "05 Progress Checks",
    "99 Old History",
]

ONBOARDING_PATH = Path("/home/user/azirar/.agents/RESEARCH_AGENT_ONBOARDING.md")
ORCHESTRATION_PATH = Path("/home/user/azirar/.agents/RESEARCH_ORCHESTRATION.md")
PAPERPILOT_PATH = Path("/home/user/azirar/.agents/PAPERPILOT_PROJECT_STANDARD.md")
GLOBAL_CLAUDE_PATH = Path("/home/user/azirar/.claude/CLAUDE.md")


def herdr(*args: str) -> dict:
    result = subprocess.run(
        ["herdr", *args],
        check=True,
        text=True,
        capture_output=True,
    )
    return json.loads(result.stdout)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def process_started_at(pid: int) -> float:
    stat_fields = Path(f"/proc/{pid}/stat").read_text().split()
    start_ticks = int(stat_fields[21])
    clock_ticks = os.sysconf(os.sysconf_names["SC_CLK_TCK"])
    uptime = float(Path("/proc/uptime").read_text().split()[0])
    boot_time = time.time() - uptime
    return boot_time + start_ticks / clock_ticks


def require_fresh_frogmouth(pane_id: str, markdown_path: Path) -> None:
    payload = herdr("pane", "process-info", "--pane", pane_id)
    processes = payload["result"]["process_info"]["foreground_processes"]
    frogmouth = next(
        (
            process
            for process in processes
            if process.get("name") == "frogmouth"
            or any("frogmouth" in arg for arg in process.get("argv", []))
        ),
        None,
    )
    if frogmouth is None:
        fail(f"{pane_id} is not running Frogmouth")
    process_cwd = Path(frogmouth.get("cwd", "."))
    resolved_args = {
        str(
            (
                Path(arg)
                if Path(arg).is_absolute()
                else process_cwd / arg
            ).resolve()
        )
        for arg in frogmouth.get("argv", [])
        if arg.endswith(".md")
    }
    if str(markdown_path.resolve()) not in resolved_args:
        fail(f"{pane_id} is not displaying {markdown_path}")
    if markdown_path.stat().st_mtime > process_started_at(frogmouth["pid"]) + 1:
        fail(f"{markdown_path} changed after Frogmouth started; refresh the pane")


def foreground_argv(pane_id: str) -> list[str]:
    payload = herdr("pane", "process-info", "--pane", pane_id)
    processes = payload["result"]["process_info"]["foreground_processes"]
    if not processes:
        fail(f"{pane_id} has no foreground process")
    return processes[0].get("argv", [])


def require_model(
    pane: dict, role: str, model: str, effort: str
) -> None:
    argv = foreground_argv(pane["pane_id"])
    command = " ".join(argv)
    if model not in argv:
        fail(f"{role} is not using {model}: {command}")
    effort_forms = {
        f"model_reasoning_effort={effort}",
        f'model_reasoning_effort="{effort}"',
    }
    effort_index = argv.index("--effort") + 1 if "--effort" in argv else -1
    has_claudex_effort = (
        effort_index > 0
        and effort_index < len(argv)
        and argv[effort_index] == effort
    )
    if not effort_forms.intersection(argv) and not has_claudex_effort:
        fail(f"{role} is not using {effort} reasoning: {command}")


def require_native_claude_model(
    pane: dict, role: str, model: str, effort: str
) -> None:
    argv = foreground_argv(pane["pane_id"])
    command = " ".join(argv)
    executable = Path(argv[0]).name if argv else ""
    if executable != "claude":
        fail(f"{role} is not using native Claude: {command}")
    model_index = argv.index("--model") + 1 if "--model" in argv else -1
    if model_index <= 0 or model_index >= len(argv) or model not in argv[model_index]:
        fail(f"{role} is not using {model}: {command}")
    effort_index = argv.index("--effort") + 1 if "--effort" in argv else -1
    if (
        effort_index <= 0
        or effort_index >= len(argv)
        or argv[effort_index] != effort
    ):
        fail(f"{role} is not using {effort} effort: {command}")


def main() -> None:
    if len(sys.argv) != 3:
        fail("usage: validate_live_team.py WORKSPACE_ID PROJECT_DIR")

    workspace_id = sys.argv[1]
    project_dir = Path(sys.argv[2]).resolve()

    for contract in (ONBOARDING_PATH, ORCHESTRATION_PATH, PAPERPILOT_PATH):
        if not contract.is_file() or contract.stat().st_size == 0:
            fail(f"missing or empty canonical contract {contract}")

    for filename in ("HUMAN_PLAN.md", "OLD_HISTORY.md", "AGENTS.md"):
        path = project_dir / filename
        if not path.is_file() or path.stat().st_size == 0:
            fail(f"missing or empty {path}")

    agents_text = (project_dir / "AGENTS.md").read_text(encoding="utf-8")
    if "RESEARCH_AGENT_ONBOARDING.md" not in agents_text:
        fail("AGENTS.md does not require the canonical research-agent onboarding")
    project_claude_path = project_dir / "CLAUDE.md"
    claude_path = (
        project_claude_path
        if project_claude_path.is_file()
        else GLOBAL_CLAUDE_PATH
    )
    if not claude_path.is_file() or claude_path.stat().st_size == 0:
        fail(
            "neither a project CLAUDE.md nor the canonical global "
            f"{GLOBAL_CLAUDE_PATH} is available"
        )
    claude_text = claude_path.read_text(encoding="utf-8")
    if (
        "RESEARCH_AGENT_ONBOARDING.md" not in claude_text
        and "RESEARCH_ORCHESTRATION.md" not in claude_text
    ):
        fail(f"{claude_path} does not import the canonical research instructions")

    human_plan = (project_dir / "HUMAN_PLAN.md").read_text(encoding="utf-8")
    required_sections = {
        "clear goal": r"^## .*(goal|trying to learn|scientific question|research question|project question|the question)",
        "current measured reality": r"^## .*(current|actually been measured|data exist|already exists|does not exist yet)",
        "meaningful milestone": r"^## .*(meaningful change|milestone|first measurable|frozen work)",
        "next useful result": r"^## .*(next useful|next inspectable|next productive|next result)",
    }
    for label, pattern in required_sections.items():
        if not re.search(pattern, human_plan, re.IGNORECASE | re.MULTILINE):
            fail(f"HUMAN_PLAN.md lacks a {label} section")
    if "locked cell" in human_plan.lower():
        fail("HUMAN_PLAN.md contains untranslated 'locked cell' shorthand")
    goal_match = re.search(
        r"^## [^\n]*(?:goal|trying to learn|scientific question|research question|project question|the question)[^\n]*$"
        r"(.*?)(?=^## |\Z)",
        human_plan,
        re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if goal_match is None or len(goal_match.group(1).split()) < 12:
        fail("HUMAN_PLAN.md lacks a readable, substantive goal")
    if len(human_plan.split()) > 2200:
        fail("HUMAN_PLAN.md exceeds 2200 words; move technical detail elsewhere")
    if re.search(r"\bw[0-9A-Za-z]+:p[0-9A-Za-z]+\b", human_plan):
        fail("HUMAN_PLAN.md contains a raw pane identifier")
    if re.search(r"\b[0-9a-f]{40,64}\b", human_plan, re.IGNORECASE):
        fail("HUMAN_PLAN.md contains a raw hash")
    if re.search(r"(?:^|[\s`])/(?:home|tmp|mnt|scratch)/", human_plan):
        fail("HUMAN_PLAN.md contains an internal filesystem path")
    if re.search(r"\b(?:gate|gates|blocker|blockers|NO_GO)\b", human_plan, re.IGNORECASE):
        fail("HUMAN_PLAN.md contains opaque stop-process language")
    internal_human_terms = re.compile(
        r"\b(?:evidence|observable|durable|routing|lifecycle|pane|session|worker)\b"
        r"|accepted meaning|completion envelope|READY FOR HUMAN|HUMAN_HANDOFF_READY",
        re.IGNORECASE,
    )
    found_internal_terms = sorted({
        match.group(0).lower()
        for match in internal_human_terms.finditer(human_plan)
    })
    if found_internal_terms:
        fail(
            "HUMAN_PLAN.md contains internal orchestration language: "
            f"{found_internal_terms}"
        )
    if re.search(r"^#{1,6}\s+[A-Z][A-Z0-9 _—-]{5,}$", human_plan, re.MULTILINE):
        fail("HUMAN_PLAN.md contains an all-caps process heading")

    tab_payload = herdr("tab", "list", "--workspace", workspace_id)
    tabs = tab_payload["result"]["tabs"]
    labels = [tab["label"] for tab in tabs]
    if labels != EXPECTED_TABS:
        fail(f"tab order is {labels!r}, expected {EXPECTED_TABS!r}")

    by_label = {tab["label"]: tab for tab in tabs}
    expected_counts = {
        "00 Human Plan": 1,
        "01 Orchestrators": 3,
        "02 Strategic Council": 1,
        "03 Suborchestrators": 1,
        "04 Workers": 1,
        "05 Progress Checks": 1,
        "99 Old History": 1,
    }
    for label, count in expected_counts.items():
        actual = by_label[label]["pane_count"]
        if actual != count:
            fail(f"{label} has {actual} panes, expected {count}")

    pane_payload = herdr("pane", "list", "--workspace", workspace_id)
    panes = pane_payload["result"]["panes"]
    panes_by_tab: dict[str, list[dict]] = {}
    for pane in panes:
        panes_by_tab.setdefault(pane["tab_id"], []).append(pane)
    require_fresh_frogmouth(
        panes_by_tab[by_label["00 Human Plan"]["tab_id"]][0]["pane_id"],
        project_dir / "HUMAN_PLAN.md",
    )
    require_fresh_frogmouth(
        panes_by_tab[by_label["99 Old History"]["tab_id"]][0]["pane_id"],
        project_dir / "OLD_HISTORY.md",
    )

    leadership = panes_by_tab[by_label["01 Orchestrators"]["tab_id"]]
    operations = [
        pane
        for pane in leadership
        if pane["label"].startswith("Operations Lead · ")
    ]
    collaborators = [
        pane
        for pane in leadership
        if pane["label"].startswith("Operations Collaborator · ")
    ]
    liaisons = [
        pane
        for pane in leadership
        if pane["label"].startswith("Human Orchestrator · ")
    ]
    if len(operations) != 1 or len(collaborators) != 1 or len(liaisons) != 1:
        fail(
            "01 Orchestrators must contain one Human Orchestrator, one "
            "Operations Lead, and one Operations Collaborator"
        )
    for pane in leadership:
        if pane.get("agent") not in {"codex", "claude"}:
            fail(f"standing leadership pane is not an agent: {pane['label']}")
        if pane.get("agent_status") not in {"idle", "done"}:
            fail(f"standing leadership is not waiting: {pane['label']}")
    require_model(operations[0], "Operations Lead", "gpt-5.6-sol", "high")
    require_model(liaisons[0], "Human Orchestrator", "gpt-5.6-sol", "high")
    require_native_claude_model(
        collaborators[0],
        "Operations Collaborator",
        "opus",
        "medium",
    )

    transient_tabs = (
        "02 Strategic Council",
        "03 Suborchestrators",
        "04 Workers",
        "05 Progress Checks",
    )
    for label in transient_tabs:
        pane = panes_by_tab[by_label[label]["tab_id"]][0]
        if pane.get("agent") or pane.get("agent_session"):
            fail(f"{label} retains a completed or active agent instead of an empty bay")

    active = [pane for pane in panes if pane.get("agent_status") in {"working", "blocked"}]
    if active:
        fail(f"active research agents remain: {[p['label'] for p in active]}")

    print(json.dumps({
        "ok": True,
        "workspace_id": workspace_id,
        "project_dir": str(project_dir),
        "tabs": labels,
        "standing_agents": [
            liaisons[0]["label"],
            operations[0]["label"],
            collaborators[0]["label"],
        ],
        "active_agents": 0,
    }, indent=2))


if __name__ == "__main__":
    main()
