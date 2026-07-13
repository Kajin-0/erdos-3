#!/usr/bin/env python3
r"""Verify an explicit coordinated S2 schedule with zero novel fiber mass.

The novel middle-fiber support of a deletion schedule is

    (union_q Xi_q) \ B(D),

where B(D) is the minimum-translation backbone.  The quantity is
nonnegative by definition.  This verifier supplies a valid coordinated
schedule on the recorded state S2 for which the support is empty, proving
that the minimum over all coordinated schedules is exactly zero.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable
import hashlib
import sys

from certified_contaminated_states import state_by_depth, v2


SCHEDULE = (
    (338, 342, 346, 4),
    (346, 403, 460, 57),
    (256, 317, 378, 61),
    (463, 464, 465, 1),
    (460, 464, 468, 4),
    (337, 398, 459, 61),
    (348, 409, 470, 61),
    (397, 403, 409, 6),
    (402, 403, 404, 1),
    (336, 397, 458, 61),
    (442, 443, 444, 1),
    (458, 464, 470, 6),
    (381, 382, 383, 1),
    (341, 403, 465, 62),
    (320, 321, 322, 1),
    (399, 403, 407, 4),
    (342, 403, 464, 61),
    (347, 403, 459, 56),
    (321, 382, 443, 61),
    (322, 383, 444, 61),
    (347, 408, 469, 61),
    (398, 403, 408, 5),
)

EXPECTED_CENTERS = {
    1: (321, 382, 403, 443, 464),
    4: (342, 403, 464),
    5: (403,),
    6: (403, 464),
    56: (403,),
    57: (403,),
    61: (317, 382, 383, 397, 398, 403, 408, 409),
    62: (403,),
}

EXPECTED_FIBERS = {
    1: (61, 82, 122, 143),
    4: (61, 122),
    5: (),
    6: (61,),
    56: (),
    57: (),
    61: (65, 66, 80, 81, 86, 91, 92),
    62: (),
}

EXPECTED_FIBER_UNION = (
    61,
    65,
    66,
    80,
    81,
    82,
    86,
    91,
    92,
    122,
    143,
)

EXPECTED_RESIDUAL = (
    317,
    341,
    343,
    378,
    382,
    383,
    397,
    403,
    404,
    407,
    408,
    443,
    444,
    458,
    464,
    468,
    469,
)

EXPECTED_STATE_SHA256 = (
    "cff7a986bfeb8def36b5597655a585f261f8a58facdb1ee9339d72a9eaa78e37"
)
EXPECTED_SCHEDULE_SHA256 = (
    "75409bc254f8ac850880dbd9a83276fb6b454f2bd064aef2a5e96bc7bb74dac8"
)
EXPECTED_FIBER_UNION_SHA256 = (
    "34ce0c2dd4042838212e083b1a06154ddc9cd7098cdbc64968f18d0fa5446f8b"
)
EXPECTED_RESIDUAL_SHA256 = (
    "c767976406872890d391155e4a7395e072f7882589dcdb912387551c05641394"
)


def canonical_set_hash(values: Iterable[int]) -> str:
    payload = ",".join(str(value) for value in sorted(set(values)))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def canonical_schedule_hash(
    schedule: Iterable[tuple[int, int, int, int]],
) -> str:
    lines: list[str] = []
    for left, middle, right, step in schedule:
        sponsor = left if v2(step) % 2 == 0 else right
        lines.append(f"{left},{middle},{right},{step},{sponsor}")
    payload = "\n".join(lines) + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def three_aps(values: Iterable[int]) -> list[tuple[int, int, int, int]]:
    value_set = set(values)
    ordered = sorted(value_set)
    result: list[tuple[int, int, int, int]] = []
    for left in ordered:
        for middle in ordered:
            if middle <= left:
                continue
            step = middle - left
            right = middle + step
            if right in value_set:
                result.append((left, middle, right, step))
    return result


def harmonic_mass(values: Iterable[int]) -> Fraction:
    return sum((Fraction(1, value) for value in set(values)), Fraction(0))


def verify() -> str:
    state = state_by_depth(2)
    working = set(state.values)
    centers: dict[int, list[int]] = defaultdict(list)

    if canonical_set_hash(working) != EXPECTED_STATE_SHA256:
        raise AssertionError("S2 state hash mismatch")

    for index, progression in enumerate(SCHEDULE, start=1):
        left, middle, right, step = progression
        if not (left < middle < right):
            raise AssertionError(f"step {index}: unordered progression")
        if middle - left != step or right - middle != step:
            raise AssertionError(f"step {index}: arithmetic progression mismatch")
        if not {left, middle, right} <= working:
            raise AssertionError(f"step {index}: progression is unavailable")
        sponsor = left if v2(step) % 2 == 0 else right
        if sponsor not in working:
            raise AssertionError(f"step {index}: sponsor already deleted")
        centers[step].append(middle)
        working.remove(sponsor)

    residual = tuple(sorted(working))
    if residual != EXPECTED_RESIDUAL:
        raise AssertionError("terminal residual mismatch")
    if three_aps(residual):
        raise AssertionError("terminal residual is not three-AP-free")

    canonical_centers = {
        step: tuple(sorted(values))
        for step, values in centers.items()
    }
    if canonical_centers != EXPECTED_CENTERS:
        raise AssertionError("selected-center profile mismatch")

    fibers: dict[int, tuple[int, ...]] = {}
    for step, values in canonical_centers.items():
        minimum = min(values)
        fibers[step] = tuple(
            sorted({value - minimum for value in values if value > minimum})
        )
    if fibers != EXPECTED_FIBERS:
        raise AssertionError("middle-fiber profile mismatch")

    fiber_union = tuple(
        sorted({value for fiber in fibers.values() for value in fiber})
    )
    if fiber_union != EXPECTED_FIBER_UNION:
        raise AssertionError("fiber union mismatch")

    minimum_state = min(state.values)
    backbone = {
        value - minimum_state
        for value in state.values
        if value > minimum_state
    }
    novel_support = set(fiber_union) - backbone
    if novel_support:
        raise AssertionError(f"novel support is nonempty: {sorted(novel_support)}")
    if harmonic_mass(novel_support) != 0:
        raise AssertionError("novel harmonic mass is not zero")

    if canonical_schedule_hash(SCHEDULE) != EXPECTED_SCHEDULE_SHA256:
        raise AssertionError("schedule hash mismatch")
    if canonical_set_hash(fiber_union) != EXPECTED_FIBER_UNION_SHA256:
        raise AssertionError("fiber-union hash mismatch")
    if canonical_set_hash(residual) != EXPECTED_RESIDUAL_SHA256:
        raise AssertionError("residual hash mismatch")

    lines = [
        "verified: valid coordinated S2 deletion schedule",
        "verified: terminal residual is three-AP-free",
        "verified: all middle fibers lie in the minimum-translation backbone",
        "state=S2",
        f"state_size={state.size}",
        f"schedule_length={len(SCHEDULE)}",
        f"residual_size={len(residual)}",
        "selected_steps=" + ",".join(str(step) for step in sorted(fibers)),
        "fiber_union=" + ",".join(str(value) for value in fiber_union),
        "novel_support=",
        "novel_harmonic_mass=0",
        "minimum_novel_harmonic_mass=0",
        f"state_sha256={EXPECTED_STATE_SHA256}",
        f"schedule_sha256={EXPECTED_SCHEDULE_SHA256}",
        f"fiber_union_sha256={EXPECTED_FIBER_UNION_SHA256}",
        f"residual_sha256={EXPECTED_RESIDUAL_SHA256}",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    certificate = verify()
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_s2_zero_novelty_schedule.py [certificate-path]")
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")


if __name__ == "__main__":
    main()
