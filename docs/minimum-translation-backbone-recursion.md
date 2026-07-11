# Minimum-translation backbone recursion

## Status

Exact strengthening and simplification of the current deletion-based recursion.

Let

```math
D\subseteq[N,2N)
```

be four-term-progression-free. Run sponsored side-anchor deletion until a three-term-progression-free residual of size `s` remains, and write

```math
K=|D|-s.
```

The existing program used spanning-forest and merge-difference children to obtain a thinned structural family. A simpler child is stronger for the one-generation harmonic estimate:

```math
\mathcal B(D)
=
\{d-m:d\in D,\ d>m\},
\qquad
m=\min D.
```

This minimum-translation backbone is a lower-scale four-term-progression-free copy of the entire parent state with one point removed. Combining it with the full middle family gives a binary raw occurrence factor `3`. Combining it with the exact middle multiplicity-fiber resolution gives a binary hybrid factor `2`.

The spanning-forest and merge constructions remain useful for overlap geometry, but they are no longer needed for the strongest one-generation branching constants.

---

## 1. The backbone child

Let

```math
m=\min D.
```

Define

```math
\mathcal B(D)
=
\{d-m:d\in D,\ d>m\}.
```

Since

```math
N\le m<d<2N,
```

one has

```math
1\le d-m<N.
```

Therefore

```math
\boxed{
\mathcal B(D)\subseteq[1,N).
}
```

Translation preserves arithmetic progressions. Hence

```math
\boxed{
\mathcal B(D)
\text{ is four-term-progression-free}.
}
```

Its cardinality is exact:

```math
\boxed{
|\mathcal B(D)|=|D|-1.
}
```

---

## 2. Per-parent association and half-contraction

Associate the backbone occurrence

```math
d-m
```

with its parent element `d`.

For every `d>m`,

```math
d-m
\le
d-N
\le
d/2,
```

because `d<2N`.

Thus

```math
\boxed{
0<d-m\le d/2.
}
```

The minimum point `m` creates no backbone output.

The root translation anchor of the child is `m`, which is an element of the lifted parent set. Consequently the inherited representation

```math
S=B-t,
\qquad B\subseteq D_{\mathrm{root}},
\qquad t\in\{0\}\cup D_{\mathrm{root}}
```

is preserved through repeated backbone recursion and dyadic shell restriction.

---

## 3. Full-middle outputs

Every deleted sponsor creates exactly one selected middle occurrence with step `q`. Since the selected progression lies in `[N,2N)`,

```math
q\le N/2.
```

The full middle children satisfy

```math
\sum_xH(M_x)
=
\sum_{i=1}^{K}\frac1{q_i}
\ge
\frac{2K}{N}.
```

Every deleted sponsor creates one middle occurrence. Every nonminimum parent creates one backbone occurrence. Therefore:

- a deleted nonminimum sponsor creates one middle and one backbone occurrence;
- the minimum creates at most one middle occurrence;
- a residual nonminimum point creates one backbone occurrence.

Hence

```math
\boxed{
\text{every parent element creates at most two outputs}.
}
```

Both outputs associated with a deleted nonminimum sponsor are at most half the sponsor label. Therefore the existing linear and higher-moment contraction inequalities remain valid.

---

## 4. Raw binary factor three

The backbone harmonic mass satisfies

```math
H(\mathcal B(D))
>
\frac{|D|-1}{N}.
```

Combining with the full middle family gives

```math
\begin{aligned}
H(\mathcal B(D))
+
\sum_xH(M_x)
&\ge
\frac{|D|-1}{N}
+
\frac{2K}{N}\\
&=
\frac{3|D|-2s-1}{N}.
\end{aligned}
```

Since

```math
H(D)\le\frac{|D|}{N},
```

one obtains

```math
\boxed{
H(\mathcal B(D))
+
\sum_xH(M_x)
\ge
3H(D)
-
2\frac{r_3(N)}N
-
\frac1N.
}
```

This is a binary occurrence-multiset theorem. It improves the previous raw factor `8/3` to `3`.

---

## 5. Exact middle multiplicity resolution

Let

```math
Q=\{q_i:1\le i\le K\}
```

be the set of distinct selected steps. For each `q in Q`, let `Xi_q` be the center-difference child from the exact middle multiplicity-fiber construction.

The exact identity is

```math
|Q|+
\sum_{q\in Q}|\Xi_q|
=K.
```

The corresponding harmonic lower bound is

```math
H(Q)
+
\sum_{q\in Q}H(\Xi_q)
\ge
\frac{K}{N}.
```

Each deleted sponsor creates exactly one multiplicity-resolved middle output:

- one terminal representative step; or
- one recursive multiplicity-fiber occurrence.

---

## 6. Binary hybrid factor two

Combine the multiplicity-resolved middle output with the backbone child.

Every deleted nonminimum sponsor creates:

1. exactly one multiplicity-resolved middle output;
2. exactly one backbone output.

Every other parent creates at most one backbone output. Thus the genealogy remains binary.

The harmonic output satisfies

```math
\begin{aligned}
&H(Q)
+
\sum_{q\in Q}H(\Xi_q)
+
H(\mathcal B(D))\\
&\qquad\ge
\frac{K}{N}
+
\frac{|D|-1}{N}\\
&\qquad=
\frac{2|D|-s-1}{N}.
\end{aligned}
```

Therefore

```math
\boxed{
H(Q)
+
\sum_{q\in Q}H(\Xi_q)
+
H(\mathcal B(D))
\ge
2H(D)
-
\frac{r_3(N)}N
-
\frac1N.
}
```

This improves the previous multiplicity-resolving factor `5/3` to `2`.

The output has the relevant hybrid form:

1. terminal harmonic mass of distinct selected steps;
2. recursive multiplicity-fiber children encoding repeated steps;
3. one lower-scale backbone child carrying almost the entire parent set.

---

## 7. Moment potential

For every retained parent `d>m`, the backbone label satisfies

```math
d-m\le d/2.
```

Every multiplicity-resolved middle output associated with a deleted sponsor `d` also satisfies

```math
y(d)\le d/2.
```

Hence for every real `p>=1`,

```math
\boxed{
\sum_{u\text{ output of }d}u^p
\le
2^{1-p}d^p.
}
```

The minimum parent has no backbone output and at most one middle output, so the same inequality holds.

Thus the global all-generation positive-moment theorem remains unchanged:

```math
\sum_{\text{terminal occurrences }q}q^p
\le
2^{1-p}
\sum_{d\in D_{\mathrm{root}}}d^p.
```

---

## 8. Relation to the deletion-DAG structural theory

The backbone theorem does not invalidate the deletion-DAG merge and spanning-forest lemmas. Those lemmas expose overlap and scale export that a translated near-copy does not reveal.

The roles are now different.

- The minimum-translation backbone gives the strongest and shortest one-generation branching inequalities.
- Merge-difference and component children remain supporting tools for controlling multiplicity, convergence diamonds, and local affine overlap.

The active quantitative constants become:

```math
\boxed{
\text{raw binary occurrence factor}=3,
}
```

and

```math
\boxed{
\text{binary multiplicity-resolving hybrid factor}=2.
}
```

---

## 9. Remaining obstruction

The backbone child is a translated near-copy of the parent. It can therefore preserve the same lifted progressions through several generations. The theorem strengthens harmonic growth but does not by itself resolve distinctness.

After center and anchor layering, the remaining obstruction is still multiplicity of one identical local progression across incomparable recursive states with the same inherited root anchor.

The next structural target is an anchor-aligned branching diamond:

```math
\boxed{
\text{classify when a middle multiplicity-fiber child and the backbone child preserve the same local progression with the same root anchor.}
}
```

For the minimum-translation backbone, such an aligned event can occur only when the middle representative anchor equals the parent minimum. This is a substantially more rigid condition than arbitrary component-child overlap.
