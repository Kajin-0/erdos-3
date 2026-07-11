"""Verify the explicit sibling two-layer sharpness counterexample.

The script checks:

1. the parent set is 4AP-free;
2. the side-anchor deletion sequence is valid;
3. the chosen spanning-tree edges are DAG edges;
4. the middle multiplicity fiber contains a step-18 3AP;
5. the component-translation child contains the same step-18 3AP.
"""

from __future__ import annotations

from typing import Iterable


N = 300

D = {
    309,
    324,
    342,
    360,
    365,
    386,
    419,
    434,
    438,
    440,
    452,
    453,
    460,
    466,
    470,
    475,
    490,
    494,
    498,
    510,
    514,
    515,
    529,
    540,
    543,
    544,
    550,
    560,
    562,
    580,
    585,
}

# (sponsor, common difference)
DELETION_SEQUENCE = [
    (494, 54),
    (386, 52),
    (490, 25),
    (515, 35),
    (540, 20),
    (585, 110),
    (440, 13),
    (560, 50),
    (453, 45),
    (466, 48),
    (514, 15),
    (529, 110),
    (544, 110),
    (562, 110),
    (580, 110),
]

FOREST_PARENT = {
    440: 494,
    386: 494,
    438: 386,
    490: 386,
    515: 490,
    540: 490,
    550: 515,
    585: 515,
    560: 540,
    580: 540,
    475: 585,
    365: 585,
    453: 440,
    466: 440,
    510: 560,
    460: 560,
    498: 453,
    543: 453,
    514: 466,
    562: 466,
    529: 514,
    544: 514,
    419: 529,
    309: 529,
    434: 544,
    324: 544,
    452: 562,
    342: 562,
    470: 580,
    360: 580,
}


def v2(n: int) -> int:
    """Return the 2-adic valuation of a positive integer."""

    if n <= 0:
        raise ValueError("v2 expects a positive integer")

    valuation = 0
    while n % 2 == 0:
        n //= 2
        valuation += 1
    return valuation


def orientation(q: int) -> int:
    """Return the coordinated side-anchor orientation for step q."""

    return 1 if v2(q) % 2 == 0 else -1


def selected_progression(sponsor: int, q: int) -> tuple[int, int, int]:
    """Return (sponsor, center, opposite endpoint)."""

    sign = orientation(q)
    return sponsor, sponsor + sign * q, sponsor + 2 * sign * q


def find_4ap(values: Iterable[int]) -> tuple[int, int] | None:
    """Return (first term, step) for a nontrivial 4AP, if one exists."""

    values_set = set(values)
    if not values_set:
        return None

    lower = min(values_set)
    upper = max(values_set)
    for first in range(lower, upper + 1):
        if first not in values_set:
            continue
        max_step = (upper - first) // 3
        for step in range(1, max_step + 1):
            if all(first + k * step in values_set for k in range(4)):
                return first, step
    return None


def is_3ap(values: Iterable[int], step: int) -> bool:
    """Check whether the three sorted values form a 3AP of the given step."""

    ordered = sorted(values)
    return len(ordered) == 3 and ordered[1] - ordered[0] == step and ordered[2] - ordered[1] == step


def trace_root(vertex: int) -> int:
    """Trace a chosen forest parent map to its root."""

    seen: set[int] = set()
    current = vertex
    while current in FOREST_PARENT:
        if current in seen:
            raise AssertionError("cycle detected in forest parent map")
        seen.add(current)
        current = FOREST_PARENT[current]
    return current


def main() -> None:
    assert all(N <= value < 2 * N for value in D)
    assert find_4ap(D) is None, f"unexpected 4AP: {find_4ap(D)}"

    current = set(D)
    dag_edges: set[tuple[int, int]] = set()

    for sponsor, q in DELETION_SEQUENCE:
        progression = selected_progression(sponsor, q)
        _, center, endpoint = progression

        assert sponsor in current, f"sponsor {sponsor} was already deleted"
        assert center in current, f"center {center} absent at deletion of {sponsor}"
        assert endpoint in current, f"endpoint {endpoint} absent at deletion of {sponsor}"

        dag_edges.add((sponsor, center))
        dag_edges.add((sponsor, endpoint))
        current.remove(sponsor)

    assert set(FOREST_PARENT) == D - {494}
    for child, parent in FOREST_PARENT.items():
        assert (parent, child) in dag_edges, f"forest edge {parent}->{child} is not a DAG edge"

    assert all(trace_root(vertex) == 494 for vertex in D)

    repeated_sponsors = [529, 544, 562, 580]
    repeated_step = 110
    centers = [selected_progression(sponsor, repeated_step)[1] for sponsor in repeated_sponsors]
    assert centers == [419, 434, 452, 470]

    minimum_center = min(centers)
    xi_110 = {center - minimum_center for center in centers if center > minimum_center}
    assert xi_110 == {15, 33, 51}
    assert is_3ap(xi_110, 18)

    component_minimum = min(D)
    theta = {value - component_minimum for value in D if value > component_minimum}
    duplicated_component_progression = {544 - component_minimum, 562 - component_minimum, 580 - component_minimum}
    assert duplicated_component_progression == {235, 253, 271}
    assert duplicated_component_progression <= theta
    assert is_3ap(duplicated_component_progression, 18)

    print("verified: D is 4AP-free")
    print("verified: deletion sequence is valid")
    print("verified: chosen forest is one rooted component")
    print("verified: Xi_110 contains step-18 progression {15, 33, 51}")
    print("verified: Theta contains step-18 progression {235, 253, 271}")
    print("verified: the sibling two-layer bound is sharp")


if __name__ == "__main__":
    main()
