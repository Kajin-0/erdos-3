#!/usr/bin/env python3
"""Certify the fifth retained generation and repeated-root reserve no-go."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from probe_fourth_generation_potential_frontier import (
    collision_details,
    terminal_point_records,
)
from probe_generation_aware_feature_profiles import (
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

EXPECTED_METRICS = {
    "raw_occurrences": 246,
    "raw_occurrence_points": 2_972,
    "exact_state_classes": 95,
    "conflict_edges": 366,
    "conflict_components": 17,
    "largest_conflict_component": 17,
    "components_with_nonunique_optimum": 0,
    "retained_states": 21,
    "retained_points": 1_032,
    "terminal_states": 8,
    "terminal_points": 17,
    "recursive_states": 13,
    "recursive_points": 1_015,
}
EXPECTED_HASHES = {
    "fifth_retained_family": "8e7be92c96f0643f85d5a819c0991eab994134dba37ca56683c7d632aab4bc4e",
    "fifth_terminal_family": "0ae08580e03148740e82eb0d9b5afb0775dcdd1fea3e5b6c6c8893db27b639af",
    "fifth_recursive_family": "7335c3e6111ce0225098f3fc769fb67592c942caf0c21a6481fce731aff1dc99",
    "generation4_current_mass": "03cac9573c3d61ac9c8a0c4066cbb8d6ea9ece01606602cacc9604634f9b1ba9",
    "generation5_current_mass": "90efd54b32c03599ff6243202ab3c7b33ab66eb5d4049e690d4a011e414e5300",
    "generation45_ratio": "8d55faef41edb883a3d2d229690ef16db69bd1be23f85871c21c3206319e0534",
    "terminal_up_collisions": "adeef159ec4b09fbbabf22e6aaf1917d1e9f48b7e9614816813efcea9fdde442",
    "numerical_terminal": "d5a4cb25339c69f24fc0482c31076219314bf0f7be1e2726d3ae1f9ba8d47ee4",
    "numerical_recursive": "ac78974926fa679c4121afc7bdb6f16aabd49f6a8de9b409ff78d8a6f7fca771",
    "state_regeneration": "7ce58f2e7bccae1c8636fc1a6ef19cf7655eedf090c49b7b9e2d9ad8e0f888bc",
}
CERTIFICATE_SHA256 = "74120626dcf65e06beae044f37ff570be8113c494ab81ad3bdeba3aa67378bfb"


def assert_between(value: Fraction, lower: Fraction, upper: Fraction, name: str) -> None:
    if not lower < value < upper:
        raise AssertionError(f"{name} outside exact bracket: {value}")


def build_certificate() -> str:
    retained_first, retained_second = reconstruct_retained_families()
    terminal_second = tuple(
        state for state in retained_second if not contains_three_term_ap(state.values)
    )
    recursive_second = tuple(
        state for state in retained_second if contains_three_term_ap(state.values)
    )
    _occ3, retained_third, _metrics3, _rows3 = propagate_recursive_states(recursive_second)
    terminal_third = tuple(
        state for state in retained_third if not contains_three_term_ap(state.values)
    )
    recursive_third = tuple(
        state for state in retained_third if contains_three_term_ap(state.values)
    )
    _occ4, retained_fourth, _metrics4, _rows4 = propagate_recursive_states(recursive_third)
    terminal_fourth = tuple(
        state for state in retained_fourth if not contains_three_term_ap(state.values)
    )
    recursive_fourth = tuple(
        state for state in retained_fourth if contains_three_term_ap(state.values)
    )
    _occ5, retained_fifth, metrics5, _rows5 = propagate_recursive_states(recursive_fourth)
    terminal_fifth = tuple(
        state for state in retained_fifth if not contains_three_term_ap(state.values)
    )
    recursive_fifth = tuple(
        state for state in retained_fifth if contains_three_term_ap(state.values)
    )

    observed = {
        **{key: metrics5[key] for key in (
            "raw_occurrences", "raw_occurrence_points", "exact_state_classes",
            "conflict_edges", "conflict_components", "largest_conflict_component",
            "components_with_nonunique_optimum", "retained_states", "retained_points",
        )},
        "terminal_states": len(terminal_fifth),
        "terminal_points": sum(len(state.values) for state in terminal_fifth),
        "recursive_states": len(recursive_fifth),
        "recursive_points": sum(len(state.values) for state in recursive_fifth),
    }
    if observed != EXPECTED_METRICS:
        raise AssertionError(f"fifth-generation metric mismatch: {observed!r}")

    observed_family_hashes = {
        "fifth_retained_family": canonical_hash(state_records(retained_fifth)),
        "fifth_terminal_family": canonical_hash(state_records(terminal_fifth)),
        "fifth_recursive_family": canonical_hash(state_records(recursive_fifth)),
    }
    for name, value in observed_family_hashes.items():
        if value != EXPECTED_HASHES[name]:
            raise AssertionError(f"{name} hash mismatch: {value}")

    profile4 = feature_profile(point_rows(recursive_fourth, generation=4))
    profile5 = feature_profile(point_rows(recursive_fifth, generation=5))
    if fraction_hash(profile4["current_mass"]) != EXPECTED_HASHES["generation4_current_mass"]:
        raise AssertionError("generation4 current-mass hash mismatch")
    if fraction_hash(profile5["current_mass"]) != EXPECTED_HASHES["generation5_current_mass"]:
        raise AssertionError("generation5 current-mass hash mismatch")
    if profile4["root_repeat_descendant_mass"] != 0 or profile5["root_repeat_descendant_mass"] != 0:
        raise AssertionError("repeated-root reserve did not vanish at both endpoints")
    ratio45 = profile5["current_mass"] / profile4["current_mass"]
    if fraction_hash(ratio45) != EXPECTED_HASHES["generation45_ratio"]:
        raise AssertionError("generation45 ratio hash mismatch")
    assert_between(
        ratio45,
        Fraction(1_329_813, 1_000_000),
        Fraction(664_907, 500_000),
        "generation45 ratio",
    )

    prior_terminal_records = (
        terminal_point_records(terminal_second, 2)
        + terminal_point_records(terminal_third, 3)
        + terminal_point_records(terminal_fourth, 4)
    )
    fifth_terminal_records = terminal_point_records(terminal_fifth, 5)
    fifth_recursive_records = terminal_point_records(recursive_fifth, 5)
    up_terminal = collision_details(prior_terminal_records, fifth_terminal_records, "u_p")
    up_recursive = collision_details(prior_terminal_records, fifth_recursive_records, "u_p")
    upi_terminal = collision_details(prior_terminal_records, fifth_terminal_records, "u_p_i")
    upi_recursive = collision_details(prior_terminal_records, fifth_recursive_records, "u_p_i")
    upis_terminal = collision_details(prior_terminal_records, fifth_terminal_records, "u_p_i_source")
    upis_recursive = collision_details(prior_terminal_records, fifth_recursive_records, "u_p_i_source")
    observed_up = [row["signature"] for row in up_terminal]
    expected_up = [[122, 1_584_351], [123, 1_584_352]]
    if observed_up != expected_up or up_recursive:
        raise AssertionError(f"fifth (u,p) collision mismatch: {observed_up!r}")
    if canonical_hash(observed_up) != EXPECTED_HASHES["terminal_up_collisions"]:
        raise AssertionError("fifth (u,p) collision hash mismatch")
    if upi_terminal or upi_recursive or upis_terminal or upis_recursive:
        raise AssertionError("refined token collision through generation five")

    prior_terminal_values = {int(row["u"]) for row in prior_terminal_records}
    numerical_terminal = sorted(prior_terminal_values & state_values(terminal_fifth))
    numerical_recursive = sorted(prior_terminal_values & state_values(recursive_fifth))
    prior_terminal_states = (
        state_value_sets(terminal_second)
        | state_value_sets(terminal_third)
        | state_value_sets(terminal_fourth)
    )
    regenerated_states = sorted(prior_terminal_states & state_value_sets(retained_fifth))
    observed_numerical = {
        "numerical_terminal": canonical_hash(numerical_terminal),
        "numerical_recursive": canonical_hash(numerical_recursive),
        "state_regeneration": canonical_hash(regenerated_states),
    }
    if len(numerical_terminal) != 16 or len(numerical_recursive) != 34 or len(regenerated_states) != 7:
        raise AssertionError("fifth numerical recreation count mismatch")
    for name, value in observed_numerical.items():
        if value != EXPECTED_HASHES[name]:
            raise AssertionError(f"{name} hash mismatch")

    lines = [
        "FIFTH-GENERATION REPEATED-ROOT NO-GO",
        "",
        "policy=local37_then_lexicographic_recursive_only",
        "retention=global_exact_duplicate_quotient_plus_maximum_harmonic_same_shell_independent_set",
        "",
        "generation4_recursive_states=12",
        "generation4_recursive_points=1717",
        "generation5_raw_occurrences=246",
        "generation5_raw_occurrence_points=2972",
        "generation5_exact_state_classes=95",
        "generation5_conflict_edges=366",
        "generation5_conflict_components=17",
        "generation5_largest_conflict_component=17",
        "generation5_components_with_nonunique_optimum=0",
        "generation5_retained_states=21",
        "generation5_retained_points=1032",
        "generation5_terminal_states=8",
        "generation5_terminal_points=17",
        "generation5_recursive_states=13",
        "generation5_recursive_points=1015",
        "",
        "generation4_root_repeat_descendant_mass=0",
        "generation5_root_repeat_descendant_mass=0",
        f"generation4_current_mass_sha256={EXPECTED_HASHES['generation4_current_mass']}",
        f"generation5_current_mass_sha256={EXPECTED_HASHES['generation5_current_mass']}",
        "generation5_over_generation4_recursive_mass_bracket=1329813/1000000,664907/500000",
        f"generation5_over_generation4_recursive_mass_sha256={EXPECTED_HASHES['generation45_ratio']}",
        "",
        "finite_coefficient_repeated_root_potential_can_contract=False",
        "reason=Delta_root_repeat_descendant_mass_is_zero_and_Delta_current_mass_is_positive",
        "coefficient_74_ratio_bracket=1329813/1000000,664907/500000",
        "coefficient_74_strict_contraction=False",
        "",
        "terminal_u_p_collisions=2",
        "terminal_u_p_collision_signatures=(122,1584351);(123,1584352)",
        "terminal_u_p_i_collisions=0",
        "terminal_u_p_i_source_collisions=0",
        "numerical_terminal_recreation_count=16",
        "numerical_recursive_recreation_count=34",
        "exact_terminal_state_regeneration_count=7",
        "",
        "conclusion: the four-generation sparse witness H+74R fails at generation five.",
        "More strongly, every finite H+kappa*R potential fails on the generation4-to-generation5 transition because R is zero at both endpoints while H increases.",
        "The immediate-provenance terminal signature (u,p,i) remains collision-free through generation five.",
        "This is a fixed-policy, fixed-retention finite no-go theorem.",
        "",
    ]
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_fifth_generation_feature_frontier.py [OUTPUT]")
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print("certificate_sha256=" + CERTIFICATE_SHA256)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
