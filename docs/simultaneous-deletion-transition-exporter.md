# Exact simultaneous deletion-transition exporter

## Status

Exact finite infrastructure and certified reference outputs for the recorded states `S_1`, `S_2`, and `S_3`.

The exporter converts one complete fixed-policy coordinated deletion resolution into a machine-readable ledger containing:

1. every selected progression and sponsor;
2. the terminal residual and terminal step outputs;
3. every middle multiplicity fiber;
4. the minimum-translation backbone;
5. every standard-dyadic recursive shell occurrence;
6. point-level parent or sponsor provenance;
7. exact duplicate state classes;
8. strict containment relations;
9. partial overlap relations;
10. exact occurrence, union, imported, novel, and duplicate harmonic masses.

The emitted occurrences are generated **simultaneously** by one complete parent resolution. They are not automatically disjoint retained Bellman children.

**Exporter:** `src/export_simultaneous_deletion_transition.py`.

**Certificate:** `data/simultaneous_deletion_transition_certificate_2026-07-13.txt`.

---

## 1. Fixed schedule policy

For a recorded parent state `D`, order all initially available nontrivial three-term progressions by

```text
(step, left endpoint, middle, right endpoint).
```

Choose the first progression still contained in the current set. For step `q`, delete the left endpoint when `v_2(q)` is even and the right endpoint when `v_2(q)` is odd.

Deletion cannot create a new progression. The exporter therefore constructs the initial progression heap once and discards stale entries after each sponsor deletion. This is exactly equivalent to re-enumerating the current state at every step.

The schedule is deterministic and complete: termination occurs precisely when the residual is three-term-progression-free.

---

## 2. Raw simultaneous output family

For the selected centers `X_q`, the middle multiplicity resolution retains one terminal representative for each distinct step and creates

```math
\Xi_q
=
\{x-\min X_q:x\in X_q,\ x>\min X_q\}.
```

The other recursive output is the minimum-translation backbone

```math
\mathcal B(D)
=
\{d-\min D:d\in D,\ d>\min D\}.
```

Each of these sets is partitioned into standard dyadic shells. Every shell is recorded as a separate recursive occurrence with:

```text
source type;
source step;
shell exponent and shell scale;
numerical values;
parent-point or sponsor provenance;
exact harmonic mass;
canonical state hash.
```

This is the complete raw simultaneous occurrence family for the fixed schedule.

---

## 3. Three overlap layers

The exporter distinguishes three relations that must not be conflated.

### Exact duplicates

Two occurrences are exact duplicates when their shell states have identical numerical support. These are grouped into exact state classes with a representative and multiplicity.

### Strict containment

An occurrence `A` is strictly contained in occurrence `B` when

```math
A\subsetneq B.
```

Exact-state quotienting does not resolve this overlap.

### Partial overlap

Two occurrences partially overlap when their intersection is nonempty but neither contains the other. The exporter records the exact intersection and harmonic mass.

A Bellman child sum requires a theorem specifying how all three relations are charged. The exporter deliberately applies no retention quotient.

---

## 4. Point-level provenance

For every recursive numerical label, the payload records every occurrence containing that label and the corresponding origin:

- for backbone labels, the parent point `min(D)+u`;
- for middle-fiber labels, the sponsor associated with the nonminimal center.

Thus two identical numerical shell states can retain distinct genealogical origins. Conversely, one numerical label can occur in several exact, contained, or partially overlapping states.

This provenance is the minimum data needed to test bounded reuse across generations.

---

## 5. Exact certified reference counts

| state | selected progressions | residual size | terminal steps | recursive occurrences | exact state classes | duplicate classes | strict containments | partial overlaps |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `S_1` | 6 | 6 | 2 | 5 | 4 | 1 | 1 | 0 |
| `S_2` | 26 | 13 | 5 | 11 | 10 | 1 | 3 | 5 |
| `S_3` | 92 | 28 | 10 | 25 | 21 | 3 | 23 | 15 |

The terminal labels already occurring recursively are

```text
S1: 1
S2: 1,61
S3: 1,61,303.
```

The overlap structure becomes substantially more complex by `S_3`: exact-state quotienting reduces `25` occurrences to `21` numerical state classes, but `23` strict containments and `15` partial intersections remain.

---

## 6. Exact middle-fiber mass decomposition

For one fixed schedule, write

```math
F=\bigcup_q\Xi_q.
```

The exporter records

```math
\sum_qH(\Xi_q)
=
\text{internal duplicate mass}
+
H(F\cap\mathcal B(D))
+
H(F\setminus\mathcal B(D)).
```

### `S_1`

```math
\text{internal duplicate mass}=0,
```

```math
H(F\cap\mathcal B(S_1))
=
\frac{5017}{4368},
```

```math
H(F\setminus\mathcal B(S_1))=0.
```

### `S_2`

```math
\text{internal duplicate mass}
=
\frac{383}{10614},
```

```math
H(F\cap\mathcal B(S_2))
=
\frac{218348937262}{1897648393355},
```

```math
H(F\setminus\mathcal B(S_2))
=
\frac{239396453}{200655312}.
```

### `S_3`

```math
\text{internal duplicate mass}
=
\frac{741175084808507}{5412538546014600},
```

```math
H(F\cap\mathcal B(S_3))
=
\frac1{202},
```

while the exact positive novel mass is

```math
\frac{263794861279616516530714602143928959351406948378652487}
{188399844058271400580736246041286596162958326209093600}.
```

The data show that imported support can become small while duplication, containment, and partial overlap remain nontrivial.

---

## 7. Payload hashes

The complete canonical JSON payload hashes are

```text
S1: 98d55ecdbbf94402eee1b82a2437d531fd2ad2d933924597d79a7266a4ac73ae
S2: 8cc11f1cdff33b6b8756d33b97fc6b550159e9ffc9fda5032e35f3195b739b4e
S3: 7bd2e36bb5f1ee4485739b910b3e804fb311da2019d54e09dfdc91df899c75c7
```

The compact certificate SHA-256 is

```text
e8162ee59d496bec8fe2d4103edc8f79de9fbd42444ef37f41fc317aec13a14b
```

---

## 8. Usage

Run the exact `S_1` through `S_3` self-test:

```bash
python3 src/export_simultaneous_deletion_transition.py self-test \
  /tmp/simultaneous_deletion_transition_certificate.txt
```

Export a complete ledger:

```bash
python3 src/export_simultaneous_deletion_transition.py export \
  --state-depth 2 \
  --output /tmp/S2_simultaneous_transition.json
```

The exporter can be run on later recorded states, but the `S_1` through `S_3` payloads are the lightweight regression frontier. Larger states may produce large schedules and overlap ledgers.

---

## 9. Consequence for the proof program

The former missing “adapter” is now split into two mathematically distinct layers.

### Completed layer: raw simultaneous transition export

For a fixed policy, the repository can now produce the complete occurrence family with exact provenance and overlap relations.

### Missing layer: retention and packing theorem

The repository still cannot replace that family by a Bellman child list because it lacks a theorem deciding:

1. which exact duplicate occurrences should be merged;
2. how strict containment is charged;
3. how partial overlap is charged;
4. whether provenance-distinct copies may both retain future value;
5. how the same numerical label is prevented from being charged repeatedly in descendants.

The next exact target is therefore a **retention quotient with a bounded-reuse certificate**, not another raw transition enumerator.

---

## 10. Scope

The exporter proves completeness only for the fixed lexicographic coordinated policy applied to the selected parent. It does not prove:

- policy optimality;
- schedule independence;
- a valid retained-child quotient;
- bounded cross-generation reuse;
- feasible Bellman reserve weights;
- a branching Carleson inequality;
- or the four-term Erdős conjecture.
