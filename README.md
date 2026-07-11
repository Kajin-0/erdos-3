# Erdős Problem #3: harmonic arithmetic progressions

This repository develops a partial-progress attack on Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open.

The active program studies four-term-progression-free sets using a multiscale **side-anchor deletion DAG**. The current best internal theorem constructs a binary genealogy of lower-scale four-term-progression-free child occurrences with harmonic branching factor `8/3`. The central unresolved step is converting occurrence mass into harmonic mass of distinct integers.

## Start here

- `docs/current-proof-program.md` — authoritative theorem chain, dependency graph, false targets, and closing gaps.
- `docs/certainty-ledger.md` — claims classified by status, confidence, and audit state.
- `docs/full-middle-binary-eight-thirds-recursion.md` — current best binary occurrence theorem.
- `docs/spanning-forest-binary-four-thirds-recursion.md` — structural balance used by the current theorem.
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

Translating incoming sponsors at each target gives lower-scale four-term-progression-free children `Delta_v` with

```math
\sum_v|\Delta_v|=K-s+\rho.
```

### Spanning-forest children

Choose one incoming edge for every nonroot DAG vertex. Translating each forest component by its smallest element gives lower-scale four-term-progression-free children `Theta_j` with

```math
\sum_j|\Theta_j|=K+s-\rho.
```

Thus the two structural families satisfy

```math
\boxed{
\sum_v|\Delta_v|
+
\sum_j|\Theta_j|
=2K.
}
```

After retaining at most one structural occurrence per parent element, at least `2K/3` structural occurrences remain.

### Full middle children

For every selected progression with center `x` and step `q`, place `q` in

```math
M_x=\{q_i:b_i=x\}.
```

Each `M_x` is four-term-progression-free: a four-term progression among its steps would give one among the points `x+q` in `D`.

Every selected step satisfies `q<=N/2`, so

```math
\boxed{
\sum_xH(M_x)
\ge
\frac{2K}{N}.
}
```

No valuation-color restriction is needed in this deletion-DAG recursion.

### Binary eight-thirds theorem

Retain every middle occurrence and at most one structural occurrence per parent. Every deleted sponsor produces at most two children: one middle and one structural. Every residual parent produces at most one structural child.

Therefore

```math
\boxed{
\sum H(\text{binary child occurrences})
\ge
\frac83H(D)
-
\frac83\frac{r_3(N)}N.
}
```

This supersedes the earlier binary factors `7/6`, `4/3`, and `16/9`.

## Central gap

The theorem controls

```math
\sum_d\frac{m(d)}d,
```

where `m(d)` counts occurrences of numerical label `d`.

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

The approved closing targets are:

1. a weighted multiplicity rate strictly below `8/3`;
2. a bounded multiscale potential;
3. an energy bound for repeated numerical labels across child states;
4. a stopping theorem for repeated rapid contraction.

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