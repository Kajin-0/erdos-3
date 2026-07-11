# Current proof program: deletion DAG and binary four-thirds recursion

## Purpose and status

This is the authoritative overview of the active mathematical program for Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. The current project focuses on proving that every four-term-progression-free set has convergent reciprocal sum.

This document:

1. states the active theorem chain in dependency order;
2. separates proved-in-repository lemmas from standard facts, computations, false targets, and open gaps;
3. identifies the shortest active route;
4. prevents new proof languages unless they prove or falsify an explicit closing target.

All recent theorem-style claims are **proved in the repository but not yet independently audited**, unless stated otherwise.

---

# 1. Global dyadic reduction

Let

```math
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j}.
```

Then, up to absolute constants,

```math
\sum_{n\in A}\frac1n=\infty
\quad\Longleftrightarrow\quad
\sum_j\alpha_j=\infty.
```

A four-term-progression-free divergent set must satisfy

```math
\alpha_j\to0,
\qquad
\sum_j\alpha_j=\infty.
```

The project seeks a cross-scale contradiction for this slowly divergent dyadic mass.

**Status:** standard reduction; high confidence.

---

# 2. Side-anchor deletion inside one block

Fix a finite four-term-progression-free block

```math
D\subseteq[N,2N).
```

Repeatedly choose a nontrivial three-term progression

```math
y,
\qquad y+q,
\qquad y+2q
```

in the current set and delete its coordinated side anchor:

```math
\begin{cases}
y,&v_2(q)\equiv0\pmod2,\\
y+2q,&v_2(q)\equiv1\pmod2.
\end{cases}
```

Stop when the residual set is three-term-progression-free. Write

```math
K=|D|-s
```

for the number of deletions. Quantitative Roth gives

```math
s\le r_3(N).
```

Every selected common difference satisfies

```math
q\le N/2.
```

Hence the selected reciprocal step load

```math
\mathcal L_*(D)=\sum_{i=1}^K\frac1{q_i}
```

obeys

```math
\boxed{\mathcal L_*(D)\ge\frac{2K}{N}.}
```

**Status:** proved in repository; medium-high confidence pending audit.

Primary notes:

- `docs/sponsored-three-ap-binary-recursion.md`
- `docs/side-anchor-sponsored-middle-recursion.md`
- `docs/side-anchor-deletion-dag.md`

---

# 3. Affine deletion DAG

Write each selected progression as

```math
(a_i,b_i,c_i),
\qquad
a_i+c_i=2b_i,
```

where `a_i` is the deleted side anchor. Add edges

```math
a_i\longrightarrow b_i,
\qquad
a_i\longrightarrow c_i.
```

Deletion time increases along every edge, so the graph is acyclic. Every deleted vertex has outdegree two; every residual vertex has outdegree zero.

The DAG has

```math
K+s=|D|
```

vertices and

```math
2K
```

edges. Let

```math
\rho
```

be the number of indegree-zero vertices.

**Status:** proved in repository; medium-high confidence pending audit.

Primary note:

- `docs/side-anchor-deletion-dag.md`

---

# 4. Merge-difference children

Let `d^-(v)` be indegree. The exact indegree excess is

```math
M
=
\sum_v\max\{d^-(v)-1,0\}
=
K-s+\rho.
```

For each vertex `v`, let

```math
I_v=\{a_i:a_i\to v\},
\qquad
p_v=\min I_v,
```

and define

```math
\Delta_v
=
\{a-p_v:a\in I_v,\ a>p_v\}.
```

Then

```math
\Delta_v\subseteq[1,N),
```

`Delta_v` is four-term-progression-free, and

```math
\boxed{
\sum_v|\Delta_v|=K-s+\rho.
}
```

Therefore

```math
\boxed{
\sum_vH(\Delta_v)
\ge
\frac{K-s+\rho}{N}
=
\frac{|D|-2s+\rho}{N}.
}
```

In particular,

```math
\sum_vH(\Delta_v)
\ge
H(D)-2\frac{r_3(N)}N.
```

**Critical qualification:** this is harmonic mass with multiplicity across child states.

**Status:** proved in repository; central lemma; medium confidence pending independent review.

Primary note:

- `docs/deletion-dag-merge-difference-recursion.md`

---

# 5. Spanning-forest component children

Choose one incoming edge for every nonroot vertex of the deletion DAG. The chosen edges form a directed spanning forest with `rho` components

```math
C_1,\ldots,C_\rho.
```

For each component let

```math
m_j=\min C_j
```

and define

```math
\Theta_j
=
\{x-m_j:x\in C_j,\ x>m_j\}.
```

Then

```math
\Theta_j\subseteq[1,N),
```

`Theta_j` is four-term-progression-free, and

```math
\boxed{
\sum_j|\Theta_j|
=|D|-\rho
=K+s-\rho.
}
```

Thus

```math
\boxed{
\sum_jH(\Theta_j)
\ge
\frac{|D|-\rho}{N}.
}
```

**Status:** proved in repository; medium-high confidence pending audit.

Primary note:

- `docs/spanning-forest-binary-four-thirds-recursion.md`

---

# 6. Exact structural balance

The merge and component families are complementary:

```math
\begin{aligned}
\sum_v|\Delta_v|+
\sum_j|\Theta_j|
&=(K-s+\rho)+(K+s-\rho)\\
&=2K.
\end{aligned}
```

Therefore

```math
\boxed{
\sum_vH(\Delta_v)
+
\sum_jH(\Theta_j)
\ge
\frac{2K}{N}.
}
```

The residual term `s` and root term `rho` cancel exactly.

This is the central structural identity behind the current best binary recursion.

---

# 7. Selected middle children

Partition selected steps by

```math
\chi(q)=v_2(q)-v_3(q)\pmod3.
```

Choose the color carrying maximal reciprocal load and group those steps by their middle point. The resulting children `M_x^*` are four-term-progression-free and satisfy

```math
\boxed{
\sum_xH(M_x^*)
\ge
\frac13\mathcal L_*(D)
\ge
\frac{2K}{3N}.
}
```

Each deleted sponsor creates at most one selected middle occurrence.

**Status:** proved in repository; medium confidence pending audit.

Primary notes:

- `docs/sponsored-three-ap-binary-recursion.md`
- `docs/deletion-dag-merge-difference-recursion.md`

---

# 8. Binary four-thirds thinning

Associate each component occurrence `x-m_j` with the parent element `x`. Each parent carries at most one such occurrence.

Associate each merge occurrence `a-p_v` with its nonminimal sponsor `a`. A deleted sponsor has two outgoing DAG edges, so it carries at most two merge occurrences.

Thus:

- a residual parent carries at most one structural occurrence;
- a deleted parent carries at most three structural occurrences: one component occurrence and at most two merge occurrences.

The two structural families contain exactly `2K` occurrences. Selecting at most one structural occurrence per parent retains at least

```math
\frac{2K}{3}
```

structural occurrences. Since every retained structural label is below `N`,

```math
\boxed{
\sum H(\text{retained structural children})
\ge
\frac{2K}{3N}.
}
```

Retain also the selected middle occurrence associated with each sponsor. Every parent now creates at most two child occurrences, and

```math
\boxed{
\sum H(\text{binary children})
\ge
\frac{4K}{3N}.
}
```

Since `K=|D|-s`,

```math
\boxed{
\sum H(\text{binary children})
\ge
\frac43H(D)
-
\frac43\frac{r_3(N)}N.
}
```

This supersedes the previous best binary bound

```math
\frac76H(D)-\frac53\frac{r_3(N)}N.
```

The old `7/6` thinning remains correct but is no longer the active quantitative bound.

**Critical qualification:** the `4/3` theorem still counts numerical labels with multiplicity.

**Status:** proved in repository; current best binary occurrence theorem; medium confidence pending independent audit.

Primary note:

- `docs/spanning-forest-binary-four-thirds-recursion.md`

---

# 9. Supporting root-depth dichotomy

The merge estimate alone contains the root term `rho/N`.

If

```math
\rho\ge\delta|D|,
```

then

```math
\sum_vH(\Delta_v)
\ge
(1+\delta)H(D)
-
2\frac{r_3(N)}N.
```

If roots are sparse, the maximum directed path length satisfies

```math
L
\ge
\left\lceil
\log_2\left(\frac{|D|}{\rho}+1\right)
\right\rceil-1.
```

Along a directed path,

```math
x_{j+1}-x_j
=
\sigma(q_j)c_jq_j,
\qquad c_j\in\{1,2\},
```

where

```math
\sigma(q)
=
\begin{cases}
+1,&v_2(q)\equiv0\pmod2,\\
-1,&v_2(q)\equiv1\pmod2.
\end{cases}
```

This dichotomy is now supporting rather than necessary for obtaining a supercritical binary occurrence factor. It may still help control multiplicity or triple-loaded sponsors.

**Status:** proved in repository; medium confidence pending audit.

Primary note:

- `docs/deletion-dag-root-depth-dichotomy.md`

---

# 10. Supporting local packing theory

For a coordinated side shell

```math
S\subseteq[R,2R)
```

and paired middle subset `T`, the componentwise scale-export theory gives

```math
\boxed{
|A(S)\cup M_q(T)|
+
R H(T\cap[1,R))
\ge
2+
\frac43(|S|+|T|)-\eta,
}
```

where `0<=eta<=2` records anchor coincidences.

When `T subseteq[R,2R)`, the lower-scale correction vanishes.

This shows that efficient local overlap transfers capacity downward in scale. It is supporting theory and is not part of the shortest current proof chain.

Primary notes:

- `docs/full-component-scale-export.md`
- `docs/unequal-cardinality-scale-compensated-packing.md`
- `docs/component-deficit-potential-reduction.md`
- `docs/three-by-three-component-scale-export.md`

---

# 11. Active dependency graph

```text
Dyadic harmonic reduction
        |
        v
Side-anchor 3AP deletion
        |
        v
Affine deletion DAG ----------------> selected middle children
        |
        +-------------------------------+
        |                               |
        v                               v
merge-difference children      spanning-forest children
        |                               |
        +---------------+---------------+
                        |
                        v
             exact structural total 2K
                        |
                        v
          per-parent structural thinning
                        |
                        +---- selected middle occurrence
                        |
                        v
             binary occurrence factor 4/3
                        |
                        v
        OPEN: multiplicity-versus-scale control
```

---

# 12. Central unresolved gap

The recursion controls harmonic mass with multiplicity:

```math
\sum_d\frac{m(d)}d,
```

where `m(d)` is the number of retained descendant occurrences of the numerical label `d`.

The original problem concerns distinct mass:

```math
\sum_{d:m(d)>0}\frac1d.
```

No current result converts the binary `4/3` occurrence branching into supercritical growth of distinct integers.

The missing theorem must control the joint behavior of

```math
\boxed{
\text{multiplicity},
\quad
\text{scale contraction},
\quad
\text{genealogical overlap}.
}
```

---

# 13. Explicit closing targets

New mathematical work must prove or falsify one of the following.

## Target A: weighted multiplicity

Prove an upper bound for the retained binary genealogy whose exponential multiplicity rate is strictly below

```math
\frac43.
```

A representative form is

```math
\sum_d\frac{m_h(d)}d
\le
C\lambda^h
\sum_{d:m_h(d)>0}\frac1d,
\qquad
\lambda<\frac43.
```

## Target B: bounded multiscale potential

Construct a potential `Phi` satisfying both:

```math
\Phi(\text{children})
\ge
(1+\delta)\Phi(\text{parent})
-
\text{summable Roth error},
```

and a uniform upper bound in terms of the root set.

## Target C: triple-loaded sponsor structure

A deleted sponsor may carry all three unthinned structural occurrences:

1. one component occurrence;
2. two merge occurrences.

Prove that such sponsors are sparse, force an additional lower-scale label, or can be thinned more efficiently. Any fixed improvement above the current retained structural fraction `1/3` improves the binary factor beyond `4/3`.

## Target D: aggressive falsification

Search for scalable examples having simultaneously:

- small unique descendant harmonic mass;
- high occurrence multiplicity;
- rapid scale contraction;
- persistence across multiple generations.

A one-generation multiplicity example is not enough if its repeated labels terminate immediately or are compensated by much smaller labels.

---

# 14. Explicitly false or superseded routes

The following cannot be used as originally proposed.

## False: uniformly bounded depth-two lift overlap

A fixed root point and terminal direction can support arbitrarily many depth-two affine lifts inside a four-term-progression-free set.

Primary note:

- `docs/depth-two-overlap-counterexample.md`

## False: universal uncorrected local `8/3` packing

A coordinated four-term-progression-free example has

```math
|S|=|T|=45,
\qquad
|A(S)\cup M_q(T)|=107<120.
```

The corrected theorem requires lower-scale harmonic credit.

Primary note:

- `docs/seven-thirds-local-packing-counterexample.md`

## False: naive recursive density increment

Passing to predecessor children does not automatically increase normalized density.

## False: fixed-size sampling creates off-diagonal discrepancy

Sampling preserves the corrected off-diagonal interaction in expectation; it does not generate the needed discrepancy.

## Superseded as best binary bound: `7/6`

The earlier merge-plus-middle thinning remains valid, but the spanning-forest construction improves the binary occurrence factor to `4/3` with a smaller Roth-error coefficient.

---

# 15. Research discipline

Do not create another standalone theorem note unless it:

1. proves or falsifies Targets A–D;
2. corrects a material error in the active chain; or
3. supplies an independently checkable audit of a central lemma.

Computational work should measure both occurrence and distinct quantities, including

```math
R_{\mathrm{mult}}
=
\frac{\sum H(\text{child occurrences})}{H(D)},
```

```math
R_{\mathrm{unique}}
=
\frac{H(\text{distinct child labels})}{H(D)},
```

multiplicity by scale, residual fraction, and persistence over multiple generations.

The full Erdős problem remains unresolved.
