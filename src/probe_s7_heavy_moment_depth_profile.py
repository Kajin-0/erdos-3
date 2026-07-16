#!/usr/bin/env python3
"""Profile exact p0 moment-depth interpolation on S7 direct heavy shells."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

from probe_s7_direct_pair_discharge import (
    completion_candidates,
    harmonic,
)
from probe_s7_hole_support_closure import (
    build_s7,
    canonical_pair,
    read_full_hole_map,
)
from probe_sponsor_pair_transport_frontier import pair_weight, serialize_mass
from verify_retained_terminal_split import contains_three_term_ap

Pair = tuple[int, int]


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_heavy_moment_depth_profile.py "
            "TERMINAL_PAYMENT_JSON FULL_S7_HOLE_MAP_TSV OUTPUT_JSON"
        )

    payment = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    source_rows = payment.get("source_rows")
    if not isinstance(source_rows, list):
        raise AssertionError("terminal-payment payload lacks source rows")

    s7 = build_s7()
    holes = read_full_hole_map(Path(sys.argv[2]))
    parent_base = 1_048_576
    parent_level = parent_base.bit_length() - 1
    q = Fraction(2, 5)  # 2^{-p0}, p0=log_2(5/2)

    activated: set[Pair] = {
        tuple(int(value) for value in row["pair"])
        for row in source_rows
    }
    selected_holes: list[tuple[Pair, int, str, int, Fraction, Pair]] = []
    for pair in sorted(activated):
        candidates = completion_candidates(pair)
        if any(row[0] in s7 for row in candidates):
            continue
        certified = [row for row in candidates if row[0] in holes]
        if not certified:
            continue
        completion, role, step, coefficient = min(certified)
        selected_holes.append(
            (
                pair,
                completion,
                role,
                step,
                coefficient,
                canonical_pair(*holes[completion]),
            )
        )

    groups: dict[tuple[Pair, int, str, Fraction], set[int]] = defaultdict(set)
    roles_by_support: dict[Pair, set[tuple[int, str, Fraction]]] = defaultdict(set)
    for _pair, completion, role, step, coefficient, support in selected_holes:
        groups[(support, completion, role, coefficient)].add(step)
        roles_by_support[support].add((completion, role, coefficient))

    reserve = set(activated)
    heavy_roles: list[tuple[Fraction, tuple[int, ...]]] = []
    for support, roles in sorted(roles_by_support.items()):
        multiplicity = len(roles)
        threshold = (
            Fraction()
            if support in reserve
            else pair_weight(support) / multiplicity
        )
        for completion, role, coefficient in sorted(roles):
            steps = groups[(support, completion, role, coefficient)]
            load = coefficient * harmonic(steps)
            if load > threshold:
                heavy_roles.append((coefficient, tuple(sorted(steps))))

    by_shell: dict[tuple[str, int], Fraction] = defaultdict(Fraction)
    for coefficient, steps in heavy_roles:
        shells: dict[int, set[int]] = defaultdict(set)
        for step in steps:
            shell_base = 1 << (int(step).bit_length() - 1)
            shells[shell_base].add(int(step))
        for shell_base, shell_steps in shells.items():
            kind = (
                "recursive"
                if contains_three_term_ap(tuple(sorted(shell_steps)))
                else "terminal"
            )
            by_shell[(kind, shell_base)] += coefficient * harmonic(shell_steps)

    rows: list[dict[str, object]] = []
    totals: dict[str, Fraction] = defaultdict(Fraction)
    for (kind, shell_base), raw_mass in sorted(by_shell.items()):
        shell_level = shell_base.bit_length() - 1
        drop = parent_level - shell_level
        if drop < 1:
            raise AssertionError("heavy child did not descend one owner level")
        normalized_moment = raw_mass * q**drop
        excess_depth = raw_mass * (drop - 1)
        reconstructed = (
            Fraction(5, 2) * normalized_moment
            + Fraction(3, 5) * excess_depth
        )
        if reconstructed < raw_mass:
            raise AssertionError("moment-depth interpolation failed on heavy shell")
        slack = reconstructed - raw_mass
        rows.append(
            {
                "kind": kind,
                "shell_base": shell_base,
                "owner_drop": drop,
                "raw_mass": serialize_mass(raw_mass),
                "normalized_p0_moment": serialize_mass(normalized_moment),
                "excess_depth_mass": serialize_mass(excess_depth),
                "reconstructed_raw_bound": serialize_mass(reconstructed),
                "interpolation_slack": serialize_mass(slack),
            }
        )
        totals[f"{kind}_raw_mass"] += raw_mass
        totals[f"{kind}_normalized_p0_moment"] += normalized_moment
        totals[f"{kind}_excess_depth_mass"] += excess_depth
        totals[f"{kind}_reconstructed_raw_bound"] += reconstructed
        totals["raw_mass"] += raw_mass
        totals["normalized_p0_moment"] += normalized_moment
        totals["excess_depth_mass"] += excess_depth
        totals["reconstructed_raw_bound"] += reconstructed

    if totals["raw_mass"] != (
        totals["terminal_raw_mass"] + totals["recursive_raw_mass"]
    ):
        raise AssertionError("heavy terminal/recursive mass partition failed")
    if totals["reconstructed_raw_bound"] < totals["raw_mass"]:
        raise AssertionError("aggregate heavy interpolation failed")

    output = {
        "schema": "s7_heavy_moment_depth_profile_v1",
        "scope": "certified S7 direct heavy shell outputs only",
        "parent_base": parent_base,
        "boundary_exponent": "log_2(5/2)",
        "q_two_to_minus_p0": str(q),
        "counts": {
            "heavy_role_fibers": len(heavy_roles),
            "aggregated_shell_rows": len(rows),
            "terminal_shell_bases": sum(row["kind"] == "terminal" for row in rows),
            "recursive_shell_bases": sum(row["kind"] == "recursive" for row in rows),
        },
        "totals": {
            name: serialize_mass(value) for name, value in sorted(totals.items())
        },
        "rows": rows,
        "checks": {
            "every_heavy_shell_descends": True,
            "terminal_recursive_partition_exact": True,
            "rowwise_moment_depth_interpolation": True,
            "aggregate_moment_depth_interpolation": True,
            "light_and_direct_pair_outputs_excluded": True,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    Path(sys.argv[3]).write_text(
        json.dumps(output, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
