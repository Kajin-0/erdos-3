#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import hashlib
import sys


def normalize(word):
    shift = min(word)
    return tuple(x - shift for x in word)


def signature(word):
    l0, l1, l2, l3 = word
    return l1 - l0, l0 - 2 * l1 + l2, l1 - 2 * l2 + l3


def text(word):
    return "".join(map(str, word))


def parse_word(value):
    return tuple(map(int, value))


def add(left, right):
    return tuple(x + y for x, y in zip(left, right))


def subtract(left, right):
    return tuple(x - y for x, y in zip(left, right))


WORDS = sorted({normalize(word) for word in product(range(3), repeat=4)})
PLUS = {
    1: ("0011", "1100"),
    2: ("0011", "2200"),
    3: ("0011", "1201"),
    4: ("0011", "0202"),
}
MINUS = {
    1: ("0112", "0011"),
    2: ("0112", "0022"),
    3: ("0112", "1021"),
    4: ("0112", "2020"),
}
# Coefficient order is x,d,S,U.
BASE = [
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (1, 2, 0, -1),
    (1, 3, 0, -1),
]


def projected(k, sign, outer, parent):
    points = []
    for index in range(4):
        point = BASE[index]
        point = add(point, (0, 0, parent[index], 0))
        point = add(point, (0, 0, k * outer[index], sign * outer[index]))
        points.append(point)
    differences = [subtract(points[i + 1], points[i]) for i in range(3)]
    assert differences[0] == differences[1] == differences[2]
    return points, differences[0]


def build_certificate():
    rectangle_words = [
        word for word in WORDS
        if signature(word)[1:] in ((1, -1), (-1, 1))
    ]
    lines = [
        "FOUR-RATIO RECTANGLE TRANSPORT CLASSIFICATION",
        "",
        f"normalized_words={len(WORDS)}",
        "rectangle_outer_words=" + ",".join(map(text, rectangle_words)),
        "",
    ]
    counts = {}
    for k in range(1, 9):
        pairs = []
        for outer in rectangle_words:
            _, a, b = signature(outer)
            for parent in WORDS:
                _, parent_a, parent_b = signature(parent)
                if (parent_a, parent_b) == (-k * a, -k * b):
                    pairs.append((outer, parent))
        counts[k] = len(pairs)
        lines.append(f"k={k} rectangle_cancellation_pairs={len(pairs)}")
    assert [counts[k] for k in range(1, 5)] == [8, 8, 4, 4]
    assert all(counts[k] == 0 for k in range(5, 9))

    expected_difference = {
        ("plus", 1): (0, 1, 0, 0),
        ("plus", 2): (0, 1, 0, 0),
        ("plus", 3): (0, 1, 1, 0),
        ("plus", 4): (0, 1, 2, 0),
        ("minus", 1): (0, 1, 1, -1),
        ("minus", 2): (0, 1, 2, -1),
        ("minus", 3): (0, 1, 2, -1),
        ("minus", 4): (0, 1, 2, -1),
    }
    lines.extend(["", "selected canonical channels:"])
    for name, table, sign in (("plus", PLUS, 1), ("minus", MINUS, -1)):
        for k, (outer_text, parent_text) in table.items():
            outer = parse_word(outer_text)
            parent = parse_word(parent_text)
            _, a, b = signature(outer)
            _, parent_a, parent_b = signature(parent)
            assert (parent_a, parent_b) == (-k * a, -k * b)
            points, difference = projected(k, sign, outer, parent)
            assert difference == expected_difference[(name, k)]
            lines.append(
                f"{name} k={k} lambda={outer_text} mu={parent_text} "
                f"q_coeff={difference} point_coeffs={points}"
            )

    lines.extend([
        "",
        "window statement:",
        "If 0<U<S and B contains x,x+d,x+2d-U,x+3d-U with d>0,",
        "then every T=kS+U and T=kS-U, k=1,2,3,4, has a transported nontrivial 4-AP in G_T(G_S(B)).",
        "The four windows [kS-Umax,kS+Umax] overlap whenever Umax>=S/2.",
        "",
    ])
    return "\n".join(lines)


def main():
    certificate = build_certificate()
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_four_ratio_rectangle_transport.py [OUTPUT]")
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print("verified: exact k=1,2,3,4 rectangle transport channels")
    print("pair_counts=8,8,4,4")
    print("verified: no integer rectangle cancellation ratio k>=5")
    print("certificate_sha256=" + hashlib.sha256(certificate.encode()).hexdigest())


if __name__ == "__main__":
    main()
