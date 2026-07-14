#!/usr/bin/env python3
"""Reject unsafe deterministic-probe workflow patterns.

The linter is intentionally text based. It catches the exact failure mode that
masked probe diagnostics: staging a named optional path with ``git add -A``.
It also requires probe writers to use the shared recorder/staging path and the
repository-wide serialization group.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

WORKFLOW_DIR = Path(".github/workflows")
UNSAFE_STAGE = re.compile(r"\bgit\s+add\s+-A\s+(?:--\s+)?data/[^\s]+")
DIRECT_OPTIONAL_REDIRECT = re.compile(
    r">\s*data/[^\s]*(?:_probe\.json|_summary\.txt|_certificate[^\s]*\.txt)"
)
PROBE_WRITER_MARKERS = (
    "_probe.json",
    "_summary.txt",
    "_status.txt",
)
SAFE_RECORDER_MARKERS = (
    "reusable-python-probe-recorder.yml",
    "src/stage_optional_probe_outputs.sh",
    "src/commit_probe_outputs.sh",
)


def main() -> int:
    failures: list[str] = []
    for path in sorted(WORKFLOW_DIR.glob("*.y*ml")):
        text = path.read_text(encoding="utf-8")
        for match in UNSAFE_STAGE.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            failures.append(
                f"{path}:{line}: unsafe named optional staging: {match.group(0)!r}"
            )

        is_probe_writer = (
            "contents: write" in text
            and any(marker in text for marker in PROBE_WRITER_MARKERS)
        )
        if is_probe_writer:
            if "group: probe-result-writers-main" not in text:
                failures.append(
                    f"{path}: probe writer must use concurrency group "
                    "probe-result-writers-main"
                )
            if not any(marker in text for marker in SAFE_RECORDER_MARKERS):
                failures.append(
                    f"{path}: probe writer must use the shared hardened recorder"
                )
            for match in DIRECT_OPTIONAL_REDIRECT.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                failures.append(
                    f"{path}:{line}: deterministic output must be written "
                    f"atomically through a temporary file: {match.group(0)!r}"
                )

    if failures:
        print("probe workflow lint failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("probe workflow lint passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
