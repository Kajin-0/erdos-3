#!/usr/bin/env python3
"""Profile the completion-step light/heavy transfer on the exact S7 frontier."""
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
from verify_completion_step_fiber_light_heavy import is_four_ap_free

Pair = tuple[int, int]


def read_classification(
    path: Path,
) -> dict[int, dict[str, object]]:
    result: dict[int, dict[str, object]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            completion = int(row["completion"])
            if completion in result:
                raise AssertionError("duplicate completion classification")
            result[completion] = {
                "status": row["status"],
                "witness": tuple(int(row[f"p{index}"]) for index in range(4)),
                "missing_index": int(row["missing_index"]),
            }
    return result


def target_orientation(target: Pair, completion: int) -> int:
    left, right = target
    gap = right - left
    if completion == left - gap:
        return 1
    if completion == right + gap:
        return -1
    raise AssertionError("selected completion is not an endpoint extension")


def pair_weight(pair: Pair) -> Fraction:
    return Fraction(1, pair[1] - pair[0])


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_completion_step_light_heavy.py "
            "TERMINAL_PAYMENT_JSON CLASSIFICATION_TSV OUTPUT_JSON"
        )
    payment_path = Path(sys.argv[1])
    classification_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])

    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    classifications = read_classification(classification_path)
    s7 = build_s7()
    target_rows = payment.get("target_rows")
    source_rows = payment.get("source_rows")
    if not isinstance(target_rows, list) or not isinstance(source_rows, list):
        raise AssertionError("terminal-payment payload lacks full rows")

    original_source_pairs = {
        tuple(int(value) for value in row["pair"]) for row in source_rows
    }
    fibers: dict[tuple[Pair, int, int], set[int]] = defaultdict(set)
    assignment_rows: list[tuple[object, ...]] = []
    certified_target_mass = Fraction()
    certified_targets = 0

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
        if classification is None:
            raise AssertionError("selected completion was not classified")
        if classification["status"] != "certified_S7_hole":
            continue

        witness = classification["witness"]
        missing = int(classification["missing_index"])
        support = canonical_pair(witness, missing)
        orientation = target_orientation(target, completion)
        gap = target[1] - target[0]
        fibers[(support, completion, orientation)].add(gap)
        certified_targets += 1
        certified_target_mass += Fraction(1, gap)
        assignment_rows.append(
            (target, completion, orientation, support, gap)
        )

    by_support: dict[Pair, list[tuple[int, int, set[int]]]] = defaultdict(list)
    for (support, completion, orientation), steps in fibers.items():
        by_support[support].append((completion, orientation, steps))

    counts = Counter()
    mass_profile: dict[str, Fraction] = defaultdict(Fraction)
    multiplicity_profile = Counter()
    fiber_size_profile = Counter()
    shell_base_profile = Counter()
    shell_mass_profile: dict[int, Fraction] = defaultdict(Fraction)
    light_supports: set[Pair] = set()
    heavy_rows: list[tuple[object, ...]] = []
    light_rows: list[tuple[object, ...]] = []

    for support, support_fibers in sorted(by_support.items()):
        fiber_count = len(support_fibers)
        multiplicity_profile[fiber_count] += 1
        if fiber_count > 4:
            raise AssertionError("support has more than four oriented fibers")
        support_gap = support[1] - support[0]
        threshold = Fraction(1, fiber_count * support_gap)
        light_load = Fraction()

        for completion, orientation, steps in sorted(support_fibers):
            if not is_four_ap_free(steps):
                raise AssertionError("S7 completion-step fiber is not four-AP-free")
            mass = sum((Fraction(1, step) for step in steps), Fraction())
            fiber_size_profile[len(steps)] += 1
            has_far_step = any(step < support_gap for step in steps)
            orientation_name = "right_of_completion" if orientation == 1 else "left_of_completion"
            aspect_name = "far" if has_far_step else "near_only"

            if mass <= threshold:
                counts["light_fibers"] += 1
                counts[f"light_{orientation_name}"] += 1
                mass_profile["light_fiber_mass"] += mass
                mass_profile[f"light_{orientation_name}_mass"] += mass
                light_load += mass
                light_rows.append(
                    (
                        support,
                        completion,
                        orientation,
                        tuple(sorted(steps)),
                        fraction_text(mass),
                        fraction_text(threshold),
                    )
                )
                if has_far_step:
                    raise AssertionError("light fiber contains a far step")
            else:
                counts["heavy_fibers"] += 1
                counts[f"heavy_{orientation_name}"] += 1
                counts[f"heavy_{aspect_name}"] += 1
                mass_profile["heavy_fiber_mass"] += mass
                mass_profile[f"heavy_{orientation_name}_mass"] += mass
                mass_profile[f"heavy_{aspect_name}_mass"] += mass
                if mass <= Fraction(1, 4 * support_gap):
                    raise AssertionError("heavy fiber lacks quarter-share bound")
                shell_groups: dict[int, set[int]] = defaultdict(set)
                for step in steps:
                    shell_base = 1 << (step.bit_length() - 1)
                    if shell_base > 262144:
                        raise AssertionError("S7 heavy fiber failed N/4 descent")
                    shell_groups[shell_base].add(step)
                counts["heavy_resolved_shells"] += len(shell_groups)
                for shell_base, shell_steps in shell_groups.items():
                    shell_base_profile[shell_base] += 1
                    shell_mass_profile[shell_base] += sum(
                        (Fraction(1, step) for step in shell_steps), Fraction()
                    )
                heavy_rows.append(
                    (
                        support,
                        completion,
                        orientation,
                        tuple(sorted(steps)),
                        fraction_text(mass),
                        fraction_text(threshold),
                        tuple(sorted(shell_groups)),
                    )
                )

        if light_load:
            if light_load > Fraction(1, support_gap):
                raise AssertionError("light load exceeds support capacity")
            light_supports.add(support)

    if mass_profile["light_fiber_mass"] + mass_profile["heavy_fiber_mass"] != certified_target_mass:
        raise AssertionError("light/heavy mass partition failed")
    if sum((len(steps) for steps in fibers.values()), 0) != certified_targets:
        raise AssertionError("target token partition failed")

    existing_light_supports = light_supports & original_source_pairs
    new_light_supports = light_supports - original_source_pairs
    light_support_union = sum((pair_weight(pair) for pair in light_supports), Fraction())
    existing_light_union = sum(
        (pair_weight(pair) for pair in existing_light_supports), Fraction()
    )
    new_light_union = sum(
        (pair_weight(pair) for pair in new_light_supports), Fraction()
    )

    output = {
        "schema": "s7_completion_step_light_heavy_profile_v1",
        "scope": "edge-unresolved certified-hole targets on the refined R4_to_F5 frontier",
        "generation_six_propagated": False,
        "counts": {
            "certified_hole_targets": certified_targets,
            "oriented_completion_fibers": len(fibers),
            "canonical_support_pairs": len(by_support),
            "light_support_pairs": len(light_supports),
            "existing_light_support_pairs": len(existing_light_supports),
            "new_light_support_pairs": len(new_light_supports),
            "maximum_targets_per_fiber": max(fiber_size_profile, default=0),
            "maximum_fibers_per_support": max(multiplicity_profile, default=0),
            **dict(sorted(counts.items())),
        },
        "masses": {
            "certified_hole_target_mass": serialize_mass(certified_target_mass),
            **{
                name: serialize_mass(value)
                for name, value in sorted(mass_profile.items())
            },
            "light_support_union_mass": serialize_mass(light_support_union),
            "existing_light_support_union_mass": serialize_mass(existing_light_union),
            "new_light_support_union_mass": serialize_mass(new_light_union),
        },
        "fibers_per_support_profile": [
            {"fibers": value, "supports": multiplicity_profile[value]}
            for value in sorted(multiplicity_profile)
        ],
        "fiber_size_profile": [
            {"targets": value, "fibers": fiber_size_profile[value]}
            for value in sorted(fiber_size_profile)
        ],
        "heavy_shell_profile": [
            {
                "shell_base": shell_base,
                "shells": shell_base_profile[shell_base],
                "harmonic_mass": serialize_mass(shell_mass_profile[shell_base]),
            }
            for shell_base in sorted(shell_base_profile)
        ],
        "hashes": {
            "assignments": canonical_hash(sorted(assignment_rows)),
            "light_fibers": canonical_hash(sorted(light_rows)),
            "heavy_fibers": canonical_hash(sorted(heavy_rows)),
        },
        "checks": {
            "target_partition": sum((len(steps) for steps in fibers.values()), 0) == certified_targets,
            "mass_partition": mass_profile["light_fiber_mass"] + mass_profile["heavy_fiber_mass"] == certified_target_mass,
            "support_multiplicity_at_most_four": max(multiplicity_profile, default=0) <= 4,
            "heavy_shells_descend_to_N_over_4": max(shell_base_profile, default=0) <= 262144,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    output_path.write_text(json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
