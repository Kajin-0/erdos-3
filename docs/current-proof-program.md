# Current proof program: backbone recursion and density-sensitive persistence

## Status

This is the authoritative overview of the active program for Erdős Problem #3.

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. The project focuses on proving that every four-term-progression-free set has convergent reciprocal sum.

All recent theorem-style claims below are proved internally but have not received independent expert review.

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

Let

```math
K=|D|-s.
```

Every deleted sponsor creates one selected middle-step occurrence `q<=N/2`.

The selected progressions also define an affine deletion DAG, which remains useful for supporting overlap geometry.

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
```

`B(D)` is four-term-progression-free, and

```math
\boxed{|
\mathcal B(D)|=|D|-1.}
```

Every associated backbone label satisfies

```math
0<d-m\le d/2.
```

The child root anchor is `m`, an element of the lifted parent set. Thus every recursive state retains the form

```math
S=B-t,
\qquad
B\subseteq D_{\mathrm{root}},
\qquad
t\in\{0\}\cup D_{\mathrm{root}}.
```

**Primary note:** `docs/minimum-translation-backbone-recursion.md`.

---

# 4. Raw binary factor three

For every center `x`, let

```math
M_x=\{q_i:b_i=x\}
```

be the full selected middle child. Every `M_x` is four-term-progression-free, and

```math
\sum_xH(M_x)
\ge
\frac{2K}{N}.
```

The backbone satisfies

```math
H(\mathcal B(D))
>
\frac{|D|-1}{N}.
```

The genealogy is binary, and

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

This is the strongest raw occurrence theorem. Equal numerical labels are counted repeatedly.

---

# 5. Exact within-state middle multiplicity fibers

Let `Q` be the distinct selected middle steps. For each `q in Q`, let `X_q` be its selected centers and define

```math
\Xi_q
=
\{x-\min X_q:x\in X_q,\ x>\min X_q\}.
```

Every `Xi_q` is four-term-progression-free and lies in `[1,N)`. The exact identity is

```math
\boxed{
|Q|+
\sum_q|\Xi_q|
=K.
}
```

One copy of every distinct step becomes terminal mass, while every additional copy becomes a lower-scale recursive child.

---

# 6. Binary multiplicity-resolving factor two

Combining the exact middle multiplicity fibers with the backbone gives a binary hybrid output satisfying

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

This is the active one-generation bridge from parent harmonic mass toward terminal distinct mass.

---

# 7. Shell interface

Every child in `[1,N)` must be partitioned into standard dyadic shells

```math
[2^j,2^{j+1})
```

before side-anchor deletion is reapplied. Harmonic mass is additive across shells.

A repeated progression is relevant only if it survives inside one shell. Every multigeneration theorem and every counterexample must be checked after this decomposition.

---

# 8. Half-contraction and positive moments

Every retained output associated with parent label `a` is at most `a/2`, and every parent creates at most two outputs. Hence, for every real `p>=1`,

```math
\boxed{
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
}
```

Across the full recursive tree, if `mu(q)` is total terminal multiplicity, then

```math
\boxed{
\sum_q\mu(q)q^p
\le
2^{1-p}
\sum_{a\text{ root}}a^p.
}
```

Every recursive path has logarithmic depth.

---

# 9. Global lifted-center layers

A terminal step `q` in a state `S=B-t` lifts to a progression

```math
x-q,
\quad x,
\quad x+q
```

inside the root block.

Let `nu_q(x)` count occurrences lifting to center `x`. Define

```math
L(q)=\max_x\nu_q(x)
```

and

```math
X_{q,k}=\{x:\nu_q(x)\ge k\}.
```

Translating every nonempty center layer by its minimum gives lower-scale four-term-progression-free children `Omega_{q,k}` with

```math
\boxed{
\mu(q)
=
L(q)
+
\sum_{k=1}^{L(q)}|\Omega_{q,k}|.
}
```

Thus all repetition occurring at different lifted centers is exported.

---

# 10. Root-anchor layers

Fix one exact lifted progression `P(x,q)`. Let `lambda_{x,q}(t)` count terminal copies produced in states with root anchor `t`.

For nonroot anchors define

```math
M_{x,q}
=
\max_{t\in D}\lambda_{x,q}(t).
```

Nested anchor layers translate to lower-scale four-term-progression-free children `Gamma_{x,q,k}` satisfying

```math
\boxed{
\sum_{t\in D}\lambda_{x,q}(t)
=
M_{x,q}
+
\sum_{k=1}^{M_{x,q}}|\Gamma_{x,q,k}|.
}
```

Thus every exact-progression copy occurring with a different root anchor is exported.

---

# 11. Same-anchor antichain budget

The root sponsor of `P(x,q)` is

```math
a=x-\sigma(q)q.
```

In a state anchored at `t`, the local sponsor label is

```math
s=a-t.
```

Copies with the same anchor have equal positive label `s` and form an antichain in the half-contracting occurrence tree. Therefore

```math
\boxed{
\lambda_{x,q}(t)(a-t)
\le a.
}
```

Hence

```math
\lambda_{x,q}(t)
\le
\left\lfloor\frac{a}{a-t}\right\rfloor.
```

High same-anchor multiplicity forces the anchor into a short interval immediately below the sponsor:

```math
\lambda_{x,q}(t)\ge m
\quad\Longrightarrow\quad
 t\ge a\left(1-\frac1m\right).
```

---

# 12. Predecessor-anchor layers

Fix an exact progression and a target anchor `t`. Let `c_{x,q,t}(p)` count copies whose immediate parent state has anchor `p`.

Nested predecessor layers translate to lower-scale four-term-progression-free children `Lambda_{x,q,t,k}` with

```math
\boxed{
\sum_{p\in D}c_{x,q,t}(p)
=
C_{x,q}(t)
+
\sum_{k=1}^{C_{x,q}(t)}
|\Lambda_{x,q,t,k}|,
}
```

where

```math
C_{x,q}(t)
=
\max_{p\in D}c_{x,q,t}(p).
```

The predecessor and target anchors satisfy

```math
p\le2t-a<t.
```

For one fixed transition `p -> t`, the parent occurrences form an antichain, giving

```math
\boxed{
c_{x,q,t}(p)(a-p)\le a.
}
```

The construction can be iterated backward through the complete anchor history.

**Primary note:** `docs/predecessor-anchor-layer-resolution.md`.

---

# 13. Sharp one-step aligned diamond

For every `N>=32`, the block

```math
D_N
=
N+
\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

is four-term-progression-free.

Four selected step-one progressions produce

```math
\Xi_1=\{16,21,26\},
```

while the minimum-translation backbone shell contains the same progression. Both child states have the same root anchor `N`.

Thus one parent can create two copies of the same local progression with the same anchor. The local bound `2` is sharp.

---

# 14. Self-replicating aligned diamonds

The sharp one-step diamond can repeat recursively.

Let

```math
S_1
=
32+
\{0,1,2,16,17,18,21,22,23,26,27,28\}.
```

It produces two identical-history terminal copies of step `5`.

Assume `S_h subseteq[L_h,2L_h)` is four-term-progression-free and produces `2^h` copies with the same complete anchor history. Put

```math
A_h=\{0\}\cup S_h
```

and choose an odd integer

```math
R_h>2\max S_h.
```

The no-carry union

```math
G_{h+1}
=
A_h
\cup
(A_h+R_h)
\cup
(A_h+2R_h)
```

is four-term-progression-free.

After translation into a ratio-two block:

- the step-`R_h` middle multiplicity fiber is exactly `S_h`;
- the minimum-translation backbone shell `[L_h,2L_h)` is exactly `S_h`;
- both child copies have the same new root anchor.

Therefore

```math
\boxed{
\text{persistence}(S_{h+1})
=2^{h+1}.
}
```

The cardinalities satisfy

```math
n_{h+1}=3(n_h+1),
\qquad
n_1=12,
```

so

```math
\boxed{
n_h
=
\frac{9\cdot3^h-3}{2}.
}
```

Consequently

```math
\boxed{
\text{identical-history persistence}
\asymp
|S_h|^{\log_3 2}.
}
```

Absolute, logarithmic, polylogarithmic, and subpower bounds below exponent `log_3 2` are false in terms of parent cardinality.

A 39-point depth-two instance produces four copies and is verified by

```text
src/verify_self_replicating_aligned_diamond_depth2.py
```

**Primary note:** `docs/self-replicating-aligned-diamond.md`.

---

# 15. Supporting deletion-DAG structure

The exact merge and spanning-component identities remain valid:

```math
\sum_v|\Delta_v|=K-s+\rho,
```

```math
\sum_j|\Theta_j|=K+s-\rho,
```

and

```math
\sum_v|\Delta_v|
+
\sum_j|\Theta_j|
=2K.
```

They are no longer needed for the strongest one-generation constants, but remain potential ingredients in a density-sensitive persistence theorem.

The raw factors

```math
\frac76,
\qquad
\frac43,
\qquad
\frac{16}{9},
\qquad
\frac83
```

are superseded by raw factor `3`.

The previous multiplicity-resolving factor `5/3` is superseded by factor `2`.

---

# 16. Current unresolved problem

The self-replicating construction proves that four-term-progression-freeness alone does not control exact-progression persistence strongly enough.

However, the construction is sparse in its ambient interval. Its cardinality grows like `3^h`, while the scale required by the recursive separation grows faster.

The active closing target is now

```math
\boxed{
\text{a density-sensitive persistence theorem.}
}
```

Useful forms would include:

1. a lower bound on ambient scale required for `h` aligned-diamond levels;
2. a tradeoff between persistence multiplicity and dyadic density;
3. a potential coupling reciprocal mass to the `3`-for-`2` replication law;
4. a proof that blocks with nonsummable dyadic density cannot sustain efficient replication indefinitely;
5. a classification of constructions that approach the minimum possible scale growth per replication level.

No current theorem closes this gap. The full Erdős problem remains unresolved.
