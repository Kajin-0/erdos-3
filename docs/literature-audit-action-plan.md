# Literature audit action plan

## What the audit changes

The audit makes one conclusion operationally important:

> Do not spend more time on naive modular digit-set search or blind stochastic deletion/rebuild.

Alexander Walker's public work already covers the most obvious version of that direction:
branch-and-bound search over digit/remainder templates, Baillie-Schmelzer harmonic
post-processing, and published `k=4` shifted Kempner benchmarks.  The best public `k=4`
benchmark identified in the audit is the base-55 shifted Kempner set with harmonic sum
`4.43975`.

The repository should therefore pivot toward solver and model classes that are adjacent to,
but not identical with, Walker's existing code.

## Known public benchmarks

The initial machine-readable benchmark pack is stored in

```text
data/public_benchmarks.csv
```

Current entries include:

| id | meaning |
|---|---|
| `walker_4_base11` | Walker's `k=4` base-11 comparator with harmonic sum `4.42175`. |
| `walker_4_base55` | Walker's best public `k=4` shifted Kempner benchmark with harmonic sum `4.43975`. |
| `bailey_3_certified_2026` | Certified `f(3)` lower-bound artifact used as a reproducibility model, not as a `k=4` target. |

The script

```text
src/benchmark_report.py
```

validates the modular certificate for one-layer digit benchmarks and recomputes the density
exponent.

## Directions now classified as low priority

### 1. Plain modular digit-set branch-and-bound

Walker's `searchkfree` repository already does this seriously.  Reimplementing the same
search in Python is useful only for validation, not for new progress.

### 2. Naive period-2 and period-3 stochastic deletion

This repository already tested a small stochastic witness-deletion/rebuild layer.  It did not
beat the Walker base-55 density exponent.  More blind random search is unlikely to be efficient.

### 3. Treating density exponent as the final objective

The density exponent is useful for screening, but the actual target is harmonic sum.  A solver
that optimizes only

```math
\alpha = \frac{\log |D|}{\log b}
```

may miss lower-exponent but higher-harmonic candidates.

## Directions to pursue next

### Track A: cyclic pseudo-Boolean / MaxSAT search

The first implemented pivot is

```text
src/cyclic_pb_encoder.py
```

It emits OPB pseudo-Boolean models for cyclic `k`-AP-free residue templates.  For each residue
variable

```math
x_d = 1 \iff d \in D,
```

and each cyclic AP residue mask `M`, it writes the hard constraint

```math
\sum_{d\in M}x_d \le |M|-1.
```

This provides a standard interface to external PB/MaxSAT solvers.  The objective is currently a
screening proxy, not an exact harmonic score.

### Track B: harmonic scoring backend

The next missing infrastructure is a Python-side harmonic scorer that can at least reproduce
Walker's public `k=4` values from digit sets.  Longer term, this should become an automaton-aware
transfer-operator backend.

### Track C: small carry-state automata

Walker explicitly notes that not every `k`-free Kempner set is explained by the simplest modular
criterion.  This is the best reason to move from plain digit sets to finite automata / carry-state
languages.

The first realistic target is not a large arbitrary DFA.  It is a 2- to 6-state regular language
over base-`b` digits with exact 4-AP certification by product/carry automaton.

## Immediate experiment queue

1. Generate OPB files for bases around the known benchmark, especially composite bases near `55`.
2. Use an external PB solver to maximize the harmonic-proxy objective with size constraints around
   `|D|=21`.
3. Validate every solver output with the exact modular checker.
4. Run harmonic post-processing only on candidates that beat or match the public benchmark proxy.
5. Implement automaton-aware harmonic scoring only after the cyclic PB route is reproducible.

## Success criterion

Near-term success is one of the following:

1. A new certified `k=4` shifted Kempner set with harmonic sum greater than `4.43975`.
2. A negative but exhaustive PB/MaxSAT certificate for a meaningful family, such as selected
   composite bases and fixed size profiles near Walker's base-55 result.
3. A regular-language candidate that is certified 4-AP-free and not equivalent to a plain one-layer
   digit set.
