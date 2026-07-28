#!/usr/bin/env python3
"""Render and validate the canonical communication contract for a Herdr role."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


CONTRACTS = {
    "human-orchestrator": (
        "ROLE: Human Orchestrator",
        "RECEIVES FROM: Human; Operations",
        "SENDS TO: Human; Operations",
        "OWNS: Goal meaning; human questions and decisions; human-language explanation; Human Plan meaning",
        "MUST NOT: Contact technical roles directly; manage workers or sessions; execute project work; edit files; use Git; control Herdr",
        "ROUTING RULE: Send every technical request to Operations. Ask the Human only for meaning or a decision, then return the answer to Operations.",
    ),
    "operations": (
        "ROLE: Operations",
        "RECEIVES FROM: Human Orchestrator; workers; suborchestrators; plan writers; advisors; researchers; verifiers",
        "SENDS TO: Human Orchestrator; assigned technical roles",
        "OWNS: Technical state; decomposition; execution; role lifecycle; integration; synchronization",
        "MUST NOT: Use the Human Orchestrator as an execution manager; send routine technical chatter to the human side; speak to the Human except an immediate safety emergency",
        "ROUTING RULE: Be the sole normal bridge between the Human Orchestrator and every technical role.",
    ),
    "human-plan-writer": (
        "ROLE: Human Plan Writer",
        "RECEIVES FROM: Operations",
        "SENDS TO: Operations",
        "OWNS: One accepted update to HUMAN_PLAN.md",
        "MUST NOT: Edit any other file; contact the Human or Human Orchestrator; manage work; broaden the accepted meaning",
        "ROUTING RULE: Receive the accepted brief from Operations, return one plan-only commit to Operations, then stop.",
    ),
    "worker": (
        "ROLE: Worker",
        "RECEIVES FROM: Operations or one owning suborchestrator",
        "SENDS TO: The same assigning role",
        "OWNS: One concrete subtask; one branch; one worktree; one result",
        "MUST NOT: Contact the Human or Human Orchestrator; edit HUMAN_PLAN.md; launch agents; broaden scope; perform unrelated work",
        "ROUTING RULE: Report evidence and the completion envelope only to the assigning role, then stop.",
    ),
    "suborchestrator": (
        "ROLE: Suborchestrator",
        "RECEIVES FROM: Operations",
        "SENDS TO: Operations; its assigned workers",
        "OWNS: One independent multi-step workstream with at least three productive subtasks",
        "MUST NOT: Contact the Human or Human Orchestrator; create another suborchestrator; manage work outside its workstream",
        "ROUTING RULE: Launch one worker per subtask, integrate the workstream for Operations, report to Operations, then stop.",
    ),
    "strategic-advisor": (
        "ROLE: Strategic Advisor",
        "RECEIVES FROM: Operations",
        "SENDS TO: Operations",
        "OWNS: One bounded consequential question",
        "MUST NOT: Contact the Human or Human Orchestrator; implement; manage; inspect broadly; create agents",
        "ROUTING RULE: Return one yes-or-no answer or one concrete recommendation to Operations, then stop.",
    ),
    "research-lead": (
        "ROLE: Research Lead",
        "RECEIVES FROM: Operations or Architect",
        "SENDS TO: The same assigning role; assigned research observers",
        "OWNS: One bounded evidence question and synthesis",
        "MUST NOT: Implement findings; edit project code; contact the Human directly; broaden the evidence search",
        "ROUTING RULE: Use read-only observers only when assigned, synthesize evidence for the assigning role, then stop.",
    ),
    "research-observer": (
        "ROLE: Research Observer",
        "RECEIVES FROM: One research lead",
        "SENDS TO: The same research lead",
        "OWNS: One bounded read-only evidence task",
        "MUST NOT: Implement; edit; commit; push; contact other roles; broaden the search",
        "ROUTING RULE: Return evidence only to the assigning research lead, then stop.",
    ),
    "verifier": (
        "ROLE: Verifier",
        "RECEIVES FROM: Operations or trusted event service",
        "SENDS TO: Operations",
        "OWNS: One bounded unusual-event check",
        "MUST NOT: Contact the Human or Human Orchestrator; edit project code; manage work; review unrelated evidence",
        "ROUTING RULE: Return one next action, one human question, or no issue to Operations, then stop.",
    ),
}


def render(role: str) -> str:
    return "\n".join(("ROLE CONTRACT", *CONTRACTS[role], "END ROLE CONTRACT"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("role", choices=sorted(CONTRACTS))
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--print", action="store_true", dest="print_contract")
    action.add_argument("--check", metavar="PATH", help="Prompt file, or - for stdin")
    args = parser.parse_args()

    contract = render(args.role)
    if args.print_contract:
        print(contract)
        return 0

    text = sys.stdin.read() if args.check == "-" else Path(args.check).read_text()
    missing = [line for line in contract.splitlines() if line not in text]
    if missing:
        print("Role card is invalid; missing canonical lines:", file=sys.stderr)
        for line in missing:
            print(f"- {line}", file=sys.stderr)
        return 1

    print(f"Role card valid: {args.role}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
