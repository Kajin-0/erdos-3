#!/usr/bin/env python3
"""Probe the fifth retained recursive generation and H+74R exactly."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
import sys

from probe_fourth_generation_potential_frontier import (
    collision_details,
    compact_bracket,
    terminal_point_records,
)
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
    state_value_sets,
    state_values,
)
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
sys.setrecursionlimit(30_000)

COEFFICIENT = Fraction(74)


def main() -> int:
    retained_first, retained_second = reconstruct_retained_families()
    terminal_second = tuple(
        state for state in retained_second if not contains_three_term_ap(state.values)
    )
    recursive_second = tuple(
        state for state in retained_second if contains_three_term_ap(state.values)
    )
    _occ3, retained_third, metrics3, _rows3 = propagate_recursive_states(recursive_second)
    terminal_third = tuple(
        state for state in retained_third if not contains_three_term_ap(state.values)
    )
    recursive_third = tuple(
        state for state in retained_third if contains_three_term_ap(state.values)
    )
    _occ4, retained_fourth, metrics4, _rows4 = propagate_recursive_states(recursive_third)
    terminal_fourth = tuple(
        state for state in retained_fourth if not contains_three_term_ap(state.values)
    )
    recursive_fourth = tuple(
        state for state in retained_fourth if contains_three_term_ap(state.values)
    )
    occurrences5, retained_fifth, metrics5, child_rows5 = propagate_recursive_states(recursive_fourth)
    terminal_fifth = tuple(
        state for state in retained_fifth if not contains_three_term_ap(state.values)
    )
    recursive_fifth = tuple(
        state for state in retained_fifth if contains_three_term_ap(state.values)
    )

    families = {
        "generation1_retained": retained_first,
        "generation2_recursive": recursive_second,
        "generation3_recursive": recursive_third,
        "generation4_recursive": recursive_fourth,
        "generation5_recursive": recursive_fifth,
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
    ratio45 = potentials["generation5_recursive"] / potentials["generation4_recursive"]
    raw_ratio45 = (
        profiles["generation5_recursive"]["current_mass"]
        / profiles["generation4_recursive"]["current_mass"]
    )

    prior_terminal_records = (
        terminal_point_records(terminal_second, 2)
        + terminal_point_records(terminal_third, 3)
        + terminal_point_records(terminal_fourth, 4)
    )
    fifth_terminal_records = terminal_point_records(terminal_fifth, 5)
    fifth_recursive_records = terminal_point_records(recursive_fifth, 5)
    collisions = {}
    for mode in ("u_p", "u_p_i", "u_p_i_source"):
        terminal_details = collision_details(
            prior_terminal_records, fifth_terminal_records, mode
        )
        recursive_details = collision_details(
            prior_terminal_records, fifth_recursive_records, mode
        )
        collisions[mode] = {
            "terminal_count": len(terminal_details),
            "recursive_count": len(recursive_details),
            "all_count": len(terminal_details) + len(recursive_details),
            "terminal_signatures": [row["signature"] for row in terminal_details],
            "recursive_signatures": [row["signature"] for row in recursive_details],
            "terminal_signatures_sha256": canonical_hash(
                [row["signature"] for row in terminal_details]
            ),
            "recursive_signatures_sha256": canonical_hash(
                [row["signature"] for row in recursive_details]
            ),
        }

    prior_terminal_values = {int(row["u"]) for row in prior_terminal_records}
    numerical_terminal = sorted(prior_terminal_values & state_values(terminal_fifth))
    numerical_recursive = sorted(prior_terminal_values & state_values(recursive_fifth))
    prior_terminal_states = (
        state_value_sets(terminal_second)
        | state_value_sets(terminal_third)
        | state_value_sets(terminal_fourth)
    )
    regenerated_states = sorted(prior_terminal_states & state_value_sets(retained_fifth))

    root_counts = Counter(
        root
        for state in recursive_fifth
        for root in state.representative.provenance
    )
    immediate_counts = Counter(
        immediate
        for state in recursive_fifth
        for immediate in state.representative.immediate_provenance
    )

    output = {
        "schema": "fifth_generation_feature_frontier_probe_v1",
        "policy": "local37_then_lexicographic_recursive_only",
        "retention": "global_exact_duplicate_quotient_plus_maximum_harmonic_same_shell_independent_set",
        "generation3_metrics": metrics3,
        "generation4_metrics": metrics4,
        "generation5_metrics": {
            **metrics5,
            "terminal_states": len(terminal_fifth),
            "terminal_points": sum(len(state.values) for state in terminal_fifth),
            "recursive_states": len(recursive_fifth),
            "recursive_points": sum(len(state.values) for state in recursive_fifth),
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
        "integer_witness": {
            "coefficient": 74,
            "generation4_decimal": decimal_text(
                potentials["generation4_recursive"]
            ),
            "generation5_decimal": decimal_text(
                potentials["generation5_recursive"]
            ),
            "generation4_sha256": fraction_hash(
                potentials["generation4_recursive"]
            ),
            "generation5_sha256": fraction_hash(
                potentials["generation5_recursive"]
            ),
            "ratio45_decimal": decimal_text(ratio45),
            "ratio45_bracket_millionth": compact_bracket(ratio45),
            "ratio45_sha256": fraction_hash(ratio45),
            "strict_fifth_contraction": ratio45 < 1,
        },
        "raw_recursive_ratio45": {
            "decimal": decimal_text(raw_ratio45),
            "bracket_millionth": compact_bracket(raw_ratio45),
            "sha256": fraction_hash(raw_ratio45),
        },
        "terminal_collisions": collisions,
        "numerical_recreation": {
            "terminal_value_count": len(numerical_terminal),
            "recursive_value_count": len(numerical_recursive),
            "exact_state_regeneration_count": len(regenerated_states),
            "terminal_values_sha256": canonical_hash(numerical_terminal),
            "recursive_values_sha256": canonical_hash(numerical_recursive),
            "exact_state_regeneration_sha256": canonical_hash(regenerated_states),
        },
        "hashes": {
            "fifth_raw_occurrences": canonical_hash(
                [
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
                    for row in occurrences5
                ]
            ),
            "fifth_retained_family": canonical_hash(state_records(retained_fifth)),
            "fifth_terminal_family": canonical_hash(state_records(terminal_fifth)),
            "fifth_recursive_family": canonical_hash(state_records(recursive_fifth)),
            "child_transition_summary": canonical_hash(child_rows5),
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
