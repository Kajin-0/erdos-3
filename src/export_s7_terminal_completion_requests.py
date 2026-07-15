#!/usr/bin/env python3
"""Export terminal completion requests not already supported by an S7 AP edge."""
from __future__ import annotations

from pathlib import Path
import json
import sys


def build_s7() -> set[int]:
    base = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}
    scales = (64, 256, 2048, 8192, 32768, 262144, 1048576)
    separations = (61, 303, 1597, 8195, 93476, 230164)
    state = {scales[0] + value for value in base}
    for index, separation in enumerate(separations):
        anchor = {0} | state
        raw = {
            value + layer * separation
            for value in anchor
            for layer in range(3)
        }
        state = {scales[index + 1] + value for value in raw}
    if (len(state), min(state), max(state)) != (9840, 1048576, 2021668):
        raise AssertionError("certified S7 reconstruction mismatch")
    return state


def completion_roots(pair: tuple[int, int], roots: set[int]) -> set[int]:
    left, right = pair
    gap = right - left
    candidates = {left - gap, right + gap}
    if gap % 2 == 0:
        candidates.add(left + gap // 2)
    return candidates & roots


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit(
            "usage: export_s7_terminal_completion_requests.py INPUT_JSON OUTPUT_TXT"
        )
    source = Path(sys.argv[1])
    target = Path(sys.argv[2])
    payload = json.loads(source.read_text(encoding="utf-8"))
    if payload["schema"] != "terminal_pair_payment_frontier_probe_v2":
        raise AssertionError("unexpected terminal-payment schema")
    rows = payload.get("target_rows")
    if not isinstance(rows, list):
        raise AssertionError("terminal-payment payload lacks target_rows; use --include-rows")

    s7 = build_s7()
    completions: set[int] = set()
    skipped_edge_targets = 0
    skipped_edge_mass_numerator = 0
    for row in rows:
        if row["completion_status"] != "ambient_unresolved":
            continue
        pair = tuple(int(value) for value in row["target"])
        if completion_roots(pair, s7):
            skipped_edge_targets += 1
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
        raise AssertionError("no edge-unresolved completion requests found")
    target.write_text(
        "".join(f"{value}\n" for value in sorted(completions)),
        encoding="utf-8",
    )
    print(f"S7_edge_supported_targets_skipped={skipped_edge_targets}")
    print(f"distinct_completion_requests={len(completions)}")
    print(f"minimum_completion={min(completions)}")
    print(f"maximum_completion={max(completions)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
