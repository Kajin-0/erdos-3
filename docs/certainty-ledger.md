# Certainty ledger

This file records claims that should survive context loss. The full Erdős reciprocal-sum problem remains open. The active dependency structure is in `docs/current-proof-program.md`.

---

## CL-001: Dyadic reciprocal-sum reduction

**Status:** standard.  
**Certainty:** high.

For `alpha_j=|A intersect [2^j,2^{j+1})|/2^j`, divergence of `sum_{n in A}1/n` is equivalent up to constants to `sum_j alpha_j=infinity`.

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

Repeated labels at different centers or anchors are exported by translated layers. Fixed complete anchor histories obey `lambda_{x,q}(t)(a-t)<=a`.

---

## CL-006: Self-replicating aligned diamonds

**Status:** proved recursively; finite instances verified.  
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

A 34-state automaton and a `17238`-state carry search certify no nontrivial four-term progression in the union.

---

## CL-008: Sharp exact-model classification

**Status:** elementary theorem.  
**Certainty:** high internally.

Exact uncontaminated equal-translate reproduction requires `L'>=8L`. Moreover

```math
P_h\alpha_h\le C_0(3/4)^h,
\qquad
\sum_hP_h\alpha_h\le4C_0.
```

---

## CL-009: Finite contaminated depth-five burst

**Status:** exact finite construction.  
**Certainty:** high.

The scale factors are `4,8,4,4`, and `W_5/W_1=91/32`. Universal local contraction and contraction over every four-step window are false.

---

## CL-010: Path-dependent recovery

**Status:** exact finite construction.  
**Certainty:** high.

The alternative recovery `R_5=93476` admits the factor-four descendant `R_6=230164`, giving `4,8,4,4,8,4` through `S_7`, with `W_7/W_5=205/182>1`. Universal two-generation recovery and contraction over every six-step window are false.

---

## CL-011: Complete cheap-extension exclusion from `S_7`

**Status:** exact finite theorem with structural witnesses.  
**Certainty:** high.

```math
N_{7,2}=N_{7,4}=0.
```

The factor-four domain has `359419` disjoint candidates, exhausted by completion, `1001`, and `0011` witnesses.

---

## CL-012: Exact depth-eight continuation

**Status:** exact finite construction.  
**Certainty:** high.

`R_7=2097164`, `|S_8|=29523`, `P_8=256`, and `W_8=29523/32768`.

---

## CL-013: Complete cheap-extension exclusion from `S_8`

**Status:** exact finite theorem with structural witnesses.  
**Certainty:** high.

```math
N_{8,2}=N_{8,4}=0.
```

The factor-four domain has `4190292` disjoint candidates and is fully exhausted.

---

## CL-014: Exact depth-nine continuation

**Status:** exact finite construction.  
**Certainty:** high.

`R_8=16777217`, `|S_9|=88572`, `P_9=512`, and `W_9=22143/32768`.

---

## CL-015: Complete cheap-extension exclusion from `S_9`

**Status:** exact finite theorem with structural witnesses.  
**Certainty:** high.

```math
N_{9,2}=N_{9,4}=0.
```

The factor-four domain has `39459384` disjoint candidates. Completion and recursive rectangle witnesses reduce it to seven explicit terminal witnesses.

---

## CL-016: Exact depth-ten continuation

**Status:** exact finite construction.  
**Certainty:** high.

`R_9=134217729`, `|S_10|=265719`, `P_10=1024`, and `W_10=265719/524288`. The finite scale pattern is `4,8,4,4,8,4,8,8,8`.

---

## CL-017: Top-layer reduction

**Status:** elementary theorem with exact rational pattern verification.  
**Certainty:** high internally.

In every certified exact-tail geometry used through CL-030, each new four-term progression in three translates comes from either a completion at `R` or the half-separation point `R/2` inside the state.

---

## CL-018: Completion descent

**Status:** elementary theorem with exact rational pattern verification.  
**Certainty:** high internally.

For `R=2L+k`, child completion targets descend through the unique layer pattern `012`. The scheduled target `4k` descends exactly to the preceding separation `2L+k`.

---

## CL-019: Explicit infinite exact tail from `S_10`

**Status:** exact infinite theorem with finite seed certificate.  
**Certainty:** high internally; awaiting independent review.

For one explicit offset schedule,

```math
\sum_{n\ge0}W_{10+n}=\frac{33215}{16384}.
```

---

## CL-020: Original exact-tail basin criterion

**Status:** elementary theorem.  
**Certainty:** high internally.

If `S subseteq [L,7L/4)`, `0<k<=L/32`, and the first exact step is valid, then `L'=8L`, `k'=4k` defines an infinite exact tail. Its charge is `4P(N+1)/L`.

---

## CL-021: Original depth-ten basin fan

**Status:** exact signed-completion classification.  
**Certainty:** high.

In `4<=k<=L_10/32`, exactly `11129810` offsets enter exact infinite tails. Each has charge `33215/16384`.

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

A scale word parsable into blocks `[8 or larger]`, `[one 4 plus two 8-equivalents]`, and `[one 2 plus four 8-equivalents]` has summable weighted density. The worst block factor is `2551/2560<1`. Universal geometric realizability remains open.

---

## CL-025: Cheap-step slack and contamination trichotomy

**Status:** elementary exact theorem.  
**Certainty:** high.

For `T=2L-max S`,

```math
T'=T+(c-2)L-2R.
```

Factor-two and factor-four debt is accompanied by strict slack consumption or imported prefix contamination.

---

## CL-026: Exact `S_10` cheap candidate domains

**Status:** exact finite domain certificate.  
**Certainty:** high for support, counts, and hashes.

Factor two:

```text
maximum R              76583775
sponsor-compatible     51055851
layer-disjoint         33026376
FNV-64                  59cfbc6761c6224d
```

Factor four:

```text
maximum R             613454687
sponsor-compatible    408969792
layer-disjoint        348012826
FNV-64                 ae1d9e1ec77b2dfb
```

---

## CL-027: Complete exact factor-eight classification from `S_10`

**Status:** exact finite classification.  
**Certainty:** high.

For `1<=k<=613454687`, the first-step obstruction split is

```text
completion-blocked       54999
half-separation-blocked  59034
overlap                       0
```

so `408855759` offsets give valid exact factor-eight children.

---

## CL-028: Half-scale exact-tail basin

**Status:** elementary infinite theorem with exact rational pattern verification and finite `S_10` counting.  
**Certainty:** high internally; awaiting independent review.

For `S subseteq [L,7L/4)` and `0<k<L/2`, a valid first exact step implies an infinite scheduled exact tail. At `S_10`, exactly `178872402` offsets enter such tails.

---

## CL-029: Full-fitting scheduled basin from `S_10`

**Status:** exact finite obstruction classification plus elementary infinite induction.  
**Certainty:** high internally; awaiting independent review.

Across the complete fitting exact range, only `88608` already-valid exact children fail the unmodified schedule. Thus `408767151` valid exact children enter infinite tails without repair.

---

## CL-030: Complete exact-child infinite-tail fan from `S_10`

**Status:** exact finite repair classification plus elementary infinite induction.  
**Certainty:** high internally; awaiting independent review.

The `88606` valid second-step failures are repaired by `4k -> 4k+1`. The only two third-step failures, `603979776` and `613416960`, are repaired by `16k -> 16k+1`.

Therefore

```math
\boxed{408767151+88606+2=408855759.}
```

Every valid positive exact factor-eight child of `S_10` has a certified infinite exact four-term-progression-free continuation. Every tail has charge `33215/16384`.

---

## CL-031: Complete factor-two inheritance exclusion from `S_10`

**Status:** exact embedding theorem using the certified depth-nine factor-four exclusion.  
**Certainty:** high.

The depth-ten construction contains

```math
L_{10}+(\{0\}\cup S_9)\subseteq S_{10}.
```

Hence, for every separation `R`,

```math
L_{10}+G_9(R)\subseteq G_{10}(R).
```

The factor-four fit endpoint from `S_9` is `76583776`; the factor-two fit endpoint from `S_10` is `76583775`. Since `N_{9,4}=0`,

```math
\boxed{N_{10,2}=0.}
```

The genuinely new factor-four domain has `314986450` layer-disjoint candidates.

---

## CL-032: First 10000 genuinely new `S_10` factor-four candidates

**Status:** exact finite prefix certificate with explicit deterministic witnesses.  
**Certainty:** high for the certified prefix only.

The first `10000` sponsor-compatible, layer-disjoint candidates above the inherited cutoff all contain explicit nontrivial four-term progressions. The certified prefix runs from `R=76583927` through `R=76697408`.

This leaves at most `314976450` candidates unclassified. It does not prove `N_{10,4}=0` and does not validate the rejected bulk anchor reduction. Further contiguous prefix certification is deprioritized.

**Primary references:**

- `docs/depth-ten-factor-four-first10000.md`;
- `src/run_verify_depth10_factor4_first10000.sh`;
- `docs/depth-ten-factor-four-exclusion-audit.md`.

---

## CL-033: Exact 34-class three-translate obstruction recurrence

**Status:** elementary state-independent theorem with exact symbolic verification.  
**Certainty:** high internally; awaiting independent review.

For `G_R(B)=B union (B+R) union (B+2R)`, the `80` nonconstant raw four-term layer words reduce, after global layer normalization and reversal, to exactly `34` obstruction classes: `30` reversal pairs and the self-reversing classes `0110`, `0220`, `1001`, and `2002`.

For a layer word `lambda`, define

```math
r_\lambda=\lambda_1-\lambda_0,
```

```math
a_\lambda=\lambda_0-2\lambda_1+\lambda_2,
```

```math
b_\lambda=\lambda_1-2\lambda_2+\lambda_3.
```

The triple `(r,a,b)` uniquely reconstructs the normalized word. The class occurs at separation `R` exactly when

```math
x,
\quad x+d,
\quad x+2d-aR,
\quad x+3d-(2a+b)R
```

belong to `B`, with `d+rR != 0`.

The pair-start sets satisfy the exact recurrence

```math
P_d(G_S(B))
=
\bigcup_{i,j\in\{0,1,2\}}
\left(P_{d+(i-j)S}(B)+iS\right).
```

The full labeled class coverage closes on the three-parameter affine spectrum:

```math
\widetilde\Gamma_\lambda(G_S(B);T)
=
\sum_{\mu\in\{0,1,2\}^4}
\mathcal F_B(
 a_\lambda T+a_\mu S,
 b_\lambda T+b_\mu S;
 r_\lambda T+r_\mu S
).
```

This corrects the insufficient one-scalar third-difference formulation: a four-term progression requires two second-difference equations.

**Primary references:**

- `docs/three-translate-obstruction-coverage-recurrence.md`;
- `src/verify_three_translate_obstruction_classes.py`;
- `data/three_translate_obstruction_classes_certificate_2026-07-13.txt`.

---

# Superseded, explicitly false, or deprioritized targets

Do not use without new hypotheses:

1. bounded or polylogarithmic identical-history persistence;
2. cardinality-only subpower bounds below exponent `log_3 2`;
3. universal one-step `3/4` contraction for contaminated backbones;
4. universal strict contraction at every non-exact step;
5. contraction over every four- or six-step window;
6. universal two-generation recovery after an exact factor-eight step;
7. extrapolating one branch to all recoveries;
8. treating one or many exact tails as a whole-tree theorem;
9. random candidate sampling as a finite certificate;
10. recursive arguments that ignore mandatory shell resolution;
11. using one third-difference equation as a complete four-term-progression test;
12. treating pathwise summability alone as sufficient for the branching deletion tree;
13. further contiguous `S_10` prefix certification without a structural hypothesis.

---

# Open bottleneck OB-001: Whole-tree contamination reserve

The current architecture is

```text
cheap step
  -> exact Bellman debt
  -> affine obstruction coverage growth or slack/prefix consumption
  -> forced expensive step / exact-tail entry
  -> branching repayment and finite tree charge.
```

The required theorem is treewise, not merely pathwise. The active target is a nonnegative reserve `Phi` in Bellman units satisfying a branching inequality of the form

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

Approved targets:

1. classify stratified witnesses across the full `S_10` factor-four range by the `34` exact layer classes;
2. trace witnesses to parent-layer words and ancestor origins in the two-scale recurrence;
3. identify a small closed subsystem or monotone contraction of the uncovered-separation zero set;
4. define a normalized affine-coverage reserve in units `P/L`;
5. prove a branching Carleson/packing inequality for all retained children;
6. charge imported prefixes through difference export or overlap packing.

No current theorem closes this gap. The full Erdős problem remains unresolved.
