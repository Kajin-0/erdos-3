# DFA growth productive-subgraph fix

## Status

Correctness correction, implemented and regression-tested on branch `certainty-ledger`.

An external review identified that `src/dfa_growth_score.py` computed the Perron spectral radius of the complete DFA transition matrix, including rejecting sink components.  The diagnosis was correct.

## The bug

For the supplied base-11 two-state DFA,

```math
A=
\begin{pmatrix}
6&5\\
0&11
\end{pmatrix},
```

where the accepting state has six allowed digits and five transitions to the rejecting sink, while the sink has all eleven self-transitions.

The full matrix has

```math
\rho(A)=11,
```

so the old scorer reported

```math
\alpha=\frac{\log 11}{\log 11}=1.
```

But the rejecting sink contributes no accepted words.  The accepted language has exactly `6^m` words of length `m`, so the correct growth data are

```math
\rho_{\mathrm{lang}}=6,
\qquad
\alpha=\frac{\log 6}{\log 11}
=0.747221736309\ldots.
```

## Correct graph

The accepted-language exponential growth is controlled by states that are both:

1. reachable from the start state; and
2. coaccessible to an accepting state.

Equivalently, these are the states lying on some start-to-accepting path.

The corrected scorer constructs the induced digit-transition matrix on this productive subgraph.  Transitions leaving the productive subgraph are omitted.

## Implementation

The fix adds

```python
productive_states(dfa)
```

and allows

```python
transition_matrix(dfa, states)
```

to construct an induced matrix.  `score_dfa()` now computes the Perron root on

```python
growth_states = productive_states(dfa)
```

rather than on all DFA states.

The complete transition matrix is still used by `accepted_counts_by_length()`, since exact word propagation must retain all states.

## Regression tests

A deterministic test now checks the base-11 DFA with allowed digits

```math
\{0,1,2,4,5,7\}.
```

It verifies

```math
\operatorname{productive}(\mathrm{DFA})=\{\mathrm{ok}\},
```

```math
\rho=6,
```

```math
\alpha=\frac{\log 6}{\log 11},
```

and exact accepted-word counts

```math
1,6,36,216
```

for lengths `0,1,2,3`.

A second test verifies that a DFA with no accepting state has no productive states, spectral radius zero, and zero accepted counts.

## Scope of invalidation

The bug invalidated:

1. previously reported DFA growth exponents;
2. any diagnostic or screening decision that used those exponents;
3. any claim that a rejecting-sink DFA had full growth solely because the full transition matrix had Perron root `b`.

The bug did **not** invalidate:

1. the exact DFA 4-AP certifier;
2. truncated harmonic sums computed by direct enumeration;
3. accepted-word counts propagated to accepting states;
4. the theoretical certainty-ledger statement that regular-language growth is governed by the productive/coaccessible graph.

## Correctness consequence

All DFA candidates should be rescored before growth-based comparisons are reused.  The base-11 benchmark now returns the expected exponent

```math
0.747221736309\ldots
```

instead of `1`.

## Next correctness tasks

The remaining high-priority audit items from the external review are:

1. add deterministic benchmark tests for harmonic scores and neighborhood counts;
2. harden PB assignment parsing and verify cardinality/objective completeness;
3. add reproducibility manifests containing solver version, command, model hash, status, bound, gap, and independently checked assignment;
4. separate finite harmonic-extremizer experiments from the full divergent-series proof track.
