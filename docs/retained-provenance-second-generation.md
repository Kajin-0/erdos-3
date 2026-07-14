# Second-generation retained provenance reuse

## Status

Exact finite two-generation theorem for the retained `S_7` local-optimum family.

The first-generation quotient supplies `21` point-disjoint retained states with explicit root provenance. Each retained state is then resolved by lexicographic coordinated deletion. All descendant shell occurrences are aggregated globally, exact numerical duplicates are quotiented, and the same maximum-harmonic point-conflict rule is applied again.

**Verifier:** `src/verify_retained_provenance_second_generation.py`.

**Certificate:** `data/retained_provenance_second_generation_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
79fca7aa04469adefdd855d08a63b4bbefd7621c6c324d54cd6748f54e734caa
```

---

## 1. Second-generation raw family

The `21` first-generation retained states contain `11,753` points. Fifteen contain a three-term progression and nineteen produce at least one recursive shell occurrence.

Their complete lexicographic transitions contain:

```text
selected actions = 10,426
terminal residual points = 1,327
raw descendant shell occurrences = 442.
```

After exact-state quotienting, the global descendant family has:

```text
exact state classes = 173
point-conflict edges = 1,046
connected components = 22
largest component = 21.
```

The exact component solver visits `204` dynamic-programming states. Every component has a unique maximum-harmonic independent set.

---

## 2. Second retained family

The unique second-generation retained family has:

```text
retained state classes = 27
retained distinct labels = 7,925
dropped distinct labels = 5,900.
```

The retained states are pairwise point-disjoint. Every retained point carries both:

- its immediate parent or sponsor in the first-generation state; and
- its mapped root provenance in the original `S_7` transition.

The retained-family SHA-256 is

```text
dbb6d888c790cf5a67f2e3a6ed86400506c93baac3701f39d15d858c19b21596.
```

---

## 3. Root-provenance reuse

Across the `7,925` retained descendant points, there are `7,648` distinct original `S_7` provenance labels.

The exact multiplicity spectrum is:

| multiplicity | root provenance labels |
|---:|---:|
| 1 | 7,376 |
| 2 | 267 |
| 3 | 5 |

Therefore:

```text
repeated provenance labels = 272
extra provenance occurrences = 277
maximum multiplicity = 3.
```

Only `265` provenance labels are reused across two distinct first-generation retained branches; no provenance label appears in more than two first-generation branches.

The harmonic provenance overhead satisfies

```math
\frac{40}{1000}
<
\frac{H_{\rm repeated}}{H_{\rm unique}}
<
\frac{41}{1000}.
```

Equivalently, occurrence-weighted root provenance is only about `1.04037` times unique root-provenance mass.

This is the first exact finite bound on retained cross-branch provenance reuse.

---

## 4. The scale-expansion obstruction

Despite the modest provenance multiplicity, retained harmonic mass grows sharply:

```math
\frac{6828}{1000}
<
\frac{H_{\rm retained}^{(2)}}{H_{\rm retained}^{(1)}}
<
\frac{6829}{1000}.
```

Thus the second retained family has approximately `6.82863` times the harmonic mass of the first retained family.

Within the second-generation raw family, the retained quotient captures:

```math
0.896
<
\frac{H_{\rm retained}^{(2)}}{H_{\rm raw\ union}^{(2)}}
<
0.897,
```

but only

```math
0.206
<
\frac{H_{\rm retained}^{(2)}}{H_{\rm raw\ occurrences}^{(2)}}
<
0.207.
```

The large inter-generation growth is therefore primarily a scale-contraction effect, not an uncontrolled provenance-multiplicity effect.

---

## 5. Interpretation

A simple multiplicity capacity cannot close the Bellman inequality:

- retained root provenance has maximum multiplicity three;
- harmonic provenance overhead is only `4.0%`–`4.1%`;
- yet retained harmonic mass expands by more than a factor of `6.828`.

The next packing coordinate must couple provenance with at least one of:

```text
scale contraction
terminal or completion obstruction credit
retained-state depth
future cheap-extension exclusion.
```

This theorem does not imply divergence or failure of the overall proof program. It rules out the narrower idea that bounded provenance reuse alone pays for recursive harmonic growth.