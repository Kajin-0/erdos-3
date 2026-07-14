# Full-edge coordinated branching

## Status

Exact strengthening of full-color coordinated branching.

The doubled side reserve is not merely latent capacity. It is a valid scale-descending four-AP-free child. Emitting it produces one child occurrence for each of the three pair edges of every parent three-AP.

The resulting occurrence branching factor is `5`, and the pair-token-union branching factor is at least `5/2`.

---

## 1. Child family

Let `B\subseteq[N,2N)` be four-AP-free and let

```math
\mathcal L(B)
=
\sum_{x,d:\ x,x+d,x+2d\in B}
\frac1d.
```

Use the full-color construction:

1. parity-selected first/last side children `V_1(x),V_3(x)`;
2. all three middle-color children `V_{2,c}(x)`.

Add the doubled side children

```math
2V_1(x)
```

and

```math
2V_3(x).
```

For every side child `V`, the sets

```math
V,
\qquad
2V,
\qquad
3V
```

are pairwise disjoint. Scaling by `2` shows that

```math
2V,
\qquad
4V,
\qquad
6V
```

are also pairwise disjoint. Hence `2V` satisfies the same first-three-dilate condition as `V`.

Scaling preserves four-AP-freeness, so every doubled side child is four-AP-free.

---

## 2. Scale descent

A three-AP inside the half-open block `[N,2N)` has step

```math
0<d<\frac N2.
```

Therefore

```math
d<\frac N2
```

for side and middle children, and

```math
2d<N
```

for doubled side children.

After dyadic shelling, every child lies strictly below the parent dyadic block. The doubled child does not create a same-scale branch.

---

## 3. Exact harmonic identity

The full-color side mass is

```math
\sum_{\rm side}H(V)=\mathcal L(B).
```

The doubled side mass is

```math
\sum_{\rm side}H(2V)
=
\frac12\mathcal L(B).
```

The full middle-color mass is

```math
\sum_{\rm middle}H(V_{2,c})
=
\mathcal L(B).
```

Thus

```math
\boxed{
\sum_{\rm full\mbox{-}edge\ children}H(C)
=
\frac52\mathcal L(B).
}
```

Using

```math
\mathcal L(B)
\ge
2\left(
\alpha-
\frac{r_3(N)}N
\right)
```

and `H(B)\le\alpha`, we obtain

```math
\boxed{
\sum_{\rm full\mbox{-}edge\ children}H(C)
\ge
5H(B)
-
5\frac{r_3(N)}N.
}
```

Every parent three-AP creates exactly three child memberships.

---

## 4. Pair-edge provenance

For a progression

```math
x,
\qquad
x+d,
\qquad
x+2d,
```

assign:

```text
side child d      -> parity-selected adjacent edge;
middle child d    -> the other adjacent edge;
doubled side 2d   -> outer edge.
```

This is a weight-preserving bijection between the three child occurrences and the three unordered pair edges:

```math
\frac1d,
\qquad
\frac1d,
\qquad
\frac1{2d}.
```

Thus full-edge child occurrence mass is exactly parent three-AP edge-occurrence mass.

---

## 5. Pair-edge multiplicity theorem

Fix an unordered pair

```math
\{a,b\},
\qquad
a<b,
\qquad
D=b-a.
```

It can occur as an outer edge of at most one three-AP: this requires the unique midpoint

```math
\frac{a+b}{2}
```

to be an integer in `B`.

It can occur as an adjacent edge in at most one three-AP. The only possibilities are

```math
a-D,\ a,\ b
```

and

```math
a,\ b,\ b+D.
```

If both existed, then

```math
a-D,\ a,\ b,\ b+D
```

would be a four-term progression of step `D`, contrary to four-AP-freeness.

Therefore

```math
\boxed{
\text{every physical pair edge belongs to at most two three-APs.}
}
```

One occurrence may be outer and one adjacent; the example `{0,1,2,4}` shows that multiplicity two is possible.

---

## 6. Pair-union branching

Let `E_{\rm occ}(B)` be the multiset of pair tokens attached to full-edge child occurrences, and let `E_\cup(B)` be its distinct pair union.

The exact edge dictionary gives

```math
W_{\rm occ}(E(B))
=
\frac52\mathcal L(B).
```

The pair-edge multiplicity theorem gives

```math
\max_e\operatorname{mult}_{E_{\rm occ}}(e)
\le2.
```

Hence

```math
\boxed{
W_\cup(E(B))
\ge
\frac12W_{\rm occ}(E(B))
=
\frac54\mathcal L(B).
}
```

Combining with the three-AP lower bound,

```math
\boxed{
W_\cup(E(B))
\ge
\frac52\left(
\alpha-
\frac{r_3(N)}N
\right)
\ge
\frac52H(B)
-
\frac52\frac{r_3(N)}N.
}
```

Thus the pair-token-deduplicated one-generation branching factor is at least `5/2`.

---

## 7. Oriented affine realization

The child states admit signed affine root coordinates.

Write a parent as

```math
S_{r,\sigma}(P)
=
\{\sigma(p-r):p\in P\},
\qquad
\sigma\in\{-1,+1\}.
```

For each role anchor, the side, middle, and doubled side children use one fixed anchor root as reference and one orientation `\sigma` or `-\sigma`. Their current point labels are exactly the distances of the assigned parent pair edges.

Therefore every child current pair and every child latent pair belongs to the parent latent pair universe

```math
\binom P2.
```

Orientation affects numerical coordinates, not unordered pair identity or pair weight.

---

## 8. One-parent Bellman row

For one parent, full-edge current pair occurrences have multiplicity at most two. If occurrence multiplicity is retained, the exact repeated-pair mass is

```math
R_{\rm edge}
=
W_{\rm occ}-W_\cup.
```

If current pair tokens are unioned and recursive latent pairs already used as current are removed, then the complete child resource union is a subset of `\binom P2`. Consequently

```math
W_\cup(\text{child current})
+
W_\cup(\text{new recursive latent pairs})
\le
J(P).
```

The remaining whole-tree problem is not local pair creation. It is reuse of the same parent pair across overlapping descendant branches.

---

## 9. Strategic consequence

The construction now has the exact profile

```text
occurrence branching factor:       5;
pair-token maximum multiplicity:   2;
pair-union branching factor:      5/2;
strict dyadic scale descent:        yes;
children per progression:            3.
```

Because `5/2>2`, pair-union production grows faster than the dyadic scale factor. A whole-tree theorem would follow from a sufficiently strong bound on cross-branch persistence of one physical pair token.

The next structural target is therefore precise:

```text
bound the number and weighted mass of full-edge descendant branches
that can reuse one unordered root pair.
```

Aligned-diamond persistence and rectangle/completion transport are the relevant obstruction models. No generation-six retained quotient is needed.
