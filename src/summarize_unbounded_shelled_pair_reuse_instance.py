#!/usr/bin/env python3
"""Summarize the multiplicity-four shelled pair-reuse certificate."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: summarize_unbounded_shelled_pair_reuse_instance.py INPUT OUTPUT")
    data = json.loads(Path(sys.argv[1]).read_text())
    lines = [
        "Multiplicity-four shell-valid latent-pair reuse",
        "================================================",
        "",
        f"m={data['m']}",
        "reference_set=" + ",".join(map(str, data["reference_set"])),
        f"d={data['d']}",
        f"K={data['K']}",
        f"translation={data['translation']}",
        "parent_block=" + ",".join(map(str, data["parent_block"])),
        f"parent_support_size={data['parent_support_size']}",
        "parent_four_ap_free=true",
        "child_shell=" + ",".join(map(str, data["child_shell"])),
        f"recursive_children={len(data['recursive_child_keys'])}",
        "common_root_triple=" + ",".join(map(str, data["common_root_triple"])),
        f"maximum_certified_latent_pair_multiplicity={data['maximum_certified_latent_pair_multiplicity']}",
    ]
    for row in data["common_pair_multiplicities"]:
        lines.append(
            "common_pair="
            + ",".join(map(str, row["pair"]))
            + f";weight={row['weight']};multiplicity={row['multiplicity']}"
        )
    lines.append(f"payload_sha256={data['payload_sha256']}")
    Path(sys.argv[2]).write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
