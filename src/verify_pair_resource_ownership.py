#!/usr/bin/env python3
"""Certify exact pair-resource containment for R4->F5."""
from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import sys

import probe_pair_resource_ownership as probe

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED = {
    "probe_payload_sha256": "5ec066d16ec0175e7e78e2aafb05404aca67af8090edc143a4dfe6697b55d51c",
    "parent_resources_sha256": "69446f6ea2ebea4700942b54a94f9e211790a21f40d1fb5944058c0b702a1d2e",
    "child_resources_sha256": "bd056d5ed1fd97139bcd804f1b34673a4d5f8b3bf45787dc515b068e6bf4171f",
    "child_rows_sha256": "3f4d7e3f08aa9b95864dc1ef53b657d8c3a280ffb0fdcdc5cab470c802abbecb",
    "unused_parent_pairs_sha256": "f3ca0b9ed198e6d0e9869e1fda244d855893246ee047f4344a9046015087ee12",
}


def load_probe() -> dict[str, object]:
    buffer = StringIO()
    with redirect_stdout(buffer):
        status = probe.main()
    if status != 0:
        raise AssertionError(f"pair-resource probe failed: {status}")
    return json.loads(buffer.getvalue())


def build_certificate() -> str:
    payload = load_probe()
    if payload["probe_payload_sha256"] != EXPECTED["probe_payload_sha256"]:
        raise AssertionError("probe payload changed")
    for key in (
        "parent_resources",
        "child_resources",
        "child_rows",
        "unused_parent_pairs",
    ):
        if payload["hashes"][key] != EXPECTED[f"{key}_sha256"]:
            raise AssertionError(f"{key} changed")
    if payload["generation_six_propagated"]:
        raise AssertionError("generation six was unexpectedly propagated")
    if not payload["containment_verified"]:
        raise AssertionError("child resource containment failed")
    if not payload["partition_verified"]:
        raise AssertionError("pair resource partition failed")
    if not payload["child_pair_disjointness_verified"]:
        raise AssertionError("child pair resources overlap")

    counts = payload["counts"]
    expected_counts = {
        "parent_states": 12,
        "parent_current_pairs": 1717,
        "parent_latent_pairs": 370505,
        "parent_resource_pairs": 372222,
        "parent_max_pair_multiplicity": 1,
        "fifth_states": 21,
        "fifth_current_pairs": 1032,
        "fifth_terminal_current_pairs": 17,
        "fifth_recursive_current_pairs": 1015,
        "fifth_recursive_latent_pairs": 106381,
        "child_resource_pairs": 107413,
        "child_max_pair_multiplicity": 1,
        "unused_parent_pairs": 264809,
        "terminal_from_parent_current": 0,
        "terminal_from_parent_latent": 17,
        "recursive_current_from_parent_current": 0,
        "recursive_current_from_parent_latent": 1015,
        "recursive_latent_from_parent_current": 0,
        "recursive_latent_from_parent_latent": 106381,
    }
    for key, expected in expected_counts.items():
        if counts[key] != expected:
            raise AssertionError(f"count {key} changed: {counts[key]}")

    masses = payload["masses"]
    expected_masses = {
        "child_occurrence_resource": "1586.466623468978",
        "child_union_resource": "1586.466623468978",
        "child_repeated_resource": "0.000000000000",
        "parent_occurrence_resource": "2745.394378841703",
        "parent_union_resource": "2745.394378841703",
        "unused_parent_resource": "1158.927755372724",
        "child_over_parent_ratio": "0.577864745297",
    }
    for key, expected in expected_masses.items():
        if masses[key]["decimal"] != expected:
            raise AssertionError(f"mass {key} changed")

    lines = [
        "pair_resource_ownership_certificate_v1",
        "scope=certified_R4_recursive_to_complete_F5_retained_transition",
        "generation_six_propagated=false",
        "containment_verified=true",
        "partition_verified=true",
        "child_pair_disjointness_verified=true",
        "parent_states=12",
        "parent_current_pairs=1717",
        "parent_latent_pairs=370505",
        "parent_resource_pairs=372222",
        "parent_max_pair_multiplicity=1",
        "fifth_states=21",
        "fifth_current_pairs=1032",
        "fifth_terminal_current_pairs=17",
        "fifth_recursive_current_pairs=1015",
        "fifth_recursive_latent_pairs=106381",
        "child_resource_pairs=107413",
        "child_max_pair_multiplicity=1",
        "unused_parent_pairs=264809",
        "terminal_from_parent_current=0",
        "terminal_from_parent_latent=17",
        "recursive_current_from_parent_current=0",
        "recursive_current_from_parent_latent=1015",
        "recursive_latent_from_parent_current=0",
        "recursive_latent_from_parent_latent=106381",
        "child_resource_mass_decimal=1586.466623468978",
        "parent_resource_mass_decimal=2745.394378841703",
        "unused_parent_resource_mass_decimal=1158.927755372724",
        "child_over_parent_ratio_decimal=0.577864745297",
        f"parent_resources_sha256={payload['hashes']['parent_resources']}",
        f"child_resources_sha256={payload['hashes']['child_resources']}",
        f"child_rows_sha256={payload['hashes']['child_rows']}",
        f"unused_parent_pairs_sha256={payload['hashes']['unused_parent_pairs']}",
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
