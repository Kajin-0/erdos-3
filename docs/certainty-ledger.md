# Certainty ledger

This file records claims that should survive context loss. The full Erdős reciprocal-sum problem remains open. The authoritative dependency order is in `docs/current-proof-program.md`.

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

## CL-002: One-generation recursion

**Status:** proved in repository.

**Certainty:** medium-high.

For a four-term-progression-free block `D subseteq[N,2N)`, coordinated deletion leaves a three-term-progression-free residual of size `s<=r_3(N)` and removes `K=|D|-s` sponsors.

The minimum-translation backbone is four-term-progression-free, lies in `[1,N)`, has size `|D|-1`, and satisfies `d-m<=d/2`.

The raw occurrence inequality is

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

The exact middle-fiber identity is

```math
\boxed{
|Q|+
\sum_q|\Xi_q|=K.
}
```

The strongest multiplicity-resolving inequality is

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

---

## CL-003: Shell resolution and global compression

**Status:** proved or required as stated.

**Certainty:** medium-high.

Every child must be resolved into standard dyadic shells before recursion. Every parent creates at most two outputs, each at most half its label. For `p>=1`,

```math
\boxed{
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
}
```

Across the tree,

```math
\boxed{
\sum_q\mu(q)q^p
\le
2^{1-p}\sum_{a\text{ root}}a^p.
}
```

Copies at different centers and anchors are exported by translated layers. Same-anchor copies obey

```math
\boxed{
\lambda_{x,q}(t)(a-t)\le a.
}
```

---

## CL-004: Self-replicating aligned diamonds

**Status:** proved in repository; finite instances computationally verified.

**Certainty:** medium-high.

There are four-term-progression-free states with

```math
|S_h|=rac{9\cdot3^h-3}{2},
\qquad
P_h=2^h.
```

Thus

```math
P_h\asymp|S_h|^{\log_3 2}.
```

Bounded, logarithmic, polylogarithmic, and sufficiently small subpower persistence bounds are false in terms of parent cardinality alone.

---

## CL-005: Exact scale-eight family

**Status:** computer-assisted exact construction.

**Certainty:** high for the finite-state certificate; medium-high for the interpretation pending independent review.

There are four-term-progression-free states with

```math
L_h=8^{h+1},
\qquad
|S_h|=rac{9\cdot3^h-3}{2},
\qquad
P_h=2^h=\frac12L_h^{1/3}.
```

A 34-state base-eight automaton recognizes the union. The exact product/carry search explores `17238` states and finds no nontrivial four-term progression.

**Verifier:** `src/verify_scale_eight_aligned_diamond.py`.

**Certificate signature:**

```text
e08c121adfee8cfa635ccb11d65c8519604611865ba504237f84896f908d757d
```

---

## CL-006: Exact equal-translate model is sharply classified

**Status:** proved by elementary progression, shell, and cardinality arguments.

**Certainty:** high internally.

The exact model satisfies

```math
\boxed{L'\ge8L,}
```

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

**Caveat:** this does not control contaminated descendants after an exact step.

---

## CL-007: Finite contaminated depth-five burst

**Status:** exact finite computer-assisted construction.

**Certainty:** high for the finite certificate; medium-high for the recursive interpretation pending independent review.

The scale factors are

```math
\boxed{4,8,4,4.}
```

For

```math
W_h=P_h^{\mathrm{cert}}\frac{|S_h|}{L_h},
```

```math
W_1=\frac38,
\qquad
W_5=\frac{273}{256},
```

so

```math
\boxed{
\frac{W_5}{W_1}=\frac{91}{32}.
}
```

Universal local contraction and contraction over every four-generation window are false.

---

## CL-008: Smallest-recovery branch

**Status:** exact finite computer-assisted search.

**Certainty:** high for the finite domains.

The depth-five state has

```math
N_{5,2}=N_{5,4}=0.
```

For the first exact recovery `R_5=65547`, the recovered state again has no factor-two or factor-four continuation. Along this selected branch,

```math
\frac{W_7}{W_5}\le\frac{205}{364}.
```

**Caveat:** this is branch-specific.

---

## CL-009: Alternative depth-seven branch

**Status:** exact finite computer-assisted construction.

**Certainty:** high for the construction and hashes; medium-high for the recursive interpretation pending independent review.

The alternative exact recovery

```math
R_5=93476
```

admits the factor-four continuation

```math
R_6=230164.
```

The scale sequence is

```math
\boxed{4,8,4,4,8,4.}
```

The resulting state satisfies

```math
|S_7|=9840,
\qquad
P_7^{\mathrm{cert}}=128,
\qquad
W_7=\frac{615}{512}.
```

Therefore

```math
\boxed{
\frac{W_7}{W_5}=\frac{205}{182}>1.
}
```

Universal two-generation recovery and contraction over every six-generation window are false.

---

## CL-010: Complete cheap-extension exclusion from `S_7`

**Status:** exact finite computer-assisted theorem with structural witnesses.

**Certainty:** high for the candidate domains, difference filter, and witness identities.

The factor-two search gives

```math
N_{7,2}=0.
```

For factor four:

```text
maximum separation = 1086317
sponsor-compatible candidates = 724212
layer-disjoint candidates = 359419.
```

All disjoint candidates have explicit witnesses:

```text
completion witnesses = 352979
layer-pattern 1001 witnesses = 215
layer-pattern 0011 witnesses = 6225.
```

Thus

```math
\boxed{N_{7,4}=0.}
```

Every continuation from `S_7` terminates or has scale factor at least `8`.

**Verifier:** `src/verify_depth7_no_factor4_extension.cpp`.

**Certificate:** `data/depth7_no_factor4_certificate_2026-07-11.txt`.

---

## CL-011: Exact depth-eight continuation

**Status:** exact finite computer-assisted construction.

**Certainty:** high for the finite construction, exact-backbone identity, first-valid search, and state hashes; medium-high for the recursive interpretation pending independent review.

The first valid exact factor-eight continuation from `S_7` is

```math
\boxed{R_7=2097164.}
```

It produces

```math
S_8\subseteq[8388608,16777216),
\qquad
|S_8|=29523,
\qquad
P_8^{\mathrm{cert}}=256.
```

The full scale sequence is

```math
\boxed{4,8,4,4,8,4,8.}
```

The weighted density is

```math
\boxed{
W_8=\frac{29523}{32768}.
}
```

The final exact factor-eight step satisfies

```math
\boxed{
\frac{W_8}{W_7}=\frac{9841}{13120}.
}
```

Across the three-generation recovery block beginning at `S_5`,

```math
\boxed{
\frac{W_8}{W_5}=\frac{757}{896}<1.
}
```

Relative to the base,

```math
\frac{W_8}{W_1}=\frac{9841}{4096}>1.
```

Thus the cheap depth-seven release is repaid locally, but the complete finite path still has elevated weighted density relative to the base.

**Verifier:** `src/verify_contaminated_backbone_depth8.cpp`.

**Primary note:** `docs/contaminated-backbone-depth-eight-chain.md`.

**Certificate:** `data/contaminated_backbone_depth8_certificate_2026-07-11.txt`.

**Caveat:** factor-two and factor-four continuation domains from `S_8` are not yet classified. Random sampling is not a certificate.

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
9. recursive arguments that ignore mandatory dyadic shell resolution.

---

# Open bottleneck OB-001: Repeated release cycles

The known branch exhibits

```math
\text{exact recovery}
\to
\text{cheap contaminated release}
\to
\text{forced exact recovery}.
```

The active question is

```math
\boxed{
\text{can this release cycle repeat indefinitely with average scale growth at most }6?
}
```

Approved next targets:

1. classify factor-two and factor-four continuations of `S_8`;
2. if another cheap descendant exists, extend and certify the cycle;
3. explain why the depth-seven contamination creates enough completion and equal-difference witnesses to force recovery;
4. construct a contamination-debt potential that permits delayed release but forces repayment;
5. prove every infinite path has geometric-mean scale expansion greater than `6`;
6. obtain a finite-state or spectral classification with subcritical long-run growth;
7. prove an aggregate packing theorem for overlapping replay cores.

No current theorem closes this gap. The full Erdős problem remains unresolved.
