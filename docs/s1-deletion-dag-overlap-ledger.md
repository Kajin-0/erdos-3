# Exact `S_1` deletion-DAG overlap ledger

## Status

Exact finite, schedule-specific deletion-DAG certificate.

This note resolves one complete side-anchor deletion process on the recorded
base state `S_1`, computes every simultaneous hybrid output, resolves each
recursive output into standard dyadic shells, and records exact duplicates and
strict containments.

The computation is not a claim that the chosen schedule is canonical,
extremal, or representative of every parent. Its purpose is to establish the
first exact adapter between the abstract one-generation deletion theorem and
the all-child reserve data format.

**Verifier:** `src/verify_s1_deletion_dag_adapter.py`.

**Certificate:**
`data/s1_deletion_dag_adapter_certificate_2026-07-13.json`.

---

## 1. Parent state

The recorded base state is

```math
S_1=
\{64,65,66,80,81,82,85,86,87,90,91,92\}
\subseteq[64,128).
```

It has cardinality

```math
|S_1|=12
```

and contains no nontrivial four-term arithmetic progression.

---

## 2. Deterministic coordinated schedule

At each deletion time, enumerate all three-term progressions in the current
set and choose the lexicographically smallest tuple

```text
(step, left endpoint, middle, right endpoint).
```

For a selected step `q`, delete:

- the left endpoint when `v_2(q)` is even;
- the right endpoint when `v_2(q)` is odd.

For `S_1`, every selected step has even two-adic valuation, so all six sponsors
are left endpoints. The exact schedule is

| time | sponsor | middle | opposite | step |
|---:|---:|---:|---:|---:|
| 1 | 64 | 65 | 66 | 1 |
| 2 | 80 | 81 | 82 | 1 |
| 3 | 85 | 86 | 87 | 1 |
| 4 | 90 | 91 | 92 | 1 |
| 5 | 81 | 86 | 91 | 5 |
| 6 | 82 | 87 | 92 | 5 |

Every directed edge from a sponsor to its middle and opposite endpoint
increases deletion time. Hence the selected forks form an acyclic deletion
DAG.

The terminal residual is

```math
\{65,66,86,87,91,92\},
```

which is three-term-progression-free.

Thus

```math
K=6,
\qquad
s=6.
```

---

## 3. Exact middle multiplicity resolution

The distinct selected steps are

```math
Q=\{1,5\}.
```

### Step `1`

The centers are

```math
X_1=\{65,81,86,91\}.
```

After retaining the minimum center as the terminal representative, the
center-difference child is

```math
\Xi_1
=
\{81-65,86-65,91-65\}
=
\boxed{\{16,21,26\}}.
```

### Step `5`

The centers are

```math
X_5=\{86,87\}.
```

Hence

```math
\Xi_5
=
\{87-86\}
=
\boxed{\{1\}}.
```

The exact multiplicity identity is visible numerically:

```math
|Q|+|\Xi_1|+|\Xi_5|
=2+3+1
=6
=K.
```

The terminal representatives have sponsor provenance

```text
step 1 -> sponsor 64;
step 5 -> sponsor 81.
```

The recursive middle-fiber labels have provenance

```text
16 -> sponsor 80;
21 -> sponsor 85;
26 -> sponsor 90;
1  -> sponsor 82.
```

---

## 4. Minimum-translation backbone

With

```math
m=\min S_1=64,
```

the simultaneous backbone child is

```math
\mathcal B(S_1)
=
\{d-64:d\in S_1,\ d>64\}
```

and therefore

```math
\mathcal B(S_1)
=
\boxed{
\{1,2,16,17,18,21,22,23,26,27,28\}.
}
```

After standard dyadic resolution, the backbone gives three occurrences:

```math
\{1\}\subseteq[1,2),
```

```math
\{2\}\subseteq[2,4),
```

and

```math
\{16,17,18,21,22,23,26,27,28\}
\subseteq[16,32).
```

The two middle fibers each lie in one standard shell. Thus the complete
recursive occurrence family has five shell occurrences:

| index | source | shell | values |
|---:|---|---|---|
| 0 | backbone | `[1,2)` | `{1}` |
| 1 | backbone | `[2,4)` | `{2}` |
| 2 | backbone | `[16,32)` | `{16,17,18,21,22,23,26,27,28}` |
| 3 | `Xi_1` | `[16,32)` | `{16,21,26}` |
| 4 | `Xi_5` | `[1,2)` | `{1}` |

These are simultaneous recursive occurrences produced by one parent
resolution. Unlike the replay-separation catalogs, they may legitimately be
listed together before overlap processing.

---

## 5. Exact overlap structure

The family has one exact duplicate class:

```math
\boxed{
\text{occurrence }0
=
\text{occurrence }4
=
\{1\}.
}
```

It also has one strict containment:

```math
\boxed{
\Xi_1
=
\{16,21,26\}
\subsetneq
\{16,17,18,21,22,23,26,27,28\}.
}
```

More strongly,

```math
\boxed{
\Xi_1\cup\Xi_5
\subseteq
\mathcal B(S_1).
}
```

Therefore every recursive middle-fiber label is already present in the
backbone. At this parent, the middle-fiber recursion adds occurrence mass but
adds no new recursive numerical label.

This is precisely the distinction that a whole-tree reserve must encode:

```text
simultaneous occurrence mass != simultaneous distinct-label mass.
```

---

## 6. Exact harmonic ledger

The terminal occurrence mass is

```math
H(Q)
=
1+\frac15
=
\boxed{\frac65}.
```

The recursive occurrence mass, counting all five shell occurrences, is

```math
H(\mathcal B(S_1))+H(\Xi_1)+H(\Xi_5)
=
\boxed{\frac{259811791}{84540456}}.
```

Since both middle fibers are contained in the backbone, the recursive distinct
union is just the backbone itself:

```math
H\left(
\mathcal B(S_1)\cup\Xi_1\cup\Xi_5
\right)
=
H(\mathcal B(S_1))
=
\boxed{\frac{46488647}{24154416}}.
```

The recursive duplicate mass is therefore

```math
\boxed{
\frac{259811791}{84540456}
-
\frac{46488647}{24154416}
=
\frac{5017}{4368}.
}
```

If terminal labels and recursive labels are all counted as occurrences, the
total output mass is

```math
\boxed{
\frac{1806301691}{422702280}}.
```

The harmonic mass of the distinct numerical label union is only

```math
\boxed{
\frac{256597651}{120772080}}.
```

Thus the total duplicate mass is

```math
\boxed{
\frac{9385}{4368}.
}
```

The additional unit beyond the recursive duplicate mass comes from terminal
step `1`, which is already present as a recursive label.

---

## 7. Consequence for a Bellman adapter

The computation now distinguishes three data layers:

1. **complete simultaneous occurrences:** five recursive shell occurrences and
   two terminal step representatives;
2. **exact-equivalence quotient:** occurrences `0` and `4` form one exact
   duplicate class;
3. **containment packing:** occurrence `3` is strictly contained in occurrence
   `2`.

A valid all-child Bellman row must specify which layer its potential uses.

### Occurrence convention

Counting all five recursive occurrences preserves the binary genealogy and the
one-generation lower bound, but it counts duplicate numerical labels.

### Exact-state quotient

Merging the two `{1}` occurrences removes exact duplication but does not remove
the strict containment of `Xi_1` in the large backbone shell.

### Distinct-label union

Replacing the family by its numerical union removes both forms of overlap, but
it destroys the per-parent occurrence accounting that produced the branching
constant.

No one of these conventions can be substituted for another without an explicit
packing theorem. Consequently the certificate intentionally reports

```text
bellman_row_status=blocked_pending_overlap_and_retention_convention
```

rather than emitting a mathematically unjustified LP row.

---

## 8. Structural interpretation

The base aligned diamond is not merely an example with repeated labels. It
shows that the strongest within-node multiplicity resolution and the
minimum-translation backbone can be maximally aligned:

```math
\text{all recursive middle fibers}
\subseteq
\text{one simultaneous backbone child}.
```

Raw contamination count, weighted density, and shell slack do not detect this
alignment. A useful reserve coordinate must distinguish at least:

1. new obstruction support outside the backbone;
2. middle-fiber support already imported by the backbone;
3. exact duplicate shell states;
4. strict containment inside larger child states;
5. terminal labels already present recursively.

A natural next coordinate is the **novel fiber mass**

```math
\mathcal N(D)
=
H\left(
\left(\bigcup_q\Xi_q\right)
\setminus
\mathcal B(D)
\right).
```

For this certified `S_1` resolution,

```math
\boxed{\mathcal N(S_1)=0.}
```

This coordinate is more faithful than raw fiber mass, but it is not yet known
to satisfy a useful transition inequality. The next computation should test it
across every deletion schedule of `S_1`, then on the smallest descendants for
which the schedule space remains exhaustible.

---

## 9. Reproduction

Run

```bash
python3 src/verify_s1_deletion_dag_adapter.py \
  /tmp/s1_deletion_dag_adapter.json
```

The exact certificate has SHA-256

```text
e31c232158b2abed03ebf7ec12e60d44ef14cff9ae7e066afaa645c80dd9b639
```

and is included in the lightweight proof-check workflow.

---

## 10. Scope

This certificate does not prove:

- schedule independence;
- an optimal deletion schedule;
- a valid global deduplication rule;
- a monotone novel-fiber reserve;
- a branching Carleson inequality;
- or the four-term Erdős conjecture.

It provides the first exact, fully simultaneous child ledger required to state
those questions without confusing alternative continuation choices, occurrence
multiplicity, exact duplicates, and set containment.
