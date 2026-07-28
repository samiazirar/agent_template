#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


FIELDS = (
    "SESSION NAME",
    "MODEL",
    "EFFORT",
    "CHECKED GOAL",
    "STARTED AT",
    "CHECKED AT",
    "ELAPSED MINUTES",
    "STARTING EVIDENCE",
    "NEW EVIDENCE",
    "REMAINING DONE CHECK",
    "TRAJECTORY",
    "NEXT USEFUL ACTION",
    "NONBLOCKING",
)
TRAJECTORIES = {
    "advancing",
    "complete",
    "no observed advance",
    "diverging",
}
OPAQUE = (
    re.compile(r"\bw[0-9A-Za-z]+:p[0-9A-Za-z]+\b"),
    re.compile(r"\b(?:NO_GO|GO|PASS|FAIL)-?\d+\b", re.IGNORECASE),
    re.compile(r"\b(?:phase|stage|wave)\s*[A-Z]?\d+(?::[A-Z]?\d+)*\b",
               re.IGNORECASE),
)
ACTIVITY_ONLY = re.compile(
    r"^(?:working|still working|in progress|commands ran|tokens spent|"
    r"files? touched|lines? changed|pane open|elapsed|none yet)\.?$",
    re.IGNORECASE,
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

    if not re.fullmatch(r"\d+(?:\.\d+)?", values["ELAPSED MINUTES"]):
        errors.append("ELAPSED MINUTES must be a non-negative number")
    if values["TRAJECTORY"].lower() not in TRAJECTORIES:
        errors.append(
            "TRAJECTORY must be advancing, complete, no observed advance, "
            "or diverging"
        )
    if values["NONBLOCKING"].lower() != "true":
        errors.append("NONBLOCKING must be true")
    if values["MODEL"].lower() != "gpt-5.6-terra":
        errors.append("MODEL must be gpt-5.6-terra")
    if values["EFFORT"].lower() != "medium":
        errors.append("EFFORT must be medium")
    if len(values["CHECKED GOAL"].split()) < 4:
        errors.append("CHECKED GOAL is too short to state an observable goal")
    if ACTIVITY_ONLY.fullmatch(values["NEW EVIDENCE"]):
        errors.append("NEW EVIDENCE describes activity, not task progress")
    if (
        values["TRAJECTORY"].lower() in {"advancing", "complete"}
        and len(values["NEW EVIDENCE"].split()) < 5
    ):
        errors.append("advancing/complete requires a concrete evidence delta")
    if (
        values["TRAJECTORY"].lower() == "no observed advance"
        and values["NEW EVIDENCE"].lower() not in {
            "no task-relevant observable changed.",
            "no task-relevant observable changed",
        }
    ):
        errors.append(
            "NO OBSERVED ADVANCE must state that no task-relevant observable changed"
        )
    for field in FIELDS:
        if any(pattern.search(values[field]) for pattern in OPAQUE):
            errors.append(f"{field} contains opaque coordination shorthand")
    if re.search(r"\b\d+(?:\.\d+)?\s*%", values["TRAJECTORY"]):
        errors.append("TRAJECTORY must not use an invented completion percentage")
    return errors


def self_test() -> int:
    valid = """\
SESSION NAME: Progress · Petra Resume-Evidence
MODEL: gpt-5.6-terra
EFFORT: medium
CHECKED GOAL: Resume one saved training run and verify one advancing step.
STARTED AT: 2026-07-23T10:00:00+02:00
CHECKED AT: 2026-07-23T10:25:00+02:00
ELAPSED MINUTES: 25
STARTING EVIDENCE: A saved checkpoint and its previous final step.
NEW EVIDENCE: The resumed log records checkpoint reload and one higher optimizer step.
REMAINING DONE CHECK: Confirm optimizer continuity and preserve the new checkpoint.
TRAJECTORY: advancing
NEXT USEFUL ACTION: Run the continuity assertion and save the resumed checkpoint.
NONBLOCKING: true
"""
    invalid = valid.replace(
        "The resumed log records checkpoint reload and one higher optimizer step.",
        "Still working.",
    )
    if validate(valid):
        print(f"self-test valid report failed: {validate(valid)}", file=sys.stderr)
        return 1
    if not validate(invalid):
        print("self-test invalid report unexpectedly passed", file=sys.stderr)
        return 1
    print("validate_progress_check self-test: ok")
    return 0


def main() -> int:
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        return self_test()
    if len(sys.argv) != 2:
        print(
            "usage: validate_progress_check.py REPORT_FILE|-|--self-test",
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
    print("progress check: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
