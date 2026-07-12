#!/usr/bin/env python3
"""Verify the finite arithmetic certificate for the exact-tail basin fan at S_10."""
from __future__ import annotations

import hashlib
from collections import Counter

L8 = 8_388_608
L9 = 67_108_864
L10 = 536_870_912
S8_COMPLETION_MAX = 17_038_008

D_MIN = S8_COMPLETION_MAX - 2 * L8 + 1
K_MIN = D_MIN + 6
K_MAX = L8 // 8 + 3
EXPECTED_COUNT = 525_189
EXPECTED_SHA256 = "99eb9011d140b420ddf4bd2bf33b6d98d9381b36e12089e231eda8323c548e60"
EXPECTED_CLASSES = {
    0: 393_891,
    2: 98_472,
    4: 24_618,
    6: 6_155,
    8: 1_539,
    10: 385,
    12: 96,
    14: 24,
    16: 6,
    18: 2,
    20: 1,
}


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def main() -> None:
    if D_MIN != 260_793 or K_MIN != 260_799 or K_MAX != 1_048_579:
        raise AssertionError("unexpected basin interval")

    offsets = [
        k
        for k in range(K_MIN, K_MAX + 1)
        if v2(k) % 2 == 0
    ]
    if len(offsets) != EXPECTED_COUNT:
        raise AssertionError("basin offset count mismatch")
    if offsets[0] != K_MIN or offsets[-1] != K_MAX:
        raise AssertionError("basin endpoint mismatch")

    classes = Counter(v2(k) for k in offsets)
    if dict(classes) != EXPECTED_CLASSES:
        raise AssertionError(f"two-adic class mismatch: {classes}")

    payload = ",".join(str(value) for value in offsets)
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    if digest != EXPECTED_SHA256:
        raise AssertionError("basin offset hash mismatch")

    for k in offsets:
        d = k - 6
        if not (2 * L8 + d > S8_COMPLETION_MAX):
            raise AssertionError("seed completion was not excluded")
        if not (0 < k <= L9 // 8):
            raise AssertionError("first descent range failed")
        if not (0 < k - 3 <= L8 // 8):
            raise AssertionError("second descent range failed")
        if not (0 < k <= L10 // 32):
            raise AssertionError("basin small-offset bound failed")
        if v2(k) % 2:
            raise AssertionError("wrong sponsor orientation")

    print("verified: depth-ten exact-tail basin fan")
    print(f"k_min={K_MIN}")
    print(f"k_max={K_MAX}")
    print(f"valid_offset_count={len(offsets)}")
    print(f"offset_sha256={digest}")
    print("v2_classes=" + ",".join(f"{key}:{classes[key]}" for key in sorted(classes)))
    print("terminal_charge=33215/16384")


if __name__ == "__main__":
    main()
