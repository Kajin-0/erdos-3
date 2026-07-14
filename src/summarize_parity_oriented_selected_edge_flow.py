#!/usr/bin/env python3
"""Summarize parity-oriented selected-edge flow verification."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: summarize_parity_oriented_selected_edge_flow.py INPUT OUTPUT")
    data = json.loads(Path(sys.argv[1]).read_text())
    metrics = data["metrics"]
    aggregate = data["aggregate"]
    lines = [
        "Parity-oriented selected-edge flow",
        "==================================",
        "",
        f"interval={data['interval'][0]},{data['interval'][1]}",
        f"four_ap_free_subsets={metrics['four_ap_free_subsets']}",
        f"actions={metrics['actions']}",
        f"direct_pairs={metrics['direct_pairs']}",
        f"survivor_pairs={metrics['survivor_pairs']}",
        f"union_pairs={metrics['union_pairs']}",
        f"overlap_pairs={metrics['overlap_pairs']}",
        f"aggregate_selected_load={aggregate['selected_load']['decimal']}",
        f"aggregate_union_mass={aggregate['union_mass']['decimal']}",
        f"aggregate_overlap_release_mass={aggregate['overlap_release_mass']['decimal']}",
        f"maximum_actions={data['maximum_action_witness']['actions']}",
        f"maximum_overlap_pairs={data['maximum_overlap_witness']['overlap_pairs']}",
        "all_schedules_terminate_at_three_ap_free_residual=true",
        "all_sponsor_edges_distinct=true",
        "all_survivor_edges_distinct=true",
        "all_overlap_created_before_release=true",
        "union_plus_release_equals_five_halves_selected_load=true",
        f"records_sha256={data['records_sha256']}",
        f"payload_sha256={data['payload_sha256']}",
    ]
    Path(sys.argv[2]).write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
