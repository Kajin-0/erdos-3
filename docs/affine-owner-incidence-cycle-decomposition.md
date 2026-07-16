# Affine owner-incidence cycle decomposition

## Status

State-independent exact decomposition of affine pair-resource occurrence mass into parent first appearance, child first appearance, connected-component credit, and weighted cycle rank.

The theorem identifies the precise obstruction left after retaining production ownership. Branching reuse and recreation reuse are not independent error terms. Their irreducible common part is the cycle space of a fixed-gap bipartite owner graph.

---

## 1. Affine pair occurrences

Let `P` be a finite root universe. Consider a finite family of affine child occurrences indexed by `i`. One occurrence has:

```math
(r_i,\sigma_i,Q_i),
\qquad
\sigma_i\in\{-1,+1\},
\qquad
Q_i\subseteq P,
```

and numerical child image

```math
S_i=\{\sigma_i(p-r_i):p\in Q_i\}.
```

For every root pair

```math
f=\{p,q\}\in\binom{Q_i}{2},
\qquad p<q,
```

define its child physical-pair image

```math
e_i(f)
=
\operatorname{sort}
\{\sigma_i(p-r_i),\sigma_i(q-r_i)\}.
```

Translation and reflection preserve the physical gap:

```math
D(f)=q-p=D(e_i(f)).
```

Each triple `(i,f,e_i(f))` is one affine owner incidence. Distinct child occurrences remain distinct edges even when they have the same root pair and the same child pair.

---

## 2. Fixed-gap owner graph

Fix a positive gap `D`. Define a bipartite multigraph

```math
G_D=(L_D,R_D,E_D)
```

as follows.

- `L_D` consists of the parent root-pair identities of gap `D` used by at least one occurrence.
- `R_D` consists of the numerical child pair identities of gap `D` produced by at least one occurrence.
- `E_D` has one edge for every affine owner incidence from a left root pair to its right child image.

Parallel edges are retained. They represent distinct affine owners producing the same left-right pair incidence.

Write

```math
\ell_D=|L_D|,
\qquad
r_D=|R_D|,
\qquad
e_D=|E_D|,
```

and let `c_D` be the number of connected components containing at least one edge.

The multigraph cycle rank is

```math
\beta_D
=
e_D-\ell_D-r_D+c_D.
```

As usual,

```math
\beta_D\ge0.
```

A pair of parallel edges is a two-edge cycle and contributes one to `beta_D`.

---

## 3. Weighted exact identity

Every vertex and edge in `G_D` carries physical pair weight `1/D`. Define

```math
W_D=\frac{e_D}{D},
```

for occurrence-valued pair mass,

```math
P_D=\frac{\ell_D}{D},
\qquad
C_D=\frac{r_D}{D},
```

for parent and child first-appearance pair mass, and

```math
K_D=\frac{c_D}{D},
\qquad
B_D=\frac{\beta_D}{D}.
```

The graph-rank identity gives

```math
\boxed{
W_D
=
P_D+C_D-K_D+B_D.
}
```

Summing over gaps gives

```math
\boxed{
W_{\rm occ}
=
J_{\rm parent,used}
+
J_{\rm child,used}
-
K_{\rm comp}
+
B_{\rm cyc}.
}
```

No inequality or fitted coefficient is involved.

---

## 4. Branching and recreation are two views of one graph

The branching excess above parent first appearance is

```math
\boxed{
W_D-P_D
=
C_D-K_D+B_D.
}
```

The recreation excess above child first appearance is

```math
\boxed{
W_D-C_D
=
P_D-K_D+B_D.
}
```

Thus branching reuse and recreation reuse share exactly the same irreducible term:

```math
\boxed{B_D=\beta_D/D.}
```

They should not be added as independent collision penalties.

---

## 5. Forest case

If every `G_D` is a forest, then

```math
\beta_D=0
```

and

```math
W_D=P_D+C_D-K_D.
```

In this case every occurrence is accounted for by first appearance on one side or the other, with one connector credit per component. There is no residual double reuse.

Consequently the correct universal target is not a separate bound for row multiplicity and column multiplicity. It is a weighted bound for the cycle ledger

```math
B_{\rm cyc}
=
\sum_D\frac{\beta_D}{D}.
```

---

## 6. Affine geometry of cycles

For one orientation-preserving incidence, write a parent pair as

```math
\{a,a+D\}
```

and a child pair as

```math
\{b,b+D\}.
```

The affine reference is

```math
r=a-b.
```

A four-cycle with parent starts `a_1,a_2` and child starts `b_1,b_2` therefore carries four references

```math
r_{ij}=a_i-b_j
```

satisfying

```math
\boxed{
r_{11}+r_{22}=r_{12}+r_{21}.
}
```

Thus every affine four-cycle is an additive reference rectangle. Longer even cycles carry the corresponding alternating zero-sum relation.

Opposite orientations can also create a two-edge cycle. For example, the root pair `{2,4}` maps to the child pair `{1,3}` using reference `1` in the right orientation and reference `5` in the left orientation.

The cycle ledger is therefore a higher-order affine incidence resource. It refines the single-column rectangle tokens in `docs/collision-rectangle-aspect-identity.md`.

---

## 7. Small-box verification and no-go

Independent exhaustive verification over every four-AP-free subset of `[1,12]` with at least three points gives:

```text
four-AP-free parent sets                 2154
combined fixed-gap owner graphs         13176
combined graphs with positive beta       5004
maximum combined cycle rank                 18
orientation-separated graphs            21578
orientation-separated cyclic graphs       632
maximum orientation-separated rank           5
```

Hence cycle rank does not disappear after separating orientations. A universal owner-injection theorem with zero cycle term is false.

Verifier:

```text
src/verify_affine_owner_incidence_cycles.py
```

---

## 8. Remaining theorem

The pathwise pair-lineage theorem controls motion along one incidence path. The present theorem identifies what remains after all first appearances are retained:

```text
weighted affine cycle rank.
```

A complete whole-tree potential must either:

1. charge every fundamental cycle to a first-appearance additive rectangle;
2. show that cycle rectangles descend in scale or terminate;
3. bound repeated use of the same rectangle by a higher-order incidence token; or
4. combine cycle rank with the exact critical depth release.

The next admissible object is therefore a scale- and aspect-weighted cycle ledger, not another scalar multiplicity bound.