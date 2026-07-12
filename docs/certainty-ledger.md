# Certainty ledger

This file records claims that should survive context loss. Each entry states status, certainty, consequence, and caveat. The full Erdős reciprocal-sum problem remains open. The theorem dependency order is in `docs/current-proof-program.md`.

---

## CL-001: Dyadic reciprocal-sum reduction

**Status:** standard.  
**Certainty:** high.

For

```math
\alpha_j=\frac{|A\cap[2^j,2^{j+1})|}{2^j},
```

divergence of `sum_{n in A}1/n` is equivalent up to constants to `sum_j alpha_j = infinity`. A divergent four-term-progression-free candidate must have `alpha_j -> 0`.

---

## CL-002: Coordinated deletion and minimum-translation backbone

**Status:** proved in repository.  
**Certainty:** medium-high internally.  
**Audit:** awaiting independent review.

Coordinated side-anchor deletion removes `K=|D|-s` sponsors from a four-term-progression-free block `D subseteq[N,2N)` and leaves a three-term-progression-free residual with `s<=r_3(N)`.

For `m=min D`,

```math
\mathcal B(D)=\{d-m:d\in D,\ d>m\}
```

is four-term-progression-free, lies below `N`, has size `|D|-1`, and contracts every associated label by at least one half.

---

## CL-003: One-generation harmonic inequalities

**Status:** proved in repository.  
**Certainty:** medium-high internally.

The raw middle family and backbone satisfy

```math
H(\mathcal B(D))+\sum_xH(M_x)
\ge
3H(D)-2\frac{r_3(N)}N-\frac1N.
```

After exact middle-multiplicity resolution,

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

**Caveat:** the raw factor-three inequality counts repeated numerical labels before multiplicity compression.

---

## CL-004: Shell resolution and positive-moment control

**Status:** proved interface and moment bounds.  
**Certainty:** high for the shell requirement; medium-high for the recursive interpretation.

Children must be resolved into standard dyadic shells before deletion is reapplied. For every `p>=1`,

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p,
```

and across the full tree,

```math
\sum_q\mu(q)q^p\le2^{1-p}\sum_{a\text{ root}}a^p.
```

Positive moments do not by themselves control reciprocal mass.

---

## CL-005: Center, anchor, and predecessor compression

**Status:** proved in repository.  
**Certainty:** medium-high internally.

Repeated labels occurring at different lifted centers, root anchors, or predecessor anchors are exported by translated difference layers. Copies with one fixed complete anchor history obey

```math
\lambda_{x,q}(t)(a-t)\le a.
```

High unresolved multiplicity is localized immediately below the root sponsor.

---

## CL-006: Self-replicating aligned diamonds

**Status:** proved recursively; finite instances computationally verified.  
**Certainty:** medium-high.

There are four-term-progression-free states with

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h.
```

Hence

```math
P_h\asymp|S_h|^{\log_3 2}.
```

**Consequence:** bounded, logarithmic, polylogarithmic, and sufficiently small subpower persistence bounds in terms of parent cardinality are false.

---

## CL-007: Infinite exact scale-eight family

**Status:** computer-assisted exact construction.  
**Certainty:** high for the finite-state certificate; medium-high for the full interpretation pending review.

There is an infinite exact family with

```math
L_h=8^{h+1},
\qquad
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h=\frac12L_h^{1/3}.
```

A 34-state base-eight automaton and a `17238`-state carry search certify that the union contains no nontrivial four-term progression.

---

## CL-008: Sharp exact-model classification

**Status:** proved by elementary shell and progression arguments.  
**Certainty:** high internally.

Exact uncontaminated equal-translate reproduction requires

```math
L'\ge8L.
```

Writing `alpha_h=|S_h|/L_h`,

```math
P_h\alpha_h\le C_0\left(\frac34\right)^h,
\qquad
\sum_hP_h\alpha_h\le4C_0.
```

The scale-eight family attains the exponents.

**Caveat:** this does not control contaminated backbones.

---

## CL-009: Finite contaminated depth-five burst

**Status:** exact finite computer-assisted construction.  
**Certainty:** high for the finite certificate.

The scale factors are

```math
\boxed{4,8,4,4.}
```

With

```math
W_h=P_h^{\mathrm{cert}}\frac{|S_h|}{L_h},
```

```math
W_1=\frac38,
\qquad
W_5=\frac{273}{256},
\qquad
\frac{W_5}{W_1}=\frac{91}{32}.
```

**Consequence:** universal local contraction and contraction over every four-generation window are false.

---

## CL-010: Path-dependent exact recovery

**Status:** exact finite computer-assisted construction.  
**Certainty:** high for the finite branches.

The state `S_5` has no factor-two or factor-four continuation. Its smallest exact recovery enters a strongly contracting branch, but the alternative exact recovery `R_5=93476` admits the factor-four descendant `R_6=230164`.

The resulting scale pattern through `S_7` is

```math
\boxed{4,8,4,4,8,4,}
```

with

```math
\frac{W_7}{W_5}=\frac{205}{182}>1.
```

**Consequence:** universal two-generation recovery and contraction over every six-generation window are false.

---

## CL-011: Complete cheap-extension exclusion from `S_7`

**Status:** exact finite theorem with structural witnesses.  
**Certainty:** high.

```math
\boxed{N_{7,2}=N_{7,4}=0.}
```

The factor-four domain has `359419` disjoint candidates, covered by `352979` completion witnesses, `215` pattern-`1001` witnesses, and `6225` pattern-`0011` witnesses.

---

## CL-012: Exact depth-eight continuation

**Status:** exact finite construction.  
**Certainty:** high.

The first valid exact factor-eight continuation from `S_7` is

```math
R_7=2097164.
```

It produces `|S_8|=29523`, `P_8=256`, and

```math
W_8=\frac{29523}{32768}.
```

---

## CL-013: Complete cheap-extension exclusion from `S_8`

**Status:** exact finite theorem with structural witnesses.  
**Certainty:** high.

```math
\boxed{N_{8,2}=N_{8,4}=0.}
```

The factor-four domain has `4190292` disjoint candidates. Completion, `1001`, and bounded-memory `0011` witnesses exhaust the domain.

---

## CL-014: Exact depth-nine continuation

**Status:** exact finite construction.  
**Certainty:** high.

The first valid exact factor-eight continuation is

```math
R_8=16777217.
```

It produces `|S_9|=88572`, `P_9=512`, and

```math
W_9=\frac{22143}{32768}.
```

---

## CL-015: Complete cheap-extension exclusion from `S_9`

**Status:** exact finite theorem with structural witnesses.  
**Certainty:** high for the recorded domains and hashes.

```math
\boxed{N_{9,2}=N_{9,4}=0.}
```

The factor-four domain has `39459384` disjoint candidates. Completion witnesses cover `30221222`; recursive rectangle witnesses reduce the remainder to seven explicit full-parent witnesses.

---

## CL-016: Exact depth-ten continuation

**Status:** exact finite construction.  
**Certainty:** high.

The first valid exact factor-eight continuation is

```math
R_9=134217729.
```

It produces

```math
|S_{10}|=265719,
\qquad
P_{10}=1024,
\qquad
W_{10}=\frac{265719}{524288}.
```

The certified finite scale pattern is

```math
\boxed{4,8,4,4,8,4,8,8,8.}
```

---

## CL-017: Top-layer reduction lemma

**Status:** elementary theorem with exact rational pattern verification.  
**Certainty:** high internally.

Let `S subseteq[L,7L/4)`, `A={0} union S`, and `2L<R<=65L/32`. If `A` is four-term-progression-free, every nontrivial four-term progression in

```math
A\cup(A+R)\cup(A+2R)
```

comes from either:

1. a three-term progression in `S` completed at `R`; or
2. `R` even with `R/2 in S`.

The exact verifier leaves only the layer patterns

```text
0000,1111,2222
0001,0012,1112
0011,0112,1122.
```

---

## CL-018: Small-offset completion descent

**Status:** elementary theorem with exact rational pattern verification.  
**Certainty:** high internally.

For `R=2L+k`, `0<k<=L/32`, and `S'=8L+(({0} union S)+{0,R,2R})`, every three-term progression in `S'` completed at `16L+c`, with `0<c<=L/8`, descends through the unique layer pattern `012` to a progression in `S` completed at

```math
2L+(c-3k).
```

The converse lift also holds, as does the left-completion version.

---

## CL-019: Infinite exact summable tail from `S_10`

**Status:** exact infinite theorem with a finite seed certificate and elementary induction.  
**Certainty:** high internally; awaiting independent review.

Let

```math
D=262143,
\qquad
k_{10}=262149.
```

For `h>=10`, define

```math
L_{h+1}=8L_h,
\qquad
k_{h+1}=4k_h,
\qquad
R_h=2L_h+k_h,
```

and use exact three-translate reproduction.

A finite `S_8` completion certificate has `2772873` completion coordinates with maximum `17038008`, while

```math
2L_8+D=17039359.
```

Completion descent and a persistent lower gap therefore exclude both top-layer obstructions forever. Every tail state is four-term-progression-free and exact-backbone.

For `n>=0`,

```math
k_{10+n}=262149\cdot4^n,
```

```math
|S_{10+n}|=\frac{3^{12+n}-3}{2},
\qquad
P_{10+n}=2^{10+n},
```

and

```math
\boxed{
W_{10+n}=\frac{3^{12+n}-3}{2^{20+2n}}.
}
```

The tail is summable:

```math
\boxed{
\sum_{n\ge0}W_{10+n}=\frac{33215}{16384}.
}
```

**Consequence:** the recorded contaminated branch has an explicit infinite summable compensation basin.

**Caveat:** this proves one continuation path is summable; it does not control all descendants or the union across shells.

---

# Superseded or explicitly false targets

Do not use the following without new hypotheses:

1. bounded or polylogarithmic identical-history persistence;
2. a subpower persistence bound below exponent `log_3 2` based only on parent cardinality;
3. universal one-step `3/4` contraction for contaminated backbones;
4. universal strict contraction at every non-exact step;
5. contraction over every block of four or six outer steps;
6. a universal two-generation recovery theorem after an exact factor-eight step;
7. extrapolating one recovery branch to every recovery;
8. treating one summable infinite tail as a whole-tree theorem;
9. recursive arguments that ignore mandatory dyadic shell resolution.

---

# Open bottleneck OB-001: Whole-tree compensation

One explicit contaminated branch now enters an infinite exact tail with finite total weighted density. The remaining question is

```math
\boxed{
\text{does every infinite continuation path have summable total weighted density?}
}
```

Equivalent approved targets:

1. prove every infinite path has long-run geometric-mean scale expansion greater than `6`;
2. prove every path eventually enters a summable exact or near-exact basin;
3. construct a contamination-debt potential that permits delayed release but forces repayment;
4. control the entire continuation tree by a finite-state or spectral quotient;
5. prove an aggregate packing theorem for overlapping replay cores.

No current theorem closes this gap. The full Erdős problem remains unresolved.
