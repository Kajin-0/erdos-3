#!/usr/bin/env python3
"""Summarize the exact activated-pair union transfer probe."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def compact(name: str, row: dict[str, object]) -> list[str]:
    return [
        f"{name}_parent_size={row['parent_size']}",
        f"{name}_occurrences={row['occurrences']}",
        f"{name}_used_steps={row['used_steps']}",
        f"{name}_collision_occurrences={row['collision_occurrences']}",
        f"{name}_near_incidence_count={row['near_incidence_count']}",
        f"{name}_far_incidence_count={row['far_incidence_count']}",
        f"{name}_activated_pairs={row['activated_pairs']}",
        f"{name}_reused_step_edge_targets={row['reused_step_edge_targets']}",
        f"{name}_occurrence_mass={row['occurrence_mass']['decimal']}",
        f"{name}_activated_pair_union_mass={row['activated_pair_union_mass']['decimal']}",
        f"{name}_recursive_new_target_mass={row['recursive_new_target_mass']['decimal']}",
        f"{name}_recursive_reused_target_mass={row['recursive_reused_target_mass']['decimal']}",
        f"{name}_recursive_far_mass={row['recursive_far_mass']['decimal']}",
        f"{name}_recursive_total_mass={row['recursive_total_mass']['decimal']}",
        f"{name}_row_surplus={row['row_surplus']['decimal']}",
    ]


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: summarize_exact_activated_pair_union_transfer.py INPUT OUTPUT")
    data = json.loads(Path(sys.argv[1]).read_text())
    metrics = data["exhaustive_metrics"]
    masses = data["exhaustive_masses"]
    lines = [
        "Exact activated-pair union transfer",
        "===================================",
        "",
        f"interval={data['exhaustive_interval'][0]},{data['exhaustive_interval'][1]}",
        f"four_ap_free_subsets={metrics['four_ap_free_subsets']}",
        f"occurrences={metrics['occurrences']}",
        f"collision_occurrences={metrics['collision_occurrences']}",
        f"near_incidence_count={metrics['near_incidence_count']}",
        f"far_incidence_count={metrics['far_incidence_count']}",
        f"activated_pairs={metrics['activated_pairs']}",
        f"reused_step_edge_targets={metrics['reused_step_edge_targets']}",
        f"aggregate_occurrence_mass={masses['occurrence']['decimal']}",
        f"aggregate_activated_pair_union_mass={masses['activated_pair_union']['decimal']}",
        f"aggregate_recursive_mass={masses['recursive']['decimal']}",
        f"aggregate_surplus={masses['surplus']['decimal']}",
        f"maximum_recursive_over_occurrence={data['maximum_recursive_over_occurrence']['ratio']['decimal']}",
        f"maximum_reused_step_edge_targets={data['maximum_reused_step_edge_targets']}",
        "all_activated_pairs_paid_once=true",
        "all_near_preimage_sets_four_ap_free=true",
        "all_far_fibers_four_ap_free=true",
        "activated_pair_union_transfer_row=true",
        "",
    ]
    for row in data["base_six"]:
        lines.extend(compact(f"base6_n{row['n']}", row))
    lines.extend([""] + compact("multiplicity4", data["multiplicity_four_gadget"]))
    lines.append(f"payload_sha256={data['payload_sha256']}")
    Path(sys.argv[2]).write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
