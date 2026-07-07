# Small model: negative four-balanced obstruction occurs

## Status

Finite-field sanity check.  This is not an asymptotic construction and not a lower bound for the main problem.  It shows only that a negative four-balanced obstruction is formally possible for a balanced indicator of a 4AP-free set.

## Ambient group

Work in

```math
G = F_{11}.
```

Let

```math
A = {0,1,2,4,5,7} subset F_{11}.
```

Then

```math
alpha = |A|/|G| = 6/11.
```

A direct check over all pairs `(x,d) in F_11^2` shows that the only 4-term arithmetic progressions in `A` are the trivial ones with `d=0`.  Hence `A` is 4AP-free in `F_11`.

Equivalently,

```math
Lambda_4(1_A) = alpha/11 = 6/121.
```

## Balanced function

Set

```math
f = 1_A - alpha.
```

The balanced expansion has the form

```math
Lambda_4(1_A)=alpha^4 + alpha sum_i T_i + Q,
```

where

```math
Q = Lambda_4(f,f,f,f).
```

For this example, direct computation gives

```math
Q = -270/14641.
```

The trilinear terms are

```math
T_0 = -40/1331,
T_1 =  15/1331,
T_2 =  15/1331,
T_3 = -40/1331.
```

Thus the four-balanced term is genuinely negative, and two trilinear terms are also negative.

## What this example proves

This example proves only the following limited point:

```math
negative Lambda_4(f,f,f,f)
```

is not ruled out by the facts that

```math
f = 1_A-alpha
```

and `A` is 4AP-free.

So the four-balanced obstruction cannot be dismissed by a general positivity principle.

## What this example does not prove

It does not show that a negative four-balanced obstruction can persist asymptotically without useful trilinear structure.

In fact, in this small model the negative four-balanced obstruction coexists with negative trilinear terms:

```math
T_0,T_3 < 0.
```

Therefore the live question remains whether, at large dimension and small density, a negative four-balanced obstruction can be converted into a stronger trilinear obstruction on a subspace.

## Next research question

Search for or rule out asymptotic examples where

```math
Lambda_4(f,f,f,f) <= -c alpha^4
```

but every trilinear obstruction remains below the useful threshold on all subspaces of codimension `< alpha^{-1+delta}`.
