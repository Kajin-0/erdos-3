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

## CL-006: Positive logarithmic density is enough

**Status:** proved, using dyadic decomposition and Szemerédi.

**Certainty:** high.

**Statement.** If

```math
\limsup_{N\to\infty}\frac{1}{\log N}\sum_{\substack{n\le N\\n\in A}}\frac1n>0,
```

then `A` contains arithmetic progressions of every finite length.

**Proof sketch.** With dyadic densities

```math
\delta_j=|A\cap[2^j,2^{j+1})|/2^j,
```

positive logarithmic density implies that the averages `J^{-1} sum_{j <= J} delta_j` have positive
limsup.  Hence some fixed positive density occurs in infinitely many dyadic blocks.  Szemerédi's
theorem inside those blocks gives arbitrarily long APs.

**Consequence.** A genuine counterexample must have divergent reciprocal sum but zero logarithmic
density:

```math
\sum_{n\in A}\frac1n=\infty,
\qquad
\frac{1}{\log N}\sum_{\substack{n\le N\\n\in A}}\frac1n\to0.
```

Equivalently, it must have `sum_j delta_j = infinity` but `(1/J) sum_{j <= J} delta_j -> 0`.

---

## CL-007: 3AP-rich dyadic blocks cast forbidden predecessor shadows for 4AP-free sets

**Status:** proved elementary counting lemma.

**Certainty:** high.

**Statement.** Let `B subset [N,2N]` and let `T_3(B)` be the number of nontrivial three-term APs
`a, a+d, a+2d` in `B` with `d > 0`.  Define the predecessor shadow

```math
P(B)=\{a-d:\ a,a+d,a+2d\in B,\ d>0,\ a-d\ge 1\}.
```

Then

```math
|P(B)| \ge \frac{T_3(B)}{N}.
```

Moreover, if `A` is 4AP-free and `B subset A`, then `A cap P(B) = emptyset`.

**Proof sketch.** Each predecessor `p` is generated by tails `(p+d,p+2d,p+3d)`.  Since the tail lies
in `[N,2N]`, there are at most `O(N)` possible positive values of `d` for each fixed `p`; the crude
bound `N` is enough.  Thus `T_3(B) <= N |P(B)|`.  If `p` were also in `A`, then
`p,p+d,p+2d,p+3d` would be a 4AP in `A`.

**Consequence.** In the `k=4` case, a dyadic block with many 3AP tails excludes a quantitatively
large set of possible earlier elements.  This is a concrete cross-block mechanism not captured by
blockwise extremal bounds alone.

**Caveat.** The lemma alone does not prove summability because different shadows can overlap heavily,
and AP-poor blocks may evade the shadow lower bound.  The next needed ingredient is a useful
rich-tail / AP-poor dichotomy plus an overlap-control argument.

---

## CL-008: AP tails are scale-local even when the whole AP is not

**Status:** proved elementary observation.

**Certainty:** high.

**Statement.** A `k`-term AP

```math
x, x+d, \ldots, x+(k-1)d
```

need not lie in a fixed multiplicative window relative to its first term `x`; if `d >> x`, the ratio
`(x+(k-1)d)/x` can be arbitrarily large.  However, the final `k-1` terms are always scale-local:

```math
\frac{x+(k-1)d}{x+d} \le k-1.
```

Thus the final `k-1` terms occupy only `O_k(1)` dyadic scales.

**Consequence.** Cross-block attacks should focus on local tails and their potentially long-range
predecessor shadows.  It is false to treat the entire AP as confined to a bounded-width logarithmic
window; only the tail has that property.

---

## Open bottleneck OB-001: Cross-block arithmetic constraints

The remaining hard case has dyadic densities `delta_j -> 0`, `sum_j delta_j = infinity`, and zero
logarithmic density.  Blockwise Szemerédi/extremal bounds are insufficient for `k >= 4`.  The likely
missing ingredient is a theorem showing that AP-free sets with divergent dyadic harmonic mass must
create cross-block additive configurations.

A useful target would be a result of the form:

```math
\sum_j \delta_j=\infty
\quad\Longrightarrow\quad
\text{some multi-scale density configuration forces a }k\text{-AP}.
```

This is the main proof direction to attack next.
