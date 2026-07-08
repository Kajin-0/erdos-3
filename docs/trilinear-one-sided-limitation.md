# Trilinear one-sided limitation

## Status

Proof-audit negative result.  This note checks whether the negative trilinear branch can be strengthened purely from the one-sided indicator bounds on `f=1_A-alpha`.

## Setup

Let

```math
G=F_p^n,
qquad p>4,
```

and let

```math
A subset G,
qquad
alpha=|A|/|G|,
qquad
f=1_A-alpha.
```

Then

```math
E f=0,
qquad
-alpha <= f <= 1-alpha,
```

and exactly

```math
E f^2 = alpha(1-alpha).
```

For small `alpha`, this is scale `alpha`.

## Trilinear Fourier extraction

A trilinear balanced term has the form

```math
T=E_{x,d} f(L_1(x,d))f(L_2(x,d))f(L_3(x,d)),
```

where `L_1,L_2,L_3` are three distinct 4AP forms.

Fourier expansion gives a cubic sum.  After fixing one frequency factor and applying Parseval to the other two, one obtains

```math
|T| <= ||\widehat f||_{infty, nonzero} E f^2.
```

Since `E f^2=alpha(1-alpha)`, this gives

```math
|T| <= alpha ||\widehat f||_{infty, nonzero}
```

up to harmless constants.

Therefore a negative trilinear obstruction

```math
T <= -c alpha^3
```

forces only

```math
||\widehat f||_{infty, nonzero} >= c' alpha^2.
```

This is exactly the borderline logarithmic-barrier increment scale.

## Why one-sidedness alone does not improve the exponent

The one-sided indicator constraint

```math
-alpha <= f <= 1-alpha
```

is already used implicitly in the exact variance identity

```math
E f^2=alpha(1-alpha).
```

There is no additional variance saving available from boundedness alone.  In particular, any argument that only uses:

1. `E f=0`;
2. `-alpha <= f <= 1-alpha`;
3. Fourier expansion of a single trilinear term;
4. Parseval/Cauchy--Schwarz;

cannot improve the extraction beyond

```math
||\widehat f||_{infty} >= c alpha^2.
```

To force a larger increment

```math
||\widehat f||_{infty} >= c alpha^{2-epsilon},
```

one would need a stronger inequality of the schematic form

```math
|T| <= alpha^{1+epsilon} ||\widehat f||_{infty},
```

but this is incompatible with the exact variance scale without using additional structure.

## Consequence

The negative trilinear branch cannot beat the logarithmic barrier by a direct one-term Fourier extraction, even after remembering that `f` is a balanced indicator.

The improvement must use something beyond a single trilinear term, such as:

1. simultaneous signs of multiple trilinear terms;
2. interaction with the pure four-balanced term `Q`;
3. no-4AP constraints beyond the aggregate deficit;
4. hyperplane-flatness plus higher-order structure;
5. a non-iterative recurrence/counting argument.

## Updated branch status

The trilinear branch remains useful but borderline:

```math
T_i <= -c alpha^3
quad => quad
\text{hyperplane increment of size } alpha^2.
```

This matches the `r_4(N) \ll N/\log N` barrier scale, not the dyadically summable target.

## Next research question

Can the simultaneous sign identity

```math
alpha \sum_i T_i + Q <= -c alpha^4
```

be exploited to combine trilinear and four-balanced information into a stronger-than-`alpha^2` increment?
