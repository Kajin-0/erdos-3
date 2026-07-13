# First certified factor-four batch beyond the inherited `S_10` interval

## Status

Exact finite witness certificate.

The complete factor-four domain from the recorded state `S_10` remains unresolved. This note certifies the first `100` sponsor-compatible, layer-disjoint separations strictly beyond the inherited factor-two cutoff.

The certified separations run from

```math
R=76583927
```

to

```math
R=76587052.
```

Every one produces an explicit nontrivial four-term arithmetic progression in

```math
G_{10}(R)=(\{0\}\cup S_{10})+\{0,R,2R\}.
```

**Verifier:** `src/verify_depth10_factor4_first100.cpp`  
**Witness data:** `data/depth10_factor4_first100_witnesses_2026-07-13.txt`

---

## 1. Exact domain enumeration

The inherited interval ends at

```math
R=76583775.
```

The verifier reconstructs the certified states `S_8`, `S_9`, and `S_10`, rebuilds the positive-difference support recursively, and enumerates separations `R>76583775` satisfying:

1. the coordinated sponsor condition `v_2(R)` even;
2. `R` is absent from the `S_10` difference support;
3. `2R` is absent from the `S_10` difference support.

The first `100` such separations are exactly the witness keys in the certificate. The first and last are

```text
76583927
76587052
```

respectively.

---

## 2. Explicit witness verification

Each certificate row has the form

```text
R a b c d
```

and the verifier checks

```math
b-a=c-b=d-c>0.
```

It then independently verifies that each of `a,b,c,d` belongs to `G_{10}(R)` by checking membership in one of the three translate layers.

The witness file has:

```text
records:  100
FNV-64:  1a61bdf6a331636d
SHA-256: 10c561ceb5c072b372393fb99611caadb193b6f9f68a4aa8aab402b6dcabf39e
```

One representative row is

```text
76583927 862928649 901221262 939513875 977806488
```

with common difference

```math
38292613.
```

---

## 3. Consequence

The genuinely new factor-four domain contains

```math
314986450
```

layer-disjoint candidates. This certificate removes `100` of them by direct witnesses, leaving at most

```math
\boxed{314986350}
```

unclassified candidates.

This is a deliberately bounded checkpoint. It does not validate the previously rejected anchor reduction and does not imply

```math
N_{10,4}=0.
```

The next safe extension is another contiguous exact witness batch generated and verified by the same method, or a new structural lemma that outputs actual four-point witnesses.
