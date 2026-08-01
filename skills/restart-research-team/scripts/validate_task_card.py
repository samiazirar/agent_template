#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


FIELDS = (
    "PROJECT QUESTION",
    "MILESTONE RESULT",
    "OUTCOME CLASS",
    "MODEL",
    "TASK",
    "CURRENT STATE",
    "EXPECTED STATE",
    "CAUSAL LINK",
    "STARTING EVIDENCE",
    "DELIVERABLE",
    "DONE CHECK",
    "DISCONFIRMING RESULT",
)
OUTCOME_CLASSES = {
    "build",
    "run",
    "measure",
    "evaluate",
    "integrate",
    "control",
}
OPAQUE_PATTERNS = (
    re.compile(r"\bw[0-9A-Za-z]+:p[0-9A-Za-z]+\b"),
    re.compile(r"\b(?:NO_GO|GO|PASS|FAIL)-?\d+\b", re.IGNORECASE),
    re.compile(r"\b(?:phase|stage|wave)\s*[A-Z]?\d+(?::[A-Z]?\d+)*\b",
               re.IGNORECASE),
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
    errors: list[str] = []
    try:
        values = parse(text)
    except ValueError as exc:
        return [str(exc)]

    for field in FIELDS:
        if not values.get(field):
            errors.append(f"missing or empty field: {field}")

    if errors:
        return errors

    outcome_class = values["OUTCOME CLASS"].lower()
    if outcome_class not in OUTCOME_CLASSES:
        errors.append(
            "OUTCOME CLASS must be one of: "
            + ", ".join(sorted(OUTCOME_CLASSES))
        )

    model = values["MODEL"].lower()
    if len(values["MODEL"].split()) < 2:
        errors.append("MODEL must name the selected model and effort or route")
    if "luna low" in model and outcome_class in {"build", "run", "integrate"}:
        errors.append("Luna low is support-only; coding and execution use Luna max")

    current = re.sub(r"\s+", " ", values["CURRENT STATE"].lower()).strip()
    expected = re.sub(r"\s+", " ", values["EXPECTED STATE"].lower()).strip()
    if current == expected:
        errors.append("CURRENT STATE and EXPECTED STATE are identical")

    for field in ("PROJECT QUESTION", "MILESTONE RESULT", "TASK",
                  "CURRENT STATE", "EXPECTED STATE", "CAUSAL LINK"):
        for pattern in OPAQUE_PATTERNS:
            if pattern.search(values[field]):
                errors.append(f"{field} contains opaque coordination shorthand")
                break

    if not values["PROJECT QUESTION"].rstrip().endswith("?"):
        errors.append("PROJECT QUESTION must be written as a question")

    if len(values["CAUSAL LINK"].split()) < 6:
        errors.append("CAUSAL LINK is too short to explain why the task helps")

    if len(values["DISCONFIRMING RESULT"].split()) < 4:
        errors.append(
            "DISCONFIRMING RESULT must state evidence that would refute benefit"
        )

    return errors


def self_test() -> int:
    valid = """\
PROJECT QUESTION: Does measured depth improve robot planning?
MILESTONE RESULT: One resumed GPU rehearsal produces measured progress.
OUTCOME CLASS: run
MODEL: Native Codex GPT-5.6 Sol medium
TASK: Resume one short training run from its saved checkpoint.
CURRENT STATE: The program has no verified resumed GPU step.
EXPECTED STATE: The program advances at least one step after checkpoint reload.
CAUSAL LINK: Reloading and advancing exercises the exact state needed by production training.
STARTING EVIDENCE: A saved checkpoint and its previous training log.
DELIVERABLE: A resumed checkpoint plus the measured training log.
DONE CHECK: The step increases and optimizer state remains continuous.
DISCONFIRMING RESULT: Reload fails or the step does not advance.
"""
    invalid = valid.replace(
        "EXPECTED STATE: The program advances at least one step after checkpoint reload.",
        "EXPECTED STATE: The program has no verified resumed GPU step.",
    )
    if validate(valid):
        print(f"self-test valid card failed: {validate(valid)}", file=sys.stderr)
        return 1
    if not validate(invalid):
        print("self-test invalid card unexpectedly passed", file=sys.stderr)
        return 1
    print("validate_task_card self-test: ok")
    return 0


def main() -> int:
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        return self_test()
    if len(sys.argv) != 2:
        print(
            "usage: validate_task_card.py TASK_CARD_FILE|-|--self-test",
            file=sys.stderr,
        )
        return 2

    if sys.argv[1] == "-":
        text = sys.stdin.read()
    else:
        text = Path(sys.argv[1]).read_text(encoding="utf-8")

    errors = validate(text)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print("task card: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
