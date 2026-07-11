# Current proof program: deletion DAG and exact-progression persistence

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

# 2. Side-anchor deletion DAG

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

Writing the selected progressions as

```math
(a_i,b_i,c_i),
\qquad
a_i+c_i=2b_i,
```

add edges

```math
a_i\to b_i,
\qquad
a_i\to c_i.
```

Deletion time increases along every edge, so this is an acyclic graph. Every deleted vertex has outdegree two; every residual vertex has outdegree zero.

**Primary note:** `docs/side-anchor-deletion-dag.md`.

---

# 3. Structural children

Let `rho` be the number of indegree-zero vertices.

## Merge-difference children

For each target `v`, translate its incoming sponsors by their minimum. The resulting children `Delta_v` are four-term-progression-free, lie in `[1,N)`, and satisfy

```math
\boxed{
\sum_v|\Delta_v|=K-s+\rho.
}
```

## Spanning-component children

Choose one incoming edge for every nonroot vertex. Translating each forest component by its numerical minimum gives children `Theta_j` that are four-term-progression-free, lie in `[1,N)`, and satisfy

```math
\boxed{
\sum_j|\Theta_j|=K+s-\rho.
}
```

Therefore

```math
\boxed{
\sum_v|\Delta_v|+\sum_j|\Theta_j|=2K.
}
```

After associating occurrences with parent elements and retaining at most one structural occurrence per parent, at least

```math
\frac{2K}{3}
```

structural occurrences remain. Their harmonic mass is at least

```math
\frac{2K}{3N}.
```

**Primary notes:**

- `docs/deletion-dag-merge-difference-recursion.md`
- `docs/spanning-forest-binary-four-thirds-recursion.md`

---

# 4. Full middle children and raw occurrence growth

For every center `x`, define

```math
M_x=\{q_i:b_i=x\}.
```

A four-term progression among the steps in `M_x` would translate to one in `D`, so every `M_x` is four-term-progression-free.

Every selected step satisfies `q_i<=N/2`, hence

```math
\sum_xH(M_x)\ge\frac{2K}{N}.
```

Keeping every middle occurrence and at most one structural occurrence per parent gives a binary occurrence genealogy satisfying

```math
\boxed{
\sum H(\text{children})
\ge
\frac83H(D)
-
\frac83\frac{r_3(N)}N.
}
```

This is the strongest raw occurrence theorem. It counts equal numerical labels repeatedly.

**Primary note:** `docs/full-middle-binary-eight-thirds-recursion.md`.

---

# 5. Within-node multiplicity resolution

Let `Q` be the set of distinct selected steps. For each `q in Q`, let `X_q` be its selected centers and define

```math
\Xi_q
=
\{x-\min X_q:x\in X_q,\ x>\min X_q\}.
```

Each `Xi_q` is four-term-progression-free and lies in `[1,N)`. The exact identity is

```math
\boxed{
|Q|+\sum_q|\Xi_q|=K.
}
```

Thus one copy of every distinct step becomes terminal mass, while every additional copy becomes a lower-scale recursive child.

Adding the retained structural family gives

```math
\boxed{
H(Q)
+
\sum_qH(\Xi_q)
+
\sum H(\text{structural children})
\ge
\frac53H(D)
-
\frac53\frac{r_3(N)}N.
}
```

**Primary note:** `docs/middle-multiplicity-fiber-five-thirds-recursion.md`.

---

# 6. Shell interface

The children above generally lie in `[1,N)` rather than one ratio-two interval. Before applying the deletion theorem recursively, partition every child into standard dyadic shells

```math
[2^j,2^{j+1}).
```

Harmonic mass is additive across this partition.

Therefore a claimed repeated terminal progression must survive inside a shell. An arithmetic progression present only in the unshelled child is not enough.

The original 31-element sibling example proved an algebraic child overlap but did not by itself survive this interface. The corrected 34-element construction in

```text
docs/dyadic-shell-compatible-sibling-sharpness.md
```

produces the same terminal label in a middle-fiber shell and a spanning-component shell. The verifier is

```text
src/verify_dyadic_shell_sibling_sharpness.py
```

Hence the sibling two-layer theorem is genuinely sharp after standard dyadic shelling.

---

# 7. Half-contraction and positive-moment potential

Every retained output associated with parent label `a` is at most `a/2`, and each parent produces at most two outputs. Hence, for every real `p>=1`,

```math
\boxed{
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
}
```

Across all generations, if `mu(q)` is total terminal multiplicity, then

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

# 8. Global lifted-center layers

Every recursive state has the form

```math
S=B-t,
\qquad B\subseteq D,
```

for the original root block `D`.

A terminal step `q` in `S` lifts to

```math
x-q,
\quad x,
\quad x+q
```

inside `D`.

Let

```math
\nu_q(x)
```

be the number of terminal occurrences of `q` lifting to center `x`, and define

```math
L(q)=\max_x\nu_q(x).
```

For `k>=1`, put

```math
X_{q,k}=\{x:\nu_q(x)\ge k\}.
```

Every `X_{q,k}` is a subset of `D` and is therefore four-term-progression-free. Translating every nonempty layer by its minimum gives lower-scale four-term-progression-free children `Omega_{q,k}` and the exact identity

```math
\boxed{
\mu(q)
=
L(q)
+
\sum_{k=1}^{L(q)}|\Omega_{q,k}|.
}
```

Thus all cross-state repetition occurring at different lifted centers is exported to lower-scale children.

**Primary note:** `docs/global-lifted-center-layer-resolution.md`.

---

# 9. Correct interpretation of amplified gadgets

The shell-compatible sharpness gadget can be translated many times inside a larger four-term-progression-free block. This gives raw fixed-label multiplicity

```math
\mu(234)\ge cN^{1/2}
```

for infinitely many block sizes `N`.

However, different translated copies have different lifted centers. The global center layers export those copies into lower-scale difference children.

Therefore the amplification rules out bounded raw fixed-label multiplicity, but it does not obstruct the reduced persistence target.

**Primary note:** `docs/cross-state-fixed-label-amplification.md`.

---

# 10. Current unresolved quantity

After within-node fibers and global lifted-center layers, the remaining multiplicity is

```math
\boxed{
L(q)=\max_x\nu_q(x).
}
```

This counts how many recursive states reuse one exact lifted progression

```math
x-q,
\quad x,
\quad x+q.
```

A crude bound is

```math
L(q)\ll\frac Nq,
```

from binary branching and logarithmic depth, or from the localized linear-label budget.

This is far too weak for reciprocal summability.

The active closing target is:

```math
\boxed{
\text{prove an exact-progression persistence theorem.}
}
```

Useful forms would include:

1. a sublinear bound on `L(q)` that is strong when the parent density is large;
2. a charge from every repeated persistence event to a new root point or smaller difference;
3. a theorem showing that long persistence forces a large affine grid or forbidden configuration;
4. a stopping-time potential for one fixed lifted progression.

---

# 11. False, corrected, and superseded statements

Do not use the following without additional hypotheses:

1. uniformly bounded depth-two affine-lift overlap;
2. universal uncorrected local `8/3` packing;
3. naive recursive density increment in the inherited three-dilate class;
4. universal one-layer sibling collapse.

The original 31-element sibling file is now classified as an algebraic precursor, not a shell-resolved recursive example.

The binary factors

```math
\frac76,
\qquad
\frac43,
\qquad
\frac{16}{9}
```

remain valid but are superseded as raw occurrence bounds by `8/3`.

No current theorem closes the exact-progression persistence gap. The full Erdős problem remains unresolved.