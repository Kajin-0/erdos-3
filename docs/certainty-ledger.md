# Certainty ledger

This file records claims that should survive context loss. Each entry separates:

- **status**: standard / proved in repository / computationally verified / conjectural / false / superseded / open bottleneck;
- **certainty**: how strongly the project should rely on the claim;
- **audit state**: whether the claim has received independent review;
- **consequence**: what the claim proves, rules out, or redirects.

The full Erdős reciprocal-sum problem remains open.

The authoritative dependency order is maintained in:

```text
docs/current-proof-program.md
```

---

## CL-001: Automatic sets cannot be counterexamples

**Status:** proved modulo standard regular-language growth and Szemerédi.

**Certainty:** high.

**Audit state:** likely standard or folklore; not independently checked in this project.

**Consequence:** fixed finite automata and regular digit languages cannot produce a divergent reciprocal-sum counterexample.

---

## CL-002: AP-free divergent candidates are sparse in every fixed-ratio interval

**Status:** standard consequence of Szemerédi.

**Certainty:** high.

**Audit state:** standard.

**Statement.** If `A` is `k`-AP-free for fixed `k>=3`, then for every fixed `lambda>1`,

```math
\frac{|A\cap[N,\lambda N]|}{N}\to0.
```

For dyadic densities

```math
\alpha_j
=
\frac{|A\cap[2^j,2^{j+1})|}{2^j},
```

a divergent reciprocal sum requires

```math
\alpha_j\to0,
\qquad
\sum_j\alpha_j=\infty.
```

---

## CL-003: Blockwise extremal bounds reduce the problem to summability

**Status:** standard reduction.

**Certainty:** high.

**Audit state:** standard.

**Statement.** If

```math
\sum_j\frac{r_k(2^j)}{2^j}<\infty,
```

then every `k`-AP-free subset of the natural numbers has convergent reciprocal sum.

**Consequence:** known general bounds for `k>=4` are insufficient; cross-scale information is required.

---

## CL-004: Walker base-55 benchmark is locally rigid in the implemented model

**Status:** computationally verified.

**Certainty:** high for the finite computation; no global optimality claim.

**Audit state:** reproducible within the repository.

---

## CL-005: Finite-state search is not a full counterexample route

**Status:** consequence of CL-001.

**Certainty:** high.

**Consequence:** PB/MaxSAT and DFA tools are supporting or legacy work, not the active proof route.

---

## CL-006: Side-anchor deletion produces an affine DAG

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

**Statement.** For a four-term-progression-free block

```math
D\subseteq[N,2N),
```

repeatedly delete the coordinated side anchor of a selected three-term progression until a three-term-progression-free residual remains. Writing each selected progression as

```math
(a_i,b_i,c_i),
\qquad
a_i+c_i=2b_i,
```

the edges

```math
a_i\to b_i,
\qquad
a_i\to c_i
```

form an acyclic graph. Every deleted vertex has outdegree two and every residual vertex has outdegree zero.

If `K` vertices are deleted and `s` remain, then

```math
K=|D|-s,
\qquad
s\le r_3(N).
```

**Primary note:** `docs/side-anchor-deletion-dag.md`.

---

## CL-007: Exact indegree excess and merge-difference children

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** central claim awaiting independent review.

**Statement.** Let `rho` be the number of indegree-zero vertices. Then

```math
\boxed{
M
=
\sum_v\max\{d^-(v)-1,0\}
=
K-s+\rho.
}
```

For each target `v`, translating its incoming sponsors by their minimum gives a four-term-progression-free child

```math
\Delta_v\subseteq[1,N)
```

with

```math
\boxed{
\sum_v|\Delta_v|=K-s+\rho.
}
```

**Primary note:** `docs/deletion-dag-merge-difference-recursion.md`.

---

## CL-008: Spanning-forest component translations

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

**Statement.** Choose one incoming edge for every nonroot DAG vertex. Translating each forest component by its numerical minimum gives four-term-progression-free children

```math
\Theta_j\subseteq[1,N)
```

with

```math
\boxed{
\sum_j|\Theta_j|=K+s-\rho.
}
```

Together with CL-007,

```math
\boxed{
\sum_j|\Theta_j|
+
\sum_v|\Delta_v|
=2K.
}
```

**Primary note:** `docs/spanning-forest-binary-four-thirds-recursion.md`.

---

## CL-009: One structural occurrence per parent retains at least `2K/3`

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

**Statement.** Associate component occurrences with their translated parent and merge occurrences with their nonminimal sponsor. A residual parent carries at most one structural occurrence and a deleted sponsor at most three.

Retaining at most one structural occurrence per parent preserves at least

```math
\boxed{
\frac{2K}{3}
}
```

structural occurrences. Since every structural label is below `N`,

```math
\boxed{
\sum H(\text{retained structural children})
\ge
\frac{2K}{3N}.
}
```

**Primary note:** `docs/full-middle-binary-eight-thirds-recursion.md`.

---

## CL-010: Full middle children are four-term-progression-free

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

**Statement.** For each center `x`, let

```math
M_x=\{q_i:b_i=x\}.
```

If four steps in `M_x` formed a four-term progression, then the corresponding points `x+q` would form a four-term progression in `D`. Therefore every `M_x` is four-term-progression-free.

Every selected step satisfies `q_i<=N/2`, and each selected progression contributes exactly one middle occurrence. Hence

```math
\boxed{
\sum_xH(M_x)
\ge
\frac{2K}{N}.
}
```

**Consequence:** the valuation-color restriction from the older side-middle packing branch is unnecessary for deletion-DAG recursion.

**Primary note:** `docs/full-middle-binary-eight-thirds-recursion.md`.

---

## CL-011: Binary full-middle eight-thirds recursion

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

**Statement.** Retain every full-middle occurrence and at most one structural occurrence per parent element. Every deleted sponsor creates at most two children: one middle and one structural. Every residual parent creates at most one structural child.

The total retained harmonic occurrence mass satisfies

```math
\boxed{
\sum H(\text{retained binary child occurrences})
\ge
\frac{8K}{3N}.
}
```

Therefore

```math
\boxed{
\sum H(\text{retained binary child occurrences})
\ge
\frac83H(D)
-
\frac83\frac{r_3(N)}N.
}
```

**Critical caveat:** this is an occurrence-multiset inequality. It does not establish growth in the harmonic mass of distinct integers.

**Consequence:** the current best binary branching factor is `8/3`.

**Primary note:** `docs/full-middle-binary-eight-thirds-recursion.md`.

---

## CL-012: Root-rich versus long-path dichotomy

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

**Statement.** Root-rich deletion DAGs give strict merge-difference harmonic gain. Root-poor DAGs contain a long path whose increments are

```math
x_{j+1}-x_j
=
\sigma(q_j)c_jq_j,
\qquad
c_j\in\{1,2\},
```

with direction determined by `v_2(q_j) mod 2`.

**Current role:** supporting theory, not part of the shortest binary `8/3` proof.

**Primary note:** `docs/deletion-dag-root-depth-dichotomy.md`.

---

## CL-013: Componentwise scale-compensated side-middle packing

**Status:** proved in repository through finite case classification.

**Certainty:** medium.

**Audit state:** awaiting independent symbolic review.

**Statement.** For a coordinated side shell `S subseteq [R,2R)` and paired middle subset `T`,

```math
|A(S)\cup M_q(T)|
+
R H(T\cap[1,R))
\ge
2+
\frac43(|S|+|T|)-\eta.
```

**Current role:** supporting theory rather than the shortest active proof chain.

---

# Superseded quantitative results

## SP-001: Binary seven-sixths thinning

**Status:** valid but superseded by CL-011.

## SP-002: Binary four-thirds spanning-forest thinning

**Status:** valid but superseded by CL-011.

## SP-003: Color-aware binary sixteen-ninths recursion

**Status:** valid but superseded by CL-011.

**Reason:** its one-third middle-color loss was unnecessary for recursive descent. Pairwise-disjoint first three dilates were needed only in the older local packing branch, not for four-term-progression-free child recursion.

---

# Explicitly false targets

## FL-001: Uniformly bounded depth-two affine-lift overlap

**Status:** false.

**Primary note:** `docs/depth-two-overlap-counterexample.md`.

## FL-002: Universal uncorrected local eight-thirds packing

**Status:** false.

**Primary note:** `docs/seven-thirds-local-packing-counterexample.md`.

## FL-003: Naive recursive density increment

**Status:** false as a general mechanism in the inherited three-dilate class.

## FL-004: Fixed-size sampling creates genuine off-diagonal discrepancy

**Status:** false.

**Primary note:** `docs/offdiagonal-correction-direction-energy.md`.

---

# Open bottleneck OB-001: Multiplicity versus scale contraction

The current theorem controls

```math
\sum_d\frac{m(d)}d,
```

where `m(d)` is descendant multiplicity. The original problem concerns

```math
\sum_{d:m(d)>0}\frac1d.
```

Because the genealogy is binary, raw occurrence count grows at most like `2^h`, already below `(8/3)^h`. The unresolved issue is rapid numerical contraction, which increases reciprocal weight.

The approved closing targets are:

1. prove a weighted multiplicity rate strictly below `8/3`;
2. construct a bounded multiscale potential;
3. control repeated-label energy;
4. prove a stopping theorem for repeated rapid contraction;
5. computationally search for multigeneration examples with high multiplicity, rapid contraction, and low distinct harmonic gain.

No current repository theorem closes this gap.