# Exact branching-reserve LP harness

## Status

Exact rational infrastructure for exporting and checking candidate linear reserve
inequalities. This file defines the input contract and the distinction between
continuation siblings, simultaneous deletion-DAG children, and schedule-dependent
features.

**Implementation:** `src/branching_reserve_lp.py`.

The harness does not prove that any selected feature family is sufficient. It
only preserves exact arithmetic and makes proposed inequalities mechanically
checkable.

---

## 1. Target inequality

For a state `S`, the intended branching inequality has the form

```math
D(S)
+
\sum_{S'\in\operatorname{Child}(S)}\Phi(S')
\le
\Phi(S)+E(S),
```

where:

- `D(S)` is the Bellman debt to be repaid;
- `E(S)` is a separately justified controlled error;
- `Phi` is a nonnegative reserve;
- `Child(S)` is the complete retained-child family from one deletion-DAG
  resolution, including exact multiplicities after merges.

For a linear feature model,

```math
\Phi(S)
=
\sum_f w_f F_f(S),
\qquad
w_f\ge0.
```

Each input row therefore represents

```math
\sum_f
\left(
F_f(S)
-
\sum_{S'}m(S')F_f(S')
\right)w_f
\ge
D(S)-E(S).
```

All coefficients are stored as exact rational numbers.

---

## 2. JSONL row format

Each non-comment line is one JSON object:

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

Numeric values may be integers or rational strings such as `"17/32"`.
Booleans and floating-point values are rejected.

The parser converts every value to `fractions.Fraction` before forming the
constraint.

---

## 3. Critical semantic requirement

A row may aggregate only states that are retained **simultaneously** from one
parent resolution.

The exact replay catalogs produced by
`src/export_replay_transition_catalog.py` enumerate alternative separation
choices. Their records carry the semantic label

```text
alternative_continuation_siblings_not_simultaneous_children
```

and must not be copied wholesale into one `children` array.

For example, `S_1` has four valid factor-four replay siblings with separations

```text
61, 68, 69, 71.
```

This does not assert that a deletion-DAG parent has four disjoint retained
children with those states. Treating the four alternatives as a simultaneous
sum would strengthen the branching load without proof and can create a false
LP obstruction.

Before a continuation catalog can be converted into branching rows, an adapter
must certify:

1. the parent deletion-DAG object;
2. the complete retained family for that resolution;
3. multiplicities after genealogy merges;
4. overlap and imported-prefix identifications;
5. any controlled error assigned to discarded or unresolved mass.

The repository now contains the first exact finite adapter for one coordinated
resolution of `S_1`, plus an exhaustive analysis of all coordinated schedules
on `S_1`. These are reference objects, not yet a general transition generator.

---

## 4. Exact constraint construction

For every feature, the parser forms

```math
A_f
=
F_f(S)
-
\sum_{S'}m(S')F_f(S').
```

The row becomes

```math
\sum_f A_fw_f
\ge
D(S)-E(S).
```

Zero coefficients are removed. Negative multiplicities are rejected.

The LP exporter computes the least common multiple of all denominators in one
row and multiplies the complete inequality by that positive integer. The
resulting CPLEX-LP file therefore has integer row coefficients and an integer
right-hand side without decimal approximation.

---

## 5. Commands

Export a feasibility LP:

```bash
python3 src/branching_reserve_lp.py export \
  constraints.jsonl \
  reserve.lp
```

Verify proposed nonnegative weights exactly:

```bash
python3 src/branching_reserve_lp.py verify \
  constraints.jsonl \
  weights.json
```

Run the built-in parser, export, and exact-slack self-test:

```bash
python3 src/branching_reserve_lp.py self-test
```

Run all lightweight reserve checks:

```bash
bash src/run_verify_transport_reserve.sh
```

---

## 6. Weight file

A weight file is a JSON object:

```json
{
  "radius_deficit": "5/4",
  "support_holes": 3
}
```

Every supplied weight must be nonnegative. Features omitted from the file are
treated as weight zero during verification.

The verifier reports each exact slack

```math
\operatorname{slack}
=
\sum_f A_fw_f-(D-E).
```

A weight vector passes only when every slack is nonnegative.

---

## 7. Known mass-coordinate obstruction

The exact theorem in `docs/naive-reserve-coordinate-no-go.md` proves that the
nonnegative feature family

```text
weighted_density
right_shell_slack
incoming_contamination_mass
```

cannot pay even the single recorded factor-four transition `S_6 -> S_7`.
The parent-minus-child coefficient of every feature is negative, while the debt
is

```math
\frac{9841}{4096}>0.
```

This one-row sign certificate should be checked before any broader LP search.
The result does not prohibit these coordinates as auxiliary terms, but at least
one obstruction-aware feature is necessary.

---

## 8. Schedule-dependent novelty obstruction

For a coordinated deletion schedule `sigma`, define the novel middle-fiber mass

```math
\mathcal N_{\sigma}(D)
=
H\left(
\left(\bigcup_q\Xi_q^{\sigma}\right)
\setminus
\mathcal B(D)
\right).
```

The finite data now show three distinct behaviors.

### `S_1`: schedule-independent zero

All `1,560` progression-labeled coordinated schedules satisfy

```math
\bigcup_q\Xi_q^{\sigma}
\subseteq
\mathcal B(S_1),
```

so

```math
\mathcal N_{\sigma}(S_1)=0
```

for every schedule.

### `S_2`: positive reference schedule

The deterministic lexicographic schedule has

```math
\mathcal N_{\mathrm{lex}}(S_2)
=
\frac{239396453}{200655312}>0.
```

### `S_2`: exact zero schedule

The explicit witness in `docs/s2-zero-novelty-schedule.md` has

```math
\mathcal N_{\sigma_0}(S_2)=0.
```

Because novel mass is nonnegative,

```math
\boxed{
\min_{\sigma}\mathcal N_{\sigma}(S_2)=0.
}
```

Therefore `novel_fiber_mass` is not a parent-only state feature unless the row
also fixes and certifies the deletion policy. The schedule-robust lower envelope
cannot pay positive debt at `S_2`.

A future dataset may include schedule-dependent coordinates only when it also
records:

1. a canonical or optimized schedule identifier;
2. the complete progression-labeled deletion history or a certified compressed
   representation;
3. proof that the same policy is compatible with every child transition used in
   the Bellman tree;
4. exact imported, duplicate, and novel support after overlap resolution.

The LP harness deliberately does not infer those semantics from a bare feature
name.

---

## 9. Intended next inputs

The first meaningful branching dataset should contain exact small-state rows
with features such as:

1. uncovered cheap-separation capacity;
2. direct rectangle-support radius;
3. target interval demand;
4. support-hole or zero-class counts from the 34 affine obstruction classes;
5. completion-fiber deficit;
6. imported-prefix mass with overlap multiplicities;
7. dyadic slack as an auxiliary coordinate;
8. schedule-dependent fiber coordinates only under an explicit certified
   deletion policy.

The data generator must emit all retained children for each row. A selected
path, a list of alternative replay separations, or a collection of separately
valid exact tails is not sufficient.

The next structural target is a parent-intrinsic obstruction coordinate or a
constructive deletion policy whose exported reserve survives exact overlap
accounting across the full child family.

---

## 10. Scope

The harness establishes exact bookkeeping only. The repository now has finite
small-state child ledgers, but it does not establish:

- a general deletion-DAG transition generator;
- a schedule-independent positive novelty reserve;
- feasible reserve weights;
- bounded overlap;
- monotone rectangle growth;
- a branching Carleson inequality;
- or a solution of the four-term Erdős problem.

Its purpose is to ensure that future finite-state experiments fail or succeed
for mathematical reasons rather than decimal error, incomplete child lists,
ambiguous branching semantics, or unrecorded schedule choices.
