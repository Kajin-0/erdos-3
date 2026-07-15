#!/usr/bin/env python3
"""Export distinct S7-external terminal completion requests from the v2 probe."""
from __future__ import annotations

from pathlib import Path
import json
import sys


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: export_s7_terminal_completion_requests.py INPUT_JSON OUTPUT_TXT")
    source = Path(sys.argv[1])
    target = Path(sys.argv[2])
    payload = json.loads(source.read_text(encoding="utf-8"))
    if payload["schema"] != "terminal_pair_payment_frontier_probe_v2":
        raise AssertionError("unexpected terminal-payment schema")
    rows = payload.get("target_rows")
    if not isinstance(rows, list):
        raise AssertionError("terminal-payment payload lacks target_rows; use --include-rows")

    completions: set[int] = set()
    for row in rows:
        if row["completion_status"] != "ambient_unresolved":
            continue
        records = [
            record
            for record in row["completion_records"]
            if record[3] == "ambient_unresolved"
        ]
        values = {int(record[2]) for record in records}
        if len(values) != 1:
            raise AssertionError("one unresolved target has multiple completion integers")
        completions.update(values)

    if not completions:
        raise AssertionError("no unresolved completion requests found")
    target.write_text("".join(f"{value}\n" for value in sorted(completions)), encoding="utf-8")
    print(f"distinct_completion_requests={len(completions)}")
    print(f"minimum_completion={min(completions)}")
    print(f"maximum_completion={max(completions)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
