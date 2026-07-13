#!/usr/bin/env python3
"""Verify that one novel S7 cyclic-output child regenerates canonical S1."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from certified_contaminated_states import (
    BASE_PATTERN,
    SEPARATIONS,
    state_by_depth,
    three_translate_raw,
)
from export_simultaneous_deletion_transition import build_payload

SEED = frozenset({16, 21, 26})
SEED_SCALE = 16
SEED_PERSISTENCE = 1
FIRST_FACTOR = 4
FIRST_SEPARATION = 1
EXACT_TAIL_FROM_S10 = Fraction(33_215, 16_384)
EXPECTED_PATH_CHARGE = Fraction(36_953, 4_096)
EXPECTED_FUTURE_CHARGE = Fraction(36_185, 4_096)
EXPECTED_DEBT = Fraction(13, 16)
CERTIFICATE_SHA256 = (
    "2d6296a1f161ef2b971681ad7ce967720c530c65298169a664e1983644f4fac3"
)


def first_four_ap(values: frozenset[int]) -> tuple[int, int] | None:
    ordered = sorted(values)
    present = set(ordered)
    maximum = ordered[-1]
    for index, first in enumerate(ordered):
        for second in ordered[index + 1 :]:
            step = second - first
            if first + 3 * step > maximum:
                break
            if first + 2 * step in present and first + 3 * step in present:
                return first, step
    return None


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def build_certificate() -> str:
    payload = build_payload(7)
    backbone = set(payload["backbone"]["values"])
    if SEED & backbone:
        raise AssertionError("regenerating seed is not novel relative to S7 backbone")

    occurrences = [
        occurrence
        for occurrence in payload["recursive_shell_occurrences"]
        if occurrence["source"] == "middle_fiber"
        and occurrence["source_step"] == 1
        and int(occurrence["shell_scale"]) == SEED_SCALE
        and frozenset(occurrence["values"]) == SEED
    ]
    if len(occurrences) != 1:
        raise AssertionError(f"unexpected seed occurrence count: {len(occurrences)}")

    generated = three_translate_raw(SEED, FIRST_SEPARATION)
    if generated != BASE_PATTERN:
        raise AssertionError("factor-four seed extension did not reproduce base pattern")
    if first_four_ap(generated) is not None:
        raise AssertionError("regenerated base pattern contains a four-term AP")

    s1 = state_by_depth(1)
    translated = frozenset(FIRST_FACTOR * SEED_SCALE + value for value in generated)
    if translated != s1.values:
        raise AssertionError("translated seed extension is not canonical S1")

    factors = [FIRST_FACTOR]
    separations = [FIRST_SEPARATION]
    for depth, separation in enumerate(SEPARATIONS, start=1):
        parent = state_by_depth(depth)
        child = state_by_depth(depth + 1)
        factor = child.scale // parent.scale
        raw = three_translate_raw(parent.values, separation)
        reconstructed = frozenset(child.scale + value for value in raw)
        if reconstructed != child.values:
            raise AssertionError(f"canonical transition mismatch at S{depth}")
        factors.append(factor)
        separations.append(separation)

    expected_factors = [4, 4, 8, 4, 4, 8, 4, 8, 8, 8]
    if factors != expected_factors:
        raise AssertionError(f"scale word mismatch: {factors}")

    seed_weight = Fraction(SEED_PERSISTENCE * len(SEED), SEED_SCALE)
    pre_s10 = sum(
        (state_by_depth(depth).weighted_density for depth in range(1, 10)),
        Fraction(0),
    )
    future_charge = pre_s10 + EXACT_TAIL_FROM_S10
    path_charge = seed_weight + future_charge
    if future_charge != EXPECTED_FUTURE_CHARGE:
        raise AssertionError(f"future charge mismatch: {future_charge}")
    if path_charge != EXPECTED_PATH_CHARGE:
        raise AssertionError(f"path charge mismatch: {path_charge}")

    debt = Fraction(
        SEED_PERSISTENCE * (3 * len(SEED) + 4),
        SEED_SCALE,
    ) * (Fraction(8, FIRST_FACTOR) - 1)
    if debt != EXPECTED_DEBT:
        raise AssertionError(f"first-step debt mismatch: {debt}")

    lines = [
        "S7 CYCLIC OUTPUT SEED REGENERATION",
        "",
        "source_parent=S7",
        "source_terminal_step=1",
        "seed_scale=16",
        "seed_values=16,21,26",
        "seed_imported_labels=0",
        "seed_occurrence_count=1",
        "",
        "first_factor=4",
        "first_separation=1",
        "generated_raw=0,1,2,16,17,18,21,22,23,26,27,28",
        "generated_raw_equals_BASE_PATTERN=true",
        "translated_child_scale=64",
        "translated_child_equals_S1=true",
        "",
        "scale_word=" + ",".join(map(str, factors)),
        "separation_word=" + ",".join(map(str, separations)),
        "terminal_state=S10",
        "then_enters_certified_exact_tail=true",
        "",
        f"normalized_seed_weight={fraction_text(seed_weight)}",
        f"first_factor4_bellman_debt={fraction_text(debt)}",
        f"future_charge_from_S1={fraction_text(future_charge)}",
        f"path_charge_from_seed={fraction_text(path_charge)}",
        "",
        (
            "conclusion: a novel shell child emitted by the S7 cyclic component "
            "regenerates the canonical contaminated seed S1"
        ),
        (
            "in one valid factor-four step and therefore inherits the complete "
            "recorded continuation through S10 and its exact tail."
        ),
        (
            "This is a pathwise structural recurrence, not a proof that the "
            "occurrence is retained in a Bellman child quotient."
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
        raise SystemExit("usage: verify_s7_scc_seed_regeneration.py [OUTPUT]")
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
