#!/usr/bin/env python3
"""Run the canonical CL-089 through CL-100 documentation patch.

This file is intentionally the stable trigger for the documentation workflow.
"""
from __future__ import annotations

from patch_cl097_cl100_scale_transfer import main

if __name__ == "__main__":
    raise SystemExit(main())
