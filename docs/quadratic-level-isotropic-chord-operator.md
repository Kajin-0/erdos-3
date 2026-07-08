# Quadratic-level isotropic chord operator

## Status

Proof-audit formulation.  This note derives the relative analogue of the global start-incidence identity and identifies the natural mixing operator on a high-rank quadratic level set.

The goal is to make the relative pair-fiber route testable as an expansion/mixing problem rather than as a black-box relative `U^3` problem.

## Setup

Let

```math
q(x)=Q(x)+\ell(x)+c
```

be a quadratic polynomial on `F_p^n`, with symmetric bilinear form `B_Q`, and let

```math
V=V_t=\{x:q(x)=t\}.
```

Let

```math
B\subset V,
\qquad |B|/|V|=\beta,
\qquad b=1_B.
```

For an internal 4AP direction `d`, the admissibility conditions are

```math
Q(d)=0,
\qquad
B_Q(x,d)+\ell(d)=0.
```

Equivalently, for `x,y in V` with `y=x+d`, the edge condition is

```math
Q(y-x)=0.
```

Indeed, if `x,y in V`, then

```math
0=q(y)-q(x)=B_Q(x,d)+Q(d)+\ell(d),
```

so imposing `Q(d)=0` is equivalent to the derivative condition.

## The isotropic chord graph

Define the isotropic chord graph on `V` by connecting

```math
x,y\in V
```

when

```math
Q(y-x)=0.
```

Equivalently, for each `x in V`, define its admissible-neighbor set

```math
N(x)=\{y\in V: Q(y-x)=0\}.
```

For high-rank `Q`, one expects this graph to be approximately regular with

```math
|N(x)|\approx p^{n-2}
```

for typical `x`.

This graph is the relative replacement for the complete translation graph in the ambient group.

## Chord averaging operator

Define the normalized chord averaging operator

```math
(MF)(x)=E_{y\in N(x)}F(y),
\qquad x\in V.
```

For `B subset V`, the relative start-incidence identity becomes

```math
E_{y\in N(x)} b(x)b(y)=b(x)(Mb)(x).
```

If the chord graph mixes `B` well, then

```math
(Mb)(x)\approx \beta
```

for most `x in V`, and hence starts of internal pair-fibers concentrate on `B` with density `beta`, exactly as in the global identity

```math
E_d b_d=\alpha 1_A.
```

The relative version is therefore

```math
\text{start mass at }x\approx \beta b(x).
```

## Pair densities by direction

For an isotropic direction `d` with `Q(d)=0`, define

```math
X_d=V\cap\{x:B_Q(x,d)+\ell(d)=0\}.
```

Then `X_d` is the set of starts for full internal lines in direction `d`, and

```math
P_d=\{x\in X_d:x\in B,\ x+d\in B\}.
```

Its relative pair density is

```math
\rho_d=|P_d|/|X_d|.
```

Averaging over directions decomposes the edge density of `B` in the isotropic chord graph:

```math
E_{d:Q(d)=0}\rho_d
\approx \beta^2
```

provided the chord graph is sufficiently regular.

## Variance branch

If

```math
E_d |\rho_d-\beta^2|^2
```

is large, then `B` has uneven distribution over isotropic directions.  This should expose either:

1. a linear/low-rank density increment;
2. a low-rank bias in the quadratic host;
3. or a spectral obstruction detectable before invoking Prendiville.

Thus the hard branch is again the flat case:

```math
\rho_d\approx\beta^2
```

for most isotropic `d`.

## Exact disjointness in the chord graph

If `B` is internally 4AP-free, then for every nonzero isotropic direction `d`,

```math
P_d\cap(P_d-2d)=\emptyset
```

inside `X_d`.

Since `X_d` is a union of full internal lines parallel to `d`, the shift

```math
x\mapsto x+2d
```

preserves `X_d`.

Therefore each direction contributes an exact missing shifted self-overlap:

```math
\sum_{x\in X_d}1_{P_d}(x)1_{P_d}(x+2d)=0.
```

In the flat random model this overlap should be about

```math
\beta^4|X_d|.
```

## Expansion target

The core question becomes:

> Can a high-rank isotropic chord graph support a set `B subset V` of density `beta` such that, for most isotropic directions `d`, the pair-fiber `P_d` has density about `beta^2` in `X_d` but avoids its own `2d`-translate exactly?

If the answer is no above

```math
\beta\gg n^{-1-\epsilon_h},
```

then the high-rank branch gains the exponent needed for dyadic summability.

## Candidate mixing lemma

A possible lemma is:

> Let `V={q=t}` be high-rank and let `B subset V` have no low-rank density increment.  Suppose the isotropic chord operator `M` satisfies strong mixing on `B`, and the direction pair densities satisfy
>
> ```math
> \rho_d=\beta^2+o(\beta^2)
> ```
>
> for most isotropic `d`.  Then the exact disjointness conditions
>
> ```math
> P_d\cap(P_d-2d)=\emptyset
> ```
>
> cannot hold for all those `d` unless
>
> ```math
> \beta\le C_p n^{-1-\epsilon_h}.
> ```

This is a relative-expansion replacement for the too-weak implication

```math
\text{4AP-free}\Rightarrow \|f\|_{U^3,rel}\gtrsim\beta^4.
```

## Relation to high-rank geometry

The operator `M` is defined by the algebraic incidence relation

```math
x,y\in V,
\qquad
Q(y-x)=0.
```

For high-rank `Q`, this relation should behave like a pseudorandom algebraic graph after low-rank obstructions are removed.  Any failure of mixing should itself reveal a low-rank algebraic factor, placing the argument back into the low-rank branch.

## Next research question

Prove a spectral gap or mixing dichotomy for the isotropic chord operator:

```math
M F\approx E_V F
```

for functions `F` on `V` unless `F` has low-rank quadratic/linear structure.  Then combine that with pair-fiber disjointness to rule out the flat high-rank case above density `n^{-1-epsilon}`.
