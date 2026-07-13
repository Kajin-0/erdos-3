# Exact branching-reserve LP interface

## Status

Research infrastructure for the whole-tree Bellman program. This tool exports and verifies candidate reserve inequalities; it does not establish that the current feature family is sufficient.

**Implementation:** `src/branching_reserve_lp.py`

---

## 1. Target inequality

For a parent state `B` with its complete retained child family, the desired inequality is

```math
D(B)
+
\sum_{B'\in\operatorname{Child}(B)}\Phi(B')
\le
\Phi(B)+E(B),
```

where:

```text
D(B) = Bellman debt created at the parent transition;
E(B) = explicitly controlled error;
Phi   = a nonnegative linear reserve candidate.
```

Let a state feature vector be

```math
f(B)=(f_1(B),\ldots,f_m(B))
```

and let

```math
\Phi(B)=\sum_{j=1}^m w_j f_j(B),
\qquad
w_j\ge0.
```

Then each parent transition gives the exact linear constraint

```math
\sum_j
\left(
 f_j(B)
 -
 \sum_{B'}m(B')f_j(B')
\right)w_j
\ge
D(B)-E(B),
```

where `m(B')` is the child multiplicity after the chosen deduplication convention.

The essential point is that every row aggregates all retained children. Encoding one row per path would test a weaker and mathematically insufficient condition.

---

## 2. Exact input format

The input is JSON Lines. Every nonempty, non-comment line is one complete parent transition.

```json
{
  "name": "state-17-factor-four",
  "debt": "127/64",
  "error": "0",
  "parent": {
    "radius_deficit": "31/8",
    "support_holes": "5",
    "imported_prefix": "3/2"
  },
  "children": [
    {
      "multiplicity": 1,
      "features": {
        "radius_deficit": "1/2",
        "support_holes": "2",
        "imported_prefix": "1"
      }
    }
  ]
}
```

All numbers should be integers or exact rational strings. Floating-point input is rejected deliberately.

Suggested first-generation features are:

```text
radius_deficit_2;
radius_deficit_4;
support_holes_2;
support_holes_4;
completion_deficit;
imported_prefix_mass;
overlap_excess;
slack_consumed;
```

Each feature should already be normalized into Bellman-compatible units, normally by multiplication by `P/L` where appropriate.

---

## 3. Commands

Run the internal exact regression checks:

```bash
python3 src/branching_reserve_lp.py self-test
```

Export a CPLEX-LP feasibility instance:

```bash
python3 src/branching_reserve_lp.py export \
  data/branching_transitions.jsonl \
  /tmp/branching_reserve.lp
```

Verify a proposed nonnegative weight vector exactly:

```bash
python3 src/branching_reserve_lp.py verify \
  data/branching_transitions.jsonl \
  data/branching_reserve_weights.json
```

A weight file has the form

```json
{
  "radius_deficit_2": "3/2",
  "radius_deficit_4": "1",
  "support_holes_4": "7/16"
}
```

The exporter clears all rational denominators row by row, so the generated LP uses exact integer coefficients. The verifier reports the exact rational slack of every transition and exits nonzero if any row fails.

---

## 4. Required transition generator

The next missing component is a state enumerator that emits one row per parent with the complete child aggregate. It must record:

```text
parent state identifier and genealogy;
scale factor and exact Bellman debt;
all retained children after standard shell resolution;
child multiplicity or deduplication weight;
P/L-normalized interval-radius deficits;
zero-set hole counts;
completion and rectangle coverage coordinates;
imported-prefix provenance;
slack consumption;
any controlled error term and its proof source.
```

The generator must not silently discard children that are inconvenient for a candidate reserve.

---

## 5. Falsification protocol

A failed LP is useful only if it produces an exact obstruction.

For every infeasible feature family, retain:

1. the smallest failing parent transition;
2. its complete child list;
3. the negative exact slack under the proposed weights;
4. the missing structural phenomenon suggested by the failure;
5. whether the failure is caused by branching, imported prefixes, support holes, or overlap duplication.

This should become the reserve analogue of the repository stop list: failed potentials must remain documented to prevent repeated work.

---

## 6. Scope

The exporter and verifier establish only the correctness of the linear encoding and exact arithmetic. They do not provide:

1. a complete transition dataset;
2. feasible reserve weights;
3. a proof that a linear reserve suffices;
4. a controlled global error term;
5. the required branching Carleson inequality.

Their purpose is to make the next conjecture mechanically falsifiable and to prevent accidental replacement of the whole-tree theorem by a pathwise surrogate.
