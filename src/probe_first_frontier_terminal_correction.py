#!/usr/bin/env python3
"""Correct the historical F1->F2 transition by stopping terminal F1 states.

The original second-generation certificate propagated every state in the first
retained family.  Its own metrics record only 15/21 parents with selected
three-term progressions.  This probe partitions F1 by the certified 3-AP test,
propagates only the genuinely recursive subfamily, and compares:

1. historical certified F2 (all 21 F1 states propagated);
2. terminal-stopped ordinary F2 (only recursive F1 states propagated);
3. terminal-stopped residual/sponsor-refined F2.

No frontier beyond F2 is constructed.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import sys

from probe_residual_sponsor_backbone_split import (
    build_split_occurrences,
    occurrence_harmonic_mass,
    resource_profile,
    retain_occurrences,
    support_union,
)
from probe_root_lineage_transfer_classification import canonical_hash, serialize_mass
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
sys.setrecursionlimit(20_000)


def family_signature(states: tuple[object, ...]) -> str:
    return canonical_hash(
        [
            {
                "index": state.index,
                "values": list(state.values),
                "parent_class": state.representative.parent_class,
                "source": state.representative.source,
                "source_step": state.representative.source_step,
                "exponent": state.representative.exponent,
                "provenance": list(state.representative.provenance),
                "immediate": list(state.representative.immediate_provenance),
            }
            for state in states
        ]
    )


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
        raise AssertionError("family mass partition failed")
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
        "family_sha256": family_signature(states),
        "terminal_family_sha256": family_signature(terminal),
        "recursive_family_sha256": family_signature(recursive),
    }


def difference(left: dict[str, object], right: dict[str, object]) -> dict[str, object]:
    """Return left-right for the principal family metrics."""
    return {
        "states": int(left["states"]) - int(right["states"]),
        "points": int(left["points"]) - int(right["points"]),
        "terminal_states": int(left["terminal_states"])
        - int(right["terminal_states"]),
        "terminal_points": int(left["terminal_points"])
        - int(right["terminal_points"]),
        "recursive_states": int(left["recursive_states"])
        - int(right["recursive_states"]),
        "recursive_points": int(left["recursive_points"])
        - int(right["recursive_points"]),
        "total_mass": serialize_mass(
            Fraction(left["total_mass"]["fraction"])
            - Fraction(right["total_mass"]["fraction"])
        ),
        "terminal_mass": serialize_mass(
            Fraction(left["terminal_mass"]["fraction"])
            - Fraction(right["terminal_mass"]["fraction"])
        ),
        "recursive_mass": serialize_mass(
            Fraction(left["recursive_mass"]["fraction"])
            - Fraction(right["recursive_mass"]["fraction"])
        ),
    }


def main() -> int:
    first_all, historical_f2 = reconstruct_retained_families()
    first_terminal = tuple(
        state for state in first_all if not contains_three_term_ap(state.values)
    )
    first_recursive = tuple(
        state for state in first_all if contains_three_term_ap(state.values)
    )
    if len(first_all) != 21 or len(first_recursive) != 15 or len(first_terminal) != 6:
        raise AssertionError(
            "unexpected F1 split: "
            f"all={len(first_all)} recursive={len(first_recursive)} "
            f"terminal={len(first_terminal)}"
        )

    ordinary_occurrences, ordinary_f2, ordinary_metrics, ordinary_rows = (
        propagate_recursive_states(first_recursive)
    )
    refined_occurrences = build_split_occurrences(first_recursive)
    refined_f2, refined_metrics = retain_occurrences(refined_occurrences)

    if support_union(ordinary_occurrences) != support_union(refined_occurrences):
        raise AssertionError("residual/sponsor split changed corrected raw support")
    if sum(len(item.values) for item in ordinary_occurrences) != sum(
        len(item.values) for item in refined_occurrences
    ):
        raise AssertionError("residual/sponsor split changed corrected occurrences")
    if occurrence_harmonic_mass(ordinary_occurrences) != occurrence_harmonic_mass(
        refined_occurrences
    ):
        raise AssertionError("residual/sponsor split changed corrected raw mass")

    first_profile = family_profile(first_all)
    first_terminal_profile = family_profile(first_terminal)
    first_recursive_profile = family_profile(first_recursive)
    historical_profile = family_profile(historical_f2)
    ordinary_profile = family_profile(ordinary_f2)
    refined_profile = family_profile(refined_f2)

    terminal_parent_indices = {state.index for state in first_terminal}
    historical_representatives_from_terminal_parents = tuple(
        state
        for state in historical_f2
        if state.representative.parent_class in terminal_parent_indices
    )

    output = {
        "schema": "first_frontier_terminal_correction_probe_v1",
        "scope": "certified_F1_terminal_split_and_corrected_F2_reconstruction",
        "generation_three_or_later_constructed": False,
        "first_frontier": {
            "all": first_profile,
            "terminal": first_terminal_profile,
            "recursive": first_recursive_profile,
            "terminal_parent_indices": sorted(terminal_parent_indices),
            "selected_action_parent_count": sum(
                int(row["selected_actions"]) > 0 for row in ordinary_rows
            ),
        },
        "historical_F2_all_21_parents": historical_profile,
        "historical_representatives_from_terminal_parents": {
            "states": len(historical_representatives_from_terminal_parents),
            "points": sum(
                len(state.values)
                for state in historical_representatives_from_terminal_parents
            ),
            "mass": serialize_mass(
                sum(
                    (
                        state.weight
                        for state in historical_representatives_from_terminal_parents
                    ),
                    Fraction(),
                )
            ),
            "family_sha256": family_signature(
                historical_representatives_from_terminal_parents
            ),
        },
        "corrected_F2_recursive_parents_only": {
            "family": ordinary_profile,
            "propagation_metrics": ordinary_metrics,
            "raw_occurrences": len(ordinary_occurrences),
            "raw_points": sum(len(item.values) for item in ordinary_occurrences),
            "raw_support": len(support_union(ordinary_occurrences)),
            "raw_harmonic_occurrence_mass": serialize_mass(
                occurrence_harmonic_mass(ordinary_occurrences)
            ),
            "resource_profile": resource_profile(ordinary_f2),
        },
        "corrected_refined_F2": {
            "family": refined_profile,
            "retention_metrics": refined_metrics,
            "raw_occurrences": len(refined_occurrences),
            "raw_points": sum(len(item.values) for item in refined_occurrences),
            "raw_support": len(support_union(refined_occurrences)),
            "raw_harmonic_occurrence_mass": serialize_mass(
                occurrence_harmonic_mass(refined_occurrences)
            ),
            "resource_profile": resource_profile(refined_f2),
        },
        "comparisons": {
            "historical_minus_corrected_ordinary": difference(
                historical_profile, ordinary_profile
            ),
            "corrected_refined_minus_corrected_ordinary": difference(
                refined_profile, ordinary_profile
            ),
            "historical_equals_corrected_ordinary": (
                family_signature(historical_f2) == family_signature(ordinary_f2)
            ),
            "corrected_ordinary_equals_refined": (
                family_signature(ordinary_f2) == family_signature(refined_f2)
            ),
            "corrected_raw_support_preserved_by_split": True,
            "corrected_raw_occurrences_preserved_by_split": True,
            "corrected_raw_harmonic_mass_preserved_by_split": True,
        },
        "hashes": {
            "first_all": family_signature(first_all),
            "first_terminal": family_signature(first_terminal),
            "first_recursive": family_signature(first_recursive),
            "historical_f2": family_signature(historical_f2),
            "ordinary_corrected_f2": family_signature(ordinary_f2),
            "refined_corrected_f2": family_signature(refined_f2),
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
