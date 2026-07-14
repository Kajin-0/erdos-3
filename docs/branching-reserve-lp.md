# Exact branching-reserve LP harness

## Status

Exact rational infrastructure for candidate whole-tree reserve inequalities.

The repository distinguishes:

1. **replay siblings:** alternative outer separation choices;
2. **raw simultaneous occurrences:** all outputs generated together by one complete deletion schedule;
3. **retained Bellman children:** the family left after a proved retention and packing rule;
4. **LP rows:** exact inequalities formed from the retained family.

Only the fourth object is accepted by `src/branching_reserve_lp.py`.

Related exporters:

- `src/export_simultaneous_deletion_transition.py`;
- `src/export_terminal_fiber_scc_quotient.py`.

---

## 1. Target inequality

For parent `S`, the intended inequality is

```math
D(S)
+
\sum_{S'\in\mathrm{Child}(S)}\Phi(S')
\le
\Phi(S)+E(S),
```

where `Child(S)` is the complete **retained** simultaneous family.

For

```math
\Phi(S)=\sum_f w_fF_f(S),
\qquad
w_f\ge0,
```

one row represents

```math
\sum_f
\left(
F_f(S)-\sum_{S'}m(S')F_f(S')
\right)w_f
\ge
D(S)-E(S).
```

All values are exact rational numbers.

---

## 2. JSONL row format

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

Numbers may be integers or rational strings. Floating-point values and booleans are rejected. Denominators are cleared exactly before CPLEX-LP output.

---

## 3. Replay siblings are not children

The replay catalog enumerates alternative outer replication choices. `S_1` has four factor-four replay siblings, while `S_2` has `203` factor-eight replay siblings. These alternatives cannot be put into one `children` array without a simultaneous-retention theorem.

---

## 4. Raw simultaneous transition frontier

The fixed lexicographic exporter records the complete raw occurrence family with schedule, shell resolution, provenance, duplicate classes, containments, partial overlaps, terminal-recursive overlap, and exact mass ledgers.

| parent | occurrences | state classes | duplicate classes | containments | partial overlaps |
|---:|---:|---:|---:|---:|---:|
| `S_1` | 5 | 4 | 1 | 1 | 0 |
| `S_2` | 11 | 10 | 1 | 3 | 5 |
| `S_3` | 25 | 21 | 3 | 23 | 15 |
| `S_4` | 46 | 34 | 7 | 91 | 35 |
| `S_5` | 68 | 51 | 11 | 145 | 88 |
| `S_6` | 94 | 71 | 15 | 209 | 150 |
| `S_7` | 127 | 95 | 20 | 345 | 214 |

These are raw simultaneous occurrences, not retained Bellman children.

---

## 5. Required retention contract

A valid raw-payload-to-LP conversion must state:

1. whether the potential is occurrence-, state-, support-, provenance-, or component-valued;
2. which exact duplicate classes merge;
3. how provenance multiplicity is retained;
4. how strict containment is charged;
5. how partial overlap is charged;
6. how terminal-recursive overlap is handled;
7. how terminal-fiber SCCs are represented;
8. how internal SCC recycling is funded;
9. how imported labels are matched across generations;
10. a bound preventing repeated payment by the same provenance;
11. any discarded mass entered as controlled error;
12. proof that the emitted retained family is complete.

Without this contract, an exactly solved LP can represent the wrong inequality.

---

## 6. Terminal-fiber SCC state

Draw an edge

```math
q\longrightarrow u
```

when terminal label `u` belongs to `Xi_q`.

The graph contains `61 <-> 303` at `S_3`. At `S_7`, the cyclic component is

```math
\{1,5,61,303,1597,8195,323640\}.
```

A strict decreasing terminal-label rank is therefore invalid.

Collapsing SCCs gives an acyclic condensation graph, but internal recycling remains. If

```math
V(C)=\sum_{u\in C}\frac1u
```

and

```math
T(C)=\sum_{(q,u)\text{ internal edge}}\frac1u,
```

then the `S_7` component has

```math
T(C)-V(C)
=
\frac{43727503229099}{1043823972523464}>0.
```

Harmonic vertex mass alone is not sufficient component capacity.

---

## 7. Exact spectral constraint on linear SCC features

Let `A` be the internal SCC adjacency matrix. A positive linear component capacity satisfying

```math
Aw\le\lambda w
```

requires

```math
\lambda\ge\rho(A).
```

For the two-label component through `S_6`, `rho(A)=1`.

For the seven-label `S_7` component, the exact witness

```math
w=(43,59,31,31,14,10,26)^T
```

satisfies

```math
9Aw-23w>0,
\qquad
8w-3Aw>0.
```

Hence

```math
\boxed{
\frac{23}{9}<\rho(A)<\frac83.
}
```

Consequences for LP design:

1. no positive linear SCC feature can be nonexpanding on this component;
2. no such feature can achieve factor-two contraction;
3. a constraint family that assumes `Aw<=2w` is exactly infeasible before any Bellman debt is added;
4. external obstruction export, nonlinear capacity, or multi-generation amortization must enter the row.

The LP adapter should reject any component model whose claimed internal factor is below `23/9` for the recorded `S_7` payload.

---

## 8. Known feature no-go results

The following standalone feature families are already ruled out:

### Naive mass coordinates

```text
weighted_density
right_shell_slack
incoming_contamination_mass
```

cannot pay `S_6 -> S_7`.

### Raw novelty

Novel fiber mass is schedule dependent on `S_2` and has schedule minimum zero.

### Forced-fork feature

`P Psi` is positive but not a standalone telescoping potential.

### Terminal-label rank

The incidence graph is cyclic from `S_3`.

### Separation-history state

At `S_7`, overlap includes `5,49158,323640` beyond historical separations.

### Unit harmonic SCC capacity

Internal target mass exceeds vertex mass at `S_7`.

### Positive linear SCC contraction through factor two

The exact spectral lower bound is `23/9>2`.

---

## 9. Commands

Export a feasibility LP:

```bash
python3 src/branching_reserve_lp.py export \
  constraints.jsonl reserve.lp
```

Verify nonnegative weights:

```bash
python3 src/branching_reserve_lp.py verify \
  constraints.jsonl weights.json
```

Export a raw transition:

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

Run the complete suite:

```bash
bash src/run_verify_transport_reserve.sh
```

---

## 10. Active next LP input

The next dataset must include external export from the high-growth cyclic component. Candidate variables are:

- internal SCC capacity;
- outgoing condensation capacity;
- nonterminal-fiber export mass;
- affine-obstruction coverage;
- completion and rectangle-support growth;
- imported-label reuse capacity;
- target interval demand;
- dyadic slack as an auxiliary term.

The adapter should test

```math
\text{internal recycling}
+
\text{outgoing retained capacity}
+
\text{Bellman debt}
\le
\text{incoming capacity}
+
\text{obstruction export}
+
\text{controlled error}.
```

Every candidate convention must emit the smallest exact failing transition.

---

## 11. Scope

The harness and exporters establish exact bookkeeping. They do not establish:

- a valid retention quotient;
- sufficient nonlinear or external SCC capacity;
- bounded cross-generation reuse;
- feasible whole-tree weights;
- a branching Carleson inequality;
- or the four-term Erdős conjecture.
