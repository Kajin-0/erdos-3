# Collision rectangle aspect identity

## Status

Symbolic pointwise refinement of the reference-gap collision charge.

Every extra occurrence of one physical child pair determines a unique
reference pair and an explicit parent completion rectangle. The repeated pair
weight factors exactly into reference-pair weight times a dimensionless aspect
ratio.

---

## 1. Reused pair and reference pair

Fix a physical child root pair

```math
e=\{u,v\},
\qquad u<v,
\qquad D=v-u.
```

Suppose one oriented child family carries `e` at two references

```math
r_0<r_1.
```

Define the reference pair

```math
f=\{r_0,r_1\},
\qquad
\delta=r_1-r_0.
```

The pair weights are

```math
w(e)=\frac1D,
\qquad
w(f)=\frac1\delta.
```

Therefore the exact aspect-ratio identity is

```math
\boxed{
w(e)
=
\frac\delta D\,w(f).
}
```

No inequality or fitted coefficient is involved.

---

## 2. Side completion rectangle

For a side child, the parent contains

```math
x_i=2u-r_i,
\qquad
y_i=2v-r_i,
\qquad i\in\{0,1\}.
```

The four completion points satisfy

```math
y_i-x_i=2D,
```

and

```math
x_0-x_1=y_0-y_1=\delta.
```

Thus they form an affine rectangle with side lengths

```math
2D
\quad\text{and}\quad
\delta.
```

The rectangle aspect ratio is

```math
\frac\delta{2D}.
```

The four corners form a four-term arithmetic progression exactly when the two
side lengths are in ratio `2` or `1/2`. Hence four-AP-freeness excludes

```math
\boxed{\delta=D\quad\text{and}\quad\delta=4D.}
```

---

## 3. Middle completion rectangle

For a middle child, the parent completions are

```math
x_i=2r_i-u,
\qquad
y_i=2r_i-v.
```

Now

```math
|x_i-y_i|=D
```

and the reference displacement becomes

```math
|x_1-x_0|=|y_1-y_0|=2\delta.
```

The rectangle side lengths are `D` and `2delta`. Four-AP-freeness excludes

```math
\boxed{\delta=D/4\quad\text{and}\quad\delta=D}
```

in the integral cases.

---

## 4. Doubled-side completion rectangle

For a doubled-side child, the parent midpoints are

```math
x_i=\frac{r_i+u}{2},
\qquad
y_i=\frac{r_i+v}{2}.
```

The rectangle side lengths are

```math
D/2
\quad\text{and}\quad
\delta/2.
```

Therefore four-AP-freeness excludes

```math
\boxed{\delta=D/2\quad\text{and}\quad\delta=2D}
```

when integral.

---

## 5. Rectangle token

Choose one deterministic base reference `r_0` in every reuse fiber. Every
additional reference `r` creates the rectangle token

```math
\mathfrak R(e;r_0,r)
=
(e,\{r_0,r\}).
```

Its natural data are

```text
reused physical pair e;
reference pair f;
pair gap D;
reference gap delta;
aspect class floor(log_2(delta/D));
child type and shell scale;
completion rectangle corners.
```

Within one fixed reuse fiber, the map from additional references to rectangle
tokens is injective.

The repeated mass identity becomes

```math
\boxed{
R_{\rm fiber}(e)
=
\sum_{r\ne r_0}
\frac{|r-r_0|}{D}
\frac1{|r-r_0|}.
}
```

This is exactly the aspect-ratio decomposition of the reference-gap lemma.

---

## 6. Near and far rectangles

The identity separates collision debt into geometric regimes.

### Near regime

If

```math
\delta\le D,
```

then

```math
w(e)\le w(f).
```

The repeated pair can be paid directly by the reference pair, subject to a
first-appearance rule for rectangle tokens.

### Far regime

If

```math
2^kD<\delta\le2^{k+1}D,
```

then

```math
w(e)
\le
2^{k+1}w(f).
```

The coefficient is precisely the dyadic rectangle aspect. These are the
scale-separated terms that must be transported or released when the pair-gap
to shell-scale ratio grows.

---

## 7. Whole-tree interface

The collision problem has now been reduced from an unlabeled multiplicity to
a set of concrete affine rectangles. A valid treewise potential may use
first-appearance rectangle tokens and a scale coefficient depending on

```math
\rho=\frac\delta D.
```

The remaining obligations are:

1. bound reuse of the same rectangle token across distinct witness
   configurations;
2. show that large-aspect rectangles either descend to lower-scale
   reference-difference reserves or create completion/extension obstructions;
3. merge near-aspect rectangle payment with the existing physical pair union;
4. preserve the distinction between ambient external roots and genuine holes.

The key gain is exactness: every unit of repeated pair mass now has a named
reference pair, a named rectangle, and a dimensionless aspect ratio.
