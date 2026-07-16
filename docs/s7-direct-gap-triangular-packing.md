# Exact S7 direct gap-triangular pair packing

## Status

Exact finite rational max-flow certificate for the recursive heavy remainder produced by direct activated-pair discharge on the certified `S7` frontier.

The result does not prove the universal Hall inequality. It proves that the complete recorded recursive heavy demand can be absorbed by one physical capacity unit on strictly lower-gap pair resources, after previously allocated light-support usage is subtracted.

No generation six is propagated.

---

## 1. Entering direct-discharge profile

The complete activated physical pair union has

```text
pairs = 75,247
mass  = 1181.622166508078...
```

Direct completion against the full certified `S7` saturation map gives

```text
S7 edge-supported mass       = 768.942708765373...
certified-hole pair mass     = 393.326066273840...
finite admissible remainder  =  19.353391468865...
```

The capacity-aware hole split gives

```text
light support capacity =  69.692004567827...
heavy load             = 386.800774397137...
  terminal             = 384.435641253780...
  recursive            =   2.365133143358...
```

There are `278` recursive heavy shell occurrences and `23,638` terminal heavy shell occurrences.

---

## 2. Horizontal-chain candidate pairs

Every recursive heavy shell

```math
T=\{d_1<\cdots<d_n\}\subseteq[M,2M)
```

contains a three-AP and therefore has `n>=3`. Its physical horizontal adjacent chain consists of pairs with gaps

```math
d_{i+1}-d_i<M.
```

The exact frontier contains

```text
recursive states          = 278
chain pair occurrences    = 1,949
distinct physical pairs   = 991
```

All `991` pair identities already belong to the entering activated/light-support ledger. This is expected: they are lower-gap Bellman child resources, not fresh pair capacity.

---

## 3. Exact rational flow network

Construct a bipartite network:

```text
source
  -> one node per recursive heavy shell, capacity alpha H(T)
  -> its physical horizontal-chain pair nodes
  -> sink, capacity 1/gap minus prior light-support usage.
```

An activated pair is allowed one capacity unit because every incidence comes from a strictly larger gap shell. Its current occurrence is the parent Bellman term; its lower-gap capacity is the child term. Using it in the flow is triangular cancellation, not simultaneous double use.

All arithmetic is exact over `fractions.Fraction`.

---

## 4. Certified result

The exact max-flow values are

```text
recursive shell demands           = 278
chain pair universe               = 991
pairs receiving positive flow     = 206
activated child pairs used        = 206
light-support pairs used          =   0
saturated pairs                   =   6

recursive demand                  =   2.365133143358...
available lower-gap capacity      = 256.746971983705...
exact maximum flow                =   2.365133143358...
unmet demand                      =   0
unused capacity on allocated pairs=  84.582249017623...
maximum pair utilization          =   1
```

Therefore

```math
\boxed{
\text{all recorded recursive heavy demand}
\le
\text{one-copy lower-gap physical pair capacity}.
}
```

The min cut after saturation has zero reachable state demand and zero reachable pair capacity, as expected for a fully feasible flow.

---

## 5. Interpretation

The finite `S7` direct frontier now has no unpaid recursively continuing harmonic state.

Its recursive heavy term is converted exactly into lower-gap activated pair capacity:

```text
larger-gap recursive shell debt
    -> strictly lower-gap physical pair child terms
    -> exact one-capacity fractional packing.
```

The prior raw horizontal-chain occurrence mass,

```text
560.189498866638...
```

was not the correct debt. It was the sum of full pair capacities over every occurrence. The exact flow uses only

```text
2.365133143358...
```

of that capacity.

---

## 6. What this closes and what remains

### Closed on the exact frontier

- direct activated-pair classification;
- capacity-aware light/heavy support allocation;
- terminal versus recursive heavy-shell split;
- statewise horizontal-chain domination;
- physical pair overlap across all `278` recursive shells;
- exact lower-gap fractional packing with one capacity per pair.

### Still open universally

1. prove the corresponding Hall inequality for every maximal four-AP-free parent, or identify the exact obstruction class;
2. control terminal-sink first appearance and recreation across the full tree;
3. incorporate cross-shell actual-root completions into the global production ledger;
4. prove that the gap-triangular pair cancellation telescopes under the complete retained branching construction;
5. replace the finite `S7` saturation classification by the maximal-ambient dichotomy in the infinite proof.

The key advance is localization: the recorded `S7` recursive pair-activation obstruction is now completely packed. The remaining work is a universal pair-capacity theorem, not another retained generation.

---

## 7. Reproducibility

Primary verifier:

```text
src/probe_s7_direct_gap_triangular_chain_flow.py
```

Shared exact instance builder:

```text
src/s7_direct_chain_instance.py
```

Workflow:

```text
Terminal pair payment v2 check
run 29459076037
```

Artifact digest:

```text
sha256:7560380b3933e07b427b5952aa24c77cca200791e17afda4b31be543aeda4ab9
```

Flow payload hash:

```text
aebbe8b68fc7e1e35680ea42959958985057e70d4700657a2e40f0ebef17861e
```

Pair-universe hash:

```text
b3021043bb3ca331bf195b317bca6f4080fe6fa323a26e9475075ecd1da17d95
```

Positive-allocation hash:

```text
935bd95e744d3a9ec9c17767248b172f0f92f2ad54334d639d44cf236844e7f7
```