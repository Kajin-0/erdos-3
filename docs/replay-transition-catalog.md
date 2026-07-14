# Exact replay-transition sibling catalog

## Status

Exact finite computation inside the restricted standard-dyadic, disjoint
three-translate replay model.

This note introduces a canonical reconstruction of the recorded states and a
chunkable exporter for all valid separation parameters in a prescribed finite
range. The exporter is intended to populate finite-state and reserve
experiments without silently replacing the continuation graph by one selected
path.

It does **not** identify the simultaneous children of the deletion DAG. The
valid separation parameters listed for one parent are alternative continuation
siblings. A separate retention and packing theorem is required before any of
them may be summed in one branching Bellman inequality.

**Canonical state module:** `src/certified_contaminated_states.py`.

**Catalog exporter:** `src/export_replay_transition_catalog.py`.

**Certificate:**
`data/replay_transition_catalog_certificate_2026-07-13.txt`.

---

## 1. Restricted continuation model

Let

```math
S\subseteq[L,2L)
```

be one recorded state, and put

```math
A=\{0\}\cup S.
```

For a positive integer separation `R`, form

```math
G_R(S)
=
A\cup(A+R)\cup(A+2R).
```

For a requested dyadic factor `c`, the next scale is

```math
L'=cL.
```

The exporter accepts `R` exactly when all of the following hold:

1. `v_2(R)` is even, so the coordinated sponsor is the left endpoint;
2. the three translate layers are disjoint;
3. `G_R(S)` fits below `L'`;
4. `G_R(S)` contains no nontrivial four-term arithmetic progression;
5. the backbone shell

   ```math
   G_R(S)\cap[L,2L)
   ```

   contains the replay state `S`.

The fifth condition is the finite contaminated-backbone persistence condition.
If it holds, the deletion schedule inside `S` can be replayed in the backbone
subset while the middle multiplicity fiber remains exactly `S`.

The fit range is finite:

```math
1\le R\le
\left\lfloor
\frac{cL-1-\max S}{2}
\right\rfloor.
```

Thus every catalog generated over the complete fit range is exact and finite
inside this model.

---

## 2. Canonical recorded states

The new shared module reconstructs the full recorded path

```math
S_1,S_2,\ldots,S_{10}
```

from one constant table:

```text
scales:
64,
256,
2048,
8192,
32768,
262144,
1048576,
8388608,
67108864,
536870912
```

```text
separations:
61,
303,
1597,
8195,
93476,
230164,
2097164,
16777217,
134217729
```

The resulting scale word is

```math
4,8,4,4,8,4,8,8,8.
```

The module independently checks the recorded sizes

```text
12, 39, 120, 363, 1092,
3279, 9840, 29523, 88572, 265719
```

and maxima

```text
92,
470,
3124,
14510,
63668,
512764,
2021668,
14604604,
115267902,
920574272.
```

It also recomputes the incoming backbone-contamination counts

```text
0, 4, 1, 33, 1, 0, 2, 0, 0, 0.
```

This removes repeated reconstruction constants from future finite-state tools.
It does not replace the dedicated heavy verifiers for progression-freeness or
complete large-depth exclusion.

---

## 3. Exact base-state sibling set

For `S_1`, the complete factor-two fit range contains no valid continuation:

```math
\boxed{N_{1,2}=0.}
```

The complete factor-four fit range has exactly four valid siblings:

```math
\boxed{
R\in\{61,68,69,71\}.
}
```

Their backbone-contamination counts are respectively

```text
4, 1, 1, 1.
```

The previously recorded path selects `R=61`, but the local continuation graph
already branches at the base state. Any transfer operator or finite-state
quotient that stores only the selected separation loses three valid siblings at
the first cheap step.

The canonical JSONL catalog for this sibling set has SHA-256

```text
ca97331f99bfb3391a985a8d3ec2b5a52cd22c5ccf3e68b401ef551463069897
```

under the exporter's sorted-key serialization.

---

## 4. Exact depth-two sibling counts

For `S_2`, the complete cheap ranges satisfy

```math
\boxed{N_{2,2}=N_{2,4}=0.}
```

The factor-eight range contains exactly

```math
\boxed{203}
```

valid replay siblings. The first valid separation is

```math
R=303,
```

and the last is

```math
R=788.
```

This is an early finite example of the phenomenon later seen at `S_10`: an
expensive recovery scale can support a broad fan of exact continuations. The
siblings need not have identical fit slack or contamination coordinates even
when their cardinality and multiplicity-weighted density agree.

---

## 5. Exported state coordinates

For each valid separation, the exporter records:

1. separation `R`;
2. requested factor `c`;
3. next scale `cL`;
4. generated cardinality;
5. generated maximum;
6. integer fit slack;
7. backbone-contamination count;
8. exact rational weighted density;
9. exact rational right-shell slack;
10. exact rational incoming-contamination mass.

For a child with persistence `P'=2P`, these last three coordinates are

```math
W'
=
P'\frac{|G_R(S)|}{cL},
```

```math
Q'
=
P'\frac{cL-1-\max G_R(S)}{cL},
```

and

```math
C'
=
P'\frac{\kappa_R}{cL},
```

where `kappa_R` is the number of contaminating backbone points.

These are diagnostic coordinates. The no-go theorem in
`docs/naive-reserve-coordinate-no-go.md` proves that their nonnegative linear
span is insufficient for the required Bellman reserve.

---

## 6. Why siblings are not yet branching children

A continuation catalog answers:

```text
Which separation choices produce valid replay states from this parent?
```

The branching Bellman inequality asks a different question:

```text
Which retained descendant states occur simultaneously in one deletion-DAG
resolution, with what multiplicities and overlap identifications?
```

The four valid factor-four separations from `S_1` are four alternative choices
of an outer replication parameter. They are not, merely by being valid, four
disjoint children that should all appear in

```math
\sum_{S'\in\mathrm{Child}(S)}\Phi(S').
```

Summing the entire separation catalog as one child family would therefore be
an unjustified strengthening of the tree and can manufacture false
infeasibility.

The missing adapter must specify:

1. a canonical deletion-DAG parent object;
2. which replay states are retained simultaneously;
3. multiplicities after genealogy merges;
4. overlap and imported-prefix identifications;
5. the map from the retained family to the LP row format.

This distinction is now enforced in the JSONL header by the semantic label

```text
alternative_continuation_siblings_not_simultaneous_children
```

so downstream tools cannot reasonably interpret the file as a completed
branching constraint without explicitly overriding its meaning.

---

## 7. Usage

Run the exact self-test and reproduce the recorded certificate:

```bash
python3 src/export_replay_transition_catalog.py self-test \
  /tmp/replay_transition_catalog_certificate.txt
```

Export a complete small-state catalog:

```bash
python3 src/export_replay_transition_catalog.py export \
  --state-depth 1 \
  --factor 4 \
  --output /tmp/S1_factor4.jsonl
```

Chunk a larger finite range:

```bash
python3 src/export_replay_transition_catalog.py export \
  --state-depth 3 \
  --factor 4 \
  --start-r 1500 \
  --end-r 2000 \
  --output /tmp/S3_factor4_chunk.jsonl
```

The current Python progression test is exact but quadratic in the generated
state size per candidate. Large-depth exhaustive work should continue to use
the repository's specialized C++ filters and exact certificates. The exporter
is presently the canonical small-state and chunked reference implementation,
not a replacement for the large `S_9` or `S_10` closure programs.

---

## 8. Consequence for the proof program

The finite-state program now has two distinct layers:

1. **continuation catalog:** enumerate all alternative replay siblings inside a
   precisely stated restricted model;
2. **tree adapter:** determine complete simultaneous retained-child families
   and their overlap multiplicities.

Only the second layer may emit the all-child rows needed by the branching
reserve LP.

The immediate next target is therefore not another selected continuation. It
is an exact small-state deletion-DAG adapter that maps one parent resolution to
a complete retained-child aggregate, while referencing this sibling catalog
for replay-state geometry.
