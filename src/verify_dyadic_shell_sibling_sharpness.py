"""Verify the dyadic-shell-compatible sibling sharpness construction.

The script checks:

1. the 34-element root set is contained in one standard dyadic block;
2. the root set is four-term-progression-free;
3. the scaled coordinated side-anchor deletion sequence is valid;
4. the middle multiplicity-fiber shell contains a step-234 progression;
5. the spanning-component shell contains a second step-234 progression.
"""

from __future__ import annotations

from typing import Iterable

SCALE = 13
SHIFT = 4500
ROOT_LOWER = 8192
ROOT_UPPER = 16384

D0 = {
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

D1 = D0 | {284, 394, 504}
D = {SCALE * value + SHIFT for value in D1}

# Base-coordinate (sponsor, common difference) pairs.
DELETION_SEQUENCE = [
    (504, 110),
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


def affine(value: int) -> int:
    return SCALE * value + SHIFT


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 expects a positive integer")
    result = 0
    while n % 2 == 0:
        n //= 2
        result += 1
    return result


def orientation(q: int) -> int:
    return 1 if v2(q) % 2 == 0 else -1


def selected_progression(sponsor: int, q: int) -> tuple[int, int, int]:
    sign = orientation(q)
    return sponsor, sponsor + sign * q, sponsor + 2 * sign * q


def find_4ap(values: Iterable[int]) -> tuple[int, int] | None:
    values_set = set(values)
    ordered = sorted(values_set)
    for index, first in enumerate(ordered):
        for second in ordered[index + 1 :]:
            step = second - first
            if first + 2 * step in values_set and first + 3 * step in values_set:
                return first, step
    return None


def is_three_term_progression(values: Iterable[int], step: int) -> bool:
    ordered = sorted(values)
    return (
        len(ordered) == 3
        and ordered[1] - ordered[0] == step
        and ordered[2] - ordered[1] == step
    )


def main() -> None:
    assert len(D) == 34
    assert min(D) == ROOT_LOWER
    assert max(D) == 12105
    assert all(ROOT_LOWER <= value < ROOT_UPPER for value in D)
    assert find_4ap(D) is None, f"unexpected root 4AP: {find_4ap(D)}"

    current = set(D)
    selected_step_centers: list[int] = []

    for base_sponsor, base_q in DELETION_SEQUENCE:
        sponsor = affine(base_sponsor)
        q = SCALE * base_q
        progression = selected_progression(sponsor, q)
        _, center, endpoint = progression

        assert sponsor in current, f"sponsor {sponsor} was already deleted"
        assert center in current, f"center {center} absent at deletion of {sponsor}"
        assert endpoint in current, f"endpoint {endpoint} absent at deletion of {sponsor}"

        if base_q == 110:
            selected_step_centers.append(center)

        current.remove(sponsor)

    minimum_center = min(selected_step_centers)
    middle_fiber = {
        center - minimum_center
        for center in selected_step_centers
        if center > minimum_center
    }

    assert middle_fiber == {325, 520, 754, 988, 1053}

    middle_shell = {value for value in middle_fiber if 512 <= value < 1024}
    assert middle_shell == {520, 754, 988}
    assert is_three_term_progression(middle_shell, 234)
    assert find_4ap(middle_shell) is None

    old_component_minimum = affine(min(D0))
    old_component_child = {
        affine(value) - old_component_minimum
        for value in D0
        if value > min(D0)
    }

    component_shell = {
        value for value in old_component_child if 2048 <= value < 4096
    }
    duplicated_component_progression = {3055, 3289, 3523}

    assert duplicated_component_progression <= component_shell
    assert is_three_term_progression(duplicated_component_progression, 234)
    assert find_4ap(component_shell) is None

    print("verified: 34-element root lies in [8192, 16384)")
    print("verified: root set is 4AP-free")
    print("verified: scaled deletion sequence is valid")
    print("verified: middle shell [512, 1024) emits step 234")
    print("verified: component shell [2048, 4096) emits step 234")
    print("verified: sibling two-layer sharpness survives standard dyadic shelling")


if __name__ == "__main__":
    main()
