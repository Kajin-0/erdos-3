# Quadratic-level pair-fiber route

## Status

Proof-audit formulation.  This note moves the pair-fiber/shear strategy inside a high-rank quadratic level set.  This is necessary because the naive relative `U^3` lower bound from internal 4AP-freeness is only at the `beta^4` scale.

## Setup

Let

```math
q(x)=Q(x)+\ell(x)+c
```

be a quadratic polynomial on `F_p^n`, with associated symmetric bilinear form `B_Q`, and let

```math
V_t=\{x:q(x)=t\}.
```

Let

```math
B\subset V_t,
\qquad |B|/|V_t|=\beta,
\qquad b=1_B.
```

We consider internal 4APs contained entirely in `V_t`.

## Internal line geometry

For a line

```math
x,\ x+d,\ x+2d,\ x+3d
```

to lie in `V_t`, the polynomial

```math
i\mapsto q(x+id)
```

must be identically equal to `t` on `i=0,1,2,3`.  Since it has degree at most two and `p>4`, this is equivalent to the three conditions

```math
q(x)=t,
\qquad
Q(d)=0,
\qquad
B_Q(x,d)+\ell(d)=0.
```

Thus internal 4APs are parameterized by isotropic directions

```math
Q(d)=0
```

and basepoints

```math
x\in X_d:=V_t\cap\{B_Q(x,d)+\ell(d)=0\}.
```

For high-rank `q` and nondegenerate `d`, one expects

```math
|X_d|\approx p^{n-2}.
```

## Relative pair-fibers

For an admissible direction `d`, define the internal pair-fiber on the base slice `X_d` by

```math
P_d=\{x\in X_d: x\in B,\ x+d\in B\}.
```

Equivalently,

```math
p_d(x)=b(x)b(x+d)1_{X_d}(x).
```

If `B` is internally 4AP-free, then for every admissible nonzero `d`,

```math
P_d\cap(P_d-2d)=\emptyset
```

inside the same base slice `X_d`, because `x,x+d,x+2d,x+3d` would otherwise all belong to `B`.

This is the exact relative analogue of the global raw pair-fiber identity.

## Expected density

If `B` behaves randomly inside `V_t` at relative density `beta`, then for typical admissible `d`,

```math
|P_d|/|X_d|\approx \beta^2.
```

A random pair-fiber of density `beta^2` would have shifted self-overlap about

```math
\beta^4|X_d|.
```

Internal 4AP-freeness removes this overlap completely:

```math
\sum_{x\in X_d}p_d(x)p_d(x+2d)=0.
```

The averaged missing mass is therefore again at scale `beta^4`, but now distributed over the structured family of slices `X_d` and isotropic directions `d`.

## Why the relative route may be stronger than naive U3

Compressing the above identity to a single relative `U^3` norm loses the direction/slice information and yields only the naive scale

```math
\delta(\beta)\sim\beta^4.
```

The pair-fiber route keeps the stronger statement:

```math
\text{for many isotropic }d,
\quad
P_d\subset X_d,
\quad |P_d|/|X_d|\approx\beta^2,
\quad P_d\cap(P_d-2d)=\emptyset.
```

The question is whether this family of disjoint pair-fibers can exist in a high-rank quadratic level set without low-rank concentration.

## Relative variance branch

As in the global setting, if the internal pair densities

```math
\rho_d:=|P_d|/|X_d|
```

vary substantially over admissible directions, this should expose a structured density increment or low-rank bias.

Therefore the hard high-rank case should be:

```math
\rho_d\approx\beta^2
```

for most admissible isotropic `d`, while every such pair-fiber avoids its own `2d` translate.

## Candidate relative pair-fiber lemma

A useful theorem would be:

> Let `V_t` be a high-rank quadratic level set and `B subset V_t` have relative density `beta`.  Suppose `B` has no low-rank/linear density increment and its internal pair densities satisfy
>
> ```math
> \rho_d\approx\beta^2
> ```
>
> for most admissible isotropic directions `d`.  If
>
> ```math
> P_d\cap(P_d-2d)=\emptyset
> ```
>
> for all such `d`, then either
>
> ```math
> \beta\le C_p n^{-1-\epsilon_h},
> ```
>
> or `B` has a density increment of size `beta^{2-epsilon_F}` on a low-rank/quadratic refinement.

This is stronger than a relative inverse-theorem iteration and is exactly the kind of system-specific gain needed to cross the summability threshold.

## Interaction with Prendiville

Prendiville's theorem can still enter after the relative pair-fiber lemma produces structured relative `U^3` or quadratic correlation.  But the pair-fiber lemma is the likely source of the missing exponent gain.

In other words, the desired order is probably:

```math
\text{internal pair-fiber disjointness}
\Rightarrow
\text{strong relative structure}
\Rightarrow
\text{Prendiville inverse step if high-rank quadratic correlation is needed}.
```

not

```math
\text{internal 4AP-free}
\Rightarrow
\beta^4\text{ relative }U^3
\Rightarrow
\text{black-box inverse theorem}.
```

## Next research question

Can the high-rank incidence geometry of the slices

```math
X_d=V_t\cap\{B_Q(x,d)+\ell(d)=0\}
```

force expansion/mixing of the pair-fibers `P_d` strong enough that many exact disjointness conditions

```math
P_d\cap(P_d-2d)=\emptyset
```

are impossible above density

```math
\beta\gg n^{-1-\epsilon_h}?
```
