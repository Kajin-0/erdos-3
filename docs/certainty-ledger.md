# Certainty ledger

This file records claims that should survive chat-context loss.  Each entry separates:

- **status**: proved / computationally verified / conjectural / open bottleneck;
- **certainty**: how strongly this repository should rely on the claim;
- **consequence**: what the claim rules out or redirects.

The full Erdős reciprocal-sum problem remains open.

---

## CL-001: Automatic sets cannot be counterexamples

**Status:** proved, modulo standard regular-language growth and Szemerédi.

**Certainty:** high.

**Statement.** Fix an integer `b >= 2`.  Let `A subset N` be base-`b` automatic, meaning that
the canonical base-`b` representations of elements of `A` form a regular language.  If

```math
\sum_{n\in A}\frac{1}{n}=\infty,
```

then `A` has positive upper asymptotic density.  Therefore, by Szemerédi's theorem, `A` contains
arithmetic progressions of every finite length.

**Proof sketch.** Let `a_m` be the number of accepted canonical words of length `m`.  The harmonic
sum diverges iff

```math
\sum_m \frac{a_m}{b^m}=\infty.
```

For a regular language, `a_m` is controlled by the Perron spectral radius `rho` of the coaccessible
transition graph.  If `rho < b`, the above series converges.  Hence divergence forces `rho=b`.
A full spectral-radius strongly connected component in a deterministic `b`-digit automaton must
have all `b` digit transitions staying inside the component.  Once this component is reached, all
middle digit blocks are admissible, and bounded accepting suffixes give positive upper density.
Szemerédi then gives arbitrarily long APs.

**Consequence.** No fixed finite automaton / regular digit-language / automatic-set construction
can produce a divergent reciprocal-sum counterexample to Erdős Problem #3.

**Caveat.** This may be known folklore in automatic sequences or regular languages.  Treat it as
a reliable theorem, not necessarily as a novel theorem.

---

## CL-002: Any AP-free divergent candidate must be sparse in every fixed-ratio interval

**Status:** proved, using Szemerédi.

**Certainty:** high.

**Statement.** If `A subset N` is `k`-AP-free for some fixed `k >= 3`, then for every fixed
`lambda > 1`,

```math
\frac{|A\cap [N,\lambda N]|}{N}\to 0.
```

**Proof sketch.** If a fixed-ratio interval `[N_i, lambda N_i]` contained `>= delta N_i` points
for infinitely many `N_i`, then inside that interval `A` would have positive relative density.
For sufficiently large intervals, Szemerédi's theorem would force a `k`-term AP, contradiction.

**Consequence.** Any counterexample to Erdős Problem #3 must have dyadic densities

```math
\delta_j = |A\cap[2^j,2^{j+1})|/2^j
```

satisfying

```math
\delta_j\to 0,
\qquad
\sum_j \delta_j=\infty.
```

The mass must be a slowly divergent logarithmic-scale dust, not persistent dense blocks.

---

## CL-003: Blockwise extremal bounds reduce the problem to summability of r_k bounds

**Status:** standard reduction.

**Certainty:** high.

**Statement.** Let `r_k(N)` be the largest size of a `k`-AP-free subset of `[1,N]`.  If

```math
\sum_j \frac{r_k(2^j)}{2^j}<\infty,
```

then every `k`-AP-free set has convergent reciprocal sum.

**Proof sketch.** For `A_j=A cap [2^j,2^{j+1})`,

```math
\sum_{n\in A_j}\frac1n \le \frac{|A_j|}{2^j}\le C\frac{r_k(2^j)}{2^j}.
```

Summing over `j` gives the claim.

**Consequence.** The full problem would follow from sufficiently strong bounds on `r_k(N)`, e.g.
roughly

```math
r_k(N) \ll \frac{N}{(\log N)(\log\log N)^{1+\epsilon}}.
```

**Current bottleneck.** Known general `k >= 4` bounds are not strong enough for this summability.
A successful proof likely needs cross-block constraints, not only independent dyadic-block bounds.

---

## CL-004: Walker base-55 shifted Kempner benchmark is locally rigid under small substitutions

**Status:** computationally verified in this repo.

**Certainty:** high for the implemented finite check; not a theorem of global optimality.

**Statement.** Walker's public `k=4`, base-55 shifted Kempner digit set with harmonic score
`4.43975` has no AP-free same-size digit-substitution neighbors at radius 1 or 2 in the repository's
cyclic modular digit-template model.

**Consequence.** Beating Walker's benchmark likely requires a larger structural change than small
same-size perturbations of the base-55 digit set.

**Caveat.** This only concerns one finite neighborhood in one model class.  It does not prove global
optimality among shifted Kempner sets.

---

## CL-005: Finite-state / regular-language search is not a counterexample route

**Status:** consequence of CL-001.

**Certainty:** high.

**Statement.** Random DFA search, regular-language search, and finite-state digit-language search can
find finite harmonic-sum extremizers or interesting AP-free finite-density examples, but cannot find
a divergent reciprocal-sum AP-free counterexample.

**Consequence.** Use DFA tools for bounded extremizer exploration and structural insight only.  Do
not treat them as a plausible route to a full counterexample.

---

## Open bottleneck OB-001: Cross-block arithmetic constraints

The remaining hard case has dyadic densities `delta_j -> 0` but `sum_j delta_j = infinity`.
Blockwise Szemerédi/extremal bounds are insufficient for `k >= 4`.  The likely missing ingredient is
a theorem showing that AP-free sets with divergent dyadic harmonic mass must create cross-block
additive configurations.

A useful target would be a result of the form:

```math
\sum_j \delta_j=\infty
\quad\Longrightarrow\quad
\text{some multi-scale density configuration forces a }k\text{-AP}.
```

This is the main proof direction to attack next.
