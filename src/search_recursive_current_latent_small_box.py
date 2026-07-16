#!/usr/bin/env python3
"""Search actual retained quotients for a recursive current-latent owner pair."""
from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys

from search_lexicographic_reserve_pseudoforest_small_box import (
    contains_four_ap,
    ordered_pair,
    retained_family,
)
from verify_retained_terminal_split import contains_three_term_ap


def parent_profile(parent: tuple[int, ...]) -> dict[str, object]:
    retained = retained_family(parent)
    owners: dict[tuple[int, int], list[dict[str, object]]] = defaultdict(list)
    states: list[dict[str, object]] = []

    for state in retained:
        values = tuple(int(value) for value in state.values)
        roots = tuple(int(root) for root in state.representative.provenance)
        references = {root - value for value, root in zip(values, roots, strict=True)}
        if len(references) != 1:
            raise AssertionError("recursive-current search child is not affine")
        reference = references.pop()
        terminal = not contains_three_term_ap(values)
        states.append({
            "state_index": int(state.index),
            "source": str(state.representative.source),
            "source_step": state.representative.source_step,
            "reference": reference,
            "terminal": terminal,
            "values": values,
            "roots": roots,
        })
        for root in roots:
            owners[ordered_pair(reference, root)].append({
                "kind": "current", "state_index": int(state.index),
                "source": str(state.representative.source),
                "reference": reference, "terminal": terminal,
            })
        if terminal:
            continue
        for left, right in combinations(roots, 2):
            owners[ordered_pair(left, right)].append({
                "kind": "latent", "state_index": int(state.index),
                "source": str(state.representative.source),
                "reference": reference, "terminal": False,
            })

    current_latent: list[dict[str, object]] = []
    recursive_current_latent: list[dict[str, object]] = []
    for resource, rows in sorted(owners.items()):
        current = [row for row in rows if row["kind"] == "current"]
        latent = [row for row in rows if row["kind"] == "latent"]
        if current and latent:
            row = {"resource": resource, "current": current, "latent": latent}
            current_latent.append(row)
            if any(not bool(owner["terminal"]) for owner in current):
                recursive_current_latent.append(row)

    return {
        "retained_states": len(retained),
        "current_latent_resources": len(current_latent),
        "recursive_current_latent_resources": len(recursive_current_latent),
        "states": states,
        "current_latent_rows": current_latent,
        "recursive_current_latent_rows": recursive_current_latent,
    }


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: search_recursive_current_latent_small_box.py ENDPOINT OUTPUT")
    endpoint = int(sys.argv[1])
    if endpoint < 4 or endpoint > 22:
        raise SystemExit("endpoint must lie in [4,22]")

    values = tuple(range(1, endpoint + 1))
    parents_checked = 0
    parents_with_current_latent = 0
    current_latent_resources = 0
    witness = None

    for mask in range(1 << endpoint):
        parent = tuple(value for index, value in enumerate(values) if mask & (1 << index))
        if len(parent) < 3 or contains_four_ap(parent):
            continue
        parents_checked += 1
        profile = parent_profile(parent)
        count = int(profile["current_latent_resources"])
        if count:
            parents_with_current_latent += 1
            current_latent_resources += count
        if int(profile["recursive_current_latent_resources"]):
            witness = {"parent": parent, "profile": profile}
            break

    output = {
        "schema": "recursive_current_latent_small_box_v1",
        "endpoint": endpoint,
        "counts": {
            "parents_checked": parents_checked,
            "parents_with_current_latent": parents_with_current_latent,
            "current_latent_resources": current_latent_resources,
        },
        "first_recursive_current_latent_witness": witness,
        "checks": {
            "actual_lexicographic_retained_policy": True,
            "recursive_current_latent_absent": witness is None,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    Path(sys.argv[2]).write_text(json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0 if witness is None else 2


if __name__ == "__main__":
    raise SystemExit(main())
