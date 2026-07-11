# Erdős Problem #3: harmonic arithmetic progressions

This repository develops a partial-progress attack on Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open.

The active program studies four-term-progression-free sets through a multiscale **side-anchor deletion DAG**. The main current objective is to convert supercritical harmonic growth of descendant occurrences into growth of distinct integers, or to prove that repeated scale contraction must terminate.

## Start here

- `docs/current-proof-program.md` — authoritative theorem chain, dependency graph, false targets, and closing gaps.
- `docs/certainty-ledger.md` — claims classified by status and confidence.
- `docs/deletion-dag-merge-difference-recursion.md` — exact indegree-excess identity and lower-scale merge children.
- `docs/deletion-dag-root-depth-dichotomy.md` — root-rich harmonic gain versus long valuation-directed paths.
- `docs/side-anchor-deletion-dag.md` — construction of the affine deletion DAG.

## Active theorem chain

For a four-term-progression-free block

```math
D\subseteq[N,2N),
```

run side-anchor deletion until a three-term-progression-free residual of size `s<=r_3(N)` remains.

The selected progressions define an acyclic graph in which every deleted sponsor points to the two surviving points of its selected three-term progression.

If `K=|D|-s` and `rho` is the number of indegree-zero vertices, then the exact indegree excess is

```math
\boxed{
M
=
\sum_v\max\{d^-(v)-1,0\}
=
K-s+\rho.
}
```

For each target vertex `v`, translating its incoming sponsors by the smallest sponsor produces a four-term-progression-free lower-scale child `Delta_v subseteq [1,N)`. These children satisfy

```math
\boxed{
\sum_vH(\Delta_v)
\ge
H(D)-2\frac{r_3(N)}N.
}
```

Combining them with selected coordinated middle children gives occurrence-level branching

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

After binary thinning, every sponsor creates at most two child occurrences while retaining

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

These inequalities count harmonic mass **with multiplicity**. The central unsolved step is to control repeated numerical labels and rapid scale contraction.

## Current dichotomy

Let `rho` be the number of roots of the deletion DAG.

- If `rho` is a positive proportion of `|D|`, the merge-difference recursion has a strict harmonic gain.
- If roots are sparse, the DAG contains a long path whose increments have the form

  ```math
  x_{j+1}-x_j
  =
  \sigma(q_j)c_jq_j,
  \qquad c_j\in\{1,2\},
  ```

  where the direction `sigma(q_j)` is determined by `v_2(q_j) mod 2`.

A closing theorem must control weighted multiplicity, construct a bounded multiscale potential, or show that root-poor valuation-directed paths cannot persist.

## Research discipline

The project previously generated many overlapping theorem notes. The current policy is:

- no new broad proof language unless it proves or falsifies an explicit closing target in `docs/current-proof-program.md`;
- recent exact lemmas are marked as proved in the repository but awaiting independent audit;
- counterexamples and superseded routes remain documented so false approaches are not revived;
- the README and certainty ledger are the authoritative entry points.

## Supporting local packing results

The coordinated side-middle analysis proves a scale-compensated inequality. For a side shell `S subseteq [R,2R)` and a paired middle subset `T`,

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

This explains why efficient local overlap exports harmonic potential to a lower scale. It is currently a supporting ingredient rather than the shortest active proof chain.

Primary notes:

- `docs/full-component-scale-export.md`
- `docs/unequal-cardinality-scale-compensated-packing.md`
- `docs/seven-thirds-local-packing-counterexample.md`

## Explicitly falsified targets

The repository contains exact counterexamples or corrections showing that the following statements cannot be used as originally proposed:

- uniformly bounded depth-two affine-lift overlap;
- universal uncorrected local `8/3` side-middle packing;
- naive recursive density increment;
- creation of genuine off-diagonal discrepancy by fixed-size sampling.

See `docs/current-proof-program.md` for the precise classification.

## Earlier computational program

The repository also contains PB/MaxSAT, modular digit-set, shifted Kempner, and DFA search tools. These remain useful for finite extremizer exploration and reproducible computation, but automatic or regular-language constructions cannot produce a divergent reciprocal-sum counterexample.

Relevant directories and files include:

- `src/modular_kempner_search.py`
- `src/cyclic_pb_encoder.py`
- `src/dfa_ap_cert.py`
- `src/dfa_growth_score.py`
- `data/public_benchmarks.csv`
- `examples/dfa/`

These tools are now classified as legacy/supporting rather than the active route to the full problem.

## Verification status

The repository distinguishes:

- standard or literature-dependent reductions;
- symbolic proofs developed in the repository;
- computationally verified finite claims;
- conjectural targets;
- explicitly false statements.

No recent deletion-DAG theorem has yet received independent expert review. The full Erdős problem remains unresolved.
