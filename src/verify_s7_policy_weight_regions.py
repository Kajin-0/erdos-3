#!/usr/bin/env python3
"""Certify exact weight regions for lexicographic versus delayed-seed S7 policy."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from verify_s7_policy_transition_tradeoff import policy_metrics, fraction_hash
from verify_s7_delayed_seed_policy import delayed_metrics

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

REGENERATIVE_PATH_CHARGE = Fraction(36_953, 4_096)
EXPECTED_HASHES = {
    "terminal_increase": "73690f788b4d1abf1a732d94739995697bd351334e0905a73fee212dd7b6940a",
    "residual_increase": "338083c1f70f5c4115f24e0852c1233bc2d2854f710626dde1bd13339190ad3e",
    "occurrence_reduction": "0ec585dfc2ed72867755258a9f662950653eb1ab9ec5987acbbf8cd1bb7ec114",
    "union_reduction": "eeb05bb9d768fe56d2d26456cb2ed7f25cc2b6d8f1828fda801e077bdc9bef2a",
    "duplicate_reduction": "3a4eea2c641b19a8241761bcabe0e8d5e6074ba37429e1ec5a71176290c46402",
    "lambda_star": "9b5cbc67ec09a798dabae07b974ba6dd05329a70663cceff255d70f3c73e70bb",
    "kappa_star": "dab567ca2bd53b43932ccdbafd2e12a1935f77d5abd1b0ce71bd192c42f0ebd4",
    "gamma_star": "10e5fd80502ed8affefd3fb7048e7b2205403b5661a828828c5e3c07de0f17f3",
    "terminal_weight_star": "dd76eaca14f2f5cf9882c5e284a0c886aa5d04152096feb0b8dce8be695a948b",
    "equal_terminal_occurrence_difference": "b6c95f982bd8f4d95bc6e757fe9fefb478a86cc08e3613dd77029f2f2bfc108f",
    "equal_terminal_union_difference": "0b650a902dbd99e24c1e4f7229f53e160a0eb1f4c4f40ff80c3a082356ac9dbb",
    "duplicate_weight_5_difference": "8a8f1261a9eae8a84fbf53d2bcba3757883c3034145c659da63c7fc4585d6621",
    "occurrence_weight_3_difference": "35a408050d75bd146c4ced98379c688b0f94c9660c06690450595013d6549945",
    "regeneration_weight_1_32_difference": "f38a38ab1ff48cef5f63abf62d0031141fc62752ddc725a6862633da47bf3d55",
}
CERTIFICATE_SHA256 = "97f45313494b16f022f47f87ef1c788962011c76c349dc88faef1ba8e1838693"


def assert_bracket(value: Fraction, lower: Fraction, upper: Fraction) -> None:
    if not lower < value < upper:
        raise AssertionError(f"expected {lower} < {value} < {upper}")


def score_difference(
    lex: dict[str, object],
    delayed: dict[str, object],
    *,
    terminal_weight: Fraction = Fraction(1),
    occurrence_weight: Fraction = Fraction(0),
    union_weight: Fraction = Fraction(0),
    duplicate_weight: Fraction = Fraction(0),
    regeneration_weight: Fraction = Fraction(0),
) -> Fraction:
    """Return delayed score minus lexicographic score."""
    return (
        terminal_weight * (delayed["terminal_mass"] - lex["terminal_mass"])
        + occurrence_weight * (delayed["occurrence_mass"] - lex["occurrence_mass"])
        + union_weight * (delayed["union_mass"] - lex["union_mass"])
        + duplicate_weight * (delayed["duplicate_mass"] - lex["duplicate_mass"])
        + (delayed["residual_error"] - lex["residual_error"])
        - regeneration_weight * REGENERATIVE_PATH_CHARGE
    )


def build_certificate() -> str:
    lex = policy_metrics(False)
    delayed = delayed_metrics()

    terminal_increase = delayed["terminal_mass"] - lex["terminal_mass"]
    residual_increase = delayed["residual_error"] - lex["residual_error"]
    occurrence_reduction = lex["occurrence_mass"] - delayed["occurrence_mass"]
    union_reduction = lex["union_mass"] - delayed["union_mass"]
    duplicate_reduction = lex["duplicate_mass"] - delayed["duplicate_mass"]

    quantities = {
        "terminal_increase": terminal_increase,
        "residual_increase": residual_increase,
        "occurrence_reduction": occurrence_reduction,
        "union_reduction": union_reduction,
        "duplicate_reduction": duplicate_reduction,
    }
    for name, value in quantities.items():
        if fraction_hash(value) != EXPECTED_HASHES[name]:
            raise AssertionError(f"{name} hash mismatch")
        if value <= 0:
            raise AssertionError(f"{name} must be positive")

    lambda_star = (terminal_increase + residual_increase) / occurrence_reduction
    kappa_star = (
        terminal_increase + residual_increase - union_reduction
    ) / duplicate_reduction
    gamma_star = (
        terminal_increase + residual_increase - occurrence_reduction
    ) / REGENERATIVE_PATH_CHARGE
    terminal_weight_star = (
        occurrence_reduction - residual_increase
    ) / terminal_increase

    thresholds = {
        "lambda_star": lambda_star,
        "kappa_star": kappa_star,
        "gamma_star": gamma_star,
        "terminal_weight_star": terminal_weight_star,
    }
    for name, value in thresholds.items():
        if fraction_hash(value) != EXPECTED_HASHES[name]:
            raise AssertionError(f"{name} hash mismatch")

    assert_bracket(lambda_star, Fraction(298, 125), Fraction(477, 200))
    assert_bracket(kappa_star, Fraction(1089, 250), Fraction(4357, 1000))
    assert_bracket(gamma_star, Fraction(21, 1000), Fraction(11, 500))
    assert_bracket(terminal_weight_star, Fraction(209, 500), Fraction(419, 1000))

    examples = {
        "equal_terminal_occurrence_difference": score_difference(
            lex, delayed, terminal_weight=Fraction(1), occurrence_weight=Fraction(1)
        ),
        "equal_terminal_union_difference": score_difference(
            lex, delayed, terminal_weight=Fraction(1), union_weight=Fraction(1)
        ),
        "duplicate_weight_5_difference": score_difference(
            lex,
            delayed,
            terminal_weight=Fraction(1),
            union_weight=Fraction(1),
            duplicate_weight=Fraction(5),
        ),
        "occurrence_weight_3_difference": score_difference(
            lex, delayed, terminal_weight=Fraction(1), occurrence_weight=Fraction(3)
        ),
        "regeneration_weight_1_32_difference": score_difference(
            lex,
            delayed,
            terminal_weight=Fraction(1),
            occurrence_weight=Fraction(1),
            regeneration_weight=Fraction(1, 32),
        ),
    }
    for name, value in examples.items():
        if fraction_hash(value) != EXPECTED_HASHES[name]:
            raise AssertionError(f"{name} hash mismatch")

    if examples["equal_terminal_occurrence_difference"] <= 0:
        raise AssertionError("unit occurrence score should prefer lexicographic")
    if examples["equal_terminal_union_difference"] <= 0:
        raise AssertionError("unit union score should prefer lexicographic")
    for name in (
        "duplicate_weight_5_difference",
        "occurrence_weight_3_difference",
        "regeneration_weight_1_32_difference",
    ):
        if examples[name] >= 0:
            raise AssertionError(f"{name} should prefer delayed policy")

    lines = [
        "S7 POLICY WEIGHT REGIONS",
        "",
        "policies=lexicographic,delayed_seed",
        "difference_convention=delayed_score_minus_lexicographic_score",
        "regenerative_path_charge=36953/4096",
        "",
    ]
    for name, value in quantities.items():
        lines.extend(
            [
                f"{name}_sha256={EXPECTED_HASHES[name]}",
                f"{name}_numerator_digits={len(str(value.numerator))}",
                f"{name}_denominator_digits={len(str(value.denominator))}",
            ]
        )
    lines.extend(
        [
            "",
            "score_lambda=T+lambda*O+E",
            "delayed_wins_score_lambda=iff_lambda_greater_than_lambda_star",
            f"lambda_star_sha256={EXPECTED_HASHES['lambda_star']}",
            "lambda_star_bracket=298/125,477/200",
            "",
            "score_kappa=T+U+kappa*D+E",
            "delayed_wins_score_kappa=iff_kappa_greater_than_kappa_star",
            f"kappa_star_sha256={EXPECTED_HASHES['kappa_star']}",
            "kappa_star_bracket=1089/250,4357/1000",
            "",
            "score_gamma=T+O+E+gamma*G_lex",
            "delayed_wins_score_gamma=iff_gamma_greater_than_gamma_star",
            f"gamma_star_sha256={EXPECTED_HASHES['gamma_star']}",
            "gamma_star_bracket=21/1000,11/500",
            "",
            "score_a=a*T+O+E",
            "delayed_wins_score_a=iff_a_less_than_terminal_weight_star",
            f"terminal_weight_star_sha256={EXPECTED_HASHES['terminal_weight_star']}",
            "terminal_weight_star_bracket=209/500,419/1000",
            "",
        ]
    )
    for name, value in examples.items():
        lines.extend(
            [
                f"{name}_sha256={EXPECTED_HASHES[name]}",
                f"{name}_sign={'positive' if value > 0 else 'negative'}",
            ]
        )
    lines.extend(
        [
            "",
            "interpretation_positive_difference=lexicographic_score_is_lower",
            "interpretation_negative_difference=delayed_seed_score_is_lower",
            "",
            (
                "conclusion: unit terminal plus unit recursive-mass scores prefer "
                "lexicographic deletion despite the delayed policy's"
            ),
            (
                "Pareto improvements. The delayed policy becomes cheaper only "
                "after recursive occurrence, duplicate, or"
            ),
            (
                "regenerative continuation cost receives sufficient weight. "
                "These are exact necessary policy-weight boundaries,"
            ),
            (
                "not proof that any listed raw coordinate is a valid retained-child "
                "Bellman potential."
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
        raise SystemExit("usage: verify_s7_policy_weight_regions.py [OUTPUT]")
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print("certificate_sha256=" + hashlib.sha256(certificate.encode("utf-8")).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
