# Affine cycle-rank rectangle tokenization

## Status

State-independent exact tokenization of the weighted cycle term from the affine owner-incidence graph.

After choosing a deterministic spanning forest, every nonforest owner edge closes one fundamental cycle. That edge determines a nonzero reference pair at its parent-pair vertex, and its complete pair weight factors exactly through the reference-pair weight and a dimensionless aspect ratio.

---

## 1. Fixed-gap owner graph

Use the fixed-gap bipartite multigraph

```math
G_D=(L_D,R_D,E_D)
```

from `docs/affine-owner-incidence-cycle-decomposition.md`.

Every edge `a in E_D` is one affine owner incidence and carries:

```text
parent root pair l(a) in L_D;
child physical pair r(a) in R_D;
reference root rho(a);
orientation sigma(a);
physical gap D.
```

First quotient exact duplicate owner incidences. Distinct edges incident to one fixed parent-pair vertex then have distinct references: for a fixed root pair, reference and orientation determine its numerical affine image.

---

## 2. Deterministic spanning forest

Order the owner edges lexicographically by

```text
parent pair;
child pair;
reference;
orientation;
remaining production owner data.
```

Run the standard greedy spanning-forest algorithm. Let

```math
F_D\subseteq E_D
```

be the selected forest edges and

```math
X_D=E_D\setminus F_D
```

the nonforest edges.

The number of nonforest edges is exactly the cycle rank:

```math
\boxed{|X_D|=\beta_D.}
```

Each `a in X_D` closes one fundamental even cycle with the unique forest path between its endpoints.

---

## 3. Canonical reference pair for one cycle edge

Fix

```math
a\in X_D.
```

Its forest path begins at the parent-pair vertex

```math
l(a)
```

with a unique forest edge, denoted

```math
b(a)\in F_D.
```

Both `a` and `b(a)` are incident to the same parent root pair but are distinct owner incidences. Therefore their references are distinct:

```math
\rho(a)\ne\rho(b(a)).
```

Define the canonical cycle reference pair

```math
f(a)
=
\{\rho(a),\rho(b(a))\}
```

and its gap

```math
\delta(a)
=
|\rho(a)-\rho(b(a))|>0.
```

Both references belong to the parent root universe, so `f(a)` is a genuine parent physical pair.

---

## 4. Exact aspect identity

The nonforest owner edge has weight

```math
w(a)=\frac1D.
```

The reference pair has weight

```math
w(f(a))=\frac1{\delta(a)}.
```

Therefore

```math
\boxed{
w(a)
=
\frac{\delta(a)}D\,w(f(a)).
}
```

Summing over all nonforest edges gives the exact weighted cycle identity

```math
\boxed{
B_D
=
\frac{\beta_D}{D}
=
\sum_{a\in X_D}
\frac{\delta(a)}D
\frac1{\delta(a)}.
}
```

Across all gaps,

```math
\boxed{
B_{\rm cyc}
=
\sum_D\sum_{a\in X_D}
\operatorname{aspect}(a)\,w(f(a)),
\qquad
\operatorname{aspect}(a)=\frac{\delta(a)}D.
}
```

No cycle mass remains anonymous.

---

## 5. Injectivity and reuse

The map

```math
a\longmapsto(a,f(a))
```

is injective because the nonforest edge is retained in the token. Thus every unit of cycle rank has one canonical rectangle token.

The physical reference pair `f(a)` alone need not be unique. Several fundamental cycles may use the same reference pair. That is the next reuse layer, not a defect in the identity.

The correct first-appearance token is therefore

```math
\mathfrak C(a)
=
(D,a,f(a),\delta(a),\sigma(a),\text{fundamental cycle}).
```

---

## 6. Near and far cycle rectangles

### Near cycle

If

```math
\delta(a)\le D,
```

then

```math
w(a)\le w(f(a)).
```

One first-appearance reference-pair capacity can pay the cycle edge directly.

### Far cycle

If

```math
2^kD<\delta(a)\le2^{k+1}D,
```

then

```math
w(a)
\le
2^{k+1}w(f(a)).
```

The coefficient is exactly the dyadic rectangle aspect. It must be combined with scale release, later termination, or a higher-order first-appearance token.

---

## 7. Four-cycle geometry

For an orientation-preserving four-cycle, write parent pair starts as `a_1,a_2` and child pair starts as `b_1,b_2`. The four edge references are

```math
r_{ij}=a_i-b_j.
```

They satisfy

```math
r_{11}+r_{22}=r_{12}+r_{21}.
```

The fundamental-cycle token is therefore an additive affine rectangle in the parent reference set. The present spanning-forest construction extends this rectangle vocabulary to arbitrary even cycles.

---

## 8. Verification

`src/verify_affine_owner_incidence_cycles.py` independently verifies, for every four-AP-free subset of `[1,12]`:

1. the owner-incidence rank identity;
2. deterministic spanning-forest cycle count;
3. nonzero canonical reference gaps;
4. the pointwise aspect identity for every nonforest edge.

---

## 9. Remaining theorem

Branching excess, recreation excess, and cycle excess now have a common exact vocabulary:

```text
parent pair first appearance;
child pair first appearance;
component connector;
fundamental-cycle rectangle token.
```

The unresolved global quantity is no longer unlabelled multiplicity. It is reuse and scale distribution of the canonical cycle reference pairs, especially in far-aspect bands.