# Transition-cost tradeoff between two complete `S_7` policies

## Status

Exact fixed-parent finite comparison.

Reverse-lexicographic deletion avoids the isolated canonical regeneration found
under lexicographic deletion. It does not reduce the raw one-generation
transition cost. On every measured multiplicity and SCC coordinate, the
reverse transition is substantially larger.

**Verifier:** `src/verify_s7_policy_transition_tradeoff.py`.

**Certificate:** `data/s7_policy_transition_tradeoff_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
e4313f37643ad729fb8faa160ae63d5d59d61c521b149258a6aa131485dec70d
```

---

## 1. Compared objects

Both schedules resolve the same parent `S_7` with the same valuation-dependent
side-sponsor rule.

- **Lexicographic policy:** smallest current progression first.
- **Reverse-lexicographic policy:** largest current progression first.

Both are complete coordinated schedules and both leave an exact
three-term-progression-free residual.

The comparison uses middle-fiber outputs before a retention quotient. For
fibers `Xi_q`, define

```math
M_{\rm occ}=\sum_qH(\Xi_q),
```

```math
M_{\rm union}=H\left(\bigcup_q\Xi_q\right),
```

and

```math
M_{\rm dup}=M_{\rm occ}-M_{\rm union}.
```

The harmonic-average multiplicity is

```math
\overline m_H
=
\frac{M_{\rm occ}}{M_{\rm union}}.
```

These are exact transition diagnostics. They are not yet a retained-child
Bellman cost.

---

## 2. Combinatorial size

| coordinate | lexicographic | reverse lexicographic |
|---|---:|---:|
| selected actions | `9,360` | `9,180` |
| residual size | `480` | `660` |
| terminal step labels | `25` | `2,252` |
| middle-fiber shells | `124` | `2,374` |
| fiber-label occurrences | `9,335` | `6,928` |
| distinct fiber labels | `6,683` | `2,239` |
| imported distinct labels | `312` | `1` |
| novel distinct labels | `6,371` | `2,238` |

The reverse policy has fewer raw label occurrences and fewer distinct labels,
but those labels are concentrated at much smaller numerical values and are
reused far more heavily. Cardinality alone therefore gives the wrong policy
ranking.

The normalized terminal-residual errors are

```math
\frac{128\cdot480}{1048576}
=
\frac{15}{256}
```

and

```math
\frac{128\cdot660}{1048576}
=
\frac{165}{2048}.
```

The reverse residual error is also larger.

---

## 3. Harmonic output load

Exact rational arithmetic gives the compact brackets

| mass | lexicographic | reverse lexicographic |
|---|---:|---:|
| terminal-step mass | `(13/10, 4/3)` | `(11/5, 9/4)` |
| middle-fiber occurrence mass | `(19/10, 2)` | `(144, 145)` |
| distinct-union mass | `(17/10, 7/4)` | `(19/5, 4)` |
| duplicate mass | `(3/16, 1/5)` | `(140, 141)` |
| harmonic-average multiplicity | `(11/10, 10/9)` | `(37, 38)` |

The exact fractions are large. Their canonical numerator/denominator hashes
are recorded in the certificate.

The exact reverse-to-lexicographic ratios satisfy

```math
75
<
\frac{M_{\rm occ}^{\rm rev}}{M_{\rm occ}^{\rm lex}}
<
76,
```

```math
2
<
\frac{M_{\rm union}^{\rm rev}}{M_{\rm union}^{\rm lex}}
<
\frac94,
```

and

```math
744
<
\frac{M_{\rm dup}^{\rm rev}}{M_{\rm dup}^{\rm lex}}
<
745.
```

The harmonic-average multiplicity ratio lies between `33` and `34`.

Thus avoiding one canonical return comes with an enormous increase in raw
multiplicity-weighted recursive output.

---

## 4. Terminal-fiber incidence structure

For the directed graph

```math
q\longrightarrow u
\quad\Longleftrightarrow\quad
u\in\Xi_q
\text{ and }u\text{ is terminal},
```

the exact graph metrics are:

| coordinate | lexicographic | reverse lexicographic |
|---|---:|---:|
| directed incidence edges | `75` | `3,087` |
| strongly connected components | `19` | `1,967` |
| cyclic components | `1` | `1` |
| largest SCC size | `7` | `286` |
| maximum fiber-label multiplicity | `15` | `160` |

The lexicographic largest SCC is the previously certified seven-label
component. The reverse policy replaces it with a `286`-label cyclic component.
Exact edge-set and component hashes are included in the certificate.

Avoiding canonical regeneration therefore does not avoid cyclic recursive
structure. It creates a much larger cyclic state.

---

## 5. Consequence

The following policy objective is false:

```text
Prefer any complete coordinated schedule that avoids canonical regeneration.
```

The reverse policy satisfies that narrow objective but is dramatically worse
on terminal complexity, shell count, harmonic output, duplicate mass,
multiplicity, SCC size, and residual error.

A useful policy objective must score the **complete transition**, not one
recognizable descendant.

At minimum it must include:

1. terminal-step mass;
2. total and distinct middle-fiber mass;
3. duplicate or provenance-reuse load;
4. SCC recycling capacity;
5. obstruction coverage;
6. regenerative and near-regenerative future cost;
7. terminal residual error.

---

## 6. Scope

The theorem compares two deterministic schedules only. It does not prove that
lexicographic deletion is globally optimal or that its transition satisfies a
whole-tree inequality.

Raw harmonic occurrence mass is not itself the final Bellman cost. Some
outputs may merge, be dominated, produce obstruction credit, or enter
controlled tails. The result establishes that the reverse policy cannot be
preferred merely because it eliminates the exact canonical return.

---

## 7. Revised target

The next useful object is a common exact policy score

```math
\mathcal C_\pi(S)
=
\text{recursive load}
+
\text{SCC capacity}
+
\text{residual error}
-
\text{certified obstruction credit},
```

with every term normalized into Bellman units and evaluated on the complete
simultaneous transition.

The immediate finite work is:

1. define exact candidate coordinates from the two certified policy payloads;
2. test nonnegative weight systems in the rational LP harness;
3. reject coordinates that rank the reverse transition below lexicographic
   despite its exact load explosion;
4. extend the comparison to additional deterministic policies;
5. search for a policy rule with stable low transition cost across `S_1`
   through `S_7`.
