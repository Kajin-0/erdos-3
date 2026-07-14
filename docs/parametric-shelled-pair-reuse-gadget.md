# Parametric shell-valid latent-pair reuse gadget

## Status

Symbolic infinite family, with a dedicated exact certificate at `K=16`.

The family disproves pairwise latent-pair disjointness for recursive oriented
full-edge shells.  It also shows that shell-gap monotonicity alone cannot give
a one-step constant smaller than two.

---

## 1. The three-layer support

For an even integer `K>11`, define

```math
B_K
=
B_0
\cup
(K+B_1)
\cup
(2K+B_2),
```

where

```math
B_0=\{0,2\},
```

```math
B_1=\{3,7,9,11\},
```

and

```math
B_2=\{4,12,14,18,20,22\}.
```

Equivalently,

```text
B_K = {
  0, 2,
  K+3, K+7, K+9, K+11,
  2K+4, 2K+12, 2K+14, 2K+18, 2K+20, 2K+22
}.
```

---

## 2. Two recursive side shells

Use the first reference root

```math
r_1=2.
```

The three roots

```math
K+3,
\qquad
K+7,
\qquad
K+11
```

have current labels

```math
K+1,
\qquad
K+5,
\qquad
K+9.
```

Their outward reflection completions about `r_1` are

```math
2K+4,
\qquad
2K+12,
\qquad
2K+20,
```

all of which belong to `B_K`.

Use the second reference root

```math
r_2=0.
```

The roots

```math
K+7,
\qquad
K+9,
\qquad
K+11
```

have labels

```math
K+7,
\qquad
K+9,
\qquad
K+11,
```

with outward completions

```math
2K+14,
\qquad
2K+18,
\qquad
2K+22.
```

Because `K` is even, all six side labels are odd.  They therefore belong to
the parity-even first-side class.

If `K` is a power of two and `K>11`, both triples lie in the single standard
dyadic shell

```math
[K,2K).
```

Each is a three-term progression:

```math
K+1,\ K+5,\ K+9
```

has step `4`, and

```math
K+7,\ K+9,\ K+11
```

has step `2`.  Hence both shells are recursive.

Their root sets intersect in

```math
\{K+7,K+11\}.
```

Thus the physical latent pair

```math
\boxed{e_K=\{K+7,K+11\}}
```

has gap `4`, weight `1/4`, and recursive-shell multiplicity exactly two in
this displayed subfamily.

---

## 3. Four-AP-freeness for all large `K`

Every point of `B_K` has the form

```math
aK+b,
\qquad
 a\in\{0,1,2\},
```

with `b` drawn from the corresponding finite offset layer `B_a`.

Assume `K>44`.  If four ordered points

```math
x_i=a_iK+b_i,
\qquad 0\le i\le3,
```

formed a four-term arithmetic progression, then

```math
(a_0+a_2-2a_1)K
=
2b_1-b_0-b_2
```

and

```math
(a_1+a_3-2a_2)K
=
2b_2-b_1-b_3.
```

Every right-hand side has absolute value at most `44`.  Since the coefficient
of `K` is integral, `K>44` forces

```math
a_0+a_2=2a_1,
\qquad
a_1+a_3=2a_2.
```

Therefore `a_0,a_1,a_2,a_3` themselves form a four-term arithmetic
progression in `{0,1,2}`.  The only possibility is

```math
a_0=a_1=a_2=a_3.
```

The four points would then lie in one offset layer.  Direct inspection gives:

```text
B_0={0,2}                         is four-AP-free;
B_1={3,7,9,11}                    is four-AP-free;
B_2={4,12,14,18,20,22}            is four-AP-free.
```

Hence

```math
\boxed{B_K\text{ is four-AP-free for every }K>44.}
```

In particular, the conclusion holds for every dyadic `K>=64`.

---

## 4. Standard dyadic placement

For dyadic `K>=64`, translate `B_K` by `4K`.  Since

```math
0\le\min B_K
```

and

```math
\max B_K=2K+22<3K,
```

we obtain

```math
4K+B_K\subseteq[4K,8K).
```

Thus the parent is a standard dyadic block of base `4K`, while both recursive
children lie in the shell `[K,2K)`.  The reuse gadget therefore has exact
parent-to-child scale ratio `4`.

The shared pair gap remains

```math
D=4,
```

so

```math
\frac{D}{M}=\frac4K\longrightarrow0.
```

Latent reuse is therefore possible at arbitrarily small normalized pair gap.

---

## 5. Certified small instance

At `K=16`, the support is

```text
0,2,19,23,25,27,36,44,46,50,52,54.
```

The two recursive shell triples are

```text
reference 2: tokens 17,21,25; roots 19,23,27;
reference 0: tokens 23,25,27; roots 23,25,27.
```

They share the latent pair `{23,27}`.  The dedicated verifier checks exact
four-AP-freeness, shell assignment, affine root provenance, recursiveness, and
pair intersection.

---

## 6. Strategic consequence

The false target was

```text
recursive oriented child shells are pairwise latent-pair-disjoint.
```

The correct target must permit reuse but charge its geometry.  The gadget has
three separated coefficient layers and two reference roots.  More generally,
a common recursive root configuration `Q` carried by a reference set `R`
forces the reflected layer family

```math
2Q-R.
```

When `Q` is a three-term progression, this is a union of three equal translates
of `-R`.  Hence repeated latent-pair use is naturally coupled to the existing
three-translate and aligned-diamond obstruction theory.

The next theorem should bound weighted reuse by the scale cost of these forced
translate layers.  Neither a uniform multiplicity-one claim nor gap-ratio
monotonicity alone can succeed.
