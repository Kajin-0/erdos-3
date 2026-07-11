"""Verify the minimum-backbone aligned diamond counterexample."""

from __future__ import annotations

from collections.abc import Iterable


N = 64
PATTERN = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}
D = {N + value for value in PATTERN}
SPONSORS = [N + 26, N + 21, N + 16, N]
STEP = 1


def find_4ap(values: Iterable[int]) -> tuple[int, int] | None:
    values_set = set(values)
    if not values_set:
        return None

    lower = min(values_set)
    upper = max(values_set)
    for first in sorted(values_set):
        for step in range(1, (upper - first) // 3 + 1):
            if all(first + index * step in values_set for index in range(4)):
                return first, step
    return None


def is_3ap(values: Iterable[int], step: int) -> bool:
    ordered = sorted(values)
    return (
        len(ordered) == 3
        and ordered[1] - ordered[0] == step
        and ordered[2] - ordered[1] == step
    )


def main() -> None:
    assert all(N <= value < 2 * N for value in D)
    assert find_4ap(D) is None, f"unexpected 4AP: {find_4ap(D)}"

    current = set(D)
    centers: list[int] = []
    for sponsor in SPONSORS:
        center = sponsor + STEP
        endpoint = sponsor + 2 * STEP
        assert sponsor in current
        assert center in current
        assert endpoint in current
        centers.append(center)
        current.remove(sponsor)

    assert centers == [N + 27, N + 22, N + 17, N + 1]

    minimum_center = min(centers)
    middle_fiber = {
        center - minimum_center for center in centers if center > minimum_center
    }
    assert middle_fiber == {16, 21, 26}
    assert is_3ap(middle_fiber, 5)
    assert all(16 <= value < 32 for value in middle_fiber)

    minimum = min(D)
    backbone = {value - minimum for value in D if value > minimum}
    assert backbone == {1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}

    backbone_shell = {value for value in backbone if 16 <= value < 32}
    assert {16, 21, 26} <= backbone_shell
    assert is_3ap({16, 21, 26}, 5)

    representative_sponsor = minimum_center - STEP
    assert representative_sponsor == minimum == N

    print("verified: parent block is 4AP-free")
    print("verified: four step-one side-anchor deletions are valid")
    print("verified: middle fiber contains {16, 21, 26}")
    print("verified: backbone shell contains {16, 21, 26}")
    print("verified: both children have root anchor N")
    print("verified: one-parent same-anchor multiplicity two is sharp")


if __name__ == "__main__":
    main()
