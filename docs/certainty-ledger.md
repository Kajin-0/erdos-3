# Certainty ledger

This file records claims that should survive chat-context loss. Each entry separates:

- **status**: standard / proved in repository / computationally verified / conjectural / false / open bottleneck;
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

**Statement.** Fix `b>=2`. If `A subseteq N` is base-`b` automatic and

```math
\sum_{n\in A}\frac1n=\infty,
```

then `A` has positive upper asymptotic density and therefore contains arithmetic progressions of every finite length.

**Consequence.** No fixed finite automaton, regular digit language, or automatic-set construction can produce a divergent reciprocal-sum counterexample.

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

**Consequence.** The hard case is slowly divergent logarithmic-scale dust, not persistent dense blocks.

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

**Consequence.** Known general `r_k(N)` bounds for `k>=4` are insufficient; a successful proof likely needs cross-scale arithmetic information.

---

## CL-004: Walker base-55 benchmark is locally rigid in the implemented model

**Status:** computationally verified.

**Certainty:** high for the finite computation; no global optimality claim.

**Audit state:** reproducible within the repository.

**Statement.** Walker's public base-55 shifted Kempner digit set has no AP-free same-size digit-substitution neighbor at radius one or two in the repository's cyclic modular model.

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

with `a_i` deleted, the directed edges

```math
a_i\to b_i,
\qquad
a_i\to c_i
```

form an acyclic graph. Every deleted vertex has outdegree two; every residual vertex has outdegree zero.

If `K` vertices are deleted and `s` remain, then

```math
K=|D|-s,
\qquad
s\le r_3(N).
```

**Dependencies:** side-anchor deletion rule; deletion-time ordering; Roth residual bound.

**Consequence.** The overlap problem can be studied through a concrete geometric DAG rather than an abstract role tree.

**Primary note:** `docs/side-anchor-deletion-dag.md`.

---

## CL-007: Exact indegree excess and merge-difference children

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** central claim awaiting independent review.

**Statement.** Let `rho` be the number of indegree-zero vertices of the deletion DAG. Then

```math
\boxed{
M
=
\sum_v\max\{d^-(v)-1,0\}
=
K-s+\rho.
}
```

For each vertex `v`, let `I_v` be its incoming sponsors, choose `p_v=min I_v`, and define

```math
\Delta_v
=
\{a-p_v:a\in I_v,\ a>p_v\}.
```

Then:

```math
\Delta_v\subseteq[1,N),
```

`Delta_v` is four-term-progression-free, and

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

**Dependencies:** CL-006.

**Consequence.** Indegree merging generates a canonical family of lower-scale four-term-progression-free children preserving parent harmonic mass with multiplicity.

**Primary note:** `docs/deletion-dag-merge-difference-recursion.md`.

---

## CL-008: Merge-plus-middle occurrence branching

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

**Statement.** Selecting the heaviest color of

```math
\chi(q)=v_2(q)-v_3(q)\pmod3
```

produces middle children `M_x^*` satisfying

```math
\sum_xH(M_x^*)\ge\frac{2K}{3N}.
```

Together with CL-007,

```math
\boxed{
\sum_vH(\Delta_v)
+
\sum_xH(M_x^*)
\ge
\frac53H(D)
-
\frac83\frac{r_3(N)}N.
}
```

After retaining at most one merge occurrence per sponsor,

```math
\boxed{
\sum_vH(\Delta_v')
+
\sum_xH(M_x^*)
\ge
\frac76H(D)
-
\frac53\frac{r_3(N)}N.
}
```

and each sponsor generates at most two child occurrences.

**Critical caveat.** These are occurrence-multiset inequalities. They do not establish growth in the harmonic mass of distinct integers.

**Dependencies:** CL-006 and CL-007.

**Consequence.** A canonical binary occurrence genealogy has a supercritical harmonic lower bound, but multiplicity and scale contraction remain uncontrolled.

**Primary note:** `docs/deletion-dag-merge-difference-recursion.md`.

---

## CL-009: Root-rich versus long-path dichotomy

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

**Statement.** If the deletion DAG has

```math
\rho\ge\delta|D|,
```

then

```math
\boxed{
\sum_vH(\Delta_v)
\ge
(1+\delta)H(D)
-
2\frac{r_3(N)}N.
}
```

If roots are sparse, the maximum directed path length satisfies

```math
\boxed{
L
\ge
\left\lceil
\log_2\left(\frac{|D|}{\rho}+1\right)
\right\rceil-1.
}
```

Along such a path,

```math
x_{j+1}-x_j
=
\sigma(q_j)c_jq_j,
\qquad
c_j\in\{1,2\},
```

where the sign `sigma(q_j)` is determined by `v_2(q_j) mod 2`.

**Dependencies:** CL-006 and CL-007.

**Consequence.** Near-critical merge recursion can occur only in root-poor DAGs containing long valuation-directed affine paths.

**Primary note:** `docs/deletion-dag-root-depth-dichotomy.md`.

---

## CL-010: Componentwise scale-compensated side-middle packing

**Status:** proved in repository through finite case classification.

**Certainty:** medium.

**Audit state:** awaiting independent symbolic review; some finite examples are computationally verified.

**Statement.** Let

```math
S\subseteq[R,2R)
```

be a coordinated side shell and `T` an arbitrary subset of its paired middle child. Then

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

If `T subseteq [R,2R)`, the lower-scale correction vanishes.

**Dependencies:** coordinated valuation compression; full intersection forest; finite component classification.

**Consequence.** Efficient local overlap cannot destroy the relevant capacity; it exports it to lower scale. This is supporting theory, not yet the closing global multiplicity theorem.

**Primary notes:**

- `docs/full-component-scale-export.md`
- `docs/unequal-cardinality-scale-compensated-packing.md`

---

## CL-011: Sponsored sparse recursion removes global child matching

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

**Statement.** The deletion proof can select at least

```math
|D|-r_3(N)
```

three-term progressions with distinct sponsor elements. Each sponsor creates exactly one side occurrence and at most one selected middle occurrence.

**Consequence.** The global child-state matching problem can be replaced by a canonical occurrence-level binary sponsorship map.

**Caveat.** This does not solve multiplicity; labels can contract rapidly.

**Primary note:** `docs/sponsored-three-ap-binary-recursion.md`.

---

# Explicitly false or superseded targets

## FL-001: Uniformly bounded depth-two affine-lift overlap

**Status:** false.

**Certainty:** high; explicit finite-avoidance construction.

**Statement ruled out.** A fixed root point and terminal direction do not support only boundedly many depth-two affine lifts in a four-term-progression-free set.

**Primary note:** `docs/depth-two-overlap-counterexample.md`.

---

## FL-002: Universal uncorrected local `8/3` packing

**Status:** false.

**Certainty:** high; explicit computationally checkable example.

**Statement ruled out.** One cannot universally prove

```math
|A(S)\cup M_q(T)|\ge\frac83|S|-O(1)
```

without a lower-scale correction.

A coordinated four-term-progression-free example has

```math
|S|=|T|=45,
\qquad
|A(S)\cup M_q(T)|=107<120.
```

**Primary note:** `docs/seven-thirds-local-packing-counterexample.md`.

---

## FL-003: Naive recursive density increment

**Status:** false as a general mechanism in the inherited three-dilate class.

**Certainty:** high internally.

**Statement ruled out.** Passing to predecessor children does not automatically increase normalized density; disjoint affine copies give a nonincrease bound.

**Primary note:** `docs/affine-tree-multiplicity-lower-bound.md`.

---

## FL-004: Fixed-size sampling creates genuine off-diagonal discrepancy

**Status:** false.

**Certainty:** high internally.

**Statement ruled out.** Fixed-size sampling scales the corrected off-diagonal discrepancy by the expected combinatorial factor; it does not create or amplify it.

**Primary note:** `docs/offdiagonal-correction-direction-energy.md`.

---

# Open bottlenecks

## OB-001: Cross-block arithmetic constraints

**Status:** broad original bottleneck; retained but refined.

A divergent AP-free candidate would satisfy

```math
\alpha_j\to0,
\qquad
\sum_j\alpha_j=\infty.
```

Independent blockwise extremal estimates are insufficient.

**Refinement:** OB-002 is the current precise form pursued by the deletion-DAG program.

---

## OB-002: Multiplicity versus scale contraction

**Status:** authoritative current bottleneck.

The project controls occurrence harmonic mass

```math
\sum_d\frac{m(d)}d
```

but the original set problem concerns distinct mass

```math
\sum_{d:m(d)>0}\frac1d.
```

The missing theorem must jointly control:

```math
\boxed{
\text{multiplicity},
\quad
\text{scale contraction},
\quad
\text{valuation-directed path geometry}.
}
```

Acceptable closing results include:

1. a weighted multiplicity inequality beating the binary factor `7/6`;
2. a bounded multiscale potential that grows under recursion;
3. a stopping theorem showing root-poor valuation-directed paths cannot persist;
4. a computationally discovered scalable family falsifying the route.

No current result closes OB-002.

---

# Repository policy

A new theorem note should be added only if it:

1. proves or falsifies a stated closing target in `docs/current-proof-program.md`;
2. repairs a concrete dependency gap;
3. supplies a reproducible counterexample;
4. consolidates or independently audits an existing claim.

Recent deletion-DAG claims are safe to use as **internal lemmas under review**, not as established literature results or a solution of Erdős Problem #3.
