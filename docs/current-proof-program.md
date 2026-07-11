# Current proof program: deletion DAG, multiplicity resolution, and label potential

## Purpose and status

This is the authoritative overview of the active mathematical program for Erdős Problem #3.

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. The current project focuses on the four-term-progression-free case.

All recent theorem-style statements below are proved in the repository but have not received independent expert review.

---

# 1. Global dyadic reduction

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

A four-term-progression-free divergent set must satisfy

```math
\alpha_j\to0,
\qquad
\sum_j\alpha_j=\infty.
```

**Status:** standard reduction.

---

# 2. Side-anchor deletion and affine DAG

Fix

```math
D\subseteq[N,2N)
```

four-term-progression-free. Repeatedly select a nontrivial three-term progression and delete its coordinated side anchor. Stop when the residual set is three-term-progression-free.

Let

```math
K=|D|-s,
\qquad
s\le r_3(N).
```

Write the selected progressions as

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

Deletion time increases along every edge, so this is a DAG. Every deleted vertex has outdegree two; every residual vertex has outdegree zero.

**Primary note:** `docs/side-anchor-deletion-dag.md`.

---

# 3. Merge-difference children

Let `rho` be the number of indegree-zero vertices. The exact indegree excess is

```math
M
=
\sum_v\max\{d^-(v)-1,0\}
=
K-s+\rho.
```

For each target vertex `v`, let `I_v` be its incoming sponsors, choose `p_v=min I_v`, and define

```math
\Delta_v
=
\{a-p_v:a\in I_v,\ a>p_v\}.
```

Then each `Delta_v` is four-term-progression-free, lies in `[1,N)`, and

```math
\boxed{
\sum_v|\Delta_v|=K-s+\rho.
}
```

**Primary note:** `docs/deletion-dag-merge-difference-recursion.md`.

---

# 4. Spanning-forest component children

Choose one incoming edge for every nonroot DAG vertex. The selected edges form a spanning forest with `rho` components `C_j`.

For each component define

```math
\Theta_j
=
\{x-\min C_j:x\in C_j,\ x>\min C_j\}.
```

Each `Theta_j` is four-term-progression-free, lies in `[1,N)`, and

```math
\boxed{
\sum_j|\Theta_j|=K+s-\rho.
}
```

Hence

```math
\boxed{
\sum_j|\Theta_j|+\sum_v|\Delta_v|=2K.
}
```

The residual and root terms cancel exactly.

**Primary note:** `docs/spanning-forest-binary-four-thirds-recursion.md`.

---

# 5. Structural thinning

Associate each component occurrence with its translated parent and each merge occurrence with its nonminimal sponsor.

- A residual parent carries at most one structural occurrence.
- A deleted sponsor carries at most one component occurrence and at most two merge occurrences.

Retaining at most one structural occurrence per parent preserves at least

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

Each parent now creates at most one retained structural child.

---

# 6. Full middle children and raw occurrence growth

For each center `x`, define

```math
M_x=\{q_i:b_i=x\}.
```

A center and positive step determine one progression uniquely. If four elements of `M_x` formed a four-term progression, then their translated points `x+q` would form one in `D`. Therefore every `M_x` is four-term-progression-free.

Every selected step satisfies `q_i<=N/2`, and every selected progression contributes one middle occurrence. Thus

```math
\boxed{
\sum_xH(M_x)\ge\frac{2K}{N}.
}
```

Retain every middle occurrence and at most one structural occurrence per parent. The genealogy is binary and

```math
\boxed{
\sum H(\text{binary child occurrences})
\ge
\frac83H(D)
-
\frac83\frac{r_3(N)}N.
}
```

This is the strongest raw occurrence theorem.

**Critical qualification:** repeated numerical labels are counted repeatedly.

**Primary note:** `docs/full-middle-binary-eight-thirds-recursion.md`.

---

# 7. Exact middle multiplicity fibers

Let

```math
Q=\{q_i:1\le i\le K\}
```

be the set of distinct selected steps. For each `q in Q`, define its center fiber

```math
X_q=\{b_i:q_i=q\}.
```

Choose `x_q=min X_q` and define

```math
\Xi_q
=
\{x-x_q:x\in X_q,\ x>x_q\}.
```

Each `Xi_q` is four-term-progression-free and lies in `[1,N)`. If `m(q)=|X_q|`, then

```math
|\Xi_q|=m(q)-1.
```

Since `sum_q m(q)=K`,

```math
\boxed{
|Q|+\sum_{q\in Q}|\Xi_q|=K.
}
```

Interpretation:

- retain one terminal distinct copy of each numerical step `q`;
- convert every additional occurrence of `q` into one lower-scale center-difference occurrence.

No within-node middle multiplicity is discarded at the cardinality level.

**Primary note:** `docs/middle-multiplicity-fiber-five-thirds-recursion.md`.

---

# 8. Binary multiplicity-resolving five-thirds theorem

Associate the representative copy of `q` with the sponsor of the progression centered at `x_q`. Associate every `Xi_q` occurrence with the sponsor of its corresponding nonrepresentative progression.

Every deleted sponsor receives exactly one multiplicity-resolved middle output:

- either one terminal distinct step;
- or one recursive `Xi_q` occurrence.

Together with at most one retained structural child, every parent creates at most two outputs.

The representative steps contribute at least `2|Q|/N`. The fiber children contribute at least `(K-|Q|)/N`. Hence

```math
H(Q)+\sum_qH(\Xi_q)
\ge
\frac{K+|Q|}{N}
\ge
\frac KN.
```

Adding the retained structural mass gives

```math
\boxed{
H(Q)
+
\sum_qH(\Xi_q)
+
\sum H(\text{retained structural children})
\ge
\frac53H(D)
-
\frac53\frac{r_3(N)}N.
}
```

This factor is smaller than `8/3`, but the output is more relevant to the original problem:

- `H(Q)` is terminal distinct harmonic mass inside the parent node;
- `Xi_q` recursively records all additional copies;
- structural children carry the deletion-DAG overlap information.

This is the active bridge from occurrence growth toward distinct mass.

**Primary note:** `docs/middle-multiplicity-fiber-five-thirds-recursion.md`.

---

# 9. Half-contraction of every retained output

The coordinated side-anchor orientation depends only on `q`. Therefore there is a sign `sigma(q)` such that every selected progression of step `q` satisfies

```math
b=a+\sigma(q)q.
```

For a fixed repeated step `q`, differences between centers equal differences between sponsors. If `x_q` is the minimum center and `a_q` its sponsor, then a nonrepresentative fiber label satisfies

```math
x-x_q=a-a_q.
```

Since `a_q>=N` and `a<2N`,

```math
0<x-x_q\le a-N\le a/2.
```

The terminal representative step also satisfies

```math
q\le N/2\le a/2.
```

The retained structural labels satisfy the same half-contraction:

```math
x-\min C\le x-N\le x/2,
```

and

```math
a-p_v\le a-N\le a/2.
```

Thus every parent creates at most two outputs, each at most one half of the parent label.

For every real `p>=1`,

```math
\boxed{
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
}
```

**Primary note:** `docs/half-contraction-multiscale-label-potential.md`.

---

# 10. All-generation label-moment potential

Let `E_p(h)` be the total `p`-moment of recursive occurrences at generation `h`, and let `T_p(h)` be the total `p`-moment of terminal outputs created at that generation.

The per-parent half-contraction gives

```math
T_p(h)+E_p(h+1)
\le
2^{1-p}E_p(h).
```

Consequently,

```math
E_p(h)
\le
2^{(1-p)h}E_p(0).
```

Summing over generations gives

```math
\boxed{
\sum_{h\ge0}T_p(h)
\le
2^{1-p}E_p(0)
\qquad(p\ge1).
}
```

For `p=1`,

```math
\boxed{
\sum_{\text{all terminal occurrences }q}q
\le
\sum_{\text{root occurrences }a}a.
}
```

For `p=2`,

```math
\boxed{
\sum_{\text{all terminal occurrences }q}q^2
\le
\frac12
\sum_{\text{root occurrences }a}a^2.
}
```

Every recursive path starting at `a_0` has length at most

```math
\lfloor\log_2 a_0\rfloor.
```

If `mu(q)` denotes total terminal multiplicity across all states and generations, then

```math
\boxed{
\sum_q\mu(q)q^p
\le
2^{1-p}
\sum_{a\text{ root occurrence}}a^p
\qquad(p\ge1).
}
```

This is the first global quantitative control of cross-state multiplicity in the active program.

---

# 11. Current unresolved gap

Positive moments are now globally bounded. Therefore any critical cross-state multiplicity must concentrate near the smallest numerical labels.

The unresolved regime is

```math
\boxed{
\text{small-label concentration}
\quad+
\text{cross-state multiplicity}
\quad+
\text{genealogical overlap}.
}
```

Approved next targets:

1. prove that excessive multiplicity at the bottom scales forces additional distinct labels;
2. build a potential combining reciprocal mass with the positive-moment bounds;
3. prove an additive-energy bound for equal small terminal labels generated by distinct states;
4. computationally search for multigeneration examples concentrating terminal mass near `1`.

The positive-moment theorem does not by itself control

```math
\sum_q\frac{\mu(q)}q,
```

because small labels are inexpensive in every positive moment.

---

# 12. Supporting and superseded results

Supporting results include:

- root-rich versus long valuation-directed path dichotomy;
- componentwise scale-compensated side-middle packing;
- finite component classifications;
- explicit counterexamples to bounded affine-lift overlap and uncorrected local `8/3` packing.

The binary factors

```math
\frac76,
\qquad
\frac43,
\qquad
\frac{16}{9}
```

remain valid but are superseded as raw occurrence bounds by `8/3`.

No theorem in the repository currently converts the hybrid `5/3` recursion and bounded positive moments into a global distinct-mass contradiction. The full Erdős problem remains unresolved.