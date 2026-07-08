# Fourier formulation of the two-shadow obstruction

## Status

Proof-audit reformulation.  This note expresses the endpoint shadow `E`, the skew shadow `I`, and the 4AP-free condition as Fourier identities over `F_p`.

## Fourier convention

For `g:F_p -> C`, write

```math
\widehat g(r)=E_{x in F_p} g(x)e(-rx/p).
```

Then

```math
g(x)=sum_{r in F_p} \widehat g(r)e(rx/p).
```

Let

```math
h=1_A,
qquad
alpha=E h=m/p.
```

## Endpoint shadow

The normalized endpoint shadow count is the ordinary 3AP average:

```math
E/p^2 = E_{x,d} h(x)h(x+d)h(x+2d).
```

Fourier expansion gives

```math
E/p^2 = sum_{r in F_p} \widehat h(r)^2 \widehat h(-2r).
```

The zero-frequency term is `alpha^3`, hence

```math
E - m^3/p
= p^2 sum_{r != 0} \widehat h(r)^2 \widehat h(-2r).
```

## Skew shadow

Take the skew interior pattern in the form

```math
I/p^2 = E_{x,d} h(x)h(x+d)h(x+3d).
```

Fourier expansion gives

```math
I/p^2
= sum_{r in F_p} \widehat h(2r)\widehat h(-3r)\widehat h(r).
```

Again the zero-frequency term is `alpha^3`, so

```math
I - m^3/p
= p^2 sum_{r != 0} \widehat h(2r)\widehat h(-3r)\widehat h(r).
```

Thus the two lower bounds

```math
E >= m^3/p,
qquad
I >= m^3/p
```

are equivalent to nonnegativity of two different cubic Fourier sums.

## Full 4AP-free condition

The normalized 4AP count is

```math
Lambda_4(h)=E_{x,d}h(x)h(x+d)h(x+2d)h(x+3d).
```

Fourier expansion gives

```math
Lambda_4(h)
= sum_{r,s in F_p}
  \widehat h(r+2s)\widehat h(-2r-3s)\widehat h(r)\widehat h(s).
```

If `A` is 4AP-free, then only `d=0` contributes, so

```math
Lambda_4(h)=m/p^2=alpha/p.
```

The zero-frequency term is `alpha^4`, hence

```math
sum_{(r,s) != (0,0)}
  \widehat h(r+2s)\widehat h(-2r-3s)\widehat h(r)\widehat h(s)
= alpha/p-alpha^4.
```

When `p` is large compared with `alpha^{-3}`, the right side is approximately `-alpha^4`.

## Product enemy in Fourier form

The pure tensor enemy criterion requires

```math
E >= m^3/p,
qquad
I >= m^3/p,
```

and

```math
max(E,I)>max(p,m^3/p).
```

In Fourier language, it asks for two nonnegative cubic biases, with at least one large enough to dominate the tensor sign, while the quartic 4AP expression has a forced negative deficit.

## Interpretation

The two-shadow obstruction is not only a run-count problem.  It is also a compatibility problem between:

1. the endpoint cubic Fourier sum;
2. the skew cubic Fourier sum;
3. the negative quartic Fourier identity forced by 4AP-freeness.

A proof of the two-shadow domination conjecture may need to show that the two cubic sums cannot both be nonnegative and large while the quartic 4AP sum is as negative as required by 4AP-freeness.

## Next research question

Can the negative quartic identity

```math
Lambda_4(h)-alpha^4 = alpha/p-alpha^4
```

be combined with nonnegative endpoint and skew cubic biases to force

```math
E <= p
```

and

```math
I <= p?
```
