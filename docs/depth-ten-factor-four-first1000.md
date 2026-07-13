# First 1000 certified factor-four candidates beyond the inherited `S_10` interval

## Status

Exact finite witness certificate.

The complete factor-four domain from the recorded state `S_10` remains unresolved. This note certifies the first `1000` sponsor-compatible, layer-disjoint separations strictly beyond the inherited factor-two cutoff.

The first `100` candidates were certified in `docs/depth-ten-factor-four-first100.md`. The present verifier certifies domain positions `101` through `1000`, adding `900` explicit four-term-progression witnesses.

The full certified prefix runs from

```math
R=76583927
```

to

```math
R=76603903.
```

Every separation in this prefix produces a nontrivial four-term arithmetic progression in

```math
G_{10}(R)=(\{0\}\cup S_{10})+\{0,R,2R\}.
```

**Prior verifier:** `src/verify_depth10_factor4_first100.cpp`  
**New verifier:** `src/verify_depth10_factor4_positions_101_1000.cpp`  
**Certificate:** `data/depth10_factor4_positions_101_1000_certificate_2026-07-13.txt`

---

## 1. Exact domain prefix

The inherited interval ends at

```math
R=76583775.
```

The new verifier reconstructs `S_8`, `S_9`, and `S_10`, rebuilds the positive-difference support recursively, and enumerates the first `1000` separations above the cutoff satisfying:

1. `v_2(R)` is even;
2. `R` is absent from the positive-difference support of `\{0\}\cup S_{10}`;
3. `2R` is absent from that support.

It verifies that domain position `101` is

```text
76587092
```

and domain position `1000` is

```text
76603903.
```

---

## 2. Deterministically generated explicit witnesses

For each of positions `101` through `1000`, the verifier uses a fixed custom xorshift generator and a separation-dependent seed. It samples two points from the three translate layers, treats them as the first two terms of a progression, and accepts only after independently confirming that the third and fourth terms are also members of `G_{10}(R)`.

The procedure is deterministic. It either produces an actual checked four-point witness or fails after a fixed cap of `3000000` trials.

All `900` candidates succeed. The complete generated witness text has:

```text
records:  900
FNV-64:   dc92ceac26789b47
SHA-256:  0c8e16f6c4206c2fe2fd1a451d0c2aab1445baac154923b5656e3599e1b4897c
```

The run used:

```text
total deterministic trials: 79638832
maximum trials for one R:       781823
maximum-trial R:              76602965
```

Passing an output path to the verifier writes all `900` rows in the form

```text
R a b c d
```

with

```math
b-a=c-b=d-c>0.
```

---

## 3. Consequence

The genuinely new factor-four domain contains

```math
314986450
```

layer-disjoint candidates. The first `1000` are now directly excluded, leaving at most

```math
\boxed{314985450}
```

unclassified candidates.

This is a finite prefix theorem. It does not validate the rejected bulk anchor reduction and does not imply

```math
N_{10,4}=0.
```

The useful new empirical fact is that direct full-candidate witnesses are sufficiently dense for deterministic bounded search to certify a substantially larger contiguous prefix without relying on the unsupported reduction.