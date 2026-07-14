#!/usr/bin/env python3
"""Emit compact pair-resource summaries for R1->F2 and R2->F3."""
from __future__ import annotations

from pathlib import Path
import json
import sys


def main() -> int:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/pair_resource_early_transitions_probe.json"
    )
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    lines = [
        "pair_resource_early_transitions_summary_v1",
        f"probe_payload_sha256={payload['probe_payload_sha256']}",
        f"transition_summaries_sha256={payload['hashes']['transition_summaries']}",
        f"later_generation_propagated_for_test={str(payload['later_generation_propagated_for_test']).lower()}",
    ]
    for row in payload["transitions"]:
        parent = row["parent"]
        child = row["child"]
        containment = row["containment"]
        bellman = row["bellman"]
        lines.extend(["", f"[{row['name']}]", "parent:"])
        for key in (
            "states",
            "points",
            "affine_states",
            "resource_occurrences",
            "distinct_resources",
            "maximum_resource_multiplicity",
            "repeated_resource_tokens",
            "current_pairs",
            "latent_pairs",
        ):
            lines.append(f"{key}={parent[key]}")
        lines.extend(
            [
                f"occurrence_resource_mass={parent['occurrence_resource_mass']['decimal']}",
                f"union_resource_mass={parent['union_resource_mass']['decimal']}",
                f"repeated_resource_mass={parent['repeated_resource_mass']['decimal']}",
                "child:",
            ]
        )
        for key in (
            "total_states",
            "total_points",
            "terminal_states",
            "recursive_states",
            "affine_states",
            "resource_occurrences",
            "distinct_resources",
            "maximum_resource_multiplicity",
            "repeated_resource_tokens",
            "terminal_current_pairs",
            "recursive_current_pairs",
            "recursive_latent_pairs",
        ):
            lines.append(f"{key}={child[key]}")
        lines.extend(
            [
                f"occurrence_resource_mass={child['occurrence_resource_mass']['decimal']}",
                f"union_resource_mass={child['union_resource_mass']['decimal']}",
                f"repeated_resource_mass={child['repeated_resource_mass']['decimal']}",
                "containment:",
                f"all_resources_contained={str(containment['all_resources_contained']).lower()}",
                f"missing_current_occurrences={containment['missing_current_occurrences']}",
                f"missing_latent_occurrences={containment['missing_latent_occurrences']}",
                "bellman:",
                f"occurrence_left={bellman['occurrence_left']['decimal']}",
                f"occurrence_right={bellman['occurrence_right']['decimal']}",
                f"occurrence_surplus={bellman['occurrence_surplus']['decimal']}",
                f"occurrence_ratio={bellman['occurrence_ratio']['decimal']}",
                f"occurrence_verified={str(bellman['occurrence_verified']).lower()}",
                f"union_left={bellman['union_left']['decimal']}",
                f"union_right={bellman['union_right']['decimal']}",
                f"union_surplus={bellman['union_surplus']['decimal']}",
                f"union_ratio={bellman['union_ratio']['decimal']}",
                f"union_verified={str(bellman['union_verified']).lower()}",
                "type_counts:",
            ]
        )
        for key in sorted(row["type_counts"]):
            lines.append(f"{key}={row['type_counts'][key]}")
        lines.extend(
            [
                f"parent_resources_sha256={row['hashes']['parent_resources']}",
                f"child_resources_sha256={row['hashes']['child_resources']}",
                f"parent_references_sha256={row['hashes']['parent_references']}",
            ]
        )
    text = "\n".join(lines) + "\n"
    if output_path is None:
        print(text, end="")
    else:
        output_path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
