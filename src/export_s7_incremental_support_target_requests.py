#!/usr/bin/env python3
"""Export completion requests for genuinely new targets from hole-support transport."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import json
import sys

from probe_sponsor_pair_transport_frontier import (
    canonical_hash,
    pair_weight,
    parent_schedule,
    reconstruct_fourth_recursive,
    transport,
)
from probe_terminal_pair_payment_frontier_v2 import terminal_semantics

Pair = tuple[int, int]


def build_s7() -> set[int]:
    base = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}
    scales = (64, 256, 2048, 8192, 32768, 262144, 1048576)
    separations = (61, 303, 1597, 8195, 93476, 230164)
    state = {scales[0] + value for value in base}
    for index, separation in enumerate(separations):
        state = {
            scales[index + 1] + value + layer * separation
            for value in ({0} | state)
            for layer in range(3)
        }
    if (len(state), min(state), max(state)) != (9840, 1048576, 2021668):
        raise AssertionError("certified S7 reconstruction mismatch")
    return state


def completion_roots(pair: Pair, roots: set[int]) -> set[int]:
    left, right = pair
    gap = right - left
    candidates = {left - gap, right + gap}
    if gap % 2 == 0:
        candidates.add(left + gap // 2)
    return candidates & roots


def read_holes(path: Path) -> dict[int, tuple[tuple[int, ...], int]]:
    holes: dict[int, tuple[tuple[int, ...], int]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["status"] != "certified_S7_hole":
                continue
            completion = int(row["completion"])
            witness = tuple(int(row[f"p{index}"]) for index in range(4))
            missing = int(row["missing_index"])
            holes[completion] = witness, missing
    return holes


def canonical_pair(witness: tuple[int, ...], missing: int) -> Pair:
    for index in range(3):
        if index != missing and index + 1 != missing:
            return witness[index], witness[index + 1]
    raise AssertionError("hole witness has no adjacent support pair")


def main() -> int:
    if len(sys.argv) != 5:
        raise SystemExit(
            "usage: export_s7_incremental_support_target_requests.py "
            "TERMINAL_PAYMENT_JSON FIRST_CLASSIFICATION_TSV "
            "REQUESTS_TXT TARGETS_JSON"
        )
    payment_path = Path(sys.argv[1])
    classification_path = Path(sys.argv[2])
    requests_path = Path(sys.argv[3])
    targets_path = Path(sys.argv[4])
    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    holes = read_holes(classification_path)
    s7 = build_s7()
    target_rows = payment.get("target_rows")
    source_rows = payment.get("source_rows")
    if not isinstance(target_rows, list) or not isinstance(source_rows, list):
        raise AssertionError("terminal-payment payload lacks full rows")

    first_targets_by_completion: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in target_rows:
        if row["completion_status"] != "ambient_unresolved":
            continue
        target = tuple(int(value) for value in row["target"])
        if completion_roots(target, s7):
            continue
        completions = {
            int(record[2])
            for record in row["completion_records"]
            if record[3] == "ambient_unresolved"
        }
        if len(completions) != 1:
            raise AssertionError("one edge-unresolved target has several completions")
        completion = next(iter(completions))
        if completion in holes:
            first_targets_by_completion[completion].append(row)
    if set(first_targets_by_completion) != set(holes):
        raise AssertionError("first-layer certified-hole family is incomplete")

    first_support_pairs = {
        canonical_pair(*holes[completion]) for completion in holes
    }
    original_source_pairs = {
        tuple(int(value) for value in row["pair"]) for row in source_rows
    }
    new_supports = first_support_pairs - original_source_pairs

    parents = reconstruct_fourth_recursive()
    schedules = {parent.index: parent_schedule(parent) for parent in parents}
    new_activated: dict[Pair, int] = {}
    for pair in sorted(new_supports):
        owners = [
            parent_class
            for parent_class, schedule in schedules.items()
            if set(pair) <= schedule["roots"]
        ]
        if len(owners) > 1:
            raise AssertionError("new support pair belongs to several parents")
        if not owners:
            continue
        parent_class = owners[0]
        if set(pair) & schedules[parent_class]["sponsors"]:
            new_activated[pair] = parent_class

    new_rows: list[dict[str, object]] = []
    for pair, parent_class in sorted(new_activated.items()):
        schedule = schedules[parent_class]
        result = transport(pair, schedule)
        target: Pair = result["target"]  # type: ignore[assignment]
        semantics = terminal_semantics(target, result, schedule, s7)
        new_rows.append(
            {
                "source_pair": pair,
                "source_parent": parent_class,
                "source_weight": pair_weight(pair),
                "target": target,
                "target_weight": pair_weight(target),
                "terminal_class": result["terminal_class"],
                "path_length": len(result["path"]),
                "natural_completion": semantics["natural_completion"],
            }
        )

    grouped: dict[Pair, list[dict[str, object]]] = defaultdict(list)
    for row in new_rows:
        grouped[row["target"]].append(row)  # type: ignore[index]
    existing_targets = {
        tuple(int(value) for value in row["target"]) for row in target_rows
    }

    requests: set[int] = set()
    records: list[dict[str, object]] = []
    for target, members in sorted(grouped.items()):
        if target in existing_targets:
            continue
        edge_completions = tuple(sorted(completion_roots(target, s7)))
        natural_completions = tuple(
            sorted({int(row["natural_completion"]) for row in members})
        )
        status = "S7_edge_supported" if edge_completions else "completion_requested"
        if not edge_completions:
            requests.update(natural_completions)
        records.append(
            {
                "target": list(target),
                "target_weight": f"{pair_weight(target).numerator}/{pair_weight(target).denominator}",
                "source_count": len(members),
                "source_pairs": [list(row["source_pair"]) for row in members],
                "source_parents": sorted(
                    {int(row["source_parent"]) for row in members}
                ),
                "terminal_classes": sorted(
                    {str(row["terminal_class"]) for row in members}
                ),
                "status": status,
                "S7_edge_completions": list(edge_completions),
                "natural_completions": list(natural_completions),
            }
        )

    requests_path.write_text(
        "".join(f"{value}\n" for value in sorted(requests)),
        encoding="utf-8",
    )
    payload = {
        "schema": "s7_incremental_support_target_requests_v1",
        "generation_six_propagated": False,
        "counts": {
            "new_activated_support_pairs": len(new_activated),
            "transport_target_union": len(grouped),
            "targets_already_existing": len(set(grouped) & existing_targets),
            "incremental_targets": len(records),
            "S7_edge_supported_targets": sum(
                row["status"] == "S7_edge_supported" for row in records
            ),
            "completion_requested_targets": sum(
                row["status"] == "completion_requested" for row in records
            ),
            "distinct_completion_requests": len(requests),
        },
        "targets": records,
        "hashes": {
            "target_records_sha256": canonical_hash(records),
            "completion_requests_sha256": canonical_hash(sorted(requests)),
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    targets_path.write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
