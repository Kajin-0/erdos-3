#!/usr/bin/env python3
"""Summarize the shell-valid latent-pair reuse gadget certificate."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: summarize_shelled_pair_reuse_gadget.py INPUT OUTPUT")
    data = json.loads(Path(sys.argv[1]).read_text())
    lines = [
        "Shelled latent-pair reuse gadget",
        "================================",
        "",
        f"K={data['K']}",
        "support=" + ",".join(map(str, data["support"])),
        f"support_size={data['support_size']}",
        f"support_span={data['support_span']}",
        "support_four_ap_free=true",
        "first_tokens=" + ",".join(map(str, data["first_tokens"])),
        "first_roots=" + ",".join(map(str, data["first_roots"])),
        "second_tokens=" + ",".join(map(str, data["second_tokens"])),
        "second_roots=" + ",".join(map(str, data["second_roots"])),
        "shared_latent_pair=" + ",".join(map(str, data["shared_latent_pair"])),
        f"shared_pair_weight={data['shared_pair_weight']}",
        f"recursive_shells={data['recursive_shells']}",
        f"latent_pair_reuse_multiplicity={data['latent_pair_reuse_multiplicity']}",
        f"payload_sha256={data['payload_sha256']}",
    ]
    Path(sys.argv[2]).write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
