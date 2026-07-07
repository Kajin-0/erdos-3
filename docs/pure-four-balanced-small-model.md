# Pure four-balanced small model

## Status

Finite-field computational sanity check.  This note records that a small 4AP-free set can have a negative four-balanced term while all four trilinear terms are nonnegative.  This is not an asymptotic obstruction.

## Exhaustive small-prime search

A brute-force enumeration of all subsets of `F_p` for `p <= 19` found:

| `p` | 4AP-free subsets checked | subsets with `Q<0` | subsets with `Q<0` and all `T_i>=0` |
|---:|---:|---:|---:|
| 5  | 25    | 0    | 0 |
| 7  | 77    | 0    | 0 |
| 11 | 660   | 44   | 0 |
| 13 | 1885  | 247  | 0 |
| 17 | 13923 | 2210 | 1360 |
| 19 | 36100 | 4047 | 1482 |

Thus the pure four-balanced case first appears in this search at `p=17`.

## Example in F_17

Let

```math
A = {0,1,2,4,7} subset F_{17}.
```

Then `A` is 4AP-free in `F_17`, and

```math
alpha = 5/17.
```

For

```math
f = 1_A - alpha,
```

write

```math
Q = Lambda_4(f,f,f,f),
```

and let `T_i` be the trilinear term with `f` in all positions except position `i`.

Direct exact computation gives

```math
Q = -80/83521 < 0,
```

while

```math
T_0 = 62/4913,
T_1 = 28/4913,
T_2 = 28/4913,
T_3 = 62/4913.
```

Thus

```math
Q < 0,
qquad
T_i > 0 \quad\text{for all }i.
```

This is a genuine pure four-balanced small model.

## Tensor-power test

Let `B_n=A^n subset F_17^n` and

```math
F_n = 1_{B_n} - alpha^n.
```

For the base example,

```math
Lambda_4(1_A)=5/289,
```

and the three-point averages are

```math
lambda_{123}=lambda_{012}=11/289,
qquad
lambda_{023}=lambda_{013}=9/289.
```

The tensor-powered four-balanced term is

```math
Q_n
= (5/289)^n
  - (5/17)^n 2((11/289)^n+(9/289)^n)
  + 3(5/17)^{4n}.
```

Equivalently,

```math
Q_n / alpha^{4n}
= 3 + (289/125)^n
    - 2(187/125)^n
    - 2(153/125)^n.
```

For `n=1`, this is negative.  But for every `n>=2`, it is positive because the positive term `(289/125)^n` dominates.

So this pure four-balanced example does not tensor into an asymptotic pure four-balanced obstruction.

## Interpretation

The example shows that a negative four-balanced obstruction without a trilinear obstruction is formally possible in small dimension.

However, its tensor powers do not preserve the negative four-balanced sign.  Therefore it does not provide an asymptotic enemy case.

## Updated obstruction search

The remaining obstruction question is narrower:

Can one construct a high-dimensional 4AP-free family with density `alpha` and dimension near

```math
n <= alpha^{-1+delta}
```

such that

```math
Lambda_4(F,F,F,F) <= -c alpha^4
```

while all trilinear alternatives are nonnegative or too small on every subspace of codimension `< alpha^{-1+delta}`?
