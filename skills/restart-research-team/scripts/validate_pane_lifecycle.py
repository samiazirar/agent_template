#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys


STANDING_TAB = "01 Orchestrators"
TRANSIENT_TABS = {
    "02 Strategic Council",
    "03 Suborchestrators",
    "04 Workers",
    "05 Progress Checks",
}
TERMINAL_AGENT_STATES = {"done", "idle", "blocked"}
STANDING_PREFIXES = {
    "Human Orchestrator",
    "Operations Lead",
    "Operations Collaborator",
}
TRANSIENT_ORCHESTRATOR_PREFIX = "Plan Orchestrator"


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
        is_transient_orchestrator = (
            tab_label == STANDING_TAB
            and prefix == TRANSIENT_ORCHESTRATOR_PREFIX
        )
        if tab_label not in TRANSIENT_TABS and not is_transient_orchestrator:
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

    standing = [
        pane for pane in panes
        if tab_labels[pane["tab_id"]] == STANDING_TAB
    ]
    if standing:
        prefixes = [pane["label"].split(" · ", 1)[0] for pane in standing]
        standing_counts = {
            prefix: prefixes.count(prefix)
            for prefix in STANDING_PREFIXES
        }
        unexpected = [
            prefix
            for prefix in prefixes
            if prefix not in STANDING_PREFIXES
            and prefix != TRANSIENT_ORCHESTRATOR_PREFIX
        ]
        if any(count != 1 for count in standing_counts.values()) or unexpected:
            fail(
                "standing leadership must contain exactly one Human Orchestrator, "
                "one Operations Lead, and one Operations Collaborator; only an "
                "active temporary Plan Orchestrator may join them; "
                f"found {prefixes}"
            )

    print(json.dumps({
        "ok": True,
        "workspace_id": workspace_id,
        "stale_transient_agents": 0,
    }, indent=2))


if __name__ == "__main__":
    main()
