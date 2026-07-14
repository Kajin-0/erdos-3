# Erdős Problem #3: the four-term reciprocal-sum case

This repository develops computer-assisted and symbolic partial progress on Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. The active project studies the four-term case: whether every four-term-progression-free subset of the positive integers has convergent reciprocal sum.

## Current status

The repository has established:

1. strong one-generation harmonic recursions from coordinated side-anchor deletion;
2. exact middle-multiplicity resolution and mandatory dyadic shelling;
3. an infinite self-replicating four-AP-free scale-eight family with persistence
   ```math
   P_h=2^h=\frac12L_h^{1/3};
   ```
4. a sharp summability theorem for the exact equal-translate replication model;
5. contaminated constructions disproving universal local and fixed-window contraction;
6. an exact Bellman debt identity for cheap replication;
7. complete factor-two and factor-four exclusion from the recorded state `S_10`;
8. a complete infinite exact-tail classification for every valid factor-eight child of `S_10`;
9. exact raw simultaneous deletion transitions through `S_7`;
10. exact no-go theorems for several naive packing potentials and SCC capacities;
11. a policy-aware exact rational LP over a full five-step subset lattice through `S_7`.

The strongest state-specific closure is

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

The factor-four proof partitions all `348012826` layer-disjoint candidates into inherited obstruction, lifted completion support, and rectangle-transport classes.

This closes the recorded depth-ten state, not the full deletion tree.

## Active theorem

The decisive missing object is a provenance-preserving retention quotient converting raw overlapping simultaneous outputs into legitimate Bellman children.

The intended whole-tree inequality is schematically

```math
\Delta(S)
+
\sum_{S'\in\mathrm{Child}_\pi(S)}
\left(
\mathrm{Pack}(S')+\Phi_{\rm obs}(S')
\right)
\le
\mathrm{Pack}(S)+\Phi_{\rm obs}(S)
+
\mathrm{controlled\ error}.
```

A valid theorem must handle:

- duplicate states;
- strict containments;
- partial overlaps;
- terminal-recursive overlap;
- cyclic terminal-fiber incidence;
- policy-dependent regeneration;
- cross-generation provenance reuse.

Pathwise summability, replay catalogs, and policy-ranking LP feasibility do not by themselves imply this treewise inequality.

## Start here

- [`docs/comprehensive-research-landscape.md`](docs/comprehensive-research-landscape.md) — expert strategic map of positive results, negative theorems, explored model classes, dependency graph, stop list, and prioritized roadmap.
- [`docs/current-proof-program.md`](docs/current-proof-program.md) — authoritative active theorem chain and immediate frontier.
- [`docs/certainty-ledger.md`](docs/certainty-ledger.md) — atomic claim status and exact theorem/certificate ledger.
- [`docs/research-decision-history.md`](docs/research-decision-history.md) — chronological decisions and permanent stops.
- [`docs/branching-reserve-lp.md`](docs/branching-reserve-lp.md) — exact retained-child LP contract and current packing requirements.

## Main completed theorem families

### One-generation deletion recursion

For a four-AP-free block `D subseteq [N,2N)`, coordinated deletion and the minimum-translation backbone give

```math
H(\mathcal B(D))+\sum_xH(M_x)
\ge
3H(D)-2\frac{r_3(N)}N-\frac1N,
```

and, after exact middle-multiplicity resolution,

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

Primary references:

- [`docs/minimum-translation-backbone-recursion.md`](docs/minimum-translation-backbone-recursion.md)
- [`docs/middle-multiplicity-fiber-five-thirds-recursion.md`](docs/middle-multiplicity-fiber-five-thirds-recursion.md)

### Exact scale-eight benchmark

The aligned-diamond family satisfies

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h,
\qquad
L_h=8^{h+1}.
```

A 34-state base-eight automaton and a 17,238-state carry-product certificate prove that the infinite family is four-AP-free.

Primary references:

- [`docs/scale-eight-self-replicating-aligned-diamond.md`](docs/scale-eight-self-replicating-aligned-diamond.md)
- [`src/verify_scale_eight_aligned_diamond.py`](src/verify_scale_eight_aligned_diamond.py)

### Sharp exact-model summability

Exact uncontaminated equal-translate reproduction requires

```math
L'\ge8L.
```

The exact model has one-step efficiency `3/4` and summable multiplicity-weighted density.

Primary references:

- [`docs/three-translate-dyadic-scale-barrier.md`](docs/three-translate-dyadic-scale-barrier.md)
- [`docs/exact-three-translate-weighted-density-theorem.md`](docs/exact-three-translate-weighted-density-theorem.md)

### Contaminated debt and delayed recovery

The certified contaminated branch begins

```text
4,8,4,4,8,4,8,8,8
```

and disproves universal one-step contraction, fixed short-window contraction, and universal two-generation recovery.

The exact debt accounting is

```math
\Delta_c
=
\frac{P(3N+4)}L\left(\frac8c-1\right).
```

Primary references:

- [`docs/contaminated-backbone-depth-five-chain.md`](docs/contaminated-backbone-depth-five-chain.md)
- [`docs/current-proof-program.md`](docs/current-proof-program.md)

### Complete depth-ten cheap-extension closure

The complete factor-four domain from `S_10` is eliminated by:

1. inherited depth-nine obstruction;
2. lifted completion support;
3. complete direct rectangle support;
4. exact transport at ratios `1,2,3,4`.

Primary references:

- [`docs/complete-depth-ten-factor-four-exclusion.md`](docs/complete-depth-ten-factor-four-exclusion.md)
- [`docs/four-ratio-rectangle-transport-and-residual-profile.md`](docs/four-ratio-rectangle-transport-and-residual-profile.md)
- [`src/run_verify_s10_factor4_rectangle_closure.sh`](src/run_verify_s10_factor4_rectangle_closure.sh)

### Simultaneous transition and policy frontier

Raw simultaneous deletion output is exported through `S_7`, including duplicates, containments, partial overlaps, provenance, and terminal-fiber SCC structure.

The current finite policy score is

```math
C_{\lambda,\gamma}(\pi)
=
T_\pi+\lambda O_\pi+E_\pi+\gamma G_\pi.
```

The witness

```math
(\lambda,\gamma)=\left(3,\frac1{10}\right)
```

remains feasible across `250` exact rational constraints after full five-step subset expansion through `S_7`. Policy winners change under family enlargement, so this is a finite ranking theorem rather than a canonical-policy theorem. It is not yet a retained-child Bellman theorem.

Primary references:

- [`docs/simultaneous-deletion-transition-exporter.md`](docs/simultaneous-deletion-transition-exporter.md)
- [`docs/terminal-fiber-scc-spectral-growth.md`](docs/terminal-fiber-scc-spectral-growth.md)
- [`docs/policy-subset-lattice-s1-s7.md`](docs/policy-subset-lattice-s1-s7.md)
- [`docs/branching-reserve-lp.md`](docs/branching-reserve-lp.md)

## Reproduction

Lightweight push-gating suite:

```bash
bash src/run_verify_ci_lightweight.sh
```

Extended transport and reserve suite:

```bash
bash src/run_verify_transport_reserve.sh
```

Transition and policy frontier:

```bash
bash src/run_verify_transition_frontier.sh
```

## Claim discipline

The repository distinguishes:

- symbolic theorems;
- exact finite computer-assisted theorems;
- exact infinite theorems from finite certification plus induction;
- no-go theorems;
- experimental evidence;
- conjectures;
- superseded claims.

See [`docs/certainty-ledger.md`](docs/certainty-ledger.md) for authoritative status. The full four-term reciprocal-sum problem remains unresolved.
