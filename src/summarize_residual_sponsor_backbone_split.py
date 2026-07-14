#!/usr/bin/env python3
"""Emit a compact summary of the residual/sponsor backbone split probe."""
from __future__ import annotations

from pathlib import Path
import json
import sys


def profile_lines(prefix: str, profile: dict[str, object]) -> list[str]:
    lines: list[str] = []
    for key in (
        "states",
        "points",
        "terminal_states",
        "terminal_points",
        "recursive_states",
        "recursive_points",
        "current_resource_occurrences",
        "current_distinct_resources",
        "latent_resource_occurrences",
        "latent_distinct_resources",
        "total_resource_occurrences",
        "total_distinct_resources",
        "maximum_resource_multiplicity",
        "repeated_resource_tokens",
    ):
        lines.append(f"{prefix}_{key}={profile[key]}")
    for key in (
        "terminal_mass",
        "recursive_mass",
        "total_mass",
        "occurrence_resource_mass",
        "union_resource_mass",
        "repeated_resource_mass",
    ):
        lines.append(f"{prefix}_{key}={profile[key]['decimal']}")
    return lines


def main() -> int:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/residual_sponsor_backbone_split_probe.json"
    )
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    baseline = payload["baseline"]
    split = payload["split"]
    comparison = payload["comparison"]
    lines = [
        "residual_sponsor_backbone_split_summary_v1",
        f"probe_payload_sha256={payload['probe_payload_sha256']}",
        f"split_occurrences_sha256={payload['hashes']['split_occurrences']}",
        f"split_retained_sha256={payload['hashes']['split_retained']}",
        f"baseline_profile_sha256={payload['hashes']['baseline_profile']}",
        f"split_profile_sha256={payload['hashes']['split_profile']}",
        f"generation_six_propagated={str(payload['generation_six_propagated']).lower()}",
        f"raw_support_union_preserved={str(payload['raw_support_union_preserved']).lower()}",
        f"raw_support_union_size={payload['raw_support_union_size']}",
        f"baseline_raw_occurrences={baseline['raw_occurrences']}",
        f"baseline_raw_occurrence_points={baseline['raw_occurrence_points']}",
        f"split_raw_occurrences={split['raw_occurrences']}",
        f"split_raw_occurrence_points={split['raw_occurrence_points']}",
        f"split_raw_source_counts={json.dumps(split['raw_source_counts'], sort_keys=True, separators=(',', ':'))}",
        f"split_retained_source_counts={json.dumps(split['retained_source_counts'], sort_keys=True, separators=(',', ':'))}",
        f"retained_residual_backbone_states={split['retained_residual_backbone_states']}",
        f"retained_residual_backbone_points={split['retained_residual_backbone_points']}",
        f"retained_residual_backbone_mass={split['retained_residual_backbone_mass']['decimal']}",
        "",
        "[baseline_profile]",
        *profile_lines("baseline", baseline["profile"]),
        "",
        "[split_profile]",
        *profile_lines("split", split["profile"]),
        "",
        "[comparison]",
        f"total_mass_delta={comparison['total_mass_delta']['decimal']}",
        f"terminal_mass_delta={comparison['terminal_mass_delta']['decimal']}",
        f"recursive_mass_delta={comparison['recursive_mass_delta']['decimal']}",
        f"recursive_points_delta={comparison['recursive_points_delta']}",
        f"latent_occurrences_delta={comparison['latent_occurrences_delta']}",
        f"union_resource_mass_delta={comparison['union_resource_mass_delta']['decimal']}",
        f"occurrence_resource_mass_delta={comparison['occurrence_resource_mass_delta']['decimal']}",
    ]
    text = "\n".join(lines) + "\n"
    if output_path is None:
        print(text, end="")
    else:
        output_path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
