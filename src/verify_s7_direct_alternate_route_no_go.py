#!/usr/bin/env python3
"""Require the corrected S7 alternate-route flow to fail by an exact min cut."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json
import subprocess
import sys


def fraction(record: object) -> Fraction:
    if not isinstance(record, dict) or not isinstance(record.get("fraction"), str):
        raise AssertionError("serialized mass record lacks an exact fraction")
    return Fraction(record["fraction"])


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: verify_s7_direct_alternate_route_no_go.py "
            "TERMINAL_PAYMENT_JSON FULL_S7_HOLE_MAP_TSV OUTPUT_JSON"
        )

    script = Path(__file__).with_name("probe_s7_direct_alternate_route_flow.py")
    output_path = Path(sys.argv[3])
    process = subprocess.run(
        [sys.executable, str(script), sys.argv[1], sys.argv[2], sys.argv[3]],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if process.returncode != 2:
        raise AssertionError(
            "alternate-route probe did not return the expected infeasible status: "
            f"returncode={process.returncode}\nstdout={process.stdout}\nstderr={process.stderr}"
        )
    if not output_path.exists():
        raise AssertionError("alternate-route probe did not emit its certificate")

    payload = json.loads(output_path.read_text(encoding="utf-8"))
    checks = payload.get("checks")
    masses = payload.get("masses")
    counts = payload.get("counts")
    if not isinstance(checks, dict) or not isinstance(masses, dict) or not isinstance(counts, dict):
        raise AssertionError("alternate-route payload has an invalid schema")

    demand = fraction(masses["total_recursive_demand"])
    flow = fraction(masses["maximum_flow"])
    unmet = fraction(masses["unmet_demand"])
    cut_demand = fraction(masses["min_cut_state_demand"])
    cut_capacity = fraction(masses["min_cut_pair_capacity"])

    if not checks.get("statewise_alternate_route_domination"):
        raise AssertionError("one corrected alternate route lost singleton domination")
    if checks.get("exact_alternate_route_flow_feasible"):
        raise AssertionError("alternate route unexpectedly became globally feasible")
    if not checks.get("corrected_closing_edge"):
        raise AssertionError("corrected staircase closing edge was not certified")
    if demand - flow != unmet or cut_demand - cut_capacity != unmet:
        raise AssertionError("alternate-route max-flow/min-cut identity failed")
    if unmet <= 0:
        raise AssertionError("alternate-route no-go has no positive deficit")

    expected = {
        "recursive_states": 278,
        "min_cut_states": 19,
        "min_cut_pairs": 176,
    }
    for key, value in expected.items():
        if counts.get(key) != value:
            raise AssertionError(
                f"alternate-route no-go profile changed for {key}: {counts.get(key)}"
            )

    print(process.stdout, end="")
    print("verified: corrected S7 alternate-route exact min-cut no-go")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
