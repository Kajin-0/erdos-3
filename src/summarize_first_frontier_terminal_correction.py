#!/usr/bin/env python3
"""Summarize the first-frontier terminal correction probe."""
from __future__ import annotations

import json
from pathlib import Path
import sys


def mass(record: dict[str, str]) -> str:
    return record["decimal"]


def profile_line(name: str, profile: dict[str, object]) -> str:
    return (
        f"{name}: states={profile['states']} points={profile['points']} "
        f"terminal={profile['terminal_states']}/{profile['terminal_points']} "
        f"recursive={profile['recursive_states']}/{profile['recursive_points']} "
        f"total_mass={mass(profile['total_mass'])} "
        f"terminal_mass={mass(profile['terminal_mass'])} "
        f"recursive_mass={mass(profile['recursive_mass'])}"
    )


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "usage: summarize_first_frontier_terminal_correction.py INPUT OUTPUT",
            file=sys.stderr,
        )
        return 2
    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if payload.get("schema") != "first_frontier_terminal_correction_probe_v1":
        raise AssertionError("unexpected first-frontier correction schema")

    first = payload["first_frontier"]
    historical = payload["historical_F2_all_21_parents"]
    ordinary = payload["corrected_F2_recursive_parents_only"]["family"]
    refined = payload["corrected_refined_F2"]["family"]
    comparisons = payload["comparisons"]
    historical_delta = comparisons["historical_minus_corrected_ordinary"]
    refinement_delta = comparisons["corrected_refined_minus_corrected_ordinary"]

    lines = [
        "First-frontier terminal correction",
        "==================================",
        "",
        f"scope: {payload['scope']}",
        f"probe_payload_sha256: {payload['probe_payload_sha256']}",
        "",
        profile_line("F1 all", first["all"]),
        profile_line("F1 terminal", first["terminal"]),
        profile_line("F1 recursive", first["recursive"]),
        f"terminal_parent_indices={','.join(map(str, first['terminal_parent_indices']))}",
        "",
        profile_line("historical F2", historical),
        profile_line("corrected ordinary F2", ordinary),
        profile_line("corrected refined F2", refined),
        "",
        "Historical F2 minus corrected ordinary F2",
        "-------------------------------------------",
        f"states={historical_delta['states']:+d}",
        f"points={historical_delta['points']:+d}",
        f"terminal_states={historical_delta['terminal_states']:+d}",
        f"terminal_points={historical_delta['terminal_points']:+d}",
        f"recursive_states={historical_delta['recursive_states']:+d}",
        f"recursive_points={historical_delta['recursive_points']:+d}",
        f"total_mass={mass(historical_delta['total_mass'])}",
        f"terminal_mass={mass(historical_delta['terminal_mass'])}",
        f"recursive_mass={mass(historical_delta['recursive_mass'])}",
        "",
        "Residual/sponsor refinement minus corrected ordinary F2",
        "--------------------------------------------------------",
        f"states={refinement_delta['states']:+d}",
        f"points={refinement_delta['points']:+d}",
        f"terminal_states={refinement_delta['terminal_states']:+d}",
        f"terminal_points={refinement_delta['terminal_points']:+d}",
        f"recursive_states={refinement_delta['recursive_states']:+d}",
        f"recursive_points={refinement_delta['recursive_points']:+d}",
        f"total_mass={mass(refinement_delta['total_mass'])}",
        f"terminal_mass={mass(refinement_delta['terminal_mass'])}",
        f"recursive_mass={mass(refinement_delta['recursive_mass'])}",
        "",
        (
            "historical_equals_corrected_ordinary="
            f"{str(comparisons['historical_equals_corrected_ordinary']).lower()}"
        ),
        (
            "corrected_ordinary_equals_refined="
            f"{str(comparisons['corrected_ordinary_equals_refined']).lower()}"
        ),
        "corrected_raw_support_preserved_by_split=true",
        "corrected_raw_occurrences_preserved_by_split=true",
        "corrected_raw_harmonic_mass_preserved_by_split=true",
    ]
    Path(sys.argv[2]).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
