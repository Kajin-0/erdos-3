#!/usr/bin/env python3
"""Certify the exact fourth-to-fifth root-lineage classification."""
from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import sys

import probe_root_lineage_transfer_classification as probe

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED = {
    "probe_payload_sha256": "dc268101bda80c60b30d50c90d89cbd077d1bce203230bfbf44f073a6526f6e7",
    "survivor_rows_sha256": "53d8f83518fbeefe33ef532cba207c4f829f9c0aa6086f192ab12c30891cbffd",
    "exit_rows_sha256": "bde9a30bf562dafca35ecee982d96b121cfde59d15553b5ed4ca4d0c8a783961",
    "survivor_groups_sha256": "37a52d9fb7928a11cf815295fd71925dc95054e7ade70bd34c732ed027a226dc",
    "exit_groups_sha256": "c10aeeedad61cfcab66a5309be7ec3c59aec8149b121e4fd34b985f7f4c20356",
}

EXPECTED_SHELLS = {
    1: (622, "e34daf57c8b79fc268e11cb713402af201739e44a834fd7b53bf16cdabce92f0"),
    2: (351, "61cbb832c174229fb37ac45a2256db5f3d7887c9d6b559e8bd93b8ef157e0b6c"),
    5: (27, "32e284bcb6cc295cf4fb756dec019ee6426407d7582fb76bc353e342de49538a"),
    7: (9, "d97be5dbf98326483f7cc69cdeb21c3ac4c8b20fa349c28d2ff0a45055e7cd38"),
    9: (3, "910e830540916e0821852ae46af4a13edfedf38c442c44ca1e746adbfb36e9c3"),
    10: (3, "48fd0c8f5721ddf14b95dc97acd86d104341aef7d3460efa553d35edce933c92"),
}

EXPECTED_FATES = {
    "dropped_raw_fully_numerically_covered": (
        280,
        "1b5e01d8c9927ad103806483a32894d80f8216b43b5e0d4a0df9fc2e948a868a",
    ),
    "dropped_no_raw_output": (
        12,
        "8cee409ae283642b31dbe4ed7107f6e4490f1980e68501e75356f42df0629d76",
    ),
    "terminalized": (
        17,
        "8c54e02d7b1ef4e490e5b99e61f21cddb7603c13e89f58cb95cf5651933b5728",
    ),
    "dropped_raw_not_numerically_covered": (
        130,
        "19357d46c6aaf96a35ac0e90b573142c4ff68ecead5b384ac09538143f087231",
    ),
    "dropped_raw_partially_numerically_covered": (
        263,
        "9fd51e95efa4de9df3a041c6c70e1f2039f1ac827512fab0653e26e16b5572bb",
    ),
}

EXPECTED_PARENT_GAINS = {
    24: (22, "8d927bafe6991355eb508a439dc530fee67cf1b615a6b128cae3cfeb96b2b2fb"),
    48: (40, "6ea155983a055a6133533b0f029dc25a2d2b5ee8318b6a299fd8ac5b73941fef"),
    65: (67, "8411925085c563d64ad73dfd2b3d8ecfaa380a25d041cd2f7e45f3a9a138372b"),
    68: (9, "d97be5dbf98326483f7cc69cdeb21c3ac4c8b20fa349c28d2ff0a45055e7cd38"),
    77: (153, "cb7e00cd89cbc1d342e6d456de55ac6f9520f75fab88e4a430df987eae9810ce"),
    82: (361, "ff473bb294ad7336a47e439613b4d1bbd6a1c90552a857c92b98acecd7242ae6"),
    93: (363, "cf3c9ee947494895b6c577cf0e38a854c7a36e8e5f3984982dd5602c04e50289"),
}


def load_probe() -> dict[str, object]:
    buffer = StringIO()
    with redirect_stdout(buffer):
        status = probe.main()
    if status != 0:
        raise AssertionError(f"classification probe failed: {status}")
    return json.loads(buffer.getvalue())


def build_certificate() -> str:
    payload = load_probe()
    if payload["probe_payload_sha256"] != EXPECTED["probe_payload_sha256"]:
        raise AssertionError("probe payload changed")
    for key in (
        "survivor_rows",
        "exit_rows",
        "survivor_groups",
        "exit_groups",
    ):
        if payload["hashes"][key] != EXPECTED[f"{key}_sha256"]:
            raise AssertionError(f"{key} changed")

    counts = payload["counts"]
    expected_counts = {
        "fourth_recursive_roots": 1717,
        "surviving_roots": 1015,
        "terminalized_roots": 17,
        "dropped_roots": 685,
        "split_roots": 0,
        "survivor_immediate_provenance_matches": 1015,
    }
    for key, expected in expected_counts.items():
        if counts[key] != expected:
            raise AssertionError(f"{key} changed: {counts[key]}")
    if not payload["identity"]["verified"]:
        raise AssertionError("root-transfer identity failed")

    source_rows = payload["survivor_groups"]["child_source"]
    if len(source_rows) != 1:
        raise AssertionError("more than one surviving source type")
    source_row = source_rows[0]
    if source_row["child_source"] != "backbone" or source_row["count"] != 1015:
        raise AssertionError("surviving lineages are not exactly the backbone family")

    shell_rows = {
        int(row["shell_drop"]): row
        for row in payload["survivor_groups"]["shell_drop"]
    }
    if set(shell_rows) != set(EXPECTED_SHELLS):
        raise AssertionError("shell-drop support changed")
    for shell, (count, gain_hash) in EXPECTED_SHELLS.items():
        row = shell_rows[shell]
        if row["count"] != count or row["gain"]["sha256"] != gain_hash:
            raise AssertionError(f"shell-drop class {shell} changed")

    fate_rows = {
        row["fate"]: row for row in payload["exit_groups"]["fate"]
    }
    if set(fate_rows) != set(EXPECTED_FATES):
        raise AssertionError("exit-fate support changed")
    for fate, (count, release_hash) in EXPECTED_FATES.items():
        row = fate_rows[fate]
        if row["count"] != count or row["parent_release"]["sha256"] != release_hash:
            raise AssertionError(f"exit fate {fate} changed")

    parent_rows = {
        int(row["parent_state_class"]): row
        for row in payload["survivor_groups"]["parent_state_class"]
    }
    if set(parent_rows) != set(EXPECTED_PARENT_GAINS):
        raise AssertionError("surviving parent-class support changed")
    for parent_class, (count, gain_hash) in EXPECTED_PARENT_GAINS.items():
        row = parent_rows[parent_class]
        if row["count"] != count or row["gain"]["sha256"] != gain_hash:
            raise AssertionError(f"parent class {parent_class} changed")

    concentration = payload["survivor_gain_concentration"]
    expected_concentration = {
        "top_10": "0.535180381624",
        "top_25": "0.738996562217",
        "top_100": "0.892166532723",
    }
    for key, expected_decimal in expected_concentration.items():
        if concentration[key]["share_decimal"] != expected_decimal:
            raise AssertionError(f"gain concentration {key} changed")

    lines = [
        "root_lineage_transfer_classification_certificate_v1",
        "scope=certified_baseline_fourth_to_fifth_transition",
        "identity=H5_recursive-H4_recursive=survivor_scale_gain-exiting_parent_release",
        "identity_verified=true",
        "fourth_recursive_roots=1717",
        "surviving_roots=1015",
        "terminalized_roots=17",
        "dropped_roots=685",
        "split_roots=0",
        "survivor_immediate_provenance_matches=1015",
        "surviving_source_types=backbone",
        "surviving_backbone_roots=1015",
        "surviving_middle_fiber_roots=0",
        "shell_drop_support=1,2,5,7,9,10",
        "shell_drop_counts=622,351,27,9,3,3",
        "survivor_parent_classes=24,48,65,68,77,82,93",
        "top10_gain_share_decimal=0.535180381624",
        "top25_gain_share_decimal=0.738996562217",
        "top100_gain_share_decimal=0.892166532723",
        "dropped_no_raw_output_roots=12",
        "dropped_with_raw_output_roots=673",
        "dropped_raw_fully_numerically_covered=280",
        "dropped_raw_partially_numerically_covered=263",
        "dropped_raw_not_numerically_covered=130",
        f"survivor_scale_gain_decimal={payload['masses']['survivor_scale_gain']['decimal']}",
        f"exiting_parent_release_decimal={payload['masses']['exiting_parent_release']['decimal']}",
        f"recursive_delta_decimal={payload['masses']['recursive_delta']['decimal']}",
        f"survivor_rows_sha256={payload['hashes']['survivor_rows']}",
        f"exit_rows_sha256={payload['hashes']['exit_rows']}",
        f"survivor_groups_sha256={payload['hashes']['survivor_groups']}",
        f"exit_groups_sha256={payload['hashes']['exit_groups']}",
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
