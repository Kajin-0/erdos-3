# Fourth-to-fifth local policy sensitivity

## Scope

This theorem tests whether the certified fourth-to-fifth recursive expansion is a fragile artifact of lexicographic descendant deletion.

The parent family is the certified fourth recursive retained family:

```text
states = 12
points = 1,717
harmonic mass = 1.536133538213...
```

Each parent is resolved once lexicographically and once reverse lexicographically. The finite policy family consists of:

1. all twelve parents lexicographic;
2. all twelve parents reverse lexicographic;
3. each of the twelve single-parent lexicographic-to-reverse flips.

Every raw output family is passed through the same retention rule:

1. exact numerical state quotienting;
2. deterministic provenance representatives;
3. same-shell point-intersection conflicts;
4. maximum-total-harmonic independent-set selection in each component.

For components with tied maximum-harmonic optima, the verifier computes the minimum and maximum recursively continuing harmonic mass over **all** tied optima.

This is a finite local policy theorem. It is not universal over arbitrary coordinated deletion schedules or arbitrary retention rules.

## Exact result

All fourteen tested policies expand recursively under every maximum-harmonic retention tie choice.

The baseline satisfies

```math
1.329813
<
\frac{H_5^{\mathrm{rec}}}{H_4^{\mathrm{rec}}}
<
1.329814.
```

The best tested policy reverses only parent class `82`:

```math
\boxed{
\frac{9579}{8000}
<
\frac{H_{5,\,82\text{-reverse}}^{\mathrm{rec}}}
     {H_4^{\mathrm{rec}}}
<
\frac{18709}{15625}
}
```

or numerically

```text
1.197375982982...
```

Thus the local policy change reduces the expansion materially, but does not produce contraction.

The all-reverse policy has the same recursive harmonic mass as the all-lexicographic baseline, despite producing a substantially different retained and terminal family.

Two policies have nonunique maximum-harmonic conflict optima:

```text
all_reverse
reverse_parent_82
```

Each has exactly two global optima. In both cases the tied optima have identical recursive harmonic mass, so retention tie-breaking cannot remove the recorded expansion.

## Interpretation

The fourth-to-fifth failure is not eliminated by the nearest natural deletion-policy perturbations.

The result supports three conclusions:

1. the expansion is not merely a lexicographic tie-breaking accident;
2. policy choice still matters quantitatively, because reversing parent `82` lowers the ratio from about `1.3298` to `1.1974`;
3. a complete theorem cannot rely on maximizing immediate retained harmonic mass alone.

The correct next object is not a larger finite policy score. It is a transition law that explains how scale gain, terminalization, and discarded lineage mass transfer capacity across generations.

## Reproduction

```bash
python3 src/run_exact_python.py \
  src/verify_fourth_to_fifth_policy_sensitivity.py \
  /tmp/fourth_to_fifth_policy_sensitivity_certificate.txt

cmp \
  data/fourth_to_fifth_policy_sensitivity_certificate_2026-07-14.txt \
  /tmp/fourth_to_fifth_policy_sensitivity_certificate.txt
```

Recorded certificate SHA-256:

```text
996d444724e5081986509fe539542ab19508c648ca9f8158650b387b542d6769
```
