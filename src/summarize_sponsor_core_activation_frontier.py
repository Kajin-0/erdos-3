#!/usr/bin/env python3
"""Write a compact deterministic summary of the sponsor-core activation probe."""
from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import sys


def mass(record: dict[str, str]) -> str:
    return record["decimal"]


def fraction(record: dict[str, str]) -> Fraction:
    return Fraction(record["fraction"])


def signed(value: int) -> str:
    return f"{value:+d}"


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "usage: summarize_sponsor_core_activation_frontier.py INPUT_JSON OUTPUT_TXT",
            file=sys.stderr,
        )
        return 2

    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if payload.get("schema") != "sponsor_core_activation_frontier_probe_v1":
        raise AssertionError("unexpected sponsor-core activation probe schema")

    lines = [
        "Sponsor-core activation frontier",
        "================================",
        "",
        f"scope: {payload['scope']}",
        f"generation_six_propagated: {str(payload['generation_six_propagated']).lower()}",
        f"probe_payload_sha256: {payload['probe_payload_sha256']}",
        "",
        "Symbolic identities checked",
        "---------------------------",
    ]
    for key, value in payload["symbolic_identities"].items():
        lines.append(f"{key}: {value}")

    for row in payload["transitions"]:
        parents = row["parents"]
        available = row["available_pair_resources"]
        activated = row["activated_recursive_resources"]
        ratios = row["candidate_ratios"]
        frontier = row["retained_frontier"]
        baseline = frontier["baseline"]
        refined = frontier["refined"]

        lines.extend(
            [
                "",
                row["name"],
                "-" * len(row["name"]),
                (
                    f"parents={parents['states']} points={parents['points']} "
                    f"selected_actions={parents['selected_actions']}"
                ),
                (
                    f"selected_step_mass={mass(parents['selected_step_mass'])} "
                    f"deleted_sponsor_harmonic={mass(parents['deleted_sponsor_harmonic_mass'])}"
                ),
                (
                    f"sponsor_core_mass_occ={mass(available['sponsor_core_occurrence_mass'])} "
                    f"sponsor_core_mass_union={mass(available['sponsor_core_union_mass'])}"
                ),
                (
                    f"activated_mass_baseline_occ={mass(activated['baseline_occurrence_mass'])} "
                    f"refined_occ={mass(activated['refined_occurrence_mass'])} "
                    f"reduction={mass(activated['occurrence_mass_reduction'])}"
                ),
                (
                    f"activated_mass_baseline_union={mass(activated['baseline_union_mass'])} "
                    f"refined_union={mass(activated['refined_union_mass'])} "
                    f"reduction={mass(activated['union_mass_reduction'])}"
                ),
                (
                    "activation/selected_step="
                    f"{mass(ratios['refined_activation_over_selected_step_mass'])} "
                    "union_activation/selected_step="
                    f"{mass(ratios['refined_union_activation_over_selected_step_mass'])}"
                ),
                (
                    f"activation/core_occ={mass(ratios['refined_activation_over_sponsor_core_occurrence'])} "
                    f"activation/action_edges={mass(ratios['refined_activation_over_action_edge_mass'])}"
                ),
                (
                    f"direct_action_edge_mass={mass(activated['direct_action_edge_mass'])} "
                    f"nondirect_mass={mass(activated['nondirect_mass'])} "
                    f"direct_share={mass(activated['direct_mass_share'])}"
                ),
                (
                    f"recursive_points {baseline['recursive_points']} -> {refined['recursive_points']} "
                    f"({signed(frontier['recursive_point_change'])})"
                ),
                (
                    f"terminal_points {baseline['terminal_points']} -> {refined['terminal_points']} "
                    f"({signed(frontier['terminal_point_change'])})"
                ),
                (
                    f"recursive_mass_change={mass(frontier['recursive_mass_change'])} "
                    f"terminal_mass_change={mass(frontier['terminal_mass_change'])}"
                ),
                (
                    "maximum_parent_activation/selected_step="
                    f"{mass(row['parent_extrema']['maximum_activation_over_selected_step'])}"
                ),
                "activated distance/selected-step profile:",
            ]
        )
        for scale_row in activated["scale_profile"]:
            lines.append(
                "  "
                f"k={scale_row['floor_log2_distance_over_selected_step']:+d} "
                f"occ={scale_row['resource_occurrences']} "
                f"mass={mass(scale_row['mass'])}"
            )

    finite = payload["finite_candidate_constants"]
    lines.extend(
        [
            "",
            "Finite candidate constant",
            "-------------------------",
            (
                "max activated occurrence mass / selected-step mass = "
                f"{mass(finite['maximum_refined_activation_over_selected_step_mass'])} "
                f"at {finite['attained_at']}"
            ),
            (
                "max activated union mass / selected-step mass = "
                f"{mass(finite['maximum_refined_union_activation_over_selected_step_mass'])} "
                f"at {finite['union_attained_at']}"
            ),
        ]
    )

    Path(sys.argv[2]).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
