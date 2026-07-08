# Tensor marginal insufficiency

## Status

Proof-audit barrier.  This note tests whether the two natural marginals of the relative incidence tensor are enough to force a positive shifted self-overlap.  They are not enough in an abstract model.

Therefore the real theorem must use the multiplicative origin

```math
\mathcal P(x,d)=1_B(x)1_B(x+d)1_{Q(d)=0}1_{B_Q(x,d)=0},
```

not merely the fact that `mathcal P` has balanced start and direction marginals.

## Abstract tensor model

Let

```math
\Omega=\{(x,d):x\in X_d\}
```

be the incidence space, and let

```math
S(x,d)=(x+2d,d)
```

be the shear/shift map preserving each direction fiber.

Suppose a tensor

```math
P:\Omega\to\{0,1\}
```

has the expected hard-branch marginals:

```math
E_d P(x,d)\approx \beta 1_B(x),
```

and

```math
E_x P(x,d)\approx \beta^2 1_{Q(d)=0}.
```

Also suppose

```math
P(x,d)P(S(x,d))=0.
```

The question is whether these conditions alone force

```math
\beta\le n^{-1-\epsilon}.
```

## Abstract construction showing marginals are insufficient

For each fixed direction `d`, the map `x -> x+2d` decomposes `X_d` into cycles of length `p`.

Since the target pair-fiber density is

```math
\beta^2\ll 1,
```

one can choose a subset of each direction fiber with density approximately `beta^2` that avoids its own `2d` shift.  For example, select points from each `p`-cycle with no two adjacent under the shift.  This is possible at any density below a fixed positive constant depending only on `p`.

By randomizing these choices across directions and then balancing, one can also make the start marginal close to its expected value, at least in the abstract tensor model where `P` is not required to equal `1_B(x)1_B(x+d)`.

Thus the conditions

```math
\text{direction marginal flatness}
+
\text{start marginal flatness}
+
\text{fiberwise shift-disjointness}
```

are compatible in an abstract tensor model at densities far above the desired bound.

## Where the abstract model cheats

The construction ignores the rank-one/multiplicative constraint

```math
P(x,d)=1_B(x)1_B(x+d)1_{X_d}(x).
```

In a true pair-fiber tensor, choosing `P(x,d)=1` simultaneously asserts membership of two vertices in `B`:

```math
x\in B,
\qquad x+d\in B.
```

These assertions couple different directions.  The same vertex participates in many chords, so choices in one direction constrain choices in many other directions.

This global vertex-consistency is the only remaining source of a possible exponent gain.

## Correct obstruction formulation

The high-rank hard case should therefore be stated as:

```math
P(x,d)=b(x)b(x+d)1_{Q(d)=0}1_{B_Q(x,d)=0},
```

with

```math
E_d P(x,d)\approx \beta b(x),
\qquad
E_x P(x,d)\approx \beta^2 1_{Q(d)=0},
```

and

```math
P(x,d)P(x+2d,d)=0.
```

The first two lines alone are not enough.  The proof must use that `P` factors through one common vertex function `b`.

## Candidate vertex-consistency lemma

A plausible theorem is:

> Let `V_t` be a high-rank quadratic level set and `B subset V_t` have relative density `beta`.  Suppose the chord graph and direction densities are flat at the expected scales, and suppose
>
> ```math
> b(x)b(x+d)b(x+2d)b(x+3d)=0
> ```
>
> for every internal line.  Then either `B` has a low-rank/quadratic density increment or
>
> ```math
> \beta\le C_p n^{-1-\epsilon_h}.
> ```

The key feature is that the hypothesis is written directly in terms of `b`, not an arbitrary tensor `P`.

## Consequence for proof search

Cauchy--Schwarz or entropy arguments that only see the two marginals of `P` will fail.  They can at best reproduce the abstract tensor model.

A successful argument must introduce at least one additional compatibility condition, such as:

1. common vertex consistency across many directions;
2. triple-overlap constraints like

```math
E_x b(x)b(x+d)b(x+e);
```

3. algebraic expansion of the chord graph acting on vertex neighborhoods;
4. a sifting mechanism that upgrades many weak pair-fiber obstructions into vertex concentration.

## Next research question

Can one prove that any abstract tensor satisfying the marginal and disjointness conditions but not coming from a common vertex function is far from rank-one in a measurable way, and that this rank-one defect forces a density increment or quadratic structure when `P=b(x)b(x+d)`?
