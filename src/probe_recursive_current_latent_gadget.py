#!/usr/bin/env python3
"""Probe a structured policy-compatible recursive current-latent gadget."""
from __future__ import annotations

import hashlib
import json

from search_lexicographic_reserve_pseudoforest_small_box import contains_four_ap
from search_recursive_current_latent_small_box import parent_profile


def main() -> int:
    parent = (
        1,
        33,
        34,
        35,
        49,
        50,
        51,
        55,
        56,
        57,
        61,
        62,
        63,
    )
    if contains_four_ap(parent):
        raise AssertionError("recursive current-latent gadget contains a four-AP")

    profile = parent_profile(parent)
    count = int(profile["recursive_current_latent_resources"])
    if count == 0:
        raise AssertionError("structured gadget did not produce recursive current-latent reuse")

    output = {
        "schema": "recursive_current_latent_gadget_v1",
        "parent": parent,
        "profile": profile,
        "checks": {
            "parent_four_ap_free": True,
            "actual_lexicographic_retained_policy": True,
            "recursive_current_latent_exists": True,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
