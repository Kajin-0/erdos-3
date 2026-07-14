#!/usr/bin/env python3
"""Summarize exact generation-aware feature intervals compactly."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def parse_fraction(text: str | None) -> Fraction | None:
    if text is None:
        return None
    numerator, denominator = text.split("/", 1)
    return Fraction(int(numerator), int(denominator))


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def fraction_hash(value: Fraction | None) -> str | None:
    if value is None:
        return None
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def decimal_text(value: Fraction | None, places: int = 12) -> str | None:
    if value is None:
        return None
    sign = "-" if value < 0 else ""
    value = abs(value)
    scale = 10 ** places
    rounded = (value.numerator * scale * 2 + value.denominator) // (
        2 * value.denominator
    )
    whole, fractional = divmod(rounded, scale)
    return f"{sign}{whole}.{fractional:0{places}d}"


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: summarize_generation_aware_feature_probe.py PROBE_JSON"
        )
    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    intervals = {}
    for feature, row in payload[
        "single_feature_intervals_with_current_mass_coefficient_1"
    ].items():
        lower = parse_fraction(row["lower"])
        upper = parse_fraction(row["upper"])
        witness = parse_fraction(row["witness"])
        intervals[feature] = {
            "feasible": bool(row["feasible"]),
            "lower_decimal": decimal_text(lower),
            "upper_decimal": decimal_text(upper),
            "witness_decimal": decimal_text(witness),
            "lower_sha256": fraction_hash(lower),
            "upper_sha256": fraction_hash(upper),
            "witness_sha256": fraction_hash(witness),
        }
    summary = {
        "schema": "generation_aware_feature_profiles_summary_v1",
        "source_probe_payload_sha256": payload["probe_payload_sha256"],
        "family_counts": payload["family_counts"],
        "feature_decimals": payload["feature_decimals"],
        "feature_hashes": payload["feature_hashes"],
        "difference_decimals": payload["difference_decimals"],
        "difference_hashes": payload["difference_hashes"],
        "single_feature_intervals": intervals,
        "feasible_features": sorted(
            feature for feature, row in intervals.items() if row["feasible"]
        ),
        "infeasible_features": sorted(
            feature for feature, row in intervals.items() if not row["feasible"]
        ),
    }
    canonical = json.dumps(summary, sort_keys=True, separators=(",", ":"))
    summary["summary_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(summary, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
