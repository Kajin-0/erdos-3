#!/usr/bin/env python3
"""Certify fourth-generation retained output, potential failure, and token survival."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from probe_fourth_generation_potential_frontier import (
    collision_details,
    potential_quantities,
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
    state_tokens,
    state_value_sets,
    state_values,
)
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
sys.setrecursionlimit(30_000)

EXPECTED_METRICS = {
    "recursive_second_parent_states": 14,
    "recursive_second_parent_points": 4_789,
    "child_selected_actions": 4_120,
    "child_terminal_residual_points": 669,
    "raw_occurrences": 408,
    "raw_occurrence_points": 8_807,
    "exact_state_classes": 103,
    "conflict_edges": 407,
    "conflict_components": 20,
    "largest_conflict_component": 17,
    "components_with_nonunique_optimum": 0,
    "dp_states_examined": 126,
    "retained_states": 23,
    "retained_points": 1_794,
}
EXPECTED_SPLIT = {
    "terminal_states": 11,
    "terminal_points": 77,
    "recursive_states": 12,
    "recursive_points": 1_717,
}
EXPECTED_FEATURE_HASHES = {
    "current_mass": "03cac9573c3d61ac9c8a0c4066cbb8d6ea9ece01606602cacc9604634f9b1ba9",
    "root_repeat_descendant_mass": "a93875fe509ac2fae0e0939d3ec71c4d978244c7398dd7185ca68c393426a5a6",
    "immediate_tail_ge4_descendant_mass": "bd15677ca84a8944d52f276ae3587b2b92d4344e4bfc4db1c04b674fe7623d62",
}
EXPECTED_HASHES = {
    "child_transition_summary": "e868c32e2fefb685dbd3a514a3d345b76651e44da1a8fa8db91d3277feb1cab8",
    "fourth_raw_occurrences": "3779c87338136c33faa782a0cb37c48e7f76ac4935307dffaa42a10557417b18",
    "fourth_retained_family": "0a07682c357a189d75a592b72e1f3df67371d6eca38fa3cb4be4690d780e5129",
    "fourth_terminal_family": "f0dfdff932b1746d2678b466eac6266dca3c0103ba5c6b00e03d35a993903b1b",
    "fourth_recursive_family": "19a6afd4fa54c7af7e91b8241366c34db3d15cefadba470e2a897746c9d1bc25",
    "fourth_terminal_tokens": "88869f3a08f48bbea69de13d98a48c2cf91bad34285e2c0ed049f30e298522f8",
    "fourth_recursive_tokens": "79092f11822890b8bc19bc536351ca1b040eaff32b3a48d67dffb946b1912a20",
}
EXPECTED_RATIO_HASHES = {
    "fourth_total_over_third_recursive": "a2c62ce7a02037a7ff3910dddb932e3b6a97fc38fcc4198f5d73b6a6dd4428ac",
    "fourth_terminal_over_fourth_total": "af2bd88697e044610a2cc3d30fe6fdaf81409b479fecc098e75904697b8645cc",
    "fourth_recursive_over_fourth_total": "f8f5484e507a9a6e8d4cf4e08b6efa903b7ff40c25c588450970a42f5af19553",
    "fourth_recursive_over_third_recursive": "5dc632de3dd681a5dfa9f0e01de3303735873f922cf34d0dc6e6231ccec03c66",
}
EXPECTED_POTENTIAL_HASHES = {
    "primary_generation4": "03cac9573c3d61ac9c8a0c4066cbb8d6ea9ece01606602cacc9604634f9b1ba9",
    "primary_delta34": "6f1c3aede9e643b58953ba8c350533172976aadcee02fe182c27ddfd430ed782",
    "primary_ratio34": "5b31d5d9232ac157d2c760bee5ff7b685515198522b51e63db50feb4a388de5b",
    "secondary_generation4": "77b432097d16359afe45c1a8efc4575002da6b8ad168e0e2dd01a492e53d59e8",
    "secondary_delta34": "111647e4e9372cb7c55d5b0908290b52d654dc6a9bcf368dc4966cd6f40a03b4",
    "secondary_ratio34": "c19f9d7acea812d6f235f8026b35597c835b4b87c6c934c522165780767008d3",
}
EXPECTED_UP_COLLISIONS = (
    (61, 1_584_290),
    (62, 1_584_291),
    (122, 1_584_351),
    (123, 1_584_352),
    (147, 1_584_356),
    (152, 1_584_361),
    (153, 1_584_362),
)
EXPECTED_NUMERICAL_HASHES = {
    "terminal_values": "2ffd618af868420ee1af41c9edb6cab743d2a8f605f2e64ea3d9fcbf3da12090",
    "recursive_values": "c59425de5653c68ae3de1e752416e0580510c9f4f143ba18180b20b0d44d4ee5",
    "state_regeneration": "9bc4a2141040924f2eb96274ad456e82d74adb370c8990b75ebbee84cc743c8a",
}
CERTIFICATE_SHA256 = "2c2f2103de57bd8fdcc4c32448ea9e1cf662b325e590da5e1b0758c62298c9e5"


def assert_between(value: Fraction, lower: Fraction, upper: Fraction, name: str) -> None:
    if not lower < value < upper:
        raise AssertionError(f"{name} outside exact bracket: {value}")


def build_certificate() -> str:
    retained_first, retained_second = reconstruct_retained_families()
    terminal_second = tuple(
        state for state in retained_second
        if not contains_three_term_ap(state.values)
    )
    recursive_second = tuple(
        state for state in retained_second
        if contains_three_term_ap(state.values)
    )
    _occurrences3, retained_third, _metrics3, _child_rows3 = (
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
    if metrics4 != EXPECTED_METRICS:
        raise AssertionError(f"fourth-generation metric mismatch: {metrics4!r}")
    observed_split = {
        "terminal_states": len(terminal_fourth),
        "terminal_points": sum(len(state.values) for state in terminal_fourth),
        "recursive_states": len(recursive_fourth),
        "recursive_points": sum(len(state.values) for state in recursive_fourth),
    }
    if observed_split != EXPECTED_SPLIT:
        raise AssertionError(f"fourth-generation split mismatch: {observed_split!r}")
    if sum(len(state.values) for state in retained_fourth) != len(state_values(retained_fourth)):
        raise AssertionError("fourth-generation retained family is not point-disjoint")

    profile3 = feature_profile(point_rows(recursive_third, generation=3))
    profile4 = feature_profile(point_rows(recursive_fourth, generation=4))
    observed_feature_hashes = {
        feature: fraction_hash(profile4[feature])
        for feature in EXPECTED_FEATURE_HASHES
    }
    if observed_feature_hashes != EXPECTED_FEATURE_HASHES:
        raise AssertionError("fourth-generation feature hash mismatch")

    profiles = {
        "generation1_retained": feature_profile(point_rows(retained_first, generation=1)),
        "generation2_recursive": feature_profile(point_rows(recursive_second, generation=2)),
        "generation3_recursive": profile3,
        "generation4_recursive": profile4,
    }
    primary = potential_quantities(profiles, "root_repeat_descendant_mass", 2)
    secondary = potential_quantities(profiles, "immediate_tail_ge4_descendant_mass", 4)
    observed_potential_hashes = {
        "primary_generation4": fraction_hash(primary["generation4_recursive"]),
        "primary_delta34": fraction_hash(primary["delta34"]),
        "primary_ratio34": fraction_hash(primary["ratio34"]),
        "secondary_generation4": fraction_hash(secondary["generation4_recursive"]),
        "secondary_delta34": fraction_hash(secondary["delta34"]),
        "secondary_ratio34": fraction_hash(secondary["ratio34"]),
    }
    if observed_potential_hashes != EXPECTED_POTENTIAL_HASHES:
        raise AssertionError("fourth-generation potential hash mismatch")
    if primary["delta34"] <= 0 or secondary["delta34"] <= 0:
        raise AssertionError("a fourth-generation candidate unexpectedly contracts")
    if profile4["root_repeat_descendant_mass"] != 0:
        raise AssertionError("fourth repeated-root descendant reserve is nonzero")
    assert_between(primary["ratio34"], Fraction(677_977, 250_000), Fraction(2_711_909, 1_000_000), "primary ratio34")
    assert_between(secondary["ratio34"], Fraction(963_661, 100_000), Fraction(9_636_611, 1_000_000), "secondary ratio34")

    third_recursive_mass = profile3["current_mass"]
    fourth_recursive_mass = profile4["current_mass"]
    fourth_terminal_mass = sum((state.weight for state in terminal_fourth), Fraction())
    fourth_total_mass = fourth_terminal_mass + fourth_recursive_mass
    ratios = {
        "fourth_total_over_third_recursive": fourth_total_mass / third_recursive_mass,
        "fourth_terminal_over_fourth_total": fourth_terminal_mass / fourth_total_mass,
        "fourth_recursive_over_fourth_total": fourth_recursive_mass / fourth_total_mass,
        "fourth_recursive_over_third_recursive": fourth_recursive_mass / third_recursive_mass,
    }
    if {name: fraction_hash(value) for name, value in ratios.items()} != EXPECTED_RATIO_HASHES:
        raise AssertionError("fourth-generation mass ratio hash mismatch")
    assert_between(ratios["fourth_total_over_third_recursive"], Fraction(6_996_249, 1_000_000), Fraction(5_597, 800), "fourth total ratio")
    assert_between(ratios["fourth_terminal_over_fourth_total"], Fraction(592_741, 1_000_000), Fraction(296_371, 500_000), "fourth terminal share")
    assert_between(ratios["fourth_recursive_over_fourth_total"], Fraction(203_629, 500_000), Fraction(407_259, 1_000_000), "fourth recursive share")
    assert_between(ratios["fourth_recursive_over_third_recursive"], Fraction(2_849_279, 1_000_000), Fraction(8_904, 3_125), "fourth recursive ratio")

    root_counts = {}
    immediate_counts = {}
    for state in recursive_fourth:
        for root in state.representative.provenance:
            root_counts[root] = root_counts.get(root, 0) + 1
        for immediate in state.representative.immediate_provenance:
            immediate_counts[immediate] = immediate_counts.get(immediate, 0) + 1
    if len(root_counts) != 1_717 or max(root_counts.values()) != 1:
        raise AssertionError("fourth root provenance multiplicity mismatch")
    if len(immediate_counts) != 1_717 or max(immediate_counts.values()) != 1:
        raise AssertionError("fourth immediate provenance multiplicity mismatch")

    prior_terminal_records = terminal_point_records(terminal_second, 2) + terminal_point_records(terminal_third, 3)
    fourth_terminal_records = terminal_point_records(terminal_fourth, 4)
    fourth_recursive_records = terminal_point_records(recursive_fourth, 4)
    up_terminal = collision_details(prior_terminal_records, fourth_terminal_records, "u_p")
    up_recursive = collision_details(prior_terminal_records, fourth_recursive_records, "u_p")
    upi_terminal = collision_details(prior_terminal_records, fourth_terminal_records, "u_p_i")
    upi_recursive = collision_details(prior_terminal_records, fourth_recursive_records, "u_p_i")
    upis_terminal = collision_details(prior_terminal_records, fourth_terminal_records, "u_p_i_source")
    upis_recursive = collision_details(prior_terminal_records, fourth_recursive_records, "u_p_i_source")
    observed_up = tuple(sorted(tuple(detail["signature"]) for detail in up_terminal))
    if observed_up != EXPECTED_UP_COLLISIONS or up_recursive:
        raise AssertionError("fourth (u,p) collision set mismatch")
    if upi_terminal or upi_recursive or upis_terminal or upis_recursive:
        raise AssertionError("refined terminal token collides through generation four")
    if canonical_hash([list(row) for row in observed_up]) != "805e6d77c44f7301ccf4d8b9e77e2a245e04f242b6abe4acca9008a58d11862d":
        raise AssertionError("fourth (u,p) collision hash mismatch")

    prior_terminal_values = {int(row["u"]) for row in prior_terminal_records}
    terminal_values = sorted(prior_terminal_values & state_values(terminal_fourth))
    recursive_values = sorted(prior_terminal_values & state_values(recursive_fourth))
    prior_states = state_value_sets(terminal_second) | state_value_sets(terminal_third)
    regenerated_states = sorted(prior_states & state_value_sets(retained_fourth))
    if len(terminal_values) != 73 or len(recursive_values) != 31 or len(regenerated_states) != 6:
        raise AssertionError("fourth numerical recreation count mismatch")
    observed_numerical_hashes = {
        "terminal_values": canonical_hash(terminal_values),
        "recursive_values": canonical_hash(recursive_values),
        "state_regeneration": canonical_hash([list(values) for values in regenerated_states]),
    }
    if observed_numerical_hashes != EXPECTED_NUMERICAL_HASHES:
        raise AssertionError("fourth numerical recreation hash mismatch")

    raw_records = [
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
    observed_hashes = {
        "child_transition_summary": canonical_hash(child_rows4),
        "fourth_raw_occurrences": canonical_hash(raw_records),
        "fourth_retained_family": canonical_hash(state_records(retained_fourth)),
        "fourth_terminal_family": canonical_hash(state_records(terminal_fourth)),
        "fourth_recursive_family": canonical_hash(state_records(recursive_fourth)),
        "fourth_terminal_tokens": canonical_hash(sorted([list(row) for row in state_tokens(terminal_fourth)])),
        "fourth_recursive_tokens": canonical_hash(sorted([list(row) for row in state_tokens(recursive_fourth)])),
    }
    if observed_hashes != EXPECTED_HASHES:
        raise AssertionError("fourth-generation family hash mismatch")

    lines = [
        "FOURTH-GENERATION PROVENANCE-RESERVE FRONTIER",
        "",
        "policy=local37_then_lexicographic_recursive_only",
        "retention=global_exact_duplicate_quotient_plus_maximum_harmonic_same_shell_independent_set",
        "",
        "generation3_recursive_parent_states=14",
        "generation3_recursive_parent_points=4789",
        "child_selected_actions=4120",
        "child_terminal_residual_points=669",
        "fourth_generation_raw_occurrences=408",
        "fourth_generation_raw_occurrence_points=8807",
        "fourth_generation_exact_state_classes=103",
        "fourth_generation_conflict_edges=407",
        "fourth_generation_conflict_components=20",
        "fourth_generation_largest_conflict_component=17",
        "fourth_generation_components_with_nonunique_optimum=0",
        "fourth_generation_dp_states_examined=126",
        "",
        "fourth_generation_retained_states=23",
        "fourth_generation_retained_points=1794",
        "fourth_generation_terminal_states=11",
        "fourth_generation_terminal_points=77",
        "fourth_generation_recursive_states=12",
        "fourth_generation_recursive_points=1717",
        "fourth_generation_point_disjoint=True",
        "",
        "fourth_total_over_third_recursive_bracket=6996249/1000000,5597/800",
        "fourth_terminal_over_fourth_total_bracket=592741/1000000,296371/500000",
        "fourth_recursive_over_fourth_total_bracket=203629/500000,407259/1000000",
        "fourth_recursive_over_third_recursive_bracket=2849279/1000000,8904/3125",
        "",
        "fourth_recursive_root_provenance_distinct=1717",
        "fourth_recursive_root_provenance_repeated=0",
        "fourth_recursive_root_provenance_max_multiplicity=1",
        "fourth_recursive_immediate_provenance_distinct=1717",
        "fourth_recursive_immediate_provenance_repeated=0",
        "fourth_recursive_immediate_provenance_max_multiplicity=1",
        "",
        "primary_potential=H_current+2*H_current_on_repeated_root_provenance",
        "primary_fourth_root_repeat_descendant_mass=0",
        "primary_ratio34_bracket=677977/250000,2711909/1000000",
        "primary_strict_fourth_contraction=False",
        "",
        "secondary_potential=H_current+4*H_current_on_immediate_depth_at_least_4",
        "secondary_ratio34_bracket=963661/100000,9636611/1000000",
        "secondary_strict_fourth_contraction=False",
        "",
        "prior_terminal_vs_fourth_u_p_collisions=7",
        "prior_terminal_vs_fourth_u_p_terminal_collisions=7",
        "prior_terminal_vs_fourth_u_p_recursive_collisions=0",
        "prior_terminal_vs_fourth_u_p_i_collisions=0",
        "prior_terminal_vs_fourth_u_p_i_source_collisions=0",
        "u_p_collision_signatures_sha256=805e6d77c44f7301ccf4d8b9e77e2a245e04f242b6abe4acca9008a58d11862d",
        "",
        "fourth_numerical_terminal_recreation_count=73",
        "fourth_numerical_recursive_recreation_count=31",
        "fourth_exact_terminal_state_regeneration_count=6",
        "fourth_numerical_terminal_values_sha256=2ffd618af868420ee1af41c9edb6cab743d2a8f605f2e64ea3d9fcbf3da12090",
        "fourth_numerical_recursive_values_sha256=c59425de5653c68ae3de1e752416e0580510c9f4f143ba18180b20b0d44d4ee5",
        "fourth_exact_state_regeneration_sha256=9bc4a2141040924f2eb96274ad456e82d74adb370c8990b75ebbee84cc743c8a",
        "",
        f"fourth_retained_family_sha256={EXPECTED_HASHES['fourth_retained_family']}",
        f"fourth_terminal_family_sha256={EXPECTED_HASHES['fourth_terminal_family']}",
        f"fourth_recursive_family_sha256={EXPECTED_HASHES['fourth_recursive_family']}",
        f"fourth_raw_occurrences_sha256={EXPECTED_HASHES['fourth_raw_occurrences']}",
        f"fourth_terminal_tokens_sha256={EXPECTED_HASHES['fourth_terminal_tokens']}",
        f"fourth_recursive_tokens_sha256={EXPECTED_HASHES['fourth_recursive_tokens']}",
        "",
        "conclusion: both three-generation provenance-reserve witnesses fail at the fourth retained recursive generation.",
        "H+2R expands by a factor between 2.711908 and 2.711909 because repeated-root reserve vanishes while raw recursive mass grows.",
        "H+4T expands by a factor between 9.636610 and 9.636611 because the immediate depth-four tail regenerates.",
        "The refined terminal token (u,p,i) has no recorded collision through generation four, while (u,p) has seven terminal collisions.",
        "This is an exact fixed-policy, fixed-retention four-generation no-go and signature-survival theorem.",
        "",
    ]
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_fourth_generation_potential_frontier.py [OUTPUT]")
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print("certificate_sha256=" + CERTIFICATE_SHA256)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
