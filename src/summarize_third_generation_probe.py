#!/usr/bin/env python3
"""Emit compact exact brackets and metrics from the third-generation probe."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def parse_fraction(text: str) -> Fraction:
    numerator, denominator = text.split("/", 1)
    return Fraction(int(numerator), int(denominator))


def bracket(value: Fraction, denominator: int = 1_000_000) -> list[str]:
    lower_numerator = (value.numerator * denominator) // value.denominator
    lower = Fraction(lower_numerator, denominator)
    upper = Fraction(lower_numerator + 1, denominator)
    return [
        f"{lower.numerator}/{lower.denominator}",
        f"{upper.numerator}/{upper.denominator}",
    ]


def decimal_text(value: Fraction, places: int = 12) -> str:
    scale = 10 ** places
    rounded = (value.numerator * scale * 2 + value.denominator) // (2 * value.denominator)
    whole, fraction = divmod(rounded, scale)
    return f"{whole}.{fraction:0{places}d}"


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: summarize_third_generation_probe.py PROBE_JSON")
    source = Path(sys.argv[1])
    payload = json.loads(source.read_text(encoding="utf-8"))
    ratios = {
        name: parse_fraction(text)
        for name, text in payload["ratios"].items()
    }
    selected_metrics = {
        key: payload["metrics"][key]
        for key in (
            "recursive_second_parent_states",
            "recursive_second_parent_points",
            "child_selected_actions",
            "child_terminal_residual_points",
            "raw_occurrences",
            "raw_occurrence_points",
            "exact_state_classes",
            "conflict_edges",
            "conflict_components",
            "largest_conflict_component",
            "components_with_nonunique_optimum",
            "dp_states_examined",
            "retained_states",
            "retained_points",
            "terminal_third_states",
            "terminal_third_points",
            "recursive_third_states",
            "recursive_third_points",
            "third_same_token_recreation_count",
            "third_terminal_same_token_recreation_count",
            "third_recursive_same_token_recreation_count",
            "third_numerical_recreation_count",
            "third_terminal_numerical_recreation_count",
            "third_recursive_numerical_recreation_count",
            "third_exact_terminal_state_regeneration_count",
            "earlier_raw_token_collision_count",
            "earlier_retained_token_collision_count",
            "third_root_provenance_distinct",
            "third_root_provenance_repeated",
            "third_root_provenance_max_multiplicity",
        )
    }
    summary = {
        "schema": "third_generation_recursive_frontier_probe_summary_v1",
        "source_probe_payload_sha256": payload["probe_payload_sha256"],
        "metrics": selected_metrics,
        "ratio_decimals": {
            name: decimal_text(value) for name, value in ratios.items()
        },
        "ratio_brackets_millionth": {
            name: bracket(value) for name, value in ratios.items()
        },
        "ratio_hashes": payload["ratio_hashes"],
        "mass_hashes": payload["mass_hashes"],
        "hashes": payload["hashes"],
        "same_token_recreation": payload["collisions"][
            "second_terminal_vs_third_all_tokens"
        ],
        "same_token_recreation_terminal": payload["collisions"][
            "second_terminal_vs_third_terminal_tokens"
        ],
        "same_token_recreation_recursive": payload["collisions"][
            "second_terminal_vs_third_recursive_tokens"
        ],
        "exact_terminal_state_regeneration": payload["collisions"][
            "second_terminal_exact_state_vs_third"
        ],
    }
    print(json.dumps(summary, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
