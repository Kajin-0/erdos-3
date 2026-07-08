# Isotropic chord bilinear normal form

## Status

Proof-audit reduction.  This note normalizes the isotropic chord operator on a quadratic level set and identifies the precise finite-geometry graph whose spectral gap/mixing properties need to be used.

## Setup

Let

```math
q(x)=Q(x)+\ell(x)+c
```

on `F_p^n`, with `p` odd.  Complete the square after quotienting out the radical of the bilinear form.  In the high-rank branch, the radical/low-rank part is treated as an escape branch, so the model case is a nondegenerate homogeneous quadratic form

```math
Q:F_p^n\to F_p
```

with associated symmetric bilinear form

```math
B(x,y)=Q(x+y)-Q(x)-Q(y).
```

Let

```math
V_t=\{x:Q(x)=t\}.
```

The affine/linear terms can be restored by translating the level set and replacing `t` by the shifted value.

## Chord condition in bilinear form

For `x,y in V_t`, write

```math
d=y-x.
```

The internal-line condition is

```math
Q(d)=0.
```

But

```math
Q(y-x)=Q(y)+Q(x)-B(x,y)=2t-B(x,y).
```

Therefore, on `V_t`,

```math
Q(y-x)=0
\quad\Longleftrightarrow\quad
B(x,y)=2t.
```

Thus the isotropic chord graph is the fixed-bilinear-incidence graph

```math
x,y\in V_t,
\qquad
B(x,y)=2t.
```

This is the correct normal form for the chord operator.

## Consequence: classical finite-geometry graph

The chord graph is not an arbitrary sparse graph.  It is the graph induced on the quadric

```math
Q(x)=t
```

by a fixed value of the polar bilinear form:

```math
B(x,y)=2t.
```

For nonzero `t` and nondegenerate `Q`, this is a classical orthogonal-incidence graph.  For `t=0`, extra isotropic-cone phenomena may appear and should be handled separately or placed into a degeneracy branch.

## Expected sizes

In the nondegenerate high-rank model:

```math
|V_t|\approx p^{n-1}.
```

For fixed `x in V_t`, the neighbor set is

```math
N(x)=\{y:Q(y)=t,\ B(x,y)=2t\}.
```

This is an intersection of a quadric with a hyperplane.  Generically,

```math
|N(x)|\approx p^{n-2}.
```

Thus the graph has density roughly

```math
p^{-1}
```

inside `V_t x V_t`.

## Spectral-gap target

Let `M` be the normalized adjacency operator

```math
(MF)(x)=E_{y\in V_t: B(x,y)=2t}F(y).
```

The desired high-rank mixing statement is:

```math
\|MF-E_{V_t}F\|_{L^2(V_t)}\le \lambda\|F-E_{V_t}F\|_{L^2(V_t)}
```

with

```math
\lambda\ll p^{-c n}
```

or at least a power saving strong enough that failures of mixing are forced to come from the excluded low-rank/radical structure.

A classical Weil/exponential-sum bound for nondegenerate quadrics should give a very small normalized second eigenvalue, heuristically around

```math
\lambda\sim p^{-(n-2)/2}
```

up to constants depending on `p` and Witt type.

## Why this matters

If such a spectral gap holds, then for any `B subset V_t` of relative density `beta`,

```math
E_{x\in B}(Mb)(x)=\beta+O(\lambda/\beta^{1/2})
```

in averaged form.  In particular, for densities as large as

```math
\beta\gg n^{-1-\epsilon},
```

the chord graph is far more mixed than needed, since `lambda` is exponentially small in `n`.

Thus the obstruction cannot be the first-order chord graph failing to mix.  It must lie in the finer directional pair-fiber constraints

```math
P_d\cap(P_d-2d)=\emptyset
```

inside the slices `X_d`.

## Directional refinement still needed

The chord operator averages over all isotropic directions at once.  It controls the total number of admissible edges in `B`, hence the average pair density

```math
E_d\rho_d\approx\beta^2.
```

But it does not by itself rule out the following hard case:

```math
\rho_d\approx\beta^2\text{ for most }d,
\qquad
P_d\cap(P_d-2d)=\emptyset\text{ for every }d.
```

The missing ingredient is a second-order mixing statement for the family of line slices `X_d`, not just for the one-step chord graph.

## Candidate second-order operator

For each isotropic `d`, define the shift operator on `X_d`

```math
T_d x=x+2d.
```

The obstruction is

```math
\langle 1_{P_d},1_{P_d}\circ T_d\rangle_{X_d}=0
```

where random behavior predicts `beta^4`.

The next operator should average these slice-shift correlations:

```math
\mathcal S(B)=E_{d:Q(d)=0}\ E_{x\in X_d}
1_B(x)1_B(x+d)1_B(x+2d)1_B(x+3d).
```

This is exactly the internal 4AP count, but now viewed as a second-order statistic of the chord graph.

## Updated bottleneck

The first-order isotropic chord graph probably has a strong spectral gap in the high-rank case.  Therefore the exponent problem is not first-order edge mixing.

The bottleneck is a **second-order directional mixing theorem**:

> If `B subset V_t` has relative density `beta` and no low-rank/quadratic density increment, then the pair-fiber shifts inside the slices `X_d` mix well enough that
>
> ```math
> E_d\langle 1_{P_d},1_{P_d}\circ T_d\rangle_{X_d}
> \gtrsim \beta^4.
> ```
>
> To beat the reciprocal-sum threshold, one needs this conclusion or a structured escape for every
>
> ```math
> \beta\gg n^{-1-\epsilon}.
> ```

## Next research question

Can the second-order directional mixing theorem be reduced to a known expander-mixing or association-scheme estimate for orthogonal spaces?  If yes, the high-rank branch may yield a direct independence bound.  If no, the problem returns to the spectral shear/Prendiville route.
