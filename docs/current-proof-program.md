# Current proof program: backbone recursion and path-dependent compensation

## Status

This is the authoritative overview of the active program for Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. This repository studies the four-term case: prove that every four-term-progression-free subset of the positive integers has convergent reciprocal sum.

Recent theorem-style claims are proved internally or computationally certified as stated, but have not received independent expert review.

---

# 1. Dyadic reduction

For

```math
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j},
```

one has, up to absolute constants,

```math
\sum_{n\in A}\frac1n=\infty
\quad\Longleftrightarrow\quad
\sum_j\alpha_j=\infty.
```

A divergent four-term-progression-free candidate must satisfy

```math
\alpha_j\to0,
\qquad
\sum_j\alpha_j=\infty.
```

The closing argument must therefore control the aggregate contribution of sparse dyadic blocks.

---

# 2. One-generation recursion

For a four-term-progression-free block

```math
D\subseteq[N,2N),
```

coordinated side-anchor deletion removes

```math
K=|D|-s
```

sponsors and leaves a three-term-progression-free residual with

```math
s\le r_3(N).
```

For `m=min D`, the minimum-translation backbone

```math
\mathcal B(D)
=
\{d-m:d\in D,\ d>m\}
```

is four-term-progression-free, lies in `[1,N)`, has size `|D|-1`, and satisfies `d-m<=d/2`.

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

For distinct selected middle steps `Q` and translated center-difference children `Xi_q`,

```math
\boxed{
|Q|+
\sum_q|\Xi_q|=K.
}
```

Combining the fibers with the backbone gives

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

# 3. Shell interface and multiplicity compression

Every child must be partitioned into standard dyadic shells before deletion is reapplied. A progression crossing shell boundaries is not a recursive terminal event.

Every parent creates at most two retained outputs, each at most half its label. Hence, for `p>=1`,

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

Repeated labels at different centers, root anchors, and predecessor anchors are exported by translated layers. Copies with one fixed complete anchor history obey

```math
\boxed{
\lambda_{x,q}(t)(a-t)\le a.
}
```

High unresolved persistence is therefore localized immediately below the root sponsor.

**Primary references:**

- `docs/minimum-translation-backbone-recursion.md`;
- `docs/global-lifted-center-layer-resolution.md`;
- `docs/state-anchor-layer-and-antichain-budget.md`;
- `docs/predecessor-anchor-layer-resolution.md`;
- `docs/half-contraction-multiscale-label-potential.md`.

---

# 4. Self-replicating aligned diamonds

The base set

```math
H=\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

produces the terminal progression `16,21,26` in both a middle multiplicity fiber and the backbone.

A three-translate recursion gives four-term-progression-free states with

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h.
```

Thus

```math
P_h\asymp|S_h|^{\log_3 2}.
```

Bounded, logarithmic, polylogarithmic, and sufficiently small subpower persistence bounds are false in terms of parent cardinality alone.

**Primary reference:** `docs/self-replicating-aligned-diamond.md`.

---

# 5. Exact scale-eight model

There is a computer-certified infinite family with

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

A 34-state base-eight automaton recognizes the union, and an exact `17238`-state product/carry search finds no nontrivial four-term progression.

The exact standard-dyadic equal-translate model is sharply classified:

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

**Primary references:**

- `docs/scale-eight-self-replicating-aligned-diamond.md`;
- `docs/three-translate-dyadic-scale-barrier.md`;
- `docs/exact-three-translate-weighted-density-theorem.md`;
- `src/verify_scale_eight_aligned_diamond.py`.

---

# 6. Contaminated depth-five burst

A certified contaminated-backbone chain has scale factors

```math
\boxed{4,8,4,4.}
```

The middle fiber is exact at every step, and each backbone contains a replayable copy of the previous state.

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

so

```math
\boxed{
\frac{W_5}{W_1}=\frac{91}{32}.
}
```

Universal local contraction and contraction over every four-generation window are false.

**Primary references:**

- `docs/contaminated-backbone-depth-five-chain.md`;
- `src/verify_contaminated_backbone_depth5.py`.

---

# 7. Path-dependent recovery from `S_5`

The depth-five state admits no factor-two or factor-four continuation:

```math
\boxed{N_{5,2}=N_{5,4}=0.}
```

The smallest exact recovery `R_5=65547` produces a branch whose next state again has no factor-two or factor-four continuation. Along that selected branch,

```math
\frac{W_7}{W_5}\le\frac{205}{364}.
```

However, the alternative exact recovery

```math
R_5=93476
```

admits the factor-four descendant

```math
R_6=230164.
```

This produces

```math
S_7\subseteq[1048576,2097152),
\qquad
|S_7|=9840,
\qquad
P_7^{\mathrm{cert}}=128,
```

with

```math
W_7=\frac{615}{512},
```

and

```math
\boxed{
\frac{W_7}{W_5}=\frac{205}{182}>1.
}
```

Thus universal two-generation recovery and contraction over every six-generation window are false. Recovery behavior is path-dependent.

**Primary references:**

- `docs/forced-recovery-after-depth-five.md`;
- `docs/contaminated-backbone-depth-seven-chain.md`.

---

# 8. Complete cheap-extension exclusion from `S_7`

The depth-seven state has no factor-two or factor-four continuation:

```math
\boxed{N_{7,2}=N_{7,4}=0.}
```

The factor-four domain contains `359419` disjoint-layer candidates. Every one has an explicit witness:

```text
352979 completion witnesses
215 layer-pattern 1001 witnesses
6225 layer-pattern 0011 witnesses.
```

Every continuation from `S_7` therefore terminates or has scale factor at least `8`.

**Primary references:**

- `docs/depth-seven-factor-four-exclusion.md`;
- `src/verify_depth7_no_factor4_extension.cpp`;
- `data/depth7_no_factor4_certificate_2026-07-11.txt`.

---

# 9. Exact depth-eight continuation

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

The scale sequence through `S_8` is

```math
\boxed{4,8,4,4,8,4,8.}
```

Its weighted density is

```math
W_8=\frac{29523}{32768},
```

with

```math
\boxed{
\frac{W_8}{W_7}=\frac{9841}{13120},
}
```

and

```math
\boxed{
\frac{W_8}{W_5}=\frac{757}{896}<1.
}
```

The cheap release at depth seven is therefore repaid by the next exact factor-eight step.

**Primary references:**

- `docs/contaminated-backbone-depth-eight-chain.md`;
- `src/verify_contaminated_backbone_depth8.cpp`.

---

# 10. Complete cheap-extension exclusion from `S_8`

The complete finite domains satisfy

```math
\boxed{N_{8,2}=N_{8,4}=0.}
```

For factor two:

```text
724204 sponsor-compatible candidates
172448 disjoint-layer candidates
172448 completion witnesses.
```

For factor four:

```text
6316609 sponsor-compatible candidates
4190292 disjoint-layer candidates
3442176 completion witnesses
73 layer-pattern 1001 witnesses
748043 layer-pattern 0011 candidates, all resolved.
```

The `0011` join is certified in five bounded-memory phases, ending with three explicit terminal witnesses. No candidate survives.

Thus every continuation from `S_8` terminates or has scale factor at least `8`. Any ninth state must satisfy

```math
\boxed{
W_9\le\frac{22143}{32768},
}
```

```math
\boxed{
\frac{W_9}{W_8}\le\frac{7381}{9841},
}
```

and

```math
\boxed{
\frac{W_9}{W_5}\le\frac{7381}{11648}.
}
```

**Primary references:**

- `docs/depth-eight-no-cheap-extension.md`;
- `src/verify_depth8_no_cheap_extension.cpp`;
- `src/run_verify_depth8_no_cheap_extension.sh`;
- `data/depth8_no_cheap_extension_certificate_2026-07-11.txt`.

---

# 11. Exact depth-nine continuation

The exact candidate

```math
R=2L_8=16777216
```

is invalid because it contains

```math
0,
\quad8388608,
\quad16777216,
\quad25165824.
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
P_9^{\mathrm{cert}}=512.
```

The certified scale sequence is now

```math
\boxed{4,8,4,4,8,4,8,8.}
```

The weighted density is

```math
\boxed{
W_9=\frac{22143}{32768},
}
```

so the exclusion bound from the preceding section is attained:

```math
\boxed{
\frac{W_9}{W_8}=\frac{7381}{9841}
\approx0.750025.
}
```

Relative to `S_5`,

```math
\boxed{
\frac{W_9}{W_5}=\frac{7381}{11648}
\approx0.633671.
}
```

Relative to the base state,

```math
\frac{W_9}{W_1}=\frac{7381}{4096}>1.
```

The branch therefore exhibits one cheap release followed by two consecutive exact factor-eight repayments, but it remains above the base weighted density after eight outer generations.

**Primary references:**

- `docs/contaminated-backbone-depth-nine-chain.md`;
- `src/verify_contaminated_backbone_depth9.cpp`;
- `data/contaminated_backbone_depth9_certificate_2026-07-11.txt`.

---

# 12. Current unresolved problem: long-run continuation tree

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

The known branch has the certified pattern

```math
4,8,4,4,8,4,8,8.
```

It demonstrates:

1. several cheap contaminated steps can create substantial weighted-density growth;
2. the first exact recovery does not determine future behavior;
3. a cheap release can occur after an exact recovery;
4. structural 4-AP witnesses can force one or more later factor-eight repayments;
5. finite repayment along one branch is not yet a state-independent theorem.

The active target is

```math
\boxed{
\text{prove that every infinite continuation path has long-run average scale growth greater than }6,
}
```

or replace weighted density by a stronger invariant if that statement is false.

Immediate computational targets:

1. classify factor-two and factor-four continuations of `S_9`;
2. determine whether another cheap release occurs after the two consecutive factor-eight steps;
3. classify exact recovery states by their future cheap-release behavior;
4. construct a finite continuation graph or symbolic quotient and estimate its spectral radius.

Immediate proof targets:

1. explain why the recursive completion and equal-difference structures force the `S_7` and `S_8` repayments;
2. define a contamination-debt potential that permits delayed release but forces eventual repayment;
3. control the whole recovery tree rather than a selected path;
4. prove an aggregate packing theorem for overlapping replay cores.

The full Erdős problem remains unresolved.
