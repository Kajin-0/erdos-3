# Canonical near-pair / far-fiber transfer

## Status

State-independent refinement of the Euclidean anchor-step collision split.

Every repeated fixed-step occurrence is assigned either to one translated
physical pair or to one strictly lower-scale four-AP-free step fiber. Collisions
of translated pairs are themselves resolved into lower-scale step fibers.
No coefficient-two activated-pair union bound is required.

---

## 1. Canonical collision incidences

Let

```math
B\subseteq[N,2N)
```

be four-AP-free, and let `A` be any selected family of distinct three-AP
occurrences `(p,d)` inside `B`.

For each used step `d`, choose the minimum start

```math
a_d=\min\{p:(p,d)\in\mathcal A\}.
```

Every nonbase occurrence with start `p>a_d` defines

```math
\delta=p-a_d.
```

The parent contains the two rows

```math
\{a_d,a_d+d,a_d+2d\}
```

and

```math
\{p,p+d,p+2d\}.
```

The incidence weight is `1/d`.

---

## 2. Far incidences

Call the incidence far when

```math
d<\delta.
```

For the canonical anchor pair

```math
f=\{a_d,p\},
```

define

```math
S_f^{\rm far}
=
\{d:a_d=\min f,\ \max f\text{ is a selected step-}d\text{ start},\ d<|f|\}.
```

Every far incidence belongs to exactly one such fiber, and

```math
\boxed{
R_{\rm far}(\mathcal A)
=
\sum_fH(S_f^{\rm far}).
}
```

Each `S_f^far` is four-AP-free because

```math
\min f+S_f^{\rm far}\subseteq B.
```

Every fiber step is below `N/2`; after standard dyadic resolution, all shells
have base at most `N/4`.

---

## 3. Near incidences and translated pairs

Call the incidence near when

```math
\delta\le d.
```

Translate the anchor pair to the middle row:

```math
g(d,p)
=
\{a_d+d,p+d\}.
```

This is a physical parent pair because both endpoints belong to `B`. Its gap
is still `delta`, so

```math
w(g(d,p))
=
\frac1\delta
\ge
\frac1d.
```

Thus one first appearance of the translated pair can pay one near collision
incidence.

For a fixed anchor pair `f`, distinct steps produce distinct translated pairs:
`f+d=f+d'` implies `d=d'`.

---

## 4. Collisions at one translated pair

Different anchor pairs and steps may reach the same translated target pair

```math
g=\{x,y\}.
```

Define its preimage step set

```math
D_g
=
\{d:g=\{a_d+d,p+d\}\text{ for one near collision incidence}\}.
```

The map from an incidence to `(g,d)` is injective: the original anchor pair is
recovered as

```math
g-d=\{x-d,y-d\}.
```

The set `D_g` is four-AP-free because

```math
x-D_g\subseteq B.
```

Every `d in D_g` satisfies

```math
d\ge y-x.
```

Choose one deterministic base step

```math
d_0(g)=\min D_g.
```

The pair `g` pays its base incidence:

```math
\frac1{d_0(g)}
\le
\frac1{y-x}
=
w(g).
```

The remaining near collision mass is exactly the harmonic mass of

```math
D_g^+
=
D_g\setminus\{d_0(g)\}.
```

Therefore

```math
\boxed{
R_{\rm near}(\mathcal A)
\le
\sum_{g:D_g\ne\varnothing}w(g)
+
\sum_gH(D_g^+).
}
```

The translated target pairs `g` are distinct in the first sum.

Every residual set `D_g^+` is four-AP-free and lies below `N/2`, hence resolves
into shells of base at most `N/4`.

---

## 5. Complete collision-transfer row

Let

```math
G_{\rm near}
=
\{g:D_g\ne\varnothing\}.
```

Combining near and far incidences gives

```math
\boxed{
R_{\rm step}(\mathcal A)
\le
J(G_{\rm near})
+
\sum_gH(D_g^+)
+
\sum_fH(S_f^{\rm far}).
}
```

Every repeated occurrence is accounted for exactly once before the one
inequality that lets `g` pay its base step.

The outputs have two types:

```text
distinct physical pairs G_near;
strictly lower-scale four-AP-free fibers D_g^+ and S_f^far.
```

No light/heavy threshold and no factor-two pair-union estimate are needed.

---

## 6. Monotone geometry of the near pair

The translated pair advances both endpoints by `d`:

```math
\min g=a_d+d>a_d.
```

It is the middle vertical edge of the two-row completion rectangle. The parent
also contains the outer translate

```math
g+d=\{a_d+2d,p+2d\}.
```

Thus every activated near pair carries an explicit forward rectangle witness.
This interfaces directly with sponsor-pair forward transport and rectangle
completion.

If the same translated pair is targeted several times, all excess is removed
from pair capacity and placed in the lower-scale set `D_g^+`. Pair reuse is
not left implicit.

---

## 7. First-step plus collision decomposition

Let

```math
E_{\rm step}
=
\{\{a_d,a_d+d\}:d\text{ is used}\}.
```

These are distinct physical pairs and carry the base occurrence mass.
Together with the collision row,

```math
\boxed{
L(\mathcal A)
\le
J(E_{\rm step})
+
J(G_{\rm near})
+
\sum_gH(D_g^+)
+
\sum_fH(S_f^{\rm far}).
}
```

Potential overlap between `E_step` and `G_near` is explicit physical-pair
reuse and can be merged by the affine first-appearance pair ledger. It is the
only pair-level overlap in this row.

All remaining mass is genuine recursive output at at most one quarter of the
parent dyadic base.

---

## 8. Strategic consequence

The arbitrary selected AP occurrence family now has a threshold-free transfer:

```text
base occurrence      -> distinct step edge;
near repeated row    -> distinct forward translated pair;
near target collision-> lower-scale preimage-step fiber;
far repeated row     -> lower-scale anchor-pair step fiber.
```

This is stronger than the light/heavy theorem. The light/heavy view remains a
useful stopping interpretation, while the canonical near-pair row gives exact
first-appearance semantics and resolves near-only heavy fibers automatically.

The next whole-tree obligation is to merge overlaps between step-edge and
translated-pair first appearances, then apply sponsor-pair transport to the
resulting distinct activated pair union.
