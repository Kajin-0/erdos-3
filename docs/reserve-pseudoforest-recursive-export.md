# Reserve matching with recursive export

## Status

State-independent one-generation theorem replacing the false conjecture that every center/opposite reserve graph is a pseudoforest.

Every duplicated backbone-middle latent pair is either assigned to one unused equal-gap physical reserve or retained as its original sponsor-owned pair occurrence in a lower-scale middle shell. Reserve matching failure therefore becomes recursive descent rather than unmatched scalar debt.

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
C_d(f)=\{p+\epsilon d,q+\epsilon d\}
```

and

```math
O_d(f)=\{p+2\epsilon d,q+2\epsilon d\}.
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

## 2. Full two-choice reserve graph

First suppose that every center and opposite reserve is available.

For each fixed physical gap `g`, form the multigraph `G_g`:

```text
vertices: physical reserve-pair identities of gap g;
edge f:   joins C_d(f) to O_d(f).
```

A demand is paid physically exactly when its edge is assigned to one incident vertex, with no reserve vertex assigned twice.

Let `K` be a connected component with

```math
m=|E(K)|,
\qquad
n=|V(K)|.
```

### Tree regime

If `m=n-1`, choose a root and assign each edge to its child endpoint. Every edge is paid.

### Unicyclic regime

If `m=n`, orient the unique cycle cyclically and orient every attached tree away from the cycle. Every edge is paid.

### Excess-cycle regime

If `m>n`, choose a connected spanning unicyclic subgraph with exactly `n` edges. Assign those edges injectively as above and export every remaining edge.

Thus

```math
E(K)=E_{\rm reserve}(K)\sqcup E_{\rm export}(K)
```

with

```math
|E_{\rm reserve}(K)|=\min(m,n)
```

and

```math
|E_{\rm export}(K)|=\max(0,m-n).
```

Because

```math
\beta(K)=m-n+1,
```

the full-availability export count is

```math
\boxed{
|E_{\rm export}(K)|=\max(0,\beta(K)-1).
}
```

---

## 3. Capacity-aware incidence matching

Other parts of the accounting ledger may already own some physical reserve pairs. Let

```math
R_{\rm avail}
```

be the remaining physical reserve-pair set.

For each fixed gap, form the bipartite incidence graph

```math
\mathcal B_g=(D_g,R_{{\rm avail},g};\sim),
```

where

```math
f\sim r
```

exactly when

```math
r\in\{C_d(f),O_d(f)\}.
```

A demand may therefore have zero, one, or two available neighbors.

Choose a maximum matching

```math
\mathcal M_g\subseteq D_g\times R_{{\rm avail},g}.
```

Define

```text
D_match = demands covered by the matching;
D_export = unmatched demands;
R_used = matched physical reserve vertices.
```

Then:

```text
every matched demand uses one incident equal-gap reserve;
no physical reserve is used more than once;
every unmatched demand retains its original middle-owner occurrence.
```

No closed formula in terms of cycle rank alone is asserted after reserve deletion. Hall deficiencies created by unavailable vertices are handled exactly by the matching.

---

## 4. Exact weighted identity

For each matched pair `(f,r)`,

```math
w(f)=w(r),
```

and for every unmatched demand,

```math
w(f)=w(\widetilde f).
```

Therefore, summing over all gaps,

```math
\boxed{
W(D)=J(R_{\rm used})+W(X_{\rm rec}),
}
```

where

```text
R_used is a physical pair union;
X_rec is the occurrence-tagged family {tilde f : f in D_export};
R_used is disjoint from all physical capacity reserved before matching.
```

This is an exact conservation identity. No fitted coefficient and no unmatched scalar error remain.

Under full availability, the contribution from one connected component is

```math
\frac{\min(m,n)}g
+
\frac{\max(0,m-n)}g,
```

so its recursive-export mass is exactly

```math
\frac{\max(0,\beta(K)-1)}g.
```

---

## 5. Strict owner-scale descent

Let an exported pair occurrence lie in a retained middle shell

```math
M\subseteq[L,2L).
```

The standard middle-output geometry gives

```math
L\le\frac N4.
```

For the owner-scale moment

```math
\Theta_p(f;S)=\frac{S^p}{\operatorname{gap}(f)},
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
4^{-p}\Theta_p(D_{\rm export};N).
}
```

Physical reserve matches terminate locally. Every unmatched demand descends strictly in owner scale.

At raw reciprocal exponent zero the row is conservative. At every positive owner-scale moment the recursively exported part contracts.

---

## 6. Rank-two counterexample

The example in

```text
docs/lexicographic-reserve-rank-two-no-go.md
```

has three full-availability components:

```text
gap 50:  5 edges, 4 vertices;
gap 100: 5 edges, 4 vertices;
gap 50:  5 edges, 4 vertices.
```

A maximum incidence matching uses four physical reserves in each component and leaves one demand unmatched. The three unmatched demands retain their original middle-owner occurrences.

Their raw mass is

```math
\frac1{50}+\frac1{100}+\frac1{50}=\frac1{20}.
```

Those three exported occurrences are the complete pair ledger of one lower-scale coordinate three-AP. The product factorization in

```text
docs/reserve-pattern-product-factorization.md
```

explains this equality.

---

## 7. Production compatibility

The theorem never creates an occurrence:

```text
a matched demand consumes one previously available physical reserve;
an unmatched demand keeps its original middle-owned occurrence.
```

Thus every duplicated occurrence has exactly one continuation:

```text
physical reserve termination;
or recursive sponsor continuation.
```

This remains valid after arbitrary prior capacity reservations. Removing physical reserves can only reduce the matching and move additional original occurrences into `X_rec`; it cannot cause double use or destroy the exact identity.

---

## 8. Remaining global interface

The false pseudoforest conjecture is no longer needed. The one-generation reserve allocation is exact for arbitrary reserve graphs and arbitrary previously unavailable reserve sets.

The remaining work is treewise:

1. combine owner-scale contraction of unmatched sponsor occurrences with the exact `7/4` critical depth release;
2. impose one global ownership order for direct discharge, terminal absorption, and reserve matching;
3. merge terminal sponsor exports with terminal-current absorption;
4. prove global summability of recursively exported occurrence mass;
5. return from the occurrence ledger to the original reciprocal mass.

The local reserve-cycle obstruction is therefore classified rather than left as an unmatched Hall deficit.
