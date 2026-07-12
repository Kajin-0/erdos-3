# Current proof program: backbone recursion and long-run contamination compensation

## Status

This is the authoritative overview of the active program for Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. The project focuses on the four-term case: prove that every four-term-progression-free subset of the positive integers has convergent reciprocal sum.

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

Therefore the closing argument must control the aggregate contribution of sparse dyadic blocks rather than prove a fixed positive-density statement.

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

This counts equal numerical labels repeatedly.

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

A progression crossing shell boundaries is not a recursive terminal event. Every multigeneration theorem, verifier, and counterexample must be checked after this shell resolution.

---

# 6. Half-contraction and moment control

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

Every recursive path has logarithmic depth. Positive moments control scale, but they do not by themselves control reciprocal mass or identical-history persistence.

---

# 7. Global multiplicity compression

A terminal step `q` in a state `S=B-t` lifts to an exact root progression with center `x`.

## 7.1 Lifted-center layers

If `nu_q(x)` counts copies lifting to center `x`, define

```math
L(q)=\max_x\nu_q(x).
```

Nested center layers translate to four-term-progression-free children `Omega_{q,k}` satisfying

```math
\boxed{
\mu(q)
=
L(q)
+
\sum_{k=1}^{L(q)}|\Omega_{q,k}|.
}
```

Thus repetition at different lifted centers is exported.

## 7.2 Root-anchor layers

For one exact lifted progression, let `lambda_{x,q}(t)` count copies produced with root anchor `t`. Nested anchor layers give children `Gamma_{x,q,k}` with an exact layer identity, exporting all copies occurring at different root anchors.

## 7.3 Same-anchor antichain budget

Let `a` be the root sponsor. Copies with one anchor `t` have equal local sponsor label `a-t` and form an antichain. Therefore

```math
\boxed{
\lambda_{x,q}(t)(a-t)\le a.
}
```

In particular,

```math
\lambda_{x,q}(t)\ge m
\quad\Longrightarrow\quad
 t\ge a\left(1-\frac1m\right).
```

High unresolved multiplicity is localized immediately below the sponsor.

## 7.4 Predecessor-anchor layers

For a fixed target anchor `t`, predecessor anchors satisfy

```math
p\le2t-a<t
```

and one fixed transition obeys

```math
\boxed{
c_{x,q,t}(p)(a-p)\le a.
}
```

The construction iterates backward through complete anchor histories.

**Primary notes:**

- `docs/global-lifted-center-layer-resolution.md`;
- `docs/state-anchor-layer-and-antichain-budget.md`;
- `docs/predecessor-anchor-layer-resolution.md`.

---

# 8. Self-replicating aligned diamonds

The same complete anchor history can persist polynomially many times.

A base block built from

```math
H=\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

produces the terminal progression

```math
16,21,26
```

both in a middle multiplicity fiber and in the minimum-translation backbone.

A three-translate recursion gives four-term-progression-free states with

```math
|S_h|=\frac{9\cdot3^h-3}{2}
```

and certified identical-history persistence

```math
P_h=2^h.
```

Therefore

```math
P_h\asymp |S_h|^{\log_3 2}.
```

Consequently bounded, logarithmic, polylogarithmic, and subpower bounds below exponent `log_3 2` are false in terms of parent cardinality alone.

**Primary note:** `docs/self-replicating-aligned-diamond.md`.

---

# 9. Exact scale-eight family

There is a computer-certified infinite family

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

The union is recognized by a 34-state least-significant-digit-first base-eight automaton. The exact product/carry search explores 17,238 reachable states and reaches no accepting nontrivial four-term progression.

**Verifier:** `src/verify_scale_eight_aligned_diamond.py`.

**Primary note:** `docs/scale-eight-self-replicating-aligned-diamond.md`.

---

# 10. Exact equal-translate model is sharply classified

Suppose an exact replication step is formed from

```math
A,
\quad A+R,
\quad A+2R
```

and the uncontaminated backbone shell reproduces the previous state exactly.

## 10.1 At most three equal translate layers

Four layers would contain

```math
0,R,2R,3R,
```

so four-term-progression-freeness forces at most three equal translate layers. The occurrence genealogy is binary, so one parent has at most two persistent children.

## 10.2 Dyadic scale-eight barrier

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
P_h\le\left(\frac{L_h}{L_0}\right)^{1/3}.
}
```

The scale-eight family attains the exponent.

## 10.3 Sharp weighted-density decay

Let

```math
\alpha_h=\frac{|S_h|}{L_h},
\qquad
P_h=2^h.
```

The exact cardinality recurrence is

```math
|S_{h+1}|=3(|S_h|+1).
```

Writing

```math
C_0=\frac{|S_0|+3/2}{L_0},
```

one obtains

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

The exact one-step efficiency is

```math
\rho_{\mathrm{exact}}
=
\frac{2\cdot3}{8}
=
\frac34.
```

This classification is sharp inside the exact standard-dyadic equal-translate model.

**Primary notes:**

- `docs/three-translate-dyadic-scale-barrier.md`;
- `docs/exact-three-translate-weighted-density-theorem.md`.

---

# 11. Contaminated-backbone depth-five chain

The exact-model contraction does not extend locally when the backbone shell merely contains the replay state.

There are certified four-term-progression-free states

```math
S_h\subseteq[L_h,2L_h),
\qquad 1\le h\le5,
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
3. the deletion schedule inside the previous state can be replayed in that subset;
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
P_h^{\mathrm{cert}}\frac{|S_h|}{L_h}.
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

# 12. Current unresolved problem: long-run compensation

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

The certified four-step contaminated segment has

```math
\prod_{h=1}^{4}c_h
=4\cdot8\cdot4\cdot4
=512
<6^4=1296.
```

Hence any universal theorem must operate on a longer horizon.

The active target is

```math
\boxed{
\text{prove long-run compensation for cheap contaminated-backbone replication.}
}
```

A successful result may take one of the following forms:

1. cumulative scale expansion eventually exceeds the `6`-per-generation threshold;
2. contaminating points create exportable lower-scale difference structure;
3. repeated cheap steps force a four-term progression;
4. repeatable patterns fall into a finite symbolic class with controlled spectral growth;
5. overlap among contaminated replay cores admits an aggregate packing bound.

The immediate computational question is whether cheap scale-factor patterns extend indefinitely, periodically, or only through bounded bursts. The immediate proof question is to identify a monotone contamination or recovery potential.

The full Erdős problem remains unresolved.
