# Certainty ledger addendum — 2026-07-07

This addendum records high-certainty items discovered after the initial `docs/certainty-ledger.md` file became large.  Merge these entries into the main ledger when convenient.

---

## CL-009: Exact dilation triples are not forced by divergent harmonic mass

**Status:** proved obstruction to an attempted proof route.

**Certainty:** high.

**Pointer:** `docs/dilation-triple-failure-mode.md`.

**Statement.** Divergent reciprocal sum, even with zero logarithmic density, does not by itself force exact triples of the form `d,2d,3d`.

**Consequence.** A proof cannot rely on showing that divergent harmonic mass alone creates exact dilation triples.  Any viable long-range tail-shadow argument must use shifted tails, local AP-rich/AP-poor structure, or a different mechanism.

---

## CL-010: Dyadic summability is equivalent to the fixed-k reciprocal-sum problem for k >= 4

**Status:** proved structural reduction.

**Certainty:** high.

**Pointer:** `docs/dyadic-summability-equivalence.md`.

**Statement.** For every fixed `k >= 4`, the reciprocal-sum Erdős problem for avoiding `k`-term arithmetic progressions is equivalent to the dyadic summability condition

```math
\sum_{j\ge 1}\frac{r_k(2^j)}{2^j}<\infty,
```

where `r_k(N)` is the largest size of a `k`-AP-free subset of `[1,N]`.

**Reason.** The sufficient direction is the standard dyadic-block bound.  Conversely, if the dyadic series diverges, one can choose a sufficiently separated residue class of dyadic scales, place extremal `k`-AP-free subsets inside those blocks only, and obtain a global `k`-AP-free set with divergent reciprocal sum.

**Consequence.** For fixed `k >= 4`, cross-block constraints cannot be the universal missing ingredient.  If dyadic extremal densities are not summable, widely separated extremal blocks eliminate cross-block APs while preserving divergent reciprocal mass.

---

## OB-002: Updated central bottleneck

The universal fixed-`k` problem is now reduced to improving bounds for `r_k(N)` enough to make

```math
\sum_j r_k(2^j)/2^j
```

converge.

For `k=4`, a sufficient bound would be approximately

```math
r_4(N) \ll \frac{N}{(\log N)^{1+\epsilon}}
```

for some `epsilon > 0`, or any stronger summable decay along dyadic `N`.

For general fixed `k`, the analogous target is any bound strong enough that `r_k(2^j)/2^j` is summable in `j`.
