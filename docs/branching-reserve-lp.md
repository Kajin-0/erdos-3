# Exact branching-reserve LP harness

## Status

Exact rational infrastructure for exporting and checking candidate whole-tree reserve inequalities.

The repository distinguishes four objects:

1. **replay siblings:** alternative outer separation choices;
2. **raw simultaneous occurrences:** all outputs generated together by one complete deletion schedule;
3. **retained Bellman children:** the family left after a proved retention and packing rule;
4. **LP rows:** exact inequalities formed from the retained family.

Only the fourth object is accepted by `src/branching_reserve_lp.py`.

**LP implementation:** `src/branching_reserve_lp.py`.

**Raw transition exporter:** `src/export_simultaneous_deletion_transition.py`.

**Terminal-fiber SCC exporter:** `src/export_terminal_fiber_scc_quotient.py`.

---

## 1. Target inequality

For a parent state `S`, the intended inequality is

```math
D(S)
+
\sum_{S'\in\operatorname{Child}(S)}
\Phi(S')
\le
\Phi(S)+E(S),
```

where:

- `D(S)` is positive Bellman debt;
- `E(S)` is a separately justified controlled error;
- `Child(S)` is the complete **retained** simultaneous child family;
- `Phi` is a nonnegative reserve.

For a linear feature model,

```math
\Phi(S)=\sum_f w_fF_f(S),
\qquad
w_f\ge0.
```

One row therefore means

```math
\sum_f
\left(
F_f(S)-
\sum_{S'}m(S')F_f(S')
\right)w_f
\ge
D(S)-E(S).
```

All values are stored as exact rational numbers.

---

## 2. JSONL row format

Each non-comment line is one complete retained transition:

```json
{
  "name": "transition-name",
  "debt": "3/2",
  "error": "0",
  "parent": {
    "rectangle_deficit": "4",
    "reuse_capacity": "2"
  },
  "children": [
    {
      "multiplicity": 1,
      "features": {
        "rectangle_deficit": "1",
        "reuse_capacity": "1"
      }
    }
  ]
}
```

Numbers may be integers or rational strings such as `"17/32"`. Floating-point values and booleans are rejected.

The parser forms

```math
A_f=F_f(S)-\sum_{S'}m(S')F_f(S')
```

and exports

```math
\sum_fA_fw_f\ge D-E.
```

Denominators are cleared exactly before CPLEX-LP output.

---

## 3. Replay siblings are not children

`src/export_replay_transition_catalog.py` enumerates alternative outer replication choices. Its semantic label is

```text
alternative_continuation_siblings_not_simultaneous_children
```

For example, `S_1` has four valid factor-four replay separations, while `S_2` has `203` valid factor-eight replay separations. These alternatives may not be placed together in one `children` array without a theorem proving simultaneous retention.

---

## 4. Raw simultaneous transition export

`src/export_simultaneous_deletion_transition.py` records the complete raw occurrence family produced by one fixed lexicographic coordinated schedule. The payload contains:

1. the selected progression history;
2. terminal steps and sponsor provenance;
3. the terminal residual;
4. the minimum-translation backbone;
5. every middle multiplicity fiber;
6. every dyadic shell occurrence;
7. point-level provenance;
8. exact duplicate state classes;
9. strict containments;
10. partial overlaps;
11. terminal-recursive overlaps;
12. exact occurrence and union mass ledgers.

Its semantic label is

```text
one_complete_schedule_specific_simultaneous_output_family_before_retention_quotient
```

The certified frontier is:

| parent | occurrences | state classes | duplicate classes | containments | partial overlaps |
|---:|---:|---:|---:|---:|---:|
| `S_1` | 5 | 4 | 1 | 1 | 0 |
| `S_2` | 11 | 10 | 1 | 3 | 5 |
| `S_3` | 25 | 21 | 3 | 23 | 15 |
| `S_4` | 46 | 34 | 7 | 91 | 35 |
| `S_5` | 68 | 51 | 11 | 145 | 88 |
| `S_6` | 94 | 71 | 15 | 209 | 150 |
| `S_7` | 127 | 95 | 20 | 345 | 214 |

This completes raw fixed-policy output generation through `S_7`. It does not complete retained-child construction.

---

## 5. Why raw occurrences cannot be copied into an LP row

### Exact duplicates

Two occurrences can have identical numerical support but different provenance. A set-valued potential may quotient them; a provenance-sensitive potential may not.

### Strict containment

One child state may be a strict subset of another simultaneous child. Counting both double-counts support; dropping the smaller may discard an independent future history.

### Partial overlap

Two states may intersect without containment. Neither exact-state quotienting nor maximal-set retention resolves this case.

### Terminal-recursive overlap

A terminal step label may already occur recursively. Terminal and recursive mass cannot automatically be added as distinct support.

### Cross-generation reuse

Even a locally deduplicated numerical union can be charged again by descendants.

Therefore raw payloads report

```text
bellman_row_status=blocked_until_retention_and_bounded_overlap_rule_is_supplied
```

and do not emit LP rows directly.

---

## 6. Terminal-fiber graph and SCC boundary

For terminal step set `Q`, draw an edge

```math
q\longrightarrow u
```

when

```math
u\in Q\cap\Xi_q.
```

This graph is already cyclic at `S_3` through

```math
61\longleftrightarrow303.
```

At `S_7`, its cyclic component is

```math
\{1,5,61,303,1597,8195,323640\}.
```

Thus a feature based on a strict decreasing rank of terminal labels is invalid.

Collapsing strongly connected components produces an acyclic condensation graph, but internal recycling remains. For a component `C`, define

```math
V(C)=\sum_{u\in C}\frac1u
```

and

```math
T(C)=\sum_{(q,u)\text{ internal edge}}\frac1u.
```

For `C={61,303}` through `S_6`, `T(C)=V(C)`. At `S_7`,

```math
T(C)-V(C)
=
\frac{43727503229099}{1043823972523464}>0.
```

Therefore a raw SCC feature containing only harmonic vertex mass cannot be used as a retained capacity variable.

---

## 7. Required retention contract

A valid conversion from a raw payload to an LP row must state:

1. the potential convention: occurrence-valued, state-valued, support-valued, provenance-valued, or component-valued;
2. which exact duplicate classes merge;
3. how duplicate multiplicities are retained or discarded;
4. how strict containments are charged;
5. how partial intersections are charged;
6. how terminal-recursive overlap is handled;
7. how strongly connected components are represented;
8. how internal component recycling is funded;
9. how imported labels are identified across parent transitions;
10. a bound preventing repeated payment by the same provenance class;
11. any discarded mass entered as controlled error;
12. proof that the emitted child list is complete under that convention.

Without this contract, an exactly solved LP can still represent the wrong mathematical inequality.

---

## 8. Known feature no-go results

### Naive mass coordinates

The nonnegative span of

```text
weighted_density
right_shell_slack
incoming_contamination_mass
```

cannot pay the recorded factor-four transition `S_6 -> S_7`. Every parent-minus-child coefficient is negative while debt is

```math
\frac{9841}{4096}>0.
```

### Raw novelty

Novel fiber mass is schedule dependent on `S_2`; its minimum over coordinated schedules is zero.

### Forced-fork feature

The parent-intrinsic forced-fork reserve is positive, but

```math
F(S)=P\Psi(S)
```

is not a standalone stored Bellman potential.

### Label rank

The terminal-fiber graph is cyclic from `S_3`, so no strict decreasing label rank can orient every recursive incidence.

### Historical-separation state

At `S_7`, terminal-recursive overlap contains `5,49158,323640` in addition to historical separations. Tracking only separation history is inadequate.

### Unit harmonic SCC capacity

At `S_7`, internal target mass exceeds harmonic vertex mass by

```math
\frac{43727503229099}{1043823972523464}.
```

A component needs internal capacity or obstruction export.

---

## 9. Commands

Export a feasibility LP:

```bash
python3 src/branching_reserve_lp.py export \
  constraints.jsonl reserve.lp
```

Verify nonnegative weights exactly:

```bash
python3 src/branching_reserve_lp.py verify \
  constraints.jsonl weights.json
```

Export one raw simultaneous transition:

```bash
python3 src/export_simultaneous_deletion_transition.py export \
  --state-depth 7 \
  --output /tmp/S7_transition.json
```

Export its SCC quotient:

```bash
python3 src/export_terminal_fiber_scc_quotient.py export \
  --state-depth 7 \
  --output /tmp/S7_scc.json
```

Run the complete lightweight suite:

```bash
bash src/run_verify_transport_reserve.sh
```

---

## 10. Active next LP input

The next meaningful dataset must be produced by a retention adapter with explicit cyclic-component capacity.

The preferred experiment is:

1. merge exact numerical state classes while retaining every provenance edge;
2. represent each terminal-fiber SCC with internal edge counts and capacities;
3. introduce incoming, internal, outgoing, and obstruction-export features;
4. preserve containment and partial-overlap relations as capacity constraints;
5. test candidate inequalities against `S_1` through `S_7`;
6. emit the smallest exact transition where the convention fails.

Candidate features include:

- SCC internal recycling deficit;
- outgoing condensation capacity;
- imported-label reuse capacity;
- target interval demand and rectangle deficit;
- affine-obstruction zero classes;
- completion-fiber deficit;
- forced-fork transition output;
- dyadic slack as an auxiliary coordinate.

---

## 11. Scope

The LP harness, raw transition exporter, and SCC exporter establish exact bookkeeping. They do not establish:

- a valid retention quotient;
- sufficient internal component capacity;
- bounded cross-generation reuse;
- feasible reserve weights;
- a branching Carleson inequality;
- or the four-term Erdős conjecture.

Their purpose is to ensure that future feasibility results reflect the stated genealogy, overlap, and cyclic-capacity convention rather than decimal error or incomplete child families.
