#!/usr/bin/env python3
"""Run an exact verifier with repository-wide safe Python limits.

GitHub Actions starts Python with a recursion limit of roughly 1000. Some exact
SCC certificates legitimately traverse graphs with more than 2000 vertices.
The analysis environment used to generate those certificates had a larger
limit, so invoking the scripts directly made CI environment-dependent.
"""
from __future__ import annotations

from pathlib import Path
import runpy
import sys

MIN_RECURSION_LIMIT = 10_000


def main() -> int:
    if len(sys.argv) < 2:
        raise SystemExit("usage: run_exact_python.py SCRIPT [ARGS ...]")

    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    if sys.getrecursionlimit() < MIN_RECURSION_LIMIT:
        sys.setrecursionlimit(MIN_RECURSION_LIMIT)

    target = Path(sys.argv[1]).resolve()
    sys.argv = [str(target), *sys.argv[2:]]
    runpy.run_path(str(target), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
