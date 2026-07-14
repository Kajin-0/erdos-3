#!/usr/bin/env python3
"""Run the oriented full-edge persistence probe through [1,18]."""
from __future__ import annotations

import probe_oriented_full_edge_pair_persistence as probe

probe.LIMIT = 18

if __name__ == "__main__":
    raise SystemExit(probe.main())
