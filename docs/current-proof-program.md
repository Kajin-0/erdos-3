# Current proof program: deletion DAG and merge-difference recursion

## Purpose and status

This is the authoritative overview of the active mathematical program for Erdős Problem #3.

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. The current project focuses on the case of a four-term-progression-free set and seeks to prove that its reciprocal sum must converge.

This document has four purposes:

1. state the active definitions and theorem chain in dependency order;
2. separate proved-in-repository lemmas from computational checks, heuristics, false targets, and open gaps;
3. identify which older notes are supporting, superseded, or falsified;
4. prevent further theory expansion unless it directly proves or falsifies a stated closing target.

All recent theorem-style claims below should be regarded as **proved in the repository but not yet independently audited**, unless a stronger status is stated.

---

# 1. Global reduction

Let

```math
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j}.
```

For every `n in A_j`,

```math
2^{-j-1}<\frac1n\le2^{-j}.
```

Hence

```math
\sum_{n\in A}\frac1n=\infty
\quad\Longleftrightarrow\quad
\sum_j\alpha_j=\infty
```

up to absolute constant factors.

A four-term-progression-free divergent set must therefore have

```math
\alpha_j\to0,
\qquad
\sum_j\alpha_j=\infty.
```

The project seeks a cross-scale mechanism showing that such slowly divergent dyadic mass cannot remain four-term-progression-free.

**Status:** standard reduction; high confidence.

---

# 2. Side-anchor deletion inside one dyadic block

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

Stop when the residual set is three-term-progression-free.

Write

```math
K=|D|-s
```

for the number of deletions, where

```math
s\le r_3(N).
```

The chosen common differences satisfy

```math
q\le N/2.
```

The selected weighted step load therefore obeys

```math
\mathcal L_*(D)
=
\sum_{i=1}^K\frac1{q_i}
\ge
\frac{2K}{N}.
```

**Dependencies:** quantitative Roth only through the residual bound `s<=r_3(N)`.

**Status:** proved in repository; medium-high confidence pending external audit.

Primary notes:

- `docs/sponsored-three-ap-binary-recursion.md`
- `docs/side-anchor-sponsored-middle-recursion.md`
- `docs/side-anchor-deletion-dag.md`

---

# 3. Affine deletion DAG

For each selected progression write

```math
(a_i,b_i,c_i),
\qquad
a_i+c_i=2b_i,
```

where `a_i` is the deleted side anchor and `b_i,c_i` remain at the moment of deletion.

Add directed edges

```math
a_i\longrightarrow b_i,
\qquad
a_i\longrightarrow c_i.
```

Deletion time strictly increases along every edge, so the graph is acyclic.

Each deleted vertex has outdegree exactly two. Each residual vertex has outdegree zero. Therefore the DAG has

```math
2K
```

directed edges on

```math
K+s=|D|
```

vertices.

Let

```math
\rho
```

be the number of indegree-zero vertices.

**Status:** proved in repository; medium-high confidence pending external audit.

Primary note:

- `docs/side-anchor-deletion-dag.md`

---

# 4. Exact indegree-excess identity

Let `d^-(v)` denote indegree and define

```math
M
=
\sum_v\max\{d^-(v)-1,0\}.
```

Since

```math
\sum_vd^-(v)=2K
```

and exactly `K+s-rho` vertices have positive indegree,

```math
\boxed{M=K-s+\rho.}
```

Equivalently,

```math
M=|D|-2s+\rho.
```

This is an exact identity, not an asymptotic estimate.

**Status:** proved in repository; high internal confidence.

Primary note:

- `docs/deletion-dag-merge-difference-recursion.md`

---

# 5. Merge-difference children

For a vertex `v`, define its incoming sponsor set

```math
I_v=\{a_i:a_i\to v\}.
```

When `I_v` is nonempty, put

```math
p_v=\min I_v
```

and

```math
\Delta_v
=
\{a-p_v:a\in I_v,\ a>p_v\}.
```

Then

```math
|\Delta_v|=d^-(v)-1,
```

so

```math
\boxed{
\sum_v|\Delta_v|=M=K-s+\rho.
}
```

Because all sponsors lie in `[N,2N)`,

```math
\Delta_v\subseteq[1,N).
```

Each `Delta_v` is four-term-progression-free: translating a four-term progression in `Delta_v` by `p_v` would produce one among the incoming sponsors in `D`.

Every element of `Delta_v` is below `N`, so

```math
\sum_vH(\Delta_v)
\ge
\frac{K-s+\rho}{N}
=
\frac{|D|-2s+\rho}{N}.
```

Consequently,

```math
\boxed{
\sum_vH(\Delta_v)
\ge
H(D)-2\frac{r_3(N)}N.
}
```

Thus the merge-difference children preserve the parent harmonic mass, with multiplicity, up to the summable Roth error.

**Status:** proved in repository; central current lemma; medium confidence pending independent review.

Primary note:

- `docs/deletion-dag-merge-difference-recursion.md`

---

# 6. Selected middle children

Partition the selected steps by

```math
\chi(q)=v_2(q)-v_3(q)\pmod3.
```

Choose the color carrying maximal selected reciprocal load. Group the selected steps of that color by their middle point.

The resulting middle children `M_x^*` are four-term-progression-free, lie at scale at most `N/2`, and satisfy

```math
\sum_xH(M_x^*)
\ge
\frac13\mathcal L_*(D)
\ge
\frac{2K}{3N}.
```

Combining with the merge-difference family gives

```math
\boxed{
\sum_vH(\Delta_v)
+
\sum_xH(M_x^*)
\ge
\frac53H(D)
-
\frac83\frac{r_3(N)}N.
}
```

This is a supercritical branching inequality for a **multiset of child occurrences**.

**Critical qualification:** it does not imply a `5/3` increase in the harmonic mass of distinct integers.

**Status:** proved in repository; medium confidence pending external audit.

Primary note:

- `docs/deletion-dag-merge-difference-recursion.md`

---

# 7. Binary thinning

A deleted sponsor has two outgoing DAG edges, so it can be nonminimal in at most two incoming-sponsor sets. Retain at most one merge-difference occurrence per sponsor.

At least half the merge cardinality survives. The thinned merge family `Delta_v'`, together with the selected middle family, satisfies

```math
\boxed{
\sum_vH(\Delta_v')
+
\sum_xH(M_x^*)
\ge
\frac76H(D)
-
\frac53\frac{r_3(N)}N.
}
```

Each parent sponsor now creates at most two child occurrences:

1. one thinned merge-difference occurrence;
2. one selected middle occurrence.

This yields a canonical binary occurrence genealogy with a harmonic branching factor greater than one.

**Critical qualification:** rapid label contraction can still support reciprocal-mass growth in a binary occurrence tree.

**Status:** proved in repository; medium confidence pending external audit.

Primary note:

- `docs/deletion-dag-merge-difference-recursion.md`

---

# 8. Root-depth dichotomy

The exact merge estimate contains the root term `rho/N`.

If

```math
\rho\ge\delta|D|,
```

then

```math
\boxed{
\sum_vH(\Delta_v)
\ge
(1+\delta)H(D)
-
2\frac{r_3(N)}N.
}
```

If roots are sparse, every vertex is reachable from a root, while each vertex has outdegree at most two. Therefore the maximum directed path length `L` obeys

```math
\boxed{
L
\ge
\left\lceil
\log_2\left(\frac{|D|}{\rho}+1\right)
\right\rceil-1.
}
```

Along a directed path,

```math
x_{j+1}-x_j
=
\sigma(q_j)c_jq_j,
\qquad
c_j\in\{1,2\},
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

All path vertices remain in `[N,2N)`, so every subpath satisfies

```math
\left|
\sum_{j=u}^{v-1}\sigma(q_j)c_jq_j
\right|<N.
```

Thus a root-poor generation forces a long affine path with valuation-prescribed signs and substantial cancellation.

**Status:** proved in repository; medium confidence pending external audit.

Primary note:

- `docs/deletion-dag-root-depth-dichotomy.md`

---

# 9. Supporting local packing theory

A separate line of work analyzes overlap between a coordinated side child and its paired middle child.

The strongest consolidated statement is the unequal-cardinality scale-compensated inequality. For

```math
S\subseteq[R,2R)
```

and an arbitrary paired middle subset `T`, one has

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

When `T subseteq [R,2R)`, the correction vanishes:

```math
\boxed{
|A(S)\cup M_q(T)|
\ge
2+
\frac43(|S|+|T|)-\eta.
}
```

This theory proves that local overlap can transfer capacity downward in scale but cannot destroy it.

**Current role:** supporting evidence and a possible ingredient in a future multiplicity potential. It is not currently part of the shortest deletion-DAG proof chain.

**Status:** proved in repository through a finite component classification; medium confidence pending independent audit.

Primary notes:

- `docs/full-component-scale-export.md`
- `docs/unequal-cardinality-scale-compensated-packing.md`
- `docs/component-deficit-potential-reduction.md`
- `docs/three-by-three-component-scale-export.md`

---

# 10. Dependency graph

```text
Dyadic harmonic reduction
        |
        v
Side-anchor 3AP deletion
        |
        v
Affine deletion DAG -----> selected middle children
        |
        v
Exact indegree excess
        |
        v
Merge-difference children
        |
        +-----------------------------+
        |                             |
        v                             v
5/3 occurrence branching       root-depth dichotomy
        |
        v
binary thinning: 7/6
        |
        v
OPEN: multiplicity-versus-scale control
```

The local side-middle packing theory is currently a supporting branch feeding potential future control of the final open step.

---

# 11. Central unresolved gap

The project controls harmonic mass with multiplicity:

```math
\sum_d\frac{m(d)}d,
```

where `m(d)` is the number of descendant occurrences of the numerical value `d`.

The original problem concerns distinct mass:

```math
\sum_{d:m(d)>0}\frac1d.
```

The missing theorem must control the interaction among:

```math
\boxed{
\text{multiplicity},
\quad
\text{scale contraction},
\quad
\text{valuation-directed path geometry}.
}
```

No current repository result converts the supercritical occurrence branching into supercritical growth of distinct integers.

This is the authoritative main gap.

---

# 12. Permitted closing targets

Until one of the following is proved or falsified, no new broad proof language should be introduced.

## Target A: weighted multiplicity inequality

Prove, for the thinned binary recursion, an estimate of the form

```math
\sum_d\frac{m_h(d)}d
\le
C^h
\sum_{d\in D_0}\frac1d
+
\text{summable error},
```

with

```math
C<\frac76.
```

A scale-dependent or stopping-time version is acceptable.

## Target B: bounded global potential

Construct a potential `Phi` on labeled occurrence multisets such that

```math
\Phi(\text{children})
\ge
(1+\delta)\Phi(\text{parent})
-
\text{Roth error}
```

for some `delta>0`, while

```math
\Phi(\text{all descendants})
\le
C\Phi(\text{root})
```

uniformly.

## Target C: root-poor stopping theorem

Prove that a sequence of root-poor generations cannot persist. A sufficient theorem would bound the weighted frequency, length, or scale distribution of paths satisfying

```math
x_{j+1}-x_j
=
\sigma(q_j)c_jq_j,
\qquad
c_j\in\{1,2\}.
```

The theorem must be strong enough to make the accumulated exceptional generations summable.

## Target D: computational falsification

Search for scalable examples simultaneously exhibiting:

1. small root density;
2. long valuation-directed paths;
3. high descendant multiplicity;
4. low distinct harmonic gain.

A scalable family would seriously damage the current route. Small examples should be tested across multiple deletion policies, not only one arbitrary order.

---

# 13. Status of earlier routes

## Retained as foundational or supporting

- dyadic harmonic reduction;
- cross-scale 3AP extension load;
- three-dilate inherited fiber class;
- strict third-dilate expansion and primitive extraction;
- coordinated valuation compression;
- componentwise scale export;
- sponsored sparse recursion;
- deletion DAG and merge-difference recursion.

## Superseded as the active proof language

- pseudo-Boolean and MaxSAT digit-template search;
- DFA and regular-language counterexample search;
- generic affine-tree multiplicity without sponsorship;
- unconsolidated role-tree overlap formulations.

These remain useful computational or historical material but are not the active route to the full problem.

## Explicitly falsified targets

1. **Bounded depth-two affine-lift overlap.**
   Arbitrarily many depth-two lifts can share a root point and terminal direction inside a finite four-term-progression-free set.

2. **Universal uncorrected local `8/3` side-middle packing.**
   A finite coordinated four-term-progression-free example has `|S|=|T|=45` and parent union `107<120`.

3. **Naive recursive density increment.**
   Predecessor children cannot exceed parent normalized density under the primitive dilation constraints.

4. **Sampling creates genuine off-diagonal discrepancy.**
   Fixed-size sampling preserves off-diagonal discrepancy only by the expected combinatorial factor.

These routes should not be revived without a materially new hypothesis.

---

# 14. Verification policy

A new theorem note should be added only when it does at least one of the following:

1. proves or falsifies Target A, B, C, or D;
2. repairs a concrete gap in the dependency chain above;
3. supplies an independently checkable counterexample to a stated lemma;
4. consolidates or externally audits an existing claim.

Every future exact claim should record:

- hypotheses;
- dependencies;
- whether the proof is symbolic, computational, or mixed;
- whether it has been independently reviewed;
- whether it affects the central multiplicity-versus-scale gap.

The project should prefer fewer authoritative documents over many overlapping theorem notes.
