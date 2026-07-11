# Spanning-forest binary four-thirds recursion

## Status

Exact strengthening of the deletion-DAG occurrence recursion.

Let

```math
D\subseteq[N,2N)
```

be four-term-progression-free. Run side-anchor deletion until a three-term-progression-free residual of size `s` remains. Put

```math
K=|D|-s.
```

The affine deletion DAG has `K+s=|D|` vertices, `2K` directed edges, and `rho` indegree-zero vertices.

The merge-difference recursion previously supplied

```math
K-s+\rho
```

structural occurrences. A second canonical family comes from translating the components of a spanning forest of the deletion DAG. The two structural families have total cardinality exactly

```math
2K.
```

After selecting at most one structural occurrence per parent element and retaining the selected middle occurrence, one obtains a binary occurrence genealogy with harmonic branching factor `4/3`:

```math
\boxed{
\sum H(\text{retained structural children})
+
\sum H(\text{selected middle children})
\ge
\frac43 H(D)
-
\frac43\frac{r_3(N)}N.
}
```

This improves the previous binary factor `7/6`.

The inequality still counts numerical labels with multiplicity. It does not solve the distinct-mass problem.

---

# 1. Deletion-DAG setup

Write each selected three-term progression as

```math
(a_i,b_i,c_i),
\qquad
 a_i+c_i=2b_i,
```

where `a_i` is the deleted coordinated side anchor. Add the directed edges

```math
a_i\longrightarrow b_i,
\qquad
a_i\longrightarrow c_i.
```

Deletion time increases along every edge, so the graph is acyclic. Every deleted vertex has outdegree two and every residual vertex has outdegree zero.

Let

```math
\rho
```

be the number of indegree-zero vertices.

The exact merge excess is

```math
M
=
\sum_v\max\{d^-(v)-1,0\}
=
K-s+\rho.
```

For each vertex `v`, translating its incoming sponsors by the smallest one gives the merge-difference child

```math
\Delta_v
=
\{a-p_v:a\in I_v,\ a>p_v\},
\qquad
p_v=\min I_v.
```

Then

```math
\sum_v|\Delta_v|=K-s+\rho.
```

Each `Delta_v` is four-term-progression-free and lies in `[1,N)`.

---

# 2. A spanning forest of the deletion DAG

Every nonroot vertex has at least one incoming edge. Choose exactly one incoming edge for every nonroot vertex.

Because the deletion DAG is acyclic, the chosen edges form a directed spanning forest with exactly `rho` rooted components. Denote its vertex components by

```math
C_1,\ldots,C_\rho.
```

They partition `D`:

```math
D=C_1\sqcup\cdots\sqcup C_\rho.
```

For each component choose its numerically smallest element

```math
m_j=\min C_j
```

and define the component-translation child

```math
\Theta_j
=
\{x-m_j:x\in C_j,\ x>m_j\}.
```

Then

```math
|\Theta_j|=|C_j|-1.
```

Summing over the forest components gives the exact count

```math
\boxed{
\sum_{j=1}^{\rho}|\Theta_j|
=
|D|-\rho.
}
```

Since `|D|=K+s`, this is

```math
\sum_j|\Theta_j|=K+s-\rho.
```

## Lower scale

All vertices of a component lie in `[N,2N)`, so every positive difference satisfies

```math
1\le x-m_j<N.
```

Hence

```math
\boxed{\Theta_j\subseteq[1,N).}
```

## Four-term-progression-freeness

If

```math
d,\ d+r,\ d+2r,\ d+3r\in\Theta_j,
```

then translating by `m_j` gives a four-term progression inside

```math
C_j\subseteq D,
```

contradicting the hypothesis on `D`. Therefore

```math
\boxed{\Theta_j\text{ is four-term-progression-free}.}
```

## Harmonic lower bound

Every element of every `Theta_j` is smaller than `N`, so

```math
\boxed{
\sum_jH(\Theta_j)
\ge
\frac{|D|-\rho}{N}.
}
```

---

# 3. Exact structural-occurrence balance

The component-translation family has cardinality

```math
|D|-\rho=K+s-\rho.
```

The merge-difference family has cardinality

```math
K-s+\rho.
```

Adding them cancels both the residual and root terms:

```math
\begin{aligned}
\sum_j|\Theta_j|
+
\sum_v|\Delta_v|
&=(K+s-\rho)+(K-s+\rho)\\
&=2K.
\end{aligned}
```

Thus

```math
\boxed{
\sum_j|\Theta_j|
+
\sum_v|\Delta_v|
=2K.
}
```

Consequently the unthinned structural harmonic mass satisfies

```math
\boxed{
\sum_jH(\Theta_j)
+
\sum_vH(\Delta_v)
\ge
\frac{2K}{N}.
}
```

This identity is independent of the root count `rho`.

---

# 4. Parent-element association

Associate every component-translation occurrence

```math
x-m_j\in\Theta_j
```

with the parent element `x`. Each parent element is associated with at most one component occurrence, because the forest components partition `D` and only the minimum of a component is omitted.

Associate every merge occurrence

```math
a-p_v\in\Delta_v
```

with its nonminimal sponsor `a`.

A deleted sponsor has exactly two outgoing deletion-DAG edges. It can therefore be nonminimal in at most two incoming-sponsor sets. Hence each deleted sponsor is associated with at most two merge occurrences.

Residual vertices are never merge sponsors.

Therefore:

- a residual parent element carries at most one structural occurrence;
- a deleted parent element carries at most three structural occurrences: one component occurrence and at most two merge occurrences.

---

# 5. One structural occurrence per parent

Let

```math
r
```

be the number of component occurrences associated with residual vertices. Then

```math
0\le r\le s.
```

The total number of structural occurrences associated with deleted sponsors is

```math
2K-r.
```

Each deleted sponsor carries at most three such occurrences. Therefore the number `A` of deleted sponsors carrying at least one structural occurrence satisfies

```math
A\ge\frac{2K-r}{3}.
```

For every such deleted sponsor, retain one associated structural occurrence. Also retain all `r` structural occurrences associated with residual vertices.

Let the resulting thinned structural child subsets be denoted by

```math
\widetilde\Theta_j\subseteq\Theta_j,
\qquad
\widetilde\Delta_v\subseteq\Delta_v.
```

Their total cardinality is at least

```math
\begin{aligned}
\sum_j|\widetilde\Theta_j|
+
\sum_v|\widetilde\Delta_v|
&\ge A+r\\
&\ge\frac{2K-r}{3}+r\\
&=\frac{2K}{3}+\frac{2r}{3}\\
&\ge\frac{2K}{3}.
\end{aligned}
```

Thus

```math
\boxed{
\sum_j|\widetilde\Theta_j|
+
\sum_v|\widetilde\Delta_v|
\ge
\frac{2K}{3}.
}
```

Every retained structural label is smaller than `N`, so

```math
\boxed{
\sum_jH(\widetilde\Theta_j)
+
\sum_vH(\widetilde\Delta_v)
\ge
\frac{2K}{3N}.
}
```

Each parent element is now associated with at most one retained structural occurrence.

---

# 6. Selected middle children

For every selected progression let `q_i` be its common difference. Since the progression lies in an interval of length `N`,

```math
q_i\le\frac N2.
```

Partition the selected progressions by

```math
\chi(q)=v_2(q)-v_3(q)\pmod3
```

and retain the color carrying maximal reciprocal load. Group the retained steps by their middle point to obtain the selected middle children `M_x^*`.

As in the sponsored recursion,

```math
\boxed{
\sum_xH(M_x^*)
\ge
\frac{2K}{3N}.
}
```

Each deleted sponsor creates at most one selected middle occurrence. Residual vertices create none.

---

# 7. Binary four-thirds theorem

Retain:

1. at most one structural occurrence associated with each parent element;
2. the selected middle occurrence, when present, associated with each deleted sponsor.

Therefore every parent element creates at most two retained child occurrences.

Combining the structural and middle lower bounds gives

```math
\begin{aligned}
&\sum_jH(\widetilde\Theta_j)
+
\sum_vH(\widetilde\Delta_v)
+
\sum_xH(M_x^*)\\
&\qquad\ge
\frac{2K}{3N}
+
\frac{2K}{3N}\\
&\qquad=
\frac{4K}{3N}.
\end{aligned}
```

Since

```math
K=|D|-s,
```

we obtain

```math
\boxed{
\sum_jH(\widetilde\Theta_j)
+
\sum_vH(\widetilde\Delta_v)
+
\sum_xH(M_x^*)
\ge
\frac43\frac{|D|-s}{N}.
}
```

Using

```math
H(D)\le\frac{|D|}{N}
```

and

```math
s\le r_3(N),
```

this yields

```math
\boxed{
\sum_jH(\widetilde\Theta_j)
+
\sum_vH(\widetilde\Delta_v)
+
\sum_xH(M_x^*)
\ge
\frac43H(D)
-
\frac43\frac{r_3(N)}N.
}
```

The retained occurrence genealogy is binary:

```math
\boxed{
\text{every parent element creates at most two retained child occurrences.}
}
```

---

# 8. Comparison with the previous thinning

The earlier merge-plus-middle thinning retained

```math
\frac76H(D)
-
\frac53\frac{r_3(N)}N.
```

The spanning-forest construction improves this to

```math
\boxed{
\frac43H(D)
-
\frac43\frac{r_3(N)}N.
}
```

The improvement comes from a complementary structural family:

- merge differences are strongest when the deletion DAG has many roots;
- component translations are strongest when it has few roots;
- their cardinalities sum exactly to `2K`.

The root term cancels before thinning.

---

# 9. Remaining multiplicity gap

The theorem is still an occurrence-multiset statement. Different component and merge children may contain the same numerical labels, and descendants may merge again at later generations.

The current lower bound controls

```math
\sum_d\frac{m(d)}d,
```

not

```math
\sum_{d:m(d)>0}\frac1d.
```

The improved factor changes the quantitative closing target. A sufficient weighted multiplicity theorem would now need an exponential rate strictly below

```math
\boxed{\frac43}
```

for the retained binary genealogy.

A more local next target is to classify the deleted sponsors carrying all three unthinned structural occurrences:

1. one component-translation occurrence;
2. two merge-difference occurrences.

If such triple-loaded sponsors are sparse, or necessarily export an additional smaller label, the binary factor can be improved beyond `4/3` or coupled to a scale-compensated potential.

---

## Dependencies

- `docs/side-anchor-deletion-dag.md`
- `docs/deletion-dag-merge-difference-recursion.md`
- `docs/sponsored-three-ap-binary-recursion.md`

## Audit state

Proved in the repository. The spanning-forest translation argument and the per-parent thinning count are elementary, but the theorem has not yet received independent expert review.
