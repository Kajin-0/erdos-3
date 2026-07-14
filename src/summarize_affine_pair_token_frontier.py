#!/usr/bin/env python3
"""Emit compact affine coverage and pair-token reuse summaries."""
from __future__ import annotations

from pathlib import Path
import json
import sys


def main() -> int:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "data/affine_pair_token_frontier_probe.json"
    )
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    cumulative = payload["cumulative"]
    lines = [
        "affine_pair_token_frontier_summary_v1",
        f"probe_payload_sha256={payload['probe_payload_sha256']}",
        f"family_summaries_sha256={payload['hashes']['family_summaries']}",
        f"affine_state_rows_sha256={payload['hashes']['affine_state_rows']}",
        f"generation_six_propagated={str(payload['generation_six_propagated']).lower()}",
        f"first_root_universe_roots={payload['first_root_universe']['roots']}",
        f"first_root_universe_sha256={payload['first_root_universe']['sha256']}",
        "",
        "[families]",
    ]
    for record in payload["families"]:
        lines.append(
            ";".join(
                [
                    f"name={record['name']}",
                    f"states={record['states']}",
                    f"points={record['points']}",
                    f"terminal_states={record['terminal_states']}",
                    f"recursive_states={record['recursive_states']}",
                    f"affine_states={record['affine_states']}",
                    f"nonaffine_states={record['nonaffine_states']}",
                    f"affine_terminal_states={record['affine_terminal_states']}",
                    f"affine_recursive_states={record['affine_recursive_states']}",
                    f"affine_refs_in_F1_roots={record['affine_references_in_first_root_universe']}",
                    f"affine_refs_active_in_state={record['affine_references_active_in_state']}",
                    f"token_occurrences={record['token_occurrences']}",
                    f"distinct_tokens={record['distinct_tokens']}",
                    f"duplicate_token_classes={record['duplicate_token_classes']}",
                    f"max_token_multiplicity={record['maximum_token_multiplicity']}",
                    f"multi_immediate_tokens={record['tokens_with_multiple_immediate_provenance']}",
                    f"terminal_recursive_overlap={record['terminal_recursive_token_overlap']}",
                    f"first_tokens={record['first_appearance_tokens']}",
                    f"reused_prior_tokens={record['reused_prior_tokens']}",
                    f"H_occurrence={record['occurrence_mass']['decimal']}",
                    f"H_union={record['union_token_mass']['decimal']}",
                    f"H_duplicate_current={record['duplicate_occurrence_mass']['decimal']}",
                    f"H_first={record['first_appearance_mass']['decimal']}",
                    f"H_reused_prior={record['reused_prior_mass']['decimal']}",
                    f"state_rows_sha256={record['hashes']['state_rows']}",
                    f"token_counts_sha256={record['hashes']['token_counts']}",
                    f"first_tokens_sha256={record['hashes']['first_tokens']}",
                    f"reused_tokens_sha256={record['hashes']['reused_tokens']}",
                ]
            )
        )
    lines.extend(
        [
            "",
            "[cumulative]",
            f"occurrence_mass={cumulative['occurrence_mass']['decimal']}",
            f"first_appearance_mass={cumulative['first_appearance_mass']['decimal']}",
            f"pair_reuse_mass={cumulative['pair_reuse_mass']['decimal']}",
            f"distinct_tokens={cumulative['distinct_tokens']}",
            f"tokens_sha256={cumulative['tokens_sha256']}",
            "",
            "[nonaffine_states]",
        ]
    )
    for record in payload["families"]:
        for row in record["state_rows"]:
            if not row["affine"]:
                lines.append(
                    ";".join(
                        [
                            f"family={record['name']}",
                            f"class={row['state_class']}",
                            f"terminal={str(row['terminal']).lower()}",
                            f"source={row['source']}",
                            f"step={row['source_step']}",
                            f"size={row['size']}",
                            f"distinct_roots={row['distinct_roots']}",
                            f"tokens_sha256={row['tokens_sha256']}",
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
