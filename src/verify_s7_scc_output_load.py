#!/usr/bin/env python3
"""Verify exact output load from the cyclic S7 terminal-fiber component."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import sys
from typing import Iterable

from export_simultaneous_deletion_transition import build_payload
from verify_terminal_fiber_incidence import strongly_connected_components


COMPONENT = (1, 5, 61, 303, 1597, 8195, 323640)

EXPECTED_COUNTS = {
    "internal_terminal": (24, 7),
    "external_terminal": (12, 2),
    "external_imported": (106, 81),
    "external_novel": (7728, 6020),
}

EXPECTED_SOURCE_COUNTS = {
    1: (5, 2, 65, 2843),
    5: (6, 2, 33, 1416),
    61: (4, 2, 1, 1288),
    303: (4, 2, 1, 883),
    1597: (2, 2, 5, 773),
    8195: (1, 2, 1, 524),
    323640: (2, 0, 0, 1),
}

EXPECTED_HASHES = {
    "all_catalog": (
        "d0e2acc7a40d66afa807662945de19e79dae935258a6ecc0c57a7f206ab88957"
    ),
    "internal_terminal_occurrence_catalog": (
        "af7176202999d279d1076c55ad2d5a2657f89941f36b121a3e518ca90b600d94"
    ),
    "external_terminal_occurrence_catalog": (
        "39870613262e12e10ba5a05f8059cce7430776af96360289abe00abb018832b9"
    ),
    "external_imported_occurrence_catalog": (
        "60a3591caf8f438a44a082a9e659b701fd8af199e3beaec9374f90b7432dc607"
    ),
    "external_novel_occurrence_catalog": (
        "4855d98fa68eefaf9a7844ce9ef7175c0c55cc8bffeb3e1a51ca3886cf77c8fc"
    ),
    "external_novel_support": (
        "9bee2e123ff857b8166bb123ac3dff17b6f6201e824596ce02766d439c108197"
    ),
    "external_occurrence_fraction": (
        "e346cf0c346a32d0167d8246ecd9c1862a74e0c72e14d5cbe86f89de761a2fa5"
    ),
    "external_union_fraction": (
        "27505673c5038c153cd06a8ed3cedd426d4e05308e5026399f67f04109db3878"
    ),
    "total_occurrence_ratio": (
        "8695fe5a1fd7863199291146b1e4ddd24d84576d6d460f5cfd4eb25f43e2cfc4"
    ),
    "total_union_ratio": (
        "91b164b45b2ad4e24162b79e996e55167a56eae89df0b9a75a216ac3c0b602be"
    ),
}

CERTIFICATE_SHA256 = (
    "cb5dbba5f45c25b2c286fde17e9895d017abaa906f69f73255a5f0b5b62d081d"
)


def harmonic_mass(values: Iterable[int]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction(0))


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def fraction_hash(value: Fraction) -> str:
    payload = f"{value.numerator}/{value.denominator}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def occurrence_hash(pairs: Iterable[tuple[int, int]]) -> str:
    payload = "\n".join(
        f"{source},{target}" for source, target in sorted(pairs)
    ) + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def support_hash(values: Iterable[int]) -> str:
    payload = ",".join(str(value) for value in sorted(set(values)))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def build_certificate() -> str:
    payload = build_payload(7)
    terminal = set(payload["terminal_outputs"]["steps"])
    backbone = set(payload["backbone"]["values"])

    incidence_edges = {
        (int(step), value)
        for step, fiber in payload["middle_fibers"].items()
        for value in fiber["values"]
        if value in terminal
    }
    cyclic = [
        component
        for component in strongly_connected_components(
            terminal,
            tuple(sorted(incidence_edges)),
        )
        if len(component) > 1
        or (component[0], component[0]) in incidence_edges
    ]
    if cyclic != [COMPONENT]:
        raise AssertionError(f"unexpected cyclic components: {cyclic!r}")

    component = set(COMPONENT)
    categories: dict[str, list[tuple[int, int]]] = {
        name: [] for name in EXPECTED_COUNTS
    }
    source_counts: dict[int, tuple[int, int, int, int]] = {}

    for step in COMPONENT:
        row = {name: 0 for name in categories}
        for value in payload["middle_fibers"][str(step)]["values"]:
            if value in component:
                category = "internal_terminal"
            elif value in terminal:
                category = "external_terminal"
            elif value in backbone:
                category = "external_imported"
            else:
                category = "external_novel"
            categories[category].append((step, value))
            row[category] += 1
        source_counts[step] = tuple(row[name] for name in categories)

    if source_counts != EXPECTED_SOURCE_COUNTS:
        raise AssertionError("source-category count mismatch")

    for name, pairs in categories.items():
        observed = (len(pairs), len({value for _, value in pairs}))
        if observed != EXPECTED_COUNTS[name]:
            raise AssertionError(f"{name} count mismatch: {observed!r}")
        expected_hash = EXPECTED_HASHES[f"{name}_occurrence_catalog"]
        if occurrence_hash(pairs) != expected_hash:
            raise AssertionError(f"{name} occurrence hash mismatch")

    novel_values = [value for _, value in categories["external_novel"]]
    if support_hash(novel_values) != EXPECTED_HASHES["external_novel_support"]:
        raise AssertionError("external-novel support hash mismatch")

    all_records = [
        (name, source, target)
        for name, pairs in categories.items()
        for source, target in pairs
    ]
    all_payload = "\n".join(
        f"{name},{source},{target}"
        for name, source, target in sorted(all_records)
    ) + "\n"
    all_hash = hashlib.sha256(all_payload.encode("utf-8")).hexdigest()
    if all_hash != EXPECTED_HASHES["all_catalog"]:
        raise AssertionError("complete category catalog hash mismatch")

    vertex_mass = harmonic_mass(component)
    internal_occurrence_mass = harmonic_mass(
        value for _, value in categories["internal_terminal"]
    )

    external_pairs = [
        pair
        for name in (
            "external_terminal",
            "external_imported",
            "external_novel",
        )
        for pair in categories[name]
    ]
    external_occurrence_mass = harmonic_mass(
        value for _, value in external_pairs
    )
    external_union_mass = harmonic_mass(
        {value for _, value in external_pairs}
    )

    total_occurrence_mass = internal_occurrence_mass + external_occurrence_mass
    total_union_mass = harmonic_mass(
        {
            value
            for pairs in categories.values()
            for _, value in pairs
        }
    )

    external_occurrence_ratio = (
        external_occurrence_mass / internal_occurrence_mass
    )
    external_union_ratio = external_union_mass / internal_occurrence_mass
    total_occurrence_ratio = total_occurrence_mass / vertex_mass
    total_union_ratio = total_union_mass / vertex_mass

    if fraction_hash(external_occurrence_mass) != EXPECTED_HASHES[
        "external_occurrence_fraction"
    ]:
        raise AssertionError("external occurrence fraction hash mismatch")
    if fraction_hash(external_union_mass) != EXPECTED_HASHES[
        "external_union_fraction"
    ]:
        raise AssertionError("external union fraction hash mismatch")
    if fraction_hash(total_occurrence_ratio) != EXPECTED_HASHES[
        "total_occurrence_ratio"
    ]:
        raise AssertionError("total occurrence ratio hash mismatch")
    if fraction_hash(total_union_ratio) != EXPECTED_HASHES[
        "total_union_ratio"
    ]:
        raise AssertionError("total union ratio hash mismatch")

    if not Fraction(12, 25) < external_occurrence_ratio < Fraction(1, 2):
        raise AssertionError("external occurrence ratio bracket failed")
    if not Fraction(39, 100) < external_union_ratio < Fraction(2, 5):
        raise AssertionError("external union ratio bracket failed")
    if not Fraction(3, 2) < total_occurrence_ratio < Fraction(8, 5):
        raise AssertionError("total occurrence ratio bracket failed")
    if not Fraction(7, 5) < total_union_ratio < Fraction(3, 2):
        raise AssertionError("total union ratio bracket failed")

    if {value for _, value in categories["external_terminal"]} != {
        93476,
        230164,
    }:
        raise AssertionError("external terminal support mismatch")

    lines = [
        "S7 CYCLIC SCC OUTPUT LOAD",
        "",
        "component=1,5,61,303,1597,8195,323640",
        f"component_vertex_mass={fraction_text(vertex_mass)}",
        (
            "internal_target_occurrence_mass="
            f"{fraction_text(internal_occurrence_mass)}"
        ),
    ]

    for name, pairs in categories.items():
        lines.extend(
            [
                f"{name}_occurrences={len(pairs)}",
                f"{name}_distinct_labels={len({value for _, value in pairs})}",
                (
                    f"{name}_occurrence_catalog_sha256="
                    f"{EXPECTED_HASHES[f'{name}_occurrence_catalog']}"
                ),
            ]
        )

    lines.extend(
        [
            "external_terminal_support=93476,230164",
            (
                "external_novel_support_sha256="
                f"{EXPECTED_HASHES['external_novel_support']}"
            ),
            f"all_category_catalog_sha256={all_hash}",
        ]
    )

    for step, counts in source_counts.items():
        lines.append(f"q{step}_counts=" + ",".join(map(str, counts)))

    lines.extend(
        [
            (
                "external_occurrence_fraction_sha256="
                f"{EXPECTED_HASHES['external_occurrence_fraction']}"
            ),
            (
                "external_union_fraction_sha256="
                f"{EXPECTED_HASHES['external_union_fraction']}"
            ),
            "external_occurrence_to_internal_lower=12/25",
            "external_occurrence_to_internal_upper=1/2",
            "external_union_to_internal_lower=39/100",
            "external_union_to_internal_upper=2/5",
            (
                "total_occurrence_ratio_sha256="
                f"{EXPECTED_HASHES['total_occurrence_ratio']}"
            ),
            "total_occurrence_to_vertex_lower=3/2",
            "total_occurrence_to_vertex_upper=8/5",
            (
                "total_union_ratio_sha256="
                f"{EXPECTED_HASHES['total_union_ratio']}"
            ),
            "total_union_to_vertex_lower=7/5",
            "total_union_to_vertex_upper=3/2",
            "",
            (
                "conclusion: out-of-component labels are additional "
                "recursive output, not automatic repayment."
            ),
            (
                "Even after complete numerical deduplication, the fiber "
                "support emitted by the S7 cyclic component"
            ),
            (
                "has more than 7/5 of the component harmonic vertex mass. "
                "A closing potential must convert"
            ),
            (
                "some exported labels into obstruction credit or use "
                "nonlinear/multi-generation amortization."
            ),
            "",
        ]
    )

    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_s7_scc_output_load.py [OUTPUT]")

    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
