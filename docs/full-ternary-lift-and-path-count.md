# Full ternary lift and excess path count

## Status

Exact refinement of the affine-tree recursion.

The third-dilate expansion slack applies not only to the child fiber itself, but recursively to the entire lifted descendant set.  Consequently a depth-`h` path produces a root subset larger than the binary `2^h` cube by a polylogarithmic factor.

Combining this path-capacity loss with near-doubling of total normalized child mass forces a polylogarithmic excess in the number of depth-`h` recursive paths.

## Path setup

Let

```math
D_0\subseteq[1,M]
```

belong to the hereditary three-dilate class, and consider a depth-`h` predecessor path

```math
D_t=E_{q_t}(D_{t-1}),
\qquad
1\le t\le h.
```

Write

```math
M_t=\frac{M}{2^t}.
```

Then

```math
D_t\subseteq[1,M_t]
```

and

```math
D_t\cap2D_t=\varnothing.
```

## Full ternary lift

Define sets recursively from the bottom of the path by

```math
S_h=D_h
```

and

```math
S_{t-1}
=
(q_t+S_t)
\cup
(q_t+2S_t)
\cup
(q_t+3S_t).
```

Because `S_t subseteq D_t`, the predecessor relation gives

```math
S_{t-1}\subseteq D_{t-1}.
```

Therefore

```math
S_0\subseteq D_0.
```

The set `S_0` is precisely the set of all ternary affine forms

```math
q_1
+i_1q_2
+i_1i_2q_3
+\cdots
+\left(\prod_{r=1}^{h-1}i_r\right)q_h
+\left(\prod_{r=1}^{h}i_r\right)d,
```

where

```math
d\in D_h,
\qquad
i_1,\dots,i_h\in\{1,2,3\}.
```

Collisions between these forms are allowed.  The point is to lower-bound the size of their union.

## Expansion at every lift

Every `S_t` is a subset of `D_t`.  Since

```math
D_t\cap2D_t=\varnothing,
```

we also have

```math
S_t\cap2S_t=\varnothing.
```

The multiplicative-chain lemma therefore applies to `S_t subseteq [1,M_t]` and yields

```math
|S_t\cup2S_t\cup3S_t|
\ge
\left(
2+
\frac{1}{1+\lfloor\log_{3/2}M_t\rfloor}
\right)|S_t|.
```

Translation does not change cardinality, so

```math
|S_{t-1}|
\ge
a_t|S_t|,
```

where

```math
a_t
=
2+
\frac{1}{1+\lfloor\log_{3/2}M_t\rfloor}.
```

Iterating gives the exact path-capacity bound

```math
\boxed{
|S_0|
\ge
|D_h|\prod_{t=1}^h a_t.
}
```

Since `S_0 subseteq D_0`,

```math
\boxed{
|D_h|
\prod_{t=1}^h
\left(
2+
\frac{1}{1+\lfloor\log_{3/2}M_t\rfloor}
\right)
\le
|D_0|.
}
```

This is stronger than the binary disjoint-copy inequality

```math
2^h|D_h|\le|D_0|.
```

## Relation to the density-contraction product

Define

```math
c(M_t)=\frac{2}{a_t}.
```

Then

```math
\prod_{t=1}^h a_t
=
\frac{2^h}{G_h},
```

where

```math
G_h=\prod_{t=1}^h c(M_t)<1.
```

Thus

```math
\boxed{
\frac{2^h}{G_h}|D_h|
\le
|D_0|.
}
```

In natural-scale density notation

```math
\beta_t=\frac{|D_t|}{M_t},
```

this is exactly

```math
\boxed{
\beta_h\le G_h\beta_0.
}
```

The full ternary lift therefore gives a direct physical-space interpretation of the accumulated density contraction.

## Polylogarithmic capacity loss

The third-dilate expansion estimate gives

```math
G_h
\le
\left(
\frac{\log M_h+\log(3/2)}
{\log M+\log(3/2)}
\right)^\gamma,
```

with

```math
\gamma=\frac{\log(3/2)}{3\log2}>0.
```

Consequently

```math
\boxed{
|S_0|
\ge
2^h|D_h|
\left(
\frac{\log M+\log(3/2)}
{\log M_h+\log(3/2)}
\right)^\gamma.
}
```

So every deep path consumes more root capacity than its binary cube by a polylogarithmic factor.

## Excess number of recursive paths

Let `mathcal T_h` be the set of nonempty depth-`h` nodes and write

```math
S_h^{\mathrm{mass}}
=
\sum_{u\in\mathcal T_h}\beta_u.
```

Assume that along all nodes above depth `h`, the Roth error is proportionally small:

```math
\frac{r_3(M_t)}{M_t}
\le
\eta\beta_u,
\qquad
0\le\eta<1.
```

Then the recursive extension-load inequality gives

```math
S_h^{\mathrm{mass}}
\ge
[2(1-\eta)]^h\beta_0.
```

Every depth-`h` node satisfies the path-contraction bound

```math
\beta_u\le G_h\beta_0.
```

Therefore

```math
S_h^{\mathrm{mass}}
\le
|\mathcal T_h|G_h\beta_0.
```

Combining the two inequalities yields

```math
\boxed{
|\mathcal T_h|
\ge
\frac{[2(1-\eta)]^h}{G_h}.
}
```

Using the explicit estimate for `G_h`,

```math
\boxed{
|\mathcal T_h|
\ge
[2(1-\eta)]^h
\left(
\frac{\log M+\log(3/2)}
{\log M_h+\log(3/2)}
\right)^\gamma.
}
```

Thus persistent concentration forces not merely binary-scale branching, but a polylogarithmic excess of distinct recursive paths.

## Packing interpretation

Each path `pi in mathcal T_h` produces a lifted root set

```math
S_0(\pi)\subseteq D_0
```

with

```math
|S_0(\pi)|
\ge
\frac{2^h}{G_h}|D_\pi|.
```

The sum of these path-set sizes is therefore

```math
\sum_{\pi\in\mathcal T_h}|S_0(\pi)|
\ge
\frac{2^h}{G_h}
\sum_{\pi\in\mathcal T_h}|D_\pi|.
```

Since

```math
\sum_{\pi\in\mathcal T_h}|D_\pi|
=
M_hS_h^{\mathrm{mass}},
```

and `2^hM_h=M`,

```math
\boxed{
\sum_{\pi\in\mathcal T_h}|S_0(\pi)|
\ge
\frac{M}{G_h}S_h^{\mathrm{mass}}.
}
```

Under the low-error hypothesis this becomes

```math
\boxed{
\sum_{\pi\in\mathcal T_h}|S_0(\pi)|
\ge
\frac{M}{G_h}[2(1-\eta)]^h\beta_0.
}
```

Because all lifted sets lie inside the root `D_0`, whose size is `M beta_0`, their average overlap multiplicity is at least

```math
\boxed{
\frac{[2(1-\eta)]^h}{G_h}.
}
```

The same polylogarithmic excess that appears in the path count therefore appears as forced overlap among the full ternary lifts.

## Remaining bottleneck

The recursion has now produced quantitative slack beyond the exact binary balance:

```math
\text{forced average lift overlap}
\ge
\frac{[2(1-\eta)]^h}{G_h},
```

with

```math
G_h^{-1}
```

carrying a polylogarithmic gain.

To close the argument one needs an upper bound on overlap among full ternary affine lifts in a 4-AP-free root.  A bound matching the binary factor but losing less than the available `G_h^{-1}` gain would force a contradiction.

The next target is therefore:

> Prove that a point of a three-dilate 4-AP-free set cannot lie in too many depth-`h` full ternary lifts, or extract from high overlap two paths whose combined affine forms contain a four-term progression.
