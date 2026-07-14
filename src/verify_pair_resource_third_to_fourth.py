#!/usr/bin/env python3
"""Certify exact R3-to-F4 affine pair-resource contraction."""
from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import sys

import probe_pair_resource_third_to_fourth as probe

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED = {
    "probe_payload_sha256": "b60aadd11f59e5f1e864ec90fa3482f15e1ca08632b73fb6d212ef39d4bd61fb",
    "parent_resources_sha256": "137dd01efb904f5c591656649bb7dccd27a54731b5f79808943bd1a6f7c870cb",
    "child_resources_sha256": "8f0e8c382b82546379f37048bfd5e8d0f36e8d26e60b886ce4e66b1dab650524",
    "empty_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
}


def load_probe() -> dict[str, object]:
    buffer = StringIO()
    with redirect_stdout(buffer):
        status = probe.main()
    if status != 0:
        raise AssertionError(f"R3-to-F4 probe failed: {status}")
    return json.loads(buffer.getvalue())


def build_certificate() -> str:
    payload = load_probe()
    if payload["probe_payload_sha256"] != EXPECTED["probe_payload_sha256"]:
        raise AssertionError("probe payload changed")
    if payload["hashes"]["parent_resources"] != EXPECTED["parent_resources_sha256"]:
        raise AssertionError("parent resource family changed")
    if payload["hashes"]["child_resources"] != EXPECTED["child_resources_sha256"]:
        raise AssertionError("child resource family changed")
    if payload["hashes"]["missing_current"] != EXPECTED["empty_sha256"]:
        raise AssertionError("missing current resources appeared")
    if payload["hashes"]["missing_latent"] != EXPECTED["empty_sha256"]:
        raise AssertionError("missing latent resources appeared")
    if payload["generation_five_or_six_propagated_for_test"]:
        raise AssertionError("later generation unexpectedly propagated")

    parent = payload["parent"]
    child = payload["child"]
    containment = payload["containment"]
    bellman = payload["bellman"]
    expected_parent = {
        "recursive_states": 14,
        "points": 4789,
        "affine_states": 14,
        "nonaffine_states": 0,
        "resource_occurrences": 2155298,
        "distinct_resources": 2155127,
        "maximum_resource_multiplicity": 2,
        "repeated_resource_tokens": 171,
        "current_pairs": 4789,
        "latent_pairs": 2150356,
    }
    for key, expected in expected_parent.items():
        if parent[key] != expected:
            raise AssertionError(f"parent {key} changed")
    if parent["nonaffine_rows"]:
        raise AssertionError("non-affine R3 parent appeared")
    if parent["occurrence_resource_mass"]["decimal"] != "7828.862146571999":
        raise AssertionError("parent occurrence mass changed")
    if parent["union_resource_mass"]["decimal"] != "7821.150527735019":
        raise AssertionError("parent union mass changed")
    if parent["repeated_resource_mass"]["decimal"] != "7.711618836980":
        raise AssertionError("parent repeated mass changed")

    expected_child = {
        "total_states": 23,
        "total_points": 1794,
        "terminal_states": 11,
        "recursive_states": 12,
        "resources_from_affine_parents": 372299,
        "distinct_resources_from_affine_parents": 372286,
        "maximum_resource_multiplicity": 2,
        "repeated_resource_tokens": 13,
        "terminal_current_pairs": 77,
        "recursive_current_pairs": 1717,
        "recursive_latent_pairs": 370505,
        "points_from_nonaffine_parents": 0,
    }
    for key, expected in expected_child.items():
        if child[key] != expected:
            raise AssertionError(f"child {key} changed")
    if child["occurrence_resource_mass"]["decimal"] != "2747.630136815823":
        raise AssertionError("child occurrence mass changed")
    if child["union_resource_mass"]["decimal"] != "2747.496183058024":
        raise AssertionError("child union mass changed")
    if child["repeated_resource_mass"]["decimal"] != "0.133953757799":
        raise AssertionError("child repeated mass changed")
    if child["mass_from_nonaffine_parents"]["fraction"] != "0":
        raise AssertionError("non-affine child mass appeared")

    if not containment["all_affine_parent_resources_contained"]:
        raise AssertionError("resource containment failed")
    for key in (
        "missing_current_occurrences",
        "missing_current_pairs",
        "missing_latent_occurrences",
        "missing_latent_pairs",
    ):
        if containment[key] != 0:
            raise AssertionError(f"{key} changed")
    if not bellman["occurrence_verified"] or not bellman["union_verified"]:
        raise AssertionError("Bellman contraction failed")
    expected_bellman = {
        "occurrence_left": "2747.630136815823",
        "occurrence_right": "7828.862146571999",
        "occurrence_surplus": "5081.232009756176",
        "union_left": "2747.496183058024",
        "union_right": "7821.150527735019",
        "union_surplus": "5073.654344676995",
    }
    for key, expected in expected_bellman.items():
        if bellman[key]["decimal"] != expected:
            raise AssertionError(f"Bellman {key} changed")

    expected_types = {
        "terminal_from_parent_current": 0,
        "terminal_from_parent_latent": 77,
        "recursive_current_from_parent_current": 0,
        "recursive_current_from_parent_latent": 1717,
        "recursive_latent_from_parent_current": 0,
        "recursive_latent_from_parent_latent": 370505,
    }
    if payload["type_counts"] != expected_types:
        raise AssertionError("resource-type classification changed")

    lines = [
        "pair_resource_third_to_fourth_certificate_v1",
        "scope=certified_R3_recursive_to_complete_F4_retained_transition",
        "generation_five_or_six_propagated_for_test=false",
        "R3_recursive_states=14",
        "R3_points=4789",
        "R3_affine_states=14",
        "R3_nonaffine_states=0",
        "R3_resource_occurrences=2155298",
        "R3_distinct_resources=2155127",
        "R3_max_resource_multiplicity=2",
        "R3_repeated_resource_tokens=171",
        "R3_occurrence_resource_mass_decimal=7828.862146571999",
        "R3_union_resource_mass_decimal=7821.150527735019",
        "R3_repeated_resource_mass_decimal=7.711618836980",
        "F4_total_states=23",
        "F4_total_points=1794",
        "F4_affine_parent_resources=372299",
        "F4_distinct_affine_parent_resources=372286",
        "F4_max_resource_multiplicity=2",
        "F4_repeated_resource_tokens=13",
        "F4_occurrence_resource_mass_decimal=2747.630136815823",
        "F4_union_resource_mass_decimal=2747.496183058024",
        "F4_repeated_resource_mass_decimal=0.133953757799",
        "missing_current_resources=0",
        "missing_latent_resources=0",
        "occurrence_surplus_decimal=5081.232009756176",
        "union_surplus_decimal=5073.654344676995",
        "occurrence_verified=true",
        "union_verified=true",
        f"parent_resources_sha256={payload['hashes']['parent_resources']}",
        f"child_resources_sha256={payload['hashes']['child_resources']}",
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
