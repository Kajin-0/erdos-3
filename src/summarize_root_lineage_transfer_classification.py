#!/usr/bin/env python3
"""Emit a compact human-readable summary of the root-lineage probe JSON."""
from __future__ import annotations

from pathlib import Path
import json
import sys


def group_line(record: dict[str, object], keys: tuple[str, ...], mass_key: str) -> str:
    labels = ",".join(f"{key}={record.get(key)}" for key in keys)
    mass = record[mass_key]
    return f"{labels};count={record['count']};{mass_key}={mass['decimal']};sha256={mass['sha256']}"


def main() -> int:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/root_lineage_transfer_classification_probe.json"
    )
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    payload = json.loads(input_path.read_text(encoding="utf-8"))

    counts = payload["counts"]
    masses = payload["masses"]
    lines = [
        "root_lineage_transfer_classification_summary_v1",
        f"probe_payload_sha256={payload['probe_payload_sha256']}",
        f"survivor_rows_sha256={payload['hashes']['survivor_rows']}",
        f"exit_rows_sha256={payload['hashes']['exit_rows']}",
        f"survivor_groups_sha256={payload['hashes']['survivor_groups']}",
        f"exit_groups_sha256={payload['hashes']['exit_groups']}",
        f"fourth_recursive_roots={counts['fourth_recursive_roots']}",
        f"surviving_roots={counts['surviving_roots']}",
        f"terminalized_roots={counts['terminalized_roots']}",
        f"dropped_roots={counts['dropped_roots']}",
        f"split_roots={counts['split_roots']}",
        f"survivor_immediate_provenance_matches={counts['survivor_immediate_provenance_matches']}",
        f"recursive_fourth={masses['recursive_fourth']['decimal']}",
        f"recursive_fifth={masses['recursive_fifth']['decimal']}",
        f"survivor_scale_gain={masses['survivor_scale_gain']['decimal']}",
        f"exiting_parent_release={masses['exiting_parent_release']['decimal']}",
        f"recursive_delta={masses['recursive_delta']['decimal']}",
        f"identity_verified={str(payload['identity']['verified']).lower()}",
        "",
        "[survivor_gain_concentration]",
    ]
    for key, record in payload["survivor_gain_concentration"].items():
        lines.append(
            f"{key};count={record['count']};gain={record['gain_decimal']};share={record['share_decimal']}"
        )

    lines.extend(["", "[survivor_by_child_source]"])
    for record in payload["survivor_groups"]["child_source"]:
        lines.append(group_line(record, ("child_source",), "gain"))

    lines.extend(["", "[survivor_by_shell_drop]"])
    for record in payload["survivor_groups"]["shell_drop"]:
        lines.append(group_line(record, ("shell_drop",), "gain"))

    lines.extend(["", "[survivor_by_source_and_shell_drop]"])
    for record in payload["survivor_groups"]["child_source_shell_drop"]:
        lines.append(
            group_line(record, ("child_source", "shell_drop"), "gain")
        )

    lines.extend(["", "[survivor_by_valuation_class]"])
    for record in payload["survivor_groups"]["valuation_class"]:
        lines.append(
            group_line(
                record,
                ("child_source", "side_parity", "middle_color", "shell_drop"),
                "gain",
            )
        )

    lines.extend(["", "[top_survivor_source_steps]"])
    for record in payload["survivor_groups"]["child_source_step"][:25]:
        lines.append(
            group_line(record, ("child_source", "child_source_step"), "gain")
        )

    lines.extend(["", "[top_survivor_parent_classes]"])
    for record in payload["survivor_groups"]["parent_state_class"][:20]:
        lines.append(group_line(record, ("parent_state_class",), "gain"))

    lines.extend(["", "[exit_fates]"])
    for record in payload["exit_groups"]["fate"]:
        lines.append(group_line(record, ("fate",), "parent_release"))

    lines.extend(["", "[top_exit_parent_classes]"])
    for record in payload["exit_groups"]["parent_state_class"][:20]:
        lines.append(
            group_line(record, ("parent_state_class",), "parent_release")
        )

    lines.extend(["", "[top_individual_survivor_gains]"])
    for row in payload["top_individual_survivor_gains"][:15]:
        lines.append(
            ";".join(
                [
                    f"root={row['root']}",
                    f"parent={row['parent_current']}",
                    f"child={row['child_current']}",
                    f"gain={row['gain']}",
                    f"source={row['child_source']}",
                    f"step={row['child_source_step']}",
                    f"shell_drop={row['shell_drop']}",
                    f"side_parity={row['side_parity']}",
                    f"middle_color={row['middle_color']}",
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
