#!/usr/bin/env python3
"""Summarize the exact fourth-generation probe without collision detail bulk."""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: summarize_fourth_generation_probe.py PROBE_JSON")
    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    compact_collisions = {}
    for mode, row in payload["terminal_collisions"].items():
        terminal_signatures = [
            detail["signature"] for detail in row["terminal_details"]
        ]
        recursive_signatures = [
            detail["signature"] for detail in row["recursive_details"]
        ]
        compact_collisions[mode] = {
            "all_count": row["all_count"],
            "terminal_count": row["terminal_count"],
            "recursive_count": row["recursive_count"],
            "terminal_signatures": terminal_signatures,
            "recursive_signatures": recursive_signatures,
            "terminal_signatures_sha256": canonical_hash(terminal_signatures),
            "recursive_signatures_sha256": canonical_hash(recursive_signatures),
        }

    numerical = payload["numerical_recreation"]
    summary = {
        "schema": "fourth_generation_potential_frontier_summary_v1",
        "source_probe_payload_sha256": payload["probe_payload_sha256"],
        "family_counts": payload["family_counts"],
        "generation4_metrics": payload["generation4_metrics"],
        "feature_decimals": payload["feature_decimals"],
        "feature_hashes": payload["feature_hashes"],
        "potentials": payload["potentials"],
        "mass_ratios": payload["mass_ratios"],
        "terminal_collisions": compact_collisions,
        "numerical_recreation": {
            "terminal_value_count": len(numerical["terminal_values"]),
            "recursive_value_count": len(numerical["recursive_values"]),
            "exact_state_regeneration_count": len(
                numerical["exact_state_regeneration"]
            ),
            "terminal_values_sha256": canonical_hash(
                numerical["terminal_values"]
            ),
            "recursive_values_sha256": canonical_hash(
                numerical["recursive_values"]
            ),
            "exact_state_regeneration_sha256": canonical_hash(
                numerical["exact_state_regeneration"]
            ),
        },
        "hashes": payload["hashes"],
    }
    canonical = json.dumps(summary, sort_keys=True, separators=(",", ":"))
    summary["summary_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(summary, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
