#!/usr/bin/env python3
"""Summarize the targeted recursive-child pair-overlap search."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: summarize_recursive_child_pair_overlap.py INPUT OUTPUT")
    data = json.loads(Path(sys.argv[1]).read_text())
    target = Path(sys.argv[2])
    lines = [
        "Recursive oriented-child pair-overlap search",
        "============================================",
        "",
        f"max_value={data['max_value']}",
        f"descriptor_count={data['descriptor_count']}",
        f"shared_pair_descriptor_pairs_tested={data['shared_pair_descriptor_pairs_tested']}",
        f"viable_four_ap_free_overlap_unions={data['viable_four_ap_free_overlap_unions']}",
    ]
    for kind, count in sorted(data["descriptor_kind_counts"].items()):
        lines.append(f"descriptor_kind_{kind}={count}")
    counterexample = data.get("minimum_counterexample")
    if counterexample is None:
        lines.append("minimum_counterexample=none")
    else:
        lines.extend(
            [
                "minimum_counterexample_pair="
                + ",".join(map(str, counterexample["pair"])),
                "minimum_counterexample_support="
                + ",".join(map(str, counterexample["support"])),
                f"minimum_counterexample_support_size={counterexample['support_size']}",
                f"minimum_counterexample_support_span={counterexample['support_span']}",
                "minimum_counterexample_first_key="
                + ",".join(map(str, counterexample["first"]["child_key"])),
                "minimum_counterexample_second_key="
                + ",".join(map(str, counterexample["second"]["child_key"])),
                "minimum_counterexample_first_roots="
                + ",".join(map(str, counterexample["first_actual_roots"])),
                "minimum_counterexample_second_roots="
                + ",".join(map(str, counterexample["second_actual_roots"])),
            ]
        )
    lines.extend(
        [
            f"descriptors_sha256={data['descriptors_sha256']}",
            f"counterexample_family_sha256={data['counterexample_family_sha256']}",
        ]
    )
    target.write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
