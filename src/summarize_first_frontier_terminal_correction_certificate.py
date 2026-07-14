#!/usr/bin/env python3
"""Summarize the independent first-frontier correction certificate."""
from __future__ import annotations

import json
from pathlib import Path
import sys


def mass(record: dict[str, str]) -> str:
    return record["decimal"]


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "usage: summarize_first_frontier_terminal_correction_certificate.py INPUT OUTPUT",
            file=sys.stderr,
        )
        return 2
    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if payload.get("schema") != "first_frontier_terminal_correction_certificate_v1":
        raise AssertionError("unexpected first-frontier certificate schema")

    counts = payload["counts"]
    profiles = payload["profiles"]
    ratios = payload["ratios"]
    deltas = payload["refinement_deltas"]
    history = payload["historical_minus_corrected"]

    lines = [
        "First-frontier terminal correction certificate",
        "==============================================",
        "",
        f"terminal_parent_indices={','.join(map(str, payload['terminal_parent_indices']))}",
        (
            f"F1 states={counts['first_states']} points={counts['first_points']} "
            f"terminal={counts['first_terminal_states']}/{counts['first_terminal_points']} "
            f"recursive={counts['first_recursive_states']}/{counts['first_recursive_points']}"
        ),
        (
            f"historical_F2 states={counts['historical_states']} points={counts['historical_points']} "
            f"terminal={counts['historical_terminal_states']}/{counts['historical_terminal_points']} "
            f"recursive={counts['historical_recursive_states']}/{counts['historical_recursive_points']}"
        ),
        (
            f"corrected_F2 states={counts['corrected_states']} points={counts['corrected_points']} "
            f"terminal={counts['corrected_terminal_states']}/{counts['corrected_terminal_points']} "
            f"recursive={counts['corrected_recursive_states']}/{counts['corrected_recursive_points']}"
        ),
        (
            f"refined_F2 states={counts['refined_states']} points={counts['refined_points']} "
            f"terminal={counts['refined_terminal_states']}/{counts['refined_terminal_points']} "
            f"recursive={counts['refined_recursive_states']}/{counts['refined_recursive_points']}"
        ),
        "",
        f"F1_terminal_mass={mass(profiles['first']['terminal_mass'])}",
        f"F1_recursive_mass={mass(profiles['first']['recursive_mass'])}",
        f"F1_terminal_share={mass(ratios['first_terminal_share'])}",
        f"historical_F2_recursive_mass={mass(profiles['historical_f2']['recursive_mass'])}",
        f"corrected_F2_recursive_mass={mass(profiles['corrected_ordinary_f2']['recursive_mass'])}",
        f"refined_F2_recursive_mass={mass(profiles['corrected_refined_f2']['recursive_mass'])}",
        "",
        (
            "historical_recursive/F1_recursive="
            f"{mass(ratios['historical_recursive_over_first_recursive'])}"
        ),
        (
            "corrected_recursive/F1_recursive="
            f"{mass(ratios['corrected_recursive_over_first_recursive'])}"
        ),
        (
            "refined_recursive/F1_recursive="
            f"{mass(ratios['refined_recursive_over_first_recursive'])}"
        ),
        (
            "refinement_recursive_reduction_share="
            f"{mass(ratios['refinement_recursive_reduction_share'])}"
        ),
        "",
        f"historical_minus_corrected_total={mass(history['total'])}",
        f"historical_minus_corrected_terminal={mass(history['terminal'])}",
        f"historical_minus_corrected_recursive={mass(history['recursive'])}",
        f"refined_minus_corrected_total={mass(deltas['total'])}",
        f"refined_minus_corrected_terminal={mass(deltas['terminal'])}",
        f"refined_minus_corrected_recursive={mass(deltas['recursive'])}",
        "",
        f"certificate_payload_sha256={payload['certificate_payload_sha256']}",
    ]
    Path(sys.argv[2]).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
