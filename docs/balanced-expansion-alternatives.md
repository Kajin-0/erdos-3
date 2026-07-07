# Balanced 4AP expansion alternatives

## Status

Proof-audit refinement.  This note expands the 4AP count more precisely than the crude generalized-von-Neumann bound.  It identifies the exact multilinear alternatives forced by 4AP-freeness.

## Setup

Let `G=F_p^n` with `p>4`, let `A subset G` have density `alpha`, and write

```math
f = 1_A - alpha.
```

Then

```math
1_A = alpha + f,
qquad E f = 0.
```

Let

```math
Lambda_4(g_0,g_1,g_2,g_3)
  = E_{x,d} g_0(x)g_1(x+d)g_2(x+2d)g_3(x+3d).
```

## Expansion

Expanding `Lambda_4(1_A,1_A,1_A,1_A)` gives

```math
Lambda_4(1_A)=alpha^4
  + alpha \sum_{i=0}^3 T_i
  + Q,
```

where `T_i` is the trilinear term with `f` in all positions except position `i`, and

```math
Q = Lambda_4(f,f,f,f).
```

The terms with exactly one `f` vanish because `E f=0`.

The terms with exactly two `f` vanish because any two distinct forms among

```math
x, x+d, x+2d, x+3d
```

are jointly uniform on `G^2` when `p>4`.

## Consequence of 4AP-freeness

If `A` has no nontrivial 4AP, then only `d=0` contributes, so

```math
Lambda_4(1_A) <= alpha/|G|.
```

If `|G| >= 2 alpha^{-3}`, then

```math
Lambda_4(1_A) <= alpha^4/2.
```

Therefore

```math
| alpha \sum_i T_i + Q | >= alpha^4/2.
```

This yields the alternative:

```math
|Q| >= c alpha^4
```

or, for some `i`,

```math
|T_i| >= c alpha^3.
```

## Relation to U3

Both alternatives are controlled by `U^3`-type norms through generalized von Neumann inequalities.  The four-linear alternative only forces

```math
||f||_{U^3} >= c alpha^4,
```

while a trilinear alternative can force the stronger scale

```math
||f||_{U^3} >= c alpha^3.
```

However, 4AP-freeness alone does not guarantee that the trilinear alternative occurs.  The obstruction may sit in the four-balanced term `Q`.

## Consequence for proof strategy

A proof route that can exploit the trilinear alternative may gain one power of `alpha` in the obstruction scale.  But even an `alpha^3` obstruction is not enough for a naive black-box inverse-theorem iteration if the correlation/increment scale is only comparable to the obstruction.

The real target is stronger:

```math
convert the special multilinear deficiency into an increment near alpha^{1+epsilon},
```

or avoid ordinary density-increment iteration altogether.

## Next research question

Can the four-balanced obstruction

```math
|Lambda_4(f,f,f,f)| >= c alpha^4
```

be ruled out, amplified, or converted into a larger trilinear-type obstruction using only that `f=1_A-alpha` is a balanced indicator and `A` is 4AP-free?
