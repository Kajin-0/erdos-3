"""Verify the explicit depth-two self-replicating aligned diamond."""

from __future__ import annotations

from collections.abc import Iterable


BASE = {0, 1, 2, 16, 17, 18, 21, 22, 23, 26, 27, 28}
S1 = {32 + value for value in BASE}
A1 = {0} | S1
OUTER_STEP = 67
RAW_G2 = A1 | {value + OUTER_STEP for value in A1} | {
    value + 2 * OUTER_STEP for value in A1
}
ROOT_SHIFT = 256
S2 = {ROOT_SHIFT + value for value in RAW_G2}


def find_4ap(values: Iterable[int]) -> tuple[int, int] | None:
    values_set = set(values)
    if not values_set:
        return None

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


def verify_outer_deletions() -> set[int]:
    current = set(S2)
    centers: list[int] = []

    sponsors = sorted((ROOT_SHIFT + value for value in A1), reverse=True)
    for sponsor in sponsors:
        center = sponsor + OUTER_STEP
        endpoint = sponsor + 2 * OUTER_STEP
        assert sponsor in current
        assert center in current
        assert endpoint in current
        centers.append(center)
        current.remove(sponsor)

    representative_center = min(centers)
    middle_fiber = {
        center - representative_center
        for center in centers
        if center > representative_center
    }
    assert middle_fiber == S1
    return middle_fiber


def verify_inner_aligned_diamond(state: set[int]) -> tuple[set[int], set[int]]:
    sponsors = [58, 53, 48, 32]
    current = set(state)
    centers: list[int] = []

    for sponsor in sponsors:
        center = sponsor + 1
        endpoint = sponsor + 2
        assert sponsor in current
        assert center in current
        assert endpoint in current
        centers.append(center)
        current.remove(sponsor)

    representative_center = min(centers)
    middle_fiber = {
        center - representative_center
        for center in centers
        if center > representative_center
    }
    assert middle_fiber == {16, 21, 26}
    assert is_3ap(middle_fiber, 5)

    minimum = min(state)
    backbone = {value - minimum for value in state if value > minimum}
    backbone_shell = {value for value in backbone if 16 <= value < 32}
    assert {16, 21, 26} <= backbone_shell
    assert is_3ap({16, 21, 26}, 5)

    return middle_fiber, {16, 21, 26}


def main() -> None:
    assert S1 <= set(range(32, 64))
    assert find_4ap(S1) is None

    assert len(A1) == 13
    assert len(RAW_G2) == 39
    assert max(RAW_G2) == 194
    assert find_4ap(RAW_G2) is None

    assert all(256 <= value < 512 for value in S2)
    assert find_4ap(S2) is None

    middle_child = verify_outer_deletions()

    backbone = {value - min(S2) for value in S2 if value > min(S2)}
    backbone_shell = {value for value in backbone if 32 <= value < 64}
    assert backbone_shell == S1

    first_pair = verify_inner_aligned_diamond(middle_child)
    second_pair = verify_inner_aligned_diamond(backbone_shell)

    assert first_pair == ({16, 21, 26}, {16, 21, 26})
    assert second_pair == ({16, 21, 26}, {16, 21, 26})

    print("verified: S1 is a 4AP-free aligned diamond")
    print("verified: the 39-point outer gadget is 4AP-free")
    print("verified: outer middle fiber equals S1")
    print("verified: outer backbone shell equals S1")
    print("verified: each S1 copy emits two copies of {16, 21, 26}")
    print("verified: total identical-history terminal multiplicity is four")


if __name__ == "__main__":
    main()
