#!/usr/bin/env python3
"""Emit a compact summary of the affine root-pivot probe."""
from __future__ import annotations

from pathlib import Path
import json
import sys


def main() -> int:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/affine_root_pivot_probe.json"
    )
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    counts = payload["counts"]
    lines = [
        "affine_root_pivot_summary_v1",
        f"probe_payload_sha256={payload['probe_payload_sha256']}",
        f"state_rows_sha256={payload['hashes']['state_rows']}",
        f"survivor_rows_sha256={payload['hashes']['survivor_rows']}",
        f"reference_roots_sha256={payload['hashes']['reference_roots']}",
        f"anchor_roots_sha256={payload['hashes']['anchor_roots']}",
        f"parent_states={counts['parent_states']}",
        f"affine_parent_states={counts['affine_parent_states']}",
        f"distinct_reference_roots={counts['distinct_reference_roots']}",
        f"reference_roots_in_first_root_universe={counts['reference_roots_in_first_root_universe']}",
        f"reference_roots_active_in_parent={counts['reference_roots_active_in_parent']}",
        f"distinct_anchor_roots={counts['distinct_anchor_roots']}",
        f"anchor_roots_in_first_root_universe={counts['anchor_roots_in_first_root_universe']}",
        f"anchor_roots_active_in_fifth={counts['anchor_roots_active_in_fifth']}",
        f"survivor_pivot_identities={counts['survivor_pivot_identities']}",
        f"total_interval_gain={payload['total_interval_gain']['decimal']}",
        "",
        "[state_pivots]",
    ]
    for row in sorted(payload["state_rows"], key=lambda item: item["parent_state_class"]):
        lines.append(
            ";".join(
                [
                    f"class={row['parent_state_class']}",
                    f"size={row['parent_size']}",
                    f"reference={row['reference_root']}",
                    f"reference_active={str(row['reference_active_in_parent']).lower()}",
                    f"minimum={row['minimum']}",
                    f"anchor={row['anchor_root']}",
                    f"anchor_active_fifth={str(row['anchor_active_in_fifth']).lower()}",
                    f"survivors={row['surviving_roots']}",
                    f"terminalized={row['terminalized_roots']}",
                    f"dropped={row['dropped_roots']}",
                    f"gain={row['local_interval_gain']['decimal']}",
                    f"survivor_rows_sha256={row['survivor_rows_sha256']}",
                ]
            )
        )
    lines.extend(["", "[top_survivor_intervals]"])
    for row in payload["top_survivor_intervals"][:15]:
        lines.append(
            ";".join(
                [
                    f"root={row['root']}",
                    f"reference={row['reference_root']}",
                    f"anchor={row['anchor_root']}",
                    f"parent={row['parent_current']}",
                    f"child={row['child_current']}",
                    f"translation={row['translation']}",
                    f"gain={row['interval_gain']['decimal']}",
                    f"parent_class={row['parent_state_class']}",
                    f"child_class={row['child_state_class']}",
                ]
            )
        )
    text = "\n".join(lines) + "\n"
    if output_path is None:
        print(text, end="")
    else:
        output_path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
