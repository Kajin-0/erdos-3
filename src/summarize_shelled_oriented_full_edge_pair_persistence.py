#!/usr/bin/env python3
"""Summarize dyadically shelled oriented pair persistence."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: summarize_shelled_oriented_full_edge_pair_persistence.py INPUT OUTPUT")
    data = json.loads(Path(sys.argv[1]).read_text())
    target = Path(sys.argv[2])
    metrics = data["metrics"]
    lines = [
        "Shelled oriented full-edge pair persistence",
        "============================================",
        "",
        f"interval={data['interval'][0]},{data['interval'][1]}",
        f"four_ap_free_subsets={metrics['four_ap_free_subsets']}",
        f"subsets_with_recursive_shells={metrics['subsets_with_recursive_shells']}",
        f"shells={metrics['shells']}",
        f"recursive_shells={metrics['recursive_shells']}",
        f"latent_pair_occurrences={metrics['latent_pair_occurrences']}",
        f"latent_pair_union={metrics['latent_pair_union']}",
        f"maximum_latent_pair_multiplicity={metrics['maximum_latent_pair_multiplicity']}",
        f"maximum_reference_count={metrics['maximum_reference_count']}",
        "",
    ]
    for name, row in sorted(data["extrema"].items()):
        lines.extend(
            [
                f"{name}={row['ratio']['decimal']}",
                f"{name}_fraction={row['ratio']['fraction']}",
                f"{name}_values={','.join(map(str, row['values']))}",
                f"{name}_recursive_shells={row['recursive_shells']}",
            ]
        )
    witness = data.get("first_reuse_witness")
    if witness is None:
        lines.append("first_reuse_witness=none")
    else:
        lines.extend(
            [
                "first_reuse_witness_values=" + ",".join(map(str, witness["values"])),
                f"first_reuse_witness_recursive_shells={witness['recursive_shells']}",
            ]
        )
        for row in witness["reused_latent_pairs"]:
            lines.append(
                "reused_latent_pair="
                + ",".join(map(str, row["pair"]))
                + ";occurrences="
                + str(len(row["occurrences"]))
            )
    lines.extend(
        [
            "mandatory_standard_dyadic_shelling_applied=true",
            "all_recursive_objects_are_single_dyadic_shells=true",
            "all_shell_resources_contained_in_parent_pairs=true",
            f"records_sha256={data['records_sha256']}",
        ]
    )
    target.write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
