#!/usr/bin/env python3
"""Emit a compact summary of the R3-to-F4 pair-resource diagnostic."""
from __future__ import annotations

from pathlib import Path
import json
import sys


def main() -> int:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/pair_resource_third_to_fourth_probe.json"
    )
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    parent = payload["parent"]
    child = payload["child"]
    containment = payload["containment"]
    type_counts = payload["type_counts"]
    bellman = payload["bellman"]
    lines = [
        "pair_resource_third_to_fourth_summary_v1",
        f"probe_payload_sha256={payload['probe_payload_sha256']}",
        f"parent_resources_sha256={payload['hashes']['parent_resources']}",
        f"child_resources_sha256={payload['hashes']['child_resources']}",
        f"missing_current_sha256={payload['hashes']['missing_current']}",
        f"missing_latent_sha256={payload['hashes']['missing_latent']}",
        f"generation_five_or_six_propagated_for_test={str(payload['generation_five_or_six_propagated_for_test']).lower()}",
        "",
        "[parent]",
    ]
    for key in (
        "recursive_states",
        "points",
        "affine_states",
        "nonaffine_states",
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
            f"affine_parent_classes={','.join(str(value) for value in parent['affine_parent_classes'])}",
            f"occurrence_resource_mass={parent['occurrence_resource_mass']['decimal']}",
            f"union_resource_mass={parent['union_resource_mass']['decimal']}",
            f"repeated_resource_mass={parent['repeated_resource_mass']['decimal']}",
            "",
            "[child]",
        ]
    )
    for key in (
        "total_states",
        "total_points",
        "terminal_states",
        "recursive_states",
        "resources_from_affine_parents",
        "distinct_resources_from_affine_parents",
        "maximum_resource_multiplicity",
        "repeated_resource_tokens",
        "terminal_current_pairs",
        "recursive_current_pairs",
        "recursive_latent_pairs",
        "points_from_nonaffine_parents",
    ):
        lines.append(f"{key}={child[key]}")
    lines.extend(
        [
            f"occurrence_resource_mass={child['occurrence_resource_mass']['decimal']}",
            f"union_resource_mass={child['union_resource_mass']['decimal']}",
            f"repeated_resource_mass={child['repeated_resource_mass']['decimal']}",
            f"current_mass_from_affine_parents={child['current_mass_from_affine_parents']['decimal']}",
            f"mass_from_nonaffine_parents={child['mass_from_nonaffine_parents']['decimal']}",
            "",
            "[containment]",
        ]
    )
    for key in (
        "missing_current_occurrences",
        "missing_current_pairs",
        "missing_latent_occurrences",
        "missing_latent_pairs",
    ):
        lines.append(f"{key}={containment[key]}")
    lines.extend(
        [
            f"missing_current_mass={containment['missing_current_mass']['decimal']}",
            f"missing_latent_mass={containment['missing_latent_mass']['decimal']}",
            f"all_affine_parent_resources_contained={str(containment['all_affine_parent_resources_contained']).lower()}",
            "",
            "[type_counts]",
        ]
    )
    for key in sorted(type_counts):
        lines.append(f"{key}={type_counts[key]}")
    lines.extend(["", "[bellman]"])
    for key in (
        "occurrence_left",
        "occurrence_right",
        "occurrence_surplus",
        "union_left",
        "union_right",
        "union_surplus",
    ):
        lines.append(f"{key}={bellman[key]['decimal']}")
    lines.extend(
        [
            f"occurrence_verified={str(bellman['occurrence_verified']).lower()}",
            f"union_verified={str(bellman['union_verified']).lower()}",
            "",
            "[nonaffine_parent_states]",
        ]
    )
    for row in parent["nonaffine_rows"]:
        lines.append(
            ";".join(
                [
                    f"class={row['state_class']}",
                    f"source={row['source']}",
                    f"step={row['source_step']}",
                    f"exponent={row['exponent']}",
                    f"size={row['size']}",
                    f"distinct_roots={row['distinct_roots']}",
                    f"H={row['harmonic_mass']['decimal']}",
                    f"tokens_sha256={row['tokens_sha256']}",
                ]
            )
        )
    lines.extend(["", "[missing_current_examples]"])
    for left, right, count in containment["missing_current_examples"]:
        lines.append(f"left={left};right={right};count={count}")
    lines.extend(["", "[missing_latent_examples]"])
    for left, right, count in containment["missing_latent_examples"]:
        lines.append(f"left={left};right={right};count={count}")
    text = "\n".join(lines) + "\n"
    if output_path is None:
        print(text, end="")
    else:
        output_path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
