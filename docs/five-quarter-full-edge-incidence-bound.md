# Five-quarter full-edge incidence bound

## Status

State-independent improvement of the physical-pair incidence bound for every finite four-AP-free set.

If

```math
J(P)=\sum_{x<y\atop x,y\in P}\frac1{y-x}
```

and

```math
\mathcal L_3(P)
=
\sum_{\{a,a+d,a+2d\}\subseteq P}\frac1d,
```

then

```math
\boxed{
\frac52\mathcal L_3(P)
\le
\frac54J(P).
}
```

The previous coefficient `2` follows only from the maximum pair-incidence multiplicity. The stronger coefficient `5/4` uses four-AP-freeness a second time to control the energy of pairs having multiplicity two.

---

## 1. Full-edge incidence identity

For every three-term progression

```math
Q=\{a,a+d,a+2d\}\subseteq P,
```

its three physical edge weights sum to

```math
\frac1d+\frac1d+\frac1{2d}
=
\frac5{2d}.
```

Let

```math
m(e)
```

be the number of three-term progressions in `P` containing the physical pair `e` as an edge. Then

```math
\boxed{
\frac52\mathcal L_3(P)
=
\sum_{e\in\binom P2}m(e)w(e),
}
```

where

```math
w(e)=\frac1{\operatorname{gap}(e)}.
```

Four-AP-freeness gives

```math
m(e)\le2.
```

---

## 2. Structure of a duplicated pair

Fix a pair

```math
e=\{x,y\},
\qquad y-x=D,
```

with

```math
m(e)=2.
```

A pair has at most three possible three-AP completions:

```text
left adjacent endpoint  x-D;
right adjacent endpoint y+D;
midpoint                 x+D/2, when D is even.
```

Both adjacent endpoint completions cannot lie in `P`, because

```math
x-D,\ x,\ y,\ y+D
```

would be a four-term progression.

Therefore multiplicity two forces exactly:

```text
one adjacent-edge occurrence;
one outer-edge occurrence.
```

In particular `D=2d` is even and

```math
x+d\in P.
```

Write the duplicated pair as

```math
\{x,x+2d\}.
```

---

## 3. Two-half map

Associate to every duplicated pair its two adjacent half pairs:

```math
h_-(e)=\{x,x+d\},
```

```math
h_+(e)=\{x+d,x+2d\}.
```

Each half pair lies in `P` and has weight

```math
w(h_-(e))=w(h_+(e))=\frac1d=2w(e).
```

Thus the two images have total energy

```math
w(h_-(e))+w(h_+(e))=4w(e).
```

---

## 4. Injectivity of the two-half map

Consider the tagged map

```math
(e,\sigma)
\longmapsto
h_\sigma(e),
\qquad
\sigma\in\{-,+\}.
```

It is injective.

For a fixed orientation, one half pair determines its outer pair uniquely.

The only possible cross-orientation collision would have one pair

```math
\{u,u+r\}
```

simultaneously equal to:

```text
the left half of {u,u+2r};
the right half of {u-r,u+r}.
```

Then the four points

```math
u-r,\ u,\ u+r,\ u+2r
```

would all lie in `P`, forming a four-term progression. This is impossible.

Hence all half-pair images of duplicated pairs are distinct physical pairs.

---

## 5. Duplicate-energy bound

Let

```math
D(P)
=
\sum_{e:m(e)=2}w(e)
```

be the pair energy carried by duplicated incidences.

The injective two-half map gives a physical pair subfamily of total energy

```math
4D(P).
```

Since it is a subfamily of `binom(P,2)`,

```math
\boxed{
4D(P)\le J(P).
}
```

Equivalently,

```math
\boxed{
D(P)\le\frac14J(P).
}
```

---

## 6. Five-quarter theorem

Let

```math
U(P)=\{e:m(e)\ge1\}
```

be the physical edge-incidence union. Because `m(e)` is one or two,

```math
\frac52\mathcal L_3(P)
=
J(U(P))+D(P).
```

Using

```math
J(U(P))\le J(P)
```

and the duplicate-energy bound,

```math
\begin{aligned}
\frac52\mathcal L_3(P)
&=J(U(P))+D(P)\\
&\le J(P)+\frac14J(P).
\end{aligned}
```

Therefore

```math
\boxed{
\frac52\mathcal L_3(P)
\le
\frac54J(P).
}
```

---

## 7. Exact small-box validation

The independent verifier exhausts all

```text
22,601
```

four-AP-free subsets of `[1,16]` and checks:

```text
pair three-AP incidence at most two;
every duplicated pair is an outer and adjacent edge;
the tagged two-half map is injective;
half-pair energy equals four times duplicate energy;
duplicate energy is at most one quarter of total pair energy;
full-edge production is at most five quarters of pair energy.
```

The maximum observed ratio through `[1,16]` is

```math
\frac{45}{43}
```

on

```math
\{1,2,3,5\}.
```

This finite maximum does not establish the optimal universal coefficient. The theorem certifies `5/4`; it does not claim sharpness.

Primary executable:

```text
src/verify_full_edge_incidence_five_quarter_bound.py
```

---

## 8. Owner-exponent consequence

For the monomial child potential

```math
\mathcal V_{p,\lambda}(Q)
=
L^p\bigl(H(Q)+\lambda J(Q)\bigr),
```

complete next-generation full-edge production is paid whenever

```math
\lambda\ge\frac54.
```

Two latent owners may both occur at child half-scale. Collision-free owner packing requires

```math
2\lambda\,2^{-p}\le1.
```

Taking the certified production coefficient

```math
\lambda=\frac54
```

gives the certified monomial threshold

```math
\boxed{
p\ge p_0:=\log_2\!\left(\frac52\right).
}
```

At the boundary exponent,

```math
2^{p_0}=\frac52,
```

so:

```math
2\lambda2^{-p_0}=1,
```

```math
(1+\lambda)2^{-p_0}=\frac9{10},
```

and the established first-appearance coefficient is

```math
c_{p_0}
=
\frac3{4^{p_0}}
+
\frac1{2^{p_0+1}}
=
\frac{12}{25}+\frac15
=
\boxed{\frac{17}{25}}.
```

Thus first appearance is strictly contracting, current-latent reuse is strictly contracting, and latent-latent reuse is nonexpanding at `p_0`.

This is the first exponent certified by the `5/4` incidence theorem and the monomial owner-packing argument. It is not claimed to be globally optimal.
