# Certainty ledger

This file records claims that should survive context loss. Each entry states status, confidence, audit state, and consequence.

The full Erdős reciprocal-sum problem remains open. The authoritative dependency order is in `docs/current-proof-program.md`.

---

## CL-001: Automatic sets cannot be counterexamples

**Status:** proved modulo standard regular-language growth and Szemerédi.

**Certainty:** high.

**Audit state:** likely standard or folklore; not independently checked here.

**Consequence:** fixed finite automata and regular digit languages cannot produce a divergent reciprocal-sum counterexample.

---

## CL-002: AP-free divergent candidates are sparse in every fixed-ratio interval

**Status:** standard consequence of Szemerédi.

**Certainty:** high.

For dyadic densities

```math
\alpha_j
=
\frac{|A\cap[2^j,2^{j+1})|}{2^j},
```

a divergent AP-free candidate must satisfy

```math
\alpha_j\to0,
\qquad
\sum_j\alpha_j=\infty.
```

---

## CL-003: Blockwise extremal bounds reduce the problem to summability

**Status:** standard reduction.

**Certainty:** high.

If

```math
\sum_j\frac{r_k(2^j)}{2^j}<\infty,
```

then every `k`-AP-free set has convergent reciprocal sum.

**Consequence:** known general bounds for `k>=4` are insufficient; cross-scale structure is needed.

---

## CL-004: Earlier finite-state search is supporting work only

**Status:** computationally verified and consequence of CL-001.

**Certainty:** high for the implemented finite checks.

**Consequence:** PB/MaxSAT, shifted Kempner, modular digit, and DFA tools are not the active proof route.

---

## CL-005: Side-anchor deletion produces an affine DAG

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

For a four-term-progression-free block

```math
D\subseteq[N,2N),
```

run side-anchor deletion until a three-term-progression-free residual of size `s<=r_3(N)` remains. If `K=|D|-s`, the selected progressions define an acyclic graph in which every deleted vertex has outdegree two and every residual vertex has outdegree zero.

**Primary note:** `docs/side-anchor-deletion-dag.md`.

---

## CL-006: Exact indegree excess and merge-difference children

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** central claim awaiting independent review.

If `rho` is the number of indegree-zero vertices, then

```math
\boxed{
\sum_v\max\{d^-(v)-1,0\}=K-s+\rho.
}
```

Translating incoming sponsors at each target gives four-term-progression-free children `Delta_v subseteq[1,N)` satisfying

```math
\boxed{
\sum_v|\Delta_v|=K-s+\rho.
}
```

**Primary note:** `docs/deletion-dag-merge-difference-recursion.md`.

---

## CL-007: Spanning-forest component translations

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

Choosing one incoming edge for every nonroot DAG vertex and translating each resulting component by its numerical minimum gives four-term-progression-free children `Theta_j subseteq[1,N)` with

```math
\boxed{
\sum_j|\Theta_j|=K+s-\rho.
}
```

Together with CL-006,

```math
\boxed{
\sum_j|\Theta_j|+\sum_v|\Delta_v|=2K.
}
```

**Primary note:** `docs/spanning-forest-binary-four-thirds-recursion.md`.

---

## CL-008: One structural occurrence per parent retains at least `2K/3`

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

A residual parent carries at most one structural occurrence. A deleted sponsor carries at most one component occurrence and at most two merge occurrences. Retaining at most one structural occurrence per parent preserves at least

```math
\frac{2K}{3}
```

structural occurrences and harmonic mass at least

```math
\boxed{
\frac{2K}{3N}.
}
```

---

## CL-009: Full middle children are four-term-progression-free

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

For each center `x`, define

```math
M_x=\{q_i:b_i=x\}.
```

Each `M_x` is four-term-progression-free. Every selected step satisfies `q_i<=N/2`, so

```math
\boxed{
\sum_xH(M_x)\ge\frac{2K}{N}.
}
```

**Consequence:** the old one-third valuation-color loss is unnecessary for deletion-DAG recursion.

**Primary note:** `docs/full-middle-binary-eight-thirds-recursion.md`.

---

## CL-010: Binary full-middle eight-thirds occurrence recursion

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

Retaining every full-middle occurrence and at most one structural occurrence per parent gives a binary genealogy satisfying

```math
\boxed{
\sum H(\text{binary child occurrences})
\ge
\frac83H(D)
-
\frac83\frac{r_3(N)}N.
}
```

**Critical caveat:** this counts repeated numerical labels separately.

**Primary note:** `docs/full-middle-binary-eight-thirds-recursion.md`.

---

## CL-011: Exact middle multiplicity fibers

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

Let

```math
Q=\{q_i:1\le i\le K\}
```

be the distinct selected steps. For each `q in Q`, let

```math
X_q=\{b_i:q_i=q\}
```

and define

```math
\Xi_q
=
\{x-\min X_q:x\in X_q,\ x>\min X_q\}.
```

Each `Xi_q` is four-term-progression-free and lies in `[1,N)`. The exact identity is

```math
\boxed{
|Q|+\sum_{q\in Q}|\Xi_q|=K.
}
```

**Consequence:** every additional occurrence of a middle label is converted into a lower-scale four-term-progression-free center-difference occurrence. Within-node middle multiplicity is resolved exactly.

**Primary note:** `docs/middle-multiplicity-fiber-five-thirds-recursion.md`.

---

## CL-012: Binary multiplicity-resolving five-thirds recursion

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

Choose one representative center for each distinct step `q`. Its sponsor produces terminal distinct label `q`. Every nonrepresentative sponsor produces the corresponding `Xi_q` occurrence. Thus each deleted sponsor produces exactly one multiplicity-resolved middle output.

Together with at most one structural output per parent, the genealogy is binary and

```math
\boxed{
H(Q)
+
\sum_qH(\Xi_q)
+
\sum H(\text{retained structural children})
\ge
\frac53H(D)
-
\frac53\frac{r_3(N)}N.
}
```

**Interpretation:** `H(Q)` is terminal distinct harmonic mass inside one parent node; the `Xi_q` children encode all additional copies recursively.

**Primary note:** `docs/middle-multiplicity-fiber-five-thirds-recursion.md`.

---

## CL-013: Root-rich versus long-path dichotomy

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

Root-rich deletion DAGs give strict merge-difference harmonic gain. Root-poor DAGs contain long valuation-directed affine paths.

**Current role:** supporting theory.

**Primary note:** `docs/deletion-dag-root-depth-dichotomy.md`.

---

## CL-014: Componentwise scale-compensated side-middle packing

**Status:** proved in repository through finite case classification.

**Certainty:** medium.

**Audit state:** awaiting independent symbolic review.

**Current role:** supporting theory for possible future multiplicity potentials.

**Primary notes:**

- `docs/full-component-scale-export.md`
- `docs/unequal-cardinality-scale-compensated-packing.md`

---

# Superseded quantitative results

The binary factors

```math
\frac76,
\qquad
\frac43,
\qquad
\frac{16}{9}
```

remain valid but are superseded as raw occurrence bounds by CL-010.

---

# Explicitly false targets

The following are false and must not be reused without additional hypotheses:

1. uniformly bounded depth-two affine-lift overlap;
2. universal uncorrected local `8/3` packing;
3. naive recursive density increment in the inherited three-dilate class;
4. creation of genuine off-diagonal discrepancy by fixed-size sampling.

Primary counterexample notes remain in `docs/`.

---

# Open bottleneck OB-001: Cross-state multiplicity and scale contraction

The raw theorem controls occurrence mass

```math
\sum_d\frac{m(d)}d.
```

CL-011 and CL-012 resolve repeated middle labels within one parent node. The unresolved problem is repetition across different parent states:

```math
\boxed{
\text{cross-state multiplicity}
\quad+
\text{scale contraction}
\quad+
\text{genealogical overlap}.
}
```

Approved next targets:

1. group equal terminal steps across sibling or same-depth states and construct global fiber children;
2. build a potential that counts each terminal numerical label once and charges repeated copies recursively;
3. prove a bounded-energy theorem for equal labels across states;
4. prove a stopping theorem for repeated rapid contraction;
5. computationally search for multigeneration examples with high cross-state multiplicity and low distinct harmonic gain.

No current repository theorem closes this gap.
