#!/usr/bin/env python3
"""Verify terminal-to-fiber incidence graphs through S7.

There is a directed edge q -> u when q and u are both terminal step labels and
u belongs to the middle fiber Xi_q. Strongly connected components detect
mutually recursive terminal labels that cannot be ordered by a strict
decreasing rank.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import hashlib
import sys

from export_simultaneous_deletion_transition import build_payload


EXPECTED = {
    1: (
        2, 1, 2, 1, (),
        "b05c4979e7b9347880bd9aa4a0587d968a3bec450490971d2ad13c319882a3cb",
    ),
    2: (
        5, 3, 5, 1, (),
        "6bbb44826bc5397d4df77158553be9151c231836c5dcea404918974b2a7d4cdc",
    ),
    3: (
        10, 10, 9, 2, ((61, 303),),
        "199ebc3e1857109ecee552c1317ebd76eff328fdb8c1806f32c55e3d47f4eead",
    ),
    4: (
        11, 20, 10, 2, ((61, 303),),
        "7587b87f3d5f0210cc8fc9d0e1a917c2508293461d44eaa2ad1c4c925879547e",
    ),
    5: (
        12, 31, 11, 2, ((61, 303),),
        "ba09e6ed05f256142a7a1f3ea7f90cde645c0c7765372ec965c083a5622a1dfb",
    ),
    6: (
        13, 43, 12, 2, ((61, 303),),
        "54fdd9ba95e5e4f86eb10ef54030dda46dd138059ea5489cb6e27be74d8f0b6f",
    ),
    7: (
        25,
        75,
        19,
        7,
        ((1, 5, 61, 303, 1597, 8195, 323640),),
        "17ef6a4af54dfba4b3d97c305aeb705b20b5c9cda61a0f2d0b4de9920f052f78",
    ),
}

CERTIFICATE_SHA256 = (
    "ddedf75bd52a6cc67cef6ecb0a635b836e9a1c7c5094a860449dd35dd2651c18"
)


def strongly_connected_components(
    nodes: set[int],
    edges: tuple[tuple[int, int], ...],
) -> tuple[tuple[int, ...], ...]:
    graph: dict[int, list[int]] = defaultdict(list)
    for source, target in edges:
        graph[source].append(target)

    index = 0
    stack: list[int] = []
    on_stack: set[int] = set()
    first_index: dict[int, int] = {}
    low_link: dict[int, int] = {}
    result: list[tuple[int, ...]] = []

    def visit(vertex: int) -> None:
        nonlocal index
        first_index[vertex] = index
        low_link[vertex] = index
        index += 1
        stack.append(vertex)
        on_stack.add(vertex)

        for target in sorted(graph[vertex]):
            if target not in first_index:
                visit(target)
                low_link[vertex] = min(
                    low_link[vertex],
                    low_link[target],
                )
            elif target in on_stack:
                low_link[vertex] = min(
                    low_link[vertex],
                    first_index[target],
                )

        if low_link[vertex] == first_index[vertex]:
            component: list[int] = []
            while True:
                target = stack.pop()
                on_stack.remove(target)
                component.append(target)
                if target == vertex:
                    break
            result.append(tuple(sorted(component)))

    for vertex in sorted(nodes):
        if vertex not in first_index:
            visit(vertex)

    return tuple(
        sorted(result, key=lambda component: (
            component[0],
            len(component),
            component,
        ))
    )


def graph_metrics(depth: int) -> tuple[
    int,
    int,
    int,
    int,
    tuple[tuple[int, ...], ...],
    str,
]:
    payload = build_payload(depth)
    nodes = set(payload["terminal_outputs"]["steps"])
    edges: set[tuple[int, int]] = set()

    for step_text, fiber in payload["middle_fibers"].items():
        step = int(step_text)
        for value in fiber["values"]:
            if value in nodes:
                edges.add((step, value))

    ordered_edges = tuple(sorted(edges))
    components = strongly_connected_components(nodes, ordered_edges)
    cyclic = tuple(
        component
        for component in components
        if len(component) > 1
        or (component[0], component[0]) in edges
    )

    canonical = (
        "nodes="
        + ",".join(str(value) for value in sorted(nodes))
        + "\n"
        + "\n".join(
            f"{source}->{target}"
            for source, target in ordered_edges
        )
        + "\n"
    )
    graph_hash = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()

    return (
        len(nodes),
        len(ordered_edges),
        len(components),
        max(len(component) for component in components),
        cyclic,
        graph_hash,
    )


def build_certificate() -> str:
    lines = [
        "TERMINAL-FIBER INCIDENCE GRAPH",
        "",
        "edge=q->u iff u is terminal and u in Xi_q",
        "verified_depths=1,2,3,4,5,6,7",
    ]

    for depth in range(1, 8):
        actual = graph_metrics(depth)
        expected = EXPECTED[depth]
        if actual != expected:
            raise AssertionError(
                f"S{depth}: graph mismatch: {actual!r} != {expected!r}"
            )

        cyclic_text = (
            ";".join(
                ",".join(str(value) for value in component)
                for component in actual[4]
            )
            or "none"
        )
        lines.extend(
            [
                f"S{depth}_nodes={actual[0]}",
                f"S{depth}_edges={actual[1]}",
                f"S{depth}_scc_count={actual[2]}",
                f"S{depth}_largest_scc={actual[3]}",
                f"S{depth}_cyclic_components={cyclic_text}",
                f"S{depth}_graph_sha256={actual[5]}",
            ]
        )

    lines.extend(
        [
            "",
            (
                "conclusion: the terminal-fiber incidence graph is not "
                "acyclic."
            ),
            (
                "A 2-cycle {61,303} appears at S3 and persists through S6;"
            ),
            (
                "at S7 it expands into a 7-label strongly connected "
                "component."
            ),
            (
                "Any retention potential based on a strict decreasing "
                "order of terminal labels"
            ),
            (
                "is therefore invalid on the recorded lexicographic "
                "genealogy."
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
            "usage: verify_terminal_fiber_incidence.py [OUTPUT]"
        )
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
