#!/usr/bin/env python3
"""Certify a two-generation recursive Bellman row with terminal sinks separated."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED_MASS_SHA256 = {
    "first": "29f9f139dcdf764a486022f152d7ab0cacc8f40cd4af353f4a5e5f6bea843446",
    "terminal": "b9c790f6e8be18382848adb9e66fecc01ad26ee0e2ca77e31f93326fb5d1765e",
    "recursive": "539dfbe1e345d4e6f1e0ed1c08cfedd1eba8c3f9d195fc078ae9ac0d5e391775",
}
EXPECTED_RATIO_SHA256 = (
    "7feeb528abcb66253383e448fa50a19043a86c7059331a21f92432e09bded610"
)
EXPECTED_MARGIN_SHA256 = (
    "019f9b58c3addc0182870a02e40a616a953b3bfec09131d8d6e3024baf030bc1"
)
CERTIFICATE_SHA256 = (
    "7da70d79f271080a66d3f8ed1aa517d95bf321eb5d618822440fefdfa8504e14"
)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def build_certificate() -> str:
    retained_first, retained_second = reconstruct_retained_families()
    terminal = tuple(
        state
        for state in retained_second
        if not contains_three_term_ap(state.values)
    )
    recursive = tuple(
        state
        for state in retained_second
        if contains_three_term_ap(state.values)
    )

    first_mass = sum((state.weight for state in retained_first), Fraction())
    terminal_mass = sum((state.weight for state in terminal), Fraction())
    recursive_mass = sum((state.weight for state in recursive), Fraction())
    second_mass = sum((state.weight for state in retained_second), Fraction())
    if terminal_mass + recursive_mass != second_mass:
        raise AssertionError("terminal/recursive mass partition mismatch")

    observed_hashes = {
        "first": fraction_hash(first_mass),
        "terminal": fraction_hash(terminal_mass),
        "recursive": fraction_hash(recursive_mass),
    }
    if observed_hashes != EXPECTED_MASS_SHA256:
        raise AssertionError("Bellman-row source mass hash mismatch")

    recursive_ratio = recursive_mass / first_mass
    contraction_margin = (first_mass - recursive_mass) / first_mass
    if fraction_hash(recursive_ratio) != EXPECTED_RATIO_SHA256:
        raise AssertionError("recursive ratio hash mismatch")
    if fraction_hash(contraction_margin) != EXPECTED_MARGIN_SHA256:
        raise AssertionError("contraction margin hash mismatch")

    if not Fraction(937, 1_000) < recursive_ratio < Fraction(469, 500):
        raise AssertionError("recursive ratio outside certified rational bracket")
    if not Fraction(31, 500) < contraction_margin < Fraction(63, 1_000):
        raise AssertionError("contraction margin outside certified rational bracket")

    if Fraction(31, 500) * first_mass + recursive_mass >= first_mass:
        raise AssertionError("strict recursive Bellman row failed")

    lines = [
        "TWO-GENERATION RECURSIVE BELLMAN ROW",
        "",
        (
            "source_first_generation_retained_mass_sha256="
            f"{EXPECTED_MASS_SHA256['first']}"
        ),
        (
            "source_terminal_second_generation_mass_sha256="
            f"{EXPECTED_MASS_SHA256['terminal']}"
        ),
        (
            "source_recursive_second_generation_mass_sha256="
            f"{EXPECTED_MASS_SHA256['recursive']}"
        ),
        f"source_recursive_ratio_sha256={EXPECTED_RATIO_SHA256}",
        f"source_contraction_margin_sha256={EXPECTED_MARGIN_SHA256}",
        "",
        "recursive_ratio_bracket=937/1000,469/500",
        "contraction_margin_bracket=31/500,63/1000",
        "certified_row=(31/500)*H1+H2_recursive<H1",
        (
            "terminal_augmented_row=(31/500)*H1+H2_recursive+"
            "TermSink_first<H1+TermSink_first"
        ),
        "result=STRICTLY_FEASIBLE",
        "",
        (
            "conclusion: the certified two-generation transition has a strict "
            "recursive Bellman contraction with rational credit 31/500 of parent "
            "retained mass."
        ),
        (
            "Terminal sink mass is carried in a separate first-appearance coordinate "
            "and is neither discarded nor charged as recursive load."
        ),
        (
            "This row is fixed-policy and fixed-retention; it is not a universal "
            "whole-tree inequality."
        ),
        "",
    ]
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_two_generation_recursive_bellman_row.py [OUTPUT]")
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print("certificate_sha256=" + CERTIFICATE_SHA256)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
