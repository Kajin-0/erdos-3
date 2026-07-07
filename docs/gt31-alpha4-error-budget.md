# GT31 alpha^4 error budget

## Status

Rigorous optimization note inside the Green--Tao Theorem 3.1 framework.

## Setup

The recurrence theorem gives an absolute-error lower bound of schematic form

```math
Lambda_{a,r}(1_A) >= alpha^4 - O(eta),
```

where `alpha=|A|/p`.

If `A` has no nontrivial 4AP, the only contribution comes from the zero-step event, so the argument gives

```math
alpha^4 <= O(eta) + P(r=0).
```

## Consequence

To force a contradiction, the absolute error term must satisfy

```math
eta <= c alpha^4
```

for a sufficiently small constant `c>0`.

Thus the choice

```math
eta ~ alpha^4
```

is not arbitrary.  It is the largest admissible eta in this absolute-error recurrence framework.

## Optimization

Assume the thickness estimate has explicit form

```math
P(r=0) << exp(C eta^{-gamma})/p.
```

The cost is minimized by taking eta as large as the recurrence error allows, namely `eta ~ alpha^4`.  This gives

```math
p >> exp(C alpha^{-4 gamma})
```

and hence

```math
r_4(N) << N(log N)^(-1/(4 gamma)).
```

Therefore the reciprocal-sum target requires

```math
gamma < 1/4.
```

## Implication

There is no extra leverage from choosing eta differently inside this framework.  Any improvement must come from one of the following:

1. reduce the effective zero-step thickness exponent gamma;
2. replace the absolute-error recurrence with a fundamentally sharper recurrence statement;
3. use a different proof architecture that does not pass through the same eta-thickness bottleneck.

## Caution on relative-error dreams

A recurrence theorem with relative error instead of absolute error would be a different theorem, not a bookkeeping optimization of GT31.  Such a theorem would have to be checked against known dense AP-free constructions; it cannot simply be assumed as a local improvement.
