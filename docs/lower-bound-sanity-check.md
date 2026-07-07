# Lower-bound sanity check for the alpha^{-1+delta} target

## Status

Proof-audit sanity check.  This note asks whether known lower-bound constructions already rule out the proposed density threshold

```math
N >= exp(C alpha^{-1+delta})
```

for forcing a 4-term arithmetic progression.

## Integer lower bounds

Known Behrend--Rankin--O'Bryant style constructions give large `k`-AP-free subsets of `[N]`.  For `k=4`, the lower-bound density has the schematic form

```math
alpha(N) >= exp(-C sqrt(log N))
```

up to secondary logarithmic factors.

Equivalently, these constructions show that one cannot force a 4AP below roughly

```math
log N ~ (log(1/alpha))^2.
```

## Comparison with the desired target

The proposed sufficient threshold for the reciprocal-sum route is much larger:

```math
log N ~ alpha^{-1+delta}
      = exp((1-delta) log(1/alpha)).
```

As `alpha -> 0`,

```math
(log(1/alpha))^2 << alpha^{-1+delta}
```

for every fixed `delta<1`.

Thus known Behrend--Rankin--O'Bryant lower bounds do not contradict a theorem of the form

```math
N >= exp(C alpha^{-1+delta})
```

forcing a 4AP.

## Finite-field interpretation

In the finite-vector-space sandbox, the desired theorem is

```math
n >= C alpha^{-1+delta}
```

for `G=F_p^n`.

Basic product/sphere-type progression-free constructions in finite vector spaces usually give exponentially small densities in `n`, i.e.

```math
alpha ~ exp(-c n),
```

which corresponds only to

```math
n ~ log(1/alpha).
```

This is also far below

```math
alpha^{-1+delta}.
```

So no immediate lower-bound obstruction is visible at the target scale.

## Conclusion

The target

```math
N >= exp(C alpha^{-1+delta})
```

is not ruled out by the classical lower-bound scale.  The barrier is proof-theoretic rather than obviously false.

The main difficulty remains proving such a threshold, not reconciling it with known counterexamples.

## Caution

This is only a sanity check against standard lower-bound scales.  It is not a proof that the target is true, and it does not rule out future lower-bound constructions closer to the alpha^{-1} scale.
