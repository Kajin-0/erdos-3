# U3 obstruction is forced by 4AP deficiency

## Status

Proof-audit reduction.  This note shows that a direct 4AP-counting route cannot simply ignore the `U^3` obstruction.  It may avoid the full inverse theorem, but it still has to confront large `U^3` structure.

## Setup

Let `G=F_p^n` with `p>4`.  For functions on `G`, write

```math
Lambda_4(f_0,f_1,f_2,f_3)
  = E_{x,d in G} f_0(x)f_1(x+d)f_2(x+2d)f_3(x+3d).
```

Let `A subset G` have density `alpha`, and define the balanced function

```math
f = 1_A - alpha.
```

Then

```math
1_A = alpha + f,
qquad E f = 0.
```

## Expansion

Expanding `Lambda_4(1_A,1_A,1_A,1_A)` gives

```math
alpha^4
```

plus multilinear terms involving `f`.

Terms with one `f` vanish because `E f=0`.  Terms with exactly two `f` also vanish because any two distinct forms among

```math
x, x+d, x+2d, x+3d
```

are jointly uniform on `G^2` when `p>4`.

Thus the discrepancy from random count is controlled by the terms with at least three copies of `f`.

By the generalized von Neumann inequality, each such term is bounded by a constant multiple of

```math
||f||_{U^3}.
```

Therefore

```math
| Lambda_4(1_A) - alpha^4 | <= C ||1_A-alpha||_{U^3}
```

for an absolute constant `C`.

## Consequence for 4AP-free sets

If `A` contains no nontrivial 4AP, then only `d=0` contributes.  Hence

```math
Lambda_4(1_A) <= alpha/|G|.
```

If

```math
|G| >= 2 alpha^{-3},
```

then

```math
Lambda_4(1_A) <= alpha^4/2.
```

Consequently

```math
||1_A-alpha||_{U^3} >= c alpha^4
```

for some absolute `c>0`.

## Interpretation

Any proof that a dense set with no 4AP cannot exist at a given scale must explain why a balanced indicator with

```math
||1_A-alpha||_{U^3} >= c alpha^4
```

forces enough structure to get a contradiction.

Thus one cannot avoid the `U^3` obstruction entirely.

The possible improvement is narrower:

```math
avoid the full quantitative U^3 inverse theorem,
```

not

```math
avoid U^3 structure altogether.
```

## Updated target

A 4AP-specific proof should exploit the special form `f=1_A-alpha` and the no-4AP hypothesis to turn large `U^3` norm into a contradiction with better cost than the full inverse theorem gives.

The desired finite-field target remains:

```math
codim <= C alpha^{-1+delta}
```

or equivalently, in epsilon language,

```math
codim <= C epsilon^{-theta},  theta < 1/4.
```

## Next research question

Can the special hypotheses

1. `f=1_A-alpha` is a balanced indicator;
2. `A` has no nontrivial 4AP;
3. `||f||_{U^3} >= c alpha^4`;

be used to obtain a density increment or contradiction with total codimension below `alpha^{-1}`?
