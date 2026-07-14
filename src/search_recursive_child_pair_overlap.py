#!/usr/bin/env python3
"""Search minimal oriented full-edge recursive children sharing a latent pair.

Enumerate minimal recursive child templates whose root set is one three-term
progression.  Pair templates that share two roots, unite their forced parent
support, and test whether the union remains four-AP-free.  Any surviving union
is a rigorous counterexample to pairwise latent-pair disjointness.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations
import hashlib
import json
import sys

from probe_oriented_full_edge_pair_persistence import oriented_family
from verify_full_edge_coordinated_branching import (
    canonical_hash,
    contains_four_ap,
    three_aps,
    valuation,
)

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

MAX_VALUE = 64
KINDS = (
    "side_first",
    "side_last",
    "middle_right",
    "middle_left",
    "double_first",
    "double_last",
)
RIGHT_TYPES = {"side_first", "middle_right", "double_first"}
LEFT_TYPES = {"side_last", "middle_left", "double_last"}


@dataclass(frozen=True)
class Descriptor:
    kind: str
    reference: int
    roots: tuple[int, int, int]
    color: int | None
    support: tuple[int, ...]

    @property
    def child_key(self) -> tuple[str, int, int | None]:
        return (self.kind, self.reference, self.color)

    def record(self) -> dict[str, object]:
        return {
            "kind": self.kind,
            "reference": self.reference,
            "roots": list(self.roots),
            "color": self.color,
            "support": list(self.support),
            "child_key": list(self.child_key),
        }


def child_color(kind: str, tokens: tuple[int, int, int]) -> int | None:
    parity = tuple(valuation(token, 2) % 2 for token in tokens)
    if kind in {"side_first", "middle_right"} and parity != (0, 0, 0):
        return None
    if kind in {"side_last", "middle_left"} and parity != (1, 1, 1):
        return None
    if kind == "double_first":
        if any(token % 2 for token in tokens):
            return None
        underlying = tuple(token // 2 for token in tokens)
        if tuple(valuation(token, 2) % 2 for token in underlying) != (0, 0, 0):
            return None
        return -1
    if kind == "double_last":
        if any(token % 2 for token in tokens):
            return None
        underlying = tuple(token // 2 for token in tokens)
        if tuple(valuation(token, 2) % 2 for token in underlying) != (1, 1, 1):
            return None
        return -1
    if kind in {"middle_right", "middle_left"}:
        colors = tuple(
            (valuation(token, 2) - valuation(token, 3)) % 3 for token in tokens
        )
        if len(set(colors)) != 1:
            return None
        return colors[0]
    return -1


def forced_support(
    kind: str, reference: int, roots: tuple[int, int, int]
) -> tuple[int, ...] | None:
    if kind in RIGHT_TYPES and not reference < roots[0]:
        return None
    if kind in LEFT_TYPES and not reference > roots[-1]:
        return None
    tokens = tuple(abs(root - reference) for root in roots)
    color = child_color(kind, tokens)
    if color is None:
        return None

    if kind.startswith("side_"):
        completions = tuple(2 * root - reference for root in roots)
    elif kind.startswith("middle_"):
        completions = tuple(2 * reference - root for root in roots)
    elif kind.startswith("double_"):
        if any((reference + root) % 2 for root in roots):
            return None
        completions = tuple((reference + root) // 2 for root in roots)
    else:
        raise AssertionError(kind)

    support = tuple(sorted({reference, *roots, *completions}))
    if support[0] < 0 or support[-1] > MAX_VALUE:
        return None
    if contains_four_ap(set(support)):
        return None
    return support


def enumerate_descriptors() -> list[Descriptor]:
    descriptors: list[Descriptor] = []
    seen = set()
    for left in range(MAX_VALUE + 1):
        for step in range(1, (MAX_VALUE - left) // 2 + 1):
            roots = (left, left + step, left + 2 * step)
            for reference in range(MAX_VALUE + 1):
                for kind in KINDS:
                    support = forced_support(kind, reference, roots)
                    if support is None:
                        continue
                    tokens = tuple(abs(root - reference) for root in roots)
                    raw_color = child_color(kind, tokens)
                    color = raw_color if kind.startswith("middle_") else None
                    descriptor = Descriptor(kind, reference, roots, color, support)
                    identity = (
                        descriptor.child_key,
                        descriptor.roots,
                        descriptor.support,
                    )
                    if identity in seen:
                        continue
                    seen.add(identity)
                    descriptors.append(descriptor)
    return sorted(
        descriptors,
        key=lambda row: (
            row.support[-1] - row.support[0],
            len(row.support),
            row.support,
            row.kind,
            row.reference,
            row.roots,
        ),
    )


def validate_counterexample(
    pair: tuple[int, int], first: Descriptor, second: Descriptor
) -> dict[str, object] | None:
    if first.child_key == second.child_key:
        return None
    support = frozenset(first.support) | frozenset(second.support)
    if contains_four_ap(support):
        return None
    children, roots, references, _occurrences = oriented_family(frozenset(support))
    for descriptor in (first, second):
        key = descriptor.child_key
        if key not in children or key not in roots:
            return None
        if not set(descriptor.roots).issubset(roots[key]):
            return None
        if not three_aps(children[key]):
            return None
        if references[key] != descriptor.reference:
            return None
    if not set(pair).issubset(roots[first.child_key]):
        return None
    if not set(pair).issubset(roots[second.child_key]):
        return None
    return {
        "pair": list(pair),
        "support": sorted(support),
        "support_size": len(support),
        "support_span": max(support) - min(support),
        "first": first.record(),
        "second": second.record(),
        "first_actual_tokens": sorted(children[first.child_key]),
        "second_actual_tokens": sorted(children[second.child_key]),
        "first_actual_roots": sorted(roots[first.child_key]),
        "second_actual_roots": sorted(roots[second.child_key]),
    }


def main() -> int:
    descriptors = enumerate_descriptors()
    by_pair: dict[tuple[int, int], list[Descriptor]] = defaultdict(list)
    kind_counts = Counter(row.kind for row in descriptors)
    for descriptor in descriptors:
        for pair in combinations(descriptor.roots, 2):
            by_pair[pair].append(descriptor)

    tested_pairs = 0
    viable_unions = 0
    best: dict[str, object] | None = None
    all_counterexamples: list[dict[str, object]] = []
    for pair in sorted(by_pair):
        family = by_pair[pair]
        for first, second in combinations(family, 2):
            if first.child_key == second.child_key:
                continue
            tested_pairs += 1
            row = validate_counterexample(pair, first, second)
            if row is None:
                continue
            viable_unions += 1
            all_counterexamples.append(row)
            key = (
                int(row["support_span"]),
                int(row["support_size"]),
                tuple(row["support"]),
                tuple(row["pair"]),
                first.child_key,
                second.child_key,
            )
            if best is None or key < best["_key"]:
                best = {"_key": key, **row}

    if best is not None:
        best.pop("_key", None)
    payload = {
        "schema": "recursive_child_pair_overlap_search_v1",
        "max_value": MAX_VALUE,
        "descriptor_count": len(descriptors),
        "descriptor_kind_counts": dict(sorted(kind_counts.items())),
        "shared_pair_descriptor_pairs_tested": tested_pairs,
        "viable_four_ap_free_overlap_unions": viable_unions,
        "minimum_counterexample": best,
        "counterexample_family_sha256": canonical_hash(
            sorted(
                all_counterexamples,
                key=lambda row: (
                    row["support_span"], row["support_size"], row["support"], row["pair"]
                ),
            )
        ),
        "descriptors_sha256": canonical_hash([row.record() for row in descriptors]),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
