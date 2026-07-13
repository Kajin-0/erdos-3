# Simultaneous transition and overlap frontier through `S_7`

## Status

Exact fixed-policy computer-assisted extension of the raw simultaneous transition and pointwise multiplicity ledgers through `S_7`.

The computation required disabling Python's default 4,300-digit integer-to-string limit because exact harmonic numerators and denominators at these depths are substantially larger. No floating-point approximation is introduced.

**Verifier:** `src/verify_simultaneous_transition_s6_s7.py`.

**Certificate:** `data/simultaneous_transition_s6_s7_certificate_2026-07-13.txt`.

---

## 1. Exact transition growth

| parent | selected progressions | residual | terminal steps | raw recursive occurrences | exact state classes |
|---:|---:|---:|---:|---:|---:|
| `S_1` | 6 | 6 | 2 | 5 | 4 |
| `S_2` | 26 | 13 | 5 | 11 | 10 |
| `S_3` | 92 | 28 | 10 | 25 | 21 |
| `S_4` | 305 | 58 | 11 | 46 | 34 |
| `S_5` | 974 | 118 | 12 | 68 | 51 |
| `S_6` | 3,041 | 238 | 13 | 94 | 71 |
| `S_7` | 9,360 | 480 | 25 | 127 | 95 |

The lexicographic coordinated schedule remains computationally tractable through the first seven recorded states.

---

## 2. Exact overlap growth

| parent | exact duplicate classes | strict containments | partial overlaps |
|---:|---:|---:|---:|
| `S_1` | 1 | 1 | 0 |
| `S_2` | 1 | 3 | 5 |
| `S_3` | 3 | 23 | 15 |
| `S_4` | 7 | 91 | 35 |
| `S_5` | 11 | 145 | 88 |
| `S_6` | 15 | 209 | 150 |
| `S_7` | 20 | 345 | 214 |

Exact duplicate classes remain a minority of the overlap structure. The number of strict containments and partial overlaps grows substantially faster than the number of exact duplicate classes.

A retention quotient based only on numerical state equality cannot address the dominant relations.

---

## 3. Terminal-recursive overlap through `S_6`

For `S_1` through `S_6`, the overlap sets are

```text
S1: 1
S2: 1,61
S3: 1,61,303
S4: 1,61,303,1597
S5: 1,61,303,1597,8195
S6: 1,61,303,1597,8195,93476.
```

Thus through `S_6`, the overlap set is exactly the base step `1` plus all prior replication separations.

---

## 4. Pattern break at `S_7`

At `S_7`, terminal-recursive overlap becomes

```text
1,5,61,303,1597,8195,49158,93476,230164,323640.
```

The historical separations remain present:

```text
61,303,1597,8195,93476,230164.
```

But four additional labels occur:

```text
1,5,49158,323640.
```

The new nonhistorical labels show that a bounded-reuse state cannot be reduced to the latest separation or even the list of historical separations. The overlap state needs either:

1. a broader finite affine signature;
2. explicit provenance classes;
3. or a theorem exporting the extra labels into a controlled lower-scale object.

The exact computation does not yet determine which representation is sufficient.

---

## 5. Pointwise multiplicity spectra

At `S_6`,

```text
4781 labels have multiplicity 1
 397 labels have multiplicity 2
  54 labels have multiplicity 3
  27 labels have multiplicity 5
  27 labels have multiplicity 6
  18 labels have multiplicity 10
   6 labels have multiplicity 11
   2 labels have multiplicity 13.
```

Hence

```math
M(S_6)=13,
```

attained by

```text
93476,186952.
```

At `S_7`,

```text
14679 labels have multiplicity 1
 1105 labels have multiplicity 2
  184 labels have multiplicity 3
   81 labels have multiplicity 5
   81 labels have multiplicity 6
   54 labels have multiplicity 10
   17 labels have multiplicity 11
    5 labels have multiplicity 12
    3 labels have multiplicity 13
    1 label  has multiplicity 16.
```

Therefore

```math
M(S_7)=16,
```

attained by the incoming separation

```math
230164.
```

---

## 6. Harmonic-average multiplicity

Despite the growth

```text
M(S1),...,M(S7)=2,3,7,11,12,13,16,
```

the exact verifier proves

```math
\frac{\sum_iH(C_i)}{H(\bigcup_iC_i)}<\frac98
```

for both `S_6` and `S_7`.

Thus high multiplicity remains concentrated on relatively large labels. This controls local reciprocal-mass inflation but says nothing by itself about repeated use across generations.

---

## 7. Exact hashes

```text
S6 payload:
56d2074c478a5715a60ef77a8d21c59a12f981cbcd2c130758328e7d35bd020a

S6 multiplicity catalog:
58c007732844869a880b5763a800fce414ccf80e1f78b292311dc9360f4e4beb

S7 payload:
6f682a5a7be606c622cf4e660d7300f7f1ed76ed6d2835d1a111ef43a07b5678

S7 multiplicity catalog:
c66b8c38d6d44acce9071ac12c6e4069ace3897db8d1427e902651a8de8deae3
```

The compact certificate SHA-256 is

```text
4c1767a8c0b4e65b2deb4e576bfec6f8b74e6531f4ef12e4444fd53a9d0cb94c
```

---

## 8. Revised active state

The smallest plausible provenance state must now distinguish at least:

1. historical replication separations;
2. terminal-recursive labels outside that history;
3. exact numerical state classes;
4. origin multiplicities inside each class;
5. strict-containment and partial-overlap edges;
6. pointwise local multiplicity capacity.

A state containing only cardinality, scale, latest separation, and maximum overlap is already falsified by the `S_7` ledger as an adequate description of the observed overlap structure.

---

## 9. Scope

This result is a finite fixed-policy computation. It does not prove:

- that the harmonic-average bound `9/8` is uniform;
- that the historical-separation pattern persists on other branches;
- a finite complete provenance state;
- bounded cross-generation reuse;
- a retained-child quotient;
- a branching Bellman inequality;
- or the four-term Erdős conjecture.
