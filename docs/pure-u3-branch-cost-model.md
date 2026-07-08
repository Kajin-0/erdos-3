# Pure U3 branch cost model

## Status

Proof-audit bottleneck note.  This note quantifies what the pure four-balanced branch can buy through a generic quadratic inverse/density-increment mechanism.

## Starting point

After passing to a minimal critical counterexample, the sign-sensitive deficit leaves the pure branch

```math
Q=Lambda_4(f,f,f,f) <= -c alpha^4,
```

where

```math
f=1_A-alpha.
```

By generalized von Neumann,

```math
|Q| <= ||f||_{U^3},
```

so

```math
||f||_{U^3} >= c alpha^4.
```

Let

```math
delta_U := ||f||_{U^3}.
```

The available lower bound is

```math
delta_U >= c alpha^4.
```

## Generic quadratic inverse input

Suppose a quadratic inverse/density-increment mechanism has the schematic form

```math
||f||_{U^3} >= delta_U
quad => quad
\text{structured correlation or density increment } >= c delta_U^M,
```

possibly after passing to a structured object of codimension cost

```math
O(delta_U^{-S}).
```

Then in the pure branch this gives increment scale at best

```math
Delta alpha ~ alpha^{4M},
```

and codimension scale at best

```math
alpha^{-4S}.
```

## Iterative density-increment cost

If each step gives an increment

```math
Delta alpha >= c alpha^t,
```

with codimension cost

```math
alpha^{-s},
```

then the earlier density-increment cost model gives total dimension cost roughly

```math
alpha^{-(s+t-1)}.
```

For the quadratic inverse route,

```math
t=4M,
qquad
s=4S.
```

Therefore the total exponent is approximately

```math
4S+4M-1.
```

To beat the reciprocal-sum finite-field target, one needs total exponent below `1`, i.e.

```math
4S+4M-1 < 1.
```

Equivalently,

```math
S+M < 1/2.
```

In particular, even with no codimension cost (`S=0`), one needs

```math
M<1/2.
```

## Consequence

Any standard inverse theorem with linear-or-worse power loss

```math
M >= 1
```

is quantitatively too weak for this route.

The pure U3 branch cannot be solved by merely invoking a black-box quadratic inverse theorem unless that theorem gives an unusually strong density increment, better than square-root in the U3 obstruction size.

## Relation to the trilinear branch

The trilinear branch gives an increment of size about

```math
alpha^2.
```

This corresponds to the borderline exponent

```math
t=2.
```

With zero codimension cost per increment, this already gives total scale

```math
alpha^{-1},
```

which is exactly the logarithmic barrier and not enough for summability.

The pure U3 branch, starting only from

```math
||f||_{U^3} >= c alpha^4,
```

is no better under generic inverse machinery; it is usually worse.

## What would be needed

A successful pure-U3 mechanism must exploit special information beyond the scalar lower bound `||f||_{U^3} >= c alpha^4`, such as:

1. the sign `Q<0`, not merely `|Q|` large;
2. the bounded-indicator form `f=1_A-alpha`;
3. 4AP-freeness, not merely large U3 norm;
4. hyperplane flatness/minimality;
5. a non-iterative contradiction rather than repeated small increments;
6. a density increment whose exponent is effectively below `alpha^2` barrier.

## Updated bottleneck

The pure branch target is therefore not simply:

```math
large U3 => quadratic correlation.
```

The target must be closer to:

```math
Q <= -c alpha^4
+ 4AP-free
+ hyperplane-flat
+ indicator bounds
=>
\text{density increment stronger than } alpha^2
```

or a direct contradiction.

## Next research question

Can the sign of the four-balanced term `Q<0` force a one-sided quadratic structure that yields a larger density increment than a generic U3 inverse theorem would provide?
