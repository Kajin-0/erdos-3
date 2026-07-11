# Certainty ledger

This file records claims that should survive context loss. Each entry states status, confidence, audit state, and consequence.

The full Erdős reciprocal-sum problem remains open. The authoritative dependency order is in `docs/current-proof-program.md`.

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

a divergent reciprocal sum is equivalent up to constants to

```math
\sum_j\alpha_j=\infty.
```

A four-term-progression-free divergent candidate must have `alpha_j -> 0`.

---

## CL-002: Side-anchor deletion produces an affine DAG

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

For a four-term-progression-free block `D subseteq [N,2N)`, side-anchor deletion gives an acyclic graph with two outgoing edges from every deleted sponsor and no outgoing edges from residual vertices.

**Primary note:** `docs/side-anchor-deletion-dag.md`.

---

## CL-003: Exact structural balance

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

Merge-difference children satisfy

```math
\sum_v|\Delta_v|=K-s+\rho,
```

and spanning-component children satisfy

```math
\sum_j|\Theta_j|=K+s-\rho.
```

Therefore

```math
\boxed{
\sum_v|\Delta_v|+\sum_j|\Theta_j|=2K.
}
```

Retaining at most one structural occurrence per parent preserves at least `2K/3` occurrences.

**Primary notes:**

- `docs/deletion-dag-merge-difference-recursion.md`
- `docs/spanning-forest-binary-four-thirds-recursion.md`

---

## CL-004: Full middle children and binary eight-thirds occurrence growth

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

For each center `x`, the full middle child

```math
M_x=\{q_i:b_i=x\}
```

is four-term-progression-free. Retaining every middle occurrence and at most one structural occurrence per parent gives

```math
\boxed{
\sum H(\text{binary child occurrences})
\ge
\frac83H(D)
-
\frac83\frac{r_3(N)}N.
}
```

**Caveat:** equal numerical labels are counted repeatedly.

**Primary note:** `docs/full-middle-binary-eight-thirds-recursion.md`.

---

## CL-005: Exact within-node middle multiplicity fibers

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

For distinct selected steps `Q` and center fibers `X_q`, define

```math
\Xi_q
=
\{x-\min X_q:x\in X_q,\ x>\min X_q\}.
```

Then

```math
\boxed{
|Q|+\sum_q|\Xi_q|=K.
}
```

Every additional copy of a middle label becomes a lower-scale four-term-progression-free child.

**Primary note:** `docs/middle-multiplicity-fiber-five-thirds-recursion.md`.

---

## CL-006: Binary multiplicity-resolving five-thirds recursion

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

The terminal representatives, fiber children, and thinned structural children satisfy

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

The genealogy remains binary.

**Primary note:** `docs/middle-multiplicity-fiber-five-thirds-recursion.md`.

---

## CL-007: Half-contraction and global positive moments

**Status:** proved in repository.

**Certainty:** medium-high for the one-step inequality; medium for the multigeneration application.

**Audit state:** awaiting independent review.

Every retained output associated with parent `a` is at most `a/2`, and every parent produces at most two outputs. Therefore

```math
\boxed{
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p
\qquad(p\ge1).
}
```

If `mu(q)` is total terminal multiplicity across all generations, then

```math
\boxed{
\sum_q\mu(q)q^p
\le
2^{1-p}\sum_{a\text{ root}}a^p.
}
```

**Primary note:** `docs/half-contraction-multiscale-label-potential.md`.

---

## CL-008: Recursive children must be shell-resolved

**Status:** required interface condition.

**Certainty:** high.

A recursive child usually lies in `[1,N)`, not in one ratio-two block. Before reapplying the deletion theorem, it must be partitioned into standard dyadic shells

```math
[2^j,2^{j+1}).
```

Harmonic mass is additive across the shells. A progression spanning shell boundaries is not a recursive terminal event.

**Consequence:** every multigeneration overlap or counterexample must be checked after shell decomposition.

---

## CL-009: Dyadic-shell-compatible sibling two-layer sharpness

**Status:** proved in repository and computationally verified.

**Certainty:** high for the finite certificate.

**Audit state:** verifier included; conceptual interpretation awaiting independent review.

A 34-element four-term-progression-free root block in `[8192,16384)` produces terminal label

```math
q=234
```

in both:

1. a middle multiplicity-fiber shell `[512,1024)`;
2. a spanning-component shell `[2048,4096)`.

Therefore universal one-layer sibling collapse is false even after standard dyadic shelling.

**Primary note:** `docs/dyadic-shell-compatible-sibling-sharpness.md`.

**Verifier:** `src/verify_dyadic_shell_sibling_sharpness.py`.

---

## CL-010: Original 31-element sibling example is algebraic only

**Status:** corrected classification.

**Certainty:** high.

The original progression `15,33,51` crosses every ratio-two shell. The 31-element example proves the algebraic intersection obstruction but must not be cited alone as a shell-resolved recursive terminal counterexample.

**Primary note:** `docs/sibling-two-layer-sharpness-counterexample.md`.

---

## CL-011: Global lifted-center layer decomposition

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

Every recursive state has the form

```math
S=B-t,
\qquad B\subseteq D,
```

for the root block `D`. Every terminal occurrence of step `q` lifts to a three-term progression of the same step in `D`.

Let `nu_q(x)` count occurrences lifting to center `x`, and define

```math
L(q)=\max_x\nu_q(x),
```

and

```math
X_{q,k}=\{x:\nu_q(x)\ge k\}.
```

Translating each nonempty layer gives four-term-progression-free children `Omega_{q,k}` with

```math
\boxed{
\mu(q)
=
L(q)
+
\sum_{k=1}^{L(q)}|\Omega_{q,k}|.
}
```

**Consequence:** all cross-state repetition at different lifted centers is exported. The remaining multiplicity is repeated use of one exact lifted progression.

**Primary note:** `docs/global-lifted-center-layer-resolution.md`.

---

## CL-012: Raw fixed-label multiplicity can grow polynomially

**Status:** proved by finite avoidance.

**Certainty:** medium.

**Audit state:** quantitative counting argument awaiting independent review.

Translated copies of the shell-compatible gadget give, for infinitely many block sizes,

```math
\mu(234)\ge cN^{1/2}.
```

The copies have different lifted centers and are handled by CL-011.

**Consequence:** raw fixed-label multiplicity cannot be bounded absolutely or polylogarithmically. The active target must concern exact lifted progression persistence.

**Primary note:** `docs/cross-state-fixed-label-amplification.md`.

---

# Superseded quantitative results

The binary factors

```math
\frac76,
\qquad
\frac43,
\qquad
\frac{16}{9}
```

remain valid but are superseded as raw occurrence bounds by `8/3`.

---

# Explicitly false or corrected targets

The following must not be used without new hypotheses:

1. uniformly bounded depth-two affine-lift overlap;
2. universal uncorrected local `8/3` packing;
3. naive recursive density increment in the inherited three-dilate class;
4. universal one-layer sibling collapse;
5. use of the original 31-element overlap as a shell-resolved terminal counterexample.

---

# Open bottleneck OB-001: Exact-progression persistence

After CL-005 and CL-011, the unresolved multiplicity is

```math
\boxed{
L(q)=\max_x\nu_q(x),
}
```

the number of recursive states that reuse one exact lifted progression

```math
x-q,
\quad x,
\quad x+q.
```

A crude bound is `L(q) << N/q`, which is insufficient.

Approved targets:

1. charge repeated persistence to new root points or smaller differences;
2. prove that long persistence forces a large affine grid;
3. construct a stopping-time potential for one fixed progression;
4. search for self-replicating shell-compatible gadgets.

No current theorem closes this gap.