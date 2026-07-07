# GT31 constant hierarchy bottleneck

## Status

Proof-audit note following the extracted parameter rows.  This records the visible hierarchy among the Green--Tao constants `C2,C3,C5` and what it implies about the final thickness exponent.

## Extracted structural chain

The extracted rows give the following schematic losses:

```math
k \lesssim eta^{-2C2}
```

reachable refinement steps,

```math
d(v) \lesssim eta^{-3C2}
```

frequency/complexity growth,

```math
rho(v) \gtrsim exp(-eta^{-2C5})
```

radius lower bound after all refinements, and

```math
P(r_v=0) \lesssim exp(eta^{-C5^2})/p.
```

## Why the constants separate

A single refinement step has a radius loss of the form

```math
rho(v') >= exp(-eta^{-C5}) rho(v).
```

If there are up to `eta^{-2C2}` steps, naive accumulation gives

```math
rho(v) >= exp(-eta^{-C5} eta^{-2C2})
       = exp(-eta^{-(C5+2C2)}).
```

The published bound records this under the safer umbrella

```math
rho(v) >= exp(-eta^{-2C5}).
```

This requires `C5` to dominate `C2` by a large margin.  Similarly, volume losses accumulate over the refinement path and force the hierarchy among `C2,C3,C5`.

## Consequence for gamma

The final visible zero-step estimate has effective form

```math
P(r=0) << exp(eta^{-gamma})/p
```

with `gamma` at least comparable to `C5^2` in this bookkeeping.

The reciprocal-sum route needs

```math
gamma < 1/4.
```

Thus the Green--Tao bookkeeping is far from the reciprocal-sum threshold unless the entire localization/refinement architecture is changed.  Merely optimizing constants inside the existing hierarchy cannot plausibly turn a quantity comparable to `C5^2` into something below `1/4`, since `C5` is chosen as a large hierarchy constant.

## Updated bottleneck

The obstruction is not primarily the number of Cauchy--Schwarz applications.  The visible bottleneck is:

```math
polynomially many refinement steps
+ exponential radius loss per refinement
+ final Bohr-thickness conversion.
```

To reach the reciprocal-sum threshold inside a Green--Tao-like strategy, one would need a different mechanism that avoids repeated exponential radius shrinkage, or replaces the Bohr/factor localization with a thinner-loss object.

## Next research question

Can the recurrence theorem be proved with a localization object whose zero-step thickness satisfies

```math
P(r=0) << exp(C eta^{-gamma})/p
```

for some `gamma<1/4`, without passing through a hierarchy of large constants `C2,C3,C5`?
