#!/usr/bin/env python3
"""Certify the third retained generation and terminal-token collision exactly."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from probe_third_generation_recursive_frontier import (
    canonical_hash,
    first_generation_raw_tokens,
    fraction_hash,
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

EXPECTED_METRICS = {
    "recursive_second_parent_states": 14,
    "recursive_second_parent_points": 7_882,
    "child_selected_actions": 6_858,
    "child_terminal_residual_points": 1_024,
    "raw_occurrences": 474,
    "raw_occurrence_points": 14_639,
    "exact_state_classes": 108,
    "conflict_edges": 386,
    "conflict_components": 29,
    "largest_conflict_component": 15,
    "components_with_nonunique_optimum": 0,
    "dp_states_examined": 137,
    "retained_states": 32,
    "retained_points": 4_899,
    "terminal_third_states": 18,
    "terminal_third_points": 110,
    "recursive_third_states": 14,
    "recursive_third_points": 4_789,
    "third_root_provenance_distinct": 4_840,
    "third_root_provenance_repeated": 59,
    "third_root_provenance_max_multiplicity": 2,
}
EXPECTED_HASHES = {
    "child_transition_summary": "68113df9bd71febce4d510139532bafd90686accd594cdcc811aa988779e3173",
    "third_raw_occurrences": "304a230fb27f5d7755032e1fe79fdd38f8b2692a8b615c572e5181da73f7480a",
    "third_retained_family": "099f05089e7e5e27b99dad99eb6a1ee88f4134882c613d317ae416d7381746e8",
    "third_terminal_family": "85df2cd8f67f4a011a2ac38b970c384c89ff07098cc579b4842b6cc63a7109c4",
    "third_recursive_family": "5413108594c47f2f4a549d9ef6658fe7311fc4478b99d6f0bc463355d50d106a",
    "third_all_tokens": "849ba7d47dc60fbed4a62b0548f821a14ee7d5b119e4de60bdca1ead6f3e16af",
    "third_terminal_tokens": "5519a9c96dbdcc08bee919853396808b0edc4db352aba7cacf8c337c1058dfd1",
    "third_recursive_tokens": "d6e91367d85fa1a644db20208d0e7235143ab99446f305a77b233312e81a0ea8",
}
EXPECTED_MASS_HASHES = {
    "first_retained": "29f9f139dcdf764a486022f152d7ab0cacc8f40cd4af353f4a5e5f6bea843446",
    "second_recursive": "539dfbe1e345d4e6f1e0ed1c08cfedd1eba8c3f9d195fc078ae9ac0d5e391775",
    "third_total": "00c7e790b4e4e0bb25c8d3f0d597efe84617ae790a34fbe3e4c5fc7a5942ff0b",
    "third_terminal": "d28a961f10033c83879024fba1e32936f068472708bb5e92eb971f9ee8a260ca",
    "third_recursive": "ea01006a6cee2ea0c2cb23704e253b5871c528357b3698b4ca2076ddc7233210",
}
EXPECTED_RATIO_HASHES = {
    "third_total_over_second_recursive": "36189e373a8a9927c5b9268d381556db22367da5425587436a06a2b53389aca8",
    "third_terminal_over_third_total": "b23699ff40f580b5a45d470136cbf314c57100ee3c005e181b59c21d028e045a",
    "third_recursive_over_third_total": "4c6e98bf775d34abd3698a12b5e8dec804cb1c78e737800623bdda51c3a92258",
    "third_recursive_over_second_recursive": "9b1185a81986e29249785f20682932a1be1b59c0349f4b15670c99a68f5483f4",
    "third_recursive_over_first_retained": "23fc3338217ba11c2169abdf98240920ea4c10ea33e9a95c6f1a008650b30c0d",
}
EXPECTED_NUMERICAL_ALL = (
    1, 5, 10, 16, 21, 60, 61, 62, 65, 81, 86, 87, 92, 122, 123,
    147, 152, 153, 606, 622, 627, 632, 667, 688, 693, 728, 749, 991,
)
EXPECTED_NUMERICAL_TERMINAL = (
    1, 5, 10, 60, 61, 62, 65, 81, 86, 87, 92, 122, 123, 147, 152,
    153, 991,
)
EXPECTED_NUMERICAL_RECURSIVE = (
    16, 21, 606, 622, 627, 632, 667, 688, 693, 728, 749,
)
EXPECTED_STATE_REGENERATION = (
    (1,), (5,), (10,), (60,), (61, 62), (122, 123), (147, 152, 153),
)
CERTIFICATE_SHA256 = "efdd41c014104f328f28c3d13b097335fd2b1730859b74134344329251b135d0"


def point_records(states: tuple[object, ...]) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for state in states:
        representative = state.representative
        for value, root, immediate in zip(
            state.values,
            representative.provenance,
            representative.immediate_provenance,
            strict=True,
        ):
            records.append(
                {
                    "class_index": state.index,
                    "parent_class": representative.parent_class,
                    "source": representative.source,
                    "source_step": representative.source_step,
                    "u": value,
                    "p": root,
                    "immediate": immediate,
                }
            )
    return records


def signature(record: dict[str, object], mode: str) -> tuple[object, ...]:
    if mode == "u_p":
        return (record["u"], record["p"])
    if mode == "u_p_immediate":
        return (record["u"], record["p"], record["immediate"])
    if mode == "u_p_source":
        return (
            record["u"], record["p"], record["source"], record["source_step"]
        )
    raise ValueError(mode)


def shared_signatures(
    earlier: list[dict[str, object]],
    later: list[dict[str, object]],
    mode: str,
) -> set[tuple[object, ...]]:
    return {signature(row, mode) for row in earlier} & {
        signature(row, mode) for row in later
    }


def assert_ratio(
    name: str,
    value: Fraction,
    lower: Fraction,
    upper: Fraction,
) -> None:
    if not lower < value < upper:
        raise AssertionError(f"{name} outside exact bracket: {value}")
    if fraction_hash(value) != EXPECTED_RATIO_HASHES[name]:
        raise AssertionError(f"{name} hash mismatch")


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
    if len(terminal_second) != 13 or len(recursive_second) != 14:
        raise AssertionError("second-generation terminal split changed")

    first_raw_tokens, _first_raw_occurrence_points = first_generation_raw_tokens()
    first_retained_tokens = state_tokens(retained_first)
    second_terminal_tokens = state_tokens(terminal_second)
    second_terminal_values = state_values(terminal_second)
    second_terminal_state_sets = state_value_sets(terminal_second)

    occurrences, retained_third, metrics, child_rows = propagate_recursive_states(
        recursive_second
    )
    terminal_third = tuple(
        state for state in retained_third
        if not contains_three_term_ap(state.values)
    )
    recursive_third = tuple(
        state for state in retained_third
        if contains_three_term_ap(state.values)
    )

    third_all_tokens = state_tokens(retained_third)
    third_terminal_tokens = state_tokens(terminal_third)
    third_recursive_tokens = state_tokens(recursive_third)
    third_all_values = state_values(retained_third)
    third_terminal_values = state_values(terminal_third)
    third_recursive_values = state_values(recursive_third)
    third_state_sets = state_value_sets(retained_third)

    root_counts = Counter(
        root
        for state in retained_third
        for root in state.representative.provenance
    )
    observed_metrics = {
        **metrics,
        "terminal_third_states": len(terminal_third),
        "terminal_third_points": len(third_terminal_values),
        "recursive_third_states": len(recursive_third),
        "recursive_third_points": len(third_recursive_values),
        "third_root_provenance_distinct": len(root_counts),
        "third_root_provenance_repeated": sum(
            multiplicity > 1 for multiplicity in root_counts.values()
        ),
        "third_root_provenance_max_multiplicity": max(root_counts.values()),
    }
    if observed_metrics != EXPECTED_METRICS:
        raise AssertionError(f"third-generation metric mismatch: {observed_metrics!r}")

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
        for row in occurrences
    ]
    observed_hashes = {
        "child_transition_summary": canonical_hash(child_rows),
        "third_raw_occurrences": canonical_hash(raw_records),
        "third_retained_family": canonical_hash(state_records(retained_third)),
        "third_terminal_family": canonical_hash(state_records(terminal_third)),
        "third_recursive_family": canonical_hash(state_records(recursive_third)),
        "third_all_tokens": canonical_hash(
            sorted([list(row) for row in third_all_tokens])
        ),
        "third_terminal_tokens": canonical_hash(
            sorted([list(row) for row in third_terminal_tokens])
        ),
        "third_recursive_tokens": canonical_hash(
            sorted([list(row) for row in third_recursive_tokens])
        ),
    }
    if observed_hashes != EXPECTED_HASHES:
        raise AssertionError("third-generation family or token hash mismatch")

    first_mass = sum((state.weight for state in retained_first), Fraction())
    second_recursive_mass = sum(
        (state.weight for state in recursive_second), Fraction()
    )
    third_total_mass = sum((state.weight for state in retained_third), Fraction())
    third_terminal_mass = sum(
        (state.weight for state in terminal_third), Fraction()
    )
    third_recursive_mass = sum(
        (state.weight for state in recursive_third), Fraction()
    )
    observed_mass_hashes = {
        "first_retained": fraction_hash(first_mass),
        "second_recursive": fraction_hash(second_recursive_mass),
        "third_total": fraction_hash(third_total_mass),
        "third_terminal": fraction_hash(third_terminal_mass),
        "third_recursive": fraction_hash(third_recursive_mass),
    }
    if observed_mass_hashes != EXPECTED_MASS_HASHES:
        raise AssertionError("third-generation mass hash mismatch")

    ratios = {
        "third_total_over_second_recursive": third_total_mass / second_recursive_mass,
        "third_terminal_over_third_total": third_terminal_mass / third_total_mass,
        "third_recursive_over_third_total": third_recursive_mass / third_total_mass,
        "third_recursive_over_second_recursive": (
            third_recursive_mass / second_recursive_mass
        ),
        "third_recursive_over_first_retained": third_recursive_mass / first_mass,
    }
    assert_ratio(
        "third_total_over_second_recursive", ratios["third_total_over_second_recursive"],
        Fraction(4_748_899, 500_000), Fraction(9_497_799, 1_000_000),
    )
    assert_ratio(
        "third_terminal_over_third_total", ratios["third_terminal_over_third_total"],
        Fraction(49_263, 62_500), Fraction(788_209, 1_000_000),
    )
    assert_ratio(
        "third_recursive_over_third_total", ratios["third_recursive_over_third_total"],
        Fraction(211_791, 1_000_000), Fraction(13_237, 62_500),
    )
    assert_ratio(
        "third_recursive_over_second_recursive", ratios["third_recursive_over_second_recursive"],
        Fraction(2_011_553, 1_000_000), Fraction(1_005_777, 500_000),
    )
    assert_ratio(
        "third_recursive_over_first_retained", ratios["third_recursive_over_first_retained"],
        Fraction(235_781, 125_000), Fraction(1_886_249, 1_000_000),
    )
    expansion = ratios["third_recursive_over_second_recursive"] - 1
    if not Fraction(1_011_553, 1_000_000) < expansion < Fraction(505_777, 500_000):
        raise AssertionError("third recursive expansion margin outside bracket")

    if second_terminal_tokens & first_raw_tokens:
        raise AssertionError("second terminal token collides with first raw token")
    if second_terminal_tokens & first_retained_tokens:
        raise AssertionError("second terminal token collides with first retained token")
    if second_terminal_tokens & third_recursive_tokens:
        raise AssertionError("second terminal token recurs in third recursive output")
    if second_terminal_tokens & third_terminal_tokens != {(60, 1_354_490)}:
        raise AssertionError("unexpected terminal (u,p) recreation set")

    numerical_all = tuple(sorted(second_terminal_values & third_all_values))
    numerical_terminal = tuple(sorted(second_terminal_values & third_terminal_values))
    numerical_recursive = tuple(sorted(second_terminal_values & third_recursive_values))
    state_regeneration = tuple(sorted(second_terminal_state_sets & third_state_sets))
    if numerical_all != EXPECTED_NUMERICAL_ALL:
        raise AssertionError("numerical recreation set mismatch")
    if numerical_terminal != EXPECTED_NUMERICAL_TERMINAL:
        raise AssertionError("terminal numerical recreation set mismatch")
    if numerical_recursive != EXPECTED_NUMERICAL_RECURSIVE:
        raise AssertionError("recursive numerical recreation set mismatch")
    if state_regeneration != EXPECTED_STATE_REGENERATION:
        raise AssertionError("exact terminal state regeneration mismatch")

    second_records = point_records(terminal_second)
    third_terminal_records = point_records(terminal_third)
    third_recursive_records = point_records(recursive_third)
    if shared_signatures(second_records, third_recursive_records, "u_p"):
        raise AssertionError("terminal token recurs recursively")
    if shared_signatures(second_records, third_terminal_records, "u_p") != {
        (60, 1_354_490)
    }:
        raise AssertionError("terminal u,p collision mismatch")
    if shared_signatures(second_records, third_terminal_records, "u_p_immediate"):
        raise AssertionError("immediate provenance failed to separate collision")
    if shared_signatures(second_records, third_terminal_records, "u_p_source") != {
        (60, 1_354_490, "middle_fiber", 5)
    }:
        raise AssertionError("source signature collision mismatch")
    earlier = next(
        row for row in second_records
        if (row["u"], row["p"]) == (60, 1_354_490)
    )
    later = next(
        row for row in third_terminal_records
        if (row["u"], row["p"]) == (60, 1_354_490)
    )
    if earlier["immediate"] != 2_810 or later["immediate"] != 440:
        raise AssertionError("collision immediate-provenance values changed")

    lines = [
        "THIRD-GENERATION RECURSIVE FRONTIER",
        "",
        "policy=local37_then_lexicographic_recursive_only",
        "retention=global_exact_duplicate_quotient_plus_maximum_harmonic_same_shell_independent_set",
        "",
        "second_generation_recursive_parent_states=14",
        "second_generation_recursive_parent_points=7882",
        "child_selected_actions=6858",
        "child_terminal_residual_points=1024",
        "third_generation_raw_occurrences=474",
        "third_generation_raw_occurrence_points=14639",
        "third_generation_exact_state_classes=108",
        "third_generation_conflict_edges=386",
        "third_generation_conflict_components=29",
        "third_generation_largest_conflict_component=15",
        "third_generation_components_with_nonunique_optimum=0",
        "third_generation_dp_states_examined=137",
        "",
        "third_generation_retained_states=32",
        "third_generation_retained_points=4899",
        "third_generation_terminal_states=18",
        "third_generation_terminal_points=110",
        "third_generation_recursive_states=14",
        "third_generation_recursive_points=4789",
        "third_generation_point_disjoint=True",
        "",
        "third_total_over_second_recursive_bracket=4748899/500000,9497799/1000000",
        "third_terminal_over_third_total_bracket=49263/62500,788209/1000000",
        "third_recursive_over_third_total_bracket=211791/1000000,13237/62500",
        "third_recursive_over_second_recursive_bracket=2011553/1000000,1005777/500000",
        "third_recursive_over_first_retained_bracket=235781/125000,1886249/1000000",
        "third_recursive_expansion_over_second_bracket=1011553/1000000,505777/500000",
        "",
        "second_terminal_vs_first_raw_token_collisions=0",
        "second_terminal_vs_first_retained_token_collisions=0",
        "second_terminal_vs_third_same_u_p_collisions=1",
        "recreated_u_p_token=60,1354490",
        "recreated_token_generation2_immediate=2810",
        "recreated_token_generation3_immediate=440",
        "recreated_token_source=middle_fiber",
        "recreated_token_source_step=5",
        "second_terminal_vs_third_same_u_p_immediate_collisions=0",
        "second_terminal_vs_third_same_u_p_source_collisions=1",
        "second_terminal_vs_third_recursive_u_p_collisions=0",
        "",
        "third_numerical_recreation_count=28",
        "third_terminal_numerical_recreation_count=17",
        "third_recursive_numerical_recreation_count=11",
        "third_exact_terminal_state_regeneration_count=7",
        "third_root_provenance_distinct=4840",
        "third_root_provenance_repeated=59",
        "third_root_provenance_maximum_multiplicity=2",
        "",
        f"third_retained_family_sha256={EXPECTED_HASHES['third_retained_family']}",
        f"third_terminal_family_sha256={EXPECTED_HASHES['third_terminal_family']}",
        f"third_recursive_family_sha256={EXPECTED_HASHES['third_recursive_family']}",
        f"third_raw_occurrences_sha256={EXPECTED_HASHES['third_raw_occurrences']}",
        f"third_all_tokens_sha256={EXPECTED_HASHES['third_all_tokens']}",
        f"third_terminal_tokens_sha256={EXPECTED_HASHES['third_terminal_tokens']}",
        f"third_recursive_tokens_sha256={EXPECTED_HASHES['third_recursive_tokens']}",
        "",
        "conclusion: the strict two-generation recursive Bellman row does not iterate under the same fixed policy and retention rule.",
        "Third-generation recursive retained mass is more than 2.011553 times second-generation recursive mass and more than 1.886248 times first-generation retained mass.",
        "The token (u,p) is not collision-sound across these generations: (60,1354490) recurs as a terminal sink.",
        "Immediate provenance separates the recorded collision, while source type and source step do not.",
        "This is an exact fixed-policy, fixed-retention three-generation no-go result, not a universal whole-tree theorem.",
        "",
    ]
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_third_generation_recursive_frontier.py [OUTPUT]")
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print("certificate_sha256=" + CERTIFICATE_SHA256)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
