# Current proof program: Bellman debt and whole-tree compensation

## Status

This is the authoritative overview of the active program for Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A}1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. This repository studies the four-term case. The theorem-style claims below are proved internally or computationally certified as stated, but await independent expert review.

---

## 1. Foundational recursion

For

```math
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j},
```

```math
\sum_{n\in A}\frac1n=\infty
\quad\Longleftrightarrow\quad
\sum_j\alpha_j=\infty
```

up to constants. A divergent four-term-progression-free candidate must have `alpha_j -> 0` but `sum_j alpha_j = infinity`.

Coordinated side-anchor deletion and the minimum-translation backbone give the one-generation bounds

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

The genealogy is binary. Every recursive child must be resolved into standard dyadic shells.

Every parent creates at most two retained outputs, each at most half its label. Hence, for `p>=1`,

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p,
```

and fixed-history multiplicity obeys center, anchor, predecessor, and antichain compression. These facts control positive moments but do not close reciprocal mass.

---

## 2. Sharp exact model and cardinality obstruction

The aligned-diamond construction has

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h.
```

Thus

```math
P_h\asymp|S_h|^{\log_3 2},
```

which rules out bounded, logarithmic, polylogarithmic, and sufficiently small subpower persistence bounds based only on parent cardinality.

There is a computer-certified infinite exact scale-eight family with

```math
L_h=8^{h+1},
\qquad
P_h=\frac12L_h^{1/3}.
```

A 34-state base-eight automaton and an exact `17238`-state carry search certify that its union has no nontrivial four-term progression.

Inside the exact standard-dyadic equal-translate model,

```math
L'\ge8L,
```

```math
P_h\alpha_h\le C_0\left(\frac34\right)^h,
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

The state `S_5` has no factor-two or factor-four continuation. Its smallest exact recovery enters a contracting branch, but the alternative recovery

```math
R_5=93476
```

admits the factor-four descendant

```math
R_6=230164.
```

This gives

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

Their factor-four domains are exhausted by completion, `1001`, and equal-difference `0011` witnesses:

```text
S7 disjoint domain:      359419
S8 disjoint domain:     4190292
S9 disjoint domain:    39459384
```

The first valid exact continuations are

```math
R_7=2097164,
\qquad
R_8=16777217,
\qquad
R_9=134217729.
```

The finite scale sequence becomes

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

## 5. Infinite exact basin from `S_10`

The top-layer reduction lemma says that, for

```math
S\subseteq[L,7L/4),
\qquad
2L<R\le65L/32,
```

every new four-term progression in three translates comes from either:

1. a three-term progression in `S` completed at `R`; or
2. `R` even with `R/2 in S`.

The small-offset completion-descent lemma states that, for `R=2L+k`, a completion offset `c` in the next state descends to offset

```math
c-3k
```

in the parent.

For the recorded `S_10`, choose

```math
D=262143,
\qquad
k_{10}=262149.
```

The recurrence

```math
L_{h+1}=8L_h,
\qquad
k_{h+1}=4k_h,
\qquad
R_h=2L_h+k_h
```

produces an infinite exact-backbone four-term-progression-free tail.

For `n>=0`,

```math
W_{10+n}=\frac{3^{12+n}-3}{2^{20+2n}},
```

and

```math
\boxed{
\sum_{n\ge0}W_{10+n}=\frac{33215}{16384}.
}
```

---

## 6. General exact-tail basin criterion

A state `(S,L,k,P)` is a basin entry when

```math
S\subseteq[L,7L/4),
\qquad
0<k\le L/32,
```

```math
v_2(k)\equiv0\pmod2,
```

```math
S\cap(L,L+L/8)=\varnothing,
```

and no three-term progression in `S` has missing completion `2L+k`.

Then `L'=8L`, `k'=4k`, and `R=2L+k` define an infinite exact tail. If the entry state has size `N`, replay multiplicity `P`, and scale `L`, its exact terminal charge is

```math
\boxed{
\mathfrak B_8(N,P,L)
=
\sum_{n\ge0}W_n
=
\frac{4P(N+1)}L.
}
```

This is a reusable absorbing-state certificate.

Two completion descents from `S_10` to the certified `S_8` seed prove that every

```math
260799\le k\le1048579
```

with even `v_2(k)` is a basin entry. There are exactly

```math
\boxed{525189}
```

such offsets, giving distinct infinite exact tails with the same terminal charge.

---

## 7. Bellman potential and scale-word debt

For a constant exact scale factor `c>6`, the unique affine future-cost function is

```math
\boxed{
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac{6}{c-2}\right).
}
```

At `c=8`, this is `4P(N+1)/L`.

For an arbitrary disjoint three-translate step with scale factor `c`, define the reference potential

```math
\mathfrak B=\frac{4P(N+1)}L.
```

Its exact one-step Bellman defect is

```math
\boxed{
\mathfrak D_c
=
\mathfrak B-W-\mathfrak B'
=
\frac{P(3N+4)}L
\left(1-\frac8c\right).
}
```

Therefore:

- factor `2` and factor `4` create debt;
- factor `8` is Bellman-neutral;
- factors at least `16` create surplus.

For an `H`-step scale word with product `C_H`,

```math
\boxed{
\frac{\mathfrak B_H}{\mathfrak B_0}
=
\frac{2^H}{C_H}
\frac{3^H(N_0+\tfrac32)-\tfrac12}{N_0+1}.
}
```

The endpoint charge depends only on the scale product, not the order or contamination profile.

Exact repayment consequences:

- one factor `4` plus one factor `8` still expands the endpoint charge;
- one factor `4` plus two factor `8` steps contracts it for `N>=2`;
- one factor `2` plus four factor `8` steps contracts it for `N>=9`.

---

## 8. Repayment parsing criterion

If, from a state size at least `9`, a scale word can be partitioned into consecutive blocks of the forms

```text
[8 or larger]
[one 4 and two 8-equivalents]
[one 2 and four 8-equivalents]
```

with larger factors allowed through the product thresholds, then block-boundary Bellman charge contracts uniformly. The worst exact block factor is

```math
\frac{2551}{2560}<1.
```

Consequently

```math
\sum_hW_h<\infty.
```

This converts whole-path summability into a geometric debt-token matching problem.

---

## 9. Cheap-step geometry

For an anchored state

```math
S\subseteq[L,2L),
\qquad
\min S=L,
```

define top slack

```math
T=2L-\max S.
```

A three-translate step with factor `c` and separation `R` satisfies

```math
\boxed{
T'=T+(c-2)L-2R.
}
```

Thus:

### Factor two

```math
T'=T-2R,
```

and the backbone imports at least

```math
|S\cap[L,2L-R)|
```

prefix points as contamination.

### Factor four

```math
T'=T+2(L-R).
```

The value `R=L` is impossible because it creates `0,R,2R,3R`.

- If `R>L`, top slack decreases by at least `2` and the anchor `R` is contamination.
- If `R<L`, slack is replenished only by importing the prefix
  ```math
  S\cap[L,2L-R)
  ```
  into the backbone.

Every cheap Bellman debt therefore carries a geometric certificate: slack consumption or imported prefix contamination.

---

## 10. Exact `S_10` escape domains

The recursive positive-difference support of `S_10` gives the complete layer-disjoint candidate domains:

### Factor two

```text
maximum R:                   76583775
sponsor-compatible:          51055851
layer-disjoint:              33026376
candidate-list FNV-64:       59cfbc6761c6224d
```

### Factor four

```text
maximum R:                  613454687
sponsor-compatible:         408969792
layer-disjoint:             348012826
candidate-list FNV-64:      ae1d9e1ec77b2dfb
```

The recursive computation reproduces the certified `S_9` domains before advancing to `S_10`.

These are domain counts only. Complete four-term-progression exclusion or construction of an escape candidate remains open.

---

## 11. Current unresolved problem: whole-tree compensation

The active target is

```math
\boxed{
\text{prove that every infinite continuation path has summable total weighted density.}
}
```

The current proof architecture is:

```text
contaminated transient
    -> Bellman debt
    -> slack consumption or prefix contamination
    -> forced repayment parsing or basin entry
    -> finite terminal charge.
```

Equivalent remaining tasks:

1. prove every path eventually enters an exact or near-exact basin;
2. prove every non-basin scale word admits a repayment parsing;
3. extend the Bellman potential by a contamination reserve that dominates all children;
4. charge imported prefixes through difference export or overlap packing;
5. construct a finite-state or spectral quotient of the pre-basin continuation tree;
6. classify the `S_10` factor-two and factor-four escape domains using recursive witness propagation.

**Primary new references:**

- `docs/exact-tail-basin-criterion.md`;
- `docs/depth-ten-exact-tail-basin-fan.md`;
- `docs/exact-tail-bellman-potential.md`;
- `docs/scale-word-bellman-debt.md`;
- `docs/cheap-debt-repayment-parsing.md`;
- `docs/cheap-step-slack-contamination-debt.md`;
- `docs/depth-ten-cheap-candidate-domains.md`.

The full Erdős problem remains unresolved.
