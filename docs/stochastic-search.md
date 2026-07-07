# Stochastic periodic search

## Purpose

The exhaustive period-2 threshold search is exact but expensive for larger bases.  The next
search layer is a stochastic witness-guided heuristic implemented in

```text
src/periodic_stochastic_search.py
```

The heuristic is designed to produce candidate structures quickly.  It does not prove
optimality.  Every final candidate is still checked by the exact finite carry automaton.

## Algorithm

For a base `b` and period `m`:

1. Start from full digit sets in every residue class.
2. Use the exact automaton to find a 4-AP witness.
3. Delete one nonzero digit appearing in that witness.
4. Repeat until the periodic digit language is certified 4-AP-free.
5. Greedily re-add deleted digits when the exact certificate remains 4-AP-free.

The comparable density exponent is

```math
\alpha(D_0,\dots,D_{m-1})=
\frac{1}{m\log b}\sum_{j=0}^{m-1}\log |D_j|.
```

The current benchmark remains

```math
\alpha_{55}=\frac{\log 21}{\log 55}\approx 0.75974.
```

## First stochastic run

The file

```text
data/stochastic_periodic_run_2026-07-07.csv
```

records period-2 and period-3 exploratory runs.  No candidate exceeded the Walker base-55
benchmark.  The best candidate in this run was the period-3 base-11 system with equal layer
sizes `6,6,6`, giving

```math
\alpha=\frac{\log 6}{\log 11}\approx 0.74722.
```

This is below the target but close enough to justify improving the search machinery.

## Interpretation

The current evidence is negative for the simplest extensions:

- one-digit period-2 augmentation of the base-11 Walker set failed;
- exact period-2 threshold search through base 13 failed;
- stochastic period-2/3 search through small bases did not beat the base-55 exponent.

This does not imply no such system exists.  It says that the next serious step should not be
more naive random deletion; it should be constraint-guided search.

## Next implementation target

Add a branch-and-bound or SAT-style search over Boolean digit variables

```math
x_{j,d}=1 \iff d\in D_j.
```

The forbidden object is not a single local digit tuple but a nontrivial cycle in the carry
automaton.  A practical SAT formulation should iteratively:

1. propose digit sets satisfying the size/exponent target;
2. run the exact automaton;
3. if a witness AP appears, add a blocking clause requiring at least one witness digit-layer
   membership to be removed;
4. repeat until either a certified candidate is found or all candidates at that size profile
   are eliminated.
