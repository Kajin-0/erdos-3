#!/usr/bin/env python3
"""Emit compact pair-resource ownership diagnostics."""
from __future__ import annotations

from pathlib import Path
import json
import sys


def main() -> int:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/pair_resource_ownership_probe.json"
    )
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    counts = payload["counts"]
    masses = payload["masses"]
    lines = [
        "pair_resource_ownership_summary_v1",
        f"probe_payload_sha256={payload['probe_payload_sha256']}",
        f"parent_resources_sha256={payload['hashes']['parent_resources']}",
        f"child_resources_sha256={payload['hashes']['child_resources']}",
        f"child_rows_sha256={payload['hashes']['child_rows']}",
        f"unused_parent_pairs_sha256={payload['hashes']['unused_parent_pairs']}",
        f"generation_six_propagated={str(payload['generation_six_propagated']).lower()}",
        f"containment_verified={str(payload['containment_verified']).lower()}",
        f"partition_verified={str(payload['partition_verified']).lower()}",
        f"child_pair_disjointness_verified={str(payload['child_pair_disjointness_verified']).lower()}",
        "",
        "[counts]",
    ]
    for key in sorted(counts):
        lines.append(f"{key}={counts[key]}")
    lines.extend(["", "[masses]"])
    for key in sorted(masses):
        lines.append(f"{key}={masses[key]['decimal']};sha256={masses[key]['sha256']}")
    text = "\n".join(lines) + "\n"
    if output_path is None:
        print(text, end="")
    else:
        output_path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
