# Reserve matching with recursive export

## Status

State-independent one-generation theorem replacing the false conjecture that every center/opposite reserve graph is a pseudoforest.

Every duplicated backbone-middle latent pair is either assigned to one unused equal-gap physical reserve or retained as its original sponsor-owned middle occurrence. The raw reciprocal-pair identity is exact for arbitrary reserve graphs and arbitrary prior reserve deletion.

The corrected universal owner-scale descent is one dyadic level:

```math
L_{\rm middle}\le\frac N2.
```

The earlier quarter-scale claim was false.

---

## 1. Duplicated demand occurrences

Fix

```math
P\subseteq[N,2N)
```

and one completed coordinated deletion schedule. By the latent degree-two theorem, every duplicated latent pair

```math
f=\{p,q\}
```

has exactly:

```text
one recursive backbone owner;
one recursive middle-fiber owner.
```

If the middle owner is generated at step `d` and orientation `epsilon`, define

```math
C_d(f)=\{p+\epsilon d,q+\epsilon d\}
```

and

```math
O_d(f)=\{p+2\epsilon d,q+2\epsilon d\}.
```

Both are physical parent pairs with

```math
w(C_d(f))=w(O_d(f))=w(f).
```

Let `tilde f` be the original middle-owned numerical pair occurrence. It also has weight `w(f)`.

---

## 2. Full reserve graph

For one physical gap `g`, construct the multigraph

```text
vertices: center/opposite physical reserve identities of gap g;
edge f:   joins C_d(f) to O_d(f).
```

For a connected component with `m` demand edges and `n` reserve vertices:

```text
m <= n: all demands admit an injective reserve assignment;
m > n:  exactly m-n demands must remain as middle occurrences.
```

Equivalently, if

```math
\beta=m-n+1
```

is the component cycle rank, then under full reserve availability

```math
\boxed{
|E_{\rm export}|=\max(0,\beta-1).
}
```

This follows by retaining a spanning tree plus at most one cycle and exporting every additional edge.

---

## 3. Capacity-aware matching

Earlier accounting operations may already own some reserve pairs. Let `R_avail` be the remaining physical reserve set.

Construct the demand-to-reserve bipartite incidence graph with

```math
f\sim r
\quad\Longleftrightarrow\quad
r\in\{C_d(f),O_d(f)\}\cap R_{\rm avail}.
```

Choose a maximum matching and define:

```text
D_match  = matched duplicated demands;
D_export = unmatched duplicated demands;
R_used   = matched physical reserve union;
X_rec    = {tilde f : f in D_export}.
```

Every physical reserve is used at most once, and `R_used` is disjoint from all previously reserved physical capacity.

---

## 4. Exact raw-weight identity

Matched reserves and unmatched middle occurrences preserve the exact physical gap. Therefore

```math
\boxed{
W(D)=J(R_{\rm used})+W(X_{\rm rec}).
}
```

This is an exact conservation identity. Reserve deletion changes only the partition between physical termination and recursive continuation; it does not create scalar error or duplicate an occurrence.

Under full availability, one component of gap `g` contributes recursive mass

```math
\frac{\max(0,\beta-1)}g.
```

---

## 5. Corrected owner-scale descent

An exported middle occurrence lies in a shell

```math
M\subseteq[L,2L).
```

Every middle label is a positive difference of two parent roots in `[N,2N)`, so it is strictly below `N`. Hence

```math
\boxed{L\le\frac N2.}
```

For

```math
\Theta_p(f;S)=\frac{S^p}{\operatorname{gap}(f)},
```

one obtains

```math
\boxed{
\Theta_p(X_{\rm rec})
\le
2^{-p}\Theta_p(D_{\rm export};N).
}
```

At raw exponent zero, mass is conserved. At every positive owner exponent, exported occurrences contract. In dyadic-depth form, every export releases at least one owner level.

The former claims

```text
L_middle <= N/4;
owner contraction 4^{-p};
depth release at least two levels
```

are withdrawn. They confused coordinated affine middle shells with outer-role direct heavy-fiber geometry.

---

## 6. Sharp half-scale obstruction

The parent

```math
\{65,67,68,69,99,100,101,105,106,107,111,112,113\}
\subset[64,128)
```

is four-AP-free and, under the actual retained policy, has shared backbone-middle latent pairs with both child shell bases equal to `32=N/2`.

Thus the half-scale middle bound is sharp. At owner exponent one, one unmatched middle occurrence may carry one full parent critical pair unit after the backbone occurrence has already used the natural pair capacity.

Primary reference:

```text
docs/coordinated-middle-half-scale-critical-no-go.md
```

---

## 7. Rank-two raw reserve example

The policy-compatible rank-two example has three full-availability components:

```text
gap 50:  5 demands, 4 reserve vertices;
gap 100: 5 demands, 4 reserve vertices;
gap 50:  5 demands, 4 reserve vertices.
```

A maximum raw matching exports one middle occurrence from each component, of total mass

```math
\frac1{50}+\frac1{100}+\frac1{50}=\frac1{20}.
```

The exact joint critical assignment does not eliminate the middle residual: the translated alternatives are saturated by other fixed owner loads.

---

## 8. Production compatibility

The theorem never creates an occurrence:

```text
matched demand  -> consumes one previously available physical reserve;
unmatched demand -> keeps its original middle-owned occurrence.
```

Every duplicated occurrence has one continuation, and arbitrary prior reserve consumption is handled by the same matching.

---

## 9. Remaining interface

The local raw reserve obstruction is classified. The corrected treewise tasks are:

1. telescope middle exports with one-level owner descent;
2. retain their production ownership;
3. coordinate reserve matching with direct edge/support allocation;
4. preserve terminal and recreation occurrence value;
5. combine the exact raw identity with an owner exponent or depth potential strong enough to absorb the sharp half-scale examples.
