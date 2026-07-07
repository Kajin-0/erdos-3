# Finite-vector-space sandbox for the k=4 problem

## Status

Open research sandbox.  This note isolates the 4AP quantitative problem in `F_p^n`, where localization losses can be tracked through codimension rather than Bohr radius.

## Model

Fix a prime `p>4` and let

```math
G = F_p^n,
qquad N=|G|=p^n.
```

Let `r_4(G)` denote the largest size of a subset of `G` containing no nontrivial 4-term arithmetic progression.

The known finite-field analogue has the same broad shape as the integer `r_4(N)` bound:

```math
r_4(G) << N (log N)^{-c}
```

for some positive constant `c`.

## Why this sandbox is useful

In `Z/NZ`, Green--Tao localization pays Bohr-set radius losses.  In `F_p^n`, one can attempt to localize on subspaces or affine subspaces, where the loss is codimension.

A codimension bound

```math
codim(V) << alpha^{-theta}
```

corresponds to a scale/support loss roughly

```math
|V|/|G| = p^{-O(alpha^{-theta})}
        = exp(-O(alpha^{-theta})).
```

Thus the reciprocal-sum-relevant target is still the same exponent threshold:

```math
theta < 1.
```

For recurrence-theorem language with `eta ~ alpha^4`, this is equivalent to a zero-step cost exponent

```math
gamma < 1/4.
```

## Toy theorem target

A finite-vector-space replacement theorem strong enough to model the integer goal would be:

For every density `alpha`, every `A subset F_p^n` with `|A| >= alpha |G|` contains a nontrivial 4AP provided

```math
n >= C alpha^{-1+delta}
```

for some constants `C,delta>0` depending at most on `p`.

Equivalently,

```math
|G| >= exp(C_p alpha^{-1+delta}).
```

This would imply

```math
r_4(F_p^n) << |G| (log |G|)^(-1/(1-delta)).
```

The exponent is strictly larger than `1`, hence dyadically summable in the corresponding finite-size parameter.

## What to test

The finite-vector-space sandbox asks whether the obstruction is:

1. mainly arithmetic/Bohr-localization loss in cyclic groups; or
2. already intrinsic to 4AP structure even when localization is by subspace codimension.

If the best available finite-vector-space proof still gives only

```math
codim << alpha^{-C}
```

for a large `C`, then the barrier is not merely Bohr radius.

If one can improve the finite-vector-space model to

```math
codim << alpha^{-1+delta},
```

then it becomes a serious candidate architecture to port back to cyclic groups.

## Parameter ledger for finite-vector-space attempt

| Stage | Desired bound | Failure mode |
|---|---|---|
| Counting to U3 obstruction | polynomial in alpha | exponent too large before inverse theorem |
| U3 inverse theorem | codimension/correlation with small exponent | inverse theorem loses alpha^{-C} |
| Density increment | alpha -> alpha + Delta(alpha) | too many iterations |
| Subspace localization | codim increment per step | total codimension exceeds alpha^{-1} |
| Iteration accounting | total codim << alpha^{-1+delta} | only recovers log^{-c} with c<=1 |

## Immediate next question

Can the known finite-field 4AP argument be expressed with total codimension cost below

```math
alpha^{-1}
```

or is the published finite-field exponent already structurally far above that threshold?
