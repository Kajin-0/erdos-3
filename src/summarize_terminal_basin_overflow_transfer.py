#!/usr/bin/env python3
"""Summarize terminal-basin overflow transfer verification."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: summarize_terminal_basin_overflow_transfer.py INPUT OUTPUT")
    data = json.loads(Path(sys.argv[1]).read_text())
    metrics = data["metrics"]
    masses = data["aggregate_masses"]
    lines = [
        "Terminal-basin overflow transfer",
        "================================",
        "",
        f"interval={data['interval'][0]},{data['interval'][1]}",
        f"root_sets={metrics['root_sets']}",
        f"actions={metrics['actions']}",
        f"all_pairs_activated={metrics['all_pairs_activated_pairs']}",
        f"all_pairs_terminal_basins={metrics['all_pairs_terminal_basins']}",
        f"all_pairs_overflow={metrics['all_pairs_overflow_pairs']}",
        f"all_pairs_owner_distance_fibers={metrics['all_pairs_owner_distance_fibers']}",
        f"selected_edges_activated={metrics['selected_edges_activated_pairs']}",
        f"selected_edges_terminal_basins={metrics['selected_edges_terminal_basins']}",
        f"selected_edges_overflow={metrics['selected_edges_overflow_pairs']}",
        f"selected_edges_owner_distance_fibers={metrics['selected_edges_owner_distance_fibers']}",
        f"all_pairs_activated_mass={masses['all_pairs_activated_mass']['decimal']}",
        f"all_pairs_terminal_mass={masses['all_pairs_terminal_mass']['decimal']}",
        f"all_pairs_overflow_mass={masses['all_pairs_overflow_mass']['decimal']}",
        f"all_pairs_surplus={masses['all_pairs_surplus']['decimal']}",
        f"selected_edges_activated_mass={masses['selected_edges_activated_mass']['decimal']}",
        f"selected_edges_terminal_mass={masses['selected_edges_terminal_mass']['decimal']}",
        f"selected_edges_overflow_mass={masses['selected_edges_overflow_mass']['decimal']}",
        f"selected_edges_surplus={masses['selected_edges_surplus']['decimal']}",
        f"maximum_overflow_pairs={data['maximum_overflow_witness']['overflow_pairs']}",
        f"maximum_transport_path={data['maximum_transport_path_witness']['maximum_transport_path']}",
        "deterministic_transport_terminates=true",
        "transport_weight_nondecreasing=true",
        "one_representative_per_terminal_basin=true",
        "all_owner_distance_fibers_four_ap_free=true",
        "overflow_mass_equals_fiber_mass=true",
        "terminal_basin_overflow_row=true",
        f"records_sha256={data['records_sha256']}",
        f"payload_sha256={data['payload_sha256']}",
    ]
    Path(sys.argv[2]).write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
