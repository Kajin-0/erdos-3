#!/usr/bin/env python3
"""Certify two finite generation-aware retained potentials exactly."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from probe_generation_aware_feature_profiles import (
    FEATURE_NAMES,
    feature_profile,
    fraction_hash,
    point_rows,
    single_feature_interval,
)
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED_COUNTS = {
    "generation1_retained": (21, 11_753),
    "generation2_recursive": (14, 7_882),
    "generation3_recursive": (14, 4_789),
}
EXPECTED_FEATURE_HASHES = {
    "generation1_retained": {
        "current_mass": "29f9f139dcdf764a486022f152d7ab0cacc8f40cd4af353f4a5e5f6bea843446",
        "root_repeat_descendant_mass": "543d8bd71c223f034a1c2e02636888caa509e72203d9199a0ca982aad096b975",
        "immediate_tail_ge4_descendant_mass": "ab3ebd705645c19d14fe9715c5658421f59a5e3e01ba3393cadf4fdf6d846499",
    },
    "generation2_recursive": {
        "current_mass": "539dfbe1e345d4e6f1e0ed1c08cfedd1eba8c3f9d195fc078ae9ac0d5e391775",
        "root_repeat_descendant_mass": "b990ee4d972d408a1775b2e62adc5c1e58d3d8737b7486a8a92a00d376bda690",
        "immediate_tail_ge4_descendant_mass": "36d46dd437435683d277d7bc538ac2eb08ff82bcc1adb71b116181b88df1d288",
    },
    "generation3_recursive": {
        "current_mass": "ea01006a6cee2ea0c2cb23704e253b5871c528357b3698b4ca2076ddc7233210",
        "root_repeat_descendant_mass": "66810024432052aa1d66120407feeeca0f551553805400f6f9a0910b81a963b9",
        "immediate_tail_ge4_descendant_mass": "7832a2e6e15f94ba05e176523037f84367f966e45f79d067bf760ba214f0620b",
    },
}
EXPECTED_FEASIBLE = (
    "immediate_tail_ge4_descendant_mass",
    "root_occurrence_mass",
    "root_repeat_descendant_mass",
    "root_repeat_occurrence_mass",
)
EXPECTED_INFEASIBLE = (
    "immediate_depth_charge",
    "immediate_occurrence_mass",
    "immediate_repeat_descendant_mass",
    "immediate_repeat_occurrence_mass",
    "root_depth_charge",
    "root_tail_ge4_descendant_mass",
    "root_tail_ge8_descendant_mass",
)
EXPECTED_QUANTITY_HASHES = {
    "root_repeat_descendant_weight_2": {
        "generation1": "1951c62fa974c03d3a147308d1cee742fc54ae4bc3d022b31d5be9ee7306fd1b",
        "generation2": "11145c7be0217c0949a12d851df828fd46fdeecad63060ce95dc6adc1e548f01",
        "generation3": "6a9cf1cd77f7e61014c7e5b10534e6edbeaecc92376d760189c39ce1608caf1f",
        "delta12": "77bf8bac2c90b7f46116774b32bef5562936640f5732be30b9a9f83794d3e17b",
        "delta23": "0e32ac13269c4d300cd60c1e90617c0d19becec6a70a98d4e05a7b5d2c9de9c9",
        "ratio12": "12ea249dde6274be7aa5d50eb0a0d358cafe3736b117134b91181569de90a4ca",
        "ratio23": "041db455062715d6c7c6dc401dff43b9798b8886a2fc94b090d951c7aacec80c",
        "ratio13": "7ef1a268f1d3c45e1eb61fd86e1df9c58835b6af45b25845a6b702a558a96fd3",
        "margin12": "116b7f5fff2136fc5c6a43c4c96cce5cc91d5f7516ca44341049a51b33e09641",
        "margin23": "755c220ede3cc45f554f1edb28706568fd99b5620159c655b96d4fa562beb9b1",
    },
    "immediate_tail_ge4_weight_4": {
        "generation1": "0c07ecf90ec48c2cfe871c6fffda3de55eeee0a3f47df4c719991cae8fbaeba8",
        "generation2": "a4f69bb95c5cc52ba2bda5e5ab3d4cb048e0b359fad091f46a91828afdbd8b02",
        "generation3": "fc4313c41049a997bfc59ed34b38b1fd6449c5597cc920242b093356882a2899",
        "delta12": "864095dca241e77cfe900749a7e26aec2f71a26e3166c941b8964d3eeb0e06de",
        "delta23": "073bbfd3af2a0de6e4b4fe5258f3cb873e850d7c6909e546fa4b7c5df9c870d7",
        "ratio12": "83ee7dcb725ba6fdaa12d1e3256d26e8f458db05b5603257cc681ebb3afabe54",
        "ratio23": "4308e21de477e431ca7925c04129c1a89cbc9166b68e0422e84088a0b5f1559e",
        "ratio13": "367697aa64f0853913fe877ba6574efa72582b9589b6eff878ec04d4c3c538ad",
        "margin12": "b3dff480e89443e905c69f40193efa296ee2e875af7e5f03dcccc9a7ff9b2bbe",
        "margin23": "6b0f73dda1c41dbd43abd1673e5537c68da8f66a98066a378a013dbb06158e09",
    },
}
CERTIFICATE_SHA256 = "0e1b81e3562990e6071db64c4d6544aab1bb0c78aaae08eee780f3f9d6f81063"


def assert_between(value: Fraction, lower: Fraction, upper: Fraction, name: str) -> None:
    if not lower < value < upper:
        raise AssertionError(f"{name} outside exact bracket: {value}")


def candidate_quantities(
    profiles: dict[str, dict[str, Fraction]],
    feature: str,
    coefficient: int,
) -> dict[str, Fraction]:
    generation1 = profiles["generation1_retained"]["current_mass"] + coefficient * profiles["generation1_retained"][feature]
    generation2 = profiles["generation2_recursive"]["current_mass"] + coefficient * profiles["generation2_recursive"][feature]
    generation3 = profiles["generation3_recursive"]["current_mass"] + coefficient * profiles["generation3_recursive"][feature]
    ratio12 = generation2 / generation1
    ratio23 = generation3 / generation2
    ratio13 = generation3 / generation1
    return {
        "generation1": generation1,
        "generation2": generation2,
        "generation3": generation3,
        "delta12": generation2 - generation1,
        "delta23": generation3 - generation2,
        "ratio12": ratio12,
        "ratio23": ratio23,
        "ratio13": ratio13,
        "margin12": 1 - ratio12,
        "margin23": 1 - ratio23,
    }


def build_certificate() -> str:
    retained_first, retained_second = reconstruct_retained_families()
    recursive_second = tuple(
        state for state in retained_second
        if contains_three_term_ap(state.values)
    )
    _occurrences, retained_third, _metrics, _child_rows = propagate_recursive_states(
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
    observed_counts = {
        name: (len(states), sum(len(state.values) for state in states))
        for name, states in families.items()
    }
    if observed_counts != EXPECTED_COUNTS:
        raise AssertionError(f"family-count mismatch: {observed_counts!r}")

    profiles = {
        name: feature_profile(point_rows(states, generation=index))
        for index, (name, states) in enumerate(families.items(), start=1)
    }
    for generation, expected in EXPECTED_FEATURE_HASHES.items():
        observed = {
            feature: fraction_hash(profiles[generation][feature])
            for feature in expected
        }
        if observed != expected:
            raise AssertionError(f"feature hash mismatch for {generation}")

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
    intervals = {
        feature: single_feature_interval(
            differences["generation2_minus_generation1"]["current_mass"],
            differences["generation3_minus_generation2"]["current_mass"],
            differences["generation2_minus_generation1"][feature],
            differences["generation3_minus_generation2"][feature],
        )
        for feature in FEATURE_NAMES
        if feature != "current_mass"
    }
    feasible = tuple(sorted(feature for feature, row in intervals.items() if row["feasible"]))
    infeasible = tuple(sorted(feature for feature, row in intervals.items() if not row["feasible"]))
    if feasible != EXPECTED_FEASIBLE or infeasible != EXPECTED_INFEASIBLE:
        raise AssertionError("single-feature feasibility classification mismatch")

    primary = candidate_quantities(
        profiles, "root_repeat_descendant_mass", 2
    )
    secondary = candidate_quantities(
        profiles, "immediate_tail_ge4_descendant_mass", 4
    )
    for name, quantities in (
        ("root_repeat_descendant_weight_2", primary),
        ("immediate_tail_ge4_weight_4", secondary),
    ):
        observed = {key: fraction_hash(value) for key, value in quantities.items()}
        if observed != EXPECTED_QUANTITY_HASHES[name]:
            raise AssertionError(f"candidate quantity hash mismatch: {name}")
        if quantities["delta12"] >= 0 or quantities["delta23"] >= 0:
            raise AssertionError(f"candidate is not strictly decreasing: {name}")

    assert_between(primary["ratio12"], Fraction(145_059, 200_000), Fraction(45_331, 62_500), "primary ratio12")
    assert_between(primary["ratio23"], Fraction(939_443, 1_000_000), Fraction(234_861, 250_000), "primary ratio23")
    assert_between(primary["ratio13"], Fraction(681_373, 1_000_000), Fraction(340_687, 500_000), "primary ratio13")
    assert_between(primary["margin12"], Fraction(17_169, 62_500), Fraction(54_941, 200_000), "primary margin12")
    assert_between(primary["margin23"], Fraction(15_139, 250_000), Fraction(60_557, 1_000_000), "primary margin23")
    assert_between(secondary["ratio12"], Fraction(40_579, 100_000), Fraction(405_791, 1_000_000), "secondary ratio12")
    assert_between(secondary["ratio23"], Fraction(499_343, 500_000), Fraction(998_687, 1_000_000), "secondary ratio23")
    assert_between(secondary["ratio13"], Fraction(405_257, 1_000_000), Fraction(202_629, 500_000), "secondary ratio13")
    assert_between(secondary["margin12"], Fraction(594_209, 1_000_000), Fraction(59_421, 100_000), "secondary margin12")
    assert_between(secondary["margin23"], Fraction(1_313, 1_000_000), Fraction(657, 500_000), "secondary margin23")

    lines = [
        "GENERATION-AWARE RETAINED POTENTIALS",
        "",
        "policy=local37_then_lexicographic_recursive_only",
        "retention=global_exact_duplicate_quotient_plus_maximum_harmonic_same_shell_independent_set",
        "",
        "generation1_retained_states=21",
        "generation1_retained_points=11753",
        "generation2_recursive_states=14",
        "generation2_recursive_points=7882",
        "generation3_recursive_states=14",
        "generation3_recursive_points=4789",
        "",
        "single_feature_screen_current_mass_coefficient=1",
        "single_feature_screen_tested_features=11",
        "single_feature_screen_feasible_features=immediate_tail_ge4_descendant_mass,root_occurrence_mass,root_repeat_descendant_mass,root_repeat_occurrence_mass",
        "single_feature_screen_infeasible_features=immediate_depth_charge,immediate_occurrence_mass,immediate_repeat_descendant_mass,immediate_repeat_occurrence_mass,root_depth_charge,root_tail_ge4_descendant_mass,root_tail_ge8_descendant_mass",
        "",
        "primary_potential=H_current+2*H_current_on_repeated_root_provenance",
        f"primary_generation1_sha256={EXPECTED_QUANTITY_HASHES['root_repeat_descendant_weight_2']['generation1']}",
        f"primary_generation2_sha256={EXPECTED_QUANTITY_HASHES['root_repeat_descendant_weight_2']['generation2']}",
        f"primary_generation3_sha256={EXPECTED_QUANTITY_HASHES['root_repeat_descendant_weight_2']['generation3']}",
        "primary_ratio12_bracket=145059/200000,45331/62500",
        "primary_ratio23_bracket=939443/1000000,234861/250000",
        "primary_ratio13_bracket=681373/1000000,340687/500000",
        "primary_margin12_bracket=17169/62500,54941/200000",
        "primary_margin23_bracket=15139/250000,60557/1000000",
        "primary_strictly_decreasing=True",
        "",
        "secondary_potential=H_current+4*H_current_on_immediate_depth_at_least_4",
        f"secondary_generation1_sha256={EXPECTED_QUANTITY_HASHES['immediate_tail_ge4_weight_4']['generation1']}",
        f"secondary_generation2_sha256={EXPECTED_QUANTITY_HASHES['immediate_tail_ge4_weight_4']['generation2']}",
        f"secondary_generation3_sha256={EXPECTED_QUANTITY_HASHES['immediate_tail_ge4_weight_4']['generation3']}",
        "secondary_ratio12_bracket=40579/100000,405791/1000000",
        "secondary_ratio23_bracket=499343/500000,998687/1000000",
        "secondary_ratio13_bracket=405257/1000000,202629/500000",
        "secondary_margin12_bracket=594209/1000000,59421/100000",
        "secondary_margin23_bracket=1313/1000000,657/500000",
        "secondary_strictly_decreasing=True",
        "",
        "conclusion: two simple nonnegative generation-aware potentials decrease across both recorded recursive transitions.",
        "The repeated-root descendant potential with coefficient 2 contracts by 27.4704%-27.4705% and then 6.0556%-6.0557%.",
        "The immediate-depth-tail potential with coefficient 4 contracts strongly on the first transition and by 0.1313%-0.1314% on the second.",
        "These are exact fixed-policy, fixed-retention three-generation witnesses, not universal Bellman potentials.",
        "",
    ]
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_generation_aware_retained_potentials.py [OUTPUT]")
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print("certificate_sha256=" + CERTIFICATE_SHA256)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
