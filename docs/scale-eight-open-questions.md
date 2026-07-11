# Scale-eight benchmark: immediate open questions

The exact scale-eight family and the companion elementary theorems now classify the canonical exact standard-dyadic equal-translate obstruction.

## Resolved inside the exact model

The notes

```text
docs/three-translate-dyadic-scale-barrier.md
docs/exact-three-translate-weighted-density-theorem.md
```

prove:

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

The scale-eight construction attains the exponents. Thus ambient scale, persistence, density decay, and aggregate weighted-density charge are sharp within the exact three-translate model.

## Remaining questions

1. **General weighted-density decay.** Does there exist `epsilon>0` such that every aligned-diamond persistence event of multiplicity `P` in a block `D subseteq[N,2N)` satisfies

   ```math
   P\frac{|D|}{N}\ll P^{-\epsilon}?
   ```

   The exact-model theorem proves this with

   ```math
   \epsilon=2-\log_2 3\approx0.4150375
   ```

   for one exact genealogy. The unresolved issue is whether overlap, cross-parent merging, approximate recurrence, or multishell persistence can destroy decay.

2. **General aggregate charging.** Can arbitrary persistence be decomposed into genealogies whose total multiplicity-weighted dyadic density is summable? The exact model has the explicit bound

   ```math
   \sum_hP_h\alpha_h
   \le
   4\frac{n_0+3/2}{L_0}.
   ```

   The obstruction is interaction among many non-disjoint genealogies.

3. **Near-extremal classification.** Does persistence near `L^(1/3)` force an approximate alternating base-eight translate structure, or at least an approximate equal-translate architecture with local efficiency near `3/4`?

4. **Beyond equal translates.** Four-term-progression-freeness permits at most three equal translate layers, and the binary genealogy permits at most two persistent children. Can a genuinely non-equal, overlapping, or cross-parent construction produce a larger effective branching-density ratio?

5. **Pure proof of the automaton certificate.** Can the 34-state product/carry computation be compressed into a short invariant or hand-checkable state quotient?

## Active target

The next theorem should define and control a quantitative defect from exact replication. A useful result would show that every persistence genealogy either:

1. contains a long exact or near-exact segment, to which the sharp `3/4` contraction applies; or
2. pays a uniform additional loss in multiplicity-weighted density.

This would reduce the full bottleneck to packing and overlap control among near-exact segments.
