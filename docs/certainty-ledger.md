# Certainty ledger

This file records claims that should survive context loss. The full Erdős reciprocal-sum problem remains open. The theorem dependency order and active strategy are in `docs/current-proof-program.md`.

---

## CL-001: Dyadic reciprocal-sum reduction

**Status:** standard.  
**Certainty:** high.

For

```math
\alpha_j=\frac{|A\cap[2^j,2^{j+1})|}{2^j},
```

divergence of `sum_{n in A}1/n` is equivalent up to constants to `sum_j alpha_j = infinity`.

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

## CL-005: Multiplicity compression

**Status:** proved in repository.  
**Certainty:** medium-high internally.

Center, root-anchor, predecessor-anchor, and antichain decompositions export repeated labels. Fixed complete anchor histories obey

```math
\lambda_{x,q}(t)(a-t)\le a.
```

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

Cardinality alone cannot give bounded, logarithmic, polylogarithmic, or sufficiently small subpower persistence bounds.

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

Exact uncontaminated equal-translate reproduction requires

```math
L'\ge8L.
```

Moreover

```math
P_h\alpha_h\le C_0(3/4)^h,
\qquad
\sum_hP_h\alpha_h\le4C_0.
```

---

## CL-009: Finite contaminated depth-five burst

**Status:** exact finite construction.  
**Certainty:** high.

The scale factors are

```math
\boxed{4,8,4,4}
```

and

```math
\frac{W_5}{W_1}=\frac{91}{32}.
```

Universal local contraction and contraction over every four-step window are false.

---

## CL-010: Path-dependent recovery

**Status:** exact finite construction.  
**Certainty:** high.

The alternative recovery `R_5=93476` admits the factor-four descendant `R_6=230164`, giving

```math
\boxed{4,8,4,4,8,4}
```

through `S_7`, with

```math
\frac{W_7}{W_5}=\frac{205}{182}>1.
```

Universal two-generation recovery and contraction over every six-step window are false.

---

## CL-011: Complete cheap-extension exclusion from `S_7`

**Status:** exact finite theorem with structural witnesses.  
**Certainty:** high.

```math
\boxed{N_{7,2}=N_{7,4}=0.}
```

The factor-four domain has `359419` disjoint candidates, exhausted by completion, `1001`, and `0011` witnesses.

---

## CL-012: Exact depth-eight continuation

**Status:** exact finite construction.  
**Certainty:** high.

```math
R_7=2097164,
\quad
|S_8|=29523,
\quad
P_8=256,
\quad
W_8=\frac{29523}{32768}.
```

---

## CL-013: Complete cheap-extension exclusion from `S_8`

**Status:** exact finite theorem with structural witnesses.  
**Certainty:** high.

```math
\boxed{N_{8,2}=N_{8,4}=0.}
```

The factor-four domain has `4190292` disjoint candidates and is fully exhausted.

---

## CL-014: Exact depth-nine continuation

**Status:** exact finite construction.  
**Certainty:** high.

```math
R_8=16777217,
\quad
|S_9|=88572,
\quad
P_9=512,
\quad
W_9=\frac{22143}{32768}.
```

---

## CL-015: Complete cheap-extension exclusion from `S_9`

**Status:** exact finite theorem with structural witnesses.  
**Certainty:** high.

```math
\boxed{N_{9,2}=N_{9,4}=0.}
```

The factor-four domain has `39459384` disjoint candidates. Completion and recursive rectangle witnesses reduce it to seven explicit terminal witnesses.

---

## CL-016: Exact depth-ten continuation

**Status:** exact finite construction.  
**Certainty:** high.

```math
R_9=134217729,
```

```math
|S_{10}|=265719,
\quad
P_{10}=1024,
\quad
W_{10}=\frac{265719}{524288}.
```

The finite scale pattern is

```math
\boxed{4,8,4,4,8,4,8,8,8.}
```

---

## CL-017: Top-layer reduction

**Status:** elementary theorem with exact rational pattern verification.  
**Certainty:** high internally.

In the certified exact-tail geometry, every new four-term progression in three translates comes from either a three-term progression completed at `R` or `R/2` lying in the state. The same nine layer patterns remain complete across the full fitting exact factor-eight range of `S_10`.

---

## CL-018: Extended completion descent

**Status:** elementary theorem with exact rational pattern verification.  
**Certainty:** high internally.

For `R=2L+k`, a child completion at `16L+c` descends through the unique layer pattern `012` to a parent completion at

```math
2L+(c-3k).
```

---

## CL-019: Infinite exact summable tail from `S_10`

**Status:** exact infinite theorem with finite seed certificate.  
**Certainty:** high internally; awaiting independent review.

For one explicit offset schedule,

```math
k_{10}=262149,
\qquad
k_{h+1}=4k_h,
\qquad
R_h=2L_h+k_h,
```

`S_10` has an infinite exact four-term-progression-free tail with

```math
\sum_{n\ge0}W_{10+n}=\frac{33215}{16384}.
```

---

## CL-020: Original exact-tail basin criterion

**Status:** elementary theorem.  
**Certainty:** high internally.

If

```math
S\subseteq[L,7L/4),
\quad
0<k\le L/32,
```

with the lower gap and no completion obstruction, then `L'=8L`, `k'=4k` defines an infinite exact tail. For entry size `N`, replay multiplicity `P`, and scale `L`,

```math
\sum_{n\ge0}W_n=\frac{4P(N+1)}L.
```

---

## CL-021: Original depth-ten basin fan

**Status:** exact signed-completion classification.  
**Certainty:** high.

In `4<=k<=L_{10}/32`, exactly

```math
\boxed{11129810}
```

offsets enter exact infinite tails. Each has terminal charge `33215/16384`.

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

A scale word parsable into blocks

```text
[8 or larger]
[one 4 plus two 8-equivalents]
[one 2 plus four 8-equivalents]
```

has summable weighted density. The worst block-boundary contraction is

```math
2551/2560<1.
```

Universal geometric realizability of this parsing is not proved.

---

## CL-025: Cheap-step slack and contamination trichotomy

**Status:** elementary exact theorem.  
**Certainty:** high.

For

```math
T=2L-\max S,
```

a step of scale factor `c` and separation `R` satisfies

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

No complete exclusion or escape construction is yet claimed.

---

## CL-027: Complete exact factor-eight classification from `S_10`

**Status:** exact finite classification.  
**Certainty:** high.

For positive exact offsets

```math
1\le k\le613454687,
\qquad
R=2L_{10}+k,
```

there are `408969792` sponsor-compatible values. The obstruction split is

```text
completion-blocked       54999
half-separation-blocked  59034
overlap                       0
```

so

```math
\boxed{408855759}
```

positive offsets give valid exact factor-eight continuations.

---

## CL-028: Half-scale exact-tail basin

**Status:** elementary infinite theorem with exact rational pattern verification and finite `S_10` counting.  
**Certainty:** high internally; awaiting independent review.

Let

```math
\min S=L,
\qquad
S\subseteq[L,7L/4),
```

and let `0<k<L/2` with even `v_2(k)`. If the first exact step at

```math
R=2L+k
```

is four-term-progression-free, then the scheduled recurrence

```math
L_{n+1}=8L_n,
\qquad
k_{n+1}=4k_n
```

defines an infinite exact four-term-progression-free tail.

The first child enters

```math
S_1\subseteq[L_1,59L_1/32),
\qquad
k_1/L_1<1/4,
```

and the region

```math
S_n\subseteq[L_n,15L_n/8),
\qquad
k_n/L_n<1/4
```

is invariant. The nine top-layer patterns remain complete, scheduled completion descent has the unique pattern `012`, and the half-separation obstruction is impossible.

For `S_10`, the half-scale range contains

```text
178956970 sponsor-compatible offsets
54999 completion obstructions
29569 half-separation obstructions.
```

Therefore

```math
\boxed{178872402}
```

offsets enter certified infinite exact tails. Each has terminal charge

```math
\boxed{33215/16384.}
```

**Primary references:**

- `docs/half-scale-exact-tail-basin.md`;
- `src/verify_half_scale_exact_tail_basin.py`;
- `data/half_scale_exact_tail_basin_certificate_2026-07-12.txt`.

---

# Superseded or explicitly false targets

Do not use without new hypotheses:

1. bounded or polylogarithmic identical-history persistence;
2. cardinality-only subpower bounds below exponent `log_3 2`;
3. universal one-step `3/4` contraction for contaminated backbones;
4. universal strict contraction at every non-exact step;
5. contraction over every four- or six-step window;
6. universal two-generation recovery after an exact factor-eight step;
7. extrapolating one branch to all recoveries;
8. treating one or many basin tails as a whole-tree theorem;
9. random candidate sampling as a finite certificate;
10. recursive arguments that ignore mandatory shell resolution.

---

# Open bottleneck OB-001: Whole-tree Bellman compensation

The current architecture is

```text
cheap step
  -> exact Bellman debt
  -> slack consumption or imported prefix contamination
  -> repayment parsing or basin entry
  -> finite terminal charge.
```

The unresolved theorem is

```math
\boxed{
\text{every infinite continuation path has summable total weighted density.}
}
```

Approved targets:

1. classify the exact `S_10` factor-two and factor-four escape domains;
2. prove every path eventually enters an exact or near-exact basin;
3. classify valid exact `S_10` children with `k>=L_{10}/2`;
4. prove every non-basin path admits a debt-repayment parsing;
5. extend the Bellman potential by a contamination reserve dominating all children;
6. charge imported prefixes through difference export or overlap packing;
7. construct a finite-state or spectral quotient of the pre-basin tree.

No current theorem closes this gap. The full Erdős problem remains unresolved.
