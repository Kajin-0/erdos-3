#!/usr/bin/env python3
"""Run the canonical CL-089 through CL-100 documentation patch safely."""
from __future__ import annotations

from run_cl089_cl092_frontier_patch import install_runtime_fixes

install_runtime_fixes()

from patch_cl097_cl100_scale_transfer import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
