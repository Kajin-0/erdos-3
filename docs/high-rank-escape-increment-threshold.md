# High-rank escape increment threshold

## Status

Proof-audit scale lemma.  This note calibrates the increment size required from the structured escape branch of the high-rank quadratic-level dichotomy.

## Setup

Work in the finite-field model with a minimal critical counterexample

```math
A subset F_p^n,
qquad
alpha=|A|/p^n,
```

near the target scale

```math
n \sim C alpha^{-theta},
qquad theta=1-delta<1.
```

The high-rank quadratic-level dichotomy is expected to produce either:

1. recurrence inside the high-rank quadratic level; or
2. a structured density increment on a linear/low-rank factor of codimension

```math
s=O_p(log(1/beta)),
```

where `beta` is the relative density on the quadratic level.

In the relevant small-increment regime,

```math
beta \sim alpha.
```

Thus

```math
s=O_p(log(1/alpha)).
```

## Minimality allowance at codimension s

Minimality at codimension `s` allows affine-section density up to

```math
alpha (n/(n-s))^{1/theta}.
```

For `s << n`, this is

```math
alpha\left(1+s/(theta n)+O(s^2/n^2)\right).
```

Therefore the absolute density increment compatible with minimality is roughly

```math
alpha s/n.
```

At the critical scale `n ~ alpha^{-theta}` and `s=O(log(1/alpha))`, this becomes

```math
alpha^{1+theta} log(1/alpha)
= alpha^{2-delta} log(1/alpha).
```

## Required escape increment size

Let the structured branch produce an absolute density increment

```math
F(beta).
```

With `beta ~ alpha`, this contradicts minimality only if

```math
F(alpha) >> alpha^{2-delta} log(1/alpha).
```

This is the exact threshold for the high-rank escape branch.

## Consequences for candidate F(beta)

### Constant-factor increment

If

```math
F(beta) >= c beta,
```

then at `beta~alpha` the increment is `~alpha`, far larger than

```math
alpha^{2-delta} log(1/alpha).
```

Such an escape branch would be easily strong enough.

### Quadratic increment

If

```math
F(beta) ~ beta^2,
```

then at `beta~alpha`,

```math
F(alpha) ~ alpha^2.
```

But for `delta>0`,

```math
alpha^2 << alpha^{2-delta} log(1/alpha)
```

as `alpha -> 0`.

Thus a merely quadratic increment is not enough to break minimality at target exponent `theta=1-delta`.

### Power-saving increment

If

```math
F(beta) >= c beta^{2-epsilon_F},
```

then the escape branch beats minimality provided

```math
alpha^{2-epsilon_F} >> alpha^{2-delta} log(1/alpha),
```

which holds when

```math
epsilon_F > delta.
```

The logarithm is harmless compared with any fixed positive exponent gap.

## Resulting parameter target

For a target exponent

```math
theta=1-delta,
```

the structured escape branch is useful if it returns either:

1. a constant-factor density increment;
2. or an increment of size

```math
F(beta) >= c beta^{2-epsilon_F}
```

with

```math
epsilon_F>delta.
```

If the best available increment is only `F(beta) ~ beta^2`, the escape branch remains logarithmic-barrier limited.

## Interaction with high-rank recurrence gain

The recurrence side with independence gain `epsilon_h` supports targets

```math
delta < epsilon_h/(1+epsilon_h).
```

The escape side with increment gain `epsilon_F` supports targets

```math
delta < epsilon_F.
```

Therefore the high-rank dichotomy would support any

```math
delta < min(epsilon_F, epsilon_h/(1+epsilon_h))
```

provided the medium-rank and trilinear branches are also controlled.

## Updated theorem target

A high-rank theorem strong enough for the main proof program should aim for:

> If `B subset {q=t}` is internally 4AP-free with relative density `beta`, then either
>
> ```math
> beta <= C_p n^{-1-epsilon_h},
> ```
>
> or `B` has a linear/low-rank density increment of absolute size at least
>
> ```math
> c_p beta^{2-epsilon_F}
> ```
>
> on a factor of codimension `O_p(log(1/beta))`.

Any positive `epsilon_h` and `epsilon_F`, after taking `delta` smaller, would make this branch quantitatively useful.

## Next research question

Can the checkpoint theorem with `epsilon_h=0` produce more than a quadratic escape increment, i.e. can it give

```math
F(beta) >= c beta^{2-epsilon_F}
```

for some `epsilon_F>0`?
