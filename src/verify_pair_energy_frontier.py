#!/usr/bin/env python3
"""Certify the exact R4-to-F5 root-pair Bellman row."""
from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import sys

import probe_pair_energy_frontier as probe

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED = {
    "probe_payload_sha256": "3ad12e2da934fd74028f4ab104622883e77e1b2e6e65e82c1b7ad7141027994e",
    "profiles_sha256": "421fb8248330432afb882a30235d1aebec9bae85603bb1c9a62dbdac62e90632",
    "bellman_rows_sha256": "17cc81b82cf7ab3fd266e713da0ba2a0a4c3871aa3c1d7c7d3404f349fb991d3",
    "r4_root_multiplicity_sha256": "2589aceadec230be164114bc5a3111ad1a78b1a7f43c9b624f817c275868cdfd",
    "r4_pair_multiplicity_sha256": "534d0269f557b218545f5eeb2ad9fe01d41e0ba74fdceedf95b71ad8043b7e85",
    "r5_root_multiplicity_sha256": "73e3106c98b499149a0d39d6664636ca1fa057ab2355babd068aed65f82f5982",
    "r5_pair_multiplicity_sha256": "2f7b21f99465f22d9a2085698435683772388639ebe1b0e1783d3541de464c94",
}


def load_probe() -> dict[str, object]:
    buffer = StringIO()
    with redirect_stdout(buffer):
        status = probe.main()
    if status != 0:
        raise AssertionError(f"pair-energy probe failed: {status}")
    return json.loads(buffer.getvalue())


def build_certificate() -> str:
    payload = load_probe()
    if payload["probe_payload_sha256"] != EXPECTED["probe_payload_sha256"]:
        raise AssertionError("probe payload changed")
    if payload["hashes"]["profiles"] != EXPECTED["profiles_sha256"]:
        raise AssertionError("profile payload changed")
    if payload["hashes"]["bellman_rows"] != EXPECTED["bellman_rows_sha256"]:
        raise AssertionError("Bellman row changed")

    profiles = {profile["name"]: profile for profile in payload["profiles"]}
    if set(profiles) != {"R4_recursive", "R5_recursive"}:
        raise AssertionError("pair profile support changed")
    r4 = profiles["R4_recursive"]
    r5 = profiles["R5_recursive"]

    expected_profiles = {
        "R4_recursive": {
            "states": 12,
            "points": 1717,
            "distinct_roots": 1717,
            "maximum_root_multiplicity": 1,
            "pair_occurrences": 370505,
            "distinct_pairs": 370505,
            "maximum_pair_multiplicity": 1,
            "affine_states": 12,
            "nonaffine_states": 0,
            "H": "1.536133538213",
            "J": "2743.858245303490",
        },
        "R5_recursive": {
            "states": 13,
            "points": 1015,
            "distinct_roots": 1015,
            "maximum_root_multiplicity": 1,
            "pair_occurrences": 106381,
            "distinct_pairs": 106381,
            "maximum_pair_multiplicity": 1,
            "affine_states": 13,
            "nonaffine_states": 0,
            "H": "2.042771729559",
            "J": "1582.379988513372",
        },
    }
    for name, expected in expected_profiles.items():
        profile = profiles[name]
        for key in (
            "states",
            "points",
            "distinct_roots",
            "maximum_root_multiplicity",
            "pair_occurrences",
            "distinct_pairs",
            "maximum_pair_multiplicity",
            "affine_states",
            "nonaffine_states",
        ):
            if profile[key] != expected[key]:
                raise AssertionError(f"{name} {key} changed")
        if profile["harmonic_mass"]["decimal"] != expected["H"]:
            raise AssertionError(f"{name} H changed")
        if profile["pair_energy_occurrence"]["decimal"] != expected["J"]:
            raise AssertionError(f"{name} J changed")
        if profile["pair_energy_union"] != profile["pair_energy_occurrence"]:
            raise AssertionError(f"{name} occurrence/union energy diverged")
        if profile["repeated_pair_energy"]["fraction"] != "0":
            raise AssertionError(f"{name} repeated pair energy appeared")

    if r4["root_multiplicity_sha256"] != EXPECTED["r4_root_multiplicity_sha256"]:
        raise AssertionError("R4 root multiplicity changed")
    if r4["pair_multiplicity_sha256"] != EXPECTED["r4_pair_multiplicity_sha256"]:
        raise AssertionError("R4 pair multiplicity changed")
    if r5["root_multiplicity_sha256"] != EXPECTED["r5_root_multiplicity_sha256"]:
        raise AssertionError("R5 root multiplicity changed")
    if r5["pair_multiplicity_sha256"] != EXPECTED["r5_pair_multiplicity_sha256"]:
        raise AssertionError("R5 pair multiplicity changed")

    fifth = payload["fifth_output"]
    expected_fifth = {
        "total_states": 21,
        "total_points": 1032,
        "terminal_states": 8,
        "terminal_points": 17,
        "recursive_states": 13,
        "recursive_points": 1015,
    }
    for key, expected in expected_fifth.items():
        if fifth[key] != expected:
            raise AssertionError(f"fifth output {key} changed")
    if fifth["total_harmonic_mass"]["decimal"] != "4.086634955606":
        raise AssertionError("fifth total harmonic mass changed")
    if fifth["terminal_harmonic_mass"]["decimal"] != "2.043863226048":
        raise AssertionError("fifth terminal harmonic mass changed")
    if fifth["recursive_harmonic_mass"]["decimal"] != "2.042771729559":
        raise AssertionError("fifth recursive harmonic mass changed")

    occurrence = payload["bellman_rows"]["occurrence_pair_energy"]
    union = payload["bellman_rows"]["union_pair_energy"]
    for row in (occurrence, union):
        if not row["verified"]:
            raise AssertionError("pair-energy row no longer verifies")
        if row["left_H5_plus_J5"]["decimal"] != "1586.466623468978":
            raise AssertionError("Bellman left side changed")
        if row["right_J4"]["decimal"] != "2743.858245303490":
            raise AssertionError("Bellman right side changed")
        if row["surplus"]["decimal"] != "1157.391621834512":
            raise AssertionError("Bellman surplus changed")
        if row["ratio"]["decimal"] != "0.578188259610":
            raise AssertionError("Bellman ratio changed")
    if occurrence != union:
        raise AssertionError("occurrence and union rows diverged")
    if payload["generation_six_propagated"]:
        raise AssertionError("generation six was unexpectedly propagated")

    lines = [
        "pair_energy_frontier_certificate_v1",
        "scope=certified_R4_recursive_to_F5_retained_transition",
        "generation_six_propagated=false",
        "R4_states=12",
        "R4_points=1717",
        "R4_affine_states=12",
        "R4_max_root_multiplicity=1",
        "R4_pair_occurrences=370505",
        "R4_distinct_pairs=370505",
        "R4_max_pair_multiplicity=1",
        "R4_pair_energy_decimal=2743.858245303490",
        "R5_recursive_states=13",
        "R5_recursive_points=1015",
        "R5_affine_states=13",
        "R5_max_root_multiplicity=1",
        "R5_pair_occurrences=106381",
        "R5_distinct_pairs=106381",
        "R5_max_pair_multiplicity=1",
        "R5_pair_energy_decimal=1582.379988513372",
        "F5_total_harmonic_decimal=4.086634955606",
        "bellman_left_H5_plus_J5_decimal=1586.466623468978",
        "bellman_right_J4_decimal=2743.858245303490",
        "bellman_surplus_decimal=1157.391621834512",
        "bellman_ratio_decimal=0.578188259610",
        "bellman_verified=true",
        f"profiles_sha256={payload['hashes']['profiles']}",
        f"bellman_rows_sha256={payload['hashes']['bellman_rows']}",
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
