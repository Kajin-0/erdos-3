# Finite-field exponent calibration

## Status

Proof-audit calibration note for the finite-vector-space sandbox.

## Published finite-field bound

For fixed prime `p>4` and `G=F_p^n`, Green--Tao's revised finite-field 4AP result gives

```math
r_4(G) << |G| (log |G|)^{-c}
```

with explicit exponent

```math
c = 2^{-22}.
```

This is a positive polylogarithmic saving, but it is far below the summability threshold `c>1`.

## Cost-function conversion

A bound of the form

```math
r_4(G) << |G| (log |G|)^{-c}
```

corresponds to a finite density threshold of the schematic form

```math
|G| >= exp(C alpha^{-1/c})
```

or, since `|G|=p^n`,

```math
n >= C_p alpha^{-1/c}.
```

For `c=2^{-22}`, this is

```math
n >= C_p alpha^{-2^22}.
```

Thus the known finite-field result corresponds to a codimension/ambient-dimension cost exponent about

```math
theta = 2^22,
```

whereas the reciprocal-sum analogue would need

```math
theta < 1.
```

## Consequence

The finite-vector-space model is cleaner than the integer model because subspace codimension replaces Bohr radius, but the known finite-field theorem is not close to the reciprocal-sum threshold.

The gap is enormous:

```math
known:  theta = 2^22
needed: theta < 1.
```

Therefore the finite-field sandbox should not be treated as an already successful replacement architecture.  It is a diagnostic model for determining whether the `alpha^{-1}` barrier is structural even before cyclic-group Bohr-radius losses enter.

## Next audit question

Where does the `2^{-22}` exponent arise in the revised finite-field proof?

If it comes from repeated density increments and inverse-theorem losses, then the obstruction is likely intrinsic to current 4AP machinery.

If it comes from avoidable bookkeeping specific to the proof, the finite-field model may still be the right place to search for a thinner-loss architecture.
