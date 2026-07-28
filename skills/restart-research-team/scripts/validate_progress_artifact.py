#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from html import unescape
from pathlib import Path


START = "<!-- RESEARCH_PROGRESS_V1 START -->"
END = "<!-- RESEARCH_PROGRESS_V1 END -->"
REQUIRED = (
    "question",
    "current evidence",
    "changed since",
    "elapsed",
    "last verified evidence",
    "next observable",
    "external wait",
    "independent view",
    "work meter",
    "concrete example",
)


def visible_text(fragment: str) -> str:
    fragment = re.sub(r"<script\b.*?</script>", " ", fragment,
                      flags=re.IGNORECASE | re.DOTALL)
    fragment = re.sub(r"<style\b.*?</style>", " ", fragment,
                      flags=re.IGNORECASE | re.DOTALL)
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def validate(text: str) -> list[str]:
    errors: list[str] = []
    if text.count(START) != 1 or text.count(END) != 1:
        return ["artifact must contain exactly one progress marker pair"]
    block = text.split(START, 1)[1].split(END, 1)[0]
    plain = visible_text(block)
    lowered = plain.lower()
    for phrase in REQUIRED:
        if phrase not in lowered:
            errors.append(f"progress view lacks: {phrase}")
    if re.search(r"\bw[0-9A-Za-z]+:p[0-9A-Za-z]+\b", plain):
        errors.append("progress view exposes a raw pane identifier")
    if re.search(r"\b(?:NO_GO|GO|PASS|FAIL)-?\d+\b", plain, re.IGNORECASE):
        errors.append("progress view exposes opaque coordination shorthand")
    if re.search(r"\b(?:gate|authority|blocker)\b", plain, re.IGNORECASE):
        errors.append("progress view uses process vocabulary instead of task meaning")
    if len(plain.split()) > 900:
        errors.append("progress view exceeds 900 words")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_progress_artifact.py ARTIFACT_HTML", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    errors = validate(path.read_text(encoding="utf-8"))
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"progress artifact: valid ({path})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
