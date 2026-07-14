#!/usr/bin/env python3
"""Certify the exact minimum-anchor backbone transfer decomposition."""
from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import sys

import probe_backbone_anchor_transfer as probe

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED = {
    "probe_payload_sha256": "9eaa661bd3890f25c57201b10bdec4e5d2b5118c5c08b574f4c316c86256f6f8",
    "parent_state_rows_sha256": "62aa35c701016a653a36744fec5797d1ca780ddf3d5fdc2031a5a1da6e1280da",
    "anchor_roots_sha256": "3777b91c37e2f2b80129958f0d685f5fe10efe4048be1da570210000f88809cf",
}

EXPECTED_EXPANDING = [24, 48, 65, 68, 77, 82]
EXPECTED_CONTRACTING = [6, 8, 12, 28, 42, 93]
EXPECTED_LOCAL_NET_DECIMALS = {
    77: "0.944033903564",
    68: "0.352686712797",
    24: "0.241761428763",
    82: "0.063230645618",
    48: "0.055582216875",
    65: "0.033476902052",
    93: "-0.000885974620",
    42: "-0.086112082763",
    28: "-0.105030676578",
    12: "-0.208338650597",
    8: "-0.274242424242",
    6: "-0.509523809524",
}


def load_probe() -> dict[str, object]:
    buffer = StringIO()
    with redirect_stdout(buffer):
        status = probe.main()
    if status != 0:
        raise AssertionError(f"backbone-anchor probe failed: {status}")
    return json.loads(buffer.getvalue())


def build_certificate() -> str:
    payload = load_probe()
    if payload["probe_payload_sha256"] != EXPECTED["probe_payload_sha256"]:
        raise AssertionError("probe payload changed")
    if payload["hashes"]["parent_state_rows"] != EXPECTED["parent_state_rows_sha256"]:
        raise AssertionError("parent-state rows changed")
    if payload["hashes"]["anchor_roots"] != EXPECTED["anchor_roots_sha256"]:
        raise AssertionError("anchor roots changed")

    counts = payload["counts"]
    expected_counts = {
        "parent_states": 12,
        "minimum_anchor_roots": 12,
        "minimum_anchors_dropped_no_raw_output": 12,
        "expanding_parent_states": 6,
        "contracting_parent_states": 6,
        "neutral_parent_states": 0,
    }
    for key, expected in expected_counts.items():
        if counts[key] != expected:
            raise AssertionError(f"{key} changed: {counts[key]}")
    if payload["expanding_parent_classes"] != EXPECTED_EXPANDING:
        raise AssertionError("expanding parent classes changed")
    if payload["contracting_parent_classes"] != EXPECTED_CONTRACTING:
        raise AssertionError("contracting parent classes changed")
    if payload["neutral_parent_classes"]:
        raise AssertionError("neutral parent class appeared")

    rows = {int(row["parent_state_class"]): row for row in payload["rows"]}
    if set(rows) != set(EXPECTED_LOCAL_NET_DECIMALS):
        raise AssertionError("parent-state support changed")
    for parent_class, expected_decimal in EXPECTED_LOCAL_NET_DECIMALS.items():
        row = rows[parent_class]
        if row["local_recursive_net"]["decimal"] != expected_decimal:
            raise AssertionError(f"local net changed for class {parent_class}")
        if row["anchor_fate"] != "dropped_no_raw_output":
            raise AssertionError(f"anchor fate changed for class {parent_class}")
        if row["anchor_raw_occurrences"] != 0:
            raise AssertionError(f"anchor raw occurrence appeared for class {parent_class}")
        if row["child_source_counts"] and set(row["child_source_counts"]) != {"backbone"}:
            raise AssertionError(f"non-backbone survivor in class {parent_class}")

    masses = payload["masses"]
    expected_mass_decimals = {
        "parent_recursive_mass": "1.536133538213",
        "full_translation_gain": "9.928706884742",
        "minimum_anchor_release": "0.364729899662",
        "retained_survivor_gain": "1.816777911848",
        "exit_release": "1.310139720502",
        "recursive_net": "0.506638191346",
    }
    for key, expected_decimal in expected_mass_decimals.items():
        if masses[key]["decimal"] != expected_decimal:
            raise AssertionError(f"{key} changed")

    ratios = payload["ratios"]
    expected_ratio_decimals = {
        "full_translation_gain_over_anchor_release": "27.222081035667",
        "retained_gain_over_anchor_release": "4.981159793944",
        "retained_gain_fraction_of_full_translation": "0.182982329213",
        "top_three_parent_gain_share": "0.877945476095",
    }
    for key, expected_decimal in expected_ratio_decimals.items():
        if ratios[key]["decimal"] != expected_decimal:
            raise AssertionError(f"{key} changed")

    lines = [
        "backbone_anchor_transfer_certificate_v1",
        "scope=certified_baseline_fourth_to_fifth_transition",
        "identity=local_recursive_net=retained_backbone_gain-exit_release",
        "parent_states=12",
        "minimum_anchor_roots=12",
        "minimum_anchors_dropped_no_raw_output=12",
        "surviving_source_types=backbone",
        "expanding_parent_classes=24,48,65,68,77,82",
        "contracting_parent_classes=6,8,12,28,42,93",
        "neutral_parent_classes=none",
        "parent_recursive_mass_decimal=1.536133538213",
        "full_translation_gain_decimal=9.928706884742",
        "minimum_anchor_release_decimal=0.364729899662",
        "retained_survivor_gain_decimal=1.816777911848",
        "exit_release_decimal=1.310139720502",
        "recursive_net_decimal=0.506638191346",
        "full_translation_gain_over_anchor_release_decimal=27.222081035667",
        "retained_gain_over_anchor_release_decimal=4.981159793944",
        "retained_gain_fraction_of_full_translation_decimal=0.182982329213",
        "top_three_parent_gain_share_decimal=0.877945476095",
        f"parent_state_rows_sha256={payload['hashes']['parent_state_rows']}",
        f"anchor_roots_sha256={payload['hashes']['anchor_roots']}",
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
