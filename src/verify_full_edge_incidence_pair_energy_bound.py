#!/usr/bin/env python3
"""Exhaust the physical-pair incidence bound for four-AP-free small sets."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
import hashlib
import json


Pair = tuple[int, int]
Progression3 = tuple[int, int, int]
Progression4 = tuple[int, int, int, int]


def progressions4(upper: int) -> tuple[Progression4, ...]:
    return tuple(
        (left, left + step, left + 2 * step, left + 3 * step)
        for left in range(1, upper + 1)
        for step in range(1, (upper - left) // 3 + 1)
    )


def progressions3(values: set[int]) -> tuple[Progression3, ...]:
    if not values:
        return ()
    upper = max(values)
    return tuple(
        (left, left + step, left + 2 * step)
        for left in sorted(values)
        for step in range(1, (upper - left) // 2 + 1)
        if left + step in values and left + 2 * step in values
    )


def pair_weight(pair: Pair) -> Fraction:
    return Fraction(1, pair[1] - pair[0])


def main() -> int:
    upper = 12
    aps4 = progressions4(upper)
    counts = Counter()
    maximum_pair_multiplicity = 0
    maximum_ratio = Fraction()
    maximum_ratio_witness: tuple[int, ...] = ()
    rows: list[object] = []

    for mask in range(1 << upper):
        values = {
            value
            for value in range(1, upper + 1)
            if mask & (1 << (value - 1))
        }
        if any(set(ap) <= values for ap in aps4):
            continue
        counts["four_ap_free_sets"] += 1
        aps3 = progressions3(values)
        incidence = Counter()
        for left, middle, right in aps3:
            incidence[(left, middle)] += 1
            incidence[(middle, right)] += 1
            incidence[(left, right)] += 1

        local_maximum = max(incidence.values(), default=0)
        maximum_pair_multiplicity = max(maximum_pair_multiplicity, local_maximum)
        if local_maximum > 2:
            raise AssertionError("one physical pair belongs to more than two three-APs")

        load3 = sum(
            (Fraction(1, middle - left) for left, middle, _right in aps3),
            Fraction(),
        )
        full_edge = Fraction(5, 2) * load3
        pairs = tuple(combinations(sorted(values), 2))
        energy = sum((pair_weight(pair) for pair in pairs), Fraction())
        incidence_energy = sum(
            (multiplicity * pair_weight(pair) for pair, multiplicity in incidence.items()),
            Fraction(),
        )
        if incidence_energy != full_edge:
            raise AssertionError("full-edge incidence identity failed")
        if full_edge > 2 * energy:
            raise AssertionError("full-edge production exceeds twice pair energy")

        ratio = full_edge / energy if energy else Fraction()
        if ratio > maximum_ratio:
            maximum_ratio = ratio
            maximum_ratio_witness = tuple(sorted(values))

        rows.append(
            (
                tuple(sorted(values)),
                tuple(aps3),
                tuple(sorted(incidence.items())),
                str(full_edge),
                str(energy),
            )
        )

    expected_sets = 2233
    if counts["four_ap_free_sets"] != expected_sets:
        raise AssertionError(
            f"four-AP-free set count changed: {counts['four_ap_free_sets']}"
        )
    if maximum_pair_multiplicity != 2:
        raise AssertionError("sharp pair-incidence multiplicity two was not observed")

    payload = {
        "schema": "full_edge_incidence_pair_energy_small_box_v1",
        "universe": [1, upper],
        "counts": dict(sorted(counts.items())),
        "maximum_pair_three_ap_multiplicity": maximum_pair_multiplicity,
        "maximum_observed_full_edge_over_pair_energy": {
            "fraction": str(maximum_ratio),
            "decimal": f"{float(maximum_ratio):.12f}",
            "witness": maximum_ratio_witness,
        },
        "rows_sha256": hashlib.sha256(
            json.dumps(rows, separators=(",", ":")).encode("utf-8")
        ).hexdigest(),
        "checks": {
            "pair_multiplicity_at_most_two": True,
            "full_edge_incidence_identity": True,
            "full_edge_at_most_twice_pair_energy": True,
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("verified: full-edge incidence bounded by twice physical pair energy")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
