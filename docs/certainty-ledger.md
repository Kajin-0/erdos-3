# Certainty ledger

This file records claims that should survive context loss. The full Erdős reciprocal-sum problem remains open. The active dependency structure is in `docs/current-proof-program.md`.

---

## CL-001: Dyadic reciprocal-sum reduction

**Status:** standard.  
**Certainty:** high.

For

```math
\alpha_j=\frac{|A\cap[2^j,2^{j+1})|}{2^j},
```

divergence of `sum_{n in A}1/n` is equivalent up to constants to `sum_j alpha_j=infinity`.

---

## CL-002: Coordinated deletion and minimum-translation backbone

**Status:** proved in repository.  
**Certainty:** medium-high internally.

Coordinated deletion leaves a three-term-progression-free residual of size at most `r_3(N)`. The minimum-translation backbone is four-term-progression-free, has size `|D|-1`, lies below `N`, and contracts associated labels by at least one half.

---

## CL-003: One-generation harmonic inequalities

**Status:** proved in repository.  
**Certainty:** medium-high internally.

```math
H(\mathcal B(D))+\sum_xH(M_x)
\ge
3H(D)-2\frac{r_3(N)}N-\frac1N,
```

and

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

---

## CL-004: Shell resolution and positive moments

**Status:** proved.  
**Certainty:** high for shelling; medium-high for recursive use.

Children must be resolved into standard dyadic shells. For `p>=1`,

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p.
```

---

## CL-005: Center, anchor, predecessor, and antichain compression

**Status:** proved in repository.  
**Certainty:** medium-high internally.

Repeated labels at different centers or anchors are exported by translated layers. Fixed complete anchor histories obey the recorded antichain bounds.

---

## CL-006: Self-replicating aligned diamonds

**Status:** recursive theorem with finite verification.  
**Certainty:** medium-high.

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h,
\qquad
P_h\asymp|S_h|^{\log_3 2}.
```

---

## CL-007: Infinite exact scale-eight family

**Status:** computer-assisted exact construction.  
**Certainty:** high for the finite-state certificate.

```math
L_h=8^{h+1},
\qquad
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h=\frac12L_h^{1/3}.
```

A finite automaton and exact carry search certify no nontrivial four-term progression in the union.

---

## CL-008: Sharp exact-model classification

**Status:** elementary theorem.  
**Certainty:** high internally.

Exact uncontaminated equal-translate reproduction requires `L'>=8L`, and

```math
P_h\alpha_h\le C_0(3/4)^h,
\qquad
\sum_hP_h\alpha_h\le4C_0.
```

---

## CL-009: Finite contaminated depth-five burst

**Status:** exact finite construction.  
**Certainty:** high.

The scale factors are `4,8,4,4`, and

```math
\frac{W_5}{W_1}=\frac{91}{32}>1.
```

Universal local contraction and contraction over every four-step window are false.

---

## CL-010: Path-dependent recovery

**Status:** exact finite construction.  
**Certainty:** high.

The chain extends through `S_7` with scale word `4,8,4,4,8,4` and `W_7/W_5>1`. Universal two-generation recovery and contraction over every six-step window are false.

---

## CL-011: Complete cheap-extension exclusion from `S_7`

**Status:** exact finite theorem with structural witnesses.  
**Certainty:** high.

```math
N_{7,2}=N_{7,4}=0.
```

---

## CL-012: Exact depth-eight continuation

**Status:** exact finite construction.  
**Certainty:** high.

```math
R_7=2097164,
\qquad
|S_8|=29523,
\qquad
P_8=256.
```

---

## CL-013: Complete cheap-extension exclusion from `S_8`

**Status:** exact finite theorem with structural witnesses.  
**Certainty:** high.

```math
N_{8,2}=N_{8,4}=0.
```

---

## CL-014: Exact depth-nine continuation

**Status:** exact finite construction.  
**Certainty:** high.

```math
R_8=16777217,
\qquad
|S_9|=88572,
\qquad
P_9=512.
```

---

## CL-015: Complete cheap-extension exclusion from `S_9`

**Status:** exact finite theorem with structural witnesses.  
**Certainty:** high.

```math
N_{9,2}=N_{9,4}=0.
```

The factor-four domain has `39459384` layer-disjoint candidates and is exhausted by completion and recursive rectangle witnesses, followed by seven explicit terminal witnesses.

---

## CL-016: Exact depth-ten continuation

**Status:** exact finite construction.  
**Certainty:** high.

```math
R_9=134217729,
\qquad
L_{10}=536870912,
\qquad
|S_{10}|=265719,
\qquad
P_{10}=1024.
```

The finite scale word is `4,8,4,4,8,4,8,8,8`.

---

## CL-017: Exact-tail top-layer reduction

**Status:** elementary theorem with exact rational pattern verification.  
**Certainty:** high internally.

In every certified exact-tail geometry used through CL-030, each new four-term progression in three translates comes from either a completion at `R` or the half-separation point `R/2` inside the state.

---

## CL-018: Completion descent

**Status:** elementary theorem with exact rational pattern verification.  
**Certainty:** high internally.

For `R=2L+k`, scheduled child completion targets descend through the unique recorded layer pattern, and `4k` descends to the preceding separation.

---

## CL-019: Explicit infinite exact tail from `S_10`

**Status:** exact infinite theorem with finite seed certificate.  
**Certainty:** high internally.

For the explicit schedule,

```math
\sum_{n\ge0}W_{10+n}=\frac{33215}{16384}.
```

---

## CL-020: Original exact-tail basin criterion

**Status:** elementary theorem.  
**Certainty:** high internally.

The original small-offset criterion produces infinite exact scale-eight tails with charge `4P(N+1)/L`.

---

## CL-021: Original depth-ten basin fan

**Status:** exact finite classification.  
**Certainty:** high.

The original basin contains `11129810` certified offsets from `S_10`.

---

## CL-022: Exact-tail Bellman potential

**Status:** elementary algebraic theorem.  
**Certainty:** high.

For constant exact scale factor `c>6`,

```math
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac{6}{c-2}\right).
```

At `c=8`, `B_8=4P(N+1)/L`.

---

## CL-023: Scale-word Bellman debt identity

**Status:** elementary exact theorem.  
**Certainty:** high.

```math
\mathfrak D_c
=
\mathfrak B-W-\mathfrak B'
=
\frac{P(3N+4)}L\left(1-\frac8c\right).
```

Factors `2` and `4` create debt, `8` is neutral, and factors at least `16` create surplus.

---

## CL-024: Cheap-debt repayment parsing

**Status:** elementary sufficient theorem.  
**Certainty:** high.

A scale word parsable into the recorded repayment blocks has summable weighted density. Universal geometric realizability remains open.

---

## CL-025: Cheap-step slack and contamination trichotomy

**Status:** elementary exact theorem.  
**Certainty:** high.

For `T=2L-max S`,

```math
T'=T+(c-2)L-2R.
```

Factor-two and factor-four debt is accompanied by strict slack consumption or imported-prefix contamination.

---

## CL-026: Exact `S_10` candidate domains

**Status:** exact finite domain certificate.  
**Certainty:** high.

Factor two has `33026376` layer-disjoint candidates. Factor four has `348012826` layer-disjoint candidates and FNV-64 `ae1d9e1ec77b2dfb`.

---

## CL-027: Complete exact factor-eight classification from `S_10`

**Status:** exact finite classification.  
**Certainty:** high.

There are

```math
408855759
```

valid positive exact factor-eight children.

---

## CL-028: Half-scale exact-tail basin

**Status:** elementary infinite theorem with exact rational verification.  
**Certainty:** high internally.

A valid exact child in the half-scale region enters an infinite scheduled exact tail. At `S_10`, this gives `178872402` certified offsets.

---

## CL-029: Full-fitting scheduled basin from `S_10`

**Status:** exact finite obstruction classification plus elementary induction.  
**Certainty:** high internally.

The unmodified schedule gives infinite tails for `408767151` valid exact children.

---

## CL-030: Complete exact-child infinite-tail fan from `S_10`

**Status:** exact finite repair classification plus elementary induction.  
**Certainty:** high internally.

Finite `+1` repairs cover the remaining `88608` valid exact children. Hence every one of the `408855759` valid exact children has a certified infinite tail of charge `33215/16384`.

---

## CL-031: Complete factor-two inheritance exclusion from `S_10`

**Status:** exact embedding theorem using CL-015.  
**Certainty:** high.

```math
L_{10}+(\{0\}\cup S_9)\subseteq S_{10}
```

implies

```math
\boxed{N_{10,2}=0.}
```

---

## CL-032: First 10000 genuinely new `S_10` factor-four candidates

**Status:** exact finite prefix certificate.  
**Certainty:** high for the prefix only.

The first `10000` candidates above the inherited cutoff have explicit witnesses. This result is retained as regression data and is superseded as a frontier by CL-037.

---

## CL-033: Exact 34-class three-translate obstruction recurrence

**Status:** elementary state-independent theorem with exact symbolic verification.  
**Certainty:** high internally.

The `80` nonconstant raw layer words reduce to `34` classes. The affine spectrum closes under the exact two-scale recurrence

```math
\widetilde\Gamma_\lambda(G_S(B);T)
=
\sum_\mu
\mathcal F_B(
 a_\lambda T+a_\mu S,
 b_\lambda T+b_\mu S;
 r_\lambda T+r_\mu S
).
```

---

## CL-034: Lifted `S_9` completion reduction at `S_10`

**Status:** exact finite structural-witness theorem.  
**Certainty:** high.

The genuinely new factor-four domain contains `314986450` candidates. Lifted depth-nine completion support removes

```math
137142200
```

and leaves the exact residual

```math
\boxed{177844250}.
```

The residual ranges from `97474324` through `613454687` and has FNV-64 `00369694f2d70526`.

This theorem is valid and must not be confused with the rejected exploratory anchor reduction.

---

## CL-035: Exact four-ratio rectangle transport

**Status:** elementary state-independent theorem with exact symbolic verification.  
**Certainty:** high internally.

If `B` contains

```math
x,x+d,x+2d-U,x+3d-U,
```

with `d>0` and `0<U<S`, then for each

```math
k\in\{1,2,3,4\},
```

both `T=kS+U` and `T=kS-U` produce a nontrivial progression in `G_T(G_S(B))`. There are no positive integer rectangle-cancellation ratios `k>=5`.

---

## CL-036: Complete direct rectangle support of `B_9`

**Status:** exact finite computer-assisted theorem.  
**Certainty:** high internally; awaiting independent review.

For

```math
B_9=\{0\}\cup S_9,
```

one has

```math
\boxed{
\mathcal F_{B_9}(U,-U;0)>0
\quad
\text{for every }1\le U\le76583776.
}
```

Certificate decomposition:

```text
76581484 structural count-band values
2285 deterministic explicit terminal witnesses
7 stored exact large-fiber witnesses
```

so

```math
76581484+2285+7=76583776.
```

**Primary references:**

- `src/verify_b9_direct_rectangle_support.cpp`;
- `data/b9_direct_rectangle_support_certificate_2026-07-13.txt`;
- `data/b9_direct_rectangle_terminal7_witnesses_2026-07-13.txt`.

---

## CL-037: Complete factor-four exclusion from `S_10`

**Status:** exact finite computer-assisted theorem plus elementary transport.  
**Certainty:** high internally; awaiting independent review.

The complete layer-disjoint factor-four domain partitions as

```math
33026376+137142200+177844250=348012826.
```

The three terms are excluded by:

1. factor-two inheritance from `S_9`;
2. lifted `S_9` completion support;
3. complete `B_9` rectangle support and four-ratio transport.

The four transport windows overlap and cover the complete residual interval. The `U=0` boundary is blocked by a pure layer-index progression. Therefore

```math
\boxed{N_{10,4}=0.}
```

Together with CL-031,

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

**Primary references:**

- `docs/complete-depth-ten-factor-four-exclusion.md`;
- `src/run_verify_s10_factor4_rectangle_closure.sh`;
- `src/verify_s10_factor4_rectangle_closure.py`;
- `data/s10_factor4_rectangle_closure_certificate_2026-07-13.txt`.

---

# Superseded, explicitly false, or deprioritized targets

Do not use without new hypotheses:

1. bounded or polylogarithmic identical-history persistence;
2. cardinality-only subpower bounds below exponent `log_3 2`;
3. universal one-step `3/4` contraction for contaminated backbones;
4. universal strict contraction at every non-exact step;
5. contraction over every four- or six-step window;
6. universal two-generation recovery after an exact factor-eight step;
7. extrapolating one path to the whole continuation tree;
8. treating exact tails as a whole-tree theorem;
9. using one third-difference equation as a complete four-term-progression test;
10. treating pathwise summability as sufficient for the branching deletion tree;
11. random sampling as a finite certificate;
12. the rejected depth-ten anchor reduction;
13. further contiguous `S_10` prefix certification.

---

# Open bottleneck OB-001: Whole-tree contamination reserve

The state-specific cheap-extension problem at `S_10` is closed. The unresolved theorem is treewise, not merely pathwise.

The active target is a nonnegative reserve `Phi` in Bellman units satisfying

```math
\boxed{
W(S)
+
\sum_{S'\in\operatorname{Child}(S)}
\left(\mathfrak B(S')+\Phi(S')\right)
\le
\mathfrak B(S)+\Phi(S)
+
\operatorname{controlled\ error}.
}
```

The reserve must convert completion growth, pair-fiber/rectangle coverage, slack consumption, imported prefixes, and overlap packing into branching repayment.

Approved targets:

1. define normalized completion and rectangle reserves in units `P/L`;
2. prove a state-class zero-set contraction or coverage-growth theorem;
3. charge imported prefixes through difference export or bounded overlap;
4. prove a branching Carleson inequality for all retained children;
5. construct a finite-state or spectral quotient of the pre-basin tree;
6. identify structural hypotheses under which CL-036 persists beyond the numerical state `B_9`.

No current theorem closes this gap. The full Erdős problem remains unresolved.
