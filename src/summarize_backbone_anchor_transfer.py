#!/usr/bin/env python3
"""Emit a compact summary of the twelve-state backbone-anchor probe."""
from __future__ import annotations

from pathlib import Path
import json
import sys


def decimal(record: dict[str, str] | None) -> str:
    return "none" if record is None else record["decimal"]


def main() -> int:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/backbone_anchor_transfer_probe.json"
    )
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    counts = payload["counts"]
    masses = payload["masses"]
    ratios = payload["ratios"]
    lines = [
        "backbone_anchor_transfer_summary_v1",
        f"probe_payload_sha256={payload['probe_payload_sha256']}",
        f"parent_state_rows_sha256={payload['hashes']['parent_state_rows']}",
        f"anchor_roots_sha256={payload['hashes']['anchor_roots']}",
        f"parent_states={counts['parent_states']}",
        f"minimum_anchor_roots={counts['minimum_anchor_roots']}",
        f"minimum_anchors_dropped_no_raw_output={counts['minimum_anchors_dropped_no_raw_output']}",
        f"expanding_parent_states={counts['expanding_parent_states']}",
        f"contracting_parent_states={counts['contracting_parent_states']}",
        f"neutral_parent_states={counts['neutral_parent_states']}",
        f"expanding_parent_classes={','.join(str(value) for value in payload['expanding_parent_classes'])}",
        f"contracting_parent_classes={','.join(str(value) for value in payload['contracting_parent_classes'])}",
        f"neutral_parent_classes={','.join(str(value) for value in payload['neutral_parent_classes'])}",
        f"parent_recursive_mass={masses['parent_recursive_mass']['decimal']}",
        f"full_translation_gain={masses['full_translation_gain']['decimal']}",
        f"minimum_anchor_release={masses['minimum_anchor_release']['decimal']}",
        f"retained_survivor_gain={masses['retained_survivor_gain']['decimal']}",
        f"exit_release={masses['exit_release']['decimal']}",
        f"recursive_net={masses['recursive_net']['decimal']}",
        f"full_translation_gain_over_anchor_release={decimal(ratios['full_translation_gain_over_anchor_release'])}",
        f"retained_gain_over_anchor_release={decimal(ratios['retained_gain_over_anchor_release'])}",
        f"retained_gain_fraction_of_full_translation={decimal(ratios['retained_gain_fraction_of_full_translation'])}",
        f"top_three_parent_gain_share={decimal(ratios['top_three_parent_gain_share'])}",
        "",
        "[parent_state_rows]",
    ]
    rows = sorted(
        payload["rows"],
        key=lambda row: (-float(row["local_recursive_net"]["decimal"]), row["parent_state_class"]),
    )
    for row in rows:
        lines.append(
            ";".join(
                [
                    f"class={row['parent_state_class']}",
                    f"size={row['parent_size']}",
                    f"minimum={row['minimum']}",
                    f"anchor_root={row['anchor_root']}",
                    f"anchor_fate={row['anchor_fate']}",
                    f"smallest_gaps={','.join(str(value) for value in row['smallest_gaps'])}",
                    f"full_gain={row['full_translation_gain']['decimal']}",
                    f"full_gain_per_anchor={decimal(row['full_gain_over_anchor_release'])}",
                    f"survivors={row['surviving_roots']}",
                    f"terminalized={row['terminalized_roots']}",
                    f"dropped={row['dropped_roots']}",
                    f"retained_gain={row['survivor_gain']['decimal']}",
                    f"retained_gain_per_anchor={decimal(row['survivor_gain_over_anchor_release'])}",
                    f"retained_fraction_full_gain={decimal(row['retained_gain_fraction_of_full_translation'])}",
                    f"exit_release={row['exit_release']['decimal']}",
                    f"local_net={row['local_recursive_net']['decimal']}",
                    f"recursive_ratio={decimal(row['recursive_child_over_parent'])}",
                    f"shell_drops={json.dumps(row['shell_drop_counts'], sort_keys=True, separators=(',', ':'))}",
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
