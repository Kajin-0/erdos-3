#!/usr/bin/env python3
"""Certify the exact residual/sponsor backbone split experiment."""
from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import sys

import probe_residual_sponsor_backbone_split as probe

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED_HASHES = {
    "probe": "2991eba73a5d091b6e248060177f17468bcdce405babfb2f3932510664e283e3",
    "split_occurrences": "9b0a8836c6c3984fa0330e8e70d7d88b935a28908578865b5ea508fc2143fa42",
    "split_retained": "53135542c19a4a846b2dd8d9bac57cc7f5c7db0247611a29d46bcc5ae66452e5",
    "baseline_profile": "4cd8cde015ddd06010efc653c5feb4b7c67ceac3e0596bfc01ea2fabda71b1ad",
    "split_profile": "f6881d0fdedad67a86442840df058e01999aaec3b701b235fbd16b21b261c424",
}


def load_probe() -> dict[str, object]:
    buffer = StringIO()
    with redirect_stdout(buffer):
        status = probe.main()
    if status != 0:
        raise AssertionError(f"residual/sponsor probe failed: {status}")
    return json.loads(buffer.getvalue())


def assert_profile(
    name: str,
    profile: dict[str, object],
    expected: dict[str, int | str],
) -> None:
    for key, value in expected.items():
        if key.endswith("_decimal"):
            source = key.removesuffix("_decimal")
            if profile[source]["decimal"] != value:
                raise AssertionError(f"{name} {source} changed")
        elif profile[key] != value:
            raise AssertionError(f"{name} {key} changed")


def build_certificate() -> str:
    payload = load_probe()
    if payload["schema"] != "residual_sponsor_backbone_split_probe_v2":
        raise AssertionError("probe schema changed")
    if payload["probe_payload_sha256"] != EXPECTED_HASHES["probe"]:
        raise AssertionError("probe payload changed")
    for key in (
        "split_occurrences",
        "split_retained",
        "baseline_profile",
        "split_profile",
    ):
        if payload["hashes"][key] != EXPECTED_HASHES[key]:
            raise AssertionError(f"{key} hash changed")

    for flag in (
        "raw_support_union_preserved",
        "raw_point_occurrences_preserved",
        "raw_harmonic_occurrence_mass_preserved",
    ):
        if not payload[flag]:
            raise AssertionError(f"{flag} failed")
    if payload["unshifted_residual_inserted"]:
        raise AssertionError("unshifted residual was inserted")
    if payload["generation_six_propagated"]:
        raise AssertionError("generation six was unexpectedly propagated")
    if payload["raw_support_union_size"] != 1489:
        raise AssertionError("raw support size changed")
    if payload["raw_harmonic_occurrence_mass"]["decimal"] != "25.589294609269":
        raise AssertionError("raw harmonic occurrence mass changed")

    baseline = payload["baseline"]
    split = payload["split"]
    if baseline["raw_occurrences"] != 246:
        raise AssertionError("baseline raw occurrence count changed")
    if split["raw_occurrences"] != 272:
        raise AssertionError("split raw occurrence count changed")
    if baseline["raw_occurrence_points"] != 2972:
        raise AssertionError("baseline raw point count changed")
    if split["raw_occurrence_points"] != 2972:
        raise AssertionError("split raw point count changed")
    if split["raw_source_counts"] != {
        "backbone_residual": 39,
        "backbone_sponsor": 35,
        "middle_fiber": 198,
    }:
        raise AssertionError("split raw source counts changed")
    if split["retained_source_counts"] != {
        "backbone_residual": 15,
        "backbone_sponsor": 18,
        "middle_fiber": 4,
    }:
        raise AssertionError("split retained source counts changed")
    if split["retained_residual_backbone_states"] != 15:
        raise AssertionError("retained residual-backbone state count changed")
    if split["retained_residual_backbone_points"] != 211:
        raise AssertionError("retained residual-backbone point count changed")
    if split["retained_residual_backbone_mass"]["decimal"] != "1.928005934870":
        raise AssertionError("retained residual-backbone mass changed")

    assert_profile(
        "baseline",
        baseline["profile"],
        {
            "states": 21,
            "points": 1032,
            "terminal_states": 8,
            "terminal_points": 17,
            "recursive_states": 13,
            "recursive_points": 1015,
            "latent_resource_occurrences": 106381,
            "total_distinct_resources": 107413,
            "maximum_resource_multiplicity": 1,
            "repeated_resource_tokens": 0,
            "terminal_mass_decimal": "2.043863226048",
            "recursive_mass_decimal": "2.042771729559",
            "total_mass_decimal": "4.086634955606",
            "union_resource_mass_decimal": "1586.466623468978",
            "occurrence_resource_mass_decimal": "1586.466623468978",
            "repeated_resource_mass_decimal": "0.000000000000",
        },
    )
    assert_profile(
        "split",
        split["profile"],
        {
            "states": 37,
            "points": 1096,
            "terminal_states": 22,
            "terminal_points": 232,
            "recursive_states": 15,
            "recursive_points": 864,
            "latent_resource_occurrences": 74191,
            "total_distinct_resources": 75284,
            "maximum_resource_multiplicity": 2,
            "repeated_resource_tokens": 3,
            "terminal_mass_decimal": "2.413546690714",
            "recursive_mass_decimal": "1.873962098445",
            "total_mass_decimal": "4.287508789158",
            "union_resource_mass_decimal": "1181.930568734065",
            "occurrence_resource_mass_decimal": "1181.950486350234",
            "repeated_resource_mass_decimal": "0.019917616169",
        },
    )

    comparison = payload["comparison"]
    expected_comparison = {
        "total_mass_delta": "0.200873833552",
        "terminal_mass_delta": "0.369683464666",
        "recursive_mass_delta": "-0.168809631114",
        "recursive_points_delta": -151,
        "latent_occurrences_delta": -32190,
        "union_resource_mass_delta": "-404.536054734914",
        "occurrence_resource_mass_delta": "-404.516137118744",
    }
    for key, expected in expected_comparison.items():
        actual = comparison[key]
        if isinstance(actual, dict):
            actual = actual["decimal"]
        if actual != expected:
            raise AssertionError(f"comparison {key} changed")

    lines = [
        "residual_sponsor_backbone_split_certificate_v1",
        "scope=certified_R4_recursive_to_complete_F5_retained_transition",
        "generation_six_propagated=false",
        "unshifted_residual_inserted=false",
        "raw_support_union_preserved=true",
        "raw_point_occurrences_preserved=true",
        "raw_harmonic_occurrence_mass_preserved=true",
        "raw_support_union_size=1489",
        "raw_occurrence_points=2972",
        "raw_harmonic_occurrence_mass_decimal=25.589294609269",
        "baseline_retained_states=21",
        "baseline_recursive_points=1015",
        "baseline_recursive_mass_decimal=2.042771729559",
        "baseline_latent_pair_occurrences=106381",
        "baseline_union_resource_mass_decimal=1586.466623468978",
        "split_retained_states=37",
        "split_terminal_points=232",
        "split_recursive_points=864",
        "split_recursive_mass_decimal=1.873962098445",
        "split_latent_pair_occurrences=74191",
        "split_union_resource_mass_decimal=1181.930568734065",
        "recursive_points_delta=-151",
        "recursive_mass_delta_decimal=-0.168809631114",
        "latent_pair_occurrences_delta=-32190",
        "union_resource_mass_delta_decimal=-404.536054734914",
        f"split_occurrences_sha256={EXPECTED_HASHES['split_occurrences']}",
        f"split_retained_sha256={EXPECTED_HASHES['split_retained']}",
        f"probe_payload_sha256={EXPECTED_HASHES['probe']}",
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
