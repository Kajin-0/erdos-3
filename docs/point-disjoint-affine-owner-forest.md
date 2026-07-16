# Point-disjoint affine owner forest theorem

## Status

State-independent exact theorem for point-disjoint retained affine child families.

Pairwise disjoint numerical child supports force every child current or latent pair identity to have a unique affine owner occurrence. Consequently the fixed-gap owner-incidence graph is a disjoint union of row stars: child recreation mass and cycle rank vanish identically.

---

## 1. Point-disjoint affine children

Let

```math
S_i=\{\sigma_i(p-r_i):p\in Q_i\}\subseteq\mathbb N
```

be a finite family of affine child states with root subsets `Q_i` in one or more parent root universes.

Assume the numerical supports are pairwise disjoint:

```math
\boxed{S_i\cap S_j=\varnothing\quad(i\ne j).}
```

For one child define its numerical resource family

```math
\mathcal V_i
=
\{\{0,u\}:u\in S_i\}
\cup
\binom{S_i}{2}
```

for a recursive child. For a terminal child retain only the current pairs `{0,u}` if latent pair energy is not propagated.

The synthetic endpoint `0` represents the affine reference. All child labels are positive.

---

## 2. Numerical resource families are disjoint

Suppose one resource identity belongs to both `V_i` and `V_j`.

### Two latent resources

If

```math
\{u,v\}\in\binom{S_i}{2}\cap\binom{S_j}{2},
```

then both endpoints belong to `S_i intersect S_j`, contradicting point disjointness.

### Two current resources

If

```math
\{0,u\}=\{0,v\},
```

then `u=v` belongs to both child supports, again impossible.

### Current versus latent

A latent pair has two positive endpoints, whereas a current pair contains `0`. They cannot be equal.

Therefore

```math
\boxed{
\mathcal V_i\cap\mathcal V_j=\varnothing
\quad(i\ne j).
}
```

---

## 3. Unique child-side owner

Construct the affine owner-incidence graph from `docs/affine-owner-incidence-cycle-decomposition.md`.

Every owner occurrence maps one parent root-pair resource to one numerical child resource in `V_i`. Within one affine child, the root-to-label map is injective, so two different parent resource pairs cannot map to the same child resource identity.

Across different children the resource families are disjoint by the preceding section.

Hence every child-side vertex has degree exactly one:

```math
\boxed{
deg_{G_D}(v)=1
\quad
(v\in R_D).
}
```

Exact duplicate child occurrences are quotiented before constructing the graph.

---

## 4. Owner graph is a row-star forest

A bipartite graph in which every right vertex has degree one has no cycle. Every connected component contains exactly one parent-pair vertex and all of its child resource leaves.

Thus for every gap `D`,

```math
\boxed{
\beta_D=0,
\qquad
c_D=|L_D|.
}
```

The complete owner graph is a disjoint union of row stars.

---

## 5. Exact mass identities

Let `m(f)` be the number of point-disjoint retained child resources owned by one parent root pair `f`. Then

```math
W_{\rm child,occ}
=
\sum_f\frac{m(f)}{D(f)}.
```

Because every child resource is unique numerically,

```math
\boxed{
W_{\rm child,occ}
=
J_{\rm child,union}.
}
```

There is no one-generation child recreation excess:

```math
\boxed{
R_{\rm recreate}=0.
}
```

The only occurrence-versus-parent-union excess is the row-star branching term

```math
\boxed{
R_{\rm branch}
=
\sum_f\frac{(m(f)-1)_+}{D(f)}.
}
```

Equivalently,

```math
\boxed{
J_{\rm child,union}
=
J_{\rm parent,used}
+
R_{\rm branch}.
}
```

---

## 6. Reference-set representation of each star

For one repeated parent pair `f`, the leaves of its row star correspond to distinct affine references. The reference-gap collision theorem therefore applies directly:

```text
row-star branching excess
    -> first reference occurrence
     + aspect-tagged reference-pair rectangles.
```

No column collision or cycle correction has to be added in the same retained transition.

This prevents three quantities from being counted separately when they are the same incidence data:

```text
parent-pair multiplicity;
child-pair occurrence mass;
rectangle collision count.
```

---

## 7. Exact `S7` interface

The certified residual-sponsor split retained family has `37` point-disjoint child states. The exact probe

```text
src/probe_s7_affine_owner_incidence_graph.py
```

reconstructs its complete current-plus-recursive-latent owner graph and verifies:

```text
maximum child-side degree = 1;
child recreation mass     = 0;
cycle rank                 = 0.
```

It then profiles the remaining row-star branching mass and reuse of the resulting reference-pair tokens.

---

## 8. Scope

The theorem closes one-generation recreation and cycle accounting **after point-disjoint retention**. It does not prove that a point-disjoint retained quotient preserves enough reciprocal mass at every generation.

It also does not bound row-star branching excess. That term may have unbounded cardinality and must be controlled by reference-gap scale, rectangle aspect, terminal stopping, or the critical depth ledger.

The surviving global sequence is therefore:

```text
raw affine output
    -> point-disjoint retained quotient
    -> row-star owner forest
    -> reference-pair rectangle ledger
    -> scale/terminal accounting.
```