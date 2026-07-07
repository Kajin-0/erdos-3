# Source of the finite-field 2^-22 exponent

## Status

Proof-audit note.  This records where the finite-field exponent `2^-22` enters Green--Tao's revised finite-field 4AP result.

## Published theorem-to-corollary chain

Green--Tao's Theorem 1.1 states, in effect, that for a subset `A` of `F_p^n` of density at least `alpha`, and for parameters `0<alpha,epsilon<=1`, there is an affine subspace `W` of codimension at most

```math
C_F epsilon^{-2^{20}}
```

on which the 4AP recurrence count is bounded below up to error `epsilon`.

The paper then derives Corollary 1.2 by applying Theorem 1.1 to a 4AP-free set with

```math
epsilon = alpha^4/2.
```

This gives codimension at most

```math
C_F (alpha^4/2)^{-2^{20}}
  = O_F(alpha^{-4 * 2^{20}})
  = O_F(alpha^{-2^{22}}).
```

Combining this with the fact that a 4AP-free set contributes only trivial progressions on `W` yields

```math
alpha >= c_F (log N)^{-2^{-22}},
```

or equivalently

```math
r_4(F_p^n) <<_F N (log N)^{-2^{-22}}.
```

## Main source of 2^20

The paper explicitly states that the exponent `2^{20}` is mostly dependent on the exponent `2^{16}` in the inverse theorem for the `U^3` norm used as an input.  Improvements to that inverse-theorem exponent would improve the exponent in Theorem 1.1.

Thus the finite-field exponent loss is not mainly from Bohr-radius bookkeeping.  In the finite-field model, the visible bottleneck is:

```math
U^3 inverse theorem exponent
-> local Koopman-von Neumann theorem
-> codimension epsilon^{-2^{20}}
-> epsilon=alpha^4
-> final alpha^{-2^{22}} cost.
```

## Consequence for the sandbox

The finite-field model removes the cyclic-group Bohr-radius issue, but it still has a huge exponent barrier because the local structure theorem has codimension cost

```math
epsilon^{-2^{20}}.
```

To reach the reciprocal-sum analogue, one would need a theorem with codimension cost roughly

```math
epsilon^{-theta}
```

where, after setting `epsilon ~ alpha^4`, the total density exponent satisfies

```math
4 theta < 1.
```

Equivalently,

```math
theta < 1/4.
```

The published theorem has

```math
theta = 2^{20}.
```

So improving only constants is irrelevant; one would need a qualitatively stronger local structure/counting theorem.

## Next audit target

Inspect the finite-field `U^3` inverse theorem dependency.  The precise question is whether the `2^{16}` inverse-theorem exponent is structurally necessary for 4AP recurrence, or merely an artifact of the inverse theorem used in this proof.
