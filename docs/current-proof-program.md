# Current proof program: Bellman debt and whole-tree compensation

## Status

This is the authoritative overview of the active program for Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A}1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. This repository studies the four-term case. Claims below are proved internally or computationally certified as stated, but await independent expert review.

---

## 1. Foundational recursion

For

```math
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j},
```

one has, up to absolute constants,

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

through `S_5`. With

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

## 4. Recorded branch through `S_10`

The recorded states `S_7`, `S_8`, and `S_9` satisfy

```math
N_{h,2}=N_{h,4}=0.
```

Their factor-four layer-disjoint domains are exhausted by completion, `1001`, and equal-difference `0011` witnesses:

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

For the certified exact-tail shell geometries, every new four-term progression in three translates comes from either:

1. a three-term progression completed at the separation `R`; or
2. the half-separation point `R/2` lying in the state.

For `R=2L+k`, child completion targets descend through the unique layer pattern `012`. The scheduled target `4k` descends exactly to the preceding separation `2L+k`.

These layer statements were verified by exact rational vertex enumeration in all entry, invariant, repair, and full-fitting regions used below.

---

## 6. Complete exact factor-eight fan from `S_10`

Write every fitting exact separation as

```math
R=2L_{10}+k,
\qquad
1\le k\le613454687.
```

There are `408969792` sponsor-compatible positive offsets. The complete first-step obstruction split is

```text
completion-blocked       54999
half-separation-blocked  59034
overlap                       0
```

so

```math
\boxed{408855759}
```

offsets give valid exact factor-eight children.

The unmodified schedule

```math
L_{n+1}=8L_n,
\qquad
k_{n+1}=4k_n
```

already gives infinite exact tails for `408767151` valid children.

The remaining valid children are repaired as follows:

```text
88606 second-step failures:  4k  -> 4k+1
2 third-step failures:       16k -> 16k+1
```

The repaired offsets are odd, so the half-separation obstruction disappears. Exact rational enumeration finds no completion obstruction, and each repaired branch enters the invariant exact-tail basin after one additional exact step.

Therefore

```math
\boxed{
408767151+88606+2
=
408855759.
}
```

Every valid exact factor-eight child of `S_10` has an explicit infinite exact four-term-progression-free continuation. Every tail has total charge

```math
\boxed{
\sum_{n\ge0}W_{10+n}
=
\frac{33215}{16384}.
}
```

**Primary references:**

- `docs/complete-exact-child-tail-fan.md`;
- `src/verify_complete_exact_child_tail_fan.py`;
- `data/complete_exact_child_tail_fan_certificate_2026-07-12.txt`.

---

## 7. Bellman potential and debt

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

For any disjoint three-translate step with scale factor `c`,

```math
\boxed{
\mathfrak D_c
=
\mathfrak B-W-\mathfrak B'
=
\frac{P(3N+4)}L\left(1-\frac8c\right).
}
```

Factors `2` and `4` create debt, factor `8` is Bellman-neutral, and factors at least `16` create surplus.

A path whose scale word can be parsed into blocks

```text
[8 or larger]
[one 4 plus two 8-equivalents]
[one 2 plus four 8-equivalents]
```

has summable weighted density. The worst block-boundary contraction is

```math
\frac{2551}{2560}<1.
```

Universal geometric realizability of this parsing remains open.

---

## 8. Cheap-step geometry

For top slack

```math
T=2L-\max S,
```

a step with scale factor `c` and separation `R` satisfies

```math
\boxed{T'=T+(c-2)L-2R.}
```

Every cheap Bellman debt therefore carries a geometric certificate: strict slack consumption or imported prefix contamination.

---

## 9. Complete factor-two exclusion from `S_10`

The exact depth-ten construction contains a translated anchor copy of the preceding state:

```math
\boxed{
L_{10}+(\{0\}\cup S_9)
\subseteq
S_{10}.
}
```

Therefore, for every separation `R`,

```math
L_{10}+G_9(R)\subseteq G_{10}(R),
```

where

```math
G_h(R)=(\{0\}\cup S_h)+\{0,R,2R\}.
```

The factor-four fit endpoint from `S_9` is

```math
76583776,
```

while the factor-two fit endpoint from `S_10` is

```math
76583775.
```

Hence every sponsor-compatible layer-disjoint factor-two candidate from `S_10` lies in the already exhausted factor-four domain of `S_9`. Since

```math
N_{9,4}=0,
```

every such progression lifts by translation into the `S_10` candidate. Thus

```math
\boxed{N_{10,2}=0.}
```

This removes the factor-two Bellman debt token from the continuation tree rooted at the recorded `S_10`.

**Primary references:**

- `docs/depth-ten-factor-two-inheritance-exclusion.md`;
- `src/verify_depth10_factor2_inheritance.py`;
- `data/depth10_factor2_inheritance_certificate_2026-07-12.txt`.

---

## 10. Remaining factor-four escape domain from `S_10`

The complete factor-four domain certificate gives

```text
maximum R:            613454687
sponsor-compatible:   408969792
layer-disjoint:       348012826
FNV-64:               ae1d9e1ec77b2dfb
```

The inherited interval

```math
R\le76583775
```

contains exactly the `33026376` layer-disjoint factor-two candidates and is now completely excluded by the theorem above. The endpoint `R=76583776` has odd two-adic valuation and is not sponsor-compatible.

Therefore the genuinely new factor-four domain has

```math
\boxed{
348012826-33026376
=
314986450
}
```

layer-disjoint candidates.

Initial exact probes throughout this new range have all produced four-term progressions. The observed witnesses include completion, `1001`, `2002`, and predominantly equal-difference `0011` rectangles. These probes are evidence only; they are not yet a complete certificate.

The immediate finite target is:

```math
\boxed{
\text{classify all }314986450\text{ genuinely new factor-four candidates from }S_{10}.
}
```

Either outcome is useful:

1. a surviving candidate gives an explicit cheap descendant to analyze;
2. complete exclusion proves every nonterminating continuation from `S_10` has scale factor at least `8`, and therefore enters the already classified exact or surplus regimes.

---

## 11. Current unresolved problem: whole-tree compensation

The active theorem target is

```math
\boxed{
\text{every infinite continuation path has summable total weighted density.}
}
```

The current architecture is

```text
contaminated transient
    -> exact Bellman debt
    -> slack consumption or prefix contamination
    -> repayment parsing or exact-tail entry
    -> finite terminal charge.
```

Equivalent remaining tasks:

1. classify the `S_10` factor-four escape domain;
2. prove every path eventually enters an exact or near-exact basin;
3. prove every non-basin scale word admits a debt-repayment parsing;
4. extend the Bellman potential by a contamination reserve dominating all children;
5. charge imported prefixes through difference export or overlap packing;
6. construct a finite-state or spectral quotient of the pre-basin continuation tree.

No current theorem closes this gap. The full Erdős problem remains unresolved.
