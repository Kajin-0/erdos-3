# Current proof program: backbone recursion and same-anchor persistence

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

**Status:** standard.

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

The selected progressions also define an affine deletion DAG, but the strongest one-generation constants no longer require the DAG structural children.

**Primary notes:**

- `docs/side-anchor-sponsored-middle-recursion.md`
- `docs/side-anchor-deletion-dag.md`

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
\boxed{
|\mathcal B(D)|=|D|-1.
}
```

Associate `d-m` with parent element `d`. Since `m>=N` and `d<2N`,

```math
\boxed{
0<d-m\le d-N\le d/2.
}
```

The minimum point creates no backbone output.

The child has root translation anchor `m`, which belongs to the lifted parent set. Thus every recursive state retains the inherited form

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

For each center `x`, let

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

Every deleted nonminimum sponsor creates one middle occurrence and one backbone occurrence. Every other parent creates at most one backbone occurrence. Hence the genealogy is binary.

Combining the two families gives

```math
\begin{aligned}
H(\mathcal B(D))
+
\sum_xH(M_x)
&\ge
\frac{|D|-1+2K}{N}\\
&=
\frac{3|D|-2s-1}{N}.
\end{aligned}
```

Therefore

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

This is the strongest raw occurrence theorem. It counts equal numerical labels repeatedly.

**Primary note:** `docs/minimum-translation-backbone-recursion.md`.

---

# 5. Exact within-state middle multiplicity fibers

Let

```math
Q=\{q_i:1\le i\le K\}
```

be the set of distinct selected steps. For each `q in Q`, let

```math
X_q=\{b_i:q_i=q\}
```

be its selected centers. Define

```math
\Xi_q
=
\{x-\min X_q:x\in X_q,\ x>\min X_q\}.
```

Every `Xi_q` is four-term-progression-free and lies in `[1,N)`. If `m(q)=|X_q|`, then

```math
|\Xi_q|=m(q)-1.
```

Since `sum_q m(q)=K`,

```math
\boxed{
|Q|+
\sum_{q\in Q}|\Xi_q|
=K.
}
```

Thus one copy of every distinct middle step becomes terminal mass, while every additional copy becomes a recursive lower-scale child.

The corresponding harmonic lower bound is

```math
H(Q)
+
\sum_qH(\Xi_q)
\ge
\frac{K}{N}.
```

**Primary note:** `docs/middle-multiplicity-fiber-five-thirds-recursion.md`.

---

# 6. Binary multiplicity-resolving factor two

Combine the exact middle multiplicity resolution with the backbone child.

Every deleted nonminimum sponsor creates:

1. exactly one terminal representative or multiplicity-fiber occurrence;
2. exactly one backbone occurrence.

Every other parent creates at most one backbone occurrence. Hence the genealogy remains binary.

The harmonic output satisfies

```math
\begin{aligned}
&H(Q)
+
\sum_qH(\Xi_q)
+
H(\mathcal B(D))\\
&\qquad\ge
\frac{K}{N}
+
\frac{|D|-1}{N}\\
&\qquad=
\frac{2|D|-s-1}{N}.
\end{aligned}
```

Therefore

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

**Primary note:** `docs/minimum-translation-backbone-recursion.md`.

---

# 7. Shell interface

Every recursive child in `[1,N)` must be partitioned into standard dyadic shells

```math
[2^j,2^{j+1})
```

before the deletion theorem is reapplied. Harmonic mass is additive across this partition.

A repeated progression is relevant only if it survives inside one shell. This interface invalidated the original use of the 31-element sibling gadget as a recursive terminal example. The corrected 34-element construction proves shell-compatible two-layer overlap for the older spanning-component recursion.

**Primary note:** `docs/dyadic-shell-compatible-sibling-sharpness.md`.

---

# 8. Half-contraction and positive moments

Every retained backbone output associated with parent `d` is at most `d/2`. Every terminal representative and multiplicity-fiber output associated with a deleted sponsor is also at most half that sponsor.

Thus every parent creates at most two outputs and, for every real `p>=1`,

```math
\boxed{
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
}
```

Across the full recursive tree, if `mu(q)` denotes total terminal multiplicity, then

```math
\boxed{
\sum_q\mu(q)q^p
\le
2^{1-p}
\sum_{a\text{ root}}a^p.
}
```

In particular,

```math
\sum_q\mu(q)q
\le
\sum_a a.
```

Every recursive path has logarithmic depth.

**Primary note:** `docs/half-contraction-multiscale-label-potential.md`.

---

# 9. Global lifted-center layers

Every recursive state has the form

```math
S=B-t,
\qquad B\subseteq D_{\mathrm{root}}.
```

A terminal step `q` in `S` lifts to

```math
x-q,
\quad x,
\quad x+q
```

inside the root block.

Let `nu_q(x)` count terminal occurrences lifting to center `x`. Define

```math
L(q)=\max_x\nu_q(x)
```

and the nested layers

```math
X_{q,k}=\{x:\nu_q(x)\ge k\}.
```

Each layer is a subset of the root four-term-progression-free set. Translating each nonempty layer by its minimum gives lower-scale four-term-progression-free children `Omega_{q,k}` with

```math
\boxed{
\mu(q)
=
L(q)
+
\sum_{k=1}^{L(q)}|\Omega_{q,k}|.
}
```

Thus all cross-state repetition occurring at different lifted centers is exported.

**Primary note:** `docs/global-lifted-center-layer-resolution.md`.

---

# 10. Root-anchor layers

Fix one exact lifted progression `P(x,q)`. Every recursive state has a root translation anchor

```math
t\in\{0\}\cup D_{\mathrm{root}}.
```

Let `lambda_{x,q}(t)` count terminal copies of `P(x,q)` produced in states with anchor `t`.

For nonroot anchors define

```math
A_{x,q}^{(k)}
=
\{t\in D:\lambda_{x,q}(t)\ge k\}.
```

Each anchor layer is a subset of the root four-term-progression-free set. Translating each nonempty layer by its minimum gives lower-scale four-term-progression-free anchor-difference children `Gamma_{x,q,k}` and the exact identity

```math
\boxed{
\sum_{t\in D}\lambda_{x,q}(t)
=
M_{x,q}
+
\sum_{k=1}^{M_{x,q}}|\Gamma_{x,q,k}|,
}
```

where

```math
M_{x,q}
=
\max_{t\in D}\lambda_{x,q}(t).
```

Thus every exact-progression copy occurring with a different root anchor is exported.

**Primary note:** `docs/state-anchor-layer-and-antichain-budget.md`.

---

# 11. Same-anchor antichain budget

The coordinated orientation determines the root sponsor

```math
a=x-\sigma(q)q.
```

In a state anchored at `t`, the local sponsor label is

```math
s=a-t.
```

All terminal copies counted by `lambda_{x,q}(t)` have the same positive label `s`. Since labels strictly halve along recursive edges, two such occurrences cannot be ancestor and descendant. They form an antichain in the descendant tree of root sponsor `a`.

The conserved linear-label flow gives

```math
\boxed{
\lambda_{x,q}(t)(a-t)
\le a.
}
```

Therefore

```math
\boxed{
\lambda_{x,q}(t)
\le
\left\lfloor\frac{a}{a-t}\right\rfloor.
}
```

Since a terminal step satisfies `q<=(a-t)/2`,

```math
\lambda_{x,q}(t)
\le
\left\lfloor\frac{a}{2q}\right\rfloor.
```

A useful geometric form is

```math
\lambda_{x,q}(t)\ge m
\quad\Longrightarrow\quad
 t\ge a\left(1-\frac1m\right).
```

High same-anchor persistence is therefore concentrated in a short interval immediately below the root sponsor.

For

```math
T_m(x,q)
=
\{t\in D:\lambda_{x,q}(t)\ge m\},
```

one has

```math
\boxed{
|T_m(x,q)|
\le
r_4\!\left(\left\lceil a/m\right\rceil+1\right).
}
```

**Primary note:** `docs/state-anchor-layer-and-antichain-budget.md`.

---

# 12. Sharp anchor-aligned diamond

The universal claim

```math
M_{x,q}=1
```

is false.

For `N>=32`, the 12-point block

```math
D_N
=
N+
\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

is four-term-progression-free.

Four valid selected progressions of step `1` produce the middle multiplicity-fiber child

```math
\Xi_1=\{16,21,26\}.
```

The minimum-translation backbone shell also contains

```math
16,21,26.
```

Both children have the same root anchor `N`. Hence one parent can create two copies of the same local progression with the same anchor.

The one-parent same-anchor multiplicity bound `2` is sharp.

This gadget does not self-replicate: once the anchor `N` is removed, descendants cannot use it again. Large same-anchor multiplicity therefore requires convergence from several different parent states.

**Primary note:** `docs/minimum-backbone-aligned-diamond-counterexample.md`.

**Verifier:** `src/verify_minimum_backbone_aligned_diamond.py`.

---

# 13. Supporting deletion-DAG structure

The following exact results remain valid:

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

They are no longer needed for the strongest one-generation branching constants, but they expose merge geometry, scale export, and component overlap that may be useful for the remaining convergence problem.

The older raw factors

```math
\frac76,
\qquad
\frac43,
\qquad
\frac{16}{9},
\qquad
\frac83
```

are superseded by the backbone raw factor `3`.

The older multiplicity-resolving factor `5/3` is superseded by the backbone hybrid factor `2`.

---

# 14. Current unresolved object

After within-state middle fibers, global lifted-center layers, and root-anchor layers, the remaining multiplicity consists of

```math
\boxed{
\text{one identical local progression repeated across incomparable states with the same root anchor.}
}
```

Every such family satisfies

```math
\lambda(a-t)\le a.
```

The sharp aligned diamond shows that multiplicity two can occur in one parent step. Larger multiplicity requires predecessor-anchor convergence: several parent states must independently create child states with the same new anchor and preserve the same local progression.

The active closing target is therefore

```math
\boxed{
\text{a density-sensitive predecessor-anchor convergence theorem.}
}
```

Useful forms would include:

1. exporting every convergence diamond to an additional lower-scale difference child;
2. showing that repeated aligned convergence forces a forbidden affine configuration;
3. bounding the multiplicity tail using the short anchor interval and root density;
4. constructing a stopping-time potential for one fixed local progression.

No current theorem closes this gap. The full Erdős problem remains unresolved.
