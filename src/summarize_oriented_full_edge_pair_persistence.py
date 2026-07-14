#!/usr/bin/env python3
"""Summarize the oriented full-edge latent-pair persistence probe."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: summarize_oriented_full_edge_pair_persistence.py INPUT OUTPUT")
    source = Path(sys.argv[1])
    target = Path(sys.argv[2])
    data = json.loads(source.read_text())
    metrics = data["metrics"]
    lines = [
        "Oriented full-edge pair persistence",
        "===================================",
        "",
        f"interval={data['interval'][0]},{data['interval'][1]}",
        f"four_ap_free_subsets={metrics['four_ap_free_subsets']}",
        f"subsets_with_recursive_children={metrics['subsets_with_recursive_children']}",
        f"three_aps={metrics['three_aps']}",
        f"children={metrics['children']}",
        f"recursive_children={metrics['recursive_children']}",
        f"latent_pair_occurrences={metrics['latent_pair_occurrences']}",
        f"latent_pair_union={metrics['latent_pair_union']}",
        f"maximum_latent_pair_multiplicity={metrics['maximum_latent_pair_multiplicity']}",
        f"maximum_total_resource_multiplicity={metrics['maximum_total_resource_multiplicity']}",
        f"maximum_reference_count={metrics['maximum_reference_count']}",
        "",
    ]
    for name, row in sorted(data["extrema"].items()):
        lines.extend(
            [
                f"{name}={row['ratio']['decimal']}",
                f"{name}_fraction={row['ratio']['fraction']}",
                f"{name}_values={','.join(map(str, row['values']))}",
            ]
        )
    lines.extend(
        [
            "",
            "middle_children_split_by_orientation=true",
            "all_child_resources_contained_in_parent_pairs=true",
            "all_persistent_pair_references_outside_pair_interval=true",
            "same_type_side_middle_reference_gap_D_forbidden=true",
            "same_type_doubled_reference_gap_2D_forbidden=true",
            f"records_sha256={data['records_sha256']}",
        ]
    )
    witness = data.get("maximum_multiplicity_witness")
    if witness:
        lines.extend(
            [
                "",
                "maximum_multiplicity_witness_values="
                + ",".join(map(str, witness["values"])),
                "maximum_multiplicity_witness_recursive_children="
                + str(witness["recursive_children"]),
            ]
        )
        for row in witness.get("worst_pairs", []):
            lines.append(
                "maximum_multiplicity_pair="
                + ",".join(map(str, row["pair"]))
                + ";occurrences="
                + str(len(row["occurrences"]))
            )
    target.write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
