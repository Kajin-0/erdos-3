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

The genealogy is binary. Every recursive child must be resolved into standard dyadic shells.

Every parent creates at most two retained outputs, each at most half its label. Hence, for `p>=1`,

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p.
```

Center, root-anchor, predecessor-anchor, and antichain decompositions compress repeated labels. These tools control positive moments and local multiplicity, but not reciprocal mass by themselves.

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

## 5. Layer-pattern and completion-descent theorems

For a state in the original exact-tail shell geometry, the top-layer reduction says that every new four-term progression in three translates comes from either:

1. a three-term progression completed at the separation `R`; or
2. the half-separation point `R/2` inside the state.

For `R=2L+k`, the completion-descent equation sends a next-state target offset `c` to parent offset

```math
c-3k.
```

Exact rational enumeration proves the unique descent layer pattern is `012` throughout

```math
0<c\le4L.
```

A state-specific rational classification also proves that the same nine top-layer patterns remain the complete pattern list across the entire fitting exact factor-eight range of the recorded `S_10`.

**Primary references:**

- `docs/extended-completion-descent.md`;
- `src/verify_exact_tail_pattern_lemmas.py`.

---

## 6. General exact-tail basin criterion

A state `(S,L,k,P)` is an exact-tail basin entry when

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

Then

```math
L_{n+1}=8L_n,
\qquad
k_{n+1}=4k_n,
\qquad
R_n=2L_n+k_n
```

defines an infinite exact four-term-progression-free tail. If the entry state has size `N`, replay multiplicity `P`, and scale `L`, its exact terminal charge is

```math
\boxed{
\mathfrak B_8(N,P,L)
=
\sum_{n\ge0}W_n
=
\frac{4P(N+1)}L.
}
```

For one explicit `S_10` choice,

```math
k_{10}=262149,
```

and

```math
\sum_{n\ge0}W_{10+n}=\frac{33215}{16384}.
```

---

## 7. Complete small-offset basin fan at `S_10`

The complete signed `S_8` completion set contains

```text
2772873
```

coordinates. Two exact completion descents classify every basin-criterion offset

```math
4\le k\le L_{10}/32=16777216.
```

There are `11184809` values with even `v_2(k)`. Exactly `54999` are blocked by the signed seed completion coordinate

```math
2L_8+(k-6).
```

Therefore

```math
\boxed{11129810}
```

offsets are valid exact-tail basin entries. This is approximately `99.51%` of the sponsor-compatible offsets in the criterion range.

The canonical valid-list hashes are

```text
FNV-64  2a52c71cddac07f5
SHA-256 9cbbd28aab4db0a74d48c4a8eaf95d18b3854e56bd7138123734eaefe5b2d384
```

Each gives a distinct infinite exact tail with terminal charge `33215/16384`.

Nested independent audit subfamilies remain certified:

```text
4..1048579:       644052 valid offsets
260799..1048579:  525189 valid offsets
```

---

## 8. Complete exact factor-eight classification from `S_10`

Write every fitting exact separation as

```math
R=2L_{10}+k.
```

The full positive offset range is

```math
1\le k\le613454687.
```

There are

```text
408969792
```

sponsor-compatible positive offsets.

The complete obstruction classification is:

```text
completion-blocked:       54999
half-separation-blocked:  59034
obstruction overlap:          0
```

The zero offset `k=0` is separately invalid because `R/2=L_10` belongs to `S_10`.

Therefore

```math
\boxed{408855759}
```

positive offsets give valid four-term-progression-free exact factor-eight continuations.

Canonical obstruction-list hashes:

```text
completion SHA-256  b0cdf6b95ee9f17f39560e182b5b1f9c72e6af7fa5b1ef41a51c35a49abdf6ec
half SHA-256        45075ac0f88a7e591bdd6850846831d3d15f63db8016878e35bb0644eb739ca9
union SHA-256       92614cc5ec33add8064ef0aedaf4f8fe758600b30912315bec45aa47d48c6861
```

The `11129810` basin children form a certified infinite-summable subset of these valid exact children. The long-run behavior of the remaining valid exact children is open.

**Primary references:**

- `docs/depth-ten-full-exact-factor-eight-classification.md`;
- `src/verify_depth10_full_exact_factor8_classification.cpp`;
- `data/depth10_full_exact_factor8_classification_certificate_2026-07-12.txt`.

---

## 9. Bellman potential and scale-word debt

For constant exact scale factor `c>6`, the unique affine future-cost function is

```math
\boxed{
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac{6}{c-2}\right).
}
```

At `c=8`, this is `4P(N+1)/L`.

For an arbitrary disjoint three-translate step with scale factor `c`, define

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

Therefore factors `2` and `4` create debt, factor `8` is Bellman-neutral, and factors at least `16` create surplus.

For an `H`-step scale word with product `C_H`,

```math
\boxed{
\frac{\mathfrak B_H}{\mathfrak B_0}
=
\frac{2^H}{C_H}
\frac{3^H(N_0+\tfrac32)-\tfrac12}{N_0+1}.
}
```

Exact repayment consequences:

- one factor `4` plus one factor `8` still expands endpoint charge;
- one factor `4` plus two factor `8` steps contracts it for `N>=2`;
- one factor `2` plus four factor `8` steps contracts it for `N>=9`.

---

## 10. Repayment parsing criterion

If, from state size at least `9`, a scale word can be partitioned into consecutive blocks of the forms

```text
[8 or larger]
[one 4 and two 8-equivalents]
[one 2 and four 8-equivalents]
```

then block-boundary Bellman charge contracts uniformly. The worst exact block factor is

```math
\frac{2551}{2560}<1.
```

Consequently

```math
\sum_hW_h<\infty.
```

This converts whole-path summability into a geometric debt-token matching problem.

---

## 11. Cheap-step geometry

For an anchored state, define top slack

```math
T=2L-\max S.
```

A three-translate step with scale factor `c` and separation `R` satisfies

```math
\boxed{T'=T+(c-2)L-2R.}
```

Consequences:

- factor `2`: strict slack consumption and imported lower-prefix contamination;
- factor `4`, `R>L`: strict slack consumption and anchor contamination;
- factor `4`, `R<L`: slack replenishment only through imported prefix contamination;
- `R=L` is impossible because it creates `0,R,2R,3R`.

Every cheap Bellman debt therefore carries a geometric certificate: slack consumption or imported prefix contamination.

---

## 12. Exact `S_10` cheap escape domains

The recursive positive-difference support gives the complete layer-disjoint candidate domains.

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

These are domain counts only. Complete four-term-progression exclusion or construction of a cheap escape candidate remains open.

---

## 13. Current unresolved problem: whole-tree compensation

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

1. prove every path eventually enters an exact or near-exact basin;
2. prove every non-basin scale word admits a repayment parsing;
3. extend the Bellman potential by a contamination reserve dominating all children;
4. charge imported prefixes through difference export or overlap packing;
5. construct a finite-state or spectral quotient of the pre-basin continuation tree;
6. classify the `S_10` factor-two and factor-four escape domains;
7. classify long-run behavior of valid exact factor-eight children outside the certified basin fan.

The full Erdős problem remains unresolved.
