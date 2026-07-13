# First 5000 certified factor-four candidates beyond the inherited `S_10` interval

## Status

Exact finite witness certificate.

The complete factor-four domain from the recorded state `S_10` remains unresolved. This note certifies the first `5000` sponsor-compatible, layer-disjoint separations strictly beyond the inherited factor-two cutoff.

The previously committed verifiers certify positions `1` through `1000`. The new verifier certifies positions `1001` through `5000`, adding `4000` explicit four-term-progression witnesses.

The complete certified prefix runs from

```math
R=76583927
```

to

```math
R=76646105.
```

Every separation in this prefix produces a nontrivial four-term arithmetic progression in

```math
G_{10}(R)=(\{0\}\cup S_{10})+\{0,R,2R\}.
```

**New verifier:** `src/verify_depth10_factor4_positions_1001_5000.cpp`  
**Certificate:** `data/depth10_factor4_positions_1001_5000_certificate_2026-07-13.txt`

---

## 1. Exact domain prefix

The inherited interval ends at

```math
R=76583775.
```

The verifier reconstructs `S_8`, `S_9`, and `S_10`, rebuilds the positive-difference support recursively, and enumerates the first `5000` separations above the cutoff satisfying:

1. `v_2(R)` is even;
2. `R` is absent from the positive-difference support of `\{0\}\cup S_{10}`;
3. `2R` is absent from that support.

It verifies that domain position `1001` is

```text
76603913
```

and position `5000` is

```text
76646105.
```

---

## 2. Deterministic explicit witnesses

For each of positions `1001` through `5000`, the verifier initializes a separate fixed xorshift stream from the separation `R`. It samples two candidate points, treats them as the first two terms of a progression, and accepts only after independently checking that the third and fourth terms also belong to `G_10(R)`.

The search is parallelized across separations. Parallel scheduling cannot change any witness because each separation has an isolated deterministic RNG state.

All `4000` candidates succeed under the fixed cap of `3000000` trials per separation. The generated witness text has:

```text
records:  4000
FNV-64:   2a029f96119035a1
SHA-256:  b0dc16f4fea56c189c7b1c954ffe37bad36231ed291d9d6311d5a1c5ea3ff5d4
```

The exact run statistics are:

```text
total deterministic trials: 363937682
maximum trials for one R:       774028
maximum-trial R:              76604127
```

Every generated row has the form

```text
R a b c d
```

and is checked for

```math
b-a=c-b=d-c>0,
```

with all four points checked independently for membership in `G_10(R)`.

---

## 3. Consequence

The genuinely new factor-four domain contains

```math
314986450
```

layer-disjoint candidates. The first `5000` are now directly excluded, leaving at most

```math
\boxed{314981450}
```

unclassified candidates.

This is a finite prefix theorem. It does not validate the rejected bulk anchor reduction and does not imply

```math
N_{10,4}=0.
```

The direct-witness method continues to find explicit progressions at high density, but a complete theorem still requires either exhaustive certification of the entire domain or a valid structural reduction that outputs actual four-point witnesses.
