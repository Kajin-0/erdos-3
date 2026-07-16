#!/usr/bin/env python3
"""Exhaust the finite analogue of adjacent-root edge-swap involution."""
from __future__ import annotations

from collections import Counter
import hashlib
import json


Pair = tuple[int, int]
Progression = tuple[int, int, int, int]


def four_aps(upper: int) -> tuple[Progression, ...]:
    rows: list[Progression] = []
    for left in range(1, upper + 1):
        for step in range(1, (upper - left) // 3 + 1):
            rows.append(tuple(left + index * step for index in range(4)))
    return tuple(rows)


def is_four_ap_free(values: set[int], progressions: tuple[Progression, ...]) -> bool:
    return not any(set(row) <= values for row in progressions)


def adjacent_roots(pair: Pair, values: set[int]) -> tuple[int, ...]:
    left, right = pair
    gap = right - left
    return tuple(
        root for root in (left - gap, right + gap) if root in values
    )


def swap(pair: Pair, root: int) -> Pair:
    left, right = pair
    if root < left:
        return root, left
    if root > right:
        return right, root
    raise AssertionError("adjacent root lies inside target pair")


def main() -> int:
    upper = 12
    progressions = four_aps(upper)
    free_sets: list[set[int]] = []
    counts = Counter()
    rows: list[object] = []

    for mask in range(1 << upper):
        values = {value for value in range(1, upper + 1) if mask & (1 << (value - 1))}
        if not is_four_ap_free(values, progressions):
            continue
        free_sets.append(values)
        ordered = sorted(values)
        for left_index, left in enumerate(ordered):
            for right in ordered[left_index + 1 :]:
                pair = (left, right)
                roots = adjacent_roots(pair, values)
                if len(roots) > 1:
                    raise AssertionError("four-AP-free set has two adjacent roots")
                if not roots:
                    continue
                root = roots[0]
                image = swap(pair, root)
                image_roots = adjacent_roots(image, values)
                if image_roots != ((right if root < left else left),):
                    raise AssertionError(
                        "swapped pair does not have the original endpoint as unique reverse root"
                    )
                if swap(image, image_roots[0]) != pair:
                    raise AssertionError("edge-swap map is not an involution")
                if image[1] - image[0] != right - left:
                    raise AssertionError("edge swap changed physical gap")
                counts["tagged_swaps"] += 1
                rows.append((tuple(ordered), pair, root, image))

    counts["four_ap_free_sets"] = len(free_sets)
    payload = {
        "schema": "cross_shell_edge_swap_involution_small_box_v1",
        "universe": [1, upper],
        "counts": dict(sorted(counts.items())),
        "rows_sha256": hashlib.sha256(
            json.dumps(rows, separators=(",", ":")).encode("utf-8")
        ).hexdigest(),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("verified: adjacent-root edge-swap involution")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
