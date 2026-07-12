# Certainty ledger

This file records claims that should survive context loss. Each entry states status, certainty, consequence, and the controlling caveat.

The full Erdős reciprocal-sum problem remains open. The authoritative dependency order is in `docs/current-proof-program.md`.

---

## CL-001: Dyadic reciprocal-sum reduction

**Status:** standard.

**Certainty:** high.

For

```math
\alpha_j
=
\frac{|A\cap[2^j,2^{j+1})|}{2^j},
```

divergence of `sum_{n in A}1/n` is equivalent up to constants to

```math
\sum_j\alpha_j=\infty.
```

A four-term-progression-free divergent candidate must have `alpha_j -> 0` but `sum_j alpha_j = infinity`.

---

## CL-002: Sponsored side-anchor deletion

**Status:** proved in repository.

**Certainty:** medium-high.

For a four-term-progression-free block `D subseteq[N,2N)`, coordinated side-anchor deletion removes

```math
K=|D|-s
```

sponsors and leaves a three-term-progression-free residual with

```math
s\le r_3(N).
```

Every deleted sponsor creates one selected middle-step occurrence `q<=N/2`.

---

## CL-003: Minimum-translation backbone

**Status:** proved in repository.

**Certainty:** high internally.

For `m=min D`,

```math
\mathcal B(D)
=
\{d-m:d\in D,\ d>m\}
```

is four-term-progression-free, lies in `[1,N)`, has size `|D|-1`, and satisfies `d-m<=d/2`.

---

## CL-004: Strongest one-generation inequalities

**Status:** proved in repository.

**Certainty:** medium-high.

The raw middle family and backbone give

```math
\boxed{
H(\mathcal B(D))
+
\sum_xH(M_x)
\ge
3H(D)
-
2\frac{r_3(N)}N
-
\frac1N.
}
```

For distinct middle steps `Q` and center-difference children `Xi_q`,

```math
\boxed{
|Q|+
\sum_q|\Xi_q|=K.
}
```

Combining these fibers with the backbone gives

```math
\boxed{
H(Q)
+
\sum_qH(\Xi_q)
+
H(\mathcal B(D))
\ge
2H(D)
-
\frac{r_3(N)}N
-
\frac1N.
}
```

The genealogy remains binary.

---

## CL-005: Shell resolution is mandatory

**Status:** required interface condition.

**Certainty:** high.

Every child must be partitioned into standard dyadic shells before deletion is reapplied. A progression crossing shell boundaries is not a recursive terminal event.

---

## CL-006: Half-contraction and positive moments

**Status:** proved in repository.

**Certainty:** medium-high for one step; medium for full multigeneration use.

Every parent creates at most two outputs, each at most half its label. Therefore, for `p>=1`,

```math
\boxed{
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
}
```

Across the full tree,

```math
\boxed{
\sum_q\mu(q)q^p
\le
2^{1-p}\sum_{a\text{ root}}a^p.
}
```

---

## CL-007: Global multiplicity compression

**Status:** proved in repository.

**Certainty:** medium-high.

Copies at different lifted centers, root anchors, and predecessor anchors are exported by translated four-term-progression-free layers. Copies with one fixed complete anchor history obey

```math
\boxed{
\lambda_{x,q}(t)(a-t)\le a.
}
```

High unresolved multiplicity is localized immediately below the root sponsor.

---

## CL-008: Sharp one-step aligned diamond

**Status:** proved and computationally verified.

**Certainty:** high for the finite certificate.

The block

```math
N+\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

produces two copies of `16,21,26` with the same root anchor: one in a middle multiplicity fiber and one in the backbone.

**Consequence:** the one-parent binary bound `2` is sharp.

---

## CL-009: Self-replicating aligned diamonds

**Status:** proved in repository; finite instances computationally verified.

**Certainty:** medium-high for the recursive interpretation.

There are four-term-progression-free states with

```math
P_h=2^h,
\qquad
|S_h|=\frac{9\cdot3^h-3}{2}.
```

Hence

```math
P_h\asymp|S_h|^{\log_3 2}.
```

Bounded, logarithmic, polylogarithmic, and subpower persistence bounds below exponent `log_3 2` are false in terms of parent cardinality alone.

---

## CL-010: Scale-eight infinite family

**Status:** computer-assisted exact construction.

**Certainty:** high for the finite-state certificate; medium-high for the full interpretation pending independent review.

There are four-term-progression-free states

```math
S_h\subseteq[L_h,2L_h),
\qquad
L_h=8^{h+1},
```

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h=\frac12L_h^{1/3}.
```

A 34-state base-eight automaton and a `17238`-state product/carry search certify the infinite family.

---

## CL-011: Exact equal-translate model is sharply classified

**Status:** proved by elementary progression, shell, and cardinality arguments.

**Certainty:** high internally.

A four-term-progression-free equal-translate state has at most three layers. The occurrence genealogy is binary, so one parent has at most two persistent children.

Exact backbone reproduction forces

```math
\boxed{L'\ge8L.}
```

Writing `alpha_h=|S_h|/L_h`,

```math
\boxed{
P_h\alpha_h
\le
C_0\left(\frac34\right)^h
=
C_0P_h^{\log_2 3-2},
}
```

and

```math
\boxed{
\sum_hP_h\alpha_h\le4C_0.
}
```

The scale-eight family attains the exponents.

**Caveat:** this does not control contaminated backbones.

---

## CL-012: Finite contaminated depth-five burst

**Status:** exact finite computer-assisted construction.

**Certainty:** high for the finite certificate; medium-high for the identical-history interpretation.

The scale-factor sequence is

```math
\boxed{4,8,4,4.}
```

with

```math
W_1=\frac38,
\qquad
W_5=\frac{273}{256},
```

and

```math
\boxed{
\frac{W_5}{W_1}=\frac{91}{32}.
}
```

**Consequence:** universal local contraction and contraction over every four-generation window are false.

---

## CL-013: `S_5` has no factor-two or factor-four continuation

**Status:** exact finite exhaustive search.

**Certainty:** high for the stated model.

For the recorded depth-five state,

```math
\boxed{N_{5,2}=N_{5,4}=0.}
```

Every continuation in the standard-dyadic disjoint three-translate replay model therefore terminates or uses scale factor at least `8`.

---

## CL-014: Recovery from `S_5` is path-dependent

**Status:** exact finite computer-assisted constructions.

**Certainty:** high for the finite branches.

The smallest exact recovery `R_5=65547` is followed by another forced expensive step and satisfies

```math
\frac{W_7}{W_5}\le\frac{205}{364}.
```

However, the alternative exact recovery `R_5=93476` admits the factor-four descendant `R_6=230164`, giving

```math
\boxed{
\frac{W_7}{W_5}=\frac{205}{182}>1.
}
```

**Consequence:** universal two-generation recovery and contraction over every six-generation window are false.

---

## CL-015: Complete cheap-extension exclusion from `S_7`

**Status:** exact finite computer-assisted theorem with structural witnesses.

**Certainty:** high for the finite domain.

```math
\boxed{N_{7,2}=N_{7,4}=0.}
```

The factor-four domain contains `359419` disjoint candidates, covered by:

```text
352979 completion witnesses
215 pattern 1001 witnesses
6225 pattern 0011 witnesses.
```

---

## CL-016: Exact depth-eight continuation

**Status:** exact finite computer-assisted construction.

**Certainty:** high for the finite certificate.

The first valid exact factor-eight continuation from `S_7` is

```math
\boxed{R_7=2097164.}
```

It gives

```math
S_8\subseteq[8388608,16777216),
\qquad
|S_8|=29523,
\qquad
P_8^{\mathrm{cert}}=256,
```

and

```math
\boxed{
W_8=\frac{29523}{32768}.
}
```

The scale sequence through this state is

```math
4,8,4,4,8,4,8.
```

---

## CL-017: Complete cheap-extension exclusion from `S_8`

**Status:** exact finite computer-assisted theorem with structural witnesses.

**Certainty:** high for the finite domain and recorded intermediate hashes.

```math
\boxed{N_{8,2}=N_{8,4}=0.}
```

### Factor two

```text
724204 sponsor-compatible candidates
172448 disjoint candidates
172448 completion witnesses.
```

### Factor four

```text
6316609 sponsor-compatible candidates
4190292 disjoint candidates
3442176 completion witnesses
73 pattern 1001 witnesses
748043 candidates passed to the pattern 0011 join.
```

The `0011` join is reproduced in five bounded-memory phases:

```text
748043 -> 27182 -> 1266 -> 45 -> 4 -> 3.
```

The final three separations have explicit `0011` witnesses. No candidate survives.

**Consequence:** any ninth state must satisfy

```math
\boxed{
W_9\le\frac{22143}{32768},
\qquad
\frac{W_9}{W_8}\le\frac{7381}{9841}.
}
```

**Primary references:**

- `docs/depth-eight-no-cheap-extension.md`;
- `src/verify_depth8_no_cheap_extension.cpp`;
- `src/run_verify_depth8_no_cheap_extension.sh`;
- `data/depth8_no_cheap_extension_certificate_2026-07-11.txt`.

---

## CL-018: Exact depth-nine continuation

**Status:** exact finite computer-assisted construction.

**Certainty:** high for the finite certificate.

The exact candidate

```math
R=2L_8=16777216
```

is invalid, with witness

```math
0,
8388608,
16777216,
25165824.
```

The next sponsor-compatible separation is the first valid exact recovery:

```math
\boxed{R_8=16777217.}
```

It produces

```math
S_9\subseteq[67108864,134217728),
\qquad
|S_9|=88572,
\qquad
P_9^{\mathrm{cert}}=512,
```

with scale sequence

```math
\boxed{4,8,4,4,8,4,8,8.}
```

and

```math
\boxed{
W_9=\frac{22143}{32768},
\qquad
\frac{W_9}{W_8}=\frac{7381}{9841}.
}
```

Thus the upper bound from CL-017 is attained.

**Primary references:**

- `docs/contaminated-backbone-depth-nine-chain.md`;
- `src/verify_contaminated_backbone_depth9.cpp`;
- `data/contaminated_backbone_depth9_certificate_2026-07-11.txt`.

---

# Superseded or explicitly false targets

Do not use the following without new hypotheses:

1. bounded or polylogarithmic identical-anchor-history persistence;
2. a subpower persistence bound below exponent `log_3 2` in terms of parent cardinality;
3. universal one-step `3/4` contraction for contaminated backbones;
4. universal strict contraction at every non-exact step;
5. contraction over every block of four outer steps;
6. contraction over every block of six outer steps;
7. a universal two-generation recovery theorem after an exact factor-eight step;
8. extrapolating one recovery branch to every recovery;
9. recursive arguments that ignore mandatory dyadic shell resolution;
10. treating finite repayment on the recorded branch as a state-independent long-run theorem.

---

# Open bottleneck OB-001: Long-run continuation tree

The recorded branch has scale pattern

```math
4,8,4,4,8,4,8,8.
```

It contains a cheap contaminated release followed by two consecutive forced exact factor-eight repayments. The finite branch nevertheless remains above its base weighted density.

The active question is

```math
\boxed{
\text{does every infinite continuation path have long-run average scale growth greater than }6?
}
```

Approved next targets:

1. classify factor-two and factor-four continuations of `S_9`;
2. determine whether another cheap release occurs after the two consecutive factor-eight steps;
3. construct a contamination-debt potential that permits delayed release but forces repayment;
4. control the entire continuation tree rather than one selected path;
5. obtain a finite-state or spectral classification with subcritical long-run growth;
6. prove an aggregate packing theorem for overlapping replay cores.

No current theorem closes this gap. The full Erdős problem remains unresolved.
