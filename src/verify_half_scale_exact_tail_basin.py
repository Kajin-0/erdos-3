#!/usr/bin/env python3
"""Verify the enlarged half-scale exact-tail basin and the S10 entry count."""
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement, product


def solve_unique(matrix, rhs):
    rows = [[Q(x) for x in row] + [Q(value)] for row, value in zip(matrix, rhs)]
    n = len(rows[0]) - 1
    pivot_row = 0
    pivots = []
    for column in range(n):
        pivot = next((r for r in range(pivot_row, len(rows)) if rows[r][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for r in range(len(rows)):
            if r == pivot_row or not rows[r][column]:
                continue
            scale = rows[r][column]
            rows[r] = [rows[r][c] - scale * rows[pivot_row][c] for c in range(n + 1)]
        pivots.append(column)
        pivot_row += 1
    for r in range(pivot_row, len(rows)):
        if all(rows[r][c] == 0 for c in range(n)) and rows[r][-1] != 0:
            return None
    if pivot_row < n:
        return None
    solution = [Q(0)] * n
    for r, column in enumerate(pivots[:n]):
        solution[column] = rows[r][-1]
    return tuple(solution)


def vertices(equalities, rhs, bounds):
    n = len(bounds)
    m = len(equalities)
    boundary_equations = []
    for index, (lower, upper) in enumerate(bounds):
        row = [Q(0)] * n
        row[index] = Q(1)
        boundary_equations.append((tuple(row), Q(lower)))
        boundary_equations.append((tuple(row), Q(upper)))
    result = set()
    for selected in combinations(range(len(boundary_equations)), n - m):
        matrix = list(equalities) + [boundary_equations[i][0] for i in selected]
        values = list(rhs) + [boundary_equations[i][1] for i in selected]
        point = solve_unique(matrix, values)
        if point is None:
            continue
        if not all(Q(lo) <= point[i] <= Q(hi) for i, (lo, hi) in enumerate(bounds)):
            continue
        result.add(point)
    return result


def top_patterns(state_upper, separation_upper):
    feasible = []
    for layers in combinations_with_replacement(range(3), 4):
        for nonzero in product((0, 1), repeat=4):
            bounds = [(Q(1), state_upper) if flag else (Q(0), Q(0)) for flag in nonzero]
            bounds.append((Q(2), separation_upper))
            c1 = layers[0] - 2 * layers[1] + layers[2]
            c2 = layers[1] - 2 * layers[2] + layers[3]
            equations = (
                (Q(1), Q(-2), Q(1), Q(0), Q(c1)),
                (Q(0), Q(1), Q(-2), Q(1), Q(c2)),
            )
            points = vertices(equations, (Q(0), Q(0)), bounds)
            if points and max(
                p[1] - p[0] + Q(layers[1] - layers[0]) * p[4] for p in points
            ) > 0:
                feasible.append((layers, nonzero))
                break
    return feasible


def scheduled_descent_patterns(state_upper, kappa_upper):
    feasible = []
    for layers in combinations_with_replacement(range(3), 3):
        for nonzero in product((0, 1), repeat=3):
            bounds = [(Q(1), state_upper) if flag else (Q(0), Q(0)) for flag in nonzero]
            bounds.append((Q(0), kappa_upper))
            second_difference = layers[0] - 2 * layers[1] + layers[2]
            completion_layer = 2 * layers[2] - layers[1]
            equations = (
                (Q(1), Q(-2), Q(1), Q(second_difference)),
                (Q(0), Q(-1), Q(2), Q(completion_layer - 4)),
            )
            rhs = (Q(-2 * second_difference), Q(8 - 2 * completion_layer))
            points = vertices(equations, rhs, bounds)
            if points and max(
                p[1] - p[0] + Q(layers[1] - layers[0]) * (Q(2) + p[3])
                for p in points
            ) > 0:
                feasible.append((layers, nonzero))
                break
    return feasible


def build_s10():
    base = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}

    def raw(state, separation):
        anchor = {0} | state
        return anchor | {x + separation for x in anchor} | {
            x + 2 * separation for x in anchor
        }

    state = {64 + x for x in base}
    for scale, separation in zip(
        (256, 2048, 8192, 32768),
        (61, 303, 1597, 8195),
    ):
        state = {scale + x for x in raw(state, separation)}
    for scale, separation in (
        (262144, 93476),
        (1048576, 230164),
        (8388608, 2097164),
        (67108864, 16777217),
        (536870912, 134217729),
    ):
        state = {scale + x for x in raw(state, separation)}
    return state


def sponsor_count(maximum):
    total = 0
    power = 1
    while power <= maximum:
        total += maximum // power - maximum // (2 * power)
        power *= 4
    return total


def main():
    expected_top = [
        ((0, 0, 0, 0), (1, 1, 1, 1)),
        ((0, 0, 0, 1), (1, 1, 1, 0)),
        ((0, 0, 1, 1), (0, 1, 0, 1)),
        ((0, 0, 1, 2), (0, 1, 1, 1)),
        ((0, 1, 1, 2), (1, 0, 1, 0)),
        ((1, 1, 1, 1), (1, 1, 1, 1)),
        ((1, 1, 1, 2), (1, 1, 1, 0)),
        ((1, 1, 2, 2), (0, 1, 0, 1)),
        ((2, 2, 2, 2), (1, 1, 1, 1)),
    ]
    if top_patterns(Q(7, 4), Q(5, 2)) != expected_top:
        raise AssertionError("entry-region top pattern mismatch")
    if top_patterns(Q(15, 8), Q(9, 4)) != expected_top:
        raise AssertionError("invariant-region top pattern mismatch")

    expected_descent = [((0, 1, 2), (1, 1, 1))]
    if scheduled_descent_patterns(Q(7, 4), Q(1, 2)) != expected_descent:
        raise AssertionError("entry-region scheduled descent mismatch")
    if scheduled_descent_patterns(Q(15, 8), Q(1, 4)) != expected_descent:
        raise AssertionError("invariant-region scheduled descent mismatch")

    scale = 536870912
    maximum_k = scale // 2 - 1
    sponsor_offsets = sponsor_count(maximum_k)
    if sponsor_offsets != 178956970:
        raise AssertionError("half-scale sponsor count mismatch")

    completion_blocked = 54999  # From the complete CL-027 S10 classification.
    state = build_s10()
    if len(state) != 265719 or min(state) != scale or max(state) != 920574272:
        raise AssertionError("S10 reconstruction mismatch")

    half_values = set()
    for value in state:
        k = 2 * (value - scale)
        if 1 <= k <= maximum_k and ((k & -k).bit_length() - 1) % 2 == 0:
            half_values.add(k)
    if (
        len(half_values) != 29569
        or min(half_values) != 150994944
        or max(half_values) != 230535804
    ):
        raise AssertionError("half-scale half-obstruction mismatch")

    valid = sponsor_offsets - completion_blocked - len(half_values)
    if valid != 178872402:
        raise AssertionError("half-scale basin count mismatch")

    print("verified: half-scale entry region has the same nine top-layer patterns")
    print("verified: invariant region has the same nine top-layer patterns")
    print("verified: scheduled completion descent has only layer pattern 012")
    print("s10_half_scale_sponsor_offsets=178956970")
    print("s10_completion_blocked=54999")
    print("s10_half_blocked_below_half_scale=29569")
    print("s10_half_scale_infinite_tail_entries=178872402")


if __name__ == "__main__":
    main()
