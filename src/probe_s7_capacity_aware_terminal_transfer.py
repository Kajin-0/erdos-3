#!/usr/bin/env python3
"""Profile the collision-sound capacity-aware terminal transfer on S7."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import csv
import hashlib
import json
import sys

from probe_s7_hole_support_closure import build_s7, canonical_pair, completion_roots
from probe_sponsor_pair_transport_frontier import canonical_hash, serialize_mass

Pair = tuple[int, int]


def read_classification(path: Path) -> dict[int, dict[str, object]]:
    result: dict[int, dict[str, object]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            completion = int(row["completion"])
            result[completion] = {
                "status": row["status"],
                "witness": tuple(int(row[f"p{index}"]) for index in range(4)),
                "missing_index": int(row["missing_index"]),
            }
    return result


def pair_weight(pair: Pair) -> Fraction:
    return Fraction(1, pair[1] - pair[0])


def target_orientation(target: Pair, completion: int) -> int:
    left, right = target
    gap = right - left
    if completion == left - gap:
        return 1
    if completion == right + gap:
        return -1
    raise AssertionError("selected completion is not an endpoint extension")


def harmonic(values: set[int] | tuple[int, ...]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction())


def contains_three_ap(values: tuple[int, ...]) -> bool:
    lookup = set(values)
    for index, left in enumerate(values):
        for right in values[index + 1 :]:
            if (left + right) % 2 == 0 and (left + right) // 2 in lookup:
                return True
    return False


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_capacity_aware_terminal_transfer.py "
            "TERMINAL_PAYMENT_JSON CLASSIFICATION_TSV OUTPUT_JSON"
        )

    payment_path = Path(sys.argv[1])
    classification_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])
    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    classifications = read_classification(classification_path)
    target_rows = payment.get("target_rows")
    if not isinstance(target_rows, list):
        raise AssertionError("terminal-payment payload lacks target rows")
    s7 = build_s7()

    collision_sources: set[Pair] = set()
    for row in target_rows:
        first = tuple(int(value) for value in row["first_source_pair"])
        for parent_class, pair_values, _weight in row["source_pairs"]:
            _ = parent_class
            pair = tuple(int(value) for value in pair_values)
            if pair != first:
                collision_sources.add(pair)

    collision_mass = sum((pair_weight(pair) for pair in collision_sources), Fraction())
    recorded_collision = Fraction(payment["masses"]["source_weighted_collision"]["fraction"])
    if collision_mass != recorded_collision:
        raise AssertionError("collision source pair union changed")

    fibers: dict[tuple[Pair, int, int], set[int]] = defaultdict(set)
    certified_target_mass = Fraction()
    certified_target_count = 0
    assignment_rows: list[tuple[object, ...]] = []
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
            raise AssertionError("edge-unresolved target lacks one selected completion")
        completion = next(iter(completions))
        classification = classifications.get(completion)
        if classification is None or classification["status"] != "certified_S7_hole":
            continue
        support = canonical_pair(
            classification["witness"],  # type: ignore[arg-type]
            int(classification["missing_index"]),
        )
        orientation = target_orientation(target, completion)
        gap = target[1] - target[0]
        fibers[(support, completion, orientation)].add(gap)
        certified_target_count += 1
        certified_target_mass += Fraction(1, gap)
        assignment_rows.append((target, completion, orientation, support, gap))

    by_support: dict[Pair, list[tuple[int, int, set[int]]]] = defaultdict(list)
    for (support, completion, orientation), steps in fibers.items():
        by_support[support].append((completion, orientation, steps))

    reserved_supports = set(by_support) & collision_sources
    light_supports: set[Pair] = set()
    light_rows: list[tuple[object, ...]] = []
    heavy_rows: list[tuple[object, ...]] = []
    light_mass = Fraction()
    heavy_mass = Fraction()
    reserved_heavy_mass = Fraction()
    counts = Counter()
    terminal_shell_mass = Fraction()
    recursive_shell_mass = Fraction()
    terminal_shells = 0
    recursive_shells = 0
    shell_size_profile = Counter()

    for support, rows in sorted(by_support.items()):
        multiplicity = len(rows)
        reserved = support in collision_sources
        threshold = (
            Fraction()
            if reserved
            else Fraction(1, multiplicity * (support[1] - support[0]))
        )
        if reserved:
            counts["reserved_supports"] += 1

        for completion, orientation, steps in sorted(rows):
            mass = harmonic(steps)
            if mass <= threshold:
                if reserved:
                    raise AssertionError("reserved support produced a light fiber")
                counts["light_fibers"] += 1
                light_mass += mass
                light_supports.add(support)
                light_rows.append(
                    (
                        support,
                        completion,
                        orientation,
                        tuple(sorted(steps)),
                        f"{mass.numerator}/{mass.denominator}",
                        f"{threshold.numerator}/{threshold.denominator}",
                    )
                )
                continue

            counts["heavy_fibers"] += 1
            heavy_mass += mass
            if reserved:
                counts["reserved_heavy_fibers"] += 1
                reserved_heavy_mass += mass

            shells: dict[int, list[int]] = defaultdict(list)
            for step in steps:
                shell_base = 1 << (step.bit_length() - 1)
                shells[shell_base].append(step)
            for shell_base, values in sorted(shells.items()):
                state = tuple(sorted(values))
                shell_size_profile[len(state)] += 1
                shell_mass = harmonic(state)
                recursive = contains_three_ap(state)
                if recursive:
                    recursive_shells += 1
                    recursive_shell_mass += shell_mass
                else:
                    terminal_shells += 1
                    terminal_shell_mass += shell_mass
                heavy_rows.append(
                    (
                        support,
                        completion,
                        orientation,
                        shell_base,
                        state,
                        recursive,
                        f"{shell_mass.numerator}/{shell_mass.denominator}",
                    )
                )

    if light_supports & collision_sources:
        raise AssertionError("light and collision pair outputs overlap")
    if light_mass + heavy_mass != certified_target_mass:
        raise AssertionError("capacity-aware light/heavy mass partition failed")
    if terminal_shell_mass + recursive_shell_mass != heavy_mass:
        raise AssertionError("capacity-aware terminal/recursive partition failed")

    light_support_mass = sum((pair_weight(pair) for pair in light_supports), Fraction())
    outgoing_pairs = collision_sources | light_supports
    outgoing_pair_mass = sum((pair_weight(pair) for pair in outgoing_pairs), Fraction())
    if outgoing_pair_mass != collision_mass + light_support_mass:
        raise AssertionError("disjoint outgoing pair identity failed")
    if light_mass > light_support_mass:
        raise AssertionError("light load exceeds unreserved support capacity")

    output = {
        "schema": "s7_capacity_aware_terminal_transfer_v1",
        "scope": "edge-unresolved certified-hole targets on the refined R4_to_F5 S7 frontier",
        "generation_six_propagated": False,
        "counts": {
            "collision_source_pairs": len(collision_sources),
            "certified_hole_targets": certified_target_count,
            "oriented_completion_fibers": len(fibers),
            "canonical_support_pairs": len(by_support),
            "reserved_canonical_supports": len(reserved_supports),
            "light_support_pairs": len(light_supports),
            "outgoing_pair_union": len(outgoing_pairs),
            "terminal_heavy_shells": terminal_shells,
            "recursive_heavy_shells": recursive_shells,
            **dict(sorted(counts.items())),
        },
        "masses": {
            "collision_source_pair_mass": serialize_mass(collision_mass),
            "certified_hole_target_mass": serialize_mass(certified_target_mass),
            "light_fiber_mass": serialize_mass(light_mass),
            "heavy_fiber_mass": serialize_mass(heavy_mass),
            "reserved_heavy_fiber_mass": serialize_mass(reserved_heavy_mass),
            "light_support_pair_mass": serialize_mass(light_support_mass),
            "outgoing_pair_union_mass": serialize_mass(outgoing_pair_mass),
            "terminal_heavy_shell_mass": serialize_mass(terminal_shell_mass),
            "recursive_heavy_shell_mass": serialize_mass(recursive_shell_mass),
        },
        "shell_size_profile": [
            {"points": size, "shells": shell_size_profile[size]}
            for size in sorted(shell_size_profile)
        ],
        "hashes": {
            "collision_sources": canonical_hash(sorted(collision_sources)),
            "target_assignments": canonical_hash(sorted(assignment_rows)),
            "light_fibers": canonical_hash(sorted(light_rows)),
            "heavy_shells": canonical_hash(sorted(heavy_rows)),
            "outgoing_pair_union": canonical_hash(sorted(outgoing_pairs)),
        },
        "checks": {
            "collision_mass_matches_source_weighted_row": collision_mass == recorded_collision,
            "light_collision_disjoint": not (light_supports & collision_sources),
            "light_heavy_mass_partition": light_mass + heavy_mass == certified_target_mass,
            "terminal_recursive_mass_partition": terminal_shell_mass + recursive_shell_mass == heavy_mass,
            "outgoing_pair_disjoint_union": outgoing_pair_mass == collision_mass + light_support_mass,
            "light_load_paid_by_support_union": light_mass <= light_support_mass,
            "all_capacity_aware_heavy_shells_terminal": recursive_shells == 0,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    output_path.write_text(json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
