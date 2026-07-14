#!/usr/bin/env python3
"""Summarize the exhaustive full-color coordinated branching verifier."""
from __future__ import annotations

import json
from pathlib import Path
import sys


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "usage: summarize_full_color_coordinated_branching.py INPUT OUTPUT",
            file=sys.stderr,
        )
        return 2
    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if payload.get("schema") != "full_color_coordinated_branching_exhaustive_v1":
        raise AssertionError("unexpected full-color branching schema")
    lines = [
        "Full-color coordinated branching exhaustive check",
        "================================================",
        "",
        f"interval={payload['interval'][0]},{payload['interval'][1]}",
        f"four_ap_free_subsets_tested={payload['four_ap_free_subsets_tested']}",
        f"subsets_with_three_aps={payload['subsets_with_three_aps']}",
        f"total_three_ap_occurrences={payload['total_three_ap_occurrences']}",
        f"total_child_states={payload['total_child_states']}",
        f"total_child_memberships={payload['total_child_memberships']}",
        f"maximum_three_aps_in_one_subset={payload['maximum_three_aps_in_one_subset']}",
        f"maximum_children_in_one_subset={payload['maximum_children_in_one_subset']}",
        f"exact_two_memberships_per_progression={str(payload['exact_two_memberships_per_progression']).lower()}",
        f"all_children_four_ap_free={str(payload['all_children_four_ap_free']).lower()}",
        (
            "all_children_have_disjoint_first_three_dilates="
            f"{str(payload['all_children_have_disjoint_first_three_dilates']).lower()}"
        ),
        f"exact_harmonic_identity={payload['exact_harmonic_identity']}",
        f"records_sha256={payload['records_sha256']}",
        f"payload_sha256={payload['payload_sha256']}",
    ]
    Path(sys.argv[2]).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
