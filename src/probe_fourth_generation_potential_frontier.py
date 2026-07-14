#!/usr/bin/env python3
"""Probe the fourth retained generation and provenance-reserve potentials exactly."""
from __future__ import annotations

from collections import Counter
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
from probe_third_generation_recursive_frontier import (
    canonical_hash,
    propagate_recursive_states,
    state_records,
    state_tokens,
    state_value_sets,
    state_values,
)
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
sys.setrecursionlimit(30_000)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def compact_bracket(value: Fraction, denominator: int = 1_000_000) -> list[str]:
    lower_numerator = (value.numerator * denominator) // value.denominator
    lower = Fraction(lower_numerator, denominator)
    upper = Fraction(lower_numerator + 1, denominator)
    return [fraction_text(lower), fraction_text(upper)]


def terminal_point_records(
    states: tuple[object, ...], generation: int
) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for state in states:
        representative = state.representative
        for current, root, immediate in zip(
            state.values,
            representative.provenance,
            representative.immediate_provenance,
            strict=True,
        ):
            records.append(
                {
                    "generation": generation,
                    "class_index": state.index,
                    "parent_class": representative.parent_class,
                    "source": representative.source,
                    "source_step": representative.source_step,
                    "u": current,
                    "p": root,
                    "i": immediate,
                    "state_values": list(state.values),
                }
            )
    return records


def signature_set(
    records: list[dict[str, object]], mode: str
) -> set[tuple[object, ...]]:
    if mode == "u_p":
        return {(row["u"], row["p"]) for row in records}
    if mode == "u_p_i":
        return {(row["u"], row["p"], row["i"]) for row in records}
    if mode == "u_p_i_source":
        return {
            (
                row["u"], row["p"], row["i"],
                row["source"], row["source_step"],
            )
            for row in records
        }
    raise ValueError(mode)


def collision_details(
    prior: list[dict[str, object]],
    current: list[dict[str, object]],
    mode: str,
) -> list[dict[str, object]]:
    prior_map: dict[tuple[object, ...], list[dict[str, object]]] = {}
    current_map: dict[tuple[object, ...], list[dict[str, object]]] = {}
    for row in prior:
        key = next(iter(signature_set([row], mode)))
        prior_map.setdefault(key, []).append(row)
    for row in current:
        key = next(iter(signature_set([row], mode)))
        current_map.setdefault(key, []).append(row)
    return [
        {
            "signature": list(key),
            "prior": prior_map[key],
            "current": current_map[key],
        }
        for key in sorted(set(prior_map) & set(current_map), key=repr)
    ]


def potential_quantities(
    profiles: dict[str, dict[str, Fraction]],
    feature: str,
    coefficient: int,
) -> dict[str, Fraction]:
    values = {
        generation: profile["current_mass"] + coefficient * profile[feature]
        for generation, profile in profiles.items()
    }
    ratio34 = values["generation4_recursive"] / values["generation3_recursive"]
    return {
        **values,
        "delta34": values["generation4_recursive"] - values["generation3_recursive"],
        "ratio34": ratio34,
        "margin34": 1 - ratio34,
        "ratio14": values["generation4_recursive"] / values["generation1_retained"],
    }


def main() -> int:
    retained_first, retained_second = reconstruct_retained_families()
    terminal_second = tuple(
        state for state in retained_second
        if not contains_three_term_ap(state.values)
    )
    recursive_second = tuple(
        state for state in retained_second
        if contains_three_term_ap(state.values)
    )
    _occurrences3, retained_third, metrics3, _child_rows3 = (
        propagate_recursive_states(recursive_second)
    )
    terminal_third = tuple(
        state for state in retained_third
        if not contains_three_term_ap(state.values)
    )
    recursive_third = tuple(
        state for state in retained_third
        if contains_three_term_ap(state.values)
    )
    occurrences4, retained_fourth, metrics4, child_rows4 = (
        propagate_recursive_states(recursive_third)
    )
    terminal_fourth = tuple(
        state for state in retained_fourth
        if not contains_three_term_ap(state.values)
    )
    recursive_fourth = tuple(
        state for state in retained_fourth
        if contains_three_term_ap(state.values)
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
    primary = potential_quantities(
        profiles, "root_repeat_descendant_mass", 2
    )
    secondary = potential_quantities(
        profiles, "immediate_tail_ge4_descendant_mass", 4
    )

    third_recursive_mass = profiles["generation3_recursive"]["current_mass"]
    fourth_total_mass = sum(
        (state.weight for state in retained_fourth), Fraction()
    )
    fourth_terminal_mass = sum(
        (state.weight for state in terminal_fourth), Fraction()
    )
    fourth_recursive_mass = profiles["generation4_recursive"]["current_mass"]
    if fourth_terminal_mass + fourth_recursive_mass != fourth_total_mass:
        raise AssertionError("fourth terminal/recursive mass partition failed")

    mass_ratios = {
        "fourth_total_over_third_recursive": fourth_total_mass / third_recursive_mass,
        "fourth_terminal_over_fourth_total": fourth_terminal_mass / fourth_total_mass,
        "fourth_recursive_over_fourth_total": fourth_recursive_mass / fourth_total_mass,
        "fourth_recursive_over_third_recursive": fourth_recursive_mass / third_recursive_mass,
    }

    prior_terminal_records = (
        terminal_point_records(terminal_second, 2)
        + terminal_point_records(terminal_third, 3)
    )
    fourth_terminal_records = terminal_point_records(terminal_fourth, 4)
    fourth_recursive_records = terminal_point_records(recursive_fourth, 4)
    fourth_all_records = fourth_terminal_records + fourth_recursive_records

    collisions = {}
    for mode in ("u_p", "u_p_i", "u_p_i_source"):
        terminal_details = collision_details(
            prior_terminal_records, fourth_terminal_records, mode
        )
        recursive_details = collision_details(
            prior_terminal_records, fourth_recursive_records, mode
        )
        collisions[mode] = {
            "terminal_count": len(terminal_details),
            "recursive_count": len(recursive_details),
            "all_count": len(terminal_details) + len(recursive_details),
            "terminal_details": terminal_details,
            "recursive_details": recursive_details,
        }

    prior_terminal_values = {
        int(row["u"]) for row in prior_terminal_records
    }
    numerical_terminal = sorted(
        prior_terminal_values & state_values(terminal_fourth)
    )
    numerical_recursive = sorted(
        prior_terminal_values & state_values(recursive_fourth)
    )
    prior_terminal_states = (
        state_value_sets(terminal_second) | state_value_sets(terminal_third)
    )
    fourth_states = state_value_sets(retained_fourth)
    exact_state_regeneration = sorted(prior_terminal_states & fourth_states)

    root_counts = Counter(
        root
        for state in recursive_fourth
        for root in state.representative.provenance
    )
    immediate_counts = Counter(
        immediate
        for state in recursive_fourth
        for immediate in state.representative.immediate_provenance
    )

    raw_records4 = [
        {
            "index": row.index,
            "parent_class": row.parent_class,
            "source": row.source,
            "source_step": row.source_step,
            "exponent": row.exponent,
            "values": list(row.values),
            "provenance": list(row.provenance),
            "immediate_provenance": list(row.immediate_provenance),
        }
        for row in occurrences4
    ]

    output = {
        "schema": "fourth_generation_potential_frontier_probe_v1",
        "policy": "local37_then_lexicographic_recursive_only",
        "retention": "global_exact_duplicate_quotient_plus_maximum_harmonic_same_shell_independent_set",
        "generation3_metrics": metrics3,
        "generation4_metrics": {
            **metrics4,
            "terminal_states": len(terminal_fourth),
            "terminal_points": sum(len(state.values) for state in terminal_fourth),
            "recursive_states": len(recursive_fourth),
            "recursive_points": sum(len(state.values) for state in recursive_fourth),
            "root_provenance_distinct": len(root_counts),
            "root_provenance_repeated": sum(
                multiplicity > 1 for multiplicity in root_counts.values()
            ),
            "root_provenance_max_multiplicity": max(root_counts.values(), default=0),
            "immediate_provenance_distinct": len(immediate_counts),
            "immediate_provenance_repeated": sum(
                multiplicity > 1 for multiplicity in immediate_counts.values()
            ),
            "immediate_provenance_max_multiplicity": max(
                immediate_counts.values(), default=0
            ),
        },
        "family_counts": {
            name: {
                "states": len(states),
                "points": sum(len(state.values) for state in states),
            }
            for name, states in families.items()
        },
        "feature_decimals": {
            name: {
                "current_mass": decimal_text(profile["current_mass"]),
                "root_repeat_descendant_mass": decimal_text(
                    profile["root_repeat_descendant_mass"]
                ),
                "immediate_tail_ge4_descendant_mass": decimal_text(
                    profile["immediate_tail_ge4_descendant_mass"]
                ),
            }
            for name, profile in profiles.items()
        },
        "feature_hashes": {
            name: {
                "current_mass": fraction_hash(profile["current_mass"]),
                "root_repeat_descendant_mass": fraction_hash(
                    profile["root_repeat_descendant_mass"]
                ),
                "immediate_tail_ge4_descendant_mass": fraction_hash(
                    profile["immediate_tail_ge4_descendant_mass"]
                ),
            }
            for name, profile in profiles.items()
        },
        "potentials": {
            "root_repeat_descendant_weight_2": {
                "decimals": {
                    key: decimal_text(value) for key, value in primary.items()
                },
                "hashes": {
                    key: fraction_hash(value) for key, value in primary.items()
                },
                "ratio34_bracket_millionth": compact_bracket(primary["ratio34"]),
                "margin34_bracket_millionth": compact_bracket(primary["margin34"]),
                "strict_fourth_contraction": primary["delta34"] < 0,
            },
            "immediate_tail_ge4_weight_4": {
                "decimals": {
                    key: decimal_text(value) for key, value in secondary.items()
                },
                "hashes": {
                    key: fraction_hash(value) for key, value in secondary.items()
                },
                "ratio34_bracket_millionth": compact_bracket(secondary["ratio34"]),
                "margin34_bracket_millionth": compact_bracket(secondary["margin34"]),
                "strict_fourth_contraction": secondary["delta34"] < 0,
            },
        },
        "mass_ratios": {
            name: {
                "decimal": decimal_text(value),
                "hash": fraction_hash(value),
                "bracket_millionth": compact_bracket(value),
            }
            for name, value in mass_ratios.items()
        },
        "terminal_collisions": collisions,
        "numerical_recreation": {
            "terminal_values": numerical_terminal,
            "recursive_values": numerical_recursive,
            "exact_state_regeneration": [
                list(values) for values in exact_state_regeneration
            ],
        },
        "hashes": {
            "child_transition_summary": canonical_hash(child_rows4),
            "fourth_raw_occurrences": canonical_hash(raw_records4),
            "fourth_retained_family": canonical_hash(
                state_records(retained_fourth)
            ),
            "fourth_terminal_family": canonical_hash(
                state_records(terminal_fourth)
            ),
            "fourth_recursive_family": canonical_hash(
                state_records(recursive_fourth)
            ),
            "fourth_all_tokens": canonical_hash(
                sorted([list(row) for row in state_tokens(retained_fourth)])
            ),
            "fourth_terminal_tokens": canonical_hash(
                sorted([list(row) for row in state_tokens(terminal_fourth)])
            ),
            "fourth_recursive_tokens": canonical_hash(
                sorted([list(row) for row in state_tokens(recursive_fourth)])
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
