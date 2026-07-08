# Erdős Problem #3: reciprocal-sum AP proof ledger

This repository contains a concrete proof-audit and computation program around Erdős Problem #3:

> If `A ⊆ N` and `∑_{n∈A} 1/n = ∞`, must `A` contain arbitrarily long arithmetic progressions?

The full problem is open. The repository keeps a permanent ledger of reliable partial results, verified computations, failed routes, and active bottlenecks so progress is not lost across long research sessions.

## Current main target

For fixed `k >= 4`, the current high-certainty reduction is:

```math
\text{fixed-}k\text{ reciprocal-sum problem}
\quad\Longleftrightarrow\quad
\sum_{j\ge 1}\frac{r_k(2^j)}{2^j}<\infty,
```

where `r_k(N)` is the largest size of a `k`-AP-free subset of `[1,N]`.

For `k=4`, a sufficient concrete target is

```math
r_4(N) \ll \frac{N}{(\log N)^{1+\epsilon}}
```

for some `epsilon>0`, or any dyadically summable alternative such as

```math
r_4(N)/N \ll 1/((\log N)(\log\log N)^{1+\epsilon}).
```

Cross-block arithmetic constraints remain useful inside structured model classes, but they are no longer the universal missing ingredient for fixed `k>=4`: if the dyadic extremal series diverges, extremal AP-free blocks can be placed on widely separated dyadic scales to preserve divergent reciprocal mass while eliminating cross-block APs.

## Certainty ledger

The file

```text
docs/certainty-ledger.md
```

records claims that are safe to rely on.  Current high-certainty entries include:

- base-`b` automatic sets cannot be divergent reciprocal-sum counterexamples;
- any AP-free divergent candidate must be sparse in every fixed-ratio interval;
- positive logarithmic reciprocal density is enough to force APs;
- exact dilation triples `d,2d,3d` are not forced by divergent harmonic mass;
- for fixed `k>=4`, the problem is equivalent to dyadic summability of `r_k(2^j)/2^j`;
- the Walker base-55 local-rigidity computation in the cyclic digit-template model.

## Active proof-audit tracks

The main mathematical track is the `k=4` quantitative extremal problem.  The branch currently emphasizes:

1. Green--Tao architecture audit: identify exactly where localization/refinement losses prevent a summable `r_4` bound.
2. Minimal-critical finite-field model: reduce a hypothetical obstruction to a hyperplane-flat object with a signed 4AP deficit.
3. Trilinear branch: currently gives only an `alpha^2` increment, the logarithmic-barrier scale.
4. Pure `U^3` / four-balanced branch: needs a one-sided structural theorem stronger than generic inverse machinery.
5. Quadratic rank split: low-rank correlation must give a cheap affine increment; high-rank correlation needs a relative recurrence theorem on quadratic level sets.

The finite-state/DFA material is a publishable side track, not the main proof route.  It certifies that fixed regular digit languages cannot produce divergent reciprocal-sum AP-free counterexamples and supplies reproducible benchmark machinery.

## Contents

- `docs/certainty-ledger.md` — durable ledger of proved results, verified computations, and bottlenecks.
- `docs/dyadic-summability-equivalence.md` — proof that fixed `k>=4` is equivalent to dyadic summability.
- `docs/r4-bound-roadmap.md` — concrete `k=4` summability target and current bound gap.
- `docs/r4-finite-cost-target.md` — finite theorem and density-increment cost formulation.
- `docs/gt31-alpha4-error-budget.md` — recurrence error budget forcing `eta ~ alpha^4`.
- `docs/r4-replacement-architecture-spec.md` — replacement architecture requirements for beating the GT-style barrier.
- `docs/minimal-critical-dichotomy.md` — trilinear versus pure `U^3` obstruction split under minimality.
- `docs/low-rank-quadratic-minimality-threshold.md` — rank/increment threshold for low-rank quadratic structure.
- `docs/high-rank-relative-recurrence-target.md` — recurrence target for high-rank quadratic level sets.
- `docs/high-rank-escape-increment-threshold.md` — increment-size threshold for the high-rank escape branch.
- `docs/finite-state-paper-audit.md` — finite-state obstruction paper framing and limits.
- `docs/harmonic-search-status.md` — harmonic-aware scoring gate and Walker local rigidity result.
- `docs/pb-solver-workflow.md` — end-to-end PB/MaxSAT workflow for cyclic digit templates.
- `docs/regular-language-certifier.md` — DFA model, AP certificate, examples, and next search target.
- `docs/dfa-growth-triage.md` — DFA growth exponent and truncated shifted harmonic triage.
- `src/modular_kempner_search.py` — branch-and-bound search for modular 4-free digit sets.
- `src/periodic_digit_ap.py` — finite automaton checker for one periodic digit system.
- `src/periodic_exhaustive_search.py` — exact period-2 threshold search engine.
- `src/periodic_stochastic_search.py` — stochastic witness-guided periodic search with exact certification.
- `src/benchmark_report.py` — validates public benchmark metadata and modular certificates.
- `src/shifted_kempner_sum.py` — scores shifted Kempner harmonic sums `K(D,b)+1`.
- `src/candidate_score.py` — certifies and scores a single proposed one-layer candidate.
- `src/cyclic_neighborhood_scan.py` — scans fixed-size digit-substitution neighborhoods.
- `src/cyclic_pb_encoder.py` — emits OPB pseudo-Boolean models for cyclic AP-free templates.
- `src/score_pb_solution.py` — parses external PB/MaxSAT assignments, re-certifies, and scores them.
- `src/pb_experiment_matrix.py` — generates reproducible PB/MaxSAT experiment matrices.
- `src/dfa_ap_cert.py` — exact 4-AP certifier for LSD-first regular digit languages.
- `src/dfa_growth_score.py` — growth-rate and truncated shifted-harmonic triage for DFA languages.
- `src/random_dfa_search.py` — random small-DFA candidate generator with exact AP certification.
- `src/dfa_canonicalize.py` — DFA minimization/canonicalization and SHA256 signatures.
- `examples/dfa/base11_digit_set.json` — two-state DFA encoding Walker's base-11 digit set.
- `examples/dfa/all_digits_base3.json` — positive-control DFA that contains 4-APs.
- `data/public_benchmarks.csv` — known public benchmarks and provenance links.
- `data/benchmark_scores_2026-07-07.csv` — reproduction of Walker's public k=4 shifted sums.
- `data/walker55_neighborhood_scan_2026-07-07.csv` — radius-1/2 neighborhood scan of Walker's base-55 set.
- `data/pb_experiment_matrix_2026-07-07.csv` — focused PB experiment commands around Walker-scale bases.
- `data/small_base_run_2026-07-07.csv` — first reproducible small-base modular run.
- `data/period2_threshold_run_2026-07-07.csv` — exhaustive period-2 threshold run for bases 11–13.
- `data/stochastic_periodic_run_2026-07-07.csv` — first period-2/3 stochastic high-water-mark run.

## Reproduce first modular run

```bash
python src/modular_kempner_search.py --verify-known --b-min 5 --b-max 34 --topn 1 \
  --csv data/small_base_run.csv
```

## Check Walker's base-11 set

```bash
python src/modular_kempner_search.py --verify-known --b-min 11 --b-max 11 --topn 1
```

## Test period-2 local augmentation of the base-11 set

```bash
python src/periodic_digit_ap.py \
  --base 11 \
  --digits "0,1,2,4,5,7" \
  --local-augment
```

Expected first observation: no one-digit period-2 augmentation of `{0,1,2,4,5,7}` preserves 4-AP-freeness under the automaton certificate.
