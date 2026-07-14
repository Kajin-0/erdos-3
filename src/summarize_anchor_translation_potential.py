#!/usr/bin/env python3
"""Emit a compact summary of the minimum-anchor translation-potential probe."""
from __future__ import annotations

from pathlib import Path
import json
import sys


def display(record: dict[str, str] | None) -> str:
    return "none" if record is None else record["decimal"]


def main() -> int:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/anchor_translation_potential_probe.json"
    )
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    interval = payload["coefficient_interval"]
    lines = [
        "anchor_translation_potential_summary_v1",
        f"probe_payload_sha256={payload['probe_payload_sha256']}",
        f"generation_records_sha256={payload['hashes']['generation_records']}",
        f"constraints_sha256={payload['hashes']['constraints']}",
        f"natural_kappa_one_sha256={payload['hashes']['natural_kappa_one']}",
        f"definition={payload['definition']}",
        f"generation_six_propagated={str(payload['generation_six_propagated']).lower()}",
        f"coefficient_interval_feasible={str(interval['feasible']).lower()}",
        f"coefficient_lower={display(interval['lower'])}",
        f"coefficient_upper={display(interval['upper'])}",
        f"coefficient_witness={display(interval['witness'])}",
        f"natural_kappa_one_contracts_all={str(payload['natural_kappa_one']['contracts_all_transitions']).lower()}",
        "",
        "[generations]",
    ]
    for generation in payload["generations"]:
        lines.append(
            ";".join(
                [
                    f"name={generation['name']}",
                    f"states={generation['states']}",
                    f"points={generation['points']}",
                    f"H={generation['harmonic_mass']['decimal']}",
                    f"A={generation['translation_reserve']['decimal']}",
                    f"anchor_release={generation['anchor_release']['decimal']}",
                    f"H_plus_A={generation['h_plus_a']['decimal']}",
                    f"A_over_H={generation['reserve_over_harmonic']['decimal']}",
                    f"A_over_anchor={generation['reserve_over_anchor_release']['decimal']}",
                    f"state_rows_sha256={generation['state_rows_sha256']}",
                ]
            )
        )
    lines.extend(["", "[coefficient_constraints]"])
    for constraint in payload["constraints"]:
        lines.append(
            ";".join(
                [
                    f"transition={constraint['transition']}",
                    f"delta_H={constraint['delta_h']['decimal']}",
                    f"delta_A={constraint['delta_a']['decimal']}",
                    f"relation={constraint['relation']}",
                    f"bound={display(constraint['bound'])}",
                ]
            )
        )
    lines.extend(["", "[kappa_one_transitions]"])
    for transition in payload["natural_kappa_one"]["transitions"]:
        lines.append(
            ";".join(
                [
                    f"transition={transition['transition']}",
                    f"current={transition['current']['decimal']}",
                    f"next={transition['next']['decimal']}",
                    f"delta={transition['delta']['decimal']}",
                    f"ratio={transition['ratio']['decimal']}",
                    f"contracts={str(transition['contracts']).lower()}",
                ]
            )
        )
    if payload["witness_transitions"] is not None:
        lines.extend(["", "[witness_transitions]"])
        for transition in payload["witness_transitions"]:
            lines.append(
                ";".join(
                    [
                        f"transition={transition['transition']}",
                        f"current={transition['current']['decimal']}",
                        f"next={transition['next']['decimal']}",
                        f"delta={transition['delta']['decimal']}",
                        f"ratio={transition['ratio']['decimal']}",
                        f"contracts={str(transition['contracts']).lower()}",
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
