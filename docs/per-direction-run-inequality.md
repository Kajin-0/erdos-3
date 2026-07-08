# Per-direction run inequality

## Status

Proof-audit inequality.  This improves the crude pointwise disjointness bound by using the cyclic run decomposition for each nonzero common difference.

## Setup

Let `A subset F_p` be 4AP-free, with

```math
m=|A|.
```

Fix `d != 0` and view `A` along the direction `d` as a cyclic binary string

```math
b_t = 1_A(td),
qquad t in F_p.
```

The string has no four consecutive ones.  Decompose it into cyclic one-runs of lengths

```math
ell_s in {1,2,3}
```

separated by zero gaps

```math
g_s >= 1.
```

Let

```math
n_j = # { s : ell_s=j },\qquad j=1,2,3.
```

Then

```math
m = n_1+2n_2+3n_3.
```

## Fixed-direction shadow contribution

For this direction, the endpoint shadow contribution is

```math
E_d=n_3.
```

The two interior contributions satisfy

```math
J_{1,d}+J_{2,d}
<= 2(n_2+n_3),
```

because each run of length at least two can contribute to at most one right-adjacent single-zero gap and at most one left-adjacent single-zero gap.

Therefore the full missing-slot shadow contribution for this direction obeys

```math
2E_d+J_{1,d}+J_{2,d}
<= 2n_3+2(n_2+n_3)
= 2n_2+4n_3.
```

Using

```math
m=n_1+2n_2+3n_3,
```

we get

```math
2n_2+4n_3 = m-n_1+n_3 <= m+n_3 <= 4m/3.
```

Thus, for every nonzero direction,

```math
2E_d+J_{1,d}+J_{2,d} <= 4m/3.
```

This bound is sharp for the cyclic pattern `1110 1110 ...`, where `m=3p/4` and the left side equals `p=4m/3`.

## Global inequality

Summing over all nonzero directions and adding the `d=0` contribution `4m` gives

```math
2E+2I
<= 4m + (p-1)(4m/3).
```

Equivalently,

```math
2E+2I <= (4m/3)(p+2).
```

This improves the previous universal disjointness bound

```math
2E+2I <= p(p-1)+4m
```

whenever `m < 3p/4`.

## Consequence under random-scale lower bounds

The pure tensor enemy criterion requires

```math
E >= m^3/p,
qquad
I >= m^3/p.
```

Substituting into the improved inequality gives

```math
4m^3/p <= (4m/3)(p+2).
```

After cancellation,

```math
m^2 <= p(p+2)/3.
```

In density form,

```math
alpha^2 <= (1+2/p)/3.
```

Thus a pure tensor enemy must have density at most approximately

```math
1/sqrt(3) = 0.577350...
```

This is sharper than the earlier `4^{-1/3}=0.629960...` cutoff, but it is still only a high-density obstruction.

## Interpretation

The per-direction run inequality uses genuine 4AP-free structure beyond simple shadow disjointness.  However, it still does not constrain the small-density regime relevant to the reciprocal-sum problem.

The remaining task is to exploit not only the number of local run features in each direction, but their algebraic compatibility across many directions.

## Next research question

Can cross-direction compatibility of length-three runs and single-zero near-runs improve the high-density cutoff into the desired domination statement

```math
E,I >= m^3/p
quad => quad
E,I <= p?
```
