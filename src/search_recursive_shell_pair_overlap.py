#!/usr/bin/env python3
"""Targeted pair-overlap search with mandatory dyadic shelling.

A recursive child witness must lie in one standard dyadic shell.  Reuse the
minimal three-root template search, reject descriptors whose three current
tokens cross a dyadic boundary, and extend the coordinate box to [0,128].
"""
from __future__ import annotations

import search_recursive_child_pair_overlap as search

search.MAX_VALUE = 128
_original_forced_support = search.forced_support


def shelled_forced_support(
    kind: str, reference: int, roots: tuple[int, int, int]
) -> tuple[int, ...] | None:
    tokens = tuple(abs(root - reference) for root in roots)
    if not tokens or len({token.bit_length() - 1 for token in tokens}) != 1:
        return None
    return _original_forced_support(kind, reference, roots)


search.forced_support = shelled_forced_support

if __name__ == "__main__":
    raise SystemExit(search.main())
