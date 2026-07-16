#!/usr/bin/env python3
"""Exact source-weighted terminal-sink overflow profile for the S7 frontier."""
from __future__ import annotations
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib, json, sys


def pack(x: Fraction) -> dict[str, str]:
    return {"fraction": str(x), "decimal": f"{float(x):.15f}"}


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: probe_s7_source_weighted_sink_overflow.py INPUT OUTPUT")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    sources = {
        (int(r["parent_class"]), tuple(map(int, r["pair"]))): r
        for r in data["source_rows"]
    }
    graph = Counter()
    for key, row in sources.items():
        target = (key[0], tuple(map(int, row["target"])))
        if target == key:
            graph["fixed_sources"] += 1
        elif target in sources:
            graph["source_to_source"] += 1
            if tuple(map(int, sources[target]["target"])) != target[1]:
                graph["source_to_nonfixed_source"] += 1
        else:
            graph["source_to_external_sink"] += 1

    counts = Counter()
    totals: dict[str, Fraction] = defaultdict(Fraction)
    by_parent: dict[str, Fraction] = defaultdict(Fraction)
    by_status: dict[str, Fraction] = defaultdict(Fraction)
    by_class: dict[str, Fraction] = defaultdict(Fraction)
    max_ratio = Fraction()
    max_target = None

    for row in data["target_rows"]:
        source_mass = sum((Fraction(x[2]) for x in row["source_pairs"]), Fraction())
        capacity = Fraction(row["target_weight"])
        overflow = max(Fraction(), source_mass - capacity)
        target = tuple(map(int, row["target"]))
        anchored = any(
            tuple(map(int, pair)) == target
            and int(sources[(int(parent), tuple(map(int, pair)))]["path_length"]) == 0
            for parent, pair, _weight in row["source_pairs"]
        )
        counts["targets"] += 1
        counts["anchored_targets" if anchored else "unanchored_targets"] += 1
        if int(row["source_count"]) > 1:
            counts["collision_targets"] += 1
        if overflow:
            counts["overflow_targets"] += 1
            counts["anchored_overflow_targets" if anchored else "unanchored_overflow_targets"] += 1
        parents = tuple(map(int, row["parent_classes"]))
        if len(parents) != 1:
            counts["cross_parent_targets"] += 1
        totals["source_mass"] += source_mass
        totals["target_capacity"] += capacity
        totals["capacity_overflow"] += overflow
        totals["unused_capacity"] += max(Fraction(), capacity - source_mass)
        totals["anchored_overflow" if anchored else "unanchored_overflow"] += overflow
        totals["source_collision"] += Fraction(row["source_collision_weight"])
        pkey = str(parents[0]) if len(parents) == 1 else ",".join(map(str, parents))
        by_parent[pkey] += overflow
        by_status[str(row["completion_status"])] += overflow
        for value in set(map(str, row["terminal_classes"])):
            by_class[value] += overflow
        if capacity and source_mass / capacity > max_ratio:
            max_ratio, max_target = source_mass / capacity, target

    expected_counts = {
        "targets": 40512, "anchored_targets": 35841, "unanchored_targets": 4671,
        "collision_targets": 19593, "overflow_targets": 19512,
        "anchored_overflow_targets": 18151, "unanchored_overflow_targets": 1361,
        "cross_parent_targets": 0,
    }
    expected_graph = {
        "fixed_sources": 35841, "source_to_source": 30361,
        "source_to_external_sink": 9045, "source_to_nonfixed_source": 0,
    }
    if {k: counts.get(k, 0) for k in expected_counts} != expected_counts:
        raise AssertionError(f"sink count profile changed: {dict(counts)}")
    if {k: graph.get(k, 0) for k in expected_graph} != expected_graph:
        raise AssertionError(f"sink functional graph changed: {dict(graph)}")
    if totals["source_mass"] != Fraction(data["masses"]["activated_initial_union"]["fraction"]):
        raise AssertionError("source mass mismatch")
    if totals["capacity_overflow"] != totals["anchored_overflow"] + totals["unanchored_overflow"]:
        raise AssertionError("overflow partition failed")
    if totals["source_collision"] < totals["capacity_overflow"]:
        raise AssertionError("capacity overflow exceeds source collision")

    def profile(values: dict[str, Fraction], key: str) -> list[dict[str, object]]:
        return [{key: name, "overflow": pack(value)} for name, value in sorted(values.items(), key=lambda x: (-x[1], x[0]))]

    output = {
        "schema": "s7_source_weighted_sink_overflow_v1",
        "scope": data["scope"], "generation_six_propagated": False,
        "counts": expected_counts, "functional_graph": expected_graph,
        "masses": {name: pack(value) for name, value in sorted(totals.items())},
        "maximum_source_to_target_capacity_ratio": {
            "fraction": str(max_ratio), "decimal": f"{float(max_ratio):.15f}", "target": max_target,
        },
        "overflow_by_parent": profile(by_parent, "parent_class"),
        "overflow_by_completion_status": profile(by_status, "status"),
        "overflow_by_terminal_class": profile(by_class, "terminal_class"),
        "checks": {
            "all_target_collisions_intra_parent": True,
            "source_target_graph_has_only_fixed_cycles": True,
            "source_weighted_overflow_partition_exact": True,
            "target_capacity_does_not_cover_source_mass": totals["capacity_overflow"] > 0,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    Path(sys.argv[2]).write_text(json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
