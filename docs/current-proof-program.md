# Current proof program: deletion DAG and binary eight-thirds recursion

## Purpose and status

This is the authoritative overview of the active mathematical program for Erdős Problem #3.

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. The current project focuses on the four-term-progression-free case and seeks to prove that every such set has convergent reciprocal sum.

This document:

1. states the active theorem chain in dependency order;
2. separates proved-in-repository lemmas from computational checks, false targets, and open gaps;
3. identifies the current best quantitative recursion;
4. prohibits new proof languages unless they directly prove or falsify an explicit closing target.

All recent theorem-style statements below are **proved in the repository but not independently audited**, unless stated otherwise.

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

**Status:** standard reduction; high confidence.

---

# 2. Side-anchor deletion

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

and delete its coordinated side anchor:

```math
\begin{cases}
y,&v_2(q)\equiv0\pmod2,\\
y+2q,&v_2(q)\equiv1\pmod2.
\end{cases}
```

Stop when the residual set is three-term-progression-free. Let

```math
K=|D|-s
```

be the number of deletions. Then

```math
s\le r_3(N),
\qquad
q_i\le N/2
```

for every selected progression.

**Status:** proved in repository; medium-high confidence pending external audit.

Primary notes:

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

where `a_i` is deleted while `b_i,c_i` remain. Add edges

```math
a_i\to b_i,
\qquad
a_i\to c_i.
```

Deletion time increases along every edge, so the graph is acyclic. Every deleted vertex has outdegree two; every residual vertex has outdegree zero.

Let

```math
\rho
```

be the number of indegree-zero vertices.

**Status:** proved in repository; medium-high confidence pending external audit.

Primary note:

- `docs/side-anchor-deletion-dag.md`

---

# 4. Exact indegree excess

Define

```math
M
=
\sum_v\max\{d^-(v)-1,0\}.
```

The DAG has `2K` edges and `K+s` vertices. Exactly `K+s-rho` vertices have positive indegree, so

```math
\boxed{M=K-s+\rho.}
```

This is an exact identity.

**Status:** proved in repository; high internal confidence.

---

# 5. Merge-difference children

For each target vertex `v`, let

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

Then:

```math
\Delta_v\subseteq[1,N),
```

`Delta_v` is four-term-progression-free, and

```math
\boxed{
\sum_v|\Delta_v|=K-s+\rho.
}
```

Consequently,

```math
\sum_vH(\Delta_v)
\ge
\frac{K-s+\rho}{N}.
```

**Status:** proved in repository; central lemma; medium confidence pending independent review.

Primary note:

- `docs/deletion-dag-merge-difference-recursion.md`

---

# 6. Spanning-forest component children

Choose one incoming edge for every nonroot DAG vertex. The chosen edges form a spanning forest with components

```math
C_1,\ldots,C_\rho.
```

For each component, put

```math
m_j=\min C_j
```

and define

```math
\Theta_j
=
\{x-m_j:x\in C_j,\ x>m_j\}.
```

Then:

```math
\Theta_j\subseteq[1,N),
```

`Theta_j` is four-term-progression-free, and

```math
\boxed{
\sum_j|\Theta_j|=|D|-\rho=K+s-\rho.
}
```

Adding the two structural families gives

```math
\boxed{
\sum_j|\Theta_j|
+
\sum_v|\Delta_v|
=2K.
}
```

The residual term `s` and root term `rho` cancel.

**Status:** proved in repository; medium confidence pending independent review.

Primary note:

- `docs/spanning-forest-binary-four-thirds-recursion.md`

---

# 7. Structural thinning

Associate each component occurrence

```math
x-m_j
```

with `x`, and each merge occurrence

```math
a-p_v
```

with its nonminimal sponsor `a`.

A residual parent carries at most one structural occurrence. A deleted sponsor carries at most:

1. one component occurrence;
2. two merge occurrences, one for each outgoing DAG edge.

If `r` structural occurrences are associated with residual vertices, then the deleted sponsors carry `2K-r` structural occurrences. Since each deleted sponsor carries at most three, at least

```math
\frac{2K-r}{3}
```

deleted sponsors carry one or more structural occurrences.

Retain one structural occurrence from each such sponsor and retain all `r` residual occurrences. Then

```math
\boxed{
\#\{\text{retained structural occurrences}\}
\ge
\frac{2K}{3}.
}
```

Every retained structural label is below `N`, so

```math
\boxed{
\sum H(\text{retained structural children})
\ge
\frac{2K}{3N}.
}
```

Each parent element is now associated with at most one retained structural occurrence.

**Status:** proved in repository; medium confidence pending independent review.

---

# 8. Full middle children

For every center `x`, define

```math
M_x
=
\{q_i:b_i=x\}.
```

A center and positive step determine one progression uniquely, so there is no duplication inside a fixed `M_x`.

If

```math
q,
\quad q+r,
\quad q+2r,
\quad q+3r
```

were contained in `M_x`, then

```math
x+q,
\quad x+q+r,
\quad x+q+2r,
\quad x+q+3r
```

would form a four-term progression in `D`. Hence

```math
\boxed{M_x\text{ is four-term-progression-free}.}
```

Every selected step satisfies `q_i<=N/2`, and every selected progression contributes exactly one middle occurrence. Therefore

```math
\boxed{
\sum_xH(M_x)
=
\sum_{i=1}^{K}\frac1{q_i}
\ge
\frac{2K}{N}.
}
```

The valuation-color restriction used in the older side-middle packing program is unnecessary here. Recursive descent only requires the child itself to be four-term-progression-free and lower scale; it does not require pairwise-disjoint first three dilates.

**Status:** proved in repository; central new simplification; medium confidence pending independent review.

Primary note:

- `docs/full-middle-binary-eight-thirds-recursion.md`

---

# 9. Binary eight-thirds theorem

Retain:

1. every sponsored middle occurrence;
2. at most one structural occurrence associated with each parent element.

A deleted sponsor creates exactly one middle occurrence and at most one retained structural occurrence. A residual parent creates no middle occurrence and at most one structural occurrence. Therefore

```math
\boxed{
\text{every parent element creates at most two retained child occurrences.}
}
```

Combining the structural and middle estimates gives

```math
\sum H(\text{retained child occurrences})
\ge
\frac{2K}{3N}
+
\frac{2K}{N}
=
\frac{8K}{3N}.
```

Since `K=|D|-s`, `s<=r_3(N)`, and `H(D)<=|D|/N`,

```math
\boxed{
\sum H(\text{retained child occurrences})
\ge
\frac83H(D)
-
\frac83\frac{r_3(N)}N.
}
```

This is the current best binary occurrence theorem. It supersedes the previous factors `7/6`, `4/3`, and `16/9`.

**Critical qualification:** the inequality counts harmonic mass with multiplicity.

**Status:** proved in repository; medium confidence pending independent review.

Primary note:

- `docs/full-middle-binary-eight-thirds-recursion.md`

---

# 10. Supporting local packing and path theory

The repository also proves:

1. a root-rich versus long valuation-directed path dichotomy;
2. a scale-compensated side-middle packing inequality;
3. finite component classifications explaining local overlap;
4. exact counterexamples to bounded affine-lift overlap and uncorrected local `8/3` packing.

These remain supporting results. They are not needed for the shortest proof of the binary `8/3` occurrence theorem.

---

# 11. Explicitly false or superseded targets

The following statements must not be used:

1. **Uniformly bounded depth-two affine-lift overlap:** false by explicit construction.
2. **Universal uncorrected local `8/3` packing:** false by an explicit coordinated 4AP-free example.
3. **Naive recursive density increment:** false in the inherited three-dilate class.
4. **Fixed-size sampling creates genuine off-diagonal discrepancy:** false.

The following quantitative results remain valid but are superseded:

```math
\frac76,
\qquad
\frac43,
\qquad
\frac{16}{9}.
```

Their proof ideas remain documented because the structural balance and allocation arguments feed the current theorem.

---

# 12. Dependency graph

```text
Dyadic harmonic reduction
        |
        v
Side-anchor deletion
        |
        v
Affine deletion DAG
        |
        +-------------------------+
        |                         |
        v                         v
Merge-difference children   spanning-forest children
        |                         |
        +------------+------------+
                     |
                     v
          structural balance = 2K
                     |
                     v
       one structural child per parent
                     |
                     +----------------------+
                     |                      |
                     v                      v
          structural mass >= 2K/3N   full middle mass >= 2K/N
                     |                      |
                     +----------+-----------+
                                |
                                v
                 binary occurrence factor 8/3
                                |
                                v
              OPEN: multiplicity versus contraction
```

---

# 13. Central unresolved gap

The project controls harmonic mass with multiplicity:

```math
\sum_d\frac{m(d)}d,
```

where `m(d)` is the number of descendant occurrences of numerical value `d`.

The original problem concerns distinct mass:

```math
\sum_{d:m(d)>0}\frac1d.
```

The missing theorem must control the interaction among

```math
\boxed{
\text{multiplicity},
\quad
\text{scale contraction},
\quad
\text{genealogical overlap}.
}
```

Because the genealogy is binary, raw occurrence count grows at most like `2^h`, already below `(8/3)^h`. The remaining issue is that reciprocal weight increases when labels contract.

No current result converts the supercritical occurrence inequality into supercritical growth of distinct integers.

---

# 14. Approved closing targets

Further theory work must directly prove or falsify at least one of the following.

## Target A: weighted multiplicity

Prove an effective bound whose exponential rate is strictly below `8/3`, for example

```math
\sum_d\frac{m_h(d)}d
\le
C^h\,\Psi(D_0),
\qquad
C<\frac83.
```

## Target B: bounded multiscale potential

Construct a potential `Phi` that grows under the binary recursion but remains bounded by root data.

## Target C: repeated-label energy

Control an energy such as

```math
E_h
=
\sum_d\frac{m_h(d)^2}{d}
```

strongly enough to transfer occurrence mass to distinct mass.

## Target D: contraction stopping theorem

Show that repeated rapid label contraction forces either distinct lower-scale mass or a forbidden additive configuration.

## Target E: computational falsification

Search for multigeneration examples simultaneously exhibiting:

- high repeated-label multiplicity;
- rapid scale contraction;
- low distinct harmonic gain;
- sustained binary branching.

A scalable family would damage the route. Failure to find one would identify the most plausible closing theorem.

---

# 15. Research gate

Do not create a new standalone proof language merely to rename the final gap.

A new theorem note is justified only if it:

1. proves one approved closing target;
2. disproves one approved closing target with an explicit counterexample;
3. materially improves the audited theorem chain;
4. supplies a reproducible computation testing the current route.

The full Erdős problem remains unresolved.