# U3 inverse black-box target

## Status

Proof-audit note.  This treats the finite-field U3 inverse theorem as a black box and records what strength would be needed to reach the reciprocal-sum threshold through the current finite-field strategy.

## Current finite-field chain

The revised finite-field Green--Tao proof has the schematic chain

```math
U^3 inverse theorem
-> local Koopman-von Neumann theorem
-> codim <= C epsilon^{-2^20}
-> epsilon = alpha^4/2
-> codim <= O(alpha^{-2^22})
-> r_4(F_p^n) << N(log N)^{-2^{-22}}.
```

The paper states that the `2^20` exponent is mostly dependent on the `2^16` exponent in the U3 inverse theorem input.

## Required local theorem strength

Suppose a finite-field local recurrence theorem gave codimension

```math
codim(W) <= C epsilon^{-theta}.
```

Applying it to a 4AP-free set forces

```math
epsilon ~ alpha^4.
```

Then the codimension cost is

```math
codim(W) <= C alpha^{-4 theta}.
```

The reciprocal-sum analogue needs total cost exponent below `1`, hence

```math
4 theta < 1,
```

or

```math
theta < 1/4.
```

## Consequence for inverse-theorem improvements

If the local theorem exponent remains a positive power inherited from a quantitative U3 inverse theorem, then merely reducing `2^16` to a smaller large constant is not enough.

To succeed through this same black-box route, the combined inverse-theorem-plus-localization exponent must be below `1/4` before the `epsilon=alpha^4` substitution.

Thus the necessary target is not:

```math
improve 2^16 substantially.
```

It is:

```math
replace the U3 inverse/localization black box by a mechanism with effective theta < 1/4.
```

## Interpretation

The full U3 inverse theorem may be an overpowered input.  The recurrence problem may not need to classify all functions with large U3 norm; it may need only enough structure to count 4APs in dense sets.

A plausible improvement route would therefore avoid a full inverse theorem and prove a specialized recurrence/counting theorem with lower codimension cost.

## Next research question

Can one prove a 4AP-specific local counting theorem in `F_p^n` with

```math
codim(W) <= C epsilon^{-theta}
```

for some `theta<1/4`, without proving a comparably strong full U3 inverse theorem?
