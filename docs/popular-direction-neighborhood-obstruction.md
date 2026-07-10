# Popular-direction neighborhood obstruction

## Status

Exact transfer lemma from structured popular directions back to the original set `A`.

This improves the earlier direct-density transfer.  One does not need the popularity threshold `tau` to exceed the ambient pair baseline `|A|^2/N`.  Instead, every point-neighborhood in the direction set is itself 4-AP-free, so any structured direction set with small internal 4-AP-free density creates a contradiction.

## Setup

Let `A subset Z` be 4-AP-free.  For a signed direction `r`, define

```math
m(r)=|\{x\in A:x+r\in A\}|.
```

Let `R` be a finite direction set.  For each `x in A`, define the direction neighborhood

```math
N_R(x)=\{r\in R:x+r\in A\}.
```

Equivalently,

```math
N_R(x)=R\cap(A-x).
```

## Point-neighborhood lemma

For every `x in A`, the set `N_R(x)` is 4-AP-free as a subset of the integers.

### Proof

If `N_R(x)` contained a nontrivial four-term progression

```math
r,\ r+q,\ r+2q,\ r+3q,
\qquad q\ne0,
```

then

```math
x+r,\ x+r+q,\ x+r+2q,\ x+r+3q
```

would be a nontrivial four-term progression in `A`, contradiction.

Thus

```math
\boxed{N_R(x)\text{ is 4-AP-free for every }x\in A.}
```

## Incidence identity

Double counting pairs `(x,r)` with

```math
x\in A,
\qquad
r\in R,
\qquad
x+r\in A
```

gives

```math
\boxed{
\sum_{x\in A}|N_R(x)|
=
\sum_{r\in R}m(r).
}
```

If every direction in `R` is `tau`-popular,

```math
m(r)\ge\tau
\qquad(r\in R),
```

then

```math
\sum_{x\in A}|N_R(x)|
\ge
\tau|R|.
```

Hence some `x in A` satisfies

```math
\boxed{
|N_R(x)|
\ge
\frac{\tau}{|A|}|R|.
}
```

This is stronger than merely locating `A` densely inside one translate of `R`: the dense subset obtained inside `R` is known to be 4-AP-free.

## Intrinsic extremal-density formulation

Define

```math
\rho_4(R)
=
\max\left\{
\frac{|B|}{|R|}:
B\subseteq R,
\ B\text{ is 4-AP-free}
\right\}.
```

Since each `N_R(x)` is 4-AP-free,

```math
|N_R(x)|\le\rho_4(R)|R|.
```

Combining this with the incidence lower bound yields the exact obstruction

```math
\boxed{
\frac{\tau}{|A|}
\le
\rho_4(R).
}
```

Equivalently:

> A 4-AP-free set cannot support a direction set `R` in which every direction has pair multiplicity at least `tau` if the internal 4-AP-free density of `R` is smaller than `tau/|A|`.

This is the correct transfer target for the small-doubling direction branch.

# Consequence for a generalized arithmetic progression

Suppose `R` is contained in a proper generalized arithmetic progression

```math
P
=
\left\{
a+n_1v_1+\cdots+n_sv_s:
0\le n_i<L_i
\right\}
```

of rank `s`, with

```math
|P|\le C|R|.
```

Let

```math
L_{\max}=\max_i L_i.
```

Since `P` is proper,

```math
|P|=\prod_{i=1}^sL_i,
```

and therefore

```math
L_{\max}\ge |P|^{1/s}\ge |R|^{1/s}.
```

Let `B subset R` be 4-AP-free.  View `B` inside the coefficient box of `P`.  Fix every coordinate except one having length `L_max`.  Along each resulting line, `B` is a 4-AP-free subset of an interval of length `L_max`.

Therefore

```math
|B|
\le
\frac{|P|}{L_{\max}}r_4(L_{\max}),
```

where `r_4(L)` is the largest size of a 4-AP-free subset of an interval of length `L`.

Dividing by `|R|` gives

```math
\boxed{
\rho_4(R)
\le
C\frac{r_4(L_{\max})}{L_{\max}}.
}
```

Thus the incidence obstruction becomes

```math
\boxed{
\frac{\tau}{|A|}
\le
C\frac{r_4(L_{\max})}{L_{\max}}.
}
```

## Using a polylogarithmic r4 bound

If one inserts a bound of the form

```math
r_4(L)
\le
C_0\frac{L}{(\log L)^c},
```

then

```math
\frac{\tau}{|A|}
\le
\frac{CC_0}{(\log L_{\max})^c}.
```

Since

```math
\log L_{\max}
\ge
\frac1s\log|R|,
```

one obtains

```math
\boxed{
\frac{\tau}{|A|}
\le
CC_0s^c(\log|R|)^{-c}.
}
```

Consequently, for fixed progression rank and covering constant, a sufficiently large set of `tau`-popular structured directions is impossible.

# Application to the high-J direction-energy branch

The direction-energy lemma produces a threshold-popular set

```math
D_\tau=\{r:m(r)\ge\tau\}
```

with large additive energy.  In the controlled-growth branch, BSG gives a substantial subset

```math
R\subseteq D_\tau
```

with small doubling.

A Freiman-type theorem in the integers then places `R` inside a bounded-rank generalized arithmetic progression `P` of size at most a controlled multiple of `|R|`.

The neighborhood obstruction gives

```math
\frac{\tau}{|A|}
\le
\rho_4(R)
\ll_{K}
(\log|R|)^{-c},
```

where the implicit constants depend on the small-doubling parameter.

This yields a genuine contradiction whenever the structured popular-direction set is large enough relative to the normalized threshold `tau/|A|`.

# Why this improves the previous transfer

The earlier direct localization only showed that some translate `x+R` contains `A` with relative density at least

```math
\frac{\tau}{|A|}.
```

Comparing this to the ambient density required

```math
\tau>\frac{|A|^2}{N},
```

which is far above the natural skew-interaction scale.

The neighborhood obstruction removes that requirement.  Even when

```math
\frac{\tau}{|A|}\ll\frac{|A|}{N},
```

a contradiction is possible because the neighborhood is not an arbitrary dense subset of `R`; it must remain 4-AP-free inside a highly structured set.

# Current quantitative bottleneck

At the natural skew scale

```math
\tau\approx\alpha^4N,
\qquad
|A|=\alpha N,
```

one has

```math
\frac{\tau}{|A|}\approx\alpha^3.
```

The progression bound therefore contradicts 4-AP-freeness only once `R` is large enough that

```math
(\log|R|)^{-c}
\ll
\alpha^3
```

up to structural constants.

This requirement may be extremely large, but it is a concrete scale condition rather than the false threshold `tau>alpha^2N`.

# Revised structural route

The high-`J` route now reads

```math
\text{large skew-interaction graph}
\Longrightarrow
\text{additive energy in }D_\tau
```

then either

```math
\text{direction expansion}
```

or

```math
\text{small-doubling }R\subseteq D_\tau
\Longrightarrow
\text{GAP container for }R
\Longrightarrow
\frac{\tau}{|A|}\le\rho_4(R)
\Longrightarrow
\text{quantitative obstruction}.
```

## Immediate next task

Quantify the complete chain from a `J`-energy excess to parameters

```math
\tau,
\quad
|\mathcal G_\tau|,
\quad
|R|,
\quad
\text{doubling}(R),
```

and determine whether the resulting lower bound on `|R|` can cross the neighborhood-obstruction scale before the pair-mass budget is exhausted.
