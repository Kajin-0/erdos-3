#!/usr/bin/env python3
"""Verify the full-fitting exact-tail basin classification at S10."""
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement, product
import hashlib

L10 = 536_870_912
K_MAX = 613_454_687
VALID_EXACT = 408_855_759
FNV_OFFSET = 1469598103934665603
FNV_PRIME = 1099511628211

EXPECTED_TOP = [
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
EXPECTED_DESCENT = [((0, 1, 2), (1, 1, 1))]


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


def raw(state, separation):
    anchor = {0} | state
    return anchor | {x + separation for x in anchor} | {x + 2 * separation for x in anchor}


def build_s10():
    state = {64 + x for x in {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}}
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


def v2(value):
    return (value & -value).bit_length() - 1


def sponsor_compatible(value):
    return 1 <= value <= K_MAX and v2(value) % 2 == 0


def hashes(values):
    payload = "".join(f"{value}," for value in sorted(values)).encode()
    fnv = FNV_OFFSET
    for byte in payload:
        fnv ^= byte
        fnv = (fnv * FNV_PRIME) & ((1 << 64) - 1)
    return f"{fnv:016x}", hashlib.sha256(payload).hexdigest()


def main():
    q = Q(920574272, L10)
    r = Q(K_MAX, L10)
    for generation in range(3):
        if top_patterns(q, Q(2) + r) != EXPECTED_TOP:
            raise AssertionError(f"top-pattern mismatch at generation {generation}")
        if scheduled_descent_patterns(q, r) != EXPECTED_DESCENT:
            raise AssertionError(f"descent mismatch at generation {generation}")
        q = Q(1) + (q + Q(4) + 2 * r) / 8
        r /= 2
    if not (q < Q(15, 8) and r < Q(1, 4)):
        raise AssertionError("third scheduled state does not enter invariant basin")
    if top_patterns(Q(15, 8), Q(9, 4)) != EXPECTED_TOP:
        raise AssertionError("invariant top-pattern mismatch")
    if scheduled_descent_patterns(Q(15, 8), Q(1, 4)) != EXPECTED_DESCENT:
        raise AssertionError("invariant descent mismatch")

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

    if len(first_half) != 59034:
        raise AssertionError("first-step half-obstruction count mismatch")
    if len(second_half) != 88614 or (min(second_half), max(second_half)) != (268435456, 460287135):
        raise AssertionError("second-step half-obstruction mismatch")
    if third_half != {603979776, 613416960}:
        raise AssertionError("third-step half-obstruction mismatch")
    if len(first_half & second_half) != 8 or first_half & third_half or second_half & third_half:
        raise AssertionError("half-obstruction overlap mismatch")

    # Completion obstructions lie below 260796, while all new half obstructions
    # are at least L10/2, so the classes are disjoint.
    if min(second_half | third_half) <= 260795:
        raise AssertionError("unexpected completion/new-half overlap range")

    additional = (second_half | third_half) - first_half
    if len(additional) != 88608:
        raise AssertionError("additional scheduled obstruction count mismatch")
    basin = VALID_EXACT - len(additional)
    if basin != 408767151:
        raise AssertionError("full-fitting basin count mismatch")

    expected_hashes = {
        "second": (
            "9cbe1d4b4bf738d2",
            "09f3cbb9ae87bfefcdc117f8e4340f4a1c93792ccf2a6b3ccacd5f2489ccb15e",
        ),
        "third": (
            "91e961fb57e2e687",
            "ae93a9f5f94348348c156b29e75074a61097723d2d98bd497629c3df5a16ba4f",
        ),
        "additional": (
            "bd7c3b1c8c99b586",
            "87e998e9e425e84c934ddb9c205ab4d934cd1af9f832662e7436595a66fae122",
        ),
    }
    if hashes(second_half) != expected_hashes["second"]:
        raise AssertionError("second-half hash mismatch")
    if hashes(third_half) != expected_hashes["third"]:
        raise AssertionError("third-half hash mismatch")
    if hashes(additional) != expected_hashes["additional"]:
        raise AssertionError("additional-obstruction hash mismatch")

    print("verified: full S10 fitting range retains the nine top-layer patterns")
    print("verified: scheduled completion descent is uniquely 012 through three finite generations")
    print("verified: third scheduled state enters the invariant half-scale region")
    print("valid_exact_factor8_children=408855759")
    print("second_scheduled_half_obstructions=88614")
    print("third_scheduled_half_obstructions=2")
    print("overlap_with_first_half_obstructions=8")
    print("additional_scheduled_obstructions=88608")
    print("full_fitting_infinite_tail_entries=408767151")
    print("coverage_fraction=10481209/10483481")
    print("second_half_fnv64=9cbe1d4b4bf738d2")
    print("third_half_fnv64=91e961fb57e2e687")
    print("additional_fnv64=bd7c3b1c8c99b586")


if __name__ == "__main__":
    main()
