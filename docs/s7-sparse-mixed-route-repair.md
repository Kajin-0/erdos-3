# Sparse mixed-route repair of the exact `S7` cut

## Status

Exact finite positive certificate repairing the corrected alternate-route Hall obstruction with a sparse set of first-copy horizontal-chain incidences.

The alternate route alone has a 19-state min-cut deficit. Adding every primary-chain edge for those 19 states makes the flow feasible, but most added incidences are unnecessary. One deterministic exact maximum flow uses only 11 primary physical pairs owned by 12 states. Deleting every unused primary incidence preserves feasibility.

---

## 1. Alternate-route obstruction

The corrected alternate network has

```text
recursive states             278
recursive demand             2.365133143358...
alternate maximum flow       2.361437656917...
unmet demand                 0.003695486441...
```

Its exact minimum cut contains

```text
states                        19
pair identities              176
cut demand            0.103968642815...
cut capacity          0.100273156374...
```

All 19 cut states are right-adjacent:

```text
shell base 512   :  4 states
shell base 1024  :  2 states
shell base 2048  : 13 states
```

---

## 2. Candidate primary augmentation

The 19 cut states collectively have

```text
112 primary-chain pair identities;
 98 absent from the alternate pair universe;
 14 already present in that universe.
```

Add these primary incidences only to the cut states and rerun the complete exact rational flow. The network becomes feasible:

```text
mixed maximum flow           2.365133143358...
mixed unmet demand           0
```

The added primary allocation is

```math
0.004148152390\ldots
```

compared with the original cut deficit

```math
0.003695486441\ldots.
```

Thus the repair ratio is

```math
\boxed{1.122491573610\ldots}.
```

---

## 3. Sparse positive support

Inspect one deterministic maximum-flow witness and retain only the primary incidences carrying positive flow. The support has

```text
states using a primary edge   12
primary physical pairs        11
```

Re-solving after deleting every other primary incidence remains exactly feasible. Therefore these 11 pairs form a complete sparse repair certificate.

The pair gaps are

```text
8, 9, 9, 10, 10, 31, 31, 61, 61, 152, 426.
```

The two gap-31 states at shell base `512` share one primary pair; every other used primary pair has one state owner in the selected flow.

The state-shell profile of positive primary use is

```text
shell base 512   : 2 states
shell base 1024  : 1 state
shell base 2048  : 9 states
```

---

## 4. Strict scale descent

Every used primary gap is below the shell base of every state assigning mass to it. The largest used gap is

```math
426<512.
```

Hence the repair retains strict gap descent. No same-scale physical-pair exception is introduced.

The repair is therefore compatible with the lineage gap-moment theorem:

```text
alternate route for the bulk of the flow;
11 sparse primary bridges across the obstructing cut;
all primary bridges strictly lower-gap.
```

---

## 5. Interpretation

Local route surplus is not enough: the alternate route has an exact Hall obstruction even though every state is individually over-capacitated.

The obstruction is nevertheless localized. The primary route does not need to replace the alternate route globally. A small family of lower-gap primary bridges repairs the cut.

This suggests the correct finite orientation procedure:

1. begin with one canonical route;
2. compute an exact deficient cut;
3. expose an alternate lower-gap route only for cut states;
4. retain only positive repair incidences;
5. repeat if a new cut remains.

On the certified `S7` frontier, one augmentation step is sufficient.

This is an exact finite algorithmic theorem, not a universal Hall theorem. Dense maximal-ambient constructions still rule out unrestricted physical-union packing.

**Probe:** `src/probe_s7_alternate_cut_primary_repair.py`  
**Workflow run:** `29466025218`  
**Payload SHA-256:** `ef282d1cb0c9463696d8566ef029f29db1fb19caca8cc1717d42ac65e508cc9`
