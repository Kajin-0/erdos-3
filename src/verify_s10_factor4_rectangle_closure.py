#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import hashlib
import sys

S = 134217729
UMAX = 76583776
RESIDUAL_LOW = 97474324
RESIDUAL_HIGH = 613454687
INHERITED_COUNT = 33026376
LIFTED_COMPLETION_COUNT = 137142200
RESIDUAL_COUNT = 177844250
TOTAL_DISJOINT_COUNT = 348012826


def normalize(word):
    shift = min(word)
    return tuple(x - shift for x in word)


def signature(word):
    l0, l1, l2, l3 = word
    return l1 - l0, l0 - 2 * l1 + l2, l1 - 2 * l2 + l3


WORDS = sorted({normalize(word) for word in product(range(3), repeat=4)})


def build_certificate():
    cancellation_counts = []
    for k in range(1, 9):
        count = 0
        for outer in WORDS:
            _, a, b = signature(outer)
            if (a, b) not in ((1, -1), (-1, 1)):
                continue
            for parent in WORDS:
                _, c, d = signature(parent)
                if (c, d) == (-k * a, -k * b):
                    count += 1
        cancellation_counts.append(count)

    assert cancellation_counts[:4] == [8, 8, 4, 4]
    assert cancellation_counts[4:] == [0, 0, 0, 0]

    windows = [(k * S - UMAX, k * S + UMAX) for k in range(1, 5)]
    assert windows[0][0] <= RESIDUAL_LOW
    assert windows[-1][1] >= RESIDUAL_HIGH
    for left, right in zip(windows, windows[1:]):
        assert left[1] >= right[0]

    for test_value in [
        RESIDUAL_LOW,
        RESIDUAL_HIGH,
        *[endpoint for interval in windows for endpoint in interval],
    ]:
        if RESIDUAL_LOW <= test_value <= RESIDUAL_HIGH:
            assert any(abs(test_value - k * S) <= UMAX for k in range(1, 5))

    pure_layer = {}
    for k in range(1, 5):
        layer_sumset = sorted({i + k * j for i in range(3) for j in range(3)})
        progressions = []
        for start in layer_sumset:
            for step in range(1, 20):
                if all(start + term * step in layer_sumset for term in range(4)):
                    progressions.append((start, step))
        assert progressions
        pure_layer[k] = (layer_sumset, progressions[0])

    assert (
        INHERITED_COUNT + LIFTED_COMPLETION_COUNT + RESIDUAL_COUNT
        == TOTAL_DISJOINT_COUNT
    )

    lines = [
        "S10 FACTOR-FOUR CLOSURE LOGIC",
        "",
        f"S={S}",
        f"Umax={UMAX}",
        f"residual_interval={RESIDUAL_LOW},{RESIDUAL_HIGH}",
        "rectangle_cancellation_counts=" + ",".join(map(str, cancellation_counts)),
        "windows:",
    ]
    for k, (low, high) in enumerate(windows, start=1):
        lines.append(f"  k={k} {low} {high}")

    lines.extend(["", "pure-layer U=0 witnesses:"])
    for k, (layer_sumset, progression) in pure_layer.items():
        lines.append(
            f"  k={k} layer_sumset={layer_sumset} "
            f"AP_start={progression[0]} AP_step={progression[1]}"
        )

    lines.extend(
        [
            "",
            f"partition={INHERITED_COUNT}+{LIFTED_COMPLETION_COUNT}+"
            f"{RESIDUAL_COUNT}={TOTAL_DISJOINT_COUNT}",
            "conclusion: if direct B9 rectangle support contains every "
            "1<=U<=Umax, then every residual T is blocked; U=0 is blocked "
            "by pure layers; hence N_10_4=0.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    certificate = build_certificate()
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_s10_factor4_rectangle_closure.py [OUTPUT]")
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print("verified: four transport windows cover the full S10 factor-four residual")
    print("verified: pure-layer U=0 boundary for k=1,2,3,4")
    print(
        "verified: candidate partition "
        f"{INHERITED_COUNT}+{LIFTED_COMPLETION_COUNT}+{RESIDUAL_COUNT}="
        f"{TOTAL_DISJOINT_COUNT}"
    )
    print("certificate_sha256=" + hashlib.sha256(certificate.encode()).hexdigest())


if __name__ == "__main__":
    main()
