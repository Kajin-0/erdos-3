#!/usr/bin/env python3
"""Export the SCC quotient of the terminal-to-fiber incidence graph."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

from export_simultaneous_deletion_transition import build_payload
from verify_terminal_fiber_incidence import strongly_connected_components


EXPECTED = {
    1: (
        "c8f9afb431e903b54c3e41fc6795fe7334e448dbe4b5b8975bb6a1c14c135b69",
        2,
        1,
        0,
        0,
        "0",
    ),
    2: (
        "e81ffd1df5bec410d3e3dd96e84c136792313bbb4c42a89a1488b3bcc3c05f4f",
        5,
        3,
        0,
        0,
        "0",
    ),
    3: (
        "2d6b760230cac0e79c9212c510b1114e5504ab1805432b5210abce342c4aa28f",
        9,
        6,
        1,
        2,
        "0",
    ),
    4: (
        "818f65fa27fd60809d6181bb5b1de7dc7873fee09d02cb8b489232c9b792245b",
        10,
        15,
        1,
        2,
        "0",
    ),
    5: (
        "5cdc05d87dd4fe9d0717012288a7d5859bda9273d51dc691758349c87f23a58c",
        11,
        25,
        1,
        2,
        "0",
    ),
    6: (
        "9738e822444c9776c36523d8bced55ca677eeeb5635a0520eacb069f08f111d3",
        12,
        36,
        1,
        2,
        "0",
    ),
    7: (
        "0249bce4a12db2e2faa40873d25cce9741fba7c5f2a2c94f16b42b1873bc7804",
        19,
        26,
        1,
        24,
        "43727503229099/1043823972523464",
    ),
}

CERTIFICATE_SHA256 = (
    "3166cbb0801eb774e8b6691ace6a8612f5457a9415bd8ae3762a1260216d0fe2"
)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def build_quotient(depth: int) -> dict[str, object]:
    payload = build_payload(depth)
    nodes = set(payload["terminal_outputs"]["steps"])
    edges: set[tuple[int, int]] = set()

    for step_text, fiber in payload["middle_fibers"].items():
        step = int(step_text)
        for value in fiber["values"]:
            if value in nodes:
                edges.add((step, value))

    ordered_edges = tuple(sorted(edges))
    strongly_connected = strongly_connected_components(
        nodes,
        ordered_edges,
    )
    component_of = {
        value: index
        for index, component in enumerate(strongly_connected)
        for value in component
    }

    records: list[dict[str, object]] = []
    for index, component in enumerate(strongly_connected):
        member_set = set(component)
        internal_edges = tuple(
            sorted(
                (source, target)
                for source, target in ordered_edges
                if source in member_set and target in member_set
            )
        )
        incoming = tuple(
            sorted(
                {
                    component_of[source]
                    for source, target in ordered_edges
                    if target in member_set and source not in member_set
                }
            )
        )
        outgoing = tuple(
            sorted(
                {
                    component_of[target]
                    for source, target in ordered_edges
                    if source in member_set and target not in member_set
                }
            )
        )

        vertex_mass = sum(
            (Fraction(1, value) for value in member_set),
            Fraction(0),
        )
        internal_target_mass = sum(
            (Fraction(1, target) for _source, target in internal_edges),
            Fraction(0),
        )

        records.append(
            {
                "id": index,
                "members": list(component),
                "cyclic": bool(
                    len(component) > 1
                    or (component[0], component[0]) in edges
                ),
                "internal_edges": [list(edge) for edge in internal_edges],
                "incoming_components": list(incoming),
                "outgoing_components": list(outgoing),
                "vertex_harmonic_mass": fraction_text(vertex_mass),
                "internal_target_mass": fraction_text(
                    internal_target_mass
                ),
                "recycling_excess": fraction_text(
                    internal_target_mass - vertex_mass
                ),
            }
        )

    condensation_edges = tuple(
        sorted(
            {
                (component_of[source], component_of[target])
                for source, target in ordered_edges
                if component_of[source] != component_of[target]
            }
        )
    )

    return {
        "schema": "terminal_fiber_scc_quotient/v1",
        "depth": depth,
        "edge_semantics": "q_to_u_when_u_is_terminal_and_u_in_Xi_q",
        "components": records,
        "condensation_edges": [list(edge) for edge in condensation_edges],
    }


def serialize(payload: dict[str, object]) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"


def payload_digest(payload: dict[str, object]) -> str:
    return hashlib.sha256(serialize(payload).encode("utf-8")).hexdigest()


def build_certificate() -> str:
    lines = [
        "TERMINAL-FIBER SCC QUOTIENT",
        "",
        "schema=terminal_fiber_scc_quotient/v1",
        "verified_depths=1,2,3,4,5,6,7",
    ]

    for depth in range(1, 8):
        payload = build_quotient(depth)
        cyclic = [
            component
            for component in payload["components"]
            if component["cyclic"]
        ]
        internal_edge_count = sum(
            len(component["internal_edges"])
            for component in cyclic
        )
        recycling_excess = sum(
            (
                Fraction(component["recycling_excess"])
                for component in cyclic
            ),
            Fraction(0),
        )

        actual = (
            payload_digest(payload),
            len(payload["components"]),
            len(payload["condensation_edges"]),
            len(cyclic),
            internal_edge_count,
            fraction_text(recycling_excess),
        )
        if actual != EXPECTED[depth]:
            raise AssertionError(
                f"S{depth} quotient mismatch: "
                f"{actual!r} != {EXPECTED[depth]!r}"
            )

        members = (
            ";".join(
                ",".join(str(value) for value in component["members"])
                for component in cyclic
            )
            or "none"
        )
        lines.extend(
            [
                f"S{depth}_components={actual[1]}",
                f"S{depth}_condensation_edges={actual[2]}",
                f"S{depth}_cyclic_components={actual[3]}",
                f"S{depth}_cyclic_members={members}",
                f"S{depth}_internal_cyclic_edges={actual[4]}",
                f"S{depth}_recycling_excess={actual[5]}",
                f"S{depth}_quotient_sha256={actual[0]}",
            ]
        )

    recycling_ratio = Fraction(
        6_588_286_581_562_338,
        6_369_649_065_416_843,
    )
    lines.extend(
        [
            "",
            (
                "S7_internal_target_to_vertex_capacity="
                + fraction_text(recycling_ratio)
            ),
            (
                "conclusion: SCC condensation removes label-level cycles "
                "but not internal recycling."
            ),
            (
                "The unit harmonic capacity is exactly balanced on the "
                "{61,303} cycle through S6"
            ),
            (
                "and fails at S7 by positive recycling excess "
                "43727503229099/1043823972523464."
            ),
            (
                "A valid SCC state therefore needs internal capacity or "
                "obstruction export, not only vertex mass."
            ),
            "",
        ]
    )

    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(
            f"certificate SHA-256 mismatch: {digest}"
        )
    return certificate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    test_parser = subparsers.add_parser("self-test")
    test_parser.add_argument("output", nargs="?", type=Path)

    export_parser = subparsers.add_parser("export")
    export_parser.add_argument("--state-depth", type=int, required=True)
    export_parser.add_argument("--output", type=Path)

    args = parser.parse_args()
    if args.command == "self-test":
        certificate = build_certificate()
        if args.output is not None:
            args.output.write_text(certificate, encoding="utf-8")
        print(certificate, end="")
        return 0

    serialized = serialize(build_quotient(args.state_depth))
    if args.output is None:
        sys.stdout.write(serialized)
    else:
        args.output.write_text(serialized, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
