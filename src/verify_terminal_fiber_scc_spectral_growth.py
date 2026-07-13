#!/usr/bin/env python3
"""Verify exact spectral-growth bounds for cyclic terminal-fiber SCCs."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from export_simultaneous_deletion_transition import build_payload
from verify_terminal_fiber_incidence import strongly_connected_components


EXPECTED_SWAP_HASH = (
    "9d03a684ed88bcdd992e6dbe02b7fa54d25dc9441096f3ac3988f03f38f19700"
)
EXPECTED_S7_HASH = (
    "41d9402acc277af39e3dcd83b91d043d2bef565698fd84ec8d75fa670dc49407"
)
CERTIFICATE_SHA256 = (
    "aa753127d2d0adbcb124b0a9f6e5c053350d422cd66fe2a4c73d1045b2917bf4"
)

WITNESS = (43, 59, 31, 31, 14, 10, 26)
EXPECTED_AW = (112, 155, 81, 81, 36, 26, 69)
EXPECTED_LOWER_RESIDUAL = (19, 38, 16, 16, 2, 4, 23)
EXPECTED_UPPER_RESIDUAL = (8, 7, 5, 5, 4, 2, 1)


def cyclic_matrix(
    depth: int,
) -> tuple[tuple[int, ...], tuple[tuple[int, ...], ...], str]:
    payload = build_payload(depth)
    nodes = set(payload["terminal_outputs"]["steps"])
    edges: set[tuple[int, int]] = set()

    for step_text, fiber in payload["middle_fibers"].items():
        step = int(step_text)
        for value in fiber["values"]:
            if value in nodes:
                edges.add((step, value))

    ordered_edges = tuple(sorted(edges))
    cyclic = tuple(
        component
        for component in strongly_connected_components(
            nodes,
            ordered_edges,
        )
        if len(component) > 1
        or (component[0], component[0]) in edges
    )
    if len(cyclic) != 1:
        raise AssertionError(
            f"S{depth}: expected one cyclic component, got {cyclic!r}"
        )

    members = cyclic[0]
    adjacency = tuple(
        tuple(
            1 if (source, target) in edges else 0
            for target in members
        )
        for source in members
    )
    record = {
        "members": list(members),
        "adjacency": [list(row) for row in adjacency],
    }
    canonical = json.dumps(
        record,
        sort_keys=True,
        separators=(",", ":"),
    ) + "\n"
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return members, adjacency, digest


def matrix_vector(
    matrix: tuple[tuple[int, ...], ...],
    vector: tuple[int, ...],
) -> tuple[int, ...]:
    return tuple(
        sum(coefficient * value for coefficient, value in zip(row, vector))
        for row in matrix
    )


def matrix_product(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    size = len(left)
    return tuple(
        tuple(
            sum(left[row][index] * right[index][column] for index in range(size))
            for column in range(size)
        )
        for row in range(size)
    )


def identity(size: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(1 if row == column else 0 for column in range(size))
        for row in range(size)
    )


def build_certificate() -> str:
    lines = [
        "TERMINAL-FIBER SCC SPECTRAL GROWTH",
        "",
        "theorem=Collatz-Wielandt exact rational bracket",
    ]

    for depth in range(3, 7):
        members, adjacency, digest = cyclic_matrix(depth)
        if members != (61, 303):
            raise AssertionError(f"S{depth}: unexpected members")
        if digest != EXPECTED_SWAP_HASH:
            raise AssertionError(f"S{depth}: adjacency hash mismatch")
        if matrix_product(adjacency, adjacency) != identity(2):
            raise AssertionError(f"S{depth}: A^2 is not the identity")

        lines.extend(
            [
                f"S{depth}_members=61,303",
                f"S{depth}_adjacency_sha256={digest}",
                f"S{depth}_A_squared_identity=true",
                f"S{depth}_spectral_radius=1",
            ]
        )

    members, adjacency, digest = cyclic_matrix(7)
    if members != (1, 5, 61, 303, 1597, 8195, 323640):
        raise AssertionError("S7: unexpected cyclic members")
    if digest != EXPECTED_S7_HASH:
        raise AssertionError("S7: adjacency hash mismatch")

    image = matrix_vector(adjacency, WITNESS)
    lower_residual = tuple(
        9 * image_value - 23 * witness_value
        for image_value, witness_value in zip(image, WITNESS)
    )
    upper_residual = tuple(
        8 * witness_value - 3 * image_value
        for image_value, witness_value in zip(image, WITNESS)
    )

    if image != EXPECTED_AW:
        raise AssertionError("S7: matrix-vector image mismatch")
    if lower_residual != EXPECTED_LOWER_RESIDUAL:
        raise AssertionError("S7: lower residual mismatch")
    if upper_residual != EXPECTED_UPPER_RESIDUAL:
        raise AssertionError("S7: upper residual mismatch")
    if not all(value > 0 for value in lower_residual + upper_residual):
        raise AssertionError("S7: spectral bracket is not strict")

    lines.extend(
        [
            "",
            "S7_members=1,5,61,303,1597,8195,323640",
            f"S7_adjacency_sha256={digest}",
            "S7_w=" + ",".join(str(value) for value in WITNESS),
            "S7_Aw=" + ",".join(str(value) for value in image),
            (
                "S7_9Aw_minus_23w="
                + ",".join(str(value) for value in lower_residual)
            ),
            (
                "S7_8w_minus_3Aw="
                + ",".join(str(value) for value in upper_residual)
            ),
            "S7_spectral_radius_lower=23/9",
            "S7_spectral_radius_upper=8/3",
            (
                "conclusion: every positive linear internal capacity has "
                "expansion factor at least 23/9 on the S7 cyclic component."
            ),
            (
                "In particular, no such capacity is nonexpanding or "
                "factor-two contractive without external obstruction export."
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
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: verify_terminal_fiber_scc_spectral_growth.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
