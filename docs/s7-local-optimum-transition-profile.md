# S7 local-optimum raw transition profile

## Status

Exact finite comparison of three complete `S_7` coordinated deletion schedules:

```text
lexicographic
seed_5_142
37-step terminal-neighborhood local optimum.
```

The comparison uses the complete raw simultaneous occurrence family before any retention quotient.

**Verifier:** `src/verify_s7_local_optimum_transition_profile.py`.

**Certificate:** `data/s7_local_optimum_transition_profile_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
1bf8d15efd7c8cb1f9b04fba769d19e43d2b630d9fe36f141bbcc4466f9bb19e
```

---

## 1. Exact structural comparison

| coordinate | lexicographic | `seed_5_142` | local optimum |
|---|---:|---:|---:|
| selected actions | 9,360 | 9,347 | 9,323 |
| residual size | 480 | 493 | 517 |
| terminal step classes | 25 | 50 | 28 |
| middle-fiber occurrences | 9,335 | 9,297 | 9,295 |
| distinct middle labels | 6,683 | 6,169 | 7,278 |
| imported middle labels | 312 | 305 | 346 |
| novel middle labels | 6,371 | 5,864 | 6,932 |
| dyadic shell occurrences | 127 | 227 | 131 |
| exact shell state classes | 95 | 144 | 87 |
| duplicate state groups | 20 | 45 | 22 |
| strict containments | 345 | 1,028 | 229 |
| partial overlaps | 214 | 1,180 | 390 |
| maximum point multiplicity | 16 | 34 | 18 |
| terminal-fiber incidence edges | 75 | 141 | 83 |
| cyclic SCCs | 1 | 1 | **0** |
| largest SCC | 7 | 2 | **1** |

The local-optimum terminal-fiber graph is acyclic. This removes the specific SCC recycling obstruction present in both reference policies.

---

## 2. Harmonic load

Let `O_mid` denote total middle-fiber occurrence mass and `O_raw` denote total recursive shell occurrence mass, including the backbone shells.

The exact ratios satisfy

```math
\frac{247}{1000}
<
\frac{O_{\rm mid}^{\rm local}}{O_{\rm mid}^{\rm lex}}
<
\frac{248}{1000},
```

and

```math
\frac{513}{1000}
<
\frac{O_{\rm mid}^{\rm local}}{O_{\rm mid}^{\rm seed}}
<
\frac{514}{1000}.
```

For the complete raw recursive occurrence family,

```math
\frac{254}{1000}
<
\frac{O_{\rm raw}^{\rm local}}{O_{\rm raw}^{\rm lex}}
<
\frac{255}{1000},
```

and

```math
\frac{522}{1000}
<
\frac{O_{\rm raw}^{\rm local}}{O_{\rm raw}^{\rm seed}}
<
\frac{523}{1000}.
```

Thus the optimized policy cuts raw harmonic occurrence load to roughly one quarter of lexicographic deletion and one half of `seed_5_142`.

---

## 3. The remaining retention obstruction

The improvement is not uniform across overlap coordinates.

Relative to lexicographic deletion:

- strict containments decrease from `345` to `229`;
- the terminal-fiber cycle disappears;
- harmonic occurrence load falls sharply;
- but partial overlaps increase from `214` to `390`;
- and maximum point multiplicity rises from `16` to `18`.

The raw family is therefore still non-disjoint. Eliminating cyclic terminal-label recycling does not by itself establish a retained-child packing inequality.

The next theorem must specify how overlapping shell occurrences are retained or charged with provenance. It must control at least:

```text
exact duplicates
strict containment
partial overlap
point multiplicity
cross-generation provenance reuse.
```

This profile is now the principal adversarial test for any proposed retention quotient.