# Full-color pair-edge capacity

## Status

Exact bridge between full-color coordinated branching and affine pair-token activation.

For every parent three-term progression, the full-color construction produces:

1. one side-child step token;
2. one doubled side reserve token;
3. one middle-color step token.

Their weights are exactly the weights of the three unordered pair edges of the progression.

---

## 1. One progression

Let

```math
x,
\qquad
x+d,
\qquad
x+2d
```

be a three-term progression in a four-AP-free block.

Its unordered root-pair edges are:

```math
e_L=\{x,x+d\},
```

```math
e_R=\{x+d,x+2d\},
```

and

```math
e_O=\{x,x+2d\}.
```

Their pair weights are

```math
w(e_L)=\frac1d,
\qquad
w(e_R)=\frac1d,
\qquad
w(e_O)=\frac1{2d}.
```

---

## 2. Full-color child assignment

The coordinated parity rule chooses exactly one side endpoint:

```text
even v2(d): first endpoint x;
odd  v2(d): last endpoint x+2d.
```

Let `C_side` be the corresponding side child. It contains the step token `d`.

The full middle coloring

```math
\chi(d)=v_2(d)-v_3(d)\pmod3
```

chooses exactly one middle-color child `C_mid`. It also contains the step token `d`.

Define the side doubled reserve by

```math
2C_{\rm side}
=
\{2s:s\in C_{\rm side}\}.
```

The side-child construction guarantees

```math
C_{\rm side}
\cap
2C_{\rm side}
=
\varnothing.
```

---

## 3. Edge-capacity dictionary

If the first endpoint is selected as the side role, assign

```text
side token d       -> left adjacent edge e_L;
middle token d     -> right adjacent edge e_R;
side reserve 2d    -> outer edge e_O.
```

If the last endpoint is selected as the side role, reverse the two adjacent assignments:

```text
side token d       -> right adjacent edge e_R;
middle token d     -> left adjacent edge e_L;
side reserve 2d    -> outer edge e_O.
```

In both cases the weights match exactly:

```math
\frac1d,
\qquad
\frac1d,
\qquad
\frac1{2d}.
```

Thus every progression has a weight-preserving bijection

```math
\boxed{
\{e_L,e_R,e_O\}
\longleftrightarrow
\{(C_{\rm side},d),
(C_{\rm mid},d),
(C_{\rm side},2d)\}.
}
```

---

## 4. Aggregate identity

Let the side children be the parity-selected `V_1(x)` and `V_3(x)`, and let the middle children be all `V_{2,c}(x)`.

The full-color theorem gives

```math
\sum_{\rm side}H(C)=\mathcal L(B)
```

and

```math
\sum_{\rm middle}H(C)=\mathcal L(B).
```

Since

```math
H(2C)=\frac12H(C),
```

we have

```math
\sum_{\rm side}
\left(
H(C)+H(2C)
\right)
=
\frac32\mathcal L(B).
```

Adding the middle contribution gives

```math
\boxed{
\sum_{\rm side}
\left(
H(C)+H(2C)
\right)
+
\sum_{\rm middle}H(C)
=
\frac52\mathcal L(B).
}
```

The right side is exactly the total pair-edge weight of all parent three-AP occurrences.

---

## 5. Completed target packing

Let `Z` be a set of distinct terminal pair targets. Suppose each target `z\in Z` is assigned to a parent three-AP containing `z` as one of its three edges.

Map `z` to the corresponding full-color edge-capacity token of that progression.

The map is injective:

- one progression-edge token represents one unordered root pair;
- two distinct targets cannot be the same edge of the same progression.

Therefore

```math
\boxed{
\sum_{z\in Z}w(z)
\le
\sum_{\rm side}
\left(
H(C)+H(2C)
\right)
+
\sum_{\rm middle}H(C).
}
```

This is the pair-edge form of the `5/2` arithmetic-progression witness bound, but now the capacity is located explicitly on scale-descending child objects.

---

## 6. Why the doubled reserve is legitimate

For every side child `C`, the established valuation exclusions give pairwise disjoint sets

```math
C,
\qquad
2C,
\qquad
3C.
```

Hence the ordinary side token and doubled side reserve are distinct within one child state.

Both have a direct pair interpretation:

```text
C   stores one adjacent edge per progression;
2C  stores the outer edge per progression.
```

The third dilate remains unused by this edge dictionary and may be retained as additional obstruction or transport reserve.

---

## 7. Potential form

Define the local edge-capacity functional

```math
\mathcal E(C)
=
\begin{cases}
H(C)+H(2C)=\frac32H(C),&C\text{ side child},\\[4pt]
H(C),&C\text{ middle child}.
\end{cases}
```

Then

```math
\boxed{
\sum_{\rm full\mbox{-}color\ children}
\mathcal E(C)
=
\frac52\mathcal L(B).
}
```

This functional is state-independent and has an exact combinatorial meaning; it is not a fitted coefficient.

A whole-tree use still requires first-appearance or union semantics for edge-capacity tokens. The affine pair ledger supplies the natural token identity: every edge capacity is one unordered root pair.

---

## 8. Remaining terms

Combining sponsor transport with the edge-capacity dictionary leaves:

1. pair targets whose specified completion is outside the current parent;
2. genuine ambient holes and their four-AP witnesses;
3. transport-target collision reuse;
4. reuse of the same progression-edge capacity across different retained branches;
5. dyadic boundary transport when the completing progression crosses blocks.

For completed in-parent distinct targets, the coefficient gap is closed exactly.
