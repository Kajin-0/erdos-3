# High-J parameter chain and the single-scale barrier

## Status

Quantitative audit of the current high-`J` structural route.

This note proves an exact dyadic extraction lemma from `J`-matrix energy, propagates its parameters through the direction-energy lemma, and identifies a fundamental limitation:

> At the natural skew-interaction scale, the resulting neighborhood obstruction has strength about `alpha^3`, not `alpha`.  Even maximal concentration under pair-regularity can recover at most the ordinary single-block `r_4(N)` scale.  Therefore this route cannot by itself prove the divergent reciprocal-sum conjecture; a genuinely cross-scale input is still required.

## Setup

Let `A` be a finite 4-AP-free set in an ambient group or interval model of size `N`, with

```math
|A|=a=\alpha N.
```

Let `D` be a direction set of size

```math
K=|D|.
```

For `d,e in D`, define

```math
J(d,e)
=
|\{x:x,x+d,x+2e,x+3e\in A\}|.
```

Write

```math
T=\sum_{d,e\in D}J(d,e),
\qquad
\mathcal E=\sum_{d,e\in D}J(d,e)^2,
```

and define

```math
\mu=\frac{T}{K^2},
\qquad
\kappa=\frac{K^2\mathcal E}{T^2}.
```

Thus

```math
\mathcal E=\kappa\frac{T^2}{K^2}
=\kappa K^2\mu^2.
```

Assume

```math
0\le J(d,e)\le U.
```

## Exact dyadic extraction lemma

Assume `kappa>1`.  Put

```math
L
=
1+\left\lceil\log_2\frac{U}{\mu}\right\rceil.
```

Then there exists a dyadic factor

```math
\lambda=2^r,
\qquad
1\le\lambda\le\frac{U}{\mu},
```

and a threshold

```math
\tau=\lambda\mu
```

such that the graph

```math
\mathcal G_\tau
=
\{(d,e)\in D\times D:\tau\le J(d,e)<2\tau\}
```

satisfies

```math
\boxed{
|\mathcal G_\tau|
\ge
\frac{\kappa-1}{4L\lambda^2}K^2.
}
```

### Proof

The contribution of entries below the mean is bounded by

```math
\sum_{J(d,e)<\mu}J(d,e)^2
\le
\mu\sum_{d,e}J(d,e)
=
\frac{T^2}{K^2}.
```

Therefore the entries with `J(d,e)>=mu` contribute at least

```math
\mathcal E-\frac{T^2}{K^2}
=
(\kappa-1)\frac{T^2}{K^2}.
```

There are at most `L` dyadic levels between `mu` and `U`, so one level contributes at least

```math
\frac{\kappa-1}{L}\frac{T^2}{K^2}.
```

On the level `tau<=J<2tau`, every squared entry is smaller than `4tau^2`.  Hence

```math
4\tau^2|\mathcal G_\tau|
\ge
\frac{\kappa-1}{L}\frac{T^2}{K^2}.
```

Using `tau=lambda T/K^2` gives the claimed bound.

Define the extracted graph density

```math
\delta
=
\frac{|\mathcal G_\tau|}{K^2}.
```

Then

```math
\boxed{
\delta
\ge
\frac{\kappa-1}{4L\lambda^2}.
}
```

The gain in threshold is therefore paid for quadratically in graph density.

## Direction-energy output

For signed directions `r`, write

```math
m(r)=|\{x:x,x+r\in A\}|,
```

and define

```math
D_\tau=\{r:m(r)\ge\tau\}.
```

The edge-to-difference lemma gives

```math
E(D_\tau)
\ge
\frac{|\mathcal G_\tau|^2}{K}
=
\delta^2K^3.
```

Therefore

```math
\boxed{
E(D_\tau)
\ge
\frac{(\kappa-1)^2}{16L^2\lambda^4}K^3.
}
```

Let

```math
H=|D_\tau|.
```

Since additive energy is at most the cube of the set size,

```math
E(D_\tau)\le H^3,
```

so

```math
\boxed{
H
\ge
\delta^{2/3}K
\ge
\left(\frac{\kappa-1}{4L\lambda^2}\right)^{2/3}K.
}
```

On the other hand, the total pair-mass identity

```math
\sum_r m(r)=a^2
```

gives

```math
\boxed{
H\le\frac{a^2}{\tau}.
}
```

## Structure-or-expansion with explicit parameters

Fix an expansion factor `Lambda>=1`.

### Expansion branch

If

```math
H>\Lambda K,
```

then the threshold-`tau` direction set has expanded by a factor larger than `Lambda`.

### Controlled-growth branch

If

```math
H\le\Lambda K,
```

then

```math
\frac{E(D_\tau)}{H^3}
\ge
\frac{\delta^2}{\Lambda^3}.
```

Thus the BSG input parameter is at least

```math
\boxed{
\theta
=
\frac{\delta^2}{\Lambda^3}
\ge
\frac{(\kappa-1)^2}{16L^2\lambda^4\Lambda^3}.
}
```

A quantitative BSG theorem then gives a subset

```math
R\subseteq D_\tau
```

whose relative size and doubling constant depend polynomially on `theta` in a standard formulation.  The important tradeoff is already visible before invoking any particular BSG constants:

```math
\tau=\lambda\mu
```

grows linearly in `lambda`, while the normalized direction energy decays as

```math
\theta\asymp\lambda^{-4}.
```

## Neighborhood obstruction

Every `r in R` has

```math
m(r)\ge\tau.
```

For each `x in A`, the neighborhood

```math
N_R(x)=\{r\in R:x+r\in A\}
```

is 4-AP-free.  Double counting therefore gives the exact inequality

```math
\boxed{
\frac{\tau}{a}
\le
\rho_4(R),
}
```

where `rho_4(R)` is the largest relative size of a 4-AP-free subset of `R`.

If BSG and a Freiman-type theorem place `R` inside a bounded-rank progression with controlled covering constant, then a bound

```math
r_4(M)\ll\frac{M}{(\log M)^c}
```

gives schematically

```math
\frac{\tau}{a}
\lesssim_{\theta}
(\log|R|)^{-c}.
```

The constants deteriorate as `theta` decreases.

## Natural-scale calibration

In a density-`alpha` pseudorandom model,

```math
\mu\asymp\alpha^4N.
```

Since

```math
a=\alpha N,
```

the normalized popularity threshold is

```math
\boxed{
\frac{\tau}{a}
\asymp
\lambda\alpha^3.
}
```

Ignoring all BSG/Freiman losses and optimistically taking `|R|` comparable to a power of `N`, the neighborhood obstruction could contradict 4-AP-freeness only if

```math
\boxed{
\lambda\alpha^3
\gtrsim
(\log N)^{-c}.
}
```

At the natural level `lambda=1`, this requires

```math
\alpha
\gtrsim
(\log N)^{-c/3}.
```

This is far stronger than what divergence of dyadic block densities guarantees.

Indeed, if `N=2^j`, then `log N` is comparable to `j`.  A divergent sequence such as

```math
\alpha_j=\frac{1}{j\log j}
```

satisfies

```math
\sum_j\alpha_j=\infty
```

but, for every fixed `0<c<1`,

```math
\alpha_j\ll j^{-c/3}.
```

Thus a natural-scale single-block contradiction does not reach the harmonic-divergence regime.

## Maximum concentration under pair regularity

Suppose the original direction set is pair-regular at scale `sigma`, meaning

```math
m(d)\le C\sigma
\qquad(d\in D).
```

Since

```math
J(d,e)\le m(d),
```

one has

```math
U\le C\sigma
```

and therefore

```math
\lambda
\le
\frac{C\sigma}{\mu}.
```

At the natural pair and skew scales

```math
\sigma\asymp\alpha^2N,
\qquad
\mu\asymp\alpha^4N,
```

this gives

```math
\lambda\lesssim\alpha^{-2}.
```

Consequently, even the largest possible normalized threshold satisfies

```math
\boxed{
\frac{\tau}{a}
\lesssim
\alpha.
}
```

So maximal `J` concentration under ordinary pair regularity can recover at most the ordinary finite-density obstruction

```math
\alpha\lesssim(\log N)^{-c}.
```

It cannot improve the summability exponent needed for the reciprocal-sum problem.

If `sigma` is much larger than `alpha^2N`, then the pair counts are already anomalously concentrated; that is a separate density-increment/Fourier branch rather than a gain supplied by the `J` argument.

## Single-scale barrier

The current chain

```math
J\text{-energy}
\Longrightarrow
\text{dyadic large-}J\text{ graph}
\Longrightarrow
\text{energy in }D_\tau
\Longrightarrow
\text{small-doubling popular directions}
\Longrightarrow
\frac{\tau}{a}\le\rho_4(R)
```

is valid and structurally meaningful.

However, at one scale it cannot by itself prove the full Erdős conjecture:

1. at natural `J` scale it produces `tau/a` of order `alpha^3`;
2. increasing `tau` by a factor `lambda` loses a factor `lambda^4` in the BSG energy parameter;
3. under pair regularity, even maximal concentration gives `tau/a` only of order `alpha`;
4. a blockwise `alpha`-level obstruction is exactly the known finite `r_4` barrier and does not force summability of the block densities.

## Required next step

A successful route must use information across many logarithmic scales rather than seek an isolated block contradiction.

The next target should be a cross-scale accumulation statement of the following form:

> If `A` is 4-AP-free and the dyadic block densities `alpha_j` have divergent sum, then the popular-direction structures or expansion branches generated on many scales cannot remain mutually incoherent.

The quantitative objective is to replace the single-scale cubic quantity

```math
\alpha_j^3
```

by an aggregate controlled by

```math
\sum_j\alpha_j,
```

or by another nonsummable expression forced by reciprocal divergence.

Without such a cross-scale gain, the high-`J` machinery remains a finite-block structural theorem rather than a route to the full conjecture.
