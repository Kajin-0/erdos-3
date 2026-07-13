#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import hashlib
import sys


def norm(word):
    shift = min(word)
    return tuple(value - shift for value in word)


def signature(word):
    l0, l1, l2, l3 = word
    return (
        l1 - l0,
        l0 - 2 * l1 + l2,
        l1 - 2 * l2 + l3,
    )


words = sorted({norm(word) for word in product(range(3), repeat=4)})
channels = []
for outer in words:
    if outer == (0, 0, 0, 0):
        continue
    r_outer, a_outer, b_outer = signature(outer)
    if a_outer == 0 and b_outer == 0:
        continue
    for parent in words:
        if parent == (0, 0, 0, 0):
            continue
        r_parent, a_parent, b_parent = signature(parent)
        if a_parent == -4 * a_outer and b_parent == -4 * b_outer:
            channels.append(
                (outer, parent, signature(outer), signature(parent))
            )

assert channels == [
    ((0, 0, 1, 1), (0, 2, 0, 2), (0, 1, -1), (2, -4, 4)),
    ((0, 1, 1, 2), (2, 0, 2, 0), (1, -1, 1), (-2, 4, -4)),
    ((1, 1, 0, 0), (2, 0, 2, 0), (0, -1, 1), (-2, 4, -4)),
    ((2, 1, 1, 0), (0, 2, 0, 2), (-1, 1, -1), (2, -4, 4)),
]

# Exact construction checks over a finite symbolic integer box.
for separation in range(1, 8):
    for effective in range(1, 2 * separation):
        for start in range(-3, 4):
            for difference in range(1, 8):
                base = (
                    start,
                    start + difference,
                    start + 2 * difference - effective,
                    start + 3 * difference - effective,
                )

                tested = 4 * separation + effective
                outer = (0, 0, 1, 1)
                parent = (0, 2, 0, 2)
                points = tuple(
                    base[index]
                    + parent[index] * separation
                    + outer[index] * tested
                    for index in range(4)
                )
                assert (
                    points[1] - points[0]
                    == points[2] - points[1]
                    == points[3] - points[2]
                    == difference + 2 * separation
                )

                tested = 4 * separation - effective
                outer = (0, 1, 1, 2)
                parent = (2, 0, 2, 0)
                points = tuple(
                    base[index]
                    + parent[index] * separation
                    + outer[index] * tested
                    for index in range(4)
                )
                assert (
                    points[1] - points[0]
                    == points[2] - points[1]
                    == points[3] - points[2]
                    == difference + 2 * separation - effective
                    > 0
                )

lines = [
    "K=4 RECTANGLE TRANSPORT CHANNEL",
    "",
    "base_rectangle=x,x+d,x+2d-U,x+3d-U",
    "positive_common_difference=d>0",
    "",
    "plus_transport:",
    "  T=4S+U",
    "  outer_lambda=0011",
    "  parent_mu=0202",
    "  output_common_difference=d+2S",
    "",
    "minus_transport:",
    "  T=4S-U",
    "  hypotheses=0<U<2S",
    "  outer_lambda=0112",
    "  parent_mu=2020",
    "  output_common_difference=d+2S-U",
    "",
    "all_normalized_k4_signature_channels:",
]
for outer, parent, outer_signature, parent_signature in channels:
    lines.append(
        "  "
        + "".join(map(str, outer))
        + " "
        + "".join(map(str, parent))
        + f" lambda_sig={outer_signature} mu_sig={parent_signature}"
    )
certificate = "\n".join(lines) + "\n"

if len(sys.argv) > 2:
    raise SystemExit("usage: verify_rectangle_transport_channel.py [OUTPUT]")
if len(sys.argv) == 2:
    Path(sys.argv[1]).write_text(certificate, encoding="utf-8")

print("verified: exact k=4 rectangle transport lemma")
print("normalized_k4_channels=4")
print("channels=0011/0202,0112/2020,1100/2020,2110/0202")
print("certificate_sha256=" + hashlib.sha256(certificate.encode()).hexdigest())
