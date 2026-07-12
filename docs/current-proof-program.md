# Current proof program: backbone recursion and long-run contamination compensation

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

# 2. Sponsored side-anchor deletion

Fix a four-term-progression-free block

```math
D\subseteq[N,2N).
```

Repeatedly select a nontrivial three-term progression and delete its coordinated side anchor. Stop with a three-term-progression-free residual of size

```math
s\le r_3(N).
```

Put

```math
K=|D|-s.
```

Every deleted sponsor creates one selected middle-step occurrence `q<=N/2`.

The selected progressions also define an affine deletion DAG. That structure is no longer needed for the strongest one-generation constants, but remains relevant to overlap and contamination geometry.

---

# 3. Minimum-translation backbone

Let

```math
m=\min D
```

and define

```math
\mathcal B(D)
=
\{d-m:d\in D,\ d>m\}.
```

Then

```math
\mathcal B(D)\subseteq[1,N),
\qquad
|\mathcal B(D)|=|D|-1,
```

and `B(D)` is four-term-progression-free. Every associated label satisfies

```math
0<d-m\le d/2.
```

Every recursive state retains the affine form

```math
S=B-t,
\qquad
B\subseteq D_{\mathrm{root}},
\qquad
t\in\{0\}\cup D_{\mathrm{root}}.
```

**Primary note:** `docs/minimum-translation-backbone-recursion.md`.

---

# 4. Strongest one-generation inequalities

## 4.1 Raw occurrence factor three

Let `M_x` be the full selected middle child at lifted center `x`. Then

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

## 4.2 Exact within-state multiplicity fibers

Let `Q` be the set of distinct selected middle steps. For each `q in Q`, translate its selected center set by its minimum to obtain a four-term-progression-free child `Xi_q`. Then

```math
\boxed{
|Q|+
\sum_q|\Xi_q|
=K.
}
```

One copy of each distinct step becomes terminal mass; every additional copy becomes a lower-scale child.

## 4.3 Multiplicity-resolving factor two

Combining the exact middle fibers with the backbone gives

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

# 5. Mandatory shell interface

Every child in `[1,N)` must be partitioned into standard dyadic shells

```math
[2^j,2^{j+1})
```

before deletion is reapplied. Harmonic mass is additive across shells.

A progression crossing shell boundaries is not a recursive terminal event. Every multigeneration theorem, verifier, and counterexample must be checked after shell resolution.

---

# 6. Half-contraction and global multiplicity compression

Every retained output associated with a parent label `a` is at most `a/2`, and every parent creates at most two outputs. Hence, for every `p>=1`,

```math
\boxed{
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
}
```

Across the full recursive tree,

```math
\boxed{
\sum_q\mu(q)q^p
\le
2^{1-p}
\sum_{a\text{ root}}a^p.
}
```

Every recursive path has logarithmic depth. Positive moments control scale, but not reciprocal mass or identical-history persistence by themselves.

Repeated terminal labels are compressed in stages:

1. different lifted centers are exported by center-difference layers;
2. different root anchors are exported by anchor-difference layers;
3. different predecessor anchors are exported recursively;
4. copies with one complete anchor history obey antichain budgets.

For root sponsor `a` and anchor `t`,

```math
\boxed{
\lambda_{x,q}(t)(a-t)\le a.
}
```

Thus

```math
\lambda_{x,q}(t)\ge m
\quad\Longrightarrow\quad
 t\ge a\left(1-\frac1m\right).
```

High unresolved multiplicity is localized immediately below the sponsor.

**Primary notes:**

- `docs/global-lifted-center-layer-resolution.md`;
- `docs/state-anchor-layer-and-antichain-budget.md`;
- `docs/predecessor-anchor-layer-resolution.md`;
- `docs/half-contraction-multiscale-label-potential.md`.

---

# 7. Self-replicating aligned diamonds

The same complete anchor history can persist polynomially many times.

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

Bounded, logarithmic, polylogarithmic, and subpower bounds below exponent `log_3 2` are false in terms of parent cardinality alone.

**Primary note:** `docs/self-replicating-aligned-diamond.md`.

---

# 8. Exact scale-eight family

There is a computer-certified infinite family

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

The union is recognized by a 34-state least-significant-digit-first base-eight automaton. The exact product/carry search explores `17238` reachable states and reaches no accepting nontrivial four-term progression.

**Verifier:** `src/verify_scale_eight_aligned_diamond.py`.

**Primary note:** `docs/scale-eight-self-replicating-aligned-diamond.md`.

---

# 9. Exact equal-translate model is sharply classified

Suppose an exact replication step is formed from

```math
A,
\quad A+R,
\quad A+2R
```

and the uncontaminated backbone shell reproduces the previous state exactly.

Four equal translate layers would contain

```math
0,R,2R,3R,
```

so four-term-progression-freeness permits at most three layers. The occurrence genealogy is binary, so one parent has at most two persistent children.

Exact uncontaminated backbone reproduction requires `R>=2L`. Since `2R` belongs to the raw state and the next raw state must fit below `L'`,

```math
L'>2R\ge4L.
```

Because `L'/L` is a power of two,

```math
\boxed{L'\ge8L.}
```

After `h` exact generations,

```math
\boxed{
P_h\le
\left(\frac{L_h}{L_0}\right)^{1/3}.
}
```

Let

```math
\alpha_h=\frac{|S_h|}{L_h},
\qquad
C_0=\frac{|S_0|+3/2}{L_0}.
```

The exact recurrence `|S_{h+1}|=3(|S_h|+1)` gives

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

---

# 10. Contaminated-backbone depth-five burst

The exact-model contraction does not extend locally when the backbone shell merely contains the replay state.

There are certified four-term-progression-free states

```math
S_h\subseteq[L_h,2L_h),
\qquad
1\le h\le5,
```

with scales

```math
(L_1,L_2,L_3,L_4,L_5)
=
(64,256,2048,8192,32768)
```

and separations

```math
(R_1,R_2,R_3,R_4)
=
(61,303,1597,8195).
```

The dyadic scale factors are

```math
\boxed{4,8,4,4.}
```

At each step:

1. the selected middle multiplicity fiber is exactly the previous state;
2. the relevant backbone shell contains the previous state plus contaminating points;
3. the verified deletion schedule can be replayed inside that subset;
4. both continuations share the new root anchor;
5. certified identical-history persistence doubles.

Thus

```math
P_h^{\mathrm{cert}}=2^h
```

is a certified lower bound.

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
\frac{91}{32}
=2.84375.
}
```

Therefore the following are false without stronger hypotheses:

1. universal one-step `3/4` contraction for contaminated backbones;
2. universal strict contraction at every non-exact step;
3. contraction over every four-step replication window;
4. a local near-exact/defective dichotomy in which every non-exact step pays an immediate stronger loss.

**Verifier:** `src/verify_contaminated_backbone_depth5.py`.

**Primary note:** `docs/contaminated-backbone-depth-five-chain.md`.

**Certificate:** `data/contaminated_backbone_depth5_certificate_2026-07-11.txt`.

---

# 11. Finite forced recovery after the burst

The depth-five state satisfies

```math
S_5\subseteq[32768,65536),
\qquad
|S_5|=1092.
```

An exhaustive finite search over every sponsor-compatible disjoint three-translate continuation gives:

```math
\boxed{N_{5,2}=0,}
\qquad
\boxed{N_{5,4}=0.}
```

The factor-two search contains `622` candidates; the factor-four search contains `22467` candidates.

Therefore every continuation of this recorded state in the standard-dyadic replay-containment model must use scale factor at least `8`.

The first valid sponsor-compatible exact-backbone factor-eight recovery is

```math
\boxed{R_5^*=65547.}
```

It gives a four-term-progression-free state

```math
S_6\subseteq[262144,524288),
\qquad
|S_6|=3279.
```

A second exhaustive search gives

```math
\boxed{N_{6,2}=0,}
\qquad
\boxed{N_{6,4}=0.}
```

The factor-two search contains `22459` candidates; the factor-four search contains `197222` candidates.

Thus any continuation from this selected recovered state either terminates or again uses scale factor at least `8`.

The selected first recovery satisfies

```math
\frac{W_6}{W_5}
=
\frac{1093}{1456}.
```

Any next continuation satisfies

```math
\frac{W_7}{W_6}
\le
\frac{820}{1093}.
```

Therefore

```math
\boxed{
\frac{W_7}{W_5}
\le
\frac{205}{364}
\approx0.563187,
}
```

or equivalently

```math
\boxed{W_7\le\frac{615}{1024}}
```

if a seventh state exists in this model.

This is the first explicit finite compensation block after a contaminated cheap-growth burst:

```math
4,8,4,4
\quad\longrightarrow\quad
8,\ge8.
```

**Verifier:** `src/verify_forced_recovery_after_depth5.py`.

**Primary note:** `docs/forced-recovery-after-depth-five.md`.

**Certificate:** `data/forced_recovery_after_depth5_certificate_2026-07-11.txt`.

**Caveat:** this is a state-specific finite theorem. It does not prove that every factor-eight continuation of `S_5`, or every contaminated genealogy, has the same recovery behavior.

---

# 12. Current unresolved problem: state-independent long-run compensation

For disjoint three-translate growth,

```math
|S_{h+1}|=3(|S_h|+1)
```

and certified persistence doubles. If

```math
c_h=\frac{L_{h+1}}{L_h},
```

then

```math
\boxed{
\frac{W_{h+1}}{W_h}
=
\frac{6}{c_h}
\left(1+\frac1{|S_h|}\right).
}
```

Ignoring the lower-order term, long-run contraction requires geometric-mean scale expansion greater than `6`.

The contaminated burst shows that compensation need not occur locally or over four generations. The finite recovery result shows that one explicit cheap burst is followed by a two-generation contraction block along its first exact recovery.

The active target is

```math
\boxed{
\text{prove state-independent long-run compensation for cheap contaminated-backbone replication.}
}
```

A successful result may take one of the following forms:

1. every sufficiently long genealogy has cumulative scale expansion above the `6`-per-generation threshold;
2. contamination creates exportable lower-scale difference mass;
3. repeated cheap steps force a four-term progression;
4. repeatable patterns fall into a finite symbolic class with subcritical spectral growth;
5. overlap among contaminated replay cores obeys an aggregate packing theorem;
6. a monotone contamination-debt potential forces recovery or termination.

The immediate computational target is to classify all valid factor-eight continuations of `S_5` by whether they admit factor-two or factor-four successors.

The immediate proof target is to identify a state-independent recovery invariant that turns finite forced-recovery blocks into a summable multiscale estimate.

The full Erdős problem remains unresolved.
