#!/usr/bin/env python3
"""Certify the fourth-to-fifth root-lineage transfer identity exactly."""
from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import sys

import probe_fourth_to_fifth_root_transfer as probe

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED = {
    "probe_payload_sha256": "08c8f9cdf6e5d044da2d67fbe5c508f6b9ca1c46f3fa62894130188b1321d3c9",
    "surviving_recursive_roots": 1015,
    "exiting_recursive_roots": 702,
    "exiting_to_terminal_roots": 17,
    "exiting_dropped_roots": 685,
    "split_recursive_and_terminal_roots": 0,
    "fifth_all_repeated_root_labels": 0,
    "survivor_scale_gain_sha256": "1d62e1e6da7ee7ad6b3520febd71f52b31e98681f88125c2b1c4daaded0bcffc",
    "exiting_parent_release_sha256": "c353514da2336b2f62fa111690f4f4d424e7dcc152ec55539b137845a14212b3",
    "recursive_delta_sha256": "469eb05f73ca7e4c903eb3ee96a978993d4828bd86d7dc0b33200368916ab880",
    "gain_release_ratio_sha256": "0959127f1407bfba2d780f67713af93d1501a671f8bf25eaeb7058f1cd6b823a",
}


def load_probe() -> dict[str, object]:
    buffer = StringIO()
    with redirect_stdout(buffer):
        status = probe.main()
    if status != 0:
        raise AssertionError(f"root-transfer probe failed: {status}")
    return json.loads(buffer.getvalue())


def build_certificate() -> str:
    payload = load_probe()
    if payload["probe_payload_sha256"] != EXPECTED["probe_payload_sha256"]:
        raise AssertionError("probe payload changed")
    if not payload["identity"]["verified"]:
        raise AssertionError("root-transfer identity failed")
    counts = payload["counts"]
    for key in (
        "surviving_recursive_roots",
        "exiting_recursive_roots",
        "exiting_to_terminal_roots",
        "exiting_dropped_roots",
        "split_recursive_and_terminal_roots",
        "fifth_all_repeated_root_labels",
    ):
        if counts[key] != EXPECTED[key]:
            raise AssertionError(f"{key} changed: {counts[key]}")
    hashes = payload["mass_hashes"]
    if hashes["survivor_scale_gain"] != EXPECTED["survivor_scale_gain_sha256"]:
        raise AssertionError("survivor scale gain changed")
    if hashes["exiting_parent_release"] != EXPECTED["exiting_parent_release_sha256"]:
        raise AssertionError("exit release changed")
    if hashes["recursive_delta"] != EXPECTED["recursive_delta_sha256"]:
        raise AssertionError("recursive delta changed")
    ratio = payload["ratios"]["survivor_gain_over_exit_release"]
    if ratio["sha256"] != EXPECTED["gain_release_ratio_sha256"]:
        raise AssertionError("gain/release ratio changed")

    lines = [
        "fourth_to_fifth_root_transfer_certificate_v1",
        "scope=certified_baseline_fourth_to_fifth_recursive_transition",
        "identity=H5_recursive-H4_recursive=survivor_scale_gain-exiting_parent_release",
        "identity_verified=true",
        f"fourth_recursive_roots={counts['fourth_recursive_roots']}",
        f"surviving_recursive_roots={counts['surviving_recursive_roots']}",
        f"exiting_recursive_roots={counts['exiting_recursive_roots']}",
        f"exiting_to_terminal_roots={counts['exiting_to_terminal_roots']}",
        f"exiting_dropped_roots={counts['exiting_dropped_roots']}",
        f"split_recursive_and_terminal_roots={counts['split_recursive_and_terminal_roots']}",
        f"fifth_all_repeated_root_labels={counts['fifth_all_repeated_root_labels']}",
        f"fifth_all_max_root_multiplicity={counts['fifth_all_max_root_multiplicity']}",
        f"survivor_scale_gain_decimal={payload['mass_decimals']['survivor_scale_gain']}",
        f"survivor_scale_gain_sha256={hashes['survivor_scale_gain']}",
        f"exiting_parent_release_decimal={payload['mass_decimals']['exiting_parent_release']}",
        f"exiting_parent_release_sha256={hashes['exiting_parent_release']}",
        f"terminal_exit_parent_release_decimal={payload['mass_decimals']['terminal_exit_parent_release']}",
        f"dropped_exit_parent_release_decimal={payload['mass_decimals']['dropped_exit_parent_release']}",
        f"recursive_delta_decimal={payload['mass_decimals']['recursive_delta']}",
        f"recursive_delta_sha256={hashes['recursive_delta']}",
        "gain_release_ratio_lower=277341/200000",
        "gain_release_ratio_upper=693353/500000",
        f"gain_release_ratio_decimal={ratio['decimal']}",
        f"gain_release_ratio_sha256={ratio['sha256']}",
        f"terminal_mass_from_exiting_roots_decimal={payload['mass_decimals']['terminal_mass_from_exiting_roots']}",
        f"terminal_mass_from_split_roots_decimal={payload['mass_decimals']['terminal_mass_from_split_roots']}",
        f"surviving_root_rows_sha256={payload['hashes']['surviving_root_rows']}",
        f"exiting_roots_sha256={payload['hashes']['exiting_roots']}",
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
