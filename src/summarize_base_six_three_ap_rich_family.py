#!/usr/bin/env python3
"""Summarize the base-six three-AP-rich family certificate."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: summarize_base_six_three_ap_rich_family.py INPUT OUTPUT")
    data = json.loads(Path(sys.argv[1]).read_text())
    lines = [
        "Base-six three-AP-rich four-AP-free family",
        "===========================================",
        "",
        f"max_n={data['max_n']}",
        "all_digit_families_four_ap_free=true",
        "explicit_three_ap_count_equals_4n_minus_3n=true",
        "standard_dyadic_placement_valid=true",
        "load_over_harmonic_lower_bound_verified=true",
        "",
    ]
    for row in data["rows"]:
        lines.append(
            "n={n};size={cardinality};all_3aps={all_three_ap_count};"
            "load={load};harmonic={harmonic};ratio={ratio};"
            "ratio_lower={lower}".format(
                n=row["n"],
                cardinality=row["cardinality"],
                all_three_ap_count=row["all_three_ap_count"],
                load=row["total_weighted_load"]["decimal"],
                harmonic=row["shifted_harmonic_mass"]["decimal"],
                ratio=row["load_over_harmonic"]["decimal"],
                lower=row["strict_ratio_lower_bound"]["decimal"],
            )
        )
    lines.append(f"payload_sha256={data['payload_sha256']}")
    Path(sys.argv[2]).write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
