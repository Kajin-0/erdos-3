#!/usr/bin/env python3
"""Certify a common occurrence-weight policy cone on S1 through S7."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from certified_contaminated_states import state_by_depth
from verify_s7_regenerative_seed_policy_dependence import (
    all_three_aps,
    middle_fibers,
    resolve,
)
from verify_s7_policy_transition_tradeoff import (
    fraction_hash,
    harmonic,
    policy_metrics,
)
from verify_s7_delayed_seed_policy import delayed_metrics

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

LAMBDA = Fraction(3)
EXPECTED = {
    1: {
        "lex_selected": 6,
        "reverse_selected": 6,
        "lex_residual": 6,
        "reverse_residual": 6,
        "lex_terminal_steps": 2,
        "reverse_terminal_steps": 4,
        "lex_occurrences": 4,
        "reverse_occurrences": 2,
        "score_hash": "496cf601dff1b45d679d3b660ec70a7a97de1503fbe13272de83a9fa7fb9a830",
        "score_digits": (2, 3),
    },
    2: {
        "lex_selected": 26,
        "reverse_selected": 26,
        "lex_residual": 13,
        "reverse_residual": 13,
        "lex_terminal_steps": 5,
        "reverse_terminal_steps": 12,
        "lex_occurrences": 21,
        "reverse_occurrences": 14,
        "score_hash": "26e14da583cf20deabf463d369ea3a56fce8f6c00c0685e98b731821b78a9634",
        "score_digits": (20, 20),
    },
    3: {
        "lex_selected": 92,
        "reverse_selected": 92,
        "lex_residual": 28,
        "reverse_residual": 28,
        "lex_terminal_steps": 10,
        "reverse_terminal_steps": 38,
        "lex_occurrences": 82,
        "reverse_occurrences": 54,
        "score_hash": "9526756d3da7ecdd3681c9cab4abf7e51b4403ad471a1239c716ad14f72f2baa",
        "score_digits": (73, 72),
    },
    4: {
        "lex_selected": 305,
        "reverse_selected": 298,
        "lex_residual": 58,
        "reverse_residual": 65,
        "lex_terminal_steps": 11,
        "reverse_terminal_steps": 113,
        "lex_occurrences": 294,
        "reverse_occurrences": 185,
        "score_hash": "f78dd546d272dbe0850925a3b3fc9ed1acaf754b934436c2ccc9120ae624145c",
        "score_digits": (366, 364),
    },
    5: {
        "lex_selected": 974,
        "reverse_selected": 966,
        "lex_residual": 118,
        "reverse_residual": 126,
        "lex_terminal_steps": 12,
        "reverse_terminal_steps": 287,
        "lex_occurrences": 962,
        "reverse_occurrences": 679,
        "score_hash": "30d292ac197806fba673fbe471be74e51deefd31d6888d8929f109e83155927a",
        "score_digits": (1299, 1297),
    },
    6: {
        "lex_selected": 3041,
        "reverse_selected": 2969,
        "lex_residual": 238,
        "reverse_residual": 310,
        "lex_terminal_steps": 13,
        "reverse_terminal_steps": 808,
        "lex_occurrences": 3028,
        "reverse_occurrences": 2161,
        "score_hash": "a6049293f2e2d956021768f5b6c4c8a8b7876a1efdec9d26e9e87320c1e11c1e",
        "score_digits": (5220, 5218),
    },
}
S7_DELAYED_SCORE_HASH = "35a408050d75bd146c4ced98379c688b0f94c9660c06690450595013d6549945"
S7_REVERSE_SCORE_HASH = "d71f7a9b1d7e8975ab12d2961587f5b1e3260d31ba344b81d5d4d4141e12e28d"
LAMBDA_STAR_HASH = "9b5cbc67ec09a798dabae07b974ba6dd05329a70663cceff255d70f3c73e70bb"
CERTIFICATE_SHA256 = "4d1e8eae67c474dee651bcee35397c84906c0216649ddfe7794529c1d990d907"


def coordinates(depth: int, reverse: bool) -> dict[str, object]:
    state = state_by_depth(depth)
    progressions = all_three_aps(state.values)
    selected, residual = resolve(state.values, progressions, reverse)
    _centers, fibers = middle_fibers(selected)
    steps = set(fibers)
    occurrences = [value for values in fibers.values() for value in values]
    return {
        "selected": len(selected),
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
    }


def score_difference(
    alternative: dict[str, object],
    lexicographic: dict[str, object],
    weight: Fraction = LAMBDA,
) -> Fraction:
    """Return alternative score minus lexicographic score."""
    return (
        alternative["terminal_mass"] - lexicographic["terminal_mass"]
        + weight
        * (
            alternative["occurrence_mass"]
            - lexicographic["occurrence_mass"]
        )
        + alternative["residual_error"] - lexicographic["residual_error"]
    )


def build_certificate() -> str:
    observed: dict[int, tuple[dict[str, object], dict[str, object]]] = {}
    score_differences: dict[int, Fraction] = {}

    for depth in range(1, 7):
        lex = coordinates(depth, False)
        reverse = coordinates(depth, True)
        observed[depth] = (lex, reverse)
        expected = EXPECTED[depth]
        compact = {
            "lex_selected": lex["selected"],
            "reverse_selected": reverse["selected"],
            "lex_residual": lex["residual"],
            "reverse_residual": reverse["residual"],
            "lex_terminal_steps": lex["terminal_steps"],
            "reverse_terminal_steps": reverse["terminal_steps"],
            "lex_occurrences": lex["occurrences"],
            "reverse_occurrences": reverse["occurrences"],
        }
        expected_compact = {key: expected[key] for key in compact}
        if compact != expected_compact:
            raise AssertionError(
                f"S{depth} policy-coordinate mismatch: {compact!r}"
            )

        difference = score_difference(reverse, lex)
        score_differences[depth] = difference
        if difference <= 0:
            raise AssertionError(f"S{depth}: lambda=3 must prefer lexicographic")
        if fraction_hash(difference) != expected["score_hash"]:
            raise AssertionError(f"S{depth}: score hash mismatch")
        digits = (
            len(str(difference.numerator)),
            len(str(difference.denominator)),
        )
        if digits != expected["score_digits"]:
            raise AssertionError(f"S{depth}: score digit-count mismatch")

    lex1, reverse1 = observed[1]
    terminal_difference1 = reverse1["terminal_mass"] - lex1["terminal_mass"]
    occurrence_difference1 = reverse1["occurrence_mass"] - lex1["occurrence_mass"]
    residual_difference1 = reverse1["residual_error"] - lex1["residual_error"]
    if not terminal_difference1 > 0 or not occurrence_difference1 < 0:
        raise AssertionError("S1 sign pattern mismatch")
    lambda_cap = (
        terminal_difference1 + residual_difference1
    ) / (-occurrence_difference1)
    if lambda_cap != Fraction(260, 63):
        raise AssertionError(f"S1 lambda cap mismatch: {lambda_cap}")
    if score_differences[1] != Fraction(71, 624):
        raise AssertionError("S1 lambda=3 score mismatch")

    for depth in range(2, 7):
        lex, reverse = observed[depth]
        if reverse["terminal_mass"] <= lex["terminal_mass"]:
            raise AssertionError(f"S{depth}: terminal sign mismatch")
        if reverse["occurrence_mass"] <= lex["occurrence_mass"]:
            raise AssertionError(f"S{depth}: occurrence sign mismatch")
        if reverse["residual_error"] < lex["residual_error"]:
            raise AssertionError(f"S{depth}: residual sign mismatch")

    lex7 = policy_metrics(False)
    reverse7 = policy_metrics(True)
    delayed7 = delayed_metrics()

    reverse_score7 = score_difference(reverse7, lex7)
    delayed_score7 = score_difference(delayed7, lex7)
    if reverse_score7 <= 0:
        raise AssertionError("S7 lambda=3 must reject reverse policy")
    if delayed_score7 >= 0:
        raise AssertionError("S7 lambda=3 must prefer delayed-seed policy")
    if fraction_hash(reverse_score7) != S7_REVERSE_SCORE_HASH:
        raise AssertionError("S7 reverse score hash mismatch")
    if fraction_hash(delayed_score7) != S7_DELAYED_SCORE_HASH:
        raise AssertionError("S7 delayed score hash mismatch")

    terminal_increase = delayed7["terminal_mass"] - lex7["terminal_mass"]
    residual_increase = delayed7["residual_error"] - lex7["residual_error"]
    occurrence_reduction = lex7["occurrence_mass"] - delayed7["occurrence_mass"]
    lambda_star = (
        terminal_increase + residual_increase
    ) / occurrence_reduction
    if fraction_hash(lambda_star) != LAMBDA_STAR_HASH:
        raise AssertionError("lambda-star hash mismatch")
    if not (
        lambda_star
        < Fraction(477, 200)
        < LAMBDA
        < lambda_cap
    ):
        raise AssertionError("common occurrence-weight cone is empty")

    lines = [
        "POLICY OCCURRENCE WEIGHT CONE S1-S7",
        "",
        "score=C_lambda=T+lambda*O+E",
        "difference_convention=alternative_minus_lexicographic",
        "",
        "s1_reverse_occurrence_difference_sign=negative",
        "s1_lex_preferred_iff_lambda_less_than=260/63",
        "s1_lambda_cap=260/63",
        "s1_score_lambda3=71/624",
        "s1_score_lambda3_sha256=" + EXPECTED[1]["score_hash"],
        "",
    ]
    for depth in range(2, 7):
        expected = EXPECTED[depth]
        lex, reverse = observed[depth]
        residual_sign = (
            "positive"
            if reverse["residual_error"] > lex["residual_error"]
            else "zero"
        )
        lines.extend(
            [
                f"S{depth}_reverse_terminal_difference_sign=positive",
                f"S{depth}_reverse_occurrence_difference_sign=positive",
                f"S{depth}_reverse_residual_difference_sign={residual_sign}",
                f"S{depth}_score_lambda3_sha256={expected['score_hash']}",
                f"S{depth}_score_lambda3_numerator_digits={expected['score_digits'][0]}",
                f"S{depth}_score_lambda3_denominator_digits={expected['score_digits'][1]}",
                f"S{depth}_lex_selected={expected['lex_selected']}",
                f"S{depth}_reverse_selected={expected['reverse_selected']}",
                f"S{depth}_lex_terminal_steps={expected['lex_terminal_steps']}",
                f"S{depth}_reverse_terminal_steps={expected['reverse_terminal_steps']}",
                "",
            ]
        )
    lines.extend(
        [
            "S7_delayed_minus_lex_score_lambda3_sha256=" + S7_DELAYED_SCORE_HASH,
            "S7_delayed_minus_lex_score_lambda3_sign=negative",
            "S7_reverse_minus_lex_score_lambda3_sha256=" + S7_REVERSE_SCORE_HASH,
            "S7_reverse_minus_lex_score_lambda3_sign=positive",
            "",
            "lambda_star_sha256=" + LAMBDA_STAR_HASH,
            "lambda_star_upper_bound=477/200",
            "certified_common_subcone=477/200<lambda<260/63",
            "witness_lambda=3",
            "",
            (
                "conclusion: for every lambda in the certified common subcone, "
                "lexicographic deletion is cheaper than"
            ),
            (
                "reverse lexicographic deletion on S1 through S7, while the "
                "delayed-seed policy is cheaper than"
            ),
            (
                "lexicographic deletion on S7. This is an exact finite "
                "policy-ranking theorem for the tested schedules,"
            ),
            (
                "not a proof that C_lambda is a retained-child Bellman potential "
                "or globally optimal over all schedules."
            ),
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
            "usage: verify_policy_occurrence_cone_s1_s7.py [OUTPUT]"
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
