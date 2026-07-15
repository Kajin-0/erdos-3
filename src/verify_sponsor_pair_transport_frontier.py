#!/usr/bin/env python3
"""Verify the exact sponsor-pair transport classification certificate."""
from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import sys

import probe_sponsor_pair_transport_frontier as probe

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED_PROBE_SHA256 = "062aa9b6a940bfeac6d24036bd2cdaeeb80b30498bc7c69fd83072281eb87e1d"
EXPECTED_ACTIVE_ROWS_SHA256 = "17b731b7c0758876e7930158bd99e1b1a037c32eda238fdcf3d9374856fb45c9"
EXPECTED_TARGET_COUNTER_SHA256 = "208db966a2747eb2568c6ac25bc9b8cb57c139b92af8c8f1203fa220d8b1541c"

EXPECTED_COUNTS = {
    "parent_states": 12,
    "split_retained_states": 37,
    "resource_occurrences": 75_287,
    "distinct_resource_pairs": 75_284,
    "activated_distinct_pairs": 75_247,
    "inactive_residual_distinct_pairs": 37,
    "terminal_target_distinct_pairs": 40_512,
    "terminal_collision_targets": 19_593,
    "maximum_terminal_target_multiplicity": 32,
    "maximum_transport_path_length": 6,
    "in_parent_completed_pairs": 8_725,
    "parent_external_completion_pairs": 66_522,
}

EXPECTED_MASSES = {
    "activated_initial_union": "1181.622166508078",
    "terminal_target_occurrence": "1681.403685763747",
    "terminal_target_union": "970.461110516518",
    "transport_collision": "710.942575247229",
    "selected_action_incidence_bound": "853.192982305550",
    "direct_target_union": "399.890641838252",
    "transport_rhs": "2824.633970064733",
    "transport_slack": "1643.011803556655",
}

EXPECTED_TERMINAL = {
    "backward": (72_363, "760.440265648176", "1228.079324208665"),
    "direct": (1_513, "417.530512851610", "420.905273251794"),
    "residual": (1_371, "3.651388008292", "32.419088303288"),
}

EXPECTED_RESOURCE = {
    ("latent_recursive",): (74_188, "1177.643059944907"),
    ("current_terminal",): (192, "2.085226848558"),
    ("current_recursive",): (864, "1.873962098445"),
    ("current_terminal", "latent_recursive"): (3, "0.019917616169"),
}

EXPECTED_SOURCE = {
    ("backbone_sponsor",): (75_055, "1179.930455501841"),
    ("backbone_residual",): (174, "1.619603708883"),
    ("middle_fiber",): (15, "0.052189681185"),
    ("backbone_sponsor", "middle_fiber"): (3, "0.019917616169"),
}

EXPECTED_COLLISION_MULTIPLICITIES = {
    2: 14_695,
    3: 1_195,
    4: 2_367,
    5: 68,
    6: 192,
    7: 196,
    8: 540,
    9: 95,
    10: 26,
    11: 14,
    12: 11,
    13: 10,
    14: 24,
    15: 20,
    16: 95,
    17: 9,
    18: 13,
    19: 2,
    20: 4,
    22: 2,
    28: 1,
    30: 4,
    31: 3,
    32: 7,
}


def load_probe() -> dict[str, object]:
    buffer = StringIO()
    with redirect_stdout(buffer):
        status = probe.main()
    if status != 0:
        raise AssertionError(f"sponsor-pair probe failed: {status}")
    return json.loads(buffer.getvalue())


def profile_map(rows: list[dict[str, object]]) -> dict[object, dict[str, object]]:
    result: dict[object, dict[str, object]] = {}
    for row in rows:
        key = row["key"]
        if isinstance(key, list):
            key = tuple(key)
        result[key] = row
    return result


def build_certificate() -> str:
    payload = load_probe()
    if payload["schema"] != "sponsor_pair_transport_frontier_probe_v1":
        raise AssertionError("probe schema changed")
    if payload["generation_six_propagated"]:
        raise AssertionError("generation six was unexpectedly propagated")
    if payload["probe_payload_sha256"] != EXPECTED_PROBE_SHA256:
        raise AssertionError("probe payload hash changed")
    if payload["hashes"]["active_rows"] != EXPECTED_ACTIVE_ROWS_SHA256:
        raise AssertionError("active-row hash changed")
    if payload["hashes"]["terminal_target_counter"] != EXPECTED_TARGET_COUNTER_SHA256:
        raise AssertionError("terminal-target counter hash changed")

    for key, expected in EXPECTED_COUNTS.items():
        if payload["counts"][key] != expected:
            raise AssertionError(f"count changed: {key}")
    for key, expected in EXPECTED_MASSES.items():
        if payload["masses"][key]["decimal"] != expected:
            raise AssertionError(f"mass changed: {key}")
    for key, value in payload["checks"].items():
        if not value:
            raise AssertionError(f"transport check failed: {key}")

    terminal = profile_map(payload["terminal_class_profile"])
    for key, (count, initial, target) in EXPECTED_TERMINAL.items():
        row = terminal[key]
        if row["count"] != count:
            raise AssertionError(f"terminal count changed: {key}")
        if row["initial_mass"]["decimal"] != initial:
            raise AssertionError(f"terminal initial mass changed: {key}")
        if row["target_occurrence_mass"]["decimal"] != target:
            raise AssertionError(f"terminal target mass changed: {key}")

    resource = profile_map(payload["resource_signature_profile"])
    for key, (count, initial) in EXPECTED_RESOURCE.items():
        row = resource[key]
        if row["count"] != count or row["initial_mass"]["decimal"] != initial:
            raise AssertionError(f"resource profile changed: {key}")

    source = profile_map(payload["child_source_profile"])
    for key, (count, initial) in EXPECTED_SOURCE.items():
        row = source[key]
        if row["count"] != count or row["initial_mass"]["decimal"] != initial:
            raise AssertionError(f"source profile changed: {key}")

    collision_counts = Counter(
        int(row["multiplicity"]) for row in payload["collision_targets"]
    )
    if dict(sorted(collision_counts.items())) != EXPECTED_COLLISION_MULTIPLICITIES:
        raise AssertionError("collision multiplicity profile changed")

    parent = profile_map(payload["parent_profile"])
    if parent[93]["count"] != 46_723 or parent[82]["count"] != 23_325:
        raise AssertionError("dominant parent profile changed")
    side = profile_map(payload["first_sponsor_side_profile"])
    if side[1]["count"] != 71_766 or side[-1]["count"] != 3_481:
        raise AssertionError("sponsor-side profile changed")

    lines = [
        "sponsor_pair_transport_frontier_certificate_v1",
        "scope=certified_residual_sponsor_R4_to_complete_F5_retained_transition",
        "generation_six_propagated=false",
        "activated_distinct_pairs=75247",
        "inactive_residual_distinct_pairs=37",
        "backward_pairs=72363",
        "direct_pairs=1513",
        "residual_pairs=1371",
        "latent_recursive_pairs=74188",
        "backbone_sponsor_pairs=75055",
        "in_parent_completed_pairs=8725",
        "parent_external_completion_pairs=66522",
        "terminal_target_distinct_pairs=40512",
        "terminal_collision_targets=19593",
        "maximum_terminal_target_multiplicity=32",
        "maximum_transport_path_length=6",
        "activated_initial_union_mass_decimal=1181.622166508078",
        "backward_initial_mass_decimal=760.440265648176",
        "direct_initial_mass_decimal=417.530512851610",
        "residual_initial_mass_decimal=3.651388008292",
        "transport_collision_mass_decimal=710.942575247229",
        "terminal_target_union_mass_decimal=970.461110516518",
        "set_valued_transport_inequality=true",
        f"active_rows_sha256={EXPECTED_ACTIVE_ROWS_SHA256}",
        f"terminal_target_counter_sha256={EXPECTED_TARGET_COUNTER_SHA256}",
        f"probe_payload_sha256={EXPECTED_PROBE_SHA256}",
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
