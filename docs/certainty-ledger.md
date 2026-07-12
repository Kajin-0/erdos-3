# Certainty ledger

This file records claims that should survive context loss. Each entry states status, certainty, consequence, and the controlling caveat.

The full Erdős reciprocal-sum problem remains open. The authoritative theorem dependency order is in `docs/current-proof-program.md`.

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

**Audit state:** awaiting independent review.

For a four-term-progression-free block `D subseteq[N,2N)`, coordinated side-anchor deletion removes

```math
K=|D|-s
```

sponsors and leaves a three-term-progression-free residual of size

```math
s\le r_3(N).
```

Every deleted sponsor creates one selected middle-step occurrence `q<=N/2`.

---

## CL-003: Minimum-translation backbone

**Status:** proved in repository.

**Certainty:** high internally.

**Audit state:** awaiting independent review.

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

**Primary note:** `docs/minimum-translation-backbone-recursion.md`.

---

## CL-004: Raw binary factor three

**Status:** proved in repository.

**Certainty:** medium-high.

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

**Caveat:** equal numerical labels are counted repeatedly.

---

## CL-005: Exact within-state middle multiplicity fibers

**Status:** proved in repository.

**Certainty:** medium-high.

For distinct selected steps `Q` and center-difference children `Xi_q`,

```math
\boxed{
|Q|+
\sum_q|\Xi_q|
=K.
}
```

Every additional copy of a selected middle step becomes a lower-scale four-term-progression-free child.

---

## CL-006: Binary multiplicity-resolving factor two

**Status:** proved in repository.

**Certainty:** medium-high.

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

## CL-007: Shell resolution is mandatory

**Status:** required interface condition.

**Certainty:** high.

Every child in `[1,N)` must be partitioned into standard dyadic shells before deletion is reapplied. A progression crossing shell boundaries is not a recursive terminal event.

---

## CL-008: Half-contraction and positive moments

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

Recursive depth is logarithmic.

---

## CL-009: Lifted-center, root-anchor, and predecessor decompositions

**Status:** proved in repository.

**Certainty:** medium-high.

Copies of one numerical label occurring at different lifted centers, root anchors, or predecessor anchors are exported into translated lower-scale four-term-progression-free children.

For one fixed predecessor transition,

```math
\boxed{
c_{x,q,t}(p)(a-p)\le a.
}
```

**Primary notes:**

- `docs/global-lifted-center-layer-resolution.md`;
- `docs/state-anchor-layer-and-antichain-budget.md`;
- `docs/predecessor-anchor-layer-resolution.md`.

---

## CL-010: Same-anchor antichain budget

**Status:** proved in repository.

**Certainty:** medium-high.

For root sponsor `a` and anchor `t`,

```math
\boxed{
\lambda_{x,q}(t)(a-t)
\le a.
}
```

Hence

```math
\lambda_{x,q}(t)\ge m
\quad\Longrightarrow\quad
 t\ge a\left(1-\frac1m\right).
```

High unresolved persistence is localized immediately below the sponsor.

---

## CL-011: Sharp one-step aligned diamond

**Status:** proved in repository and computationally verified.

**Certainty:** high for the finite certificate.

The block

```math
N+
\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

is four-term-progression-free and produces two copies of

```math
16,21,26
```

with the same root anchor: one in a middle multiplicity fiber and one in the minimum-translation backbone.

**Consequence:** the one-parent binary bound `2` is sharp.

---

## CL-012: Self-replicating aligned diamonds

**Status:** proved in repository; finite instances computationally verified.

**Certainty:** medium-high for the recursive construction.

There are four-term-progression-free states with

```math
P_h=2^h,
\qquad
|S_h|=
\frac{9\cdot3^h-3}{2}.
```

Therefore

```math
P_h\asymp|S_h|^{\log_3 2}.
```

**Consequence:** bounded, logarithmic, polylogarithmic, and subpower persistence bounds below exponent `log_3 2` are false in terms of parent cardinality.

---

## CL-013: Scale-eight infinite aligned-diamond family

**Status:** computer-assisted exact construction.

**Certainty:** high for the finite-state certificate; medium-high for the full interpretation pending independent review.

There are four-term-progression-free states

```math
S_h\subseteq[L_h,2L_h)
```

with

```math
L_h=8^{h+1},
\qquad
|S_h|=
\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h.
```

Thus

```math
\boxed{
P_h=\frac12L_h^{1/3}.
}
```

A 34-state base-eight automaton recognizes the union. The exact product/carry search explores `17238` reachable states and reaches no accepting nontrivial four-term progression.

**Verifier:** `src/verify_scale_eight_aligned_diamond.py`.

**Primary note:** `docs/scale-eight-self-replicating-aligned-diamond.md`.

**Certificate signature:**

```text
e08c121adfee8cfa635ccb11d65c8519604611865ba504237f84896f908d757d
```

---

## CL-014: Exact equal-translate model is sharply classified

**Status:** proved by elementary progression, shell, and cardinality arguments.

**Certainty:** high internally.

**Audit state:** awaiting independent review.

A four-term-progression-free equal-translate state has at most three layers, because four layers contain

```math
0,R,2R,3R.
```

The occurrence genealogy is binary, so one parent has at most two persistent children.

If the backbone reproduces the previous state exactly, standard dyadic shelling forces

```math
\boxed{L'\ge8L.}
```

Consequently

```math
\boxed{
P_h\le
\left(\frac{L_h}{L_0}\right)^{1/3}.
}
```

Writing `alpha_h=|S_h|/L_h` and `C_0=(|S_0|+3/2)/L_0`,

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
\sum_{h\ge0}P_h\alpha_h\le4C_0.
}
```

The scale-eight family attains the exponents. The exact model is sharply classified.

**Primary notes:**

- `docs/three-translate-dyadic-scale-barrier.md`;
- `docs/exact-three-translate-weighted-density-theorem.md`.

**Caveat:** this does not control contaminated backbones.

---

## CL-015: Finite contaminated-backbone depth-five burst

**Status:** exact finite computer-assisted construction.

**Certainty:** high for the finite certificate; medium-high for the identical-history interpretation pending independent review.

There are four-term-progression-free states

```math
S_h\subseteq[L_h,2L_h),
\qquad
1\le h\le5,
```

with scales

```math
(64,256,2048,8192,32768)
```

and separations

```math
(61,303,1597,8195).
```

The outer dyadic scale factors are

```math
\boxed{4,8,4,4.}
```

At each step, the middle fiber is exactly the previous state, while the relevant backbone shell contains the previous state plus additional points. The verified deletion schedule can be replayed inside that subset, and both continuations inherit the same new root anchor.

Thus

```math
P_h^{\mathrm{cert}}=2^h
```

is a certified lower bound.

The state cardinalities are

```math
12,39,120,363,1092,
```

and the contamination counts are

```math
4,1,33,1.
```

For

```math
W_h
=
P_h^{\mathrm{cert}}
\frac{|S_h|}{L_h},
```

one has

```math
W_1=\frac38,
\qquad
W_5=\frac{273}{256},
```

so

```math
\boxed{
\frac{W_5}{W_1}
=
\frac{91}{32}.
}
```

**Verifier:** `src/verify_contaminated_backbone_depth5.py`.

**Primary note:** `docs/contaminated-backbone-depth-five-chain.md`.

**Certificate:** `data/contaminated_backbone_depth5_certificate_2026-07-11.txt`.

**Caveat:** the construction is finite. It does not prove indefinite extension, long-run growth, or a divergent reciprocal-sum counterexample.

---

## CL-016: Finite forced recovery after the depth-five burst

**Status:** exact finite computer-assisted search and elementary weighted-density consequence.

**Certainty:** high for the finite search domains and recorded hashes; medium-high for the recursive interpretation pending independent review.

The depth-five state has

```math
L_5=32768,
\qquad
|S_5|=1092,
```

and hash

```text
a315deca0997d946ca9bb5058d2a04bfe3e585332d4db5260e7d9edc9142f841
```

Every sponsor-compatible disjoint three-translate continuation was tested at dyadic factors `2` and `4`:

```math
\boxed{N_{5,2}=0,}
\qquad
\boxed{N_{5,4}=0.}
```

The factor-two domain contains `622` candidates. The factor-four domain contains `22467` candidates.

The first valid sponsor-compatible exact-backbone factor-eight recovery is

```math
\boxed{R_5^*=65547.}
```

It produces

```math
S_6\subseteq[262144,524288),
\qquad
|S_6|=3279,
```

with hash

```text
ff10f8482f475206eba84c4cbbcef48ec0402ec1870edf81575495b9aae7d463
```

Every factor-two and factor-four continuation of this selected `S_6` was then tested:

```math
\boxed{N_{6,2}=0,}
\qquad
\boxed{N_{6,4}=0.}
```

The factor-two domain contains `22459` candidates. The factor-four domain contains `197222` candidates.

Therefore any next continuation either terminates or has scale factor at least `8`.

The selected first recovery and any possible next continuation satisfy

```math
\frac{W_6}{W_5}
=
\frac{1093}{1456},
```

```math
\frac{W_7}{W_6}
\le
\frac{820}{1093},
```

and hence

```math
\boxed{
\frac{W_7}{W_5}
\le
\frac{205}{364}
\approx0.563187.
}
```

Equivalently,

```math
\boxed{W_7\le\frac{615}{1024}}
```

if a seventh state exists in this model.

**Verifier:** `src/verify_forced_recovery_after_depth5.py`.

**Primary note:** `docs/forced-recovery-after-depth-five.md`.

**Certificate:** `data/forced_recovery_after_depth5_certificate_2026-07-11.txt`.

**Consequence:** the explicit cheap burst `4,8,4,4` is followed, along its first exact recovery, by the finite compensation block `8,>=8` or termination.

**Caveat:** this is state-specific. It does not prove that every factor-eight continuation of `S_5`, or every contaminated genealogy, has the same recovery behavior.

---

# Superseded or explicitly false targets

Do not use the following without new hypotheses:

1. bounded or polylogarithmic identical-anchor-history persistence;
2. a subpower persistence bound below exponent `log_3 2` in terms of parent cardinality;
3. universal one-step `3/4` contraction when the backbone merely contains the replay state;
4. universal strict contraction at every non-exact step;
5. contraction over every block of four consecutive outer steps;
6. a local near-exact/defective dichotomy in which every departure from exact reproduction immediately pays a stronger contraction;
7. recursive arguments that ignore mandatory dyadic shell resolution;
8. extrapolating the finite forced-recovery block to every factor-eight continuation or every contaminated state.

---

# Open bottleneck OB-001: State-independent long-run contamination compensation

The exact equal-translate obstruction is controlled. Contaminated backbones can support short bursts of cheap replication during which multiplicity-weighted density grows. One explicit burst is followed by a certified finite recovery block, but no state-independent theorem is known.

For disjoint three-translate growth,

```math
\frac{W_{h+1}}{W_h}
=
\frac{6}{c_h}
\left(1+\frac1{|S_h|}\right),
\qquad
c_h=\frac{L_{h+1}}{L_h}.
```

Ignoring the lower-order term, long-run contraction requires geometric-mean scale expansion greater than `6`.

The active target is

```math
\boxed{
\text{prove state-independent long-run compensation for cheap contaminated-backbone replication.}
}
```

Approved target forms:

1. cumulative scale expansion eventually exceeds the `6`-per-generation threshold;
2. contamination creates exportable lower-scale difference mass;
3. repeated cheap steps force a four-term progression;
4. repeatable patterns admit a finite-state or spectral classification with subcritical growth;
5. overlap among contaminated replay cores obeys an aggregate packing theorem;
6. a monotone contamination-debt potential forces recovery or termination.

The immediate computational target is to classify all valid factor-eight continuations of `S_5` by whether they admit factor-two or factor-four successors.

No current theorem closes the state-independent gap. The full Erdős problem remains unresolved.
