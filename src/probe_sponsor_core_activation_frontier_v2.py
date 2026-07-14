#!/usr/bin/env python3
"""Run the sponsor-core frontier with correct terminal-sink semantics.

The historical F1->F2 certificate propagated all 21 first retained states.  The
current terminal classifier shows that some of those states are already
three-AP-free.  This entry point records that discrepancy and computes the first
sponsor-core row from the genuinely recursive F1 subfamily only.  The later
R2->F3, R3->F4, and R4->F5 rows remain the established certified frontiers.

No sixth generation is constructed.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import sys

from probe_root_lineage_transfer_classification import serialize_mass
from probe_sponsor_core_activation_frontier import (
    recursive_states,
    state_signature,
    transition_record,
)
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
sys.setrecursionlimit(20_000)


def family_profile(states: tuple[object, ...]) -> dict[str, object]:
    terminal = tuple(
        state for state in states if not contains_three_term_ap(state.values)
    )
    recursive = tuple(
        state for state in states if contains_three_term_ap(state.values)
    )
    total_mass = sum((state.weight for state in states), Fraction())
    terminal_mass = sum((state.weight for state in terminal), Fraction())
    recursive_mass = sum((state.weight for state in recursive), Fraction())
    if terminal_mass + recursive_mass != total_mass:
        raise AssertionError("terminal/recursive mass partition failed")
    return {
        "states": len(states),
        "points": sum(len(state.values) for state in states),
        "terminal_states": len(terminal),
        "terminal_points": sum(len(state.values) for state in terminal),
        "recursive_states": len(recursive),
        "recursive_points": sum(len(state.values) for state in recursive),
        "total_mass": serialize_mass(total_mass),
        "terminal_mass": serialize_mass(terminal_mass),
        "recursive_mass": serialize_mass(recursive_mass),
        "family_sha256": state_signature(states),
        "terminal_family_sha256": state_signature(terminal),
        "recursive_family_sha256": state_signature(recursive),
    }


def finite_maximum(
    transitions: list[dict[str, object]], ratio_key: str
) -> tuple[Fraction, str]:
    values: list[tuple[Fraction, str]] = []
    for row in transitions:
        record = row["candidate_ratios"][ratio_key]
        if record is None:
            continue
        values.append((Fraction(record["fraction"]), row["name"]))
    return max(values, default=(Fraction(), ""))


def main() -> int:
    retained_first_all, retained_second_certified = reconstruct_retained_families()
    terminal_first = tuple(
        state
        for state in retained_first_all
        if not contains_three_term_ap(state.values)
    )
    r1 = recursive_states(retained_first_all)
    if not terminal_first:
        raise AssertionError(
            "expected the historical first retained family to contain terminal states"
        )
    if len(r1) + len(terminal_first) != len(retained_first_all):
        raise AssertionError("first retained terminal/recursive partition failed")

    # Correct first transition: propagate only states that still contain a 3-AP.
    occ2_corrected, retained_second_corrected, _metrics2c, _rows2c = (
        propagate_recursive_states(r1)
    )

    # Later rows retain the established certified frontiers for direct comparison.
    r2_certified = recursive_states(retained_second_certified)
    occ3, retained_third, _metrics3, _rows3 = propagate_recursive_states(
        r2_certified
    )
    r3_certified = recursive_states(retained_third)
    occ4, retained_fourth, _metrics4, _rows4 = propagate_recursive_states(
        r3_certified
    )
    r4_certified = recursive_states(retained_fourth)
    occ5, retained_fifth, _metrics5, _rows5 = propagate_recursive_states(
        r4_certified
    )

    transitions = [
        transition_record(
            "R1_recursive_only_to_F2_corrected",
            r1,
            occ2_corrected,
            retained_second_corrected,
        ),
        transition_record(
            "R2_certified_to_F3",
            r2_certified,
            occ3,
            retained_third,
        ),
        transition_record(
            "R3_certified_to_F4",
            r3_certified,
            occ4,
            retained_fourth,
        ),
        transition_record(
            "R4_certified_to_F5",
            r4_certified,
            occ5,
            retained_fifth,
        ),
    ]

    maximum_activation_ratio = finite_maximum(
        transitions, "refined_activation_over_selected_step_mass"
    )
    maximum_union_activation_ratio = finite_maximum(
        transitions, "refined_union_activation_over_selected_step_mass"
    )

    first_terminal_mass = sum(
        (state.weight for state in terminal_first), Fraction()
    )
    first_recursive_mass = sum((state.weight for state in r1), Fraction())

    output = {
        "schema": "sponsor_core_activation_frontier_probe_v1",
        "scope": (
            "corrected_recursive_R1_row_plus_certified_R2_through_R4_"
            "residual_sponsor_frontiers"
        ),
        "generation_six_propagated": False,
        "frontier_semantics": {
            "historical_F1_to_F2_propagated_all_first_retained_states": True,
            "corrected_R1_row_propagates_terminal_states": False,
            "first_retained_family": family_profile(retained_first_all),
            "first_terminal_mass": serialize_mass(first_terminal_mass),
            "first_recursive_mass": serialize_mass(first_recursive_mass),
            "historical_certified_F2": family_profile(retained_second_certified),
            "corrected_recursive_only_F2": family_profile(
                retained_second_corrected
            ),
            "corrected_F2_equals_historical_F2": (
                state_signature(retained_second_corrected)
                == state_signature(retained_second_certified)
            ),
        },
        "symbolic_identities": {
            "pair_energy_deletion": (
                "J(P)-J(Q)=sum of pair weights incident to deleted sponsors "
                "at first deletion"
            ),
            "sponsor_core_partition": (
                "core_energy+unused_residual_sponsor_cross_energy=J(P)-J(Q)"
            ),
            "action_edge_energy": (
                "sum_selected [1/q+1/(2q)]=(3/2) sum_selected 1/q"
            ),
        },
        "transitions": transitions,
        "finite_candidate_constants": {
            "maximum_refined_activation_over_selected_step_mass": serialize_mass(
                maximum_activation_ratio[0]
            ),
            "attained_at": maximum_activation_ratio[1],
            "maximum_refined_union_activation_over_selected_step_mass": serialize_mass(
                maximum_union_activation_ratio[0]
            ),
            "union_attained_at": maximum_union_activation_ratio[1],
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
