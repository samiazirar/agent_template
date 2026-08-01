#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FIELDS = (
    "PROJECT QUESTION",
    "MILESTONE RESULT",
    "GOAL SOURCE",
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
OPTIONAL_FIELDS = (
    "LUNA FAILURE",
    "HUMAN MODEL CHOICE",
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
        if match and match.group(1) in FIELDS + OPTIONAL_FIELDS:
            current = match.group(1)
            if current in values:
                raise ValueError(f"duplicate field: {current}")
            values[current] = [match.group(2).strip()]
        elif current and line.strip():
            values[current].append(line.strip())
    return {field: " ".join(parts).strip() for field, parts in values.items()}


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def validate(text: str, human_plan: str | None = None) -> list[str]:
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

    if human_plan is not None and normalize(values["GOAL SOURCE"]) not in normalize(human_plan):
        errors.append("GOAL SOURCE must be an exact sentence copied from HUMAN_PLAN.md")

    if len(values["CAUSAL LINK"].split()) < 6:
        errors.append("CAUSAL LINK is too short to explain why the task helps")

    if len(values["DISCONFIRMING RESULT"].split()) < 4:
        errors.append(
            "DISCONFIRMING RESULT must state evidence that would refute benefit"
        )

    luna_failure = values.get("LUNA FAILURE", "")
    if luna_failure and (
        not re.search(r"\b[0-9a-f]{8}-[0-9a-f-]{27,}\b", luna_failure, re.IGNORECASE)
        or len(luna_failure.split()) < 5
    ):
        errors.append("LUNA FAILURE must include the failed native session ID and concrete reason")

    human_choice = values.get("HUMAN MODEL CHOICE", "")
    if human_choice and len(human_choice.split()) < 4:
        errors.append("HUMAN MODEL CHOICE must record the explicit choice and selected model")

    return errors


def self_test() -> int:
    valid = """\
PROJECT QUESTION: Does measured depth improve robot planning?
MILESTONE RESULT: One resumed GPU rehearsal produces measured progress.
GOAL SOURCE: Resume the saved training run and measure whether it advances.
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
    human_plan = "# Goal\nResume the saved training run and measure whether it advances.\n"
    if validate(valid, human_plan):
        print(f"self-test valid card failed: {validate(valid, human_plan)}", file=sys.stderr)
        return 1
    if not validate(invalid):
        print("self-test invalid card unexpectedly passed", file=sys.stderr)
        return 1
    print("validate_task_card self-test: ok")
    return 0


def main() -> int:
    if sys.argv[1:] == ["--self-test"]:
        return self_test()
    parser = argparse.ArgumentParser()
    parser.add_argument("task_card")
    parser.add_argument("--human-plan")
    args = parser.parse_args()

    if args.task_card == "-":
        text = sys.stdin.read()
    else:
        text = Path(args.task_card).read_text(encoding="utf-8")

    human_plan = (
        Path(args.human_plan).read_text(encoding="utf-8")
        if args.human_plan
        else None
    )

    errors = validate(text, human_plan)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print("task card: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
