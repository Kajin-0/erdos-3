# Scale-eight benchmark: immediate open questions

The exact scale-eight family changes the next quantitative questions.

1. **Universal weighted-density decay.** Is there `epsilon>0` such that every aligned-diamond persistence event of multiplicity `P` in a block `D subseteq[N,2N)` satisfies

   ```math
   P\frac{|D|}{N}\ll P^{-\epsilon}?
   ```

   The scale-eight family permits at most

   ```math
   \epsilon\le 2-\log_2 3\approx0.4150375
   ```

   for a sharp power-law statement.

2. **Aggregate charging.** If a point participates in several nested persistence events, can its reciprocal mass be charged with total weight bounded by an absolute constant or a summable function of depth?

3. **Near-extremal classification.** Does persistence near `L^(1/3)` force an approximate alternating base-eight translate structure?

4. **Beyond the exact three-translate model.** The note

   ```text
   docs/three-translate-dyadic-scale-barrier.md
   ```

   proves that every exact standard-dyadic three-translate replication step satisfies

   ```math
   L'\ge8L.
   ```

   Therefore the scale-eight construction is ambient-scale optimal inside that model, and a factor below `8` is impossible there. The remaining sharpness question is whether a more general persistence mechanism—overlapping layers, several parent states, nonuniform branching, or reproduction distributed across shells—can beat the exponent `1/3`.

5. **Pure proof of the automaton certificate.** Can the 34-state product/carry computation be compressed into a short invariant or hand-checkable state quotient?

The first two questions are the active closing directions. The third and fourth determine whether the exact three-translate obstruction is representative of all near-extremal persistence. The fifth would improve auditability.
