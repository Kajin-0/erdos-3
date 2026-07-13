#!/usr/bin/env python3
"""Verify that one novel S7 cyclic-output child regenerates canonical S1."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import sys

from certified_contaminated_states import (
    BASE_PATTERN,
    SCALES,
    SEPARATIONS,
    state_by_depth,
    three_translate_raw,
)
from export_simultaneous_deletion_transition import build_payload
from verify_s7_scc_local_completion_credit import COMPONENT, parity_ok

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
    "b05c5b91ba5b148a1dbe999edc0617a5370889f4244cd66553c9d7a8c6ee9679"
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


def all_canonical_regenerations(
    payload: dict[str, object],
) -> list[tuple[tuple[int, ...], int, int, int]]:
    """Find exact factor-two/factor-four returns to canonical S1,...,S10."""
    grouped: dict[tuple[int, ...], int] = {}
    for occurrence in payload["recursive_shell_occurrences"]:
        if occurrence["source"] != "middle_fiber":
            continue
        if occurrence["source_step"] not in COMPONENT:
            continue
        values = tuple(occurrence["values"])
        scale = int(occurrence["shell_scale"])
        previous = grouped.setdefault(values, scale)
        if previous != scale:
            raise AssertionError("exact state appeared at two shell scales")

    scale_to_depth = {
        scale: depth
        for depth, scale in enumerate(SCALES, start=1)
    }
    regenerations: list[tuple[tuple[int, ...], int, int, int]] = []
    for values, scale in grouped.items():
        for factor in (2, 4):
            next_scale = factor * scale
            depth = scale_to_depth.get(next_scale)
            if depth is None:
                continue
            target = state_by_depth(depth).values
            target_raw = frozenset(value - next_scale for value in target)
            if len(target_raw) != 3 * (len(values) + 1):
                continue
            upper = (next_scale - 1 - max(values)) // 2
            candidates = sorted(
                value
                for value in target_raw
                if 1 <= value <= upper
                and 2 * value in target_raw
                and parity_ok(value)
            )
            for separation in candidates:
                if three_translate_raw(values, separation) == target_raw:
                    regenerations.append((values, factor, separation, depth))
    return sorted(regenerations)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def build_certificate() -> str:
    payload = build_payload(7)
    backbone = set(payload["backbone"]["values"])
    regenerations = all_canonical_regenerations(payload)
    expected_regeneration = [((16, 21, 26), 4, 1, 1)]
    if regenerations != expected_regeneration:
        raise AssertionError(
            f"canonical regeneration catalog mismatch: {regenerations!r}"
        )
    if SEED & backbone:
        raise AssertionError(
            "regenerating seed is not novel relative to S7 backbone"
        )

    occurrences = [
        occurrence
        for occurrence in payload["recursive_shell_occurrences"]
        if occurrence["source"] == "middle_fiber"
        and occurrence["source_step"] == 1
        and int(occurrence["shell_scale"]) == SEED_SCALE
        and frozenset(occurrence["values"]) == SEED
    ]
    if len(occurrences) != 1:
        raise AssertionError(
            f"unexpected seed occurrence count: {len(occurrences)}"
        )

    generated = three_translate_raw(SEED, FIRST_SEPARATION)
    if generated != BASE_PATTERN:
        raise AssertionError(
            "factor-four seed extension did not reproduce base pattern"
        )
    if first_four_ap(generated) is not None:
        raise AssertionError(
            "regenerated base pattern contains a four-term AP"
        )

    s1 = state_by_depth(1)
    translated = frozenset(
        FIRST_FACTOR * SEED_SCALE + value
        for value in generated
    )
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
        (
            state_by_depth(depth).weighted_density
            for depth in range(1, 10)
        ),
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
        "canonical_regeneration_count=1",
        "unique_factor2_factor4_canonical_regeneration=true",
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
        raise SystemExit(
            "usage: verify_s7_scc_seed_regeneration.py [OUTPUT]"
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
