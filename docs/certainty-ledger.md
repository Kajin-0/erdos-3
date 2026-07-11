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

**Statement.** If `A subseteq N` is base-`b` automatic and

```math
\sum_{n\in A}\frac1n=\infty,
```

then `A` has positive upper asymptotic density and therefore contains arithmetic progressions of every finite length.

**Consequence.** No fixed finite automaton or regular digit language can produce a divergent reciprocal-sum counterexample.

---

## CL-002: An AP-free divergent candidate is sparse in every fixed-ratio interval

**Status:** standard consequence of Szemerédi.

**Certainty:** high.

**Audit state:** standard.

**Statement.** If `A subseteq N` is `k`-AP-free for fixed `k>=3`, then for every fixed `lambda>1`,

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

then every `k`-AP-free subset of `N` has convergent reciprocal sum.

**Consequence.** Known general `r_k(N)` bounds for `k>=4` are insufficient; cross-scale information is needed.

---

## CL-004: Walker base-55 benchmark is locally rigid in the implemented model

**Status:** computationally verified.

**Certainty:** high for the finite computation; no global optimality claim.

**Audit state:** reproducible within the repository.

**Statement.** Walker's public base-55 shifted Kempner digit set has no AP-free same-size digit-substitution neighbor at radius one or two in the implemented cyclic modular model.

**Consequence.** Small perturbations in that finite model are unlikely to improve the benchmark.

---

## CL-005: Finite-state search is not a full counterexample route

**Status:** consequence of CL-001.

**Certainty:** high.

**Audit state:** same as CL-001.

**Statement.** DFA and regular-language searches can study finite extremizers but cannot produce an AP-free set with divergent reciprocal sum.

**Consequence.** The PB/MaxSAT and DFA infrastructure is supporting or legacy work, not the active proof route.

---

## CL-006: Side-anchor deletion produces an affine DAG

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

**Statement.** Let

```math
D\subseteq[N,2N)
```

be four-term-progression-free. Repeatedly select a three-term progression and delete its coordinated side anchor until the residual set is three-term-progression-free.

Writing each selected progression as

```math
(a_i,b_i,c_i),
\qquad
a_i+c_i=2b_i,
```

with `a_i` deleted, the edges

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

**Consequence.** The overlap problem becomes a concrete geometric DAG.

**Primary note:** `docs/side-anchor-deletion-dag.md`.

---

## CL-007: Exact indegree excess and merge-difference children

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** central claim awaiting independent review.

**Statement.** Let `rho` be the number of indegree-zero DAG vertices. Then

```math
\boxed{
M
=
\sum_v\max\{d^-(v)-1,0\}
=
K-s+\rho.
}
```

For each target `v`, translate its incoming sponsors by the smallest sponsor to obtain

```math
\Delta_v\subseteq[1,N).
```

Each `Delta_v` is four-term-progression-free and

```math
\boxed{
\sum_v|\Delta_v|=K-s+\rho.
}
```

Consequently,

```math
\boxed{
\sum_vH(\Delta_v)
\ge
H(D)-2\frac{r_3(N)}N.
}
```

**Critical caveat.** Harmonic mass is counted with multiplicity across child states.

**Primary note:** `docs/deletion-dag-merge-difference-recursion.md`.

---

## CL-008: Spanning-forest component children

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

**Statement.** Choose one incoming edge for every nonroot deletion-DAG vertex. The chosen edges form a spanning forest with `rho` components `C_j`.

Translating each component by its numerical minimum gives a four-term-progression-free child

```math
\Theta_j\subseteq[1,N)
```

with

```math
\boxed{
\sum_j|\Theta_j|
=|D|-\rho
=K+s-\rho.
}
```

Combining with CL-007 gives the exact structural balance

```math
\boxed{
\sum_v|\Delta_v|
+
\sum_j|\Theta_j|
=2K.
}
```

**Consequence.** The root and residual terms cancel exactly before thinning.

**Primary note:** `docs/spanning-forest-binary-four-thirds-recursion.md`.

---

## CL-009: Selected middle children

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

**Statement.** Selecting the heaviest color of

```math
\chi(q)=v_2(q)-v_3(q)\pmod3
```

and grouping by middle point produces four-term-progression-free children `M_x^*` satisfying

```math
\boxed{
\sum_xH(M_x^*)
\ge
\frac{2K}{3N}.
}
```

Each deleted sponsor creates at most one selected middle occurrence.

**Primary notes:**

- `docs/sponsored-three-ap-binary-recursion.md`
- `docs/deletion-dag-merge-difference-recursion.md`

---

## CL-010: Binary four-thirds occurrence recursion

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** current central theorem awaiting independent review.

**Statement.** Associate each component occurrence with its parent element and each merge occurrence with its nonminimal sponsor. A residual parent carries at most one structural occurrence; a deleted parent carries at most three.

Since the two structural families contain exactly `2K` occurrences, selecting at most one structural occurrence per parent retains at least

```math
\frac{2K}{3}
```

structural occurrences. Retaining also the selected middle occurrence gives a genealogy in which every parent creates at most two children and

```math
\boxed{
\sum H(\text{binary child occurrences})
\ge
\frac43H(D)
-
\frac43\frac{r_3(N)}N.
}
```

**Critical caveat.** This is an occurrence-multiset inequality. It does not establish `4/3` growth in harmonic mass of distinct integers.

**Consequence.** The required multiplicity-growth threshold is now strictly below `4/3`, improving the previous `7/6` target.

**Primary note:** `docs/spanning-forest-binary-four-thirds-recursion.md`.

---

## CL-011: Root-rich versus long-path dichotomy

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

**Statement.** If

```math
\rho\ge\delta|D|,
```

then the merge family alone satisfies

```math
\sum_vH(\Delta_v)
\ge
(1+\delta)H(D)
-
2\frac{r_3(N)}N.
```

If roots are sparse, the maximum directed path length obeys

```math
L
\ge
\left\lceil
\log_2\left(\frac{|D|}{\rho}+1\right)
\right\rceil-1.
```

Path increments have valuation-directed form

```math
x_{j+1}-x_j
=
\sigma(q_j)c_jq_j,
\qquad c_j\in\{1,2\}.
```

**Consequence.** This remains a supporting multiplicity/path tool, but it is no longer needed merely to obtain a supercritical binary occurrence factor.

**Primary note:** `docs/deletion-dag-root-depth-dichotomy.md`.

---

## CL-012: Componentwise scale-compensated side-middle packing

**Status:** proved in repository through finite case classification.

**Certainty:** medium.

**Audit state:** awaiting independent symbolic review; some finite examples are computationally verified.

**Statement.** Let

```math
S\subseteq[R,2R)
```

be a coordinated side shell and `T` a paired middle subset. Then

```math
\boxed{
|A(S)\cup M_q(T)|
+
R H(T\cap[1,R))
\ge
2+
\frac43(|S|+|T|)-\eta,
}
```

where `0<=eta<=2` records anchor coincidences.

**Consequence.** Efficient local overlap exports capacity to lower scale. This is supporting theory, not the closing global multiplicity theorem.

**Primary notes:**

- `docs/full-component-scale-export.md`
- `docs/unequal-cardinality-scale-compensated-packing.md`

---

# Explicitly false or superseded targets

## FL-001: Uniformly bounded depth-two affine-lift overlap

**Status:** false.

**Certainty:** high; explicit finite-avoidance construction.

A fixed root point and terminal direction can support arbitrarily many depth-two affine lifts in a four-term-progression-free set.

**Primary note:** `docs/depth-two-overlap-counterexample.md`.

---

## FL-002: Universal uncorrected local `8/3` packing

**Status:** false.

**Certainty:** high; explicit computationally checkable example.

A coordinated four-term-progression-free example has

```math
|S|=|T|=45,
\qquad
|A(S)\cup M_q(T)|=107<120.
```

The corrected theorem requires lower-scale credit.

**Primary note:** `docs/seven-thirds-local-packing-counterexample.md`.

---

## FL-003: Naive recursive density increment

**Status:** false as a general mechanism.

**Certainty:** high internally.

Passing to predecessor children does not automatically increase normalized density.

---

## FL-004: Fixed-size sampling creates off-diagonal discrepancy

**Status:** false.

**Certainty:** high internally.

After correcting for the missing diagonal, fixed-size sampling preserves the off-diagonal discrepancy in expectation.

**Primary note:** `docs/offdiagonal-correction-direction-energy.md`.

---

## SP-001: Binary factor `7/6`

**Status:** valid but superseded as the best quantitative bound.

The earlier merge-plus-middle thinning gives

```math
\frac76H(D)-\frac53\frac{r_3(N)}N.
```

CL-010 improves the binary occurrence factor to

```math
\frac43H(D)-\frac43\frac{r_3(N)}N.
```

---

# Open bottleneck OB-001: Multiplicity versus scale

The active recursion controls

```math
\sum_d\frac{m(d)}d,
```

where `m(d)` is occurrence multiplicity. Erdős Problem #3 concerns

```math
\sum_{d:m(d)>0}\frac1d.
```

No current theorem converts binary `4/3` occurrence branching into supercritical distinct harmonic growth.

The approved closing targets are:

1. a weighted multiplicity rate strictly below `4/3`;
2. a bounded multiscale potential;
3. structural control of triple-loaded sponsors;
4. scalable multigeneration falsification experiments.

A one-generation high-multiplicity example is insufficient if it terminates immediately or exports much smaller labels that compensate its overlap.

The full Erdős problem remains unresolved.
