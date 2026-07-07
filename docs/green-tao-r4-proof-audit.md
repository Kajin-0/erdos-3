# Green--Tao r_4(N) proof audit

## Status

Working proof-audit note.  This is not a proof of the reciprocal-sum conjecture; it identifies the
quantitative bottleneck that would have to be improved.

## Starting point

Green--Tao Part III proves

```math
r_4(N) \ll N(\log N)^{-c}
```

for some absolute `c>0`.

The reciprocal-sum Erdős problem for `k=4`, via dyadic summability, would follow from any bound with
summable dyadic density, for example

```math
r_4(N) \ll \frac{N}{(\log N)^{1+\epsilon}}.
```

Thus the concrete target is to push the logarithmic exponent effectively past `1`, or to obtain a
non-power-log decay strong enough that

```math
\sum_j r_4(2^j)/2^j < \infty.
```

## Abstract density-increment model

Let `A subset [N]` have density `alpha` and no 4AP.

A density-increment proof usually produces a structured set `B` of reduced scale `N'` such that

```math
\alpha' \ge \alpha + \Delta(\alpha)
```

and

```math
\log N' \ge \Lambda(\alpha) \log N
```

or an analogous Bohr-set radius/dimension lower bound.

The final exponent comes from the balance between:

1. the increment size `Delta(alpha)`;
2. the scale-loss function `Lambda(alpha)`;
3. regularization losses for Bohr sets or progressions;
4. the number of iterations needed before density exceeds `1`.

## Summability threshold

The dyadic target requires the iteration to exclude densities

```math
\alpha \gg (\log N)^{-1-\epsilon}.
```

So it is not enough to show a generic positive power of `log N`.  The proof must maintain enough
scale through enough increments to beat the `1/log N` summability boundary.

## Audit checklist

The proof should be decomposed into the following quantitative modules.

### 1. Counting-to-uniformity step

No 4APs should imply a large enough `U^3`-type obstruction.  The quantitative loss here affects the
starting size of the structured object.

Questions:

- What exact lower bound on the relevant uniformity norm follows from zero 4APs at density `alpha`?
- Is the dependence polynomial in `alpha`, exponential in a power of `alpha^{-1}`, or worse?

### 2. Inverse/structure theorem

The large `U^3` obstruction must produce correlation with quadratic or locally quadratic structure.

Questions:

- What is the quantitative correlation strength in terms of `alpha`?
- What dimension/rank/complexity is introduced?
- Is this step the source of the small final logarithmic exponent?

### 3. Density increment

The structured correlation must give a genuine density increment on a large enough substructure.

Questions:

- Is the density gain comparable to `alpha^C`, `alpha^C / log(1/alpha)^C`, or something weaker?
- Is the increment on an arithmetic progression, a Bohr set, or a more complicated local object?

### 4. Scale loss and regularization

The substructure must remain large enough for iteration.

Questions:

- How much does the ambient scale shrink per increment?
- Does Bohr-set regularization cause exponential losses in dimension?
- Does the radius shrink by a polynomial or exponential function of `alpha`?

### 5. Iteration accounting

If each step increases density by roughly `Delta(alpha)`, the number of steps needed is about

```math
\int_{\alpha}^{1} \frac{dt}{\Delta(t)}.
```

This must be compared against cumulative scale loss.

Questions:

- What exponent `c` is produced by the published bookkeeping?
- Which module controls that exponent?
- What quantitative strengthening would be enough to force `c>1`?

## Working conclusion

The most direct route to the `k=4` reciprocal-sum case is not another construction search.  It is a
quantitative improvement to the `r_4(N)` density-increment machinery sufficient to make

```math
\sum_j r_4(2^j)/2^j
```

converge.

The immediate next task is to extract the actual quantitative dependencies from Green--Tao Part III
and identify the dominant loss term.
