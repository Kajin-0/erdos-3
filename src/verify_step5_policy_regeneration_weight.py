#!/usr/bin/env python3
"""Certify a uniform step-5 delay policy and its regeneration penalty."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import heapq
import sys

from certified_contaminated_states import state_by_depth
from verify_s7_regenerative_seed_policy_dependence import (
    all_three_aps,
    canonical_regenerations,
    middle_fibers,
    middle_shells,
    resolve,
    schedule_hash,
    v2,
)
from verify_s7_policy_transition_tradeoff import fraction_hash, harmonic

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

SEED_CENTERS = frozenset({1_354_065, 1_354_070, 1_354_075})
REGENERATION_CHARGE = Fraction(36_953, 4_096)
GAMMA = Fraction(1, 16)
EXPECTED = {
    1: (6, 6, 2, 4, "a93875fe509ac2fae0e0939d3ec71c4d978244c7398dd7185ca68c393426a5a6", "zero", 1, 1),
    2: (25, 14, 7, 18, "16f9af66896b771cc26d6242a0b7e882d0e2a5b7028f35c22e84f77667aa148b", "negative", 13, 11),
    3: (90, 30, 14, 76, "3a655d97eb48f0071de347a0b1ef22dbdba8600cf9b25f1493164aacb9d03f86", "negative", 35, 33),
    4: (302, 61, 22, 280, "c379f067d65b48a0201ab389edc1ae7be38efa663f57abffdd216f768a0f707e", "negative", 198, 197),
    5: (970, 122, 27, 943, "62f7fae68973af47abf3fcd5386a5cdac5cfa54f341dc27568ee3d39c5ae15e4", "negative", 684, 683),
    6: (3033, 246, 29, 3004, "a79db3e7d44df4c2a31957b9333308826f8823e260b25c96b4f511f8a367b7e9", "negative", 2609, 2608),
    7: (9348, 492, 41, 9307, "9d9c2b4d999eec4f7454f2902e081372f2772896aa62c6a5778664512030d567", "negative", 9368, 9366),
}
STEP5_SCHEDULE_HASH = "2394f4eb375c0a9c61eb3ee1de27d48e1119807246ce78d90f8acff1c6062019"
HYBRID_SCHEDULE_HASH = "aa327f586db534111de1b2cba3838db0963f4a281841ce348c2875b5400ab40c"
HYBRID_BASE_HASH = "7bb4d2865da80f4ac2c8162311cd069bb8fd2521efa89f2a86a21f5da8c13c72"
GAMMA_STAR_HASH = "4926b599987c1202d1799ca206918b4275754d61fe639ed123912793f12efd07"
HYBRID_REFINED_HASH = "57326b08a77c4f7e2780d27860a018f227ad22c137bed076531bcac5feb82700"
HYBRID_LEX_REFINED_HASH = "db729b405320221987f7ca70d00a3a93ca6eeadf15078c197343cbfe39807193"
CERTIFICATE_SHA256 = "4e64334bb09a12e0c1e764f59bbe5a6c71d477f631539cfcfceccc453cca7928"


def custom_metrics(depth: int, hybrid: bool) -> dict[str, object]:
    state = state_by_depth(depth)
    progressions = all_three_aps(state.values)
    current = set(state.values)
    queue = []
    for progression in progressions:
        step, left, middle, right = progression
        delayed = step == 5 or (
            hybrid and step == 1 and middle in SEED_CENTERS
        )
        queue.append(((delayed, progression), progression))
    heapq.heapify(queue)

    selected = []
    while queue:
        _priority, (step, left, middle, right) = heapq.heappop(queue)
        if left not in current or middle not in current or right not in current:
            continue
        sponsor = left if v2(step) % 2 == 0 else right
        opposite = right if sponsor == left else left
        selected.append((sponsor, middle, opposite, step, left, right))
        current.remove(sponsor)

    selected_tuple = tuple(selected)
    residual = frozenset(current)
    _centers, fibers = middle_fibers(selected_tuple)
    steps = set(fibers)
    occurrences = [value for values in fibers.values() for value in values]
    return {
        "selected": len(selected_tuple),
        "residual": len(residual),
        "terminal_steps": len(steps),
        "occurrences": len(occurrences),
        "terminal_mass": harmonic(steps),
        "occurrence_mass": sum(
            (harmonic(values) for values in fibers.values()),
            Fraction(),
        ),
        "residual_error": Fraction(
            state.persistence * len(residual),
            state.scale,
        ),
        "schedule_hash": schedule_hash(selected_tuple, residual),
        "fibers": fibers,
    }


def lex_metrics(depth: int) -> dict[str, object]:
    state = state_by_depth(depth)
    progressions = all_three_aps(state.values)
    selected, residual = resolve(state.values, progressions, False)
    _centers, fibers = middle_fibers(selected)
    steps = set(fibers)
    return {
        "terminal_mass": harmonic(steps),
        "occurrence_mass": sum(
            (harmonic(values) for values in fibers.values()),
            Fraction(),
        ),
        "residual_error": Fraction(
            state.persistence * len(residual),
            state.scale,
        ),
        "fibers": fibers,
    }


def base_score(metrics: dict[str, object]) -> Fraction:
    return (
        metrics["terminal_mass"]
        + 3 * metrics["occurrence_mass"]
        + metrics["residual_error"]
    )


def build_certificate() -> str:
    step5_metrics: dict[int, dict[str, object]] = {}

    for depth in range(1, 8):
        lex = lex_metrics(depth)
        step5 = custom_metrics(depth, False)
        step5_metrics[depth] = step5
        expected = EXPECTED[depth]
        compact = (
            step5["selected"],
            step5["residual"],
            step5["terminal_steps"],
            step5["occurrences"],
        )
        if compact != expected[:4]:
            raise AssertionError(f"S{depth}: step-5 metric mismatch {compact!r}")

        difference = base_score(step5) - base_score(lex)
        sign = "zero" if difference == 0 else "negative" if difference < 0 else "positive"
        if sign != expected[5]:
            raise AssertionError(f"S{depth}: step-5 score sign mismatch")
        if fraction_hash(difference) != expected[4]:
            raise AssertionError(f"S{depth}: step-5 score hash mismatch")
        digits = (
            len(str(difference.numerator)),
            len(str(difference.denominator)),
        )
        if digits != expected[6:8]:
            raise AssertionError(f"S{depth}: step-5 score digit mismatch")

    step5_7 = step5_metrics[7]
    if step5_7["schedule_hash"] != STEP5_SCHEDULE_HASH:
        raise AssertionError("S7 step-5 schedule hash mismatch")
    regenerations = canonical_regenerations(
        middle_shells(step5_7["fibers"])
    )
    expected_regeneration = [(1, 16, (16, 21, 26), 4, 1, 1)]
    if regenerations != expected_regeneration:
        raise AssertionError(
            f"S7 step-5 regeneration mismatch: {regenerations!r}"
        )

    hybrid = custom_metrics(7, True)
    if (
        hybrid["selected"],
        hybrid["residual"],
        hybrid["terminal_steps"],
        hybrid["occurrences"],
    ) != (9346, 494, 51, 9295):
        raise AssertionError("S7 hybrid metric mismatch")
    if hybrid["schedule_hash"] != HYBRID_SCHEDULE_HASH:
        raise AssertionError("S7 hybrid schedule hash mismatch")
    if canonical_regenerations(middle_shells(hybrid["fibers"])):
        raise AssertionError("S7 hybrid retains canonical regeneration")

    lex7 = lex_metrics(7)
    hybrid_minus_step5 = base_score(hybrid) - base_score(step5_7)
    if hybrid_minus_step5 <= 0:
        raise AssertionError("raw C3 should prefer step-5 policy")
    if fraction_hash(hybrid_minus_step5) != HYBRID_BASE_HASH:
        raise AssertionError("hybrid raw-score hash mismatch")

    gamma_star = hybrid_minus_step5 / REGENERATION_CHARGE
    if fraction_hash(gamma_star) != GAMMA_STAR_HASH:
        raise AssertionError("gamma-star hash mismatch")
    if not Fraction(57, 1000) < gamma_star < Fraction(29, 500):
        raise AssertionError("gamma-star bracket mismatch")

    refined_hybrid_minus_step5 = (
        hybrid_minus_step5 - GAMMA * REGENERATION_CHARGE
    )
    if refined_hybrid_minus_step5 >= 0:
        raise AssertionError("gamma=1/16 should prefer hybrid")
    if fraction_hash(refined_hybrid_minus_step5) != HYBRID_REFINED_HASH:
        raise AssertionError("hybrid refined-score hash mismatch")

    refined_hybrid_minus_lex = (
        base_score(hybrid)
        - base_score(lex7)
        - GAMMA * REGENERATION_CHARGE
    )
    if refined_hybrid_minus_lex >= 0:
        raise AssertionError("refined score should prefer hybrid to lex")
    if fraction_hash(refined_hybrid_minus_lex) != HYBRID_LEX_REFINED_HASH:
        raise AssertionError("hybrid-versus-lex refined hash mismatch")

    lines = [
        "STEP-5 POLICY AND REGENERATION WEIGHT",
        "",
        "base_score=C3=T+3*O+E",
        "refined_score=C3_gamma=T+3*O+E+gamma*G_regen",
        "policy_step5=delay_all_step_5_actions_then_lexicographic",
        "policy_hybrid=delay_step_5_and_three_seed_q1_actions_then_lexicographic",
        "",
    ]
    for depth in range(1, 8):
        expected = EXPECTED[depth]
        lines.extend(
            [
                f"S{depth}_step5_selected={expected[0]}",
                f"S{depth}_step5_residual={expected[1]}",
                f"S{depth}_step5_terminal_steps={expected[2]}",
                f"S{depth}_step5_occurrences={expected[3]}",
                f"S{depth}_step5_minus_lex_C3_sha256={expected[4]}",
                f"S{depth}_step5_minus_lex_C3_sign={expected[5]}",
                f"S{depth}_step5_minus_lex_C3_numerator_digits={expected[6]}",
                f"S{depth}_step5_minus_lex_C3_denominator_digits={expected[7]}",
                "",
            ]
        )
    lines.extend(
        [
            "S7_step5_schedule_sha256=" + STEP5_SCHEDULE_HASH,
            "S7_step5_canonical_regenerations=1",
            (
                "S7_step5_regeneration=source_step:1,scale:16,"
                "values:16,21,26,factor:4,separation:1,target:S1"
            ),
            "",
            "S7_hybrid_selected=9346",
            "S7_hybrid_residual=494",
            "S7_hybrid_terminal_steps=51",
            "S7_hybrid_occurrences=9295",
            "S7_hybrid_schedule_sha256=" + HYBRID_SCHEDULE_HASH,
            "S7_hybrid_canonical_regenerations=0",
            "",
            "S7_hybrid_minus_step5_C3_sha256=" + HYBRID_BASE_HASH,
            "S7_hybrid_minus_step5_C3_sign=positive",
            "regeneration_charge=36953/4096",
            "gamma_star_sha256=" + GAMMA_STAR_HASH,
            "gamma_star_bracket=57/1000,29/500",
            "witness_gamma=1/16",
            "S7_hybrid_minus_step5_refined_sha256=" + HYBRID_REFINED_HASH,
            "S7_hybrid_minus_step5_refined_sign=negative",
            "S7_hybrid_minus_lex_refined_sha256=" + HYBRID_LEX_REFINED_HASH,
            "S7_hybrid_minus_lex_refined_sign=negative",
            "",
            (
                "conclusion: delaying every step-5 action ties lexicographic "
                "deletion on S1 and lowers C3 on S2 through S7,"
            ),
            (
                "but it preserves the isolated canonical regeneration at S7. "
                "The non-regenerative hybrid has higher raw C3,"
            ),
            (
                "so C3 alone prefers a regenerative policy. Adding a "
                "regeneration penalty gamma greater than gamma_star"
            ),
            (
                "reverses that ranking; gamma=1/16 is an exact witness. This is "
                "a finite policy-ranking theorem, not a"
            ),
            "retention or whole-tree Bellman theorem.",
            "",
        ]
    )
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: verify_step5_policy_regeneration_weight.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print(
        "certificate_sha256="
        + hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
