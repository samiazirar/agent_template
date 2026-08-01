#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


FIELDS = (
    "SESSION NAME",
    "PROJECT GOAL",
    "WATCHED CONDITION",
    "SUCCESS EVENT",
    "FAILURE EVENT",
    "OWNER",
    "MODEL",
    "EFFORT",
    "EVENT DRIVEN",
    "POLL SECONDS",
    "MAXIMUM SILENCE",
    "RECOVERY ACTION",
    "TIMEOUT",
    "TERMINAL EVENT",
    "ONE WATCHER VERIFIED",
)


def parse(text: str) -> dict[str, str]:
    values: dict[str, list[str]] = {}
    current: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        match = re.match(r"^\s*([A-Z][A-Z ]+):\s*(.*)$", line)
        if match and match.group(1) in FIELDS:
            current = match.group(1)
            if current in values:
                raise ValueError(f"duplicate field: {current}")
            values[current] = [match.group(2).strip()]
        elif current and line.strip():
            values[current].append(line.strip())
    return {field: " ".join(parts).strip() for field, parts in values.items()}


def validate(text: str) -> list[str]:
    try:
        values = parse(text)
    except ValueError as exc:
        return [str(exc)]
    errors = [
        f"missing or empty field: {field}"
        for field in FIELDS
        if not values.get(field)
    ]
    if errors:
        return errors

    if not values["SESSION NAME"].startswith("Watcher · "):
        errors.append("SESSION NAME must start with 'Watcher · '")
    if len(values["SESSION NAME"].split()) < 4:
        errors.append("SESSION NAME must include a person and goal-derived task")
    model = values["MODEL"].lower()
    if model not in {"opencode/gemini-3.6-flash", "gpt-5.6-luna"}:
        errors.append(
            "MODEL must be opencode/gemini-3.6-flash or gpt-5.6-luna"
        )
    expected_effort = "none" if model == "opencode/gemini-3.6-flash" else "low"
    if values["EFFORT"].lower() != expected_effort:
        errors.append(f"EFFORT must be {expected_effort} for {model}")
    if values["ONE WATCHER VERIFIED"].lower() != "true":
        errors.append("ONE WATCHER VERIFIED must be true")

    event_driven = values["EVENT DRIVEN"].lower()
    if event_driven != "true":
        errors.append("EVENT DRIVEN must be true")
    try:
        poll_seconds = int(values["POLL SECONDS"])
        if poll_seconds != 0:
            errors.append("POLL SECONDS must be 0 for the event-driven service")
    except ValueError:
        errors.append("POLL SECONDS must be an integer")

    if len(values["WATCHED CONDITION"].split()) < 5:
        errors.append("WATCHED CONDITION is too short to identify one exact event")
    if len(values["SUCCESS EVENT"].split()) < 4:
        errors.append("SUCCESS EVENT is too short")
    if len(values["FAILURE EVENT"].split()) < 4:
        errors.append("FAILURE EVENT is too short")
    if len(values["MAXIMUM SILENCE"].split()) < 2:
        errors.append("MAXIMUM SILENCE must state one bounded duration")
    if len(values["RECOVERY ACTION"].split()) < 5:
        errors.append("RECOVERY ACTION must name the concrete action on silence")
    if len(values["TERMINAL EVENT"].split()) < 4:
        errors.append("TERMINAL EVENT is too short")

    for field, value in values.items():
        if re.search(r"\bw[0-9A-Za-z]+:p[0-9A-Za-z]+\b", value):
            errors.append(f"{field} exposes a raw pane identifier")
        if re.search(r"\b(?:NO_GO|GO|PASS|FAIL)-?\d+\b", value, re.IGNORECASE):
            errors.append(f"{field} contains opaque coordination shorthand")
    return errors


def self_test() -> int:
    valid = """\
SESSION NAME: Watcher · Wanda Training-Resume
PROJECT GOAL: Resume one saved training run and verify new training evidence.
WATCHED CONDITION: Worker completion, process state change, or due evidence check.
SUCCESS EVENT: The resumed run writes a newer checkpoint.
FAILURE EVENT: The process exits without a newer checkpoint.
OWNER: Orchestrator · Clara ContactFlow Results
MODEL: opencode/gemini-3.6-flash
EFFORT: none
EVENT DRIVEN: true
POLL SECONDS: 0
MAXIMUM SILENCE: 30 minutes
RECOVERY ACTION: Wake the owner to inspect the latest process state and choose repair or replacement.
TIMEOUT: 90 minutes
TERMINAL EVENT: Active project batch ends.
ONE WATCHER VERIFIED: true
"""
    invalid = valid.replace(
        "MODEL: opencode/gemini-3.6-flash", "MODEL: gpt-5.6-sol"
    )
    if validate(valid):
        print(f"self-test valid card failed: {validate(valid)}", file=sys.stderr)
        return 1
    if not validate(invalid):
        print("self-test invalid card unexpectedly passed", file=sys.stderr)
        return 1
    print("validate_watcher_card self-test: ok")
    return 0


def main() -> int:
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        return self_test()
    if len(sys.argv) != 2:
        print(
            "usage: validate_watcher_card.py WATCHER_CARD_FILE|-|--self-test",
            file=sys.stderr,
        )
        return 2
    text = (
        sys.stdin.read()
        if sys.argv[1] == "-"
        else Path(sys.argv[1]).read_text(encoding="utf-8")
    )
    errors = validate(text)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("watcher card: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
