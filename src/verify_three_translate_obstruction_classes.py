#!/usr/bin/env python3
"""Exact symbolic classification and recurrence identities for three-translate 4-AP obstructions."""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path
import hashlib
import sys

Word = tuple[int, int, int, int]


def normalize(word: Word) -> Word:
    shift = min(word)
    return tuple(x - shift for x in word)  # type: ignore[return-value]


def reverse_word(word: Word) -> Word:
    return tuple(reversed(word))  # type: ignore[return-value]


def signature(word: Word) -> tuple[int, int, int]:
    l0, l1, l2, l3 = word
    r = l1 - l0
    a = l0 - 2 * l1 + l2
    b = l1 - 2 * l2 + l3
    return r, a, b


def reconstruct(sig: tuple[int, int, int]) -> Word:
    r, a, b = sig
    raw = (0, r, 2 * r + a, 3 * r + 2 * a + b)
    return normalize(raw)


def text(word: Word) -> str:
    return "".join(map(str, word))


def class_rows() -> list[tuple[int, Word, Word, int, int, int, int]]:
    raw_words = list(product(range(3), repeat=4))
    normalized = sorted({normalize(word) for word in raw_words})

    assert len(raw_words) == 81
    assert len(normalized) == 65  # 3^4 - 2^4

    unseen = set(normalized)
    orbits: list[tuple[Word, ...]] = []
    while unseen:
        seed = min(unseen)
        mate = reverse_word(seed)
        orbit = tuple(sorted({seed, mate}))
        orbits.append(orbit)
        unseen.difference_update(orbit)

    base = ((0, 0, 0, 0),)
    assert base in orbits
    nonconstant = sorted((orbit for orbit in orbits if orbit != base), key=lambda orbit: orbit[0])

    assert len(nonconstant) == 34
    assert sum(map(len, nonconstant)) == 64
    assert Counter(map(len, nonconstant)) == Counter({2: 30, 1: 4})

    rows = []
    self_reversing = []
    signatures = set()
    for idx, orbit in enumerate(nonconstant, start=1):
        rep = orbit[0]
        rev = reverse_word(rep)
        r, a, b = signature(rep)
        rr, ar, br = signature(rev)
        assert (rr, ar, br) == (-(r + a + b), b, a)
        assert reconstruct((r, a, b)) == rep
        assert rev in orbit
        if len(orbit) == 1:
            self_reversing.append(rep)
            assert a == b
        signatures.add((r, a, b))
        rows.append((idx, rep, rev, r, a, b, len(orbit)))

    assert len(signatures) == 34
    assert self_reversing == [
        (0, 1, 1, 0),
        (0, 2, 2, 0),
        (1, 0, 0, 1),
        (2, 0, 0, 2),
    ]
    return rows


def verify_affine_parameterization() -> None:
    # Exhaustive symbolic/integer check over all raw words and a box of parameters.
    for word in product(range(3), repeat=4):
        lam = tuple(word)  # type: ignore[assignment]
        r, a, b = signature(lam)
        for R in range(-3, 4):
            if R == 0:
                continue
            for x in range(-2, 3):
                for delta in range(-3, 4):
                    bases = (
                        x,
                        x + delta,
                        x + 2 * delta - a * R,
                        x + 3 * delta - (2 * a + b) * R,
                    )
                    z = tuple(bases[i] + lam[i] * R for i in range(4))
                    q = delta + r * R
                    assert z[1] - z[0] == q
                    assert z[2] - z[1] == q
                    assert z[3] - z[2] == q


def verify_two_scale_composition() -> None:
    # Exhaustively checks the algebra behind the labeled recurrence.
    words = [tuple(w) for w in product(range(3), repeat=4)]
    for lam in words:
        rl, al, bl = signature(lam)  # candidate-layer word at T
        for mu in words:
            rm, am, bm = signature(mu)  # parent-layer representations at S
            for S in (-2, -1, 1, 2):
                for T in (-2, -1, 1, 2):
                    for x in (-1, 0, 1):
                        for delta in (-2, -1, 0, 1, 2):
                            A = al * T + am * S
                            B = bl * T + bm * S
                            bases = (
                                x,
                                x + delta,
                                x + 2 * delta - A,
                                x + 3 * delta - (2 * A + B),
                            )
                            z = tuple(
                                bases[i] + mu[i] * S + lam[i] * T
                                for i in range(4)
                            )
                            q = delta + rl * T + rm * S
                            assert z[1] - z[0] == q
                            assert z[2] - z[1] == q
                            assert z[3] - z[2] == q


def build_certificate() -> str:
    rows = class_rows()
    verify_affine_parameterization()
    verify_two_scale_composition()

    lines = [
        "THREE-TRANSLATE 4-AP OBSTRUCTION CLASSIFICATION",
        "",
        "raw_layer_words=81",
        "normalized_layer_words=65",
        "base_only_class=0000",
        "nonconstant_normalized_words=64",
        "nonconstant_reversal_classes=34",
        "two_word_reversal_classes=30",
        "self_reversing_classes=4",
        "self_reversing_words=0110,0220,1001,2002",
        "",
        "signature definitions:",
        "  r=lambda1-lambda0",
        "  a=lambda0-2*lambda1+lambda2",
        "  b=lambda1-2*lambda2+lambda3",
        "",
        "class representative reverse r a b orbit_size",
    ]
    for idx, rep, rev, r, a, b, orbit_size in rows:
        lines.append(
            f"{idx:02d} {text(rep)} {text(rev)} {r:+d} {a:+d} {b:+d} {orbit_size}"
        )

    lines.extend(
        [
            "",
            "exact one-scale affine parameterization:",
            "  base points = x, x+d, x+2d-aR, x+3d-(2a+b)R",
            "  projected common difference = d+rR",
            "  nontriviality condition = d+rR != 0",
            "",
            "exact labeled two-scale composition:",
            "  A=a(lambda)T+a(mu)S",
            "  B=b(lambda)T+b(mu)S",
            "  Q=r(lambda)T+r(mu)S",
            "  base points = x, x+d, x+2d-A, x+3d-(2A+B)",
            "  projected common difference = d+Q",
            "",
            "pair-start recurrence:",
            "  P_d(G_S(B)) = union_{i,j in {0,1,2}} (P_{d+(i-j)S}(B)+iS)",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    certificate = build_certificate()
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_three_translate_obstruction_classes.py [OUTPUT]")
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    digest = hashlib.sha256(certificate.encode()).hexdigest()
    print("verified: exact 34-class three-translate 4-AP obstruction decomposition")
    print("nonconstant_reversal_classes=34")
    print("self_reversing_words=0110,0220,1001,2002")
    print("verified: one-scale affine parameterization")
    print("verified: labeled two-scale composition identity")
    print(f"certificate_sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
