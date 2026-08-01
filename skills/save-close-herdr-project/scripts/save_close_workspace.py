#!/usr/bin/env python3
"""Validate a saved research project and close only the caller's Herdr workspace."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


REQUIRED_FILES = ("HUMAN_PLAN.md", "OLD_HISTORY.md", "RESTART_HANDOFF.md")
REQUIRED_HANDOFF_TEXT = (
    "Status: CAN RESTART",
    "Close state: READY TO CLOSE",
    "## Goal",
    "## Current state",
    "## Continue from here",
    "## Running outside this workspace",
    "## Git and saved work",
    "## Restart context",
    "## Human choices",
)
TRANSIENT_TABS = {
    "03 Strategic Council",
    "04 Suborchestrators",
    "05 Workers",
    "06 Progress Checks",
}
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
STANDING_PREFIXES = {
    "Human Orchestrator",
    "Operations Lead",
    "Operations Collaborator",
}
IDLE_FOREGROUND = {"bash", "dash", "fish", "frogmouth", "sh", "zsh"}


class CloseError(RuntimeError):
    pass


def command(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
    )


def require_command(*args: str, cwd: Path | None = None) -> str:
    result = command(*args, cwd=cwd)
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip() or "command failed"
        raise CloseError(detail)
    return result.stdout.strip()


def herdr(*args: str) -> dict:
    raw = require_command("herdr", *args)
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CloseError(f"Herdr returned unreadable state: {exc}") from exc


def current_project() -> tuple[dict, str, Path]:
    if os.environ.get("HERDR_ENV") != "1":
        raise CloseError("This command must run inside Herdr.")

    workspace_id = os.environ.get("HERDR_WORKSPACE_ID", "")
    if not workspace_id:
        raise CloseError("The current Herdr workspace is unavailable.")

    pane = herdr("pane", "current", "--current")["result"]["pane"]
    if pane.get("workspace_id") != workspace_id:
        raise CloseError("Herdr did not resolve the caller's own workspace.")
    if not pane.get("label", "").startswith("Human Orchestrator · "):
        raise CloseError("Only the current project's Human Orchestrator may close it.")

    cwd = Path(pane.get("foreground_cwd") or pane.get("cwd") or ".").resolve()
    root_text = require_command("git", "rev-parse", "--show-toplevel", cwd=cwd)
    root = Path(root_text).resolve()
    return pane, workspace_id, root


def check_handoff(root: Path) -> None:
    for name in REQUIRED_FILES:
        path = root / name
        if not path.is_file() or path.stat().st_size == 0:
            raise CloseError(f"{name} is missing or empty.")

    handoff = (root / "RESTART_HANDOFF.md").read_text(encoding="utf-8")
    missing = [text for text in REQUIRED_HANDOFF_TEXT if text not in handoff]
    if missing:
        raise CloseError(
            "RESTART_HANDOFF.md is incomplete; missing: " + ", ".join(missing)
        )

    changed_in_head = require_command(
        "git", "show", "--pretty=format:", "--name-only", "HEAD", cwd=root
    ).splitlines()
    if "RESTART_HANDOFF.md" not in changed_in_head:
        raise CloseError("The final save commit must include RESTART_HANDOFF.md.")


def check_git(root: Path) -> None:
    if require_command("git", "status", "--porcelain", "--untracked-files=all", cwd=root):
        raise CloseError("The project repository still has uncommitted files.")

    remotes = require_command("git", "remote", cwd=root).splitlines()
    if not remotes:
        handoff = (root / "RESTART_HANDOFF.md").read_text(encoding="utf-8")
        if "Remote: none" not in handoff:
            raise CloseError(
                "The repository has no remote; record 'Remote: none' in the handoff."
            )
        return

    branch = require_command("git", "symbolic-ref", "--quiet", "--short", "HEAD", cwd=root)
    if not branch:
        raise CloseError("The project is on a detached Git commit.")

    upstream_result = command(
        "git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}", cwd=root
    )
    if upstream_result.returncode:
        raise CloseError("The current branch has no upstream remote branch.")

    counts = require_command(
        "git", "rev-list", "--left-right", "--count", "HEAD...@{upstream}", cwd=root
    ).split()
    if counts != ["0", "0"]:
        raise CloseError("The canonical branch is not synchronized with its upstream.")


def check_workspace(workspace_id: str) -> None:
    tabs = herdr("tab", "list", "--workspace", workspace_id)["result"]["tabs"]
    tab_names = {tab["tab_id"]: tab.get("label", "") for tab in tabs}
    panes = herdr("pane", "list", "--workspace", workspace_id)["result"]["panes"]

    remaining: list[str] = []
    busy_shells: list[str] = []
    human_roles: list[str] = []
    operations_roles: list[str] = []
    for pane in panes:
        label = pane.get("label", "")
        prefix = label.split(" · ", 1)[0]
        tab_name = tab_names.get(pane.get("tab_id"), "")
        if pane.get("agent") or pane.get("agent_session"):
            if tab_name == "01 Human":
                human_roles.append(prefix)
            if tab_name == "02 Operations":
                operations_roles.append(prefix)
            if tab_name in TRANSIENT_TABS or prefix in TRANSIENT_PREFIXES:
                remaining.append(label or f"unnamed role in {tab_name}")
            continue

        process_info = herdr("pane", "process-info", "--pane", pane["pane_id"])[
            "result"
        ]["process_info"]
        process_names = {
            item.get("name", "")
            for item in process_info.get("foreground_processes", [])
            if item.get("name")
        }
        unexpected = sorted(process_names - IDLE_FOREGROUND)
        if unexpected:
            busy_shells.append(f"{label or tab_name}: {', '.join(unexpected)}")

    if remaining:
        raise CloseError("Temporary project roles are still open: " + "; ".join(remaining))
    if busy_shells:
        raise CloseError(
            "Long-running foreground processes are still inside this workspace: "
            + "; ".join(busy_shells)
        )

    unexpected = [
        prefix
        for prefix in human_roles + operations_roles
        if prefix not in STANDING_PREFIXES
    ]
    if (
        human_roles != ["Human Orchestrator"]
        or operations_roles.count("Operations Lead") != 1
        or operations_roles.count("Operations Collaborator") > 1
        or any(prefix == "Human Orchestrator" for prefix in operations_roles)
        or any(prefix != "Human Orchestrator" for prefix in human_roles)
        or unexpected
    ):
        raise CloseError(
            "The standing project roles are ambiguous; require only one Human "
            "Orchestrator in 01 Human, and one Operations Lead with at most one "
            "Operations Collaborator in 02 Operations. Found Human: "
            f"{', '.join(human_roles) or 'none'}; Operations: "
            f"{', '.join(operations_roles) or 'none'}."
        )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check the current saved project and optionally close its workspace."
    )
    parser.add_argument(
        "--close",
        action="store_true",
        help="close the caller's current workspace after all checks pass",
    )
    args = parser.parse_args()

    try:
        pane, workspace_id, root = current_project()
        check_handoff(root)
        check_git(root)
        check_workspace(workspace_id)
    except CloseError as exc:
        print(f"Cannot close this project yet: {exc}", file=sys.stderr)
        return 1

    if not args.close:
        print(f"Ready to close {root.name}.")
        return 0

    title = f"{root.name} saved"
    body = "Closing this project workspace. Restart later from RESTART_HANDOFF.md."
    require_command(
        "herdr",
        "notification",
        "show",
        title,
        "--body",
        body,
        "--sound",
        "done",
    )
    require_command("herdr", "workspace", "close", workspace_id)
    print(f"Closed {pane.get('label', 'the project workspace')}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
