#!/usr/bin/env python3
"""Emit exact metrics for the sparse four-generation witness H + 74 R."""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import sys

from probe_generation_aware_feature_profiles import (
    decimal_text,
    feature_profile,
    fraction_hash,
    point_rows,
)
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

COEFFICIENT = Fraction(74)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def bracket(value: Fraction, denominator: int = 1_000_000) -> list[str]:
    lower_numerator = value.numerator * denominator // value.denominator
    lower = Fraction(lower_numerator, denominator)
    if lower == value:
        lower -= Fraction(1, denominator)
    upper = Fraction(lower_numerator + 1, denominator)
    return [fraction_text(lower), fraction_text(upper)]


def main() -> int:
    retained_first, retained_second = reconstruct_retained_families()
    recursive_second = tuple(
        state for state in retained_second if contains_three_term_ap(state.values)
    )
    _occ3, retained_third, _metrics3, _rows3 = propagate_recursive_states(recursive_second)
    recursive_third = tuple(
        state for state in retained_third if contains_three_term_ap(state.values)
    )
    _occ4, retained_fourth, _metrics4, _rows4 = propagate_recursive_states(recursive_third)
    recursive_fourth = tuple(
        state for state in retained_fourth if contains_three_term_ap(state.values)
    )

    families = {
        "generation1_retained": retained_first,
        "generation2_recursive": recursive_second,
        "generation3_recursive": recursive_third,
        "generation4_recursive": recursive_fourth,
    }
    profiles = {
        name: feature_profile(point_rows(states, generation=index))
        for index, (name, states) in enumerate(families.items(), start=1)
    }
    potentials = {
        name: profile["current_mass"]
        + COEFFICIENT * profile["root_repeat_descendant_mass"]
        for name, profile in profiles.items()
    }
    transitions = (
        ("generation2_over_generation1", "generation1_retained", "generation2_recursive"),
        ("generation3_over_generation2", "generation2_recursive", "generation3_recursive"),
        ("generation4_over_generation3", "generation3_recursive", "generation4_recursive"),
    )
    ratios = {
        label: potentials[child] / potentials[parent]
        for label, parent, child in transitions
    }
    margins = {label: Fraction(1) - ratio for label, ratio in ratios.items()}
    if not all(value > 0 for value in margins.values()):
        raise AssertionError("integer witness is not strictly contractive")

    current_d34 = (
        profiles["generation4_recursive"]["current_mass"]
        - profiles["generation3_recursive"]["current_mass"]
    )
    repeat_d34 = (
        profiles["generation4_recursive"]["root_repeat_descendant_mass"]
        - profiles["generation3_recursive"]["root_repeat_descendant_mass"]
    )
    threshold = -current_d34 / repeat_d34
    if not Fraction(73_015, 1_000) < threshold < Fraction(9_127, 125):
        raise AssertionError("threshold outside compact bracket")

    output = {
        "schema": "four_generation_integer_witness_v1",
        "coefficient": 74,
        "family_counts": {
            name: {
                "states": len(states),
                "points": sum(len(state.values) for state in states),
            }
            for name, states in families.items()
        },
        "potential_decimals": {
            name: decimal_text(value) for name, value in potentials.items()
        },
        "potential_hashes": {
            name: fraction_hash(value) for name, value in potentials.items()
        },
        "ratio_decimals": {name: decimal_text(value) for name, value in ratios.items()},
        "ratio_brackets_millionth": {name: bracket(value) for name, value in ratios.items()},
        "ratio_hashes": {name: fraction_hash(value) for name, value in ratios.items()},
        "margin_decimals": {name: decimal_text(value) for name, value in margins.items()},
        "margin_brackets_millionth": {name: bracket(value) for name, value in margins.items()},
        "margin_hashes": {name: fraction_hash(value) for name, value in margins.items()},
        "minimum_coefficient_decimal": decimal_text(threshold),
        "minimum_coefficient_bracket": ["73015/1000", "9127/125"],
        "minimum_coefficient_hash": fraction_hash(threshold),
        "strictly_contracts_all_three_transitions": True,
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
