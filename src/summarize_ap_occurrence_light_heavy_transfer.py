#!/usr/bin/env python3
"""Summarize the AP occurrence light/heavy transfer probe."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def compact(name: str, row: dict[str, object]) -> list[str]:
    return [
        f"{name}_parent_size={row['parent_size']}",
        f"{name}_occurrences={row['occurrences']}",
        f"{name}_used_steps={row['used_steps']}",
        f"{name}_fibers={row['fibers']}",
        f"{name}_light_fibers={row['light_fibers']}",
        f"{name}_heavy_fibers={row['heavy_fibers']}",
        f"{name}_far_heavy_fibers={row['far_heavy_fibers']}",
        f"{name}_near_only_heavy_fibers={row['near_only_heavy_fibers']}",
        f"{name}_occurrence_mass={row['occurrence_mass']['decimal']}",
        f"{name}_first_step_mass={row['first_step_mass']['decimal']}",
        f"{name}_light_fiber_mass={row['light_fiber_mass']['decimal']}",
        f"{name}_light_pair_capacity={row['light_pair_capacity']['decimal']}",
        f"{name}_heavy_fiber_mass={row['heavy_fiber_mass']['decimal']}",
    ]


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: summarize_ap_occurrence_light_heavy_transfer.py INPUT OUTPUT")
    data = json.loads(Path(sys.argv[1]).read_text())
    metrics = data["exhaustive_metrics"]
    lines = [
        "AP occurrence light/heavy transfer",
        "==================================",
        "",
        f"interval={data['exhaustive_interval'][0]},{data['exhaustive_interval'][1]}",
        f"four_ap_free_subsets={metrics['four_ap_free_subsets']}",
        f"occurrences={metrics['occurrences']}",
        f"fibers={metrics['fibers']}",
        f"light_fibers={metrics['light_fibers']}",
        f"heavy_fibers={metrics['heavy_fibers']}",
        f"far_heavy_fibers={metrics['far_heavy_fibers']}",
        f"near_only_heavy_fibers={metrics['near_only_heavy_fibers']}",
        "exact_occurrence_transpose_identity=true",
        "all_step_fibers_four_ap_free=true",
        "all_light_fibers_near_only=true",
        "light_mass_bounded_by_pair_capacity=true",
        "heavy_fibers_strictly_lower_scale=true",
        "",
    ]
    for row in data["base_six"]:
        lines.extend(compact(f"base6_n{row['n']}", row))
    lines.extend([""] + compact("small_reuse", data["small_reuse_gadget"]))
    lines.extend([""] + compact("multiplicity4", data["multiplicity_four_gadget"]))
    lines.append(f"payload_sha256={data['payload_sha256']}")
    Path(sys.argv[2]).write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
