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

The closing argument must control the aggregate contribution of sparse dyadic blocks.

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

A certified contaminated-backbone chain has scales

```math
(64,256,2048,8192,32768)
```

and scale factors

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

---

# 7. Path-dependent recovery from `S_5`

The depth-five state admits no factor-two or factor-four continuation:

```math
\boxed{N_{5,2}=N_{5,4}=0.}
```

## 7.1 Smallest exact recovery

For

```math
R_5=65547,
```

the recovered state again has no factor-two or factor-four continuation. Along this branch,

```math
\frac{W_7}{W_5}\le\frac{205}{364}.
```

## 7.2 Alternative recovery and cheap release

For

```math
R_5=93476,
```

the exact recovered state admits the factor-four descendant

```math
R_6=230164.
```

The resulting scale sequence is

```math
\boxed{4,8,4,4,8,4.}
```

with

```math
S_7\subseteq[1048576,2097152),
\qquad
|S_7|=9840,
\qquad
P_7^{\mathrm{cert}}=128,
```

and

```math
W_7=\frac{615}{512}.
```

Thus

```math
\boxed{
\frac{W_7}{W_5}=\frac{205}{182}>1,
}
```

so universal two-generation recovery and contraction over every six-generation window are false.

---

# 8. Complete cheap-extension exclusion from `S_7`

The factor-two domain has `25161` sponsor-compatible candidates, of which `202` are layer-disjoint. All fail:

```math
N_{7,2}=0.
```

The factor-four domain has

```text
724212 sponsor-compatible candidates
359419 layer-disjoint candidates.
```

Every disjoint candidate has an explicit four-term-progression witness:

```text
352979 completion witnesses
215 layer-pattern 1001 witnesses
6225 layer-pattern 0011 witnesses.
```

Therefore

```math
\boxed{N_{7,4}=0.}
```

Every continuation from `S_7` terminates or has scale factor at least `8`.

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

The full scale sequence is

```math
\boxed{4,8,4,4,8,4,8.}
```

The backbone is exact and `S_8` is four-term-progression-free.

Its weighted density is

```math
\boxed{
W_8=\frac{29523}{32768}.
}
```

The final factor-eight step gives

```math
\boxed{
\frac{W_8}{W_7}=\frac{9841}{13120}
}
```

and the three-generation block beginning at `S_5` satisfies

```math
\boxed{
\frac{W_8}{W_5}=\frac{757}{896}<1.
}
```

Thus the cheap release at depth seven is repaid by the forced exact factor-eight step.

Relative to the base,

```math
\frac{W_8}{W_1}=\frac{9841}{4096}>1,
```

so this finite compensation does not by itself establish long-run decay.

**Primary references:**

- `docs/contaminated-backbone-depth-eight-chain.md`;
- `src/verify_contaminated_backbone_depth8.cpp`;
- `data/contaminated_backbone_depth8_certificate_2026-07-11.txt`.

---

# 10. Current unresolved problem: repeated release cycles

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

The current branch exhibits a complete delayed-compensation cycle:

```math
\text{exact recovery}
\to
\text{cheap contaminated release}
\to
\text{forced exact recovery}.
```

The active target is

```math
\boxed{
\text{determine whether such release cycles can repeat indefinitely with average scale growth at most }6.
}
```

Immediate computational targets:

1. classify factor-two and factor-four continuations of `S_8`;
2. if another cheap descendant exists, extend and certify the cycle;
3. classify exact factor-eight recovery states by future cheap-release behavior.

Immediate proof targets:

1. explain why the two contaminating points at depth seven create enough completion and equal-difference witnesses to force recovery;
2. define a contamination-debt potential that allows release but forces repayment;
3. prove every infinite continuation path has geometric-mean scale expansion greater than `6`;
4. reduce repeatable patterns to a finite-state system with subcritical spectral radius;
5. control overlap among replay cores by an aggregate packing theorem.

The full Erdős problem remains unresolved.
