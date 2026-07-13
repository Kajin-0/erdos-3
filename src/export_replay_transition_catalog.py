#!/usr/bin/env python3
"""Enumerate exact replay-model continuation siblings.

The catalog is complete only inside the restricted standard-dyadic, disjoint
three-translate replay model used by the contaminated-backbone finite searches.
Its records are alternative continuation choices. They must not be summed as
simultaneous deletion-DAG children without a separate retention/packing theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable
import argparse
import hashlib
import json
import sys

from certified_contaminated_states import (
    CertifiedState,
    backbone_contamination,
    state_by_depth,
    three_translate_raw,
    v2,
)


@dataclass(frozen=True)
class ReplayChild:
    separation: int
    factor: int
    next_scale: int
    generated_size: int
    generated_maximum: int
    fit_slack_points: int
    contamination: int
    child_weighted_density: Fraction
    child_right_shell_slack: Fraction
    child_contamination_mass: Fraction


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def first_four_ap(values: Iterable[int]) -> tuple[int, int] | None:
    """Return one nontrivial four-term AP using exact membership checks."""

    ordered = sorted(set(values))
    present = set(ordered)
    maximum = ordered[-1]
    for first in ordered:
        for second in ordered:
            if second <= first:
                continue
            step = second - first
            if first + 3 * step > maximum:
                break
            if (
                first + 2 * step in present
                and first + 3 * step in present
            ):
                return first, step
    return None


def candidate_bounds(
    state: CertifiedState,
    factor: int,
) -> tuple[int, int]:
    if factor <= 1:
        raise ValueError("factor must exceed one")
    next_scale = factor * state.scale
    maximum = (next_scale - 1 - state.maximum) // 2
    return 1, maximum


def evaluate_candidate(
    state: CertifiedState,
    factor: int,
    separation: int,
) -> ReplayChild | None:
    if separation <= 0 or v2(separation) % 2:
        return None

    next_scale = factor * state.scale
    generated = three_translate_raw(state.values, separation)
    if len(generated) != 3 * (state.size + 1):
        return None
    generated_maximum = max(generated)
    if generated_maximum >= next_scale:
        return None
    if first_four_ap(generated) is not None:
        return None

    try:
        contamination = backbone_contamination(
            state.values,
            state.scale,
            generated,
        )
    except ValueError:
        return None

    child_persistence = 2 * state.persistence
    child_size = len(generated)
    fit_slack = next_scale - 1 - generated_maximum
    return ReplayChild(
        separation=separation,
        factor=factor,
        next_scale=next_scale,
        generated_size=child_size,
        generated_maximum=generated_maximum,
        fit_slack_points=fit_slack,
        contamination=contamination,
        child_weighted_density=Fraction(
            child_persistence * child_size,
            next_scale,
        ),
        child_right_shell_slack=Fraction(
            child_persistence * fit_slack,
            next_scale,
        ),
        child_contamination_mass=Fraction(
            child_persistence * contamination,
            next_scale,
        ),
    )


def enumerate_children(
    state: CertifiedState,
    factor: int,
    start_r: int | None = None,
    end_r: int | None = None,
) -> tuple[ReplayChild, ...]:
    lower, upper = candidate_bounds(state, factor)
    start = lower if start_r is None else max(lower, start_r)
    end = upper if end_r is None else min(upper, end_r)
    if end < start:
        return ()
    return tuple(
        child
        for separation in range(start, end + 1)
        if (
            child := evaluate_candidate(
                state,
                factor,
                separation,
            )
        )
        is not None
    )


def child_record(
    state: CertifiedState,
    child: ReplayChild,
) -> dict[str, object]:
    return {
        "record_type": "replay_child",
        "parent_depth": state.depth,
        "parent_scale": state.scale,
        "factor": child.factor,
        "separation": child.separation,
        "next_scale": child.next_scale,
        "generated_size": child.generated_size,
        "generated_maximum": child.generated_maximum,
        "fit_slack_points": child.fit_slack_points,
        "contamination": child.contamination,
        "features": {
            "weighted_density": fraction_text(
                child.child_weighted_density
            ),
            "right_shell_slack": fraction_text(
                child.child_right_shell_slack
            ),
            "incoming_contamination_mass": fraction_text(
                child.child_contamination_mass
            ),
        },
    }


def catalog_lines(
    state: CertifiedState,
    factor: int,
    children: tuple[ReplayChild, ...],
    start_r: int,
    end_r: int,
) -> list[str]:
    header = {
        "record_type": "replay_catalog",
        "model": "standard_dyadic_disjoint_three_translate_replay",
        "semantics": (
            "alternative_continuation_siblings_not_simultaneous_children"
        ),
        "parent_depth": state.depth,
        "parent_scale": state.scale,
        "parent_size": state.size,
        "factor": factor,
        "start_r": start_r,
        "end_r": end_r,
        "valid_count": len(children),
    }
    records = [header] + [
        child_record(state, child)
        for child in children
    ]
    return [json.dumps(record, sort_keys=True) for record in records]


def catalog_digest(lines: list[str]) -> str:
    payload = ("\n".join(lines) + "\n").encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def self_test() -> str:
    s1 = state_by_depth(1)
    s2 = state_by_depth(2)

    if enumerate_children(s1, 2):
        raise AssertionError("S1 unexpectedly has a factor-two child")

    s1_factor4 = enumerate_children(s1, 4)
    if [child.separation for child in s1_factor4] != [61, 68, 69, 71]:
        raise AssertionError("S1 factor-four sibling set mismatch")
    if [child.contamination for child in s1_factor4] != [4, 1, 1, 1]:
        raise AssertionError("S1 factor-four contamination mismatch")

    if enumerate_children(s2, 2):
        raise AssertionError("S2 unexpectedly has a factor-two child")
    if enumerate_children(s2, 4):
        raise AssertionError("S2 unexpectedly has a factor-four child")

    s2_factor8 = enumerate_children(s2, 8)
    if len(s2_factor8) != 203:
        raise AssertionError("S2 factor-eight sibling count mismatch")
    if s2_factor8[0].separation != 303:
        raise AssertionError("S2 factor-eight first sibling mismatch")
    if s2_factor8[-1].separation != 788:
        raise AssertionError("S2 factor-eight last sibling mismatch")

    start, end = candidate_bounds(s1, 4)
    lines = catalog_lines(s1, 4, s1_factor4, start, end)
    digest = catalog_digest(lines)
    certificate = "\n".join(
        [
            "REPLAY TRANSITION CATALOG SELF-TEST",
            "",
            "model=standard_dyadic_disjoint_three_translate_replay",
            (
                "semantics=alternative_continuation_siblings_"
                "not_simultaneous_children"
            ),
            "S1_factor2_valid=0",
            "S1_factor4_valid=4",
            "S1_factor4_separations=61,68,69,71",
            "S1_factor4_contamination=4,1,1,1",
            "S2_factor2_valid=0",
            "S2_factor4_valid=0",
            "S2_factor8_valid=203",
            "S2_factor8_first=303",
            "S2_factor8_last=788",
            f"S1_factor4_catalog_sha256={digest}",
            "",
        ]
    )
    return certificate


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    test_parser = subparsers.add_parser("self-test")
    test_parser.add_argument("output", nargs="?", type=Path)

    export_parser = subparsers.add_parser("export")
    export_parser.add_argument("--state-depth", type=int, required=True)
    export_parser.add_argument("--factor", type=int, required=True)
    export_parser.add_argument("--start-r", type=int)
    export_parser.add_argument("--end-r", type=int)
    export_parser.add_argument("--output", type=Path)

    args = parser.parse_args()
    if args.command == "self-test":
        certificate = self_test()
        if args.output is not None:
            args.output.write_text(certificate, encoding="utf-8")
        print(certificate, end="")
        return 0

    state = state_by_depth(args.state_depth)
    lower, upper = candidate_bounds(state, args.factor)
    start = lower if args.start_r is None else max(lower, args.start_r)
    end = upper if args.end_r is None else min(upper, args.end_r)
    children = enumerate_children(
        state,
        args.factor,
        start,
        end,
    )
    lines = catalog_lines(
        state,
        args.factor,
        children,
        start,
        end,
    )
    payload = "\n".join(lines) + "\n"
    if args.output is None:
        sys.stdout.write(payload)
    else:
        args.output.write_text(payload, encoding="utf-8")
        print(f"valid_count={len(children)}")
        print(f"catalog_sha256={catalog_digest(lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
