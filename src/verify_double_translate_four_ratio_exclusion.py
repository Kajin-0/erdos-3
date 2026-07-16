#!/usr/bin/env python3
"""Exhaustively verify the four forbidden double-translate ratios."""
from __future__ import annotations

from collections import Counter
import hashlib
import json


def contains_four_ap(values: set[int]) -> bool:
    ordered = sorted(values)
    lookup = set(ordered)
    for index, left in enumerate(ordered):
        for right in ordered[index + 1 :]:
            span = right - left
            if span % 3:
                continue
            step = span // 3
            if left + step in lookup and left + 2 * step in lookup:
                return True
    return False


def main() -> int:
    limit = 12
    counts = Counter()
    profile_rows: list[tuple[object, ...]] = []

    for c0 in range(-limit, limit + 1):
        for c1 in range(c0 + 1, limit + 1):
            delta = c1 - c0
            for d0 in range(1, limit + 1):
                for d1 in range(d0 + 1, limit + 1):
                    difference = d1 - d0
                    for orientation in (-1, 1):
                        counts["configurations"] += 1
                        points = {
                            completion + copy * orientation * step
                            for completion in (c0, c1)
                            for step in (d0, d1)
                            for copy in (1, 2)
                        }
                        ratios: list[str] = []
                        if 2 * delta == difference:
                            ratios.append("1/2")
                        if delta == difference:
                            ratios.append("1")
                        if delta == 2 * difference:
                            ratios.append("2")
                        if delta == 4 * difference:
                            ratios.append("4")

                        if ratios:
                            counts["forbidden_ratio_configurations"] += 1
                            if not contains_four_ap(points):
                                raise AssertionError(
                                    "forbidden ratio failed to create a four-AP"
                                )
                            for ratio in ratios:
                                counts[f"ratio_{ratio}"] += 1
                        elif not contains_four_ap(points):
                            counts["four_ap_free_nonforbidden_configurations"] += 1

                        profile_rows.append(
                            (
                                c0,
                                c1,
                                d0,
                                d1,
                                orientation,
                                tuple(sorted(points)),
                                tuple(ratios),
                                contains_four_ap(points),
                            )
                        )

    expected = {
        "configurations": 39600,
        "forbidden_ratio_configurations": 7506,
        "four_ap_free_nonforbidden_configurations": 23824,
        "ratio_1": 2728,
        "ratio_1/2": 1360,
        "ratio_2": 2156,
        "ratio_4": 1262,
    }
    if dict(sorted(counts.items())) != dict(sorted(expected.items())):
        raise AssertionError(f"four-ratio profile changed: {counts}")

    output = {
        "schema": "double_translate_four_ratio_exclusion_small_box_v1",
        "limit": limit,
        "counts": dict(sorted(counts.items())),
        "profile_sha256": hashlib.sha256(
            json.dumps(profile_rows, sort_keys=True, separators=(",", ":")).encode(
                "utf-8"
            )
        ).hexdigest(),
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    print("verified: double-translate four-ratio exclusion")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
