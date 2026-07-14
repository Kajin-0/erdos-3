#!/usr/bin/env python3
"""Test the affine root-pair Bellman row on the certified R4->F5 frontier.

The symbolic theorem gives, for affine minimum-pivot parents and pairwise
root-disjoint children,

    H(F5_total) + J(R5_recursive) <= J(R4_recursive),

where J is reciprocal root-pair energy.  This probe computes every term exactly,
checks root and pair multiplicities, and records the unused pair-energy surplus.
It does not propagate generation six.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
from itertools import combinations
import json
import sys

from probe_root_lineage_transfer_classification import canonical_hash, serialize_mass
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def root_multiset(states: tuple[object, ...]) -> Counter[int]:
    counts: Counter[int] = Counter()
    for state in states:
        counts.update(state.representative.provenance)
    return counts


def harmonic_mass(states: tuple[object, ...]) -> Fraction:
    return sum((state.weight for state in states), Fraction())


def affine_reference(state: object) -> int | None:
    roots = tuple(state.representative.provenance)
    values = tuple(state.values)
    if len(set(roots)) != len(roots):
        return None
    offsets = {root - value for root, value in zip(roots, values, strict=True)}
    if len(offsets) != 1:
        return None
    return next(iter(offsets))


def pair_counter(states: tuple[object, ...]) -> Counter[tuple[int, int]]:
    counter: Counter[tuple[int, int]] = Counter()
    for state in states:
        roots = tuple(sorted(state.representative.provenance))
        if len(set(roots)) != len(roots):
            raise AssertionError(
                f"state class {state.index} has repeated root provenance"
            )
        counter.update(combinations(roots, 2))
    return counter


def pair_energy(counter: Counter[tuple[int, int]], *, union: bool) -> Fraction:
    total = Fraction()
    for (left, right), multiplicity in counter.items():
        if not left < right:
            raise AssertionError("invalid root pair ordering")
        coefficient = 1 if union else multiplicity
        total += Fraction(coefficient, right - left)
    return total


def pair_profile(states: tuple[object, ...], name: str) -> dict[str, object]:
    roots = root_multiset(states)
    pairs = pair_counter(states)
    occurrence_energy = pair_energy(pairs, union=False)
    union_energy = pair_energy(pairs, union=True)
    repeated_energy = occurrence_energy - union_energy
    affine_rows = []
    for state in sorted(states, key=lambda item: item.index):
        reference = affine_reference(state)
        affine_rows.append(
            {
                "state_class": state.index,
                "size": len(state.values),
                "distinct_roots": len(set(state.representative.provenance)),
                "affine": reference is not None,
                "reference_root": reference,
                "source": state.representative.source,
                "source_step": state.representative.source_step,
                "exponent": state.representative.exponent,
            }
        )
    return {
        "name": name,
        "states": len(states),
        "points": sum(len(state.values) for state in states),
        "harmonic_mass": serialize_mass(harmonic_mass(states)),
        "distinct_roots": len(roots),
        "repeated_root_labels": sum(count > 1 for count in roots.values()),
        "maximum_root_multiplicity": max(roots.values(), default=0),
        "pair_occurrences": sum(pairs.values()),
        "distinct_pairs": len(pairs),
        "repeated_pair_tokens": sum(count > 1 for count in pairs.values()),
        "maximum_pair_multiplicity": max(pairs.values(), default=0),
        "pair_energy_occurrence": serialize_mass(occurrence_energy),
        "pair_energy_union": serialize_mass(union_energy),
        "repeated_pair_energy": serialize_mass(repeated_energy),
        "affine_states": sum(row["affine"] for row in affine_rows),
        "nonaffine_states": sum(not row["affine"] for row in affine_rows),
        "affine_rows": affine_rows,
        "root_multiplicity_sha256": canonical_hash(sorted(roots.items())),
        "pair_multiplicity_sha256": canonical_hash(
            [(left, right, count) for (left, right), count in sorted(pairs.items())]
        ),
    }


def main() -> int:
    _retained_first, retained_second = reconstruct_retained_families()
    recursive_second = tuple(
        state for state in retained_second if contains_three_term_ap(state.values)
    )
    _occ3, retained_third, _metrics3, _rows3 = propagate_recursive_states(
        recursive_second
    )
    recursive_third = tuple(
        state for state in retained_third if contains_three_term_ap(state.values)
    )
    _occ4, retained_fourth, _metrics4, _rows4 = propagate_recursive_states(
        recursive_third
    )
    recursive_fourth = tuple(
        state for state in retained_fourth if contains_three_term_ap(state.values)
    )
    _occ5, retained_fifth, metrics5, _rows5 = propagate_recursive_states(
        recursive_fourth
    )
    recursive_fifth = tuple(
        state for state in retained_fifth if contains_three_term_ap(state.values)
    )
    terminal_fifth = tuple(
        state for state in retained_fifth if not contains_three_term_ap(state.values)
    )

    profile4 = pair_profile(recursive_fourth, "R4_recursive")
    profile5 = pair_profile(recursive_fifth, "R5_recursive")
    total_h5 = harmonic_mass(retained_fifth)
    terminal_h5 = harmonic_mass(terminal_fifth)
    recursive_h5 = harmonic_mass(recursive_fifth)
    j4_occ = Fraction(profile4["pair_energy_occurrence"]["fraction"])
    j4_union = Fraction(profile4["pair_energy_union"]["fraction"])
    j5_occ = Fraction(profile5["pair_energy_occurrence"]["fraction"])
    j5_union = Fraction(profile5["pair_energy_union"]["fraction"])

    occurrence_left = total_h5 + j5_occ
    union_left = total_h5 + j5_union
    occurrence_surplus = j4_occ - occurrence_left
    union_surplus = j4_union - union_left

    if profile4["maximum_root_multiplicity"] != 1:
        raise AssertionError("R4 roots are not globally unique")
    if profile5["maximum_root_multiplicity"] != 1:
        raise AssertionError("R5 recursive roots are not globally unique")
    if profile4["maximum_pair_multiplicity"] != 1:
        raise AssertionError("R4 pair tokens repeat")
    if profile5["maximum_pair_multiplicity"] != 1:
        raise AssertionError("R5 pair tokens repeat")
    if profile4["nonaffine_states"] != 0:
        raise AssertionError("R4 contains a nonaffine root state")
    if occurrence_surplus < 0 or union_surplus < 0:
        raise AssertionError("pair-energy Bellman row fails")
    if j4_occ != j4_union or j5_occ != j5_union:
        raise AssertionError("occurrence and union pair energy differ despite uniqueness")

    output = {
        "schema": "pair_energy_frontier_probe_v1",
        "scope": "certified_R4_recursive_to_F5_retained_transition",
        "generation_six_propagated": False,
        "profiles": [profile4, profile5],
        "fifth_output": {
            "total_states": len(retained_fifth),
            "total_points": sum(len(state.values) for state in retained_fifth),
            "terminal_states": len(terminal_fifth),
            "terminal_points": sum(len(state.values) for state in terminal_fifth),
            "recursive_states": len(recursive_fifth),
            "recursive_points": sum(len(state.values) for state in recursive_fifth),
            "total_harmonic_mass": serialize_mass(total_h5),
            "terminal_harmonic_mass": serialize_mass(terminal_h5),
            "recursive_harmonic_mass": serialize_mass(recursive_h5),
        },
        "bellman_rows": {
            "occurrence_pair_energy": {
                "left_H5_plus_J5": serialize_mass(occurrence_left),
                "right_J4": serialize_mass(j4_occ),
                "surplus": serialize_mass(occurrence_surplus),
                "verified": occurrence_left <= j4_occ,
                "ratio": serialize_mass(occurrence_left / j4_occ),
            },
            "union_pair_energy": {
                "left_H5_plus_J5": serialize_mass(union_left),
                "right_J4": serialize_mass(j4_union),
                "surplus": serialize_mass(union_surplus),
                "verified": union_left <= j4_union,
                "ratio": serialize_mass(union_left / j4_union),
            },
        },
        "metrics5": metrics5,
        "hashes": {
            "profiles": canonical_hash(
                [
                    {
                        key: profile[key]
                        for key in (
                            "name",
                            "states",
                            "points",
                            "harmonic_mass",
                            "distinct_roots",
                            "repeated_root_labels",
                            "maximum_root_multiplicity",
                            "pair_occurrences",
                            "distinct_pairs",
                            "repeated_pair_tokens",
                            "maximum_pair_multiplicity",
                            "pair_energy_occurrence",
                            "pair_energy_union",
                            "repeated_pair_energy",
                            "affine_states",
                            "nonaffine_states",
                            "affine_rows",
                            "root_multiplicity_sha256",
                            "pair_multiplicity_sha256",
                        )
                    }
                    for profile in (profile4, profile5)
                ]
            ),
            "bellman_rows": canonical_hash(
                {
                    "occurrence_left": occurrence_left,
                    "occurrence_right": j4_occ,
                    "occurrence_surplus": occurrence_surplus,
                    "union_left": union_left,
                    "union_right": j4_union,
                    "union_surplus": union_surplus,
                }
            ),
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
