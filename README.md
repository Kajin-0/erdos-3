# Erdős Problem #3: harmonic arithmetic progressions

This repository develops a partial-progress attack on Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open.

The active program studies four-term-progression-free sets using a multiscale **side-anchor deletion DAG**. The current best theorem constructs a binary genealogy of lower-scale four-term-progression-free child occurrences with harmonic branching factor `16/9`. The central unresolved step is converting occurrence mass into harmonic mass of distinct integers.

## Start here

- `docs/current-proof-program.md` — authoritative theorem chain, dependency graph, false targets, and closing gaps.
- `docs/certainty-ledger.md` — claims classified by status, confidence, and audit state.
- `docs/color-aware-binary-sixteen-ninths-recursion.md` — current best binary occurrence theorem.
- `docs/spanning-forest-binary-four-thirds-recursion.md` — superseded intermediate binary theorem.
- `docs/deletion-dag-merge-difference-recursion.md` — indegree excess and merge-difference children.
- `docs/side-anchor-deletion-dag.md` — affine deletion-DAG construction.

## Active theorem chain

For a four-term-progression-free block

```math
D\subseteq[N,2N),
```

run side-anchor deletion until a three-term-progression-free residual of size

```math
s\le r_3(N)
```

remains. Put

```math
K=|D|-s.
```

The selected progressions define an acyclic graph in which every deleted sponsor points to the two surviving points of its selected three-term progression.

### Merge-difference children

If `rho` is the number of indegree-zero vertices, the exact indegree excess is

```math
\boxed{
M
=
\sum_v\max\{d^-(v)-1,0\}
=
K-s+\rho.
}
```

Translating the incoming sponsors at each target gives lower-scale four-term-progression-free children `Delta_v` with

```math
\sum_v|\Delta_v|=K-s+\rho.
```

### Spanning-forest children

Choose one incoming edge for every nonroot DAG vertex. Translating each resulting forest component by its smallest element gives lower-scale four-term-progression-free children `Theta_j` with

```math
\sum_j|\Theta_j|=K+s-\rho.
```

The two structural families therefore satisfy the exact balance

```math
\boxed{
\sum_v|\Delta_v|
+
\sum_j|\Theta_j|
=2K.
}
```

### Color-aware binary thinning

For each deleted sponsor, let `ell(a) in {0,1,2,3}` be the number of associated structural occurrences. Choose the middle color jointly with the structural allocation:

- sponsors in the chosen middle color retain their middle occurrence and at most one structural occurrence;
- sponsors outside the chosen color retain at most two structural occurrences;
- residual parents retain their structural occurrence.

Every parent element creates at most two retained child occurrences. Averaging over the three middle colors gives

```math
\boxed{
\sum H(\text{binary child occurrences})
\ge
\frac{16}{9}H(D)
-
\frac{16}{9}\frac{r_3(N)}N.
}
```

This supersedes the previous binary factors `7/6` and `4/3`.

## Central gap

The theorem controls

```math
\sum_d\frac{m(d)}d,
```

where `m(d)` counts occurrences of the numerical label `d`.

The original problem concerns

```math
\sum_{d:m(d)>0}\frac1d.
```

The unresolved task is to control

```math
\boxed{
\text{multiplicity},
\quad
\text{scale contraction},
\quad
\text{genealogical overlap}.
}
```

The current approved closing targets are:

1. a weighted multiplicity rate strictly below `16/9`;
2. a bounded multiscale potential;
3. structural exclusion of the abstract extremal load pattern `ell=0` on one third of sponsors and `ell=3` on two thirds;
4. scalable computational counterexamples that persist over multiple generations.

## Supporting results

The repository also contains:

- a root-rich versus long valuation-directed path dichotomy;
- componentwise scale-compensated side-middle packing;
- exact counterexamples to bounded affine-lift overlap;
- an exact counterexample to uncorrected local `8/3` packing;
- popular-direction, high-interaction, and affine-tree supporting lemmas.

See `docs/current-proof-program.md` for dependency and status classification.

## Research discipline

The active policy is:

- no new broad proof language unless it proves or falsifies an explicit closing target;
- recent theorem-style lemmas are marked as proved in the repository but awaiting independent audit;
- counterexamples and superseded routes remain documented;
- occurrence mass and distinct mass must be reported separately.

## Earlier computational program

The repository also contains PB/MaxSAT, modular digit-set, shifted Kempner, and DFA search tools. These remain useful for finite extremizer exploration and reproducible computation, but finite-state constructions cannot produce a divergent reciprocal-sum counterexample.

Relevant files include:

- `src/modular_kempner_search.py`
- `src/cyclic_pb_encoder.py`
- `src/dfa_ap_cert.py`
- `src/dfa_growth_score.py`
- `data/public_benchmarks.csv`
- `examples/dfa/`

These tools are supporting or legacy work rather than the active route to the full problem.

## Verification status

The repository distinguishes:

- standard or literature-dependent reductions;
- symbolic proofs developed in the repository;
- computationally verified finite claims;
- conjectural closing targets;
- explicitly false statements.

No recent deletion-DAG theorem has yet received independent expert review. The full Erdős problem remains unresolved.