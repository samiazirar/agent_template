#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys


HUMAN_TAB = "01 Human"
OPERATIONS_TAB = "02 Operations"
TRANSIENT_TABS = {
    "03 Strategic Council",
    "04 Suborchestrators",
    "05 Workers",
    "06 Progress Checks",
}
TERMINAL_AGENT_STATES = {"done", "idle", "blocked"}
TRANSIENT_PREFIXES = {
    "Plan Orchestrator",
    "Worker",
    "Suborchestrator",
    "Suborch",
    "Strategic Advisor",
    "Advisor",
    "Researcher",
    "Research Observer",
    "Verifier",
    "Watcher",
    "Progress",
    "Progress Checker",
    "Second Eye",
    "PaperPilot Maintainer",
}


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


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_pane_lifecycle.py WORKSPACE_ID")

    workspace_id = sys.argv[1]
    tabs = herdr("tab", "list", "--workspace", workspace_id)["result"]["tabs"]
    tab_labels = {tab["tab_id"]: tab["label"] for tab in tabs}
    panes = herdr("pane", "list", "--workspace", workspace_id)["result"]["panes"]

    stale: list[str] = []
    for pane in panes:
        tab_label = tab_labels[pane["tab_id"]]
        pane_label = pane.get("label", "")
        prefix = pane_label.split(" · ", 1)[0]
        is_named_transient = prefix in TRANSIENT_PREFIXES
        if tab_label not in TRANSIENT_TABS and not is_named_transient:
            continue
        if not pane.get("agent") and not pane.get("agent_session"):
            continue
        if pane.get("agent_status") in TERMINAL_AGENT_STATES:
            stale.append(
                f"{pane_label or 'unnamed pane'} "
                f"({tab_label}, state={pane.get('agent_status')})"
            )

    if stale:
        fail(
            "transient purposes have ended but panes remain open; archive their "
            f"session IDs and close them: {stale}"
        )

    human = [
        pane for pane in panes
        if tab_labels[pane["tab_id"]] == HUMAN_TAB
    ]
    human_prefixes = [pane["label"].split(" · ", 1)[0] for pane in human]
    if human_prefixes != ["Human Orchestrator"]:
        fail(
            "01 Human must contain only one Human Orchestrator; "
            f"found {human_prefixes}"
        )

    operations = [
        pane for pane in panes
        if tab_labels[pane["tab_id"]] == OPERATIONS_TAB
    ]
    operations_prefixes = [
        pane["label"].split(" · ", 1)[0] for pane in operations
    ]
    unexpected = [
        prefix
        for prefix in operations_prefixes
        if prefix not in {
            "Operations Lead",
            "Operations Collaborator",
            "Plan Orchestrator",
        }
    ]
    if (
        operations_prefixes.count("Operations Lead") != 1
        or operations_prefixes.count("Operations Collaborator") > 1
        or unexpected
    ):
        fail(
            "02 Operations must contain exactly one Operations Lead; only an "
            "explicit Operations Collaborator and an active temporary Plan "
            "Orchestrator may join it; "
            f"found {operations_prefixes}"
        )

    print(json.dumps({
        "ok": True,
        "workspace_id": workspace_id,
        "stale_transient_agents": 0,
    }, indent=2))


if __name__ == "__main__":
    main()
