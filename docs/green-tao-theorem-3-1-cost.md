# Cost extraction from Green--Tao Theorem 3.1

## Status

Working proof-audit note.  This extracts the cost bottleneck from the high-level recurrence theorem in Green--Tao Part III.

## Correction: thickness sign

The useful thickness bound has an exponential-over-`p` form

```math
P(r=0) << exp(eta^{-O(1)})/p,
```

not a negative exponential.  This agrees with the later extracted row

```math
P(r_v=0) << exp(eta^{-C5^2})/p.
```

The quantitative diagnostic below is unchanged after this sign correction.

## Source theorem shape

Green--Tao Part III proves a recurrence theorem with parameter `eta`.  In simplified terms, for a function `f: Z/pZ -> [-1,1]`, there are random variables `a,r` such that

```math
E f(a) = E_x f(x) + O(eta),
```

```math
Lambda_{a,r}(f) >= (E f(a))^4 - O(eta),
```

and

```math
P(r=0) << exp(eta^{-O(1)})/p.
```

The paper then applies this to `f=1_A` when `A subset [N]` has no nontrivial 4AP.

## How the polylog bound emerges

Let `alpha = |A|/p`.  Since `A` has no nontrivial 4AP, the weighted 4AP count can only come from the `r=0` contribution.  Thus the recurrence lower bound forces roughly

```math
alpha^4 <= O(eta) + P(r=0).
```

Choosing

```math
eta ~ alpha^4
```

leaves the condition

```math
P(r=0) << exp(eta^{-O(1)})/p
```

as the main cost.  To make the zero-step contribution negligible, one needs approximately

```math
p >> exp(eta^{-O(1)}) = exp(alpha^{-O(1)}).
```

This yields a bound of the form

```math
r_4(N) << N(log N)^{-c}
```

for some `c>0`.

## Quantitative bottleneck

Suppose the thickness estimate had the more explicit form

```math
P(r=0) << exp(C eta^{-gamma})/p.
```

Then the above argument would give the cost

```math
p >> exp(C alpha^{-4 gamma}),
```

and hence

```math
r_4(N) << N(log N)^{-1/(4 gamma)}.
```

The reciprocal-sum target requires a logarithmic exponent strictly larger than `1`, so this route would need

```math
1/(4 gamma) > 1,
```

that is

```math
gamma < 1/4.
```

## Consequence

In the Green--Tao Theorem 3.1 framework, the obstacle is not merely obtaining any polynomial dependence in `eta`.  To reach the reciprocal-sum threshold by this framework, the effective thickness cost would have to improve to better than

```math
exp(C eta^{-1/4})/p
```

up to secondary losses.

This is a sharp diagnostic for the proof audit: locate the source of the hidden `eta^{-O(1)}` in the thickness bound and determine whether its exponent could plausibly be pushed below `1/4`.

## Caveat

This note analyzes the high-level Theorem 3.1 route as stated.  A different proof architecture could bypass this exact `eta`-thickness bottleneck.
