#!/usr/bin/env python3
"""Verify a finite contaminated-backbone aligned-diamond chain.

The construction starts from the scale-64 aligned-diamond state and applies four
outer three-translate steps. Unlike the exact scale-eight family, the backbone
shell is only required to contain the previous state; additional points are
allowed. The chosen dyadic scale factors are 4, 8, 4, 4.

The script checks:

1. every generated state is four-term-progression-free;
2. every separation has the coordinated left-sponsor orientation;
3. the three translate layers are disjoint;
4. the selected step-R deletion schedule is feasible in increasing sponsor
   order;
5. the middle multiplicity fiber is exactly the previous state;
6. the relevant backbone shell contains the previous state;
7. cardinalities, persistence values, contamination counts, and exact
   multiplicity-weighted densities.
"""

from __future__ import annotations

import hashlib
from fractions import Fraction
from typing import Iterable

H = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}
TERMINAL_CORE = {16, 21, 26}

SCALES = [64, 256, 2048, 8192, 32768]
SEPARATIONS = [61, 303, 1597, 8195]
EXPECTED_HASHES = [
    "272061e4e2d7ea7f0ea4298c69e437c87631407baea59084fc5d81e62ca5c978",
    "cff7a986bfeb8def36b5597655a585f261f8a58facdb1ee9339d72a9eaa78e37",
    "5c0b2483d958e061fdad7c963ada9b3f942286fa27e29b106fdfcba621827783",
    "14c7479efe245b72430a0505b0983be1080166fb13108228159f02b2759dd093",
    "a315deca0997d946ca9bb5058d2a04bfe3e585332d4db5260e7d9edc9142f841",
]
EXPECTED_EXTRAS = [4, 1, 33, 1]


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 is defined only for positive integers")
    return (value & -value).bit_length() - 1


def first_4ap(values: Iterable[int]) -> tuple[int, int] | None:
    values_set = set(values)
    ordered = sorted(values_set)
    for first in ordered:
        for second in ordered:
            if second <= first:
                continue
            step = second - first
            if first + 2 * step in values_set and first + 3 * step in values_set:
                return first, step
    return None


def state_hash(values: Iterable[int]) -> str:
    payload = ",".join(str(value) for value in sorted(set(values)))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def three_translate_raw(state: set[int], separation: int) -> set[int]:
    anchor_set = {0} | state
    return {
        value + layer * separation
        for value in anchor_set
        for layer in range(3)
    }


def simulate_left_sponsor_schedule(state: set[int], separation: int) -> None:
    """Select every indexed step-R progression and delete its left sponsor.

    Increasing sponsor order is valid even when translate layers overlap in
    ambient position, because every center and right endpoint is larger than
    its sponsor and therefore has not yet been deleted as a later sponsor.
    """

    sponsors = sorted({0} | state)
    working = three_translate_raw(state, separation)
    for sponsor in sponsors:
        progression = {
            sponsor,
            sponsor + separation,
            sponsor + 2 * separation,
        }
        if not progression <= working:
            missing = sorted(progression - working)
            raise AssertionError(
                f"infeasible deletion schedule at sponsor {sponsor}: missing {missing}"
            )
        working.remove(sponsor)


def verify_base_state() -> None:
    anchor_set = {0} | TERMINAL_CORE
    expected = {
        value + layer
        for value in anchor_set
        for layer in range(3)
    }
    if expected != H:
        raise AssertionError("base state is not the intended three-translate gadget")
    if first_4ap(H) is not None:
        raise AssertionError("base relative state contains a four-term progression")

    centers = {1 + value for value in anchor_set}
    minimum_center = min(centers)
    middle_fiber = {
        center - minimum_center
        for center in centers
        if center > minimum_center
    }
    if middle_fiber != TERMINAL_CORE:
        raise AssertionError("base middle fiber is not the terminal core")

    backbone_shell = {value for value in H if 16 <= value < 32}
    if not TERMINAL_CORE <= backbone_shell:
        raise AssertionError("base backbone does not contain the terminal core")

    simulate_left_sponsor_schedule(TERMINAL_CORE, 1)


def main() -> None:
    verify_base_state()

    states: list[set[int]] = [{SCALES[0] + value for value in H}]
    contamination_counts: list[int] = []

    for index, separation in enumerate(SEPARATIONS):
        scale = SCALES[index]
        next_scale = SCALES[index + 1]
        state = states[index]

        if not all(scale <= value < 2 * scale for value in state):
            raise AssertionError(f"state {index + 1} left its dyadic shell")
        if first_4ap(state) is not None:
            raise AssertionError(f"state {index + 1} contains a four-term progression")
        if v2(separation) % 2:
            raise AssertionError(f"step {index + 1} has the wrong sponsor orientation")

        raw = three_translate_raw(state, separation)
        expected_size = 3 * (len(state) + 1)
        if len(raw) != expected_size:
            raise AssertionError(f"translate layers overlap at step {index + 1}")
        if max(raw) >= next_scale:
            raise AssertionError(f"raw state does not fit below next scale at step {index + 1}")
        if first_4ap(raw) is not None:
            raise AssertionError(f"raw state contains a four-term progression at step {index + 1}")

        simulate_left_sponsor_schedule(state, separation)

        centers = {separation + value for value in ({0} | state)}
        minimum_center = min(centers)
        middle_fiber = {
            center - minimum_center
            for center in centers
            if center > minimum_center
        }
        if middle_fiber != state:
            raise AssertionError(f"middle fiber is not exact at step {index + 1}")

        backbone_shell = {
            value
            for value in raw
            if scale <= value < 2 * scale
        }
        if not state <= backbone_shell:
            raise AssertionError(f"backbone loses the replay state at step {index + 1}")
        contamination_counts.append(len(backbone_shell - state))

        next_state = {next_scale + value for value in raw}
        states.append(next_state)

    for index, state in enumerate(states):
        scale = SCALES[index]
        expected_size = (9 * (3 ** (index + 1)) - 3) // 2
        if len(state) != expected_size:
            raise AssertionError(f"wrong cardinality for state {index + 1}")
        if not all(scale <= value < 2 * scale for value in state):
            raise AssertionError(f"state {index + 1} left its shell")
        witness = first_4ap(state)
        if witness is not None:
            raise AssertionError(
                f"state {index + 1} contains a four-term progression: {witness}"
            )
        digest = state_hash(state)
        if digest != EXPECTED_HASHES[index]:
            raise AssertionError(f"state hash mismatch at depth {index + 1}")

    if contamination_counts != EXPECTED_EXTRAS:
        raise AssertionError("unexpected backbone contamination profile")

    weighted_densities: list[Fraction] = []
    for index, state in enumerate(states):
        persistence = 2 ** (index + 1)
        weighted_densities.append(
            Fraction(persistence * len(state), SCALES[index])
        )

    total_growth = weighted_densities[-1] / weighted_densities[0]
    if total_growth != Fraction(91, 32):
        raise AssertionError("unexpected total weighted-density growth")

    print("verified: base aligned diamond")
    print("verified: every generated state is 4-AP-free")
    print("verified: every outer deletion schedule is feasible")
    print("verified: every middle fiber is the previous state")
    print("verified: every contaminated backbone contains the previous state")
    print(f"depth={len(states)}")
    print("scale_factors=4,8,4,4")
    print("separations=" + ",".join(str(value) for value in SEPARATIONS))
    print("state_sizes=" + ",".join(str(len(state)) for state in states))
    print("contamination=" + ",".join(str(value) for value in contamination_counts))
    print(
        "weighted_density="
        + ",".join(f"{value.numerator}/{value.denominator}" for value in weighted_densities)
    )
    print("weighted_density_growth=91/32")
    for index, digest in enumerate(EXPECTED_HASHES, start=1):
        print(f"state_{index}_sha256={digest}")


if __name__ == "__main__":
    main()
