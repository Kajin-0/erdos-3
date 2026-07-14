#!/usr/bin/env python3
"""Independently verify the corrected first retained frontier.

Reconstruct the certified first family, stop its six three-AP-free states,
propagate only the fifteen recursive states, and compare the ordinary and
residual/sponsor-refined retained second frontiers.

This verifier intentionally omits quadratic latent-pair profiles.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import sys

from probe_first_frontier_terminal_correction_v2 import family_signature
from probe_residual_sponsor_backbone_split import (
    build_split_occurrences,
    occurrence_harmonic_mass,
    retain_occurrences,
    support_union,
)
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
sys.setrecursionlimit(20_000)

EXPECTED_COUNTS = {
    "first_states": 21,
    "first_points": 11_753,
    "first_terminal_states": 6,
    "first_terminal_points": 52,
    "first_recursive_states": 15,
    "first_recursive_points": 11_701,
    "historical_states": 27,
    "historical_points": 7_925,
    "historical_terminal_states": 13,
    "historical_terminal_points": 43,
    "historical_recursive_states": 14,
    "historical_recursive_points": 7_882,
    "corrected_states": 27,
    "corrected_points": 7_923,
    "corrected_terminal_states": 12,
    "corrected_terminal_points": 38,
    "corrected_recursive_states": 15,
    "corrected_recursive_points": 7_885,
    "refined_states": 45,
    "refined_points": 8_164,
    "refined_terminal_states": 33,
    "refined_terminal_points": 944,
    "refined_recursive_states": 12,
    "refined_recursive_points": 7_220,
}

EXPECTED_TERMINAL_PARENT_INDICES = (0, 1, 2, 8, 74, 86)
EXPECTED_FAMILY_HASHES = {
    "first_all": "138ef8dfb0a0c6f2f37796cd6d6f82c81366ffe51642d1b701446e5c19ff6721",
    "first_recursive": "9c684fbbcd86498864abd9edd34c66237e55514069ea7d0ebe56bb9116e67022",
    "corrected_ordinary": "c83306865777eaf930aae1dbe8b4e709be66afc29956a78a20f04dfc49b3214c",
    "corrected_ordinary_recursive": "04ad7d200fb658ca926a9c8c2356440ed219927595e81aca85d8cb68de5f2f2b",
}
EXPECTED_HISTORICAL_MINUS_CORRECTED = {
    "total": Fraction(653, 11_583),
    "terminal": Fraction(20_453, 99_792),
    "recursive": Fraction(-649, 4_368),
}
EXPECTED_REFINEMENT_DELTA_HASHES = {
    "total": "3be67a3111aea8185a984fccbe00660abd3d7bf8e5c8a78d804d528a4005f55e",
    "terminal": "29b5b38d7d0146f72ff313de12ca0b7bd7fb0ee54e005ce492bfea9bbc62aceb",
    "recursive": "23587633ed808075bb6a067fafcf1204e772c95c0094f3c6d20f5a19f75699df",
}


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def decimal_text(value: Fraction, places: int = 12) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    scale = 10**places
    rounded = (value.numerator * scale * 2 + value.denominator) // (
        2 * value.denominator
    )
    whole, fractional = divmod(rounded, scale)
    return f"{sign}{whole}.{fractional:0{places}d}"


def mass_record(value: Fraction) -> dict[str, str]:
    return {
        "fraction": fraction_text(value),
        "decimal": decimal_text(value),
        "sha256": fraction_hash(value),
    }


def split(states: tuple[object, ...]) -> tuple[tuple[object, ...], tuple[object, ...]]:
    terminal = tuple(
        state for state in states if not contains_three_term_ap(state.values)
    )
    recursive = tuple(
        state for state in states if contains_three_term_ap(state.values)
    )
    if len(terminal) + len(recursive) != len(states):
        raise AssertionError("terminal/recursive partition failed")
    return terminal, recursive


def mass(states: tuple[object, ...]) -> Fraction:
    return sum((state.weight for state in states), Fraction())


def profile(states: tuple[object, ...]) -> dict[str, object]:
    terminal, recursive = split(states)
    return {
        "states": len(states),
        "points": sum(len(state.values) for state in states),
        "terminal_states": len(terminal),
        "terminal_points": sum(len(state.values) for state in terminal),
        "recursive_states": len(recursive),
        "recursive_points": sum(len(state.values) for state in recursive),
        "total_mass": mass_record(mass(states)),
        "terminal_mass": mass_record(mass(terminal)),
        "recursive_mass": mass_record(mass(recursive)),
        "family_sha256": family_signature(states),
        "recursive_family_sha256": family_signature(recursive),
    }


def main() -> int:
    first_all, historical_f2 = reconstruct_retained_families()
    first_terminal, first_recursive = split(first_all)
    terminal_indices = tuple(sorted(state.index for state in first_terminal))
    if terminal_indices != EXPECTED_TERMINAL_PARENT_INDICES:
        raise AssertionError(f"terminal parent indices changed: {terminal_indices}")

    ordinary_occurrences, corrected_ordinary, propagation_metrics, _rows = (
        propagate_recursive_states(first_recursive)
    )
    refined_occurrences = build_split_occurrences(first_recursive)
    corrected_refined, retention_metrics = retain_occurrences(refined_occurrences)

    if support_union(ordinary_occurrences) != support_union(refined_occurrences):
        raise AssertionError("refinement changed corrected raw support")
    if sum(len(row.values) for row in ordinary_occurrences) != sum(
        len(row.values) for row in refined_occurrences
    ):
        raise AssertionError("refinement changed corrected raw occurrence count")
    if occurrence_harmonic_mass(ordinary_occurrences) != occurrence_harmonic_mass(
        refined_occurrences
    ):
        raise AssertionError("refinement changed corrected raw harmonic mass")

    profiles = {
        "first": profile(first_all),
        "historical_f2": profile(historical_f2),
        "corrected_ordinary_f2": profile(corrected_ordinary),
        "corrected_refined_f2": profile(corrected_refined),
    }

    observed_counts = {
        "first_states": profiles["first"]["states"],
        "first_points": profiles["first"]["points"],
        "first_terminal_states": profiles["first"]["terminal_states"],
        "first_terminal_points": profiles["first"]["terminal_points"],
        "first_recursive_states": profiles["first"]["recursive_states"],
        "first_recursive_points": profiles["first"]["recursive_points"],
        "historical_states": profiles["historical_f2"]["states"],
        "historical_points": profiles["historical_f2"]["points"],
        "historical_terminal_states": profiles["historical_f2"]["terminal_states"],
        "historical_terminal_points": profiles["historical_f2"]["terminal_points"],
        "historical_recursive_states": profiles["historical_f2"]["recursive_states"],
        "historical_recursive_points": profiles["historical_f2"]["recursive_points"],
        "corrected_states": profiles["corrected_ordinary_f2"]["states"],
        "corrected_points": profiles["corrected_ordinary_f2"]["points"],
        "corrected_terminal_states": profiles["corrected_ordinary_f2"]["terminal_states"],
        "corrected_terminal_points": profiles["corrected_ordinary_f2"]["terminal_points"],
        "corrected_recursive_states": profiles["corrected_ordinary_f2"]["recursive_states"],
        "corrected_recursive_points": profiles["corrected_ordinary_f2"]["recursive_points"],
        "refined_states": profiles["corrected_refined_f2"]["states"],
        "refined_points": profiles["corrected_refined_f2"]["points"],
        "refined_terminal_states": profiles["corrected_refined_f2"]["terminal_states"],
        "refined_terminal_points": profiles["corrected_refined_f2"]["terminal_points"],
        "refined_recursive_states": profiles["corrected_refined_f2"]["recursive_states"],
        "refined_recursive_points": profiles["corrected_refined_f2"]["recursive_points"],
    }
    if observed_counts != EXPECTED_COUNTS:
        raise AssertionError(f"frontier counts changed: {observed_counts}")

    observed_hashes = {
        "first_all": profiles["first"]["family_sha256"],
        "first_recursive": profiles["first"]["recursive_family_sha256"],
        "corrected_ordinary": profiles["corrected_ordinary_f2"]["family_sha256"],
        "corrected_ordinary_recursive": profiles["corrected_ordinary_f2"][
            "recursive_family_sha256"
        ],
    }
    if observed_hashes != EXPECTED_FAMILY_HASHES:
        raise AssertionError(f"frontier family hashes changed: {observed_hashes}")

    first_recursive_mass = Fraction(
        profiles["first"]["recursive_mass"]["fraction"]
    )
    historical_terminal_mass = Fraction(
        profiles["historical_f2"]["terminal_mass"]["fraction"]
    )
    historical_recursive_mass = Fraction(
        profiles["historical_f2"]["recursive_mass"]["fraction"]
    )
    historical_total_mass = historical_terminal_mass + historical_recursive_mass
    ordinary_terminal_mass = Fraction(
        profiles["corrected_ordinary_f2"]["terminal_mass"]["fraction"]
    )
    ordinary_recursive_mass = Fraction(
        profiles["corrected_ordinary_f2"]["recursive_mass"]["fraction"]
    )
    ordinary_total_mass = ordinary_terminal_mass + ordinary_recursive_mass
    refined_terminal_mass = Fraction(
        profiles["corrected_refined_f2"]["terminal_mass"]["fraction"]
    )
    refined_recursive_mass = Fraction(
        profiles["corrected_refined_f2"]["recursive_mass"]["fraction"]
    )
    refined_total_mass = refined_terminal_mass + refined_recursive_mass

    historical_minus_corrected = {
        "total": historical_total_mass - ordinary_total_mass,
        "terminal": historical_terminal_mass - ordinary_terminal_mass,
        "recursive": historical_recursive_mass - ordinary_recursive_mass,
    }
    if historical_minus_corrected != EXPECTED_HISTORICAL_MINUS_CORRECTED:
        raise AssertionError(
            f"historical/corrected mass deltas changed: {historical_minus_corrected}"
        )

    refinement_deltas = {
        "total": refined_total_mass - ordinary_total_mass,
        "terminal": refined_terminal_mass - ordinary_terminal_mass,
        "recursive": refined_recursive_mass - ordinary_recursive_mass,
    }
    observed_delta_hashes = {
        key: fraction_hash(value) for key, value in refinement_deltas.items()
    }
    if observed_delta_hashes != EXPECTED_REFINEMENT_DELTA_HASHES:
        raise AssertionError(
            f"refinement mass delta hashes changed: {observed_delta_hashes}"
        )

    ratios = {
        "first_terminal_share": (
            Fraction(profiles["first"]["terminal_mass"]["fraction"])
            / Fraction(profiles["first"]["total_mass"]["fraction"])
        ),
        "historical_recursive_over_first_recursive": (
            historical_recursive_mass / first_recursive_mass
        ),
        "corrected_recursive_over_first_recursive": (
            ordinary_recursive_mass / first_recursive_mass
        ),
        "refined_recursive_over_first_recursive": (
            refined_recursive_mass / first_recursive_mass
        ),
        "refinement_recursive_reduction_share": (
            (ordinary_recursive_mass - refined_recursive_mass)
            / ordinary_recursive_mass
        ),
    }

    output = {
        "schema": "first_frontier_terminal_correction_certificate_v1",
        "terminal_parent_indices": list(terminal_indices),
        "counts": observed_counts,
        "family_hashes": observed_hashes,
        "profiles": profiles,
        "historical_minus_corrected": {
            key: mass_record(value)
            for key, value in historical_minus_corrected.items()
        },
        "refinement_deltas": {
            key: mass_record(value) for key, value in refinement_deltas.items()
        },
        "ratios": {key: mass_record(value) for key, value in ratios.items()},
        "raw_refinement_invariants": {
            "support_preserved": True,
            "occurrences_preserved": True,
            "harmonic_occurrence_mass_preserved": True,
        },
        "propagation_metrics": propagation_metrics,
        "refined_retention_metrics": retention_metrics,
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["certificate_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
