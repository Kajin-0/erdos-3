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

**Audit state:** not independently checked in this project; likely standard or folklore.

**Statement.** If a base-`b` automatic set has divergent reciprocal sum, then it has positive upper density and hence contains arithmetic progressions of every finite length.

**Consequence.** Fixed finite automata and regular digit languages cannot produce a divergent reciprocal-sum counterexample.

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

**Consequence.** The hard case is slowly divergent logarithmic-scale dust.

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

**Consequence.** Known general bounds for `k>=4` are insufficient; cross-scale information is required.

---

## CL-004: Walker base-55 benchmark is locally rigid in the implemented model

**Status:** computationally verified.

**Certainty:** high for the finite computation; no global optimality claim.

**Audit state:** reproducible within the repository.

**Consequence.** Small substitutions in the implemented cyclic modular model do not improve the benchmark.

---

## CL-005: Finite-state search is not a full counterexample route

**Status:** consequence of CL-001.

**Certainty:** high.

**Audit state:** same as CL-001.

**Consequence.** PB/MaxSAT and DFA tools are supporting or legacy work, not the active proof route.

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

**Consequence.** The overlap problem becomes a concrete geometric DAG problem.

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

For each target `v`, translate its incoming sponsors by their minimum to obtain

```math
\Delta_v\subseteq[1,N).
```

Each `Delta_v` is four-term-progression-free and

```math
\boxed{
\sum_v|\Delta_v|=K-s+\rho.
}
```

**Consequence.** Indegree merging generates canonical lower-scale children.

**Primary note:** `docs/deletion-dag-merge-difference-recursion.md`.

---

## CL-008: Spanning-forest component translations

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

**Statement.** Choose one incoming edge for every nonroot DAG vertex. The selected edges form a spanning forest with `rho` components. Translating each component by its numerical minimum produces four-term-progression-free children

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

**Consequence.** The residual and root terms cancel exactly at the structural-occurrence level.

**Primary note:** `docs/spanning-forest-binary-four-thirds-recursion.md`.

---

## CL-009: Structural load is at most three per deleted sponsor

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

**Statement.** Associate each component occurrence with its translated parent and each merge occurrence with its nonminimal sponsor. A residual parent carries at most one structural occurrence. A deleted sponsor carries at most:

1. one component occurrence;
2. two merge occurrences.

Thus its structural load satisfies

```math
\ell(a)\in\{0,1,2,3\}.
```

If `r` structural occurrences are attached to residual vertices, then

```math
\boxed{
\sum_{a\text{ deleted}}\ell(a)=2K-r.
}
```

**Consequence.** Structural thinning can be treated as a finite per-sponsor allocation problem.

---

## CL-010: Color-aware binary sixteen-ninths recursion

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

**Statement.** Give each deleted sponsor the color

```math
c(a)
=
v_2(q_a)-v_3(q_a)\pmod3.
```

Choose one color globally. Sponsors in that color retain their middle occurrence and at most one structural occurrence. Sponsors outside it retain at most two structural occurrences. Residual parents retain their structural occurrence.

Every parent creates at most two retained child occurrences.

Averaging over the three colors gives, for structural load `ell`,

```math
g(\ell)
=
\frac{2+1_{\ell\ge1}+2\min\{\ell,2\}}3
\ge
\frac23+\frac59\ell.
```

Using CL-009, some color satisfies

```math
\boxed{
\sum H(\text{retained binary child occurrences})
\ge
\frac{16K}{9N}.
}
```

Therefore

```math
\boxed{
\sum H(\text{retained binary child occurrences})
\ge
\frac{16}{9}H(D)
-
\frac{16}{9}\frac{r_3(N)}N.
}
```

**Critical caveat.** This is an occurrence-multiset inequality. It does not establish growth in the harmonic mass of distinct integers.

**Consequence.** The current best binary branching factor is `16/9`.

**Primary note:** `docs/color-aware-binary-sixteen-ninths-recursion.md`.

---

## CL-011: Root-rich versus long-path dichotomy

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

**Statement.** If

```math
\rho\ge\delta|D|,
```

then the merge-difference family has strict harmonic gain. If roots are sparse, the DAG contains a long path whose increments have the form

```math
x_{j+1}-x_j
=
\sigma(q_j)c_jq_j,
\qquad
c_j\in\{1,2\},
```

with the sign determined by `v_2(q_j) mod 2`.

**Consequence.** Near-critical merge behavior requires long valuation-directed affine cancellation.

**Primary note:** `docs/deletion-dag-root-depth-dichotomy.md`.

---

## CL-012: Componentwise scale-compensated side-middle packing

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

**Consequence.** Efficient local overlap exports potential to lower scale. This remains supporting theory rather than the shortest active proof chain.

**Primary notes:**

- `docs/full-component-scale-export.md`
- `docs/unequal-cardinality-scale-compensated-packing.md`

---

# Superseded quantitative results

## SP-001: Binary seven-sixths thinning

**Status:** valid but superseded.

**Statement.** Merge-plus-middle thinning gave binary branching factor `7/6`.

**Superseded by:** CL-010.

## SP-002: Binary four-thirds spanning-forest thinning

**Status:** valid but superseded.

**Statement.** Retaining one structural occurrence per parent and the selected middle occurrence gave binary branching factor `4/3`.

**Superseded by:** CL-010.

---

# Explicitly false targets

## FL-001: Uniformly bounded depth-two affine-lift overlap

**Status:** false.

**Certainty:** high; explicit finite-avoidance construction.

**Primary note:** `docs/depth-two-overlap-counterexample.md`.

## FL-002: Universal uncorrected local eight-thirds packing

**Status:** false.

**Certainty:** high; explicit computationally checkable example.

**Primary note:** `docs/seven-thirds-local-packing-counterexample.md`.

## FL-003: Naive recursive density increment

**Status:** false as a general mechanism in the inherited three-dilate class.

**Certainty:** high internally.

## FL-004: Fixed-size sampling creates genuine off-diagonal discrepancy

**Status:** false.

**Certainty:** high internally.

**Primary note:** `docs/offdiagonal-correction-direction-energy.md`.

---

# Open bottleneck OB-001: Multiplicity versus scale

The current theorem controls

```math
\sum_d\frac{m(d)}d,
```

where `m(d)` is descendant multiplicity. The original problem concerns

```math
\sum_{d:m(d)>0}\frac1d.
```

The active closing targets are:

1. prove an effective weighted multiplicity rate strictly below `16/9`;
2. construct a bounded multiscale potential;
3. rule out or quantify the abstract extremal structural-load pattern
   ```math
   \ell=0\text{ on one third},
   \qquad
   \ell=3\text{ on two thirds};
   ```
4. computationally search for multigeneration examples with high multiplicity, rapid contraction, and low unique harmonic gain.

No current repository result closes this gap.