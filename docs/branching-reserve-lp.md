# Exact branching-reserve LP harness

## Status

Exact rational infrastructure for exporting and checking candidate whole-tree reserve inequalities.

The repository now distinguishes four objects that must not be conflated:

1. **replay siblings:** alternative outer separation choices;
2. **raw simultaneous occurrences:** all outputs generated together by one complete deletion schedule;
3. **retained Bellman children:** the family left after a proved retention and overlap rule;
4. **LP rows:** exact inequalities formed from the retained family.

Only the fourth object is accepted by `src/branching_reserve_lp.py`.

**LP implementation:** `src/branching_reserve_lp.py`.

**Raw transition exporter:** `src/export_simultaneous_deletion_transition.py`.

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

- `D(S)` is the positive Bellman debt;
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
    "radius_deficit": "4",
    "support_holes": "2"
  },
  "children": [
    {
      "multiplicity": 1,
      "features": {
        "radius_deficit": "1",
        "support_holes": "1"
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

Denominators are cleared exactly before CPLEX-LP output is written.

---

## 3. Replay siblings are not children

`src/export_replay_transition_catalog.py` enumerates alternative outer replication choices. Its semantic label is

```text
alternative_continuation_siblings_not_simultaneous_children
```

For example, `S_1` has four valid factor-four replay separations:

```text
61,68,69,71.
```

They are four alternative continuations. They may not be placed together in one `children` array without a theorem proving that they occur simultaneously in the deletion genealogy.

---

## 4. Raw simultaneous transition export

The first missing adapter layer is now implemented.

`src/export_simultaneous_deletion_transition.py` fixes the lexicographic coordinated policy and records the complete raw occurrence family produced by one parent resolution. The payload contains:

1. the selected progression history;
2. terminal steps and their sponsor provenance;
3. the terminal residual;
4. the minimum-translation backbone;
5. every middle multiplicity fiber;
6. every standard-dyadic shell occurrence;
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

The certified reference frontier is:

| parent | raw recursive occurrences | exact state classes | duplicate classes | strict containments | partial overlaps |
|---:|---:|---:|---:|---:|---:|
| `S_1` | 5 | 4 | 1 | 1 | 0 |
| `S_2` | 11 | 10 | 1 | 3 | 5 |
| `S_3` | 25 | 21 | 3 | 23 | 15 |

This completes raw simultaneous output generation for a fixed policy. It does not complete retained-child construction.

---

## 5. Why raw occurrences cannot be copied into an LP row

The raw family contains several accounting layers.

### Exact duplicates

Two occurrences can have identical numerical support but different provenance. A set-valued potential may wish to quotient them; a provenance-sensitive potential may not. The exporter records both the numerical class and every origin.

### Strict containment

One child state may be a strict subset of another simultaneous child. Counting both preserves occurrence genealogy but double-counts numerical support. Dropping the smaller state may discard independent future histories.

### Partial overlap

Two child states may intersect without either containing the other. Neither exact-state quotienting nor maximal-set retention resolves this case.

### Terminal-recursive overlap

A terminal step label may already occur in a recursive state. Terminal and recursive mass cannot automatically be added as distinct numerical support.

### Cross-generation reuse

Even a locally correct numerical union can be charged again by descendants. A local deduplication rule is not a whole-tree packing theorem.

Therefore the raw exporter reports

```text
bellman_row_status=blocked_until_retention_and_bounded_overlap_rule_is_supplied
```

and does not emit LP constraints directly.

---

## 6. Required retention contract

A valid conversion from a raw payload to an LP row must state:

1. the potential convention: occurrence-valued, state-valued, support-valued, or provenance-valued;
2. which exact duplicate classes are merged;
3. how duplicate multiplicities are retained or discarded;
4. how strict containments are charged;
5. how partial intersections are charged;
6. how terminal-recursive overlap is handled;
7. how imported labels are identified across parent transitions;
8. a bound preventing repeated payment by the same provenance class;
9. any discarded mass entered as controlled error;
10. proof that the emitted child list is complete under that convention.

Without this contract, an LP can be exactly solved and still represent the wrong mathematical inequality.

---

## 7. Schedule-dependent features

For a coordinated schedule `sigma`, define

```math
\mathcal N_\sigma(D)
=
H\left(
\left(\bigcup_q\Xi_q^\sigma\right)
\setminus\mathcal B(D)
\right).
```

The finite facts are:

```math
\mathcal N_\sigma(S_1)=0
```

for all `1,560` coordinated schedules;

```math
\mathcal N_{\rm lex}(S_2)
=
\frac{239396453}{200655312}>0;
```

but another valid `S_2` schedule has

```math
\mathcal N_{\sigma_0}(S_2)=0.
```

Thus raw novelty may enter an LP only when the deletion policy is part of the state or when a schedule-independent theorem is available.

---

## 8. Known feature no-go results

### Naive mass coordinates

The nonnegative span of

```text
weighted_density
right_shell_slack
incoming_contamination_mass
```

cannot pay the recorded factor-four transition `S_6 -> S_7`. Every parent-minus-child coefficient is negative while the debt is

```math
\frac{9841}{4096}>0.
```

### Forced-fork feature

The parent-intrinsic forced-fork reserve `Psi` satisfies a positive local novelty-or-overlap floor, but

```math
F(S)=P\Psi(S)
```

is not a standalone stored Bellman potential. On `S_1 -> S_2`,

```math
F(S_1)-F(S_2)<0
```

while the factor-four debt is positive.

These features may remain auxiliary terms, but neither family closes the branching inequality alone.

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

Export one raw simultaneous transition ledger:

```bash
python3 src/export_simultaneous_deletion_transition.py export \
  --state-depth 2 \
  --output /tmp/S2_transition.json
```

Run the complete lightweight suite:

```bash
bash src/run_verify_transport_reserve.sh
```

---

## 10. Active next input

The next meaningful LP dataset is not another raw transition catalog. It must be produced by a retention adapter implementing a proved bounded-reuse convention.

The preferred first experiment is:

1. use the exact-state classes from the `S_1` through `S_3` raw payloads;
2. retain all provenance edges;
3. introduce explicit overlap-capacity or label-reuse variables;
4. test candidate inequalities against the exact duplicate, containment, and partial-overlap graph;
5. emit the smallest exact state where the convention fails.

Target feature families include:

- target interval demand and rectangle-support deficit;
- affine-obstruction zero classes;
- completion-fiber deficit;
- forced-fork transition output;
- imported-label reuse capacity;
- dyadic slack as an auxiliary coordinate.

---

## 11. Scope

The LP harness and raw transition exporter establish exact bookkeeping. They do not establish:

- a valid retention quotient;
- bounded cross-generation reuse;
- feasible reserve weights;
- monotone rectangle growth;
- a branching Carleson inequality;
- or the four-term Erdős conjecture.

Their purpose is to ensure that future feasibility or infeasibility results reflect the stated genealogy and overlap convention rather than decimal error, incomplete child families, or ambiguous branching semantics.
