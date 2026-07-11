# Current proof program: deletion DAG and binary sixteen-ninths recursion

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

Then

```math
\sum_{n\in A}\frac1n=\infty
\quad\Longleftrightarrow\quad
\sum_j\alpha_j=\infty
```

up to absolute constant factors.

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

Adding the two structural families gives the exact balance

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

# 7. Structural load per parent

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

For each deleted sponsor `a`, define

```math
\ell(a)\in\{0,1,2,3\}
```

to be its structural load. If `r` structural occurrences are associated with residual vertices, then

```math
0\le r\le s
```

and

```math
\boxed{
\sum_{a\text{ deleted}}\ell(a)=2K-r.
}
```

---

# 8. Color-aware binary sixteen-ninths theorem

Give each deleted sponsor the color

```math
c(a)
=
\chi(q_a)
=
v_2(q_a)-v_3(q_a)\pmod3.
```

For a candidate chosen color `c`:

- if `c(a)=c`, retain the middle occurrence of value `q_a` and one structural occurrence when available;
- if `c(a) ne c`, retain up to two structural occurrences;
- retain all residual structural occurrences.

Every parent creates at most two retained child occurrences.

A middle label satisfies

```math
q_a\le N/2,
```

so its harmonic contribution is at least `2/N`. A structural label is below `N`, so its contribution is at least `1/N`.

For a deleted sponsor of structural load `ell`, averaging its normalized contribution over the three possible chosen colors gives

```math
g(\ell)
=
\frac{2+1_{\ell\ge1}+2\min\{\ell,2\}}3.
```

Thus

```math
\begin{array}{c|cccc}
\ell&0&1&2&3\\
\hline
g(\ell)&\frac23&\frac53&\frac73&\frac73
\end{array}
```

and for every `ell in {0,1,2,3}`,

```math
\boxed{
g(\ell)\ge\frac23+\frac59\ell.}
```

Using

```math
\sum_a\ell(a)=2K-r,
```

the average normalized contribution from deleted sponsors is at least

```math
\frac23K+
\frac59(2K-r)
=
\frac{16}{9}K-
\frac59r.
```

Adding the `r` residual occurrences gives

```math
\frac{16}{9}K+
\frac49r
\ge
\frac{16}{9}K.
```

Therefore some color gives a binary child family satisfying

```math
\boxed{
\sum H(\text{retained child occurrences})
\ge
\frac{16K}{9N}.
}
```

Since `K=|D|-s`, `s<=r_3(N)`, and `H(D)<=|D|/N`,

```math
\boxed{
\sum H(\text{retained child occurrences})
\ge
\frac{16}{9}H(D)
-
\frac{16}{9}\frac{r_3(N)}N.
}
```

This is the current best binary occurrence theorem. It supersedes the previous factors `7/6` and `4/3`.

**Critical qualification:** the inequality counts harmonic mass with multiplicity.

**Status:** proved in repository; medium confidence pending independent review.

Primary note:

- `docs/color-aware-binary-sixteen-ninths-recursion.md`

---

# 9. Root-depth dichotomy

The unthinned merge estimate contains the root term `rho/N`.

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

If roots are sparse, binary reachability forces a directed path of length

```math
L
\ge
\left\lceil
\log_2\left(\frac{|D|}{\rho}+1\right)
\right\rceil-1.
```

Along such a path,

```math
x_{j+1}-x_j
=
\sigma(q_j)c_jq_j,
\qquad
c_j\in\{1,2\},
```

where `sigma(q_j)` is determined by `v_2(q_j) mod 2`.

**Current role:** supporting structural dichotomy, not part of the shortest proof of the `16/9` theorem.

Primary note:

- `docs/deletion-dag-root-depth-dichotomy.md`

---

# 10. Supporting local packing theory

The coordinated side-middle analysis proves the scale-compensated inequality

```math
|A(S)\cup M_q(T)|
+
R H(T\cap[1,R))
\ge
2+
\frac43(|S|+|T|)-\eta.
```

This says efficient local overlap exports capacity to a lower scale.

**Current role:** possible ingredient in a future multiplicity potential; not part of the shortest deletion-DAG chain.

Primary notes:

- `docs/full-component-scale-export.md`
- `docs/unequal-cardinality-scale-compensated-packing.md`

---

# 11. Explicitly false or superseded targets

The following statements must not be used:

1. **Uniformly bounded depth-two affine-lift overlap:** false by explicit construction.
2. **Universal uncorrected local `8/3` packing:** false by an explicit coordinated 4AP-free example.
3. **Naive recursive density increment:** false in the inherited three-dilate class.
4. **Creation of genuine off-diagonal discrepancy by fixed-size sampling:** false; sampling only scales the existing off-diagonal quantity.

The following valid statements are quantitatively superseded:

- binary `7/6` merge-plus-middle thinning;
- binary `4/3` spanning-forest thinning.

They remain documented as intermediate results.

---

# 12. Dependency graph

```text
Dyadic harmonic reduction
        |
        v
Side-anchor 3AP deletion
        |
        v
Affine deletion DAG
        |
        +--------------------+
        |                    |
        v                    v
merge differences      spanning-forest translations
        |                    |
        +---------+----------+
                  |
                  v
       exact structural count: 2K
                  |
                  v
       color-aware binary allocation
                  |
                  v
        16/9 occurrence branching
                  |
                  v
OPEN: multiplicity-versus-scale control
```

---

# 13. Central unresolved gap

The project controls the occurrence-multiset quantity

```math
\sum_d\frac{m(d)}d,
```

where `m(d)` is the number of descendant occurrences of the value `d`.

The original problem concerns distinct mass

```math
\sum_{d:m(d)>0}\frac1d.
```

No current theorem converts the `16/9` occurrence branching into growth of distinct integers.

The approved closing targets are:

## Target A: weighted multiplicity

Prove a bound whose effective exponential multiplicity rate is strictly below

```math
16/9.
```

## Target B: bounded multiscale potential

Construct a potential that:

1. grows under the retained recursion by a factor greater than one above the Roth-error scale;
2. is uniformly bounded by root data after accounting for lower-scale credits.

## Target C: extremal structural-load obstruction

The abstract averaging bound is sharp for the load distribution

```math
\ell=0
```

on one third of deleted sponsors and

```math
\ell=3
```

on two thirds, with no residual structural occurrences.

Determine whether this pattern can occur at large scale in a genuine four-term-progression-free side-anchor deletion DAG. A quantitative exclusion would improve the binary factor.

## Target D: aggressive falsification

Search computationally for examples with simultaneously:

- high descendant multiplicity;
- rapid scale contraction;
- low distinct harmonic gain;
- persistence over several recursive generations.

Further theory notes must directly prove or falsify one of these targets.