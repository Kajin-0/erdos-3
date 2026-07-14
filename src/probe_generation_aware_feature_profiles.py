#!/usr/bin/env python3
"""Probe exact aggregate features across three retained recursive generations."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
import sys

from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

FEATURE_NAMES = (
    "current_mass",
    "root_occurrence_mass",
    "immediate_occurrence_mass",
    "root_depth_charge",
    "immediate_depth_charge",
    "root_repeat_descendant_mass",
    "root_repeat_occurrence_mass",
    "immediate_repeat_descendant_mass",
    "immediate_repeat_occurrence_mass",
    "root_tail_ge4_descendant_mass",
    "root_tail_ge8_descendant_mass",
    "immediate_tail_ge4_descendant_mass",
)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def decimal_text(value: Fraction, places: int = 12) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    scale = 10 ** places
    rounded = (value.numerator * scale * 2 + value.denominator) // (
        2 * value.denominator
    )
    whole, fractional = divmod(rounded, scale)
    return f"{sign}{whole}.{fractional:0{places}d}"


def floor_log_ratio(parent: int, child: int) -> int:
    if parent < child:
        raise AssertionError(f"noncontracting provenance ratio: {parent}/{child}")
    return (parent // child).bit_length() - 1


def point_rows(states: tuple[object, ...], generation: int) -> list[tuple[int, int, int]]:
    rows: list[tuple[int, int, int]] = []
    for state in states:
        representative = state.representative
        roots = representative.provenance
        immediates = getattr(representative, "immediate_provenance", roots)
        for current, root, immediate in zip(
            state.values, roots, immediates, strict=True
        ):
            if root < current or immediate < current:
                raise AssertionError(
                    f"generation {generation} has expanding provenance: "
                    f"u={current}, p={root}, i={immediate}"
                )
            rows.append((current, root, immediate))
    return rows


def feature_profile(rows: list[tuple[int, int, int]]) -> dict[str, Fraction]:
    root_counts = Counter(root for _current, root, _immediate in rows)
    immediate_counts = Counter(immediate for _current, _root, immediate in rows)
    profile = {name: Fraction() for name in FEATURE_NAMES}
    for current, root, immediate in rows:
        root_depth = floor_log_ratio(root, current)
        immediate_depth = floor_log_ratio(immediate, current)
        profile["current_mass"] += Fraction(1, current)
        profile["root_occurrence_mass"] += Fraction(1, root)
        profile["immediate_occurrence_mass"] += Fraction(1, immediate)
        profile["root_depth_charge"] += Fraction(root_depth, root)
        profile["immediate_depth_charge"] += Fraction(immediate_depth, immediate)
        if root_counts[root] > 1:
            profile["root_repeat_descendant_mass"] += Fraction(1, current)
            profile["root_repeat_occurrence_mass"] += Fraction(1, root)
        if immediate_counts[immediate] > 1:
            profile["immediate_repeat_descendant_mass"] += Fraction(1, current)
            profile["immediate_repeat_occurrence_mass"] += Fraction(1, immediate)
        if root_depth >= 4:
            profile["root_tail_ge4_descendant_mass"] += Fraction(1, current)
        if root_depth >= 8:
            profile["root_tail_ge8_descendant_mass"] += Fraction(1, current)
        if immediate_depth >= 4:
            profile["immediate_tail_ge4_descendant_mass"] += Fraction(1, current)
    return profile


def single_feature_interval(
    d12_current: Fraction,
    d23_current: Fraction,
    d12_feature: Fraction,
    d23_feature: Fraction,
) -> dict[str, object]:
    lower = Fraction()
    upper: Fraction | None = None
    impossible = False
    for current_delta, feature_delta in (
        (d12_current, d12_feature),
        (d23_current, d23_feature),
    ):
        if feature_delta == 0:
            if current_delta > 0:
                impossible = True
            continue
        boundary = -current_delta / feature_delta
        if feature_delta > 0:
            upper = boundary if upper is None else min(upper, boundary)
        else:
            lower = max(lower, boundary)
    lower = max(lower, Fraction())
    feasible = not impossible and (upper is None or lower <= upper)
    witness: Fraction | None = None
    if feasible:
        witness = lower
        if upper is not None and witness == upper:
            witness = upper
    return {
        "feasible": feasible,
        "lower": fraction_text(lower),
        "upper": None if upper is None else fraction_text(upper),
        "witness": None if witness is None else fraction_text(witness),
        "witness_decimal": None if witness is None else decimal_text(witness),
    }


def main() -> int:
    retained_first, retained_second = reconstruct_retained_families()
    recursive_second = tuple(
        state for state in retained_second
        if contains_three_term_ap(state.values)
    )
    _occurrences, retained_third, metrics, _child_rows = propagate_recursive_states(
        recursive_second
    )
    recursive_third = tuple(
        state for state in retained_third
        if contains_three_term_ap(state.values)
    )

    families = {
        "generation1_retained": retained_first,
        "generation2_recursive": recursive_second,
        "generation3_recursive": recursive_third,
    }
    rows = {
        name: point_rows(states, generation=index)
        for index, (name, states) in enumerate(families.items(), start=1)
    }
    profiles = {name: feature_profile(value) for name, value in rows.items()}
    differences = {
        "generation2_minus_generation1": {
            feature: profiles["generation2_recursive"][feature]
            - profiles["generation1_retained"][feature]
            for feature in FEATURE_NAMES
        },
        "generation3_minus_generation2": {
            feature: profiles["generation3_recursive"][feature]
            - profiles["generation2_recursive"][feature]
            for feature in FEATURE_NAMES
        },
    }

    d12_current = differences["generation2_minus_generation1"]["current_mass"]
    d23_current = differences["generation3_minus_generation2"]["current_mass"]
    intervals = {
        feature: single_feature_interval(
            d12_current,
            d23_current,
            differences["generation2_minus_generation1"][feature],
            differences["generation3_minus_generation2"][feature],
        )
        for feature in FEATURE_NAMES
        if feature != "current_mass"
    }

    output = {
        "schema": "generation_aware_feature_profiles_probe_v1",
        "family_counts": {
            name: {
                "states": len(families[name]),
                "points": len(rows[name]),
            }
            for name in families
        },
        "third_generation_quotient_metrics": metrics,
        "feature_decimals": {
            name: {
                feature: decimal_text(value)
                for feature, value in profiles[name].items()
            }
            for name in profiles
        },
        "feature_hashes": {
            name: {
                feature: fraction_hash(value)
                for feature, value in profiles[name].items()
            }
            for name in profiles
        },
        "difference_decimals": {
            name: {
                feature: decimal_text(value)
                for feature, value in differences[name].items()
            }
            for name in differences
        },
        "difference_hashes": {
            name: {
                feature: fraction_hash(value)
                for feature, value in differences[name].items()
            }
            for name in differences
        },
        "single_feature_intervals_with_current_mass_coefficient_1": intervals,
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
