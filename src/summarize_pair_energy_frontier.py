#!/usr/bin/env python3
"""Emit compact exact pair-energy frontier diagnostics."""
from __future__ import annotations

from pathlib import Path
import json
import sys


def main() -> int:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/pair_energy_frontier_probe.json"
    )
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    lines = [
        "pair_energy_frontier_summary_v1",
        f"probe_payload_sha256={payload['probe_payload_sha256']}",
        f"profiles_sha256={payload['hashes']['profiles']}",
        f"bellman_rows_sha256={payload['hashes']['bellman_rows']}",
        f"generation_six_propagated={str(payload['generation_six_propagated']).lower()}",
        "",
        "[profiles]",
    ]
    for profile in payload["profiles"]:
        lines.append(
            ";".join(
                [
                    f"name={profile['name']}",
                    f"states={profile['states']}",
                    f"points={profile['points']}",
                    f"H={profile['harmonic_mass']['decimal']}",
                    f"distinct_roots={profile['distinct_roots']}",
                    f"max_root_multiplicity={profile['maximum_root_multiplicity']}",
                    f"pair_occurrences={profile['pair_occurrences']}",
                    f"distinct_pairs={profile['distinct_pairs']}",
                    f"max_pair_multiplicity={profile['maximum_pair_multiplicity']}",
                    f"J_occurrence={profile['pair_energy_occurrence']['decimal']}",
                    f"J_union={profile['pair_energy_union']['decimal']}",
                    f"repeated_pair_energy={profile['repeated_pair_energy']['decimal']}",
                    f"affine_states={profile['affine_states']}",
                    f"nonaffine_states={profile['nonaffine_states']}",
                    f"root_multiplicity_sha256={profile['root_multiplicity_sha256']}",
                    f"pair_multiplicity_sha256={profile['pair_multiplicity_sha256']}",
                ]
            )
        )
    output = payload["fifth_output"]
    lines.extend(
        [
            "",
            "[fifth_output]",
            ";".join(
                [
                    f"total_states={output['total_states']}",
                    f"total_points={output['total_points']}",
                    f"terminal_states={output['terminal_states']}",
                    f"terminal_points={output['terminal_points']}",
                    f"recursive_states={output['recursive_states']}",
                    f"recursive_points={output['recursive_points']}",
                    f"H_total={output['total_harmonic_mass']['decimal']}",
                    f"H_terminal={output['terminal_harmonic_mass']['decimal']}",
                    f"H_recursive={output['recursive_harmonic_mass']['decimal']}",
                ]
            ),
            "",
            "[bellman_rows]",
        ]
    )
    for name, row in payload["bellman_rows"].items():
        lines.append(
            ";".join(
                [
                    f"name={name}",
                    f"left={row['left_H5_plus_J5']['decimal']}",
                    f"right={row['right_J4']['decimal']}",
                    f"surplus={row['surplus']['decimal']}",
                    f"ratio={row['ratio']['decimal']}",
                    f"verified={str(row['verified']).lower()}",
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
