#!/usr/bin/env python3
"""Summarize the exhaustive full-edge coordinated branching verifier."""
from __future__ import annotations

import json
from pathlib import Path
import sys


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "usage: summarize_full_edge_coordinated_branching.py INPUT OUTPUT",
            file=sys.stderr,
        )
        return 2
    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if payload.get("schema") != "full_edge_coordinated_branching_exhaustive_v1":
        raise AssertionError("unexpected full-edge branching schema")

    metrics = payload["metrics"]
    dyadic = payload["dyadic_metrics"]
    verified = payload["verified"]
    lines = [
        "Full-edge coordinated branching exhaustive check",
        "================================================",
        "",
        f"interval={payload['interval'][0]},{payload['interval'][1]}",
        f"dyadic_bases={','.join(map(str, payload['dyadic_bases']))}",
        f"four_ap_free_subsets={metrics['four_ap_free_subsets']}",
        f"subsets_with_three_aps={metrics['subsets_with_three_aps']}",
        f"three_ap_occurrences={metrics['three_ap_occurrences']}",
        f"child_occurrences={metrics['child_occurrences']}",
        f"child_states={metrics['child_states']}",
        f"repeated_physical_pairs={metrics['repeated_physical_pairs']}",
        f"maximum_three_aps={metrics['maximum_three_aps']}",
        f"maximum_child_states={metrics['maximum_child_states']}",
        f"maximum_pair_multiplicity={metrics['maximum_pair_multiplicity']}",
        "",
        f"dyadic_four_ap_free_subsets={dyadic['dyadic_four_ap_free_subsets']}",
        f"dyadic_three_ap_occurrences={dyadic['dyadic_three_ap_occurrences']}",
        f"dyadic_child_occurrences={dyadic['dyadic_child_occurrences']}",
        f"dyadic_child_states={dyadic['dyadic_child_states']}",
        "",
    ]
    for key in sorted(verified):
        lines.append(f"{key}={str(verified[key]).lower()}")
    lines.extend(
        [
            "",
            f"records_sha256={payload['records_sha256']}",
            f"payload_sha256={payload['payload_sha256']}",
        ]
    )
    Path(sys.argv[2]).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
