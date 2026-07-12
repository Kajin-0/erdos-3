# Contaminated-backbone depth-seven chain

## Status

Exact finite computer-assisted construction.

This note extends the certified contaminated-backbone chain from depth five to depth seven. It uses an alternative exact factor-eight recovery from `S_5`, followed by another valid factor-four contaminated step.

The resulting outer scale-factor sequence is

```math
\boxed{4,8,4,4,8,4.}
```

This disproves the proposed extension of the branch-specific recovery result to all exact factor-eight continuations of `S_5`. It also shows that multiplicity-weighted density need not contract over every six-generation window.

The construction is finite. It does not prove indefinite cheap replication or a divergent reciprocal-sum counterexample.

**Verifier:** `src/verify_contaminated_backbone_depth7.cpp`.

**Certificate:** `data/contaminated_backbone_depth7_certificate_2026-07-11.txt`.

---

## 1. Starting state

The previously certified burst ends at

```math
S_5\subseteq[32768,65536),
\qquad
|S_5|=1092,
```

with

```math
\min S_5=32768,
\qquad
\max S_5=63668.
```

Its canonical SHA-256 hash is

```text
a315deca0997d946ca9bb5058d2a04bfe3e585332d4db5260e7d9edc9142f841
```

and its certified identical-history persistence lower bound is

```math
P_5^{\mathrm{cert}}=32.
```

The multiplicity-weighted density is

```math
W_5
=
P_5^{\mathrm{cert}}\frac{|S_5|}{L_5}
=
\frac{273}{256}.
```

---

## 2. Alternative exact factor-eight recovery

Set

```math
\boxed{R_5=93476.}
```

Since

```math
v_2(R_5)=2,
```

the coordinated side-anchor rule selects the left sponsor.

Put

```math
A_5=\{0\}\cup S_5
```

and form

```math
G_6
=
A_5
\cup
(A_5+R_5)
\cup
(A_5+2R_5).
```

The verifier checks:

1. the three translate layers are disjoint;
2. `G_6` is four-term-progression-free;
3. the increasing left-sponsor deletion schedule is feasible;
4. the middle multiplicity fiber is exactly `S_5`;
5. the backbone shell is exactly `S_5`.

The raw state has

```math
|G_6|=3279,
\qquad
0\le G_6\le250620<262144.
```

Its SHA-256 hash is

```text
143ac2d24d2a2fdc1c44575f3287f22d5eaaea0104faac08e047b5a437705309
```

Define

```math
S_6=262144+G_6.
```

Then

```math
S_6\subseteq[262144,524288),
\qquad
|S_6|=3279,
```

with hash

```text
c7cbf524dc999a38facba1b587967f4d58b1bc028aca5e2ff131119439d8a88a
```

and persistence lower bound

```math
P_6^{\mathrm{cert}}=64.
```

The weighted density contracts during this exact recovery:

```math
W_6
=
\frac{3279}{4096},
```

```math
\frac{W_6}{W_5}
=
\frac{1093}{1456}
\approx0.750687.
```

---

## 3. A valid factor-four continuation

Set

```math
\boxed{R_6=230164.}
```

Again,

```math
v_2(R_6)=2,
```

so the coordinated sponsor is the left endpoint.

Put

```math
A_6=\{0\}\cup S_6
```

and form

```math
G_7
=
A_6
\cup
(A_6+R_6)
\cup
(A_6+2R_6).
```

The raw state satisfies

```math
|G_7|=9840,
\qquad
0\le G_7\le973092<1048576,
```

and is four-term-progression-free. Its SHA-256 hash is

```text
3d400b6280d5425be1e0c316867ffa35c99b553ebad376b74cdcf1146e160c1d
```

The middle multiplicity fiber is exactly `S_6`. The backbone shell

```math
G_7\cap[262144,524288)
```

contains `S_6` plus exactly two contaminating points:

```math
\boxed{460328,\ 492308.}
```

Therefore the deletion schedule inside `S_6` can be replayed in the backbone subset. The middle and backbone continuations share the same new root anchor, so certified identical-history persistence doubles again.

Define

```math
S_7=1048576+G_7.
```

Then

```math
S_7\subseteq[1048576,2097152),
\qquad
|S_7|=9840,
```

with hash

```text
0e6080448a9e171fcf915e110bb23fa8278d281d4d732da20454e8a10cb47e88
```

and

```math
P_7^{\mathrm{cert}}=128.
```

---

## 4. Weighted-density growth

For

```math
W_h
=
P_h^{\mathrm{cert}}\frac{|S_h|}{L_h},
```

one has

```math
W_7
=
128\frac{9840}{1048576}
=
\frac{615}{512}.
```

The factor-four step expands weighted density by

```math
\frac{W_7}{W_6}
=
\frac{1640}{1093}
\approx1.50046.
```

Across the exact factor-eight recovery and the subsequent factor-four step,

```math
\boxed{
\frac{W_7}{W_5}
=
\frac{205}{182}
\approx1.12637.
}
```

Thus the two-generation block grows rather than contracts.

Across all six outer generations from the base state,

```math
\boxed{
\frac{W_7}{W_1}
=
\frac{205}{64}
=3.203125.
}
```

The product of the six scale factors is

```math
4\cdot8\cdot4\cdot4\cdot8\cdot4
=16384,
```

whose geometric mean is

```math
16384^{1/6}
=2^{7/3}
\approx5.03968
<6.
```

The construction therefore remains on the weighted-density-expanding side of the asymptotic scale threshold through six outer generations.

---

## 5. Exhaustive factor-two search from `S_7`

A factor-two continuation would have next scale

```math
L_8=2L_7=2097152.
```

The fit condition gives

```math
R
\le
\left\lfloor
\frac{2097152-1-\max S_7}{2}
\right\rfloor
=37741.
```

There are exactly `25161` positive separations in this range with even two-adic valuation. Difference-set filtering leaves `202` candidates with disjoint translate layers.

Every one of those `202` candidates contains a nontrivial four-term progression. Hence

```math
\boxed{N_{7,2}=0.}
```

Thus the recorded depth-seven state has no factor-two continuation in the standard-dyadic disjoint three-translate replay model.

The factor-four continuation problem from `S_7` remains open.

---

## 6. Consequences for the proof program

The branch-specific result based on the smallest exact recovery

```math
R_5=65547
```

remains correct, but it is not representative of all exact factor-eight recoveries.

The new chain proves that the following statements are false without additional hypotheses:

1. every exact factor-eight recovery is followed by termination or another factor-eight step;
2. every exact factor-eight recovery initiates a two-generation weighted-density contraction;
3. multiplicity-weighted density contracts over every six consecutive outer generations;
4. the first valid exact recovery is extremal for future continuation behavior.

The active obstruction is therefore path-dependent. A state-independent theorem must control the full recovery tree, not one selected continuation.

Promising next targets are:

1. classify all valid factor-eight continuations of `S_5` by their factor-four descendants;
2. resolve the factor-four continuation problem from `S_7`;
3. identify a contamination-debt quantity that accounts for both the exact recovery and the later cheap release;
4. model the continuation graph as a finite or approximately finite symbolic system and bound its long-run spectral growth.
