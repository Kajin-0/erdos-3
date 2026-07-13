# First 10000 certified factor-four candidates beyond the inherited `S_10` interval

## Status

Exact finite witness certificate.

The complete factor-four domain from the recorded state `S_10` remains unresolved. This note certifies the first `10000` sponsor-compatible, layer-disjoint separations strictly beyond the inherited factor-two cutoff.

The previously committed verifiers certify positions `1` through `5000`. The new verifier certifies positions `5001` through `10000`, adding `5000` explicit four-term-progression witnesses.

The complete certified prefix runs from

```math
R=76583927
```

to

```math
R=76697408.
```

Every separation in this prefix produces a nontrivial four-term arithmetic progression in

```math
G_{10}(R)=(\{0\}\cup S_{10})+\{0,R,2R\}.
```

**New verifier:** `src/verify_depth10_factor4_positions_5001_10000.cpp`  
**Certificate:** `data/depth10_factor4_positions_5001_10000_certificate_2026-07-13.txt`

---

## 1. Exact domain prefix

The inherited interval ends at

```math
R=76583775.
```

The verifier reconstructs `S_8`, `S_9`, and `S_10`, rebuilds the positive-difference support recursively, and enumerates the first `10000` separations above the cutoff satisfying:

1. `v_2(R)` is even;
2. `R` is absent from the positive-difference support of `\{0\}\cup S_{10}`;
3. `2R` is absent from that support.

It verifies that domain position `5001` is

```text
76646153
```

and position `10000` is

```text
76697408.
```

---

## 2. Deterministic explicit witnesses

For each of positions `5001` through `10000`, the verifier initializes a separate fixed xorshift stream from the separation `R`. It samples two candidate points, treats them as the first two terms of a progression, and accepts only after independently checking that the third and fourth terms also belong to `G_10(R)`.

The search is parallelized across separations. Parallel scheduling cannot change any witness because each separation has an isolated deterministic RNG state.

All `5000` candidates succeed under the fixed cap of `3000000` trials per separation. The generated witness text has:

```text
records:  5000
FNV-64:   ce7f765c19d63ade
SHA-256:  c3337255e01e414a75761767c9921442eb358dbb46d8bbbe4181789d91094412
```

The exact run statistics are:

```text
total deterministic trials: 510227717
maximum trials for one R:       914319
maximum-trial R:              76694747
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

layer-disjoint candidates. The first `10000` are now directly excluded, leaving at most

```math
\boxed{314976450}
```

unclassified candidates.

This is a finite prefix theorem. It does not validate the rejected bulk anchor reduction and does not imply

```math
N_{10,4}=0.
```

The direct-witness method continues to find explicit progressions at high density, but a complete theorem still requires either exhaustive certification of the entire domain or a valid structural reduction that outputs actual four-point witnesses.
