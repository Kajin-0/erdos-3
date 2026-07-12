#!/usr/bin/env python3
"""Audit the unsupported anchor template in the exploratory S10 factor-four reduction.

This does not decide whether the affected candidates contain some other 4-AP.
It verifies that the relation used by verify_depth10_factor4_anchor_reduction.cpp
is not, by itself, a four-term-progression witness.
"""

from itertools import combinations

L8 = 8_388_608
L9 = 67_108_864
L10 = 536_870_912
R8 = 16_777_217
R9 = 134_217_729
INHERITED_MAX = 76_583_775
MAX_R4 = 613_454_687


def raw(state: set[int], separation: int) -> set[int]:
    anchor = {0} | state
    return {
        value + layer * separation
        for value in anchor
        for layer in range(3)
    }


def translate(state: set[int], offset: int) -> set[int]:
    return {offset + value for value in state}


def build_s10() -> set[int]:
    state = {64 + x for x in {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}}
    for scale, separation in (
        (256, 61),
        (2048, 303),
        (8192, 1597),
        (32768, 8195),
        (262144, 93476),
        (1048576, 230164),
        (L8, 2097164),
        (L9, R8),
        (L10, R9),
    ):
        state = translate(raw(state, separation), scale)
    return state


def v2(value: int) -> int:
    return (value & -value).bit_length() - 1


def contains_difference(values: set[int], difference: int) -> bool:
    maximum = max(values)
    return any(
        value + difference <= maximum and value + difference in values
        for value in values
    )


def four_aps(values: set[int]) -> list[tuple[int, int, int, int]]:
    ordered = sorted(values)
    result: list[tuple[int, int, int, int]] = []
    for first, second in combinations(ordered, 2):
        step = second - first
        third = first + 2 * step
        fourth = first + 3 * step
        if third in values and fourth in values:
            result.append((first, second, third, fourth))
    return result


def main() -> None:
    s10 = build_s10()
    if len(s10) != 265_719 or min(s10) != L10 or max(s10) != 920_574_272:
        raise AssertionError("S10 reconstruction mismatch")

    # This example satisfies the exact arithmetic relation used in the anchor
    # reduction: x=3d and R=s-d. It is sponsor-compatible, lies in the genuinely
    # new factor-four interval, and its three translate layers are disjoint.
    d = 201_326_592
    x = 3 * d
    s = L10
    separation = s - d

    if x not in s10 or s not in s10:
        raise AssertionError("audit points are absent from S10")
    if not (INHERITED_MAX < separation <= MAX_R4):
        raise AssertionError("audit separation outside the new factor-four range")
    if v2(separation) % 2 != 0:
        raise AssertionError("audit separation is not sponsor-compatible")

    anchor = {0} | s10
    if contains_difference(anchor, separation) or contains_difference(anchor, 2 * separation):
        raise AssertionError("audit separation is not layer-disjoint")

    # These are every point whose presence follows solely from the three base
    # values 0, x, s and the three translate layers. If x=3d and s=d+R were a
    # direct anchor witness, a 4-AP would have to occur in this set.
    guaranteed = {
        base + layer * separation
        for base in (0, x, s)
        for layer in range(3)
    }
    progressions = four_aps(guaranteed)
    if progressions:
        raise AssertionError(f"unexpected guaranteed 4-APs: {progressions}")

    print("verified: the current anchor relation is not a direct 4-AP witness")
    print(f"audit_d={d}")
    print(f"audit_x={x}")
    print(f"audit_s={s}")
    print(f"audit_R={separation}")
    print("audit_R_layer_disjoint=true")
    print("guaranteed_point_count=9")
    print("guaranteed_4AP_count=0")
    print("conclusion=anchor_reduction_requires_an_additional_lemma_or_explicit_witness_check")


if __name__ == "__main__":
    main()
