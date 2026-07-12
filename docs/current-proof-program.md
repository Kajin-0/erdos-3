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

```math
\sum_{n\in A}\frac1n=\infty
\quad\Longleftrightarrow\quad
\sum_j\alpha_j=\infty
```

up to absolute constants.

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

through `S_5`, with

```math
W_1=\frac38,
\qquad
W_5=\frac{273}{256},
\qquad
\frac{W_5}{W_1}=\frac{91}{32}.
```

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

Therefore universal local contraction, universal two-generation recovery, and contraction over every four- or six-generation window are false. Recovery is path-dependent.

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

## 5. Exact-tail pattern theorems

For the certified exact-tail geometry, every new four-term progression in three translates comes from either:

1. a three-term progression completed at the separation `R`; or
2. the half-separation point `R/2` lying in the state.

For `R=2L+k`, completion descent maps a child target offset `c` to the parent offset

```math
c-3k.
```

Exact rational enumeration gives the unique scheduled descent layer pattern `012`. The same nine top-layer patterns remain complete across:

1. the generic small-offset basin;
2. the half-scale basin;
3. the full fitting exact range of `S_10` and its finite scheduled descendants;
4. the two `+1` repair regions used in the complete exact-child fan.

---

## 6. Exact-tail basin progression

### 6.1 Generic small-offset basin

For

```math
\min S=L,
\qquad
S\subseteq[L,7L/4),
```

with `0<k<=L/32`, even `v_2(k)`, and a valid first exact step at `R=2L+k`, the recurrence

```math
L_{n+1}=8L_n,
\qquad
k_{n+1}=4k_n
```

defines an infinite exact four-term-progression-free tail.

### 6.2 Half-scale basin

The generic entry range enlarges to

```math
\boxed{0<k<L/2.}
```

The first child enters a region from which

```math
S_n\subseteq[L_n,15L_n/8),
\qquad
k_n/L_n<1/4
```

is invariant.

### 6.3 Full-fitting scheduled basin at `S_10`

Across the full fitting exact range

```math
1\le k\le613454687,
```

only two additional scheduled half tests occur:

```math
2k\notin S_{10},
```

and

```math
8(k-L_{10})\notin S_{10}.
```

Exactly `408767151` valid exact children pass the unmodified schedule. The failing valid classes are:

```text
88606 second-step failures
2 third-step failures.
```

### 6.4 Complete exact-child fan

Every second-step failure is repaired by replacing

```math
4k
```

with

```math
4k+1.
```

The repaired offset is odd, so its half obstruction disappears. Exact rational enumeration finds no feasible completion pattern for the perturbed target, and the repaired branch enters the invariant basin after one additional exact step.

The two third-step failures

```text
603979776
613416960
```

are repaired by replacing

```math
16k
```

with

```math
16k+1.
```

The same odd-offset and no-completion argument applies.

Thus

```math
\boxed{
408767151+88606+2
=
408855759.
}
```

This equals the complete number of valid positive exact factor-eight children of `S_10`. Therefore

```math
\boxed{
\text{every valid exact factor-eight child of }S_{10}
\text{ has an infinite exact tail.}
}
```

For entry size `N`, replay multiplicity `P`, and scale `L`, every tail has terminal charge

```math
\boxed{
\sum_{n\ge0}W_n=\frac{4P(N+1)}L.
}
```

At `S_10`, every tail has charge

```math
\boxed{33215/16384.}
```

**Primary references:**

- `docs/half-scale-exact-tail-basin.md`;
- `docs/full-fitting-exact-tail-basin.md`;
- `docs/complete-exact-child-tail-fan.md`;
- `src/verify_complete_exact_child_tail_fan.py`.

---

## 7. Complete exact factor-eight classification at `S_10`

Write every fitting exact separation as

```math
R=2L_{10}+k,
\qquad
1\le k\le613454687.
```

There are `408969792` sponsor-compatible positive offsets. The first-step obstruction split is

```text
completion-blocked:       54999
half-separation-blocked:  59034
overlap:                       0
```

so

```math
\boxed{408855759}
```

offsets give valid exact factor-eight children.

The complete tail-fan theorem now assigns an explicit infinite summable continuation to every valid child:

```text
standard x4 schedule        408767151
second-step +1 repair           88606
third-step +1 repair                 2
```

The exact factor-eight branch from `S_10` is therefore completely classified both at the first step and in long-run continuation behavior.

---

## 8. Bellman potential and debt

For constant exact scale factor `c>6`,

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

The exact `S_10` layer-disjoint cheap candidate domains are:

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

These are domain certificates only. Complete exclusion or construction of a cheap escape remains open.

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
    -> repayment parsing or exact-tail entry
    -> finite terminal charge.
```

The exact factor-eight fan from `S_10` is completely closed. Equivalent remaining tasks are:

1. classify the exact `S_10` factor-two and factor-four escape domains;
2. prove every path eventually enters an exact or near-exact basin;
3. prove every non-basin scale word admits a repayment parsing;
4. extend the Bellman potential by a contamination reserve dominating all children;
5. charge imported prefixes through difference export or overlap packing;
6. construct a finite-state or spectral quotient of the pre-basin continuation tree.

No current theorem closes this gap. The full Erdős problem remains unresolved.
