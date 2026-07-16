# Reserve pseudoforest with recursive export

## Status

State-independent one-generation theorem replacing the false conjecture that every center/opposite reserve graph is itself a pseudoforest.

Every duplicated backbone-middle latent pair is either assigned to one unused equal-gap physical reserve or retained as its original sponsor-owned pair occurrence in a lower-scale middle shell. Reserve cycle excess therefore becomes recursive descent rather than unmatched scalar debt.

---

## 1. Duplicated demand occurrences

Fix one parent shell

```math
P\subseteq[N,2N)
```

and a completed coordinated deletion schedule.

Let `D` be a family of duplicated recursive latent pair occurrences. By the latent degree-two theorem, every demand

```math
f=\{p,q\}
```

has exactly:

```text
one recursive backbone owner;
one recursive middle-fiber owner.
```

Let the middle owner be generated at step `d` and orientation `epsilon`. Its two equal-gap physical reserves are

```math
C_d(f)
=
\{p+\epsilon d,q+\epsilon d\},
```

and

```math
O_d(f)
=
\{p+2\epsilon d,q+2\epsilon d\}.
```

Both lie in the parent and satisfy

```math
w(C_d(f))=w(O_d(f))=w(f).
```

The middle child also contains the sponsor-owned numerical pair occurrence corresponding affinely to `f`. Denote that occurrence by

```math
\widetilde f.
```

It has the same physical gap and weight as `f`.

---

## 2. Available-reserve graph

Some physical pairs may already be reserved by another part of the accounting ledger. Delete those unavailable reserve vertices before constructing the graph.

For each fixed physical gap `g`, form a multigraph `G_g`:

```text
vertices: available physical reserve-pair identities of gap g;
edge f:   joins C_d(f) to O_d(f) when both are available.
```

If exactly one reserve is available, treat `f` as a pendant edge to that one vertex and a private null endpoint. If neither reserve is available, send `f` directly to recursive export.

The null endpoints are occurrence-private and are never counted as physical capacity. Equivalently, one may first separate the zero-choice and one-choice demands and apply the graph theorem only to two-choice demands.

---

## 3. Component pseudoforest extraction

Let `K` be a connected two-choice component with

```math
m=|E(K)|,
\qquad
n=|V(K)|.
```

### Tree regime

If

```math
m=n-1,
```

orient every tree edge toward its child after choosing one root. Every physical vertex receives at most one edge.

### Unicyclic regime

If

```math
m=n,
```

orient the unique cycle cyclically and orient every attached tree away from the cycle. Again every physical vertex receives exactly one or zero edges.

### Excess-cycle regime

If

```math
m>n,
```

choose a connected spanning unicyclic subgraph with exactly `n` edges. Such a subgraph exists because `K` contains a spanning tree and at least one additional edge.

Orient this unicyclic subgraph injectively as above. Export every remaining edge.

Thus every connected component admits a partition

```math
E(K)
=
E_{\rm reserve}(K)
\sqcup
E_{\rm export}(K)
```

with

```math
|E_{\rm reserve}(K)|=\min(m,n)
```

and

```math
|E_{\rm export}(K)|=\max(0,m-n).
```

The reserve edges are assigned injectively to physical vertices.

---

## 4. Exact weighted identity

All edges and vertices in one component have the same gap `g` and weight `1/g`. Therefore

```math
\begin{aligned}
W(E(K))
&=
\frac m g\\
&=
\frac{\min(m,n)}g
+
\frac{\max(0,m-n)}g.
\end{aligned}
```

The first term is the mass of the injectively used physical reserve union. For every exported edge `f`, retain its original sponsor-owned occurrence `tilde f`. Hence the second term is exactly the exported occurrence mass.

Summing over all components and all gaps gives

```math
\boxed{
W(D)
=
J(R_{\rm used})
+
W(X_{\rm rec}),
}
```

where:

```text
R_used is a physical pair union;
X_rec is an occurrence-tagged recursive pair family;
R_used uses every physical reserve at most once;
every exported token is one original middle-owner occurrence.
```

No fitted constant and no scalar error term appear.

---

## 5. Relation to cycle rank

For a connected component,

```math
\beta(K)=m-n+1.
```

Therefore the exported occurrence count is

```math
\boxed{
|E_{\rm export}(K)|
=
\max(0,\beta(K)-1).
}
```

The previous two-choice defect formula is not discarded. It is reinterpreted exactly as the number of sponsor-owned occurrences that must continue recursively.

In particular, the rank-two no-go components have

```math
\beta=2,
```

so each exports exactly one pair occurrence per physical gap component.

---

## 6. Strict shell descent

Let an exported pair occurrence lie in a retained middle shell

```math
M\subseteq[L,2L).
```

The standard full-edge scale geometry gives

```math
L\le\frac N4
```

for a middle output.

For the owner-scale moment

```math
\Theta_p(f;S)
=
\frac{S^p}{\operatorname{gap}(f)},
\qquad p>0,
```

moving `f` from parent owner scale `N` to child owner scale `L` gives

```math
\Theta_p(\widetilde f;L)
\le
4^{-p}\Theta_p(f;N).
```

Consequently

```math
\boxed{
\Theta_p(X_{\rm rec})
\le
4^{-p}\Theta_p(E_{\rm export};N).
}
```

Reserve-matched edges terminate locally as physical capacity; every unmatched cycle edge descends strictly in owner scale.

At raw reciprocal exponent zero the identity is conservative. At every positive owner-scale moment, the recursive residue contracts.

---

## 7. Rank-two counterexample

The example in

```text
docs/lexicographic-reserve-rank-two-no-go.md
```

has three bad components:

```text
gap 50:  5 edges, 4 vertices;
gap 100: 5 edges, 4 vertices;
gap 50:  5 edges, 4 vertices.
```

The hybrid theorem matches four demands in each component to physical reserves and exports one sponsor-owned pair occurrence.

The exported raw mass is

```math
\frac1{50}+rac1{100}+rac1{50}
=
\frac1{20}.
```

Those three exported pairs are the complete pair ledger of one lower-scale coordinate three-AP. The product factorization in

```text
docs/reserve-pattern-product-factorization.md
```

explains this equality.

---

## 8. Production compatibility

The theorem does not create a new occurrence:

```text
the reserve-matched branch consumes one available physical reserve;
the exported branch keeps the original middle-owned occurrence.
```

Thus an occurrence has exactly one continuation:

```text
physical reserve termination;
or recursive sponsor continuation.
```

This is compatible with the production-owned token partition. It also remains valid after arbitrary physical reserve vertices are removed as already spent: removing capacity can only move more original occurrences into the recursive export family.

---

## 9. Remaining global interface

The false pseudoforest conjecture is no longer needed. The one-generation activation row is exact for arbitrary reserve graphs.

The remaining work is treewise:

1. combine owner-scale contraction of exported cycle tokens with the exact `7/4` critical depth release;
2. prevent the same physical reserve from being used by another discharge ledger;
3. merge terminal sponsor exports with terminal-current absorption;
4. prove global summability of recursively exported occurrence mass;
5. return from the occurrence ledger to the original reciprocal mass.

The local reserve-cycle obstruction is therefore classified rather than left as an unmatched Hall deficit.
