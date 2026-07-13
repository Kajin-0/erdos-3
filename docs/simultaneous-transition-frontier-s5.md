# Simultaneous transition and overlap frontier through `S_5`

## Status

Exact fixed-policy computer-assisted extension of the raw simultaneous transition and occurrence-multiplicity ledgers through `S_5`.

The core exporter retains `S_1` through `S_3` as its compact self-test. This extension certifies complete canonical payload hashes and overlap statistics for `S_4` and `S_5`.

**Verifier:** `src/verify_simultaneous_transition_s4_s5.py`.

**Certificate:** `data/simultaneous_transition_s4_s5_certificate_2026-07-13.txt`.

---

## 1. Exact transition growth

| parent | selected progressions | residual | terminal steps | raw recursive occurrences | exact state classes |
|---:|---:|---:|---:|---:|---:|
| `S_1` | 6 | 6 | 2 | 5 | 4 |
| `S_2` | 26 | 13 | 5 | 11 | 10 |
| `S_3` | 92 | 28 | 10 | 25 | 21 |
| `S_4` | 305 | 58 | 11 | 46 | 34 |
| `S_5` | 974 | 118 | 12 | 68 | 51 |

The payloads include the complete lexicographic coordinated schedule, all middle fibers, the backbone, every shell occurrence, and point-level provenance.

---

## 2. Exact overlap growth

| parent | exact duplicate classes | strict containments | partial overlaps |
|---:|---:|---:|---:|
| `S_1` | 1 | 1 | 0 |
| `S_2` | 1 | 3 | 5 |
| `S_3` | 3 | 23 | 15 |
| `S_4` | 7 | 91 | 35 |
| `S_5` | 11 | 145 | 88 |

The dominant unresolved relations are no longer exact duplicates. By `S_5`, exact-state quotienting would remove only part of the occurrence family, while `145` containment relations and `88` partial intersections would remain.

This rules out treating exact-state deduplication as the missing retention theorem.

---

## 3. Terminal-recursive overlap

The terminal step labels already occurring in recursive output are

```text
S1: 1
S2: 1,61
S3: 1,61,303
S4: 1,61,303,1597
S5: 1,61,303,1597,8195.
```

These are precisely the earlier recorded replication separations through the current depth, together with the base step `1`.

This is an exact observation on the recorded lexicographic states. It suggests that separation coordinates persist simultaneously as terminal and recursive objects, but no general persistence theorem is claimed.

---

## 4. Pointwise multiplicity spectra

For raw recursive occurrences `C_i`, define

```math
m(u)=|\{i:u\in C_i\}|.
```

The exact spectra at the two new depths are

```text
S4: 460 labels with m=1
     60 labels with m=2
      7 labels with m=3
      3 labels with m=5
      3 labels with m=6
      2 labels with m=11
```

and

```text
S5: 1482 labels with m=1
     167 labels with m=2
      18 labels with m=3
       9 labels with m=5
       9 labels with m=6
       6 labels with m=10
       2 labels with m=12.
```

Therefore

```math
M(S_4)=11,
\qquad
M(S_5)=12.
```

The maximum labels are

```text
S4: 1597,3194
S5: 8195,16390.
```

These are the incoming separation and twice the incoming separation.

---

## 5. Worst-case versus harmonic-average multiplicity

The local identity

```math
\sum_iH(C_i)=\sum_u\frac{m(u)}u
```

gives

```math
\sum_iH(C_i)
\le
M\,H\left(\bigcup_iC_i\right).
```

The exact verifier also proves

```math
\frac{\sum_iH(C_i)}{H(\bigcup_iC_i)}
<
\frac98
```

for both `S_4` and `S_5`.

Thus the two multiplicity scales diverge:

```text
maximum multiplicity through S5: 2,3,7,11,12
harmonic-average upper bounds:   8/5,11/10,11/10,9/8,9/8.
```

The large multiplicities concentrate on large inherited separation labels and contribute less reciprocal mass locally. This does not control how often their provenance is reused in later generations.

---

## 6. Payload and catalog hashes

```text
S4 payload:
023330cc1babb1f10d8956f5b966a98f38d0b6f6dc062bdf1ee00c7b47976c03

S4 multiplicity catalog:
dd0029d181a8195b03fe7db7c69f4ce7c19c85f3af3a3589103e3a1091e2c0a1

S5 payload:
028cc066383a969cbec7b9ec285aec208c99e6c7f8fa233555067eb241e0f03b

S5 multiplicity catalog:
0cba557321d68c27d86221b45943150941b1c8108b650c916d7a773ca8ed754b
```

The compact certificate SHA-256 is

```text
ada237c35a0980c15cecac51e30fd43ade50948067d6f421477af1bb79239756
```

---

## 7. Revised retention target

The data support the following separation of tasks:

### Local support packing

For each parent, numerical union mass controls raw occurrence mass with a finite local harmonic-average factor.

### Cross-generation provenance packing

The difficult part is to show that inherited separation labels and their descendants cannot be used repeatedly without either:

1. consuming a finite provenance capacity;
2. exporting a smaller difference label;
3. increasing affine obstruction coverage;
4. or eliminating a future cheap extension.

A retention theorem based only on exact-state classes or maximum local multiplicity is not adequate.

---

## 8. Scope

This extension proves exact fixed-policy finite statements through `S_5`. It does not prove:

- the observed separation-label pattern for arbitrary states;
- a uniform harmonic-average bound;
- bounded cross-generation provenance reuse;
- a valid retained-child quotient;
- a branching Bellman inequality;
- or the four-term Erdős conjecture.
