#!/usr/bin/env python3
"""Certify the fourth-to-fifth local policy-sensitivity frontier exactly."""
from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import hashlib
import json
import sys

import probe_fourth_to_fifth_retention_tie_range as probe

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED = {
    "probe_payload_sha256": "989d31521e1e17fadc2fcf8c249d591430dfc48a375ee9e53ec5c0de5fadae02",
    "policy_count": 14,
    "best_policy": "reverse_parent_82",
    "best_min_recursive_ratio_sha256": "40a1270568301a9d31f9e54dc401575eb9de6c8057ffc8fb50e83f778fea727b",
    "best_min_recursive_ratio_decimal": "1.197375982982",
    "parent_mass_sha256": "03cac9573c3d61ac9c8a0c4066cbb8d6ea9ece01606602cacc9604634f9b1ba9",
    "baseline_ratio_sha256": "8d55faef41edb883a3d2d229690ef16db69bd1be23f85871c21c3206319e0534",
}


def load_probe() -> dict[str, object]:
    buffer = StringIO()
    with redirect_stdout(buffer):
        status = probe.main()
    if status != 0:
        raise AssertionError(f"policy-sensitivity probe failed: {status}")
    return json.loads(buffer.getvalue())


def build_certificate() -> str:
    payload = load_probe()
    for key in (
        "probe_payload_sha256",
        "policy_count",
        "best_policy",
        "best_min_recursive_ratio_sha256",
        "best_min_recursive_ratio_decimal",
        "parent_mass_sha256",
    ):
        if payload[key] != EXPECTED[key]:
            raise AssertionError(f"{key} changed: {payload[key]!r}")
    if not payload["all_tested_max_harmonic_optima_expand"]:
        raise AssertionError("a tested maximum-harmonic optimum contracts")

    records = payload["records"]
    by_name = {row["policy"]: row for row in records}
    baseline = by_name["all_lexicographic"]
    if baseline["min_recursive_ratio_sha256"] != EXPECTED["baseline_ratio_sha256"]:
        raise AssertionError("baseline ratio changed")
    if baseline["global_optimizer_count"] != 1:
        raise AssertionError("baseline optimum is no longer unique")

    nonunique = [row for row in records if row["global_optimizer_count"] != 1]
    if {row["policy"] for row in nonunique} != {
        "all_reverse",
        "reverse_parent_82",
    }:
        raise AssertionError("nonunique-policy set changed")
    for row in nonunique:
        if row["global_optimizer_count"] != 2:
            raise AssertionError("unexpected optimizer count")
        if row["min_recursive_mass_sha256"] != row["max_recursive_mass_sha256"]:
            raise AssertionError("tied optimum changes recursive mass")
        if any(
            component["recursive_mass_varies"]
            for component in row["nonunique_component_rows"]
        ):
            raise AssertionError("nonunique component changes recursive mass")

    lines = [
        "fourth_to_fifth_policy_sensitivity_certificate_v1",
        "scope=all_lexicographic,all_reverse,and_twelve_single_parent_reverse_flips",
        "retention=max_total_harmonic_same_shell_independent_sets_with_all_ties",
        f"policy_count={payload['policy_count']}",
        "all_tested_max_harmonic_optima_expand=true",
        f"parent_mass_sha256={payload['parent_mass_sha256']}",
        f"best_policy={payload['best_policy']}",
        "best_ratio_lower=9579/8000",
        "best_ratio_upper=18709/15625",
        f"best_ratio_decimal={payload['best_min_recursive_ratio_decimal']}",
        f"best_ratio_sha256={payload['best_min_recursive_ratio_sha256']}",
        "baseline_ratio_lower=1329813/1000000",
        "baseline_ratio_upper=664907/500000",
        f"baseline_ratio_sha256={baseline['min_recursive_ratio_sha256']}",
        "nonunique_policies=all_reverse,reverse_parent_82",
        "nonunique_optimizer_count_each=2",
        "tied_optima_have_identical_recursive_mass=true",
        f"probe_payload_sha256={payload['probe_payload_sha256']}",
        "policy_rows:",
    ]
    for row in records:
        lines.append(
            "|".join(
                (
                    row["policy"],
                    f"optimizers={row['global_optimizer_count']}",
                    f"min_ratio={row['min_recursive_ratio_decimal']}",
                    f"min_ratio_sha256={row['min_recursive_ratio_sha256']}",
                    f"all_expand={str(row['every_max_harmonic_optimum_expands']).lower()}",
                )
            )
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    certificate = build_certificate()
    if output is None:
        print(certificate, end="")
    else:
        output.write_text(certificate, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
