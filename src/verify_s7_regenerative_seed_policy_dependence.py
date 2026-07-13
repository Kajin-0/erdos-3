#!/usr/bin/env python3
"""Verify policy dependence of the isolated regenerative S7 seed."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Iterable
import hashlib
import heapq
import json
import sys

from certified_contaminated_states import (
    SCALES,
    state_by_depth,
    three_translate_raw,
)

SEED = frozenset({16, 21, 26})
SEED_OFFSETS = (16, 21, 26)
EXPECTED_INITIAL_APS = 298_606
EXPECTED_FORCED_ACTIONS = 30
EXPECTED_Q1_FORCED_CENTERS = (1_687_866, 1_781_342, 1_918_030)
EXPECTED_Q1_POSSIBLE_CENTERS = 2_916
EXPECTED_Q1_POSSIBLE_MINIMA = 1_459
EXPECTED = {
    "lexicographic": {
        "selected": 9_360,
        "residual": 480,
        "terminal_steps": 25,
        "middle_shells": 124,
        "q1_centers": 2_916,
        "q1_minimum": 1_354_049,
        "schedule_sha256": (
            "12a369aa926f3ceac00943e8a383a9f635ec9f16b33565ec29f90c2d3d1d8ac1"
        ),
        "residual_sha256": (
            "b4517f0c67753b3297549dc7acc52818a85cb1df9261ce1a30cb78ec8d129a33"
        ),
        "q1_centers_sha256": (
            "f5c27ffd920b00b22ead173dca4111f3ec0f141b35c5b3a7d22e71a6d5d63592"
        ),
        "q1_fiber_sha256": (
            "42a9000082da6b62d3c01d163608631780c26617a518a7e142c9dcabb1a597ae"
        ),
        "seed_shells": 1,
        "canonical_regenerations": 1,
    },
    "reverse_lexicographic": {
        "selected": 9_180,
        "residual": 660,
        "terminal_steps": 2_252,
        "middle_shells": 2_374,
        "q1_centers": 55,
        "q1_minimum": 1_687_866,
        "schedule_sha256": (
            "92b9763e6f4edc408192a3e47a34d5ecdd397ee24da090f3050c7e1f8cdf9d11"
        ),
        "residual_sha256": (
            "d0c1940a9cf627e2f8c176aa8e2fdb32cc58649925043c4a7db22596dbc7b213"
        ),
        "q1_centers_sha256": (
            "d1046daa565dae6af6daa158c722e19b5161be178a14addbe40923cf68cf66f9"
        ),
        "q1_fiber_sha256": (
            "7960fdc08c817c77f4b2dfffa6fb7819f581505b49e3271f07da5384def8a2cc"
        ),
        "seed_shells": 0,
        "canonical_regenerations": 0,
    },
}
CERTIFICATE_SHA256 = (
    "8b7465459f04d07bd67a7f198b3947ca94756ce988c0c73f4e59a5fac6b4b336"
)

Progression = tuple[int, int, int, int]
Selected = tuple[int, int, int, int, int, int]


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def all_three_aps(values: Iterable[int]) -> list[Progression]:
    ordered = sorted(set(values))
    present = set(ordered)
    result: list[Progression] = []
    for left_index, left in enumerate(ordered):
        for middle in ordered[left_index + 1 :]:
            step = middle - left
            right = middle + step
            if right in present:
                result.append((step, left, middle, right))
    return sorted(result)


def resolve(
    parent: frozenset[int],
    progressions: list[Progression],
    reverse: bool,
) -> tuple[tuple[Selected, ...], frozenset[int]]:
    current = set(parent)
    queue = [
        (
            (
                tuple(-value for value in progression)
                if reverse
                else progression
            ),
            progression,
        )
        for progression in progressions
    ]
    heapq.heapify(queue)
    selected: list[Selected] = []

    while queue:
        _priority, (step, left, middle, right) = heapq.heappop(queue)
        if left not in current or middle not in current or right not in current:
            continue
        sponsor = left if v2(step) % 2 == 0 else right
        opposite = right if sponsor == left else left
        selected.append((sponsor, middle, opposite, step, left, right))
        current.remove(sponsor)

    residual = frozenset(current)
    if len(selected) + len(residual) != len(parent):
        raise AssertionError("selected/residual partition mismatch")
    if all_three_aps(residual):
        raise AssertionError("terminal residual contains a three-term AP")
    return tuple(selected), residual


def canonical_set_hash(values: Iterable[int]) -> str:
    payload = ",".join(str(value) for value in sorted(set(values)))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def schedule_hash(
    selected: tuple[Selected, ...],
    residual: frozenset[int],
) -> str:
    record = {
        "selected": [list(row) for row in selected],
        "residual": sorted(residual),
    }
    payload = json.dumps(
        record,
        sort_keys=True,
        separators=(",", ":"),
    ) + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def middle_fibers(
    selected: tuple[Selected, ...],
) -> tuple[dict[int, tuple[int, ...]], dict[int, frozenset[int]]]:
    centers: dict[int, list[int]] = defaultdict(list)
    for _sponsor, middle, _opposite, step, _left, _right in selected:
        centers[step].append(middle)

    ordered_centers: dict[int, tuple[int, ...]] = {}
    fibers: dict[int, frozenset[int]] = {}
    for step, values in centers.items():
        ordered = tuple(sorted(values))
        minimum = ordered[0]
        ordered_centers[step] = ordered
        fibers[step] = frozenset(value - minimum for value in ordered[1:])
    return ordered_centers, fibers


def middle_shells(
    fibers: dict[int, frozenset[int]],
) -> list[tuple[int, int, tuple[int, ...]]]:
    result: list[tuple[int, int, tuple[int, ...]]] = []
    for step in sorted(fibers):
        shells: dict[int, list[int]] = defaultdict(list)
        for value in sorted(fibers[step]):
            shells[value.bit_length() - 1].append(value)
        for exponent, values in sorted(shells.items()):
            result.append((step, 1 << exponent, tuple(values)))
    return result


def canonical_regenerations(
    shells: list[tuple[int, int, tuple[int, ...]]],
) -> list[tuple[int, int, tuple[int, ...], int, int, int]]:
    canonical = {
        depth: state_by_depth(depth)
        for depth in range(1, 11)
    }
    scale_to_depth = {
        state.scale: depth
        for depth, state in canonical.items()
    }
    target_raw = {
        depth: frozenset(
            value - state.scale
            for value in state.values
        )
        for depth, state in canonical.items()
    }

    result: list[tuple[int, int, tuple[int, ...], int, int, int]] = []
    for source_step, scale, values in shells:
        for factor in (2, 4):
            next_scale = factor * scale
            depth = scale_to_depth.get(next_scale)
            if depth is None:
                continue
            target = target_raw[depth]
            if len(target) != 3 * (len(values) + 1):
                continue
            upper = (next_scale - 1 - max(values)) // 2
            candidates = sorted(
                value
                for value in target
                if 1 <= value <= upper
                and 2 * value in target
                and v2(value) % 2 == 0
            )
            for separation in candidates:
                if three_translate_raw(values, separation) == target:
                    result.append(
                        (
                            source_step,
                            scale,
                            values,
                            factor,
                            separation,
                            depth,
                        )
                    )
    return sorted(result)


def forced_actions(
    progressions: list[Progression],
) -> tuple[Progression, ...]:
    sponsor_actions: dict[int, set[int]] = defaultdict(set)
    for index, (step, left, _middle, right) in enumerate(progressions):
        sponsor = left if v2(step) % 2 == 0 else right
        sponsor_actions[sponsor].add(index)

    forced: list[Progression] = []
    for index, progression in enumerate(progressions):
        _step, left, middle, right = progression
        actions_hitting = (
            sponsor_actions[left]
            | sponsor_actions[middle]
            | sponsor_actions[right]
        )
        if actions_hitting == {index}:
            forced.append(progression)
    return tuple(forced)


def policy_metrics(
    parent: frozenset[int],
    progressions: list[Progression],
    reverse: bool,
) -> dict[str, object]:
    selected, residual = resolve(parent, progressions, reverse)
    centers, fibers = middle_fibers(selected)
    shells = middle_shells(fibers)
    q1_centers = centers[1]
    q1_fiber = fibers[1]
    seed_shells = [
        row for row in shells if frozenset(row[2]) == SEED
    ]
    regenerations = canonical_regenerations(shells)
    return {
        "selected": len(selected),
        "residual": len(residual),
        "terminal_steps": len(fibers),
        "middle_shells": len(shells),
        "q1_centers": len(q1_centers),
        "q1_minimum": q1_centers[0],
        "schedule_sha256": schedule_hash(selected, residual),
        "residual_sha256": canonical_set_hash(residual),
        "q1_centers_sha256": canonical_set_hash(q1_centers),
        "q1_fiber_sha256": canonical_set_hash(q1_fiber),
        "seed_shells": len(seed_shells),
        "canonical_regenerations": len(regenerations),
        "regenerations": regenerations,
    }


def build_certificate() -> str:
    parent = state_by_depth(7).values
    progressions = all_three_aps(parent)
    if len(progressions) != EXPECTED_INITIAL_APS:
        raise AssertionError("initial progression count mismatch")

    forced = forced_actions(progressions)
    if len(forced) != EXPECTED_FORCED_ACTIONS:
        raise AssertionError("forced action count mismatch")
    q1_forced = tuple(
        sorted(middle for step, _left, middle, _right in forced if step == 1)
    )
    if q1_forced != EXPECTED_Q1_FORCED_CENTERS:
        raise AssertionError(f"q=1 forced centers mismatch: {q1_forced!r}")
    q1_possible = tuple(
        sorted(
            {
                middle
                for step, _left, middle, _right in progressions
                if step == 1
            }
        )
    )
    if len(q1_possible) != EXPECTED_Q1_POSSIBLE_CENTERS:
        raise AssertionError("q=1 possible-center count mismatch")
    possible_minima = sum(
        center <= q1_forced[0] for center in q1_possible
    )
    if possible_minima != EXPECTED_Q1_POSSIBLE_MINIMA:
        raise AssertionError("q=1 possible-minimum count mismatch")

    observed = {
        "lexicographic": policy_metrics(parent, progressions, False),
        "reverse_lexicographic": policy_metrics(parent, progressions, True),
    }
    for name, expected in EXPECTED.items():
        compact = {
            key: observed[name][key]
            for key in expected
        }
        if compact != expected:
            raise AssertionError(
                f"{name} metric mismatch: observed={compact!r}"
            )

    lex_regenerations = observed["lexicographic"]["regenerations"]
    expected_regeneration = [
        (1, 16, (16, 21, 26), 4, 1, 1)
    ]
    if lex_regenerations != expected_regeneration:
        raise AssertionError(
            f"lexicographic regeneration mismatch: {lex_regenerations!r}"
        )
    if observed["reverse_lexicographic"]["regenerations"]:
        raise AssertionError("reverse policy has a canonical regeneration")

    lex_minimum = int(observed["lexicographic"]["q1_minimum"])
    seed_centers = tuple(lex_minimum + offset for offset in SEED_OFFSETS)
    if seed_centers != (1_354_065, 1_354_070, 1_354_075):
        raise AssertionError("seed center mismatch")
    if any(center in q1_forced for center in seed_centers):
        raise AssertionError("a seed-producing center is root-forced")

    lines = [
        "S7 REGENERATIVE SEED POLICY DEPENDENCE",
        "",
        f"initial_three_ap_actions={len(progressions)}",
        f"root_forced_actions={len(forced)}",
        "q1_forced_centers=" + ",".join(map(str, q1_forced)),
        f"q1_possible_centers={len(q1_possible)}",
        f"q1_possible_minima_at_or_below_first_forced={possible_minima}",
        "seed_centers=" + ",".join(map(str, seed_centers)),
        "seed_centers_root_forced=0",
        "",
    ]

    for name in ("lexicographic", "reverse_lexicographic"):
        row = observed[name]
        prefix = "lex" if name == "lexicographic" else "reverse"
        lines.extend(
            [
                f"{prefix}_selected={row['selected']}",
                f"{prefix}_residual={row['residual']}",
                f"{prefix}_terminal_steps={row['terminal_steps']}",
                f"{prefix}_middle_shells={row['middle_shells']}",
                f"{prefix}_q1_centers={row['q1_centers']}",
                f"{prefix}_q1_minimum={row['q1_minimum']}",
                f"{prefix}_schedule_sha256={row['schedule_sha256']}",
                f"{prefix}_residual_sha256={row['residual_sha256']}",
                f"{prefix}_q1_centers_sha256={row['q1_centers_sha256']}",
                f"{prefix}_q1_fiber_sha256={row['q1_fiber_sha256']}",
                f"{prefix}_seed_shells={row['seed_shells']}",
                (
                    f"{prefix}_canonical_regenerations="
                    f"{row['canonical_regenerations']}"
                ),
                "",
            ]
        )

    lines.extend(
        [
            "lex_regeneration=source_q1,scale16,state_16_21_26,factor4,R1,S1",
            "reverse_regeneration=none",
            "",
            (
                "conclusion: the isolated exact S1 regeneration is specific "
                "to the lexicographic complete coordinated schedule."
            ),
            (
                "The reverse-lexicographic complete schedule has no seed shell "
                "and no factor-two/factor-four exact return"
            ),
            (
                "to any canonical S1 through S10 state. Regeneration is "
                "therefore not schedule-independent on the recorded parent."
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
            "usage: verify_s7_regenerative_seed_policy_dependence.py [OUTPUT]"
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
