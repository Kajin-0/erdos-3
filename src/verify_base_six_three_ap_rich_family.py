#!/usr/bin/env python3
"""Verify finite instances of the base-six three-AP-rich no-go family."""
from __future__ import annotations

from fractions import Fraction
from itertools import product
import hashlib
import json
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

MAX_N = 6


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def fraction_record(value: Fraction) -> dict[str, str]:
    text = f"{value.numerator}/{value.denominator}"
    return {
        "fraction": text,
        "decimal": f"{float(value):.12f}",
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }


def digit_set(n: int) -> frozenset[int]:
    powers = [6**index for index in range(n)]
    return frozenset(
        sum(digit * power for digit, power in zip(digits, powers, strict=True))
        for digits in product(range(3), repeat=n)
    )


def contains_four_ap(values: frozenset[int]) -> bool:
    ordered = sorted(values)
    lookup = values
    for index, left in enumerate(ordered):
        for second in ordered[index + 1 :]:
            step = second - left
            if second + step in lookup and second + 2 * step in lookup:
                return True
    return False


def all_three_ap_load(values: frozenset[int]) -> tuple[int, Fraction]:
    ordered = sorted(values)
    lookup = values
    count = 0
    load = Fraction()
    for index, left in enumerate(ordered):
        for middle in ordered[index + 1 :]:
            step = middle - left
            right = middle + step
            if right in lookup:
                count += 1
                load += Fraction(1, step)
    return count, load


def constructed_load(n: int) -> tuple[int, Fraction]:
    count = 0
    load = Fraction()
    for mask in range(1, 1 << n):
        size = mask.bit_count()
        step = sum(6**index for index in range(n) if mask & (1 << index))
        multiplicity = 3 ** (n - size)
        count += multiplicity
        load += Fraction(multiplicity, step)
    return count, load


def least_power_two_at_least(value: int) -> int:
    return 1 << (value - 1).bit_length()


def harmonic(values: frozenset[int]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction())


def main() -> int:
    rows = []
    for n in range(1, MAX_N + 1):
        raw = digit_set(n)
        if len(raw) != 3**n:
            raise AssertionError("digit-set cardinality mismatch")
        if contains_four_ap(raw):
            raise AssertionError(f"base-six family contains a four-AP at n={n}")

        expected_max = 2 * (6**n - 1) // 5
        if max(raw) != expected_max:
            raise AssertionError("digit-set maximum mismatch")

        explicit_count, explicit_load = constructed_load(n)
        if explicit_count != 4**n - 3**n:
            raise AssertionError("constructed three-AP count mismatch")

        all_count, total_load = all_three_ap_load(raw)
        if all_count < explicit_count or total_load < explicit_load:
            raise AssertionError("explicit progression family escaped full census")

        lower_load = Fraction(5 * (4**n - 3**n), 6**n)
        if not explicit_load > lower_load:
            raise AssertionError("strict aggregate weighted-load bound failed")

        unit_step_count = 3 ** (n - 1)
        if total_load < unit_step_count:
            raise AssertionError("unit-step progression load missing")

        base = least_power_two_at_least(6**n)
        shifted = frozenset(base + value for value in raw)
        if not all(base <= value < 2 * base for value in shifted):
            raise AssertionError("shifted family escaped standard dyadic block")
        if contains_four_ap(shifted):
            raise AssertionError("translation changed four-AP-freeness")

        shifted_harmonic = harmonic(shifted)
        harmonic_upper = Fraction(3**n, base)
        if shifted_harmonic > harmonic_upper:
            raise AssertionError("harmonic upper bound failed")
        ratio = total_load / shifted_harmonic
        aggregate_ratio_lower = Fraction(5 * (4**n - 3**n), 3**n)
        linear_scale_ratio_lower = Fraction(base, 3)
        if not ratio > aggregate_ratio_lower:
            raise AssertionError("aggregate load/harmonic lower bound failed")
        if ratio < linear_scale_ratio_lower:
            raise AssertionError("linear-scale load/harmonic lower bound failed")

        rows.append(
            {
                "n": n,
                "cardinality": len(raw),
                "maximum": max(raw),
                "dyadic_base": base,
                "four_ap_free": True,
                "unit_step_three_ap_count": unit_step_count,
                "explicit_three_ap_count": explicit_count,
                "all_three_ap_count": all_count,
                "explicit_weighted_load": fraction_record(explicit_load),
                "total_weighted_load": fraction_record(total_load),
                "strict_aggregate_load_lower_bound": fraction_record(lower_load),
                "unit_step_load_lower_bound": fraction_record(Fraction(unit_step_count)),
                "shifted_harmonic_mass": fraction_record(shifted_harmonic),
                "harmonic_upper_bound": fraction_record(harmonic_upper),
                "load_over_harmonic": fraction_record(ratio),
                "strict_aggregate_ratio_lower_bound": fraction_record(
                    aggregate_ratio_lower
                ),
                "linear_scale_ratio_lower_bound": fraction_record(
                    linear_scale_ratio_lower
                ),
                "family_sha256": canonical_hash(sorted(raw)),
            }
        )

    output = {
        "schema": "base_six_three_ap_rich_family_certificate_v2",
        "max_n": MAX_N,
        "rows": rows,
        "verified": {
            "all_digit_families_four_ap_free": True,
            "explicit_three_ap_count_equals_4n_minus_3n": True,
            "unit_step_three_ap_count_equals_3n_minus_1": True,
            "standard_dyadic_placement_valid": True,
            "load_over_harmonic_at_least_dyadic_base_over_three": True,
        },
    }
    output["payload_sha256"] = canonical_hash(output)
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
