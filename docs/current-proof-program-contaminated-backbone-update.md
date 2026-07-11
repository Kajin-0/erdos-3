# Current proof program update: contaminated-backbone replication

## Status

This update supersedes the proposed local near-exact/defective contraction target outside the exact equal-translate model.

The full Erdős problem remains open.

## New certified finite chain

There are four-term-progression-free states

```math
S_h\subseteq[L_h,2L_h),
\qquad 1\le h\le5,
```

with dyadic scale factors

```math
4,8,4,4
```

and certified identical-history persistence lower bound

```math
P_h^{\mathrm{cert}}=2^h.
```

At each outer step, the middle fiber is the previous state exactly. The relevant backbone shell is contaminated but contains the previous state, allowing the same nested deletion schedule to be replayed.

For

```math
W_h
=
P_h^{\mathrm{cert}}\frac{|S_h|}{L_h},
```

the chain satisfies

```math
\boxed{
\frac{W_5}{W_1}
=
\frac{91}{32}.
}
```

Thus multiplicity-weighted density grows over four outer steps.

**Primary note:** `docs/contaminated-backbone-depth-five-chain.md`.

**Verifier:** `src/verify_contaminated_backbone_depth5.py`.

## Correction to the previous target

The exact-model theorem remains valid when the backbone shell equals the replay state. In that setting the scale factor is at least `8` and the sharp local weighted-density ratio is `3/4`.

The finite chain proves that the following extension is false:

```math
\text{every non-exact or contaminated step contracts at least as strongly as the exact step.}
```

It also rules out any theorem asserting contraction over every window of four consecutive outer generations.

Therefore a local efficiency dichotomy is not sufficient.

## Revised active bottleneck

The next theorem must be global in replication depth. The active target is

```math
\boxed{
\text{prove long-run compensation for cheap contaminated-backbone steps.}
}
```

For disjoint three-translate growth,

```math
|S_{h+1}|=3(|S_h|+1)
```

and persistence doubles. If

```math
c_h=\frac{L_{h+1}}{L_h},
```

then

```math
\boxed{
\frac{W_{h+1}}{W_h}
=
\frac{6}{c_h}
\left(1+\frac1{|S_h|}\right).
}
```

Ignoring the lower-order term, long-run contraction requires geometric-mean scale expansion greater than `6`.

The certified four-step segment has

```math
\prod_{h=1}^{4}c_h
=512
<6^4=1296.
```

Any universal compensation theorem must therefore operate on a horizon longer than four steps.

## Research priorities

1. **Extension search.** Determine whether the factor pattern can be continued indefinitely, periodically, or with geometric-mean scale below `6`.
2. **Contamination genealogy.** Track the origin and descendants of points in
   ```math
   B_h\setminus S_h.
   ```
3. **Recovery theorem.** Prove that cheap steps force later large scale jumps, exported difference mass, or a forbidden progression.
4. **Finite-state reduction.** Determine whether indefinitely repeatable patterns admit a finite symbolic model and computable spectral radius.
5. **Aggregate packing.** Control overlap among multiple contaminated replay cores.

A negative result for indefinite extension would support the proof program. A positive indefinite construction with geometric-mean scale at most `6` would invalidate multiplicity-weighted density as the closing invariant and force a new route.
