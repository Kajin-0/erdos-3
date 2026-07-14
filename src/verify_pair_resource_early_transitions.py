#!/usr/bin/env python3
"""Certify exact pair-resource rows for R1->F2 and R2->F3."""
from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import sys

import probe_pair_resource_early_transitions as probe

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED = {
    "probe_payload_sha256": "63370f215633d9c9b41421bf99dcd99fab0cc9391d18a8005de5985132afef1d",
    "transition_summaries_sha256": "3955bbc1d8e8c0d86c89f667299448296a9b06de3b728266223130a7d0bc8d68",
    "R1_to_F2": {
        "parent_resources": "1c4ca6bd95318f3a183cd446a58fcd30bfe537b317277a202c5c5fe0466ce214",
        "child_resources": "7840ae6513f45a92a55a2a73f849aa3ef131378907b33372ec76bb4d88b482fb",
        "parent_references": "73ca5d449456d8346f84f22173f98369aa8d949de8b06fd497a6f969eb65a7cc",
    },
    "R2_to_F3": {
        "parent_resources": "3ef578b3f190683c0191f0bf3558aa58cfca00a8026114c9e2fc8d8a297ca53d",
        "child_resources": "7cfc719d19303394801f653668fdd4173cad46b35e06b7d182cf99db213a36e2",
        "parent_references": "6cf228ab9f1977ec82153d9098aa6f2e75a99e1839f5f15df99f94324584321f",
    },
}


def load_probe() -> dict[str, object]:
    buffer = StringIO()
    with redirect_stdout(buffer):
        status = probe.main()
    if status != 0:
        raise AssertionError(f"early-transition probe failed: {status}")
    return json.loads(buffer.getvalue())


def check_row(row: dict[str, object], expected: dict[str, object]) -> None:
    parent = row["parent"]
    child = row["child"]
    containment = row["containment"]
    bellman = row["bellman"]
    for key, value in expected["parent_counts"].items():
        if parent[key] != value:
            raise AssertionError(f"{row['name']} parent {key} changed")
    for key, value in expected["child_counts"].items():
        if child[key] != value:
            raise AssertionError(f"{row['name']} child {key} changed")
    for key, value in expected["parent_masses"].items():
        if parent[key]["decimal"] != value:
            raise AssertionError(f"{row['name']} parent {key} changed")
    for key, value in expected["child_masses"].items():
        if child[key]["decimal"] != value:
            raise AssertionError(f"{row['name']} child {key} changed")
    if not containment["all_resources_contained"]:
        raise AssertionError(f"{row['name']} containment failed")
    for key in (
        "missing_current_occurrences",
        "missing_current_pairs",
        "missing_latent_occurrences",
        "missing_latent_pairs",
    ):
        if containment[key] != 0:
            raise AssertionError(f"{row['name']} {key} changed")
    for key, value in expected["bellman_masses"].items():
        if bellman[key]["decimal"] != value:
            raise AssertionError(f"{row['name']} Bellman {key} changed")
    if bellman["occurrence_verified"] != expected["occurrence_verified"]:
        raise AssertionError(f"{row['name']} occurrence status changed")
    if bellman["union_verified"] is not True:
        raise AssertionError(f"{row['name']} union row failed")
    if row["type_counts"] != expected["type_counts"]:
        raise AssertionError(f"{row['name']} type counts changed")


def build_certificate() -> str:
    payload = load_probe()
    if payload["probe_payload_sha256"] != EXPECTED["probe_payload_sha256"]:
        raise AssertionError("probe payload changed")
    if payload["hashes"]["transition_summaries"] != EXPECTED["transition_summaries_sha256"]:
        raise AssertionError("transition summaries changed")
    if payload["later_generation_propagated_for_test"]:
        raise AssertionError("later generation unexpectedly propagated")
    rows = {row["name"]: row for row in payload["transitions"]}
    if set(rows) != {"R1_to_F2", "R2_to_F3"}:
        raise AssertionError("transition support changed")
    for name in rows:
        for hash_key in ("parent_resources", "child_resources", "parent_references"):
            if rows[name]["hashes"][hash_key] != EXPECTED[name][hash_key]:
                raise AssertionError(f"{name} {hash_key} changed")

    check_row(
        rows["R1_to_F2"],
        {
            "parent_counts": {
                "states": 21,
                "points": 11753,
                "affine_states": 21,
                "resource_occurrences": 4570986,
                "distinct_resources": 4570847,
                "maximum_resource_multiplicity": 3,
                "repeated_resource_tokens": 132,
                "current_pairs": 11748,
                "latent_pairs": 4559106,
            },
            "child_counts": {
                "total_states": 27,
                "total_points": 7925,
                "terminal_states": 13,
                "recursive_states": 14,
                "affine_states": 27,
                "resource_occurrences": 1836805,
                "distinct_resources": 1824223,
                "maximum_resource_multiplicity": 6,
                "repeated_resource_tokens": 12582,
                "terminal_current_pairs": 43,
                "recursive_current_pairs": 7882,
                "recursive_latent_pairs": 1816361,
            },
            "parent_masses": {
                "occurrence_resource_mass": "13748.209979521601",
                "union_resource_mass": "13747.585619743902",
                "repeated_resource_mass": "0.624359777699",
            },
            "child_masses": {
                "occurrence_resource_mass": "36736.589235237363",
                "union_resource_mass": "11399.171002318168",
                "repeated_resource_mass": "25337.418232919194",
            },
            "bellman_masses": {
                "occurrence_left": "36736.589235237363",
                "occurrence_right": "13748.209979521601",
                "occurrence_surplus": "-22988.379255715762",
                "occurrence_ratio": "2.672100509124",
                "union_left": "11399.171002318168",
                "union_right": "13747.585619743902",
                "union_surplus": "2348.414617425734",
                "union_ratio": "0.829175494359",
            },
            "occurrence_verified": False,
            "type_counts": {
                "terminal_from_parent_current": 0,
                "terminal_from_parent_latent": 43,
                "recursive_current_from_parent_current": 0,
                "recursive_current_from_parent_latent": 7882,
                "recursive_latent_from_parent_current": 0,
                "recursive_latent_from_parent_latent": 1816361,
            },
        },
    )
    check_row(
        rows["R2_to_F3"],
        {
            "parent_counts": {
                "states": 14,
                "points": 7882,
                "affine_states": 14,
                "resource_occurrences": 1836762,
                "distinct_resources": 1824180,
                "maximum_resource_multiplicity": 6,
                "repeated_resource_tokens": 12582,
                "current_pairs": 7839,
                "latent_pairs": 1816361,
            },
            "child_counts": {
                "total_states": 32,
                "total_points": 4899,
                "terminal_states": 18,
                "recursive_states": 14,
                "affine_states": 32,
                "resource_occurrences": 865365,
                "distinct_resources": 857085,
                "maximum_resource_multiplicity": 6,
                "repeated_resource_tokens": 8268,
                "terminal_current_pairs": 110,
                "recursive_current_pairs": 4789,
                "recursive_latent_pairs": 852186,
            },
            "parent_masses": {
                "occurrence_resource_mass": "36734.545372011315",
                "union_resource_mass": "11398.028689923307",
                "repeated_resource_mass": "25336.516682088008",
            },
            "child_masses": {
                "occurrence_resource_mass": "17565.080459895682",
                "union_resource_mass": "4288.950913734511",
                "repeated_resource_mass": "13276.129546161171",
            },
            "bellman_masses": {
                "occurrence_left": "17565.080459895682",
                "occurrence_right": "36734.545372011315",
                "occurrence_surplus": "19169.464912115633",
                "occurrence_ratio": "0.478219099042",
                "union_left": "4288.950913734511",
                "union_right": "11398.028689923307",
                "union_surplus": "7109.077776188796",
                "union_ratio": "0.376290635809",
            },
            "occurrence_verified": True,
            "type_counts": {
                "terminal_from_parent_current": 0,
                "terminal_from_parent_latent": 110,
                "recursive_current_from_parent_current": 0,
                "recursive_current_from_parent_latent": 4789,
                "recursive_latent_from_parent_current": 0,
                "recursive_latent_from_parent_latent": 852186,
            },
        },
    )

    lines = [
        "pair_resource_early_transitions_certificate_v1",
        "scope=certified_R1_to_F2_and_R2_to_F3_retained_transitions",
        "later_generation_propagated_for_test=false",
        "R1_states=21",
        "R1_affine_states=21",
        "R1_union_resource_mass_decimal=13747.585619743902",
        "F2_union_resource_mass_decimal=11399.171002318168",
        "R1_to_F2_union_ratio_decimal=0.829175494359",
        "R1_to_F2_union_verified=true",
        "R1_occurrence_resource_mass_decimal=13748.209979521601",
        "F2_occurrence_resource_mass_decimal=36736.589235237363",
        "R1_to_F2_occurrence_ratio_decimal=2.672100509124",
        "R1_to_F2_occurrence_verified=false",
        "F2_repeated_resource_mass_decimal=25337.418232919194",
        "R2_states=14",
        "R2_affine_states=14",
        "R2_union_resource_mass_decimal=11398.028689923307",
        "F3_union_resource_mass_decimal=4288.950913734511",
        "R2_to_F3_union_ratio_decimal=0.376290635809",
        "R2_to_F3_union_verified=true",
        "R2_occurrence_resource_mass_decimal=36734.545372011315",
        "F3_occurrence_resource_mass_decimal=17565.080459895682",
        "R2_to_F3_occurrence_ratio_decimal=0.478219099042",
        "R2_to_F3_occurrence_verified=true",
        "F3_repeated_resource_mass_decimal=13276.129546161171",
        f"transition_summaries_sha256={payload['hashes']['transition_summaries']}",
        f"probe_payload_sha256={payload['probe_payload_sha256']}",
    ]
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
