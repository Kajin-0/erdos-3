#!/usr/bin/env python3
"""Verify a deterministic S2 deletion-DAG novel-fiber reference state.

This uses the same lexicographic coordinated schedule as the S1 adapter. The
certificate is schedule-specific; it demonstrates that middle-fiber support
outside the minimum-translation backbone is already nonzero at S2.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

from certified_contaminated_states import state_by_depth
from verify_s1_deletion_dag_adapter import (
    harmonic,
    middle_resolution,
    resolve_schedule,
    verify_dag,
)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def schedule_hash(selected, residual) -> str:
    record = {
        "selected": [
            [
                progression.sponsor,
                progression.middle,
                progression.opposite,
                progression.step,
            ]
            for progression in selected
        ],
        "residual": sorted(residual),
    }
    payload = json.dumps(
        record,
        sort_keys=True,
        separators=(",", ":"),
    ) + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def state_hash(values) -> str:
    payload = "".join(
        f"{value},"
        for value in sorted(values)
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def build_certificate() -> str:
    state = state_by_depth(2)
    parent = state.values
    selected, residual = resolve_schedule(parent)
    verify_dag(parent, selected, residual)

    terminal_steps, fibers, _, _ = middle_resolution(selected)
    minimum = min(parent)
    backbone = frozenset(
        value - minimum
        for value in parent
        if value > minimum
    )
    fiber_union = frozenset(
        value
        for fiber in fibers.values()
        for value in fiber
    )
    novel = fiber_union - backbone
    imported = fiber_union & backbone

    fiber_occurrence_mass = sum(
        (harmonic(fiber) for fiber in fibers.values()),
        Fraction(0),
    )
    fiber_union_mass = harmonic(fiber_union)
    within_fiber_duplicate_mass = (
        fiber_occurrence_mass - fiber_union_mass
    )
    novel_mass = harmonic(novel)
    imported_mass = harmonic(imported)

    expected_fibers = {
        1: frozenset(
            {16, 21, 26, 61, 77, 82, 87, 122, 138, 143, 148}
        ),
        5: frozenset({1, 61, 62, 122, 123}),
        30: frozenset(),
        31: frozenset(),
        61: frozenset({65, 66, 86, 87, 92}),
    }
    expected_novel = frozenset({1, 16, 21, 26, 62, 77, 123, 138})
    expected_imported = frozenset(
        {61, 65, 66, 82, 86, 87, 92, 122, 143, 148}
    )

    if state.size != 39 or state.scale != 256 or state.maximum != 470:
        raise AssertionError("S2 reconstruction mismatch")
    if len(selected) != 26 or len(residual) != 13:
        raise AssertionError("S2 schedule size mismatch")
    if residual != frozenset(
        {317, 378, 382, 383, 403, 404, 409, 443, 444, 464, 465, 469, 470}
    ):
        raise AssertionError("S2 residual mismatch")
    if terminal_steps != frozenset({1, 5, 30, 31, 61}):
        raise AssertionError("S2 terminal-step mismatch")
    if fibers != expected_fibers:
        raise AssertionError("S2 middle-fiber mismatch")
    if novel != expected_novel:
        raise AssertionError("S2 novel-fiber support mismatch")
    if imported != expected_imported:
        raise AssertionError("S2 imported-fiber support mismatch")
    if novel_mass != Fraction(239_396_453, 200_655_312):
        raise AssertionError("S2 novel-fiber mass mismatch")
    if imported_mass != Fraction(218_348_937_262, 1_897_648_393_355):
        raise AssertionError("S2 imported-fiber mass mismatch")
    if within_fiber_duplicate_mass != Fraction(383, 10_614):
        raise AssertionError("S2 within-fiber duplicate mass mismatch")

    s_hash = state_hash(parent)
    path_hash = schedule_hash(selected, residual)
    if s_hash != "134d805cfd73cbee488eca475d70ce0cb02c63e60927c74643891de48ee0ede9":
        raise AssertionError("S2 state hash mismatch")
    if path_hash != "586f62323391a20555b2a452d1b1a20d55e9a5cf0387677fd2b7013cd1baa689":
        raise AssertionError("S2 schedule hash mismatch")

    lines = [
        "S2 DETERMINISTIC NOVEL-FIBER REFERENCE",
        "",
        "status=exact_finite_schedule_specific",
        "schedule_rule=lexicographic_coordinated",
        "state_scale=256",
        "state_size=39",
        "state_maximum=470",
        "selected_progressions=26",
        "residual_size=13",
        "terminal_steps=1,5,30,31,61",
        "middle_fiber_1=16,21,26,61,77,82,87,122,138,143,148",
        "middle_fiber_5=1,61,62,122,123",
        "middle_fiber_30=empty",
        "middle_fiber_31=empty",
        "middle_fiber_61=65,66,86,87,92",
        "fiber_overlap_1_5=61,122",
        "fiber_overlap_1_61=87",
        "novel_fiber_support=1,16,21,26,62,77,123,138",
        "imported_fiber_support=61,65,66,82,86,87,92,122,143,148",
        f"fiber_occurrence_mass={fraction_text(fiber_occurrence_mass)}",
        f"fiber_union_mass={fraction_text(fiber_union_mass)}",
        (
            "within_fiber_duplicate_mass="
            f"{fraction_text(within_fiber_duplicate_mass)}"
        ),
        f"novel_fiber_mass={fraction_text(novel_mass)}",
        f"imported_fiber_mass={fraction_text(imported_mass)}",
        f"state_sha256={s_hash}",
        f"schedule_sha256={path_hash}",
        "",
        (
            "conclusion: unlike S1, this deterministic S2 resolution "
            "exports positive middle-fiber support outside the backbone."
        ),
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: verify_s2_novel_fiber_reference.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    print("verified: deterministic S2 novel-fiber reference")
    print("selected_progressions=26")
    print("novel_fiber_support=1,16,21,26,62,77,123,138")
    print("novel_fiber_mass=239396453/200655312")
    print("within_fiber_duplicate_mass=383/10614")
    print(f"certificate_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
