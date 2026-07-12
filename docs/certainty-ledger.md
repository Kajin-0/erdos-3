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

is four-term-progression-free, lies in `[1,N)`, has size `|D|-1`, and satisfies

```math
d-m\le d/2.
```

---

## CL-004: Strongest one-generation inequalities

**Status:** proved in repository.

**Certainty:** medium-high.

The raw middle family and backbone satisfy

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

Equal numerical labels are counted repeatedly.

The exact within-state middle fibers satisfy

```math
\boxed{
|Q|+
\sum_q|\Xi_q|=K.
}
```

Combining them gives

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

Every child in `[1,N)` must be partitioned into standard dyadic shells before deletion is reapplied. A progression crossing shell boundaries is not a recursive terminal event.

---

## CL-006: Half-contraction and global compression

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
2^{1-p}
\sum_{a\text{ root}}a^p.
}
```

Copies at different centers, root anchors, and predecessor anchors are exported by translated layers. Copies with one fixed anchor obey

```math
\boxed{
\lambda_{x,q}(t)(a-t)\le a.
}
```

---

## CL-007: Self-replicating aligned diamonds

**Status:** proved in repository; finite instances computationally verified.

**Certainty:** medium-high for the recursive interpretation.

There are four-term-progression-free states with

```math
|S_h|=rac{9\cdot3^h-3}{2}
```

and identical-history persistence

```math
P_h=2^h.
```

Thus

```math
P_h\asymp|S_h|^{\log_3 2}.
```

Bounded, logarithmic, polylogarithmic, and sufficiently small subpower persistence bounds are false in terms of parent cardinality alone.

---

## CL-008: Scale-eight infinite family

**Status:** computer-assisted exact construction.

**Certainty:** high for the finite-state certificate; medium-high for the interpretation pending independent review.

There are four-term-progression-free states

```math
S_h\subseteq[L_h,2L_h)
```

with

```math
L_h=8^{h+1},
\qquad
|S_h|=rac{9\cdot3^h-3}{2},
\qquad
P_h=2^h.
```

Thus

```math
\boxed{
P_h=\frac12L_h^{1/3}.
}
```

A 34-state base-eight automaton recognizes the union. The exact product/carry search explores `17238` states and finds no nontrivial four-term progression.

**Verifier:** `src/verify_scale_eight_aligned_diamond.py`.

**Certificate signature:**

```text
e08c121adfee8cfa635ccb11d65c8519604611865ba504237f84896f908d757d
```

---

## CL-009: Exact equal-translate model is sharply classified

**Status:** proved by elementary progression, shell, and cardinality arguments.

**Certainty:** high internally.

A four-term-progression-free equal-translate state has at most three layers. The occurrence genealogy is binary. Exact backbone reproduction forces

```math
\boxed{L'\ge8L.}
```

Consequently

```math
\boxed{
P_h\le\left(\frac{L_h}{L_0}\right)^{1/3}.
}
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

The scale-eight family attains the exponents. The exact model is sharply classified.

**Caveat:** this does not control contaminated descendants after an exact step.

---

## CL-010: Finite contaminated depth-five burst

**Status:** exact finite computer-assisted construction.

**Certainty:** high for the finite certificate; medium-high for the identical-history interpretation pending independent review.

The scale factors are

```math
\boxed{4,8,4,4.}
```

with state sizes

```math
12,39,120,363,1092.
```

For

```math
W_h
=
P_h^{\mathrm{cert}}\frac{|S_h|}{L_h},
```

```math
W_1=\frac38,
\qquad
W_5=\frac{273}{256},
```

and

```math
\boxed{
\frac{W_5}{W_1}=rac{91}{32}.
}
```

Universal local contraction and contraction over every four-generation window are false.

**Verifier:** `src/verify_contaminated_backbone_depth5.py`.

---

## CL-011: Smallest-recovery branch

**Status:** exact finite computer-assisted search.

**Certainty:** high for the finite domains; medium-high for the recursive interpretation pending independent review.

The depth-five state has

```math
N_{5,2}=N_{5,4}=0.
```

For the first exact recovery

```math
R_5=65547,
```

the resulting state also has no factor-two or factor-four continuation. Along this selected branch,

```math
\frac{W_7}{W_5}
\le
\frac{205}{364}.
```

**Caveat:** this is branch-specific and does not describe every exact recovery from `S_5`.

---

## CL-012: Alternative depth-seven branch

**Status:** exact finite computer-assisted construction.

**Certainty:** high for the finite construction and state hashes; medium-high for the identical-history interpretation pending independent review.

The alternative exact recovery

```math
R_5=93476
```

admits the factor-four continuation

```math
R_6=230164.
```

The full scale sequence is

```math
\boxed{4,8,4,4,8,4.}
```

The resulting state has

```math
S_7\subseteq[1048576,2097152),
\qquad
|S_7|=9840,
\qquad
P_7^{\mathrm{cert}}=128.
```

Its weighted density is

```math
W_7=\frac{615}{512},
```

so

```math
\boxed{
\frac{W_7}{W_5}=rac{205}{182}>1
}
```

and

```math
\boxed{
\frac{W_7}{W_1}=rac{205}{64}.
}
```

Universal two-generation recovery and contraction over every six-generation window are false.

**Verifier:** `src/verify_contaminated_backbone_depth7.cpp`.

**Certificate:** `data/contaminated_backbone_depth7_certificate_2026-07-11.txt`.

---

## CL-013: Complete factor-two and factor-four exclusion from `S_7`

**Status:** exact finite computer-assisted theorem with structural witnesses.

**Certainty:** high for the finite candidate domains, difference filter, and witness identities; medium-high for the recursive consequence pending independent review.

The factor-two search gives

```text
25161 sponsor-compatible candidates
202 disjoint candidates
0 valid candidates.
```

Thus

```math
N_{7,2}=0.
```

For factor four,

```text
maximum separation = 1086317
sponsor-compatible candidates = 724212
disjoint candidates = 359419.
```

Every disjoint candidate has an explicit structural four-term-progression witness:

```text
completion witnesses = 352979
layer-pattern 1001 witnesses = 215
layer-pattern 0011 witnesses = 6225.
```

The witness count is exact:

```math
352979+215+6225=359419.
```

Therefore

```math
\boxed{N_{7,4}=0.}
```

Every continuation from this state either terminates or has scale factor at least `8`.

Since `|S_7|=9840`, every possible next continuation satisfies

```math
\boxed{
\frac{W_8}{W_7}
\le
\frac{9841}{13120}.
}
```

Hence, if `S_8` exists,

```math
\boxed{
W_8\le\frac{29523}{32768}
}
```

and

```math
\boxed{
\frac{W_8}{W_5}
\le
\frac{757}{896}<1.
}
```

**Verifier:** `src/verify_depth7_no_factor4_extension.cpp`.

**Primary note:** `docs/depth-seven-factor-four-exclusion.md`.

**Certificate:** `data/depth7_no_factor4_certificate_2026-07-11.txt`.

**Caveat:** this is state-specific. It does not prove state-independent long-run contraction.

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
8. extrapolating the smallest exact recovery branch to every recovery;
9. recursive arguments that ignore mandatory dyadic shell resolution.

---

# Open bottleneck OB-001: Continuation-graph control

The exact equal-translate obstruction is controlled, but contaminated descendants are path-dependent.

The active target is

```math
\boxed{
\text{control every path in the contaminated-backbone continuation graph.}
}
```

Known branch behavior:

1. the smallest exact recovery from `S_5` forces another expensive step or termination;
2. another exact recovery releases one factor-four step;
3. the released `S_7` then forbids factor two and factor four;
4. both known branches compensate relative to `S_5`, but no universal theorem is known.

Approved next targets:

1. find and classify factor-eight continuations of `S_7`;
2. determine whether their descendants release another cheap step;
3. explain structurally why completion and equal-difference witnesses force recovery from `S_7`;
4. construct a contamination-debt potential that permits delayed release but forces repayment;
5. prove every infinite path has geometric-mean scale expansion greater than `6`;
6. obtain a finite-state or spectral classification with subcritical long-run growth;
7. prove an aggregate packing theorem for overlapping replay cores.

No current theorem closes this gap. The full Erdős problem remains unresolved.
