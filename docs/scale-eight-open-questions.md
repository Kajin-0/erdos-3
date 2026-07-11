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

Four-term-progression-freeness also permits at most three equal translate layers, while the occurrence genealogy permits at most two persistent children. The scale-eight construction attains all resulting exponents. Thus ambient scale, persistence, density decay, and aggregate weighted-density charge are sharp within the exact equal-translate model.

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

4. **Beyond equal translates.** Can a genuinely non-equal, overlapping, or cross-parent construction produce a larger effective branching-density ratio than `3/4`?

5. **Pure proof of the automaton certificate.** Can the 34-state product/carry computation be compressed into a short invariant or hand-checkable state quotient?

## Active quantitative target

For a recursive segment, define its effective weighted-density ratio schematically as

```math
\rho
=
\frac{
\text{persistent-child multiplicity factor}
\times
\text{support-cardinality factor}
}{
\text{dyadic-scale factor}
}.
```

The exact equal-translate segment has

```math
\rho=\frac{2\cdot3}{8}=\frac34.
```

The next theorem should define this defect rigorously for general recursive segments and prove a dichotomy:

1. **near-exact case:** `rho` is close to `3/4`, forcing structural proximity to the exact three-translate architecture;
2. **defective case:** `rho` is bounded below `3/4` by a uniform amount, yielding stronger geometric contraction.

After that, the remaining task would be packing and overlap control among near-exact segments.
