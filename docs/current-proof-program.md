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

Fix a four-term-progression-free block

```math
D\subseteq[N,2N).
```

Coordinated side-anchor deletion removes

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

is four-term-progression-free, lies in `[1,N)`, has size `|D|-1`, and satisfies

```math
d-m\le d/2.
```

The full middle family and backbone give the raw occurrence inequality

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

Let `Q` be the distinct selected middle steps and let `Xi_q` be the translated center-difference child for step `q`. Then

```math
\boxed{
|Q|+
\sum_q|\Xi_q|=K.
}
```

Combining these fibers with the backbone gives the strongest multiplicity-resolving inequality

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

**Primary notes:**

- `docs/minimum-translation-backbone-recursion.md`;
- `docs/middle-multiplicity-fiber-five-thirds-recursion.md`.

---

# 3. Shell interface and global multiplicity compression

Every child in `[1,N)` must be partitioned into standard dyadic shells before deletion is reapplied. A progression crossing shell boundaries is not a recursive terminal event.

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
2^{1-p}
\sum_{a\text{ root}}a^p.
}
```

Repeated terminal labels are compressed by lifted-center layers, root-anchor layers, and predecessor-anchor layers. Copies with one fixed complete anchor history obey the antichain budget

```math
\boxed{
\lambda_{x,q}(t)(a-t)\le a.
}
```

Thus high unresolved persistence is localized immediately below the root sponsor.

**Primary notes:**

- `docs/global-lifted-center-layer-resolution.md`;
- `docs/state-anchor-layer-and-antichain-budget.md`;
- `docs/predecessor-anchor-layer-resolution.md`;
- `docs/half-contraction-multiscale-label-potential.md`.

---

# 4. Self-replicating aligned diamonds

The base set

```math
H=
\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

produces the terminal progression

```math
16,21,26
```

both in a middle multiplicity fiber and in the minimum-translation backbone.

A three-translate recursion gives four-term-progression-free states with

```math
|S_h|=
\frac{9\cdot3^h-3}{2}
```

and certified identical-history persistence

```math
P_h=2^h.
```

Therefore

```math
P_h\asymp|S_h|^{\log_3 2}.
```

Bounded, logarithmic, polylogarithmic, and sufficiently small subpower persistence bounds are false in terms of parent cardinality alone.

**Primary note:** `docs/self-replicating-aligned-diamond.md`.

---

# 5. Exact scale-eight model

There is a computer-certified infinite family

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

The union is recognized by a 34-state base-eight automaton. The exact product/carry search explores `17238` states and reaches no accepting nontrivial four-term progression.

For every exact standard-dyadic equal-translate genealogy:

1. at most three equal translate layers are possible;
2. binary persistence gives at most two persistent children;
3. exact backbone reproduction forces
   ```math
   L'\ge8L;
   ```
4. writing `alpha_h=|S_h|/L_h`,
   ```math
   \boxed{
   P_h\alpha_h
   \le
   C_0\left(\frac34\right)^h
   =
   C_0P_h^{\log_2 3-2};
   }
   ```
5. the aggregate charge satisfies
   ```math
   \boxed{
   \sum_hP_h\alpha_h\le4C_0.
   }
   ```

The scale-eight family attains these exponents. The exact model is sharply classified.

**Primary notes and verifier:**

- `docs/scale-eight-self-replicating-aligned-diamond.md`;
- `docs/three-translate-dyadic-scale-barrier.md`;
- `docs/exact-three-translate-weighted-density-theorem.md`;
- `src/verify_scale_eight_aligned_diamond.py`.

---

# 6. Contaminated depth-five burst

There are certified states with scales

```math
(64,256,2048,8192,32768)
```

and separations

```math
(61,303,1597,8195),
```

so the outer scale factors are

```math
\boxed{4,8,4,4.}
```

The middle fiber is exact at every step. The relevant backbone shell contains a replayable copy of the previous state, possibly with contamination.

Define

```math
W_h
=
P_h^{\mathrm{cert}}
\frac{|S_h|}{L_h}.
```

Then

```math
W_1=\frac38,
\qquad
W_5=\frac{273}{256},
```

and

```math
\boxed{
\frac{W_5}{W_1}
=
\frac{91}{32}.
}
```

Therefore universal local contraction and contraction over every four-generation window are false.

**Primary note, verifier, and certificate:**

- `docs/contaminated-backbone-depth-five-chain.md`;
- `src/verify_contaminated_backbone_depth5.py`;
- `data/contaminated_backbone_depth5_certificate_2026-07-11.txt`.

---

# 7. Two different recovery branches from `S_5`

The depth-five state admits no factor-two or factor-four continuation:

```math
\boxed{N_{5,2}=N_{5,4}=0.}
```

Every continuation therefore has scale factor at least `8`.

## 7.1 Smallest exact recovery

The first exact recovery is

```math
R_5=65547.
```

The resulting state again has no factor-two or factor-four continuation. Along this selected branch,

```math
4,8,4,4
\quad\longrightarrow\quad
8,\ge8
```

or termination, and

```math
\frac{W_7}{W_5}
\le
\frac{205}{364}.
```

## 7.2 Alternative recovery with cheap release

A different exact recovery is

```math
\boxed{R_5=93476.}
```

It admits the factor-four descendant

```math
\boxed{R_6=230164.}
```

whose backbone contains the replay state plus exactly two points:

```math
460328,
\qquad
492308.
```

The resulting scale sequence is

```math
\boxed{4,8,4,4,8,4.}
```

The depth-seven state satisfies

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

Hence

```math
\boxed{
\frac{W_7}{W_5}
=
\frac{205}{182}>1,
}
```

and

```math
\boxed{
\frac{W_7}{W_1}
=
\frac{205}{64}.
}
```

Universal two-generation recovery and contraction over every six-generation window are therefore false.

**Primary notes and verifiers:**

- `docs/forced-recovery-after-depth-five.md`;
- `docs/contaminated-backbone-depth-seven-chain.md`;
- `src/verify_forced_recovery_after_depth5.py`;
- `src/verify_contaminated_backbone_depth7.cpp`.

---

# 8. Complete cheap-extension exclusion from `S_7`

The factor-two search from `S_7` has

```text
25161 sponsor-compatible candidates
202 disjoint candidates
0 valid candidates.
```

Thus

```math
N_{7,2}=0.
```

For factor four, the fit condition gives

```math
R\le1086317.
```

There are

```text
724212 sponsor-compatible candidates
359419 disjoint candidates.
```

Every disjoint candidate receives an explicit structural four-term-progression witness:

```text
352979 completion witnesses
215 layer-pattern 1001 witnesses
6225 layer-pattern 0011 witnesses.
```

Therefore

```math
\boxed{N_{7,4}=0.}
```

Combining the two exclusions,

```math
\boxed{
\text{every continuation from }S_7\text{ terminates or has scale factor at least }8.
}
```

Since `|S_7|=9840`, every possible next continuation satisfies

```math
\boxed{
\frac{W_8}{W_7}
\le
\frac{9841}{13120}.
}
```

Therefore, if `S_8` exists,

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

Thus the alternative branch has the finite compensation pattern

```math
4,8,4,4,8,4,\ge8
```

or termination. The cheap factor-four release is followed by a forced expensive step.

**Primary note, verifier, and certificate:**

- `docs/depth-seven-factor-four-exclusion.md`;
- `src/verify_depth7_no_factor4_extension.cpp`;
- `data/depth7_no_factor4_certificate_2026-07-11.txt`.

---

# 9. Current unresolved problem: continuation-graph control

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

The known behavior is path-dependent:

1. exact recovery can lead to another expensive step;
2. exact recovery can instead release a factor-four descendant;
3. the released state then forbids another immediate factor-two or factor-four step;
4. both known branches eventually compensate relative to `S_5`, but no state-independent theorem is known.

The active target is

```math
\boxed{
\text{control every path in the contaminated-backbone continuation graph.}
}
```

Immediate computational targets:

1. find and classify factor-eight continuations of `S_7`;
2. test whether their descendants release another cheap step;
3. classify all exact factor-eight recoveries of `S_5` by descendant behavior.

Immediate proof targets:

1. explain the structural completion and equal-difference witnesses that force recovery from `S_7`;
2. define a contamination-debt potential that allows delayed release but forces repayment;
3. prove every infinite continuation path has geometric-mean scale expansion greater than `6`;
4. reduce repeatable patterns to a finite-state system with subcritical spectral radius;
5. control overlap among replay cores by an aggregate packing theorem.

The full Erdős problem remains unresolved.
