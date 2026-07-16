#!/usr/bin/env python3
"""Exhaust cross-shell edge-swap injectivity and global support multiplicity."""
from __future__ import annotations

from collections import Counter, defaultdict
import hashlib
import json


Pair = tuple[int, int]
Progression = tuple[int, int, int, int]


def standard_shell_base(value: int) -> int:
    if value <= 0:
        raise ValueError("standard dyadic shells require positive integers")
    return 1 << (value.bit_length() - 1)


def four_aps(lower: int, upper: int) -> tuple[Progression, ...]:
    rows: list[Progression] = []
    for left in range(lower, upper + 1):
        for step in range(1, (upper - left) // 3 + 1):
            rows.append(tuple(left + index * step for index in range(4)))
    return tuple(rows)


def contains_four_ap(values: set[int], rows: tuple[Progression, ...]) -> bool:
    return any(set(row) <= values for row in rows)


def three_aps(values: set[int]) -> tuple[tuple[int, int, int], ...]:
    if not values:
        return ()
    upper = max(values)
    rows: list[tuple[int, int, int]] = []
    for left in sorted(values):
        for step in range(1, (upper - left) // 2 + 1):
            middle = left + step
            right = left + 2 * step
            if middle in values and right in values:
                rows.append((left, middle, right))
    return tuple(rows)


def canonical_pair(witness: Progression, missing: int) -> Pair:
    for index in range(3):
        if index != missing and index + 1 != missing:
            return witness[index], witness[index + 1]
    raise AssertionError("hole witness has no adjacent present pair")


def verify_cross_shell_injectivity(parent: set[int]) -> tuple[int, int, list[object]]:
    images: dict[Pair, list[tuple[Pair, int, str]]] = defaultdict(list)
    rows: list[object] = []

    for left, middle, right in three_aps(parent):
        # Target left adjacent edge; completion lies to the right.
        if (
            standard_shell_base(left) == standard_shell_base(middle)
            and standard_shell_base(right) != standard_shell_base(left)
        ):
            image = (middle, right)
            images[image].append(((left, middle), right, "right_completion"))
            rows.append((tuple(sorted(parent)), (left, middle), right, image))

        # Target right adjacent edge; completion lies to the left.
        if (
            standard_shell_base(middle) == standard_shell_base(right)
            and standard_shell_base(left) != standard_shell_base(middle)
        ):
            image = (left, middle)
            images[image].append(((middle, right), left, "left_completion"))
            rows.append((tuple(sorted(parent)), (middle, right), left, image))

    for image, preimages in images.items():
        if len(preimages) > 1:
            raise AssertionError(
                f"cross-shell swapped pair {image} has multiple target preimages: {preimages}"
            )
        left, right = image
        step = right - left
        if step <= 0:
            raise AssertionError("cross-shell image is degenerate")
        left_candidate = left - step
        right_candidate = right + step
        if left_candidate in parent and right_candidate in parent:
            raise AssertionError("opposite cross-shell preimages create a four-AP")

    return len(images), sum(len(rows) > 0 for _ in [0]), rows


def verify_canonical_supports(
    parent: set[int],
    witness_rows: tuple[Progression, ...],
) -> tuple[int, int, list[object]]:
    witness_by_hole: dict[int, tuple[Progression, int]] = {}
    for witness in witness_rows:
        missing = [index for index, value in enumerate(witness) if value not in parent]
        if len(missing) != 1:
            continue
        missing_index = missing[0]
        hole = witness[missing_index]
        candidate = (witness, missing_index)
        previous = witness_by_hole.get(hole)
        if previous is None or candidate < previous:
            witness_by_hole[hole] = candidate

    fibers: dict[Pair, list[int]] = defaultdict(list)
    rows: list[object] = []
    for hole, (witness, missing_index) in witness_by_hole.items():
        support = canonical_pair(witness, missing_index)
        if not set(support) <= parent:
            raise AssertionError("canonical support is not present")
        fibers[support].append(hole)

    maximum = 0
    reused = 0
    for support, holes in sorted(fibers.items()):
        distinct = tuple(sorted(set(holes)))
        left, right = support
        step = right - left
        possible = {left - step, left + 2 * step, left + 3 * step}
        if not set(distinct) <= possible:
            raise AssertionError("canonical support left its algebraic hole fiber")
        if len(distinct) > 2:
            raise AssertionError("one canonical support serves more than two holes")
        if 3 * len(distinct) > 6:
            raise AssertionError("one support exceeds six completion roles")
        maximum = max(maximum, len(distinct))
        reused += len(distinct) > 1
        rows.append((tuple(sorted(parent)), support, distinct))

    return len(fibers), reused, rows


def main() -> int:
    parent_universe = tuple(range(1, 13))
    parent_rows = tuple(
        row for row in four_aps(1, 12) if set(row) <= set(parent_universe)
    )
    witness_rows = four_aps(0, 13)

    counts = Counter()
    cross_profile: list[object] = []
    support_profile: list[object] = []
    maximum_support_holes = 0

    for mask in range(1 << len(parent_universe)):
        parent = {
            parent_universe[index]
            for index in range(len(parent_universe))
            if (mask >> index) & 1
        }
        if contains_four_ap(parent, parent_rows):
            continue
        counts["four_ap_free_parents"] += 1

        aps = three_aps(parent)
        counts["three_ap_occurrences"] += len(aps)

        cross_count, has_cross, cross_rows = verify_cross_shell_injectivity(parent)
        counts["cross_shell_targets"] += cross_count
        counts["cross_shell_images"] += cross_count
        counts["parents_with_cross_shell_targets"] += has_cross
        cross_profile.extend(cross_rows)

        fiber_count, reused, support_rows = verify_canonical_supports(
            parent, witness_rows
        )
        if fiber_count:
            counts["parents_with_certified_holes"] += 1
        counts["canonical_support_fibers"] += fiber_count
        counts["reused_canonical_supports"] += reused
        for _parent, _support, holes in support_rows:
            maximum_support_holes = max(maximum_support_holes, len(holes))
            counts["certified_holes"] += len(holes)
        support_profile.extend(support_rows)

    expected = {
        "canonical_support_fibers": 4371,
        "certified_holes": 5590,
        "cross_shell_images": 1441,
        "cross_shell_targets": 1441,
        "four_ap_free_parents": 2233,
        "parents_with_certified_holes": 1800,
        "parents_with_cross_shell_targets": 1024,
        "reused_canonical_supports": 1219,
        "three_ap_occurrences": 3174,
    }
    if dict(sorted(counts.items())) != expected:
        raise AssertionError(f"global shell profile changed: {dict(sorted(counts.items()))}")
    if maximum_support_holes != 2:
        raise AssertionError("sharp canonical support multiplicity changed")

    payload = {
        "schema": "global_shell_pair_batching_small_box_v1",
        "parent_universe": [1, 12],
        "witness_universe": [0, 13],
        "counts": expected,
        "maximum_cross_shell_image_multiplicity": 1,
        "maximum_canonical_support_holes": maximum_support_holes,
        "maximum_roles_per_support": 3 * maximum_support_holes,
        "cross_profile_sha256": hashlib.sha256(
            json.dumps(cross_profile, separators=(",", ":")).encode("utf-8")
        ).hexdigest(),
        "support_profile_sha256": hashlib.sha256(
            json.dumps(support_profile, separators=(",", ":")).encode("utf-8")
        ).hexdigest(),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("verified: global shell-batched pair first appearance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
