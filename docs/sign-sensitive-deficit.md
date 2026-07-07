# Sign-sensitive 4AP deficit alternatives

## Status

Proof-audit refinement.  This note records that a 4AP-free set produces a negative deficit from the random 4AP count, not merely a large absolute discrepancy.

## Setup

Let `G=F_p^n` with `p>4`, let `A subset G` have density `alpha`, and write

```math
f = 1_A - alpha.
```

Use

```math
Lambda_4(g_0,g_1,g_2,g_3)
  = E_{x,d} g_0(x)g_1(x+d)g_2(x+2d)g_3(x+3d).
```

The balanced expansion is

```math
Lambda_4(1_A)=alpha^4 + alpha sum_i T_i + Q,
```

where `T_i` is the trilinear term with `f` in every position except `i`, and

```math
Q = Lambda_4(f,f,f,f).
```

## Negative deficit

If `A` has no nontrivial 4AP, then only `d=0` contributes, so

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

Therefore

```math
alpha sum_i T_i + Q <= -alpha^4/2.
```

This is stronger than an absolute-discrepancy statement: the obstruction has negative sign.

## Sign-sensitive alternative

From the preceding inequality, either

```math
Q <= -c alpha^4
```

or for some `i`,

```math
T_i <= -c alpha^3.
```

Thus the forced alternatives are not just

```math
|Q| >= c alpha^4
```

or

```math
|T_i| >= c alpha^3.
```

They are negative alternatives.

## Why the sign matters

A negative trilinear term says that `A` is anti-correlated with a three-point pattern in a specific slot.  A negative four-balanced term says that the balanced indicator is producing fewer 4APs than random at the fully balanced level.

Generic `U^3` inverse theorems discard this sign.  They detect large structure but do not by themselves exploit that the structure is specifically responsible for a negative 4AP-count deficit.

## Updated possible leverage point

A 4AP-specific proof may need to exploit the sign of the deficit, not merely its magnitude.  The desired improvement would be a theorem of the following flavor:

```math
negative multilinear 4AP deficit
+ f=1_A-alpha
+ 0 <= 1_A <= 1
=> large density increment or direct contradiction
```

with total codimension below `alpha^{-1}`.

## Next research question

Can a negative four-balanced obstruction

```math
Lambda_4(f,f,f,f) <= -c alpha^4
```

occur for a balanced indicator of a 4AP-free set without also forcing a larger negative trilinear obstruction on a structured subspace?
