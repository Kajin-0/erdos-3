# Backbone-middle two-choice reserve graph

## Status

State-independent exact Hall reduction for the genuine latent-latent residual of coordinated deletion outputs.

Every duplicated backbone-middle latent pair has two equal-gap reserve options: its center-copy pair and opposite-copy pair. Packing all duplicated mass into one physical capacity per reserve pair is equivalent to orienting the edges of a multigraph to distinct endpoints. The exact criterion is that every reserve component is a pseudoforest.

---

## 1. Duplicate demands

Use the latent degree-two theorem. Let

```math
\mathcal D_{BM}
```

be the family of parent pairs occurring latently in exactly:

```text
one recursive backbone child;
one recursive middle-fiber child.
```

One demand

```math
f=\{p,q\}\in\mathcal D_{BM}
```

belongs to a unique middle fiber with selected step `d` and orientation `epsilon`.

Its required mass is

```math
w(f)=\frac1{D(f)}.
```

---

## 2. Two reserve options

Define

```math
C(f)
=
\{p+\varepsilon d,q+\varepsilon d\}
```

and

```math
O(f)
=
\{p+2\varepsilon d,q+2\varepsilon d\}.
```

Both are physical parent pairs and

```math
D(C(f))=D(O(f))=D(f).
```

Therefore

```math
\boxed{
w(C(f))=w(O(f))=w(f).}
```

The two reserve pairs are distinct because `d>0`.

---

## 3. Reserve multigraph

Construct an undirected multigraph

```math
\mathcal G_{\rm res}.
```

- Vertices are physical reserve-pair identities appearing as some `C(f)` or `O(f)`.
- Each duplicated demand `f` contributes one edge joining `C(f)` and `O(f)`.
- Parallel demand edges are retained.

All edges incident to one fixed vertex have the same physical pair gap, because the vertex itself determines its gap. Hence all demands competing for one reserve vertex require exactly that vertex's one reciprocal-gap capacity.

---

## 4. Capacity allocation as endpoint orientation

Assigning demand `f` to its center or opposite reserve is equivalent to orienting its graph edge toward the chosen endpoint.

One physical reserve pair may pay at most one demand. Therefore the allocation is valid exactly when every vertex has indegree at most one.

Thus the pair-capacity problem is:

```text
orient every edge of G_res
so that every vertex receives at most one edge.
```

No fractional arithmetic remains because demand and endpoint capacities are equal edgewise.

---

## 5. Pseudoforest criterion

### Necessity

If a connected component has `e` demand edges and `v` reserve vertices, any endpoint assignment has only `v` available vertices. Therefore

```math
e\le v
```

is necessary.

### Sufficiency

A connected multigraph with

```math
e\le v
```

is either:

```text
a tree, with e=v-1;
a unicyclic component, with e=v.
```

For a tree, choose a root and orient every edge away from the root toward its child endpoint. Every nonroot vertex receives exactly one edge.

For a unicyclic component, orient the unique cycle cyclically and orient each attached tree away from the cycle. Every vertex receives exactly one edge.

Therefore the component admits the required assignment.

Combining necessity and sufficiency:

```math
\boxed{
\mathcal D_{BM}\text{ packs into center/opposite reserves}
\iff
|E(K)|\le|V(K)|
\text{ for every component }K.
}
```

Equivalently, every connected component has cycle rank at most one:

```math
\boxed{
\beta(K)=|E(K)|-|V(K)|+1\le1.
}
```

Thus the exact criterion is:

```text
G_res is a pseudoforest.
```

---

## 6. Hall-defect ledger

For an arbitrary reserve component define its excess

```math
\operatorname{def}(K)
=
\bigl(|E(K)|-|V(K)|\bigr)_+.
```

Since all demands in one fixed-gap component have common reciprocal weight `1/D`, the exact unmatched mass is

```math
\frac{\operatorname{def}(K)}D
```

when no additional reserve is permitted.

Across gaps, the complete two-choice Hall defect is

```math
\boxed{
R_{\rm reserve-def}
=
\sum_K
\frac{(|E(K)|-|V(K)|)_+}{D(K)}.
}
```

If components can mix gaps only through identical physical vertices, then each connected component already has one fixed gap.

---

## 7. Simple and parallel cycles

A simple cycle is not an obstruction. It has equal numbers of demand edges and reserve vertices and can be oriented cyclically.

A pair of parallel edges also forms one unicyclic component with two vertices and two edges; it remains feasible by assigning the two demands to opposite endpoints.

Failure begins only with cycle rank at least two, for example:

```text
three parallel demand edges between two reserve pairs;
a theta graph;
two cycles joined in one component.
```

---

## 8. Exact policy-compatible example

For the parent in

```text
docs/lexicographic-retained-latent-reuse-no-go.md,
```

the three duplicated pairs have options:

```text
{68,73} -> {69,74} or {70,75};
{68,78} -> {69,79} or {70,80};
{73,78} -> {74,79} or {75,80}.
```

The reserve graph is three disjoint edges. It is a forest, so the complete latent residual `1/2` packs exactly into either all center-copy or all opposite-copy reserves.

The example defeats one reference-pair payment but not the two-choice translated reserve.

---

## 9. Remaining theorem

The coordinated deletion pair-activation problem is now reduced to one precise graph question:

```math
\boxed{
\text{are all center/opposite reserve components pseudoforests,}
}
```

or, if not, can every excess-cycle component export a lower-scale or terminal token?

This is substantially narrower than a general physical-pair Hall theorem:

- latent demand degree is exactly two;
- every demand and both options have identical reciprocal weight;
- the only obstruction is reserve cycle rank at least two.