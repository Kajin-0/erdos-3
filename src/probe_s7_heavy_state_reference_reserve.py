#!/usr/bin/env python3
"""Profile repeated heavy completion-step states and reference reserves on S7."""
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
StateKey = tuple[int, tuple[int, ...], int]


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


def target_orientation(target: Pair, completion: int) -> int:
    left, right = target
    gap = right - left
    if completion == left - gap:
        return 1
    if completion == right + gap:
        return -1
    raise AssertionError("selected completion is not an endpoint extension")


def harmonic(values: tuple[int, ...] | set[int]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction())


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def dyadic_band(numerator: int, denominator: int) -> int:
    if numerator <= 0 or denominator <= 0:
        raise ValueError("aspect band requires positive arguments")
    if numerator >= denominator:
        quotient = numerator // denominator
        band = quotient.bit_length() - 1
        while (1 << (band + 1)) * denominator <= numerator:
            band += 1
        return band
    band = -1
    while numerator * (1 << (-band)) < denominator:
        band -= 1
    return band


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_heavy_state_reference_reserve.py "
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
    parent_scale = 1_048_576

    fibers: dict[tuple[Pair, int, int], set[int]] = defaultdict(set)
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
            raise AssertionError("edge-unresolved target lacks one completion")
        completion = next(iter(completions))
        classification = classifications.get(completion)
        if classification is None or classification["status"] != "certified_S7_hole":
            continue
        support = canonical_pair(
            classification["witness"],  # type: ignore[arg-type]
            int(classification["missing_index"]),
        )
        orientation = target_orientation(target, completion)
        fibers[(support, completion, orientation)].add(target[1] - target[0])

    by_support: dict[Pair, list[tuple[int, int, set[int]]]] = defaultdict(list)
    for (support, completion, orientation), steps in fibers.items():
        by_support[support].append((completion, orientation, steps))

    heavy_occurrences: list[dict[str, object]] = []
    for support, rows in sorted(by_support.items()):
        multiplicity = len(rows)
        threshold = Fraction(1, multiplicity * (support[1] - support[0]))
        for completion, orientation, steps in sorted(rows):
            mass = harmonic(steps)
            if mass <= threshold:
                continue
            shells: dict[int, list[int]] = defaultdict(list)
            for step in steps:
                shell_base = 1 << (step.bit_length() - 1)
                shells[shell_base].append(step)
            for shell_base, values in sorted(shells.items()):
                state = tuple(sorted(values))
                if not is_four_ap_free(set(state)):
                    raise AssertionError("resolved heavy state is not four-AP-free")
                heavy_occurrences.append(
                    {
                        "shell_base": shell_base,
                        "state": state,
                        "orientation": orientation,
                        "completion": completion,
                        "support": support,
                        "mass": harmonic(state),
                    }
                )

    by_state: dict[tuple[int, tuple[int, ...]], list[dict[str, object]]] = defaultdict(list)
    by_oriented_state: dict[StateKey, list[dict[str, object]]] = defaultdict(list)
    for row in heavy_occurrences:
        identity = (int(row["shell_base"]), tuple(row["state"]))
        oriented = (identity[0], identity[1], int(row["orientation"]))
        by_state[identity].append(row)
        by_oriented_state[oriented].append(row)

    occurrence_mass = sum((row["mass"] for row in heavy_occurrences), Fraction())
    state_union_mass = sum(
        (harmonic(state) for _shell, state in by_state), Fraction()
    )
    collision_mass = occurrence_mass - state_union_mass
    multiplicity_profile = Counter(len(rows) for rows in by_state.values())

    repeated_rows: list[dict[str, object]] = []
    reference_shell_occurrences: list[tuple[int, tuple[int, ...], Fraction, StateKey]] = []
    aspect_mass: dict[int, Fraction] = defaultdict(Fraction)
    aspect_cells = Counter()
    reference_reserve_occurrence_mass = Fraction()
    reference_family_count = 0
    repeated_oriented_collision_mass = Fraction()
    maximum_reference_diameter = 0
    maximum_reference_shell_base = 0

    for key, rows in sorted(by_oriented_state.items()):
        shell_base, state, orientation = key
        completions = sorted(int(row["completion"]) for row in rows)
        if len(completions) <= 1:
            continue
        if len(completions) != len(set(completions)):
            raise AssertionError("one oriented state repeats at one completion")
        reference_family_count += 1
        base = completions[0]
        differences = tuple(completion - base for completion in completions[1:])
        if not is_four_ap_free(set(completions)):
            raise AssertionError("completion reference set is not four-AP-free")
        if not is_four_ap_free(set(differences)):
            raise AssertionError("reference difference reserve is not four-AP-free")

        minimum_step = min(state)
        maximum_step = max(state)
        diameter_bound = parent_scale - 2 * maximum_step + minimum_step
        if max(differences) >= diameter_bound:
            raise AssertionError("reference diameter bound failed")
        maximum_reference_diameter = max(maximum_reference_diameter, max(differences))

        state_mass = harmonic(state)
        collision = (len(completions) - 1) * state_mass
        repeated_oriented_collision_mass += collision
        reserve_mass = harmonic(differences)
        reference_reserve_occurrence_mass += reserve_mass

        shell_groups: dict[int, list[int]] = defaultdict(list)
        for difference in differences:
            reference_shell = 1 << (difference.bit_length() - 1)
            if reference_shell > parent_scale // 2:
                raise AssertionError("reference reserve failed parent-scale descent")
            maximum_reference_shell_base = max(maximum_reference_shell_base, reference_shell)
            shell_groups[reference_shell].append(difference)
            for step in state:
                band = dyadic_band(difference, step)
                aspect_mass[band] += Fraction(1, step)
                aspect_cells[band] += 1

        for reference_shell, values in sorted(shell_groups.items()):
            reserve_state = tuple(sorted(values))
            reference_shell_occurrences.append(
                (
                    reference_shell,
                    reserve_state,
                    harmonic(reserve_state),
                    key,
                )
            )

        repeated_rows.append(
            {
                "step_shell": shell_base,
                "state": state,
                "orientation": orientation,
                "references": tuple(completions),
                "reference_differences": differences,
                "state_mass": state_mass,
                "collision_mass": collision,
                "reference_reserve_mass": reserve_mass,
                "diameter_bound": diameter_bound,
            }
        )

    if sum(aspect_mass.values(), Fraction()) != repeated_oriented_collision_mass:
        raise AssertionError("aspect-band mass identity failed")

    reference_union: dict[tuple[int, tuple[int, ...]], Fraction] = {}
    reference_multiplicity = Counter()
    for reference_shell, reserve_state, mass, _origin in reference_shell_occurrences:
        identity = (reference_shell, reserve_state)
        reference_union[identity] = mass
        reference_multiplicity[identity] += 1
    reference_union_mass = sum(reference_union.values(), Fraction())

    serial_repeated_rows = [
        {
            **row,
            "state_mass": fraction_text(row["state_mass"]),  # type: ignore[arg-type]
            "collision_mass": fraction_text(row["collision_mass"]),  # type: ignore[arg-type]
            "reference_reserve_mass": fraction_text(row["reference_reserve_mass"]),  # type: ignore[arg-type]
        }
        for row in repeated_rows
    ]
    serial_reference_shells = [
        (
            reference_shell,
            reserve_state,
            fraction_text(mass),
            origin,
        )
        for reference_shell, reserve_state, mass, origin in reference_shell_occurrences
    ]

    output = {
        "schema": "s7_heavy_state_reference_reserve_profile_v1",
        "scope": "heavy completion-step shells on the refined R4_to_F5 S7 frontier",
        "generation_six_propagated": False,
        "counts": {
            "heavy_shell_occurrences": len(heavy_occurrences),
            "distinct_heavy_state_identities": len(by_state),
            "repeated_heavy_state_identities": sum(len(rows) > 1 for rows in by_state.values()),
            "maximum_heavy_state_multiplicity": max(multiplicity_profile, default=0),
            "oriented_reference_families": reference_family_count,
            "reference_shell_occurrences": len(reference_shell_occurrences),
            "distinct_reference_reserve_states": len(reference_union),
            "maximum_reference_reserve_multiplicity": max(reference_multiplicity.values(), default=0),
            "maximum_reference_diameter": maximum_reference_diameter,
            "maximum_reference_shell_base": maximum_reference_shell_base,
        },
        "masses": {
            "heavy_shell_occurrence_mass": serialize_mass(occurrence_mass),
            "heavy_state_union_mass": serialize_mass(state_union_mass),
            "heavy_state_collision_mass": serialize_mass(collision_mass),
            "oriented_repeated_collision_mass": serialize_mass(repeated_oriented_collision_mass),
            "reference_reserve_occurrence_mass": serialize_mass(reference_reserve_occurrence_mass),
            "reference_reserve_union_mass": serialize_mass(reference_union_mass),
        },
        "heavy_state_multiplicity_profile": [
            {"multiplicity": value, "states": multiplicity_profile[value]}
            for value in sorted(multiplicity_profile)
        ],
        "aspect_band_profile": [
            {
                "band": band,
                "cells": aspect_cells[band],
                "collision_mass": serialize_mass(aspect_mass[band]),
            }
            for band in sorted(aspect_mass)
        ],
        "hashes": {
            "heavy_occurrences": canonical_hash(
                sorted(
                    (
                        row["shell_base"],
                        row["state"],
                        row["orientation"],
                        row["completion"],
                        row["support"],
                    )
                    for row in heavy_occurrences
                )
            ),
            "repeated_reference_rows": canonical_hash(serial_repeated_rows),
            "reference_shell_occurrences": canonical_hash(serial_reference_shells),
        },
        "checks": {
            "heavy_state_first_use_collision_identity": occurrence_mass == state_union_mass + collision_mass,
            "all_reference_sets_four_ap_free": True,
            "all_reference_reserves_four_ap_free": True,
            "reference_parent_scale_descent": maximum_reference_shell_base <= parent_scale // 2,
            "aspect_mass_identity": sum(aspect_mass.values(), Fraction()) == repeated_oriented_collision_mass,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    output_path.write_text(json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
