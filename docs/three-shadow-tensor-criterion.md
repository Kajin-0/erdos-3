# Three-shadow form of the tensor obstruction criterion

## Status

Proof-audit reformulation.  This converts the tensor sign criterion into finite counts of three-point shadows of a 4AP hypergraph.

## Setup

Let `A subset F_p` be 4AP-free and let

```math
m = |A|,
qquad
alpha = m/p.
```

For each `i in {0,1,2,3}`, define the three-shadow count

```math
N_i
= # { (x,d) in F_p^2 : x+jd in A \text{ for every } j != i }.
```

Thus `N_i` counts the number of partial 4APs missing only the `i`th slot.

Since `A` is 4AP-free, the only full 4APs inside `A` have `d=0`, so

```math
lambda_4 = Lambda_4(1_A,1_A,1_A,1_A) = m/p^2.
```

Therefore the normalized full 4AP ratio is

```math
a = lambda_4/alpha^4 = p^2/m^3.
```

The normalized three-shadow ratios are

```math
r_i = (N_i/p^2)/alpha^3 = p N_i/m^3.
```

## Product obstruction in shadow counts

The tensor-power pure four-balanced enemy criterion was

```math
r_i >= 1 \quad\forall i,
qquad
max_i r_i > max(a,1).
```

In terms of `N_i`, this becomes

```math
N_i >= m^3/p \quad\forall i,
```

and

```math
max_i N_i > max(p, m^3/p).
```

Thus a product/tensor pure enemy would be a 4AP-free base set whose every three-shadow is at least random-sized, and whose largest three-shadow exceeds both:

1. the random shadow scale `m^3/p`; and
2. the trivial full-AP scale `p`.

## Interpretation

This is a concrete finite combinatorial obstruction search.

The enemy object is not merely a 4AP-free set with many three-point patterns.  It must have all four partial-AP shadows nondeficient and at least one shadow large enough to dominate the full-AP ratio under tensoring.

## Relation to previous examples

The `F_11` tensor-negative example has a shadow large enough to make `Q_n<0`, but not all shadows are nondeficient; hence negative trilinear terms persist.

The `F_17` pure small model has all shadows nondeficient at level `n=1`, but no shadow dominates the full-AP ratio.  Hence tensor powers make `Q_n>0` for `n>=2`.

## Candidate shadow-domination conjecture

A possible obstruction to product enemies is:

> If `A subset F_p` is 4AP-free and `N_i >= m^3/p` for every `i`, then `N_i <= p` for every `i`.

Equivalently, if every three-shadow is at least random-sized, then no three-shadow can exceed the trivial full-AP scale enough to dominate tensor powers.

This conjecture is not proved here.  It is consistent with the exhaustive search for `p <= 19` recorded in the tensor sign criterion.

## Why this matters

If the shadow-domination conjecture were true, then direct tensor powers cannot produce an asymptotic pure four-balanced obstruction.

The obstruction search would then have to move to one of:

1. non-product constructions;
2. constructions arising after localization or projection;
3. high-dimensional examples with no one-dimensional tensor base;
4. an argument proving that four-balanced negativity forces trilinear negativity after low-codimension localization.

## Next research question

Can the shadow-domination conjecture be proved by additive combinatorial inequalities, or does it fail at larger primes?
