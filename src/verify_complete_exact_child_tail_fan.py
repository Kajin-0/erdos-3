#!/usr/bin/env python3
"""Verify repaired tails for every valid exact factor-eight child of S10."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product

from verify_full_fitting_exact_tail_basin import (
    L10,
    K_MAX,
    VALID_EXACT,
    EXPECTED_TOP,
    EXPECTED_DESCENT,
    vertices,
    top_patterns,
    scheduled_descent_patterns,
    build_s10,
    v2,
    hashes,
)


def perturbed_descent_patterns(state_upper, kappa_lower, kappa_upper, epsilon):
    """Return feasible patterns for a target child offset c=4k+epsilon."""
    feasible = []
    for layers in combinations_with_replacement(range(3), 3):
        for nonzero in product((0, 1), repeat=3):
            bounds = [(Q(1), state_upper) if flag else (Q(0), Q(0)) for flag in nonzero]
            bounds.append((kappa_lower, kappa_upper))
            second_difference = layers[0] - 2 * layers[1] + layers[2]
            completion_layer = 2 * layers[2] - layers[1]
            equations = (
                (Q(1), Q(-2), Q(1), Q(second_difference)),
                (Q(0), Q(-1), Q(2), Q(completion_layer - 4)),
            )
            rhs = (
                Q(-2 * second_difference),
                Q(8 - 2 * completion_layer) + epsilon,
            )
            points = vertices(equations, rhs, bounds)
            if points and max(
                p[1] - p[0] + Q(layers[1] - layers[0]) * (Q(2) + p[3])
                for p in points
            ) > 0:
                feasible.append((layers, nonzero))
                break
    return feasible


def sponsor_compatible(value):
    return 1 <= value <= K_MAX and v2(value) % 2 == 0


def main():
    state = build_s10()
    if len(state) != 265719 or min(state) != L10 or max(state) != 920574272:
        raise AssertionError("S10 reconstruction mismatch")

    first_half = {
        2 * (value - L10)
        for value in state
        if value > L10 and sponsor_compatible(2 * (value - L10))
    }
    second_half = {
        value // 2
        for value in state
        if value % 2 == 0 and sponsor_compatible(value // 2)
    }
    third_half = {
        L10 + value // 8
        for value in state
        if value % 8 == 0 and sponsor_compatible(L10 + value // 8)
    }
    second_rescue = second_half - first_half
    third_rescue = third_half
    if len(second_rescue) != 88606 or third_rescue != {603979776, 613416960}:
        raise AssertionError("rescue classes mismatch")
    if second_rescue & third_rescue:
        raise AssertionError("rescue classes overlap")

    q0 = Q(920574272, L10)
    epsilon0 = Q(1, L10)

    # Second-step repair: replace 4k by 4k+1.
    h1_min = Q(min(second_rescue), L10)
    h1_max = Q(max(second_rescue), L10)
    if perturbed_descent_patterns(q0, h1_min, h1_max, epsilon0):
        raise AssertionError("unexpected completion pattern for second-step repair")
    q1 = Q(1) + (q0 + 4 + 2 * h1_max) / 8
    repaired_r1 = (4 * h1_max + epsilon0) / 8
    if top_patterns(q1, Q(2) + repaired_r1) != EXPECTED_TOP:
        raise AssertionError("second-step repair top-pattern mismatch")
    if scheduled_descent_patterns(q1, repaired_r1) != EXPECTED_DESCENT:
        raise AssertionError("second-step repair scheduled descent mismatch")
    q2 = Q(1) + (q1 + 4 + 2 * repaired_r1) / 8
    r2 = repaired_r1 / 2
    if not (q2 < Q(15, 8) and r2 < Q(1, 4)):
        raise AssertionError("second-step repair does not enter invariant basin")

    # Third-step repair: after the valid scheduled 4k step, replace 16k by 16k+1.
    h2_min = Q(min(third_rescue), L10)
    h2_max = Q(max(third_rescue), L10)
    q1_h2 = Q(1) + (q0 + 4 + 2 * h2_max) / 8
    r1_min = h2_min / 2
    r1_max = h2_max / 2
    epsilon1 = Q(1, 8 * L10)
    if perturbed_descent_patterns(q1_h2, r1_min, r1_max, epsilon1):
        raise AssertionError("unexpected completion pattern for third-step repair")
    q2_h2 = Q(1) + (q1_h2 + 4 + 2 * r1_max) / 8
    repaired_r2 = h2_max / 4 + Q(1, 64 * L10)
    if top_patterns(q2_h2, Q(2) + repaired_r2) != EXPECTED_TOP:
        raise AssertionError("third-step repair top-pattern mismatch")
    if scheduled_descent_patterns(q2_h2, repaired_r2) != EXPECTED_DESCENT:
        raise AssertionError("third-step repair scheduled descent mismatch")
    q3 = Q(1) + (q2_h2 + 4 + 2 * repaired_r2) / 8
    r3 = repaired_r2 / 2
    if not (q3 < Q(15, 8) and r3 < Q(1, 4)):
        raise AssertionError("third-step repair does not enter invariant basin")

    if hashes(second_rescue) != (
        "2b0b508436f86afe",
        "4778fcf2e5af35669209046938172b5d5bafc92a72297a8fdb3447193a5b23e5",
    ):
        raise AssertionError("second rescue hash mismatch")
    if hashes(third_rescue) != (
        "91e961fb57e2e687",
        "ae93a9f5f94348348c156b29e75074a61097723d2d98bd497629c3df5a16ba4f",
    ):
        raise AssertionError("third rescue hash mismatch")

    standard_basin = 408767151
    if standard_basin + len(second_rescue) + len(third_rescue) != VALID_EXACT:
        raise AssertionError("complete exact child fan count mismatch")

    print("verified: every valid exact S10 child has an infinite exact tail")
    print("standard_scheduled_basin=408767151")
    print("second_step_plus_one_repairs=88606")
    print("third_step_plus_one_repairs=2")
    print("complete_exact_child_tail_fan=408855759")
    print("second_rescue_fnv64=2b0b508436f86afe")
    print("third_rescue_fnv64=91e961fb57e2e687")


if __name__ == "__main__":
    main()
