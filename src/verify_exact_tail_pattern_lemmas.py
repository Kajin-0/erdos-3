#!/usr/bin/env python3
"""Exact rational verification of the layer-pattern lemmas used by exact tails."""
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product

Q = Fraction


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
        if not all(
            sum(Q(a) * x for a, x in zip(row, point)) == Q(value)
            for row, value in zip(equalities, rhs)
        ):
            continue
        result.add(point)
    return result


def top_layer_patterns(state_upper, separation_upper):
    feasible = []
    for layers in combinations_with_replacement(range(3), 4):
        for nonzero in product((0, 1), repeat=4):
            bounds = [
                (Q(1), Q(state_upper)) if flag else (Q(0), Q(0))
                for flag in nonzero
            ]
            bounds.append((Q(2), Q(separation_upper)))
            c1 = layers[0] - 2 * layers[1] + layers[2]
            c2 = layers[1] - 2 * layers[2] + layers[3]
            equations = (
                (Q(1), Q(-2), Q(1), Q(0), Q(c1)),
                (Q(0), Q(1), Q(-2), Q(1), Q(c2)),
            )
            points = vertices(equations, (Q(0), Q(0)), bounds)
            if not points:
                continue
            max_step = max(
                p[1] - p[0] + Q(layers[1] - layers[0]) * p[4]
                for p in points
            )
            if max_step > 0:
                feasible.append((layers, nonzero))
                break
    return feasible


def completion_descent_patterns():
    feasible = []
    # Current separation is R/L = 2 + kappa with 0 <= kappa <= 1/32.
    # Target raw completion offset satisfies 0 <= tau=c/L <= 4.
    # This covers both completion descents needed for the full S10 exact-fit classification.
    for layers in combinations_with_replacement(range(3), 3):
        for nonzero in product((0, 1), repeat=3):
            bounds = [
                (Q(1), Q(7, 4)) if flag else (Q(0), Q(0))
                for flag in nonzero
            ]
            bounds.extend(((Q(0), Q(1, 32)), (Q(0), Q(4))))
            second_difference = layers[0] - 2 * layers[1] + layers[2]
            completion_layer = 2 * layers[2] - layers[1]
            # Variables are a0,a1,a2,kappa,tau.
            equations = (
                (Q(1), Q(-2), Q(1), Q(second_difference), Q(0)),
                (Q(0), Q(-1), Q(2), Q(completion_layer), Q(-1)),
            )
            rhs = (
                Q(-2 * second_difference),
                Q(8 - 2 * completion_layer),
            )
            points = vertices(equations, rhs, bounds)
            if not points:
                continue
            max_step = max(
                p[1] - p[0]
                + Q(layers[1] - layers[0]) * (Q(2) + p[3])
                for p in points
            )
            if max_step > 0:
                feasible.append((layers, nonzero))
                break
    return feasible


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

    generic_top = top_layer_patterns(Q(7, 4), Q(65, 32))
    if generic_top != expected_top:
        raise AssertionError(f"unexpected generic top-layer patterns: {generic_top}")

    # Exact S10 geometry:
    # max(S10)/L10 = 920574272/536870912;
    # maximum fitting exact separation is 1687196511/536870912.
    s10_top = top_layer_patterns(
        Q(920574272, 536870912),
        Q(1687196511, 536870912),
    )
    if s10_top != expected_top:
        raise AssertionError(f"unexpected S10 full-fit patterns: {s10_top}")

    descent = completion_descent_patterns()
    expected_descent = [((0, 1, 2), (1, 1, 1))]
    if descent != expected_descent:
        raise AssertionError(f"unexpected completion-descent patterns: {descent}")

    print("verified: generic small-offset top-layer classification has nine patterns")
    print("verified: full S10 exact-factor-eight fit range has the same nine patterns")
    print("verified: completion descent through target offsets 0 <= c <= 4L has only layer pattern 0,1,2")
    print("top_patterns=" + repr(expected_top))
    print("descent_patterns=" + repr(descent))


if __name__ == "__main__":
    main()
