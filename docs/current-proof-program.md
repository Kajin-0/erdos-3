# Current proof program: Bellman debt and whole-tree compensation

## Status

This is the authoritative overview of the active program for Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A}1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. This repository studies the four-term case. The claims below are proved internally or computationally certified as stated, but await independent expert review.

---

## 1. Foundational recursion

For

```math
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j},
```

one has, up to constants,

```math
\sum_{n\in A}\frac1n=\infty
\quad\Longleftrightarrow\quad
\sum_j\alpha_j=\infty.
```

Coordinated side-anchor deletion and the minimum-translation backbone give

```math
H(\mathcal B(D))+\sum_xH(M_x)
\ge
3H(D)-2\frac{r_3(N)}N-\frac1N,
```

and, after exact middle-multiplicity resolution,

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

The genealogy is binary. Every child must be resolved into standard dyadic shells. Every parent creates at most two retained outputs, each at most half its label, so for `p>=1`,

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p.
```

Center, root-anchor, predecessor-anchor, and antichain decompositions compress repeated labels. These tools control positive moments and local multiplicity, but not reciprocal mass by themselves.

---

## 2. Sharp exact model

The aligned-diamond recursion has

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h,
```

so

```math
P_h\asymp|S_h|^{\log_3 2}.
```

There is a computer-certified infinite exact scale-eight family with

```math
L_h=8^{h+1},
\qquad
P_h=\frac12L_h^{1/3}.
```

A 34-state automaton and an exact `17238`-state carry search certify that its union contains no nontrivial four-term progression.

Inside the exact standard-dyadic equal-translate model,

```math
L'\ge8L,
```

```math
P_h\alpha_h\le C_0(3/4)^h,
```

and

```math
\sum_hP_h\alpha_h\le4C_0.
```

The exact model is sharply classified.

---

## 3. Contaminated path dependence

A certified contaminated chain has scale factors

```math
\boxed{4,8,4,4}
```

through `S_5`. For

```math
W_h=P_h^{\mathrm{cert}}\frac{|S_h|}{L_h},
```

```math
W_1=\frac38,
\qquad
W_5=\frac{273}{256},
\qquad
\frac{W_5}{W_1}=\frac{91}{32}.
```

Local contraction and contraction over every four-generation window are false.

The alternative exact recovery

```math
R_5=93476
```

admits the factor-four descendant

```math
R_6=230164,
```

giving

```math
\boxed{4,8,4,4,8,4}
```

through `S_7`, with

```math
\frac{W_7}{W_5}=\frac{205}{182}>1.
```

Universal two-generation recovery and contraction over every six-generation window are false. Recovery is path-dependent.

---

## 4. Structural exclusion and the recorded branch through `S_10`

The recorded states `S_7`, `S_8`, and `S_9` satisfy

```math
N_{h,2}=N_{h,4}=0.
```

Their factor-four disjoint domains are exhausted by completion, `1001`, and equal-difference `0011` witnesses:

```text
S7:      359419
S8:     4190292
S9:    39459384
```

The first valid exact continuations are

```math
R_7=2097164,
\qquad
R_8=16777217,
\qquad
R_9=134217729.
```

The finite scale sequence is

```math
\boxed{4,8,4,4,8,4,8,8,8.}
```

At depth ten,

```math
L_{10}=536870912,
\qquad
|S_{10}|=265719,
\qquad
P_{10}=1024,
```

```math
W_{10}=\frac{265719}{524288},
```

and

```math
\frac{W_{10}}{W_5}=\frac{88573}{186368}\approx0.475259.
```

---

## 5. Exact-tail layer theorems

For the exact-tail shell geometry, the top-layer reduction says every new four-term progression in three translates comes from either:

1. a three-term progression completed at the separation `R`; or
2. the half-separation point `R/2` lying in the state.

For `R=2L+k`, completion descent maps a child target offset `c` to the parent offset

```math
c-3k.
```

Exact rational enumeration gives the unique descent layer pattern `012` in the certified regions. A state-specific rational classification also proves that the same nine top-layer patterns remain complete across the full fitting exact factor-eight range of `S_10`.

**Primary references:**

- `docs/extended-completion-descent.md`;
- `src/verify_exact_tail_pattern_lemmas.py`.

---

## 6. Exact-tail basin theorems

### 6.1 Original small-offset basin

If

```math
\min S=L,
\qquad
S\subseteq[L,7L/4),
```

```math
0<k\le L/32,
\qquad
v_2(k)\equiv0\pmod2,
```

and the first exact step at `R=2L+k` is valid, then

```math
L_{n+1}=8L_n,
\qquad
k_{n+1}=4k_n
```

defines an infinite exact four-term-progression-free tail.

### 6.2 Half-scale basin enlargement

The exact pattern audit enlarges the entry range to

```math
\boxed{0<k<L/2.}
```

Assume

```math
\min S=L,
\qquad
S\subseteq[L,7L/4),
```

and that the first exact step at `R=2L+k` is valid. Then the scheduled successor is also valid, and all later scheduled successors remain valid.

The first child satisfies

```math
S_1\subseteq[L_1,59L_1/32),
\qquad
k_1/L_1<1/4.
```

Thereafter the region

```math
S_n\subseteq[L_n,15L_n/8),
\qquad
k_n/L_n<1/4
```

is invariant. The same nine top-layer patterns remain complete, scheduled completion descent has the unique pattern `012`, and the half-separation obstruction is impossible because `0<2k_n<L_n`.

For entry size `N`, replay multiplicity `P`, and scale `L`, every such tail has terminal charge

```math
\boxed{
\sum_{n\ge0}W_n=\frac{4P(N+1)}L.
}
```

**Primary references:**

- `docs/half-scale-exact-tail-basin.md`;
- `src/verify_half_scale_exact_tail_basin.py`;
- `data/half_scale_exact_tail_basin_certificate_2026-07-12.txt`.

---

## 7. Exact child classification at `S_10`

Write every fitting exact separation as

```math
R=2L_{10}+k,
```

with

```math
1\le k\le613454687.
```

There are `408969792` sponsor-compatible positive offsets. The complete obstruction split is

```text
completion-blocked:       54999
half-separation-blocked:  59034
overlap:                       0
```

so

```math
\boxed{408855759}
```

positive offsets give valid exact factor-eight continuations.

### 7.1 Original basin fan

In `4<=k<=L_{10}/32`, exactly

```math
11129810
```

offsets enter certified infinite tails.

### 7.2 Half-scale basin fan

In

```math
1\le k<L_{10}/2,
```

there are

```text
178956970 sponsor-compatible offsets
54999 completion obstructions
29569 half-separation obstructions.
```

Therefore

```math
\boxed{178872402}
```

valid offsets enter certified infinite exact tails. This is approximately `43.75%` of all valid positive exact children and approximately `16.07` times the original basin fan.

Every tail has charge

```math
\boxed{33215/16384.}
```

The behavior of valid exact children with `k>=L_{10}/2` remains open.

---

## 8. Bellman potential and debt

For constant exact scale factor `c>6`, the affine future-cost function is

```math
\boxed{
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac{6}{c-2}\right).
}
```

At `c=8`,

```math
\mathfrak B_8=\frac{4P(N+1)}L.
```

For a disjoint three-translate step with scale factor `c`,

```math
\boxed{
\mathfrak D_c
=
\mathfrak B-W-\mathfrak B'
=
\frac{P(3N+4)}L\left(1-\frac8c\right).
}
```

Factors `2` and `4` create debt, factor `8` is neutral, and factors at least `16` create surplus.

A path whose scale word can be parsed into blocks

```text
[8 or larger]
[one 4 plus two 8-equivalents]
[one 2 plus four 8-equivalents]
```

has summable weighted density. The worst block-boundary contraction is

```math
2551/2560<1.
```

---

## 9. Cheap-step geometry and `S_10` escape domains

For top slack

```math
T=2L-\max S,
```

a step with scale factor `c` and separation `R` satisfies

```math
\boxed{T'=T+(c-2)L-2R.}
```

Every cheap Bellman debt therefore carries a geometric certificate: strict slack consumption or imported prefix contamination.

The exact `S_10` layer-disjoint candidate domains are:

### Factor two

```text
maximum R:             76583775
sponsor-compatible:    51055851
layer-disjoint:        33026376
FNV-64:                59cfbc6761c6224d
```

### Factor four

```text
maximum R:            613454687
sponsor-compatible:   408969792
layer-disjoint:       348012826
FNV-64:               ae1d9e1ec77b2dfb
```

These are domain certificates only. Complete exclusion or a cheap escape construction remains open.

---

## 10. Current unresolved problem: whole-tree compensation

The active target is

```math
\boxed{
\text{prove that every infinite continuation path has summable total weighted density.}
}
```

The current architecture is

```text
contaminated transient
    -> exact Bellman debt
    -> slack consumption or prefix contamination
    -> repayment parsing or basin entry
    -> finite terminal charge.
```

Equivalent remaining tasks:

1. classify the exact `S_10` factor-two and factor-four escape domains;
2. prove every path eventually enters an exact or near-exact basin;
3. prove every non-basin scale word admits a repayment parsing;
4. extend the Bellman potential by a contamination reserve dominating all children;
5. charge imported prefixes through difference export or overlap packing;
6. classify valid exact `S_10` children with `k>=L_{10}/2`;
7. construct a finite-state or spectral quotient of the pre-basin continuation tree.

No current theorem closes this gap. The full Erdős problem remains unresolved.
