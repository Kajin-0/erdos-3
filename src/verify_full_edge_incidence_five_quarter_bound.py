#!/usr/bin/env python3
"""Verify the five-quarter full-edge incidence bound on small four-AP-free sets."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
import hashlib
import json

Pair = tuple[int, int]


def four_aps(upper: int) -> tuple[tuple[int, int, int, int], ...]:
    return tuple(
        (left, left + step, left + 2 * step, left + 3 * step)
        for left in range(1, upper + 1)
        for step in range(1, (upper - left) // 3 + 1)
    )


def three_aps(values: set[int]) -> tuple[tuple[int, int, int], ...]:
    if not values:
        return ()
    upper = max(values)
    return tuple(
        (left, left + step, left + 2 * step)
        for left in sorted(values)
        for step in range(1, (upper - left) // 2 + 1)
        if left + step in values and left + 2 * step in values
    )


def weight(pair: Pair) -> Fraction:
    return Fraction(1, pair[1] - pair[0])


def main() -> int:
    upper = 16
    aps4 = four_aps(upper)
    counts = Counter()
    maximum_ratio = Fraction()
    maximum_witness: tuple[int, ...] = ()
    rows: list[object] = []

    for mask in range(1 << upper):
        values = {
            value for value in range(1, upper + 1)
            if mask & (1 << (value - 1))
        }
        if any(set(ap) <= values for ap in aps4):
            continue
        counts["four_ap_free_sets"] += 1

        incidence: Counter[Pair] = Counter()
        aps3 = three_aps(values)
        for left, middle, right in aps3:
            incidence[(left, middle)] += 1
            incidence[(middle, right)] += 1
            incidence[(left, right)] += 1

        if max(incidence.values(), default=0) > 2:
            raise AssertionError("pair incidence exceeds two")

        duplicated = tuple(sorted(pair for pair, multiplicity in incidence.items() if multiplicity == 2))
        half_images: dict[Pair, tuple[Pair, str]] = {}
        duplicated_energy = Fraction()
        half_energy = Fraction()

        for pair in duplicated:
            left, right = pair
            gap = right - left
            if gap % 2:
                raise AssertionError("duplicated pair lacks integral midpoint")
            middle = left + gap // 2
            if middle not in values:
                raise AssertionError("duplicated pair is not an outer three-AP edge")
            duplicated_energy += weight(pair)
            for side, image in (
                ("left", (left, middle)),
                ("right", (middle, right)),
            ):
                if image in half_images:
                    raise AssertionError(
                        f"half-pair map is not injective: {image}, {half_images[image]}, {(pair, side)}"
                    )
                half_images[image] = (pair, side)
                if image not in incidence:
                    raise AssertionError("half-pair image is not a three-AP edge")
                half_energy += weight(image)

        if half_energy != 4 * duplicated_energy:
            raise AssertionError("half-pair energy is not four times duplicate energy")

        pair_energy = sum(
            (weight(pair) for pair in combinations(sorted(values), 2)),
            Fraction(),
        )
        if 4 * duplicated_energy > pair_energy:
            raise AssertionError("duplicate energy exceeds one quarter of pair energy")

        full_edge = Fraction(5, 2) * sum(
            (Fraction(1, middle - left) for left, middle, _right in aps3),
            Fraction(),
        )
        incidence_energy = sum(
            (multiplicity * weight(pair) for pair, multiplicity in incidence.items()),
            Fraction(),
        )
        if incidence_energy != full_edge:
            raise AssertionError("full-edge incidence identity failed")
        if full_edge > Fraction(5, 4) * pair_energy:
            raise AssertionError("five-quarter full-edge bound failed")

        ratio = full_edge / pair_energy if pair_energy else Fraction()
        if ratio > maximum_ratio:
            maximum_ratio = ratio
            maximum_witness = tuple(sorted(values))

        rows.append(
            (
                tuple(sorted(values)),
                tuple(aps3),
                duplicated,
                tuple(sorted(half_images)),
                str(duplicated_energy),
                str(full_edge),
                str(pair_energy),
            )
        )

    if counts["four_ap_free_sets"] != 22601:
        raise AssertionError("four-AP-free endpoint-16 count changed")

    payload = {
        "schema": "full_edge_incidence_five_quarter_small_box_v1",
        "universe": [1, upper],
        "counts": dict(sorted(counts.items())),
        "maximum_observed_full_edge_over_pair_energy": {
            "fraction": str(maximum_ratio),
            "decimal": f"{float(maximum_ratio):.15f}",
            "witness": maximum_witness,
        },
        "checks": {
            "pair_incidence_at_most_two": True,
            "duplicated_pair_is_outer_and_adjacent": True,
            "two_half_pair_map_injective": True,
            "duplicate_energy_at_most_quarter_pair_energy": True,
            "full_edge_at_most_five_quarters_pair_energy": True,
        },
        "rows_sha256": hashlib.sha256(
            json.dumps(rows, separators=(",", ":")).encode()
        ).hexdigest(),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
