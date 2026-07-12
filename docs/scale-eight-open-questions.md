# Persistence benchmark: revised open questions

The exact scale-eight family and the companion elementary theorems classify the canonical exact standard-dyadic equal-translate obstruction. The finite contaminated-backbone chain shows that this classification does not extend locally once the backbone is allowed to contain, rather than equal, the replay state.

## Resolved inside the exact model

The notes

```text
docs/three-translate-dyadic-scale-barrier.md
docs/exact-three-translate-weighted-density-theorem.md
```

prove

```math
L'\ge8L,
```

```math
P\le(L/L_0)^{1/3},
```

```math
P\alpha(P)\ll P^{\log_2 3-2},
```

and

```math
\sum_hP_h\alpha_h<\infty.
```

The exact one-step efficiency is

```math
\rho_{\mathrm{exact}}
=
\frac{2\cdot3}{8}
=
\frac34.
```

The scale-eight construction attains the resulting exponents.

## New finite obstruction to local contraction

The note

```text
docs/contaminated-backbone-depth-five-chain.md
```

constructs certified four-term-progression-free states with scale factors

```math
4,8,4,4.
```

At every step, the middle fiber is the previous state exactly and the backbone shell contains a replayable copy of the previous state. The certified multiplicity-weighted density grows by

```math
\boxed{
\frac{W_5}{W_1}
=
\frac{91}{32}.
}
```

Therefore the following approaches are false:

1. universal one-step `3/4` contraction outside the exact model;
2. universal strict contraction for every contaminated step;
3. contraction over every block of four consecutive steps;
4. a dichotomy in which every non-exact step automatically contracts more strongly than an exact step.

## Remaining questions

1. **Long-run scale compensation.** Must every sufficiently long contaminated genealogy satisfy

   ```math
   \prod_{h=1}^{H}c_h
   >
   6^H
   ```

   after accounting for lower-order cardinality terms, where `c_h=L_{h+1}/L_h`?

2. **Contamination debt.** Is there a monotone quantity that increases during scale-factor `4` steps and must later be discharged through a larger scale jump, exported difference structure, or a forbidden progression?

3. **Indefinite extension.** Can the finite factor pattern be extended indefinitely, periodically, or with geometric-mean scale below `6`? A positive answer would invalidate multiplicity-weighted density decay as the closing invariant.

4. **Finite-state classification.** Do indefinitely repeatable contaminated patterns admit a finite symbolic description whose spectral radius controls the long-run ratio between support growth, persistence, and dyadic scale?

5. **Aggregate charging.** If several contaminated genealogies overlap, can their replay cores and contaminating points be assigned bounded total charge?

6. **Pure proof of finite-state certificates.** Can the automaton computations for the exact family, and any future contaminated family, be compressed into short invariants or hand-checkable quotients?

## Active quantitative target

For a contaminated step define

```math
B_h
=
G_{h+1}\cap[L_h,2L_h),
```

and contamination

```math
\kappa_h
=
|B_h\setminus S_h|.
```

The depth-five chain has

```math
(\kappa_1,\kappa_2,\kappa_3,\kappa_4)
=
(4,1,33,1),
```

so contamination cardinality alone does not correlate monotonically with the immediate scale factor.

The next theorem should introduce a richer overlap potential that records where contaminating points originate and how they propagate into later translate layers. The desired conclusion is not local contraction but a long-horizon inequality of the form

```math
W_H
\le
C\,\Theta_H W_0,
```

where `Theta_H` is summable or tends to zero after all contamination debt is included.
