# Certainty ledger

This file records claims that should survive context loss. Each entry states status, certainty, audit state, consequence, and the controlling caveat.

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

is four-term-progression-free, lies in `[1,N)`, has size `|D|-1`, and every associated label satisfies

```math
d-m\le d/2.
```

**Primary note:** `docs/minimum-translation-backbone-recursion.md`.

---

## CL-004: Raw binary factor three

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

The full middle family and minimum-translation backbone give

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

**Audit state:** awaiting independent review.

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

## CL-009: Lifted-center layer decomposition

**Status:** proved in repository.

**Certainty:** medium-high.

Let `nu_q(x)` count terminal copies of step `q` lifting to center `x`, and let `L(q)=max_x nu_q(x)`. Then translated center layers `Omega_{q,k}` satisfy

```math
\boxed{
\mu(q)
=
L(q)
+
\sum_{k=1}^{L(q)}|\Omega_{q,k}|.
}
```

Every repeated label occurring at a different lifted center is exported.

---

## CL-010: Root-anchor and predecessor-anchor layer decompositions

**Status:** proved in repository.

**Certainty:** medium-high.

Copies of one exact lifted progression occurring at different root anchors are exported by translated anchor layers. The process iterates backward through predecessor anchors.

For one fixed predecessor transition,

```math
\boxed{
c_{x,q,t}(p)(a-p)\le a.
}
```

**Primary notes:**

- `docs/state-anchor-layer-and-antichain-budget.md`;
- `docs/predecessor-anchor-layer-resolution.md`.

---

## CL-011: Same-anchor antichain budget

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

## CL-012: Sharp one-step aligned diamond

**Status:** proved in repository and computationally verified.

**Certainty:** high for the finite certificate.

The block

```math
N+\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

is four-term-progression-free and produces two copies of the progression

```math
16,21,26
```

with the same root anchor: one in a middle multiplicity fiber and one in the minimum-translation backbone.

**Consequence:** the one-parent binary bound `2` is sharp.

---

## CL-013: Self-replicating aligned diamonds

**Status:** proved in repository; finite instances computationally verified.

**Certainty:** medium-high for the recursive construction.

There are four-term-progression-free states `S_h` producing

```math
P_h=2^h
```

copies of the same exact local progression with the same complete anchor history, with

```math
|S_h|
=
\frac{9\cdot3^h-3}{2}.
```

Therefore

```math
P_h\asymp|S_h|^{\log_3 2}.
```

**Consequence:** bounded, logarithmic, polylogarithmic, and subpower persistence bounds below exponent `log_3 2` are false in terms of parent cardinality.

---

## CL-014: Scale-eight infinite aligned-diamond family

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
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h.
```

Thus

```math
\boxed{
P_h=\frac12L_h^{1/3}.
}
```

A 34-state base-eight automaton recognizes the union. The exact product/carry search explores 17,238 reachable states and reaches no accepting nontrivial four-term progression.

**Verifier:** `src/verify_scale_eight_aligned_diamond.py`.

**Primary note:** `docs/scale-eight-self-replicating-aligned-diamond.md`.

**Certificate signature:**

```text
e08c121adfee8cfa635ccb11d65c8519604611865ba504237f84896f908d757d
```

---

## CL-015: Exact equal-translate model is sharply classified

**Status:** proved by elementary progression, shell, and cardinality arguments.

**Certainty:** high internally.

**Audit state:** awaiting independent review.

A four-term-progression-free equal-translate state has at most three layers, because four layers contain

```math
0,R,2R,3R.
```

The occurrence genealogy is binary, so one parent has at most two persistent children.

If the backbone reproduces the previous state exactly, then `R>=2L`, and standard dyadic shelling forces

```math
\boxed{L'\ge8L.}
```

Consequently

```math
\boxed{
P_h\le\left(\frac{L_h}{L_0}\right)^{1/3}.
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

The scale-eight family attains the exponents. The exact model is therefore sharply classified.

**Primary notes:**

- `docs/three-translate-dyadic-scale-barrier.md`;
- `docs/exact-three-translate-weighted-density-theorem.md`.

**Caveat:** this does not control contaminated backbones.

---

## CL-016: Finite contaminated-backbone depth-five chain

**Status:** exact finite computer-assisted construction.

**Certainty:** high for the finite certificate; medium-high for the identical-history interpretation pending independent review.

There are four-term-progression-free states

```math
S_h\subseteq[L_h,2L_h),
\qquad 1\le h\le5,
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

and the backbone contamination counts are

```math
4,1,33,1.
```

For

```math
W_h
=
P_h^{\mathrm{cert}}\frac{|S_h|}{L_h},
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

# Superseded or explicitly false targets

Do not use the following without new hypotheses:

1. bounded or polylogarithmic identical-anchor-history persistence;
2. a subpower persistence bound below exponent `log_3 2` in terms of parent cardinality;
3. a universal one-step `3/4` contraction when the backbone merely contains the replay state;
4. universal strict contraction at every non-exact step;
5. contraction over every block of four consecutive outer steps;
6. a local near-exact/defective dichotomy in which every departure from exact reproduction immediately pays a stronger contraction;
7. recursive arguments that ignore mandatory dyadic shell resolution.

---

# Open bottleneck OB-001: Long-run contamination compensation

The exact equal-translate obstruction is controlled, but contaminated backbones can support short bursts of cheap replication during which multiplicity-weighted density grows.

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
\text{prove long-run compensation for cheap contaminated-backbone replication.}
}
```

Approved target forms:

1. cumulative scale expansion eventually exceeds the `6`-per-generation threshold;
2. contamination creates exportable lower-scale difference mass;
3. repeated cheap steps force a four-term progression;
4. repeatable patterns admit a finite-state or spectral classification with subcritical growth;
5. overlap among contaminated replay cores obeys an aggregate packing theorem.

The immediate computational question is whether cheap scale-factor patterns extend indefinitely, periodically, or only through bounded bursts.

No current theorem closes this gap. The full Erdős problem remains unresolved.
