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

divergence of `sum_{n in A}1/n` is equivalent up to constants to

```math
\sum_j\alpha_j=\infty.
```

A four-term-progression-free divergent candidate must have `alpha_j -> 0`.

---

## CL-002: Sponsored side-anchor deletion

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

For a four-term-progression-free block `D subseteq[N,2N)`, repeated coordinated side-anchor deletion removes

```math
K=|D|-s
```

sponsors and leaves a three-term-progression-free residual of size

```math
s\le r_3(N).
```

Every deleted sponsor creates one selected middle-step occurrence `q<=N/2`.

**Primary notes:**

- `docs/side-anchor-sponsored-middle-recursion.md`
- `docs/side-anchor-deletion-dag.md`

---

## CL-003: Minimum-translation backbone

**Status:** proved in repository.

**Certainty:** high internally.

**Audit state:** awaiting independent review.

For

```math
m=\min D,
```

define

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

Every backbone output associated with parent `d` satisfies

```math
0<d-m\le d/2.
```

**Primary note:** `docs/minimum-translation-backbone-recursion.md`.

---

## CL-004: Raw binary factor three

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

The full middle family and minimum-translation backbone form a binary occurrence genealogy satisfying

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

**Caveat:** equal numerical terminal labels are counted repeatedly.

**Consequence:** the previous raw factors `7/6`, `4/3`, `16/9`, and `8/3` are superseded.

**Primary note:** `docs/minimum-translation-backbone-recursion.md`.

---

## CL-005: Exact within-state middle multiplicity fibers

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

Let `Q` be the distinct selected steps and `Xi_q` the corresponding center-difference children. Then

```math
\boxed{
|Q|+
\sum_q|\Xi_q|
=K.
}
```

Every additional copy of a selected middle step becomes a lower-scale four-term-progression-free child.

**Primary note:** `docs/middle-multiplicity-fiber-five-thirds-recursion.md`.

---

## CL-006: Binary multiplicity-resolving factor two

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

Combining the exact middle multiplicity fibers with the minimum-translation backbone gives

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

**Consequence:** the previous multiplicity-resolving factor `5/3` is superseded.

**Primary note:** `docs/minimum-translation-backbone-recursion.md`.

---

## CL-007: Half-contraction and positive moments

**Status:** proved in repository.

**Certainty:** medium-high for the one-step inequality; medium for the multigeneration use.

**Audit state:** awaiting independent review.

Every retained output associated with parent `a` is at most `a/2`, and every parent creates at most two outputs. Therefore

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
2^{1-p}
\sum_{a\text{ root}}a^p.
}
```

Recursive depth is logarithmic.

**Primary note:** `docs/half-contraction-multiscale-label-potential.md`.

---

## CL-008: Recursive children must be shell-resolved

**Status:** required interface condition.

**Certainty:** high.

A recursive child in `[1,N)` must be partitioned into standard dyadic shells before side-anchor deletion is reapplied. A progression crossing shell boundaries is not a recursive terminal event.

**Consequence:** every multigeneration overlap theorem or counterexample must be checked after shell decomposition.

---

## CL-009: Global lifted-center layer decomposition

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

Every recursive state has the form

```math
S=B-t,
\qquad B\subseteq D_{\mathrm{root}}.
```

Let `nu_q(x)` count terminal occurrences of step `q` lifting to center `x`. Put

```math
L(q)=\max_x\nu_q(x)
```

and

```math
X_{q,k}=\{x:\nu_q(x)\ge k\}.
```

Translating each nonempty layer gives four-term-progression-free children `Omega_{q,k}` satisfying

```math
\boxed{
\mu(q)
=
L(q)
+
\sum_{k=1}^{L(q)}|\Omega_{q,k}|.
}
```

**Consequence:** every repeated terminal label occurring at a different lifted center is exported.

**Primary note:** `docs/global-lifted-center-layer-resolution.md`.

---

## CL-010: Root-anchor layer decomposition

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

Every nonroot recursive state has a root anchor `t in D_root`. For one exact lifted progression, let `lambda_{x,q}(t)` count copies produced in states with anchor `t`. Define

```math
M_{x,q}
=
\max_{t\in D}\lambda_{x,q}(t).
```

Nested anchor layers translate to lower-scale four-term-progression-free children `Gamma_{x,q,k}` with

```math
\boxed{
\sum_{t\in D}\lambda_{x,q}(t)
=
M_{x,q}
+
\sum_{k=1}^{M_{x,q}}|\Gamma_{x,q,k}|.
}
```

**Consequence:** every exact-progression copy occurring with a different root translation anchor is exported.

**Primary note:** `docs/state-anchor-layer-and-antichain-budget.md`.

---

## CL-011: Same-anchor antichain budget

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

Let

```math
a=x-\sigma(q)q
```

be the root sponsor of an exact lifted progression. In a state anchored at `t`, its local sponsor label is `a-t`.

Copies with the same anchor have equal positive label `a-t` and form an antichain in the half-contracting occurrence tree. Therefore

```math
\boxed{
\lambda_{x,q}(t)(a-t)
\le a.
}
```

Hence

```math
\boxed{
\lambda_{x,q}(t)
\le
\left\lfloor\frac{a}{a-t}\right\rfloor.
}
```

High multiplicity implies

```math
\lambda_{x,q}(t)\ge m
\quad\Longrightarrow\quad
 t\ge a\left(1-\frac1m\right).
```

If

```math
T_m(x,q)
=
\{t\in D:\lambda_{x,q}(t)\ge m\},
```

then

```math
\boxed{
|T_m(x,q)|
\le
r_4\!\left(\left\lceil a/m\right\rceil+1\right).
}
```

**Consequence:** unresolved same-anchor persistence is concentrated in a short interval immediately below the sponsor.

**Primary note:** `docs/state-anchor-layer-and-antichain-budget.md`.

---

## CL-012: Sharp aligned middle-backbone diamond

**Status:** proved in repository and computationally verified.

**Certainty:** high for the finite certificate.

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

while the minimum-translation backbone shell contains the same progression. Both children have root anchor `N`.

**Consequence:** one parent can create two copies of the same local progression with the same anchor. The one-parent bound `2` is sharp; a universal one-copy-per-anchor claim is false.

**Primary note:** `docs/minimum-backbone-aligned-diamond-counterexample.md`.

**Verifier:** `src/verify_minimum_backbone_aligned_diamond.py`.

---

## CL-013: Supporting deletion-DAG structural balance

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

Merge-difference and spanning-component children satisfy

```math
\sum_v|\Delta_v|=K-s+\rho,
```

```math
\sum_j|\Theta_j|=K+s-\rho,
```

and

```math
\boxed{
\sum_v|\Delta_v|
+
\sum_j|\Theta_j|
=2K.
}
```

These results are no longer needed for the strongest one-generation constants, but remain supporting overlap geometry.

**Primary notes:**

- `docs/deletion-dag-merge-difference-recursion.md`
- `docs/spanning-forest-binary-four-thirds-recursion.md`

---

## CL-014: Shell-compatible spanning-component sharpness

**Status:** proved in repository and computationally verified.

**Certainty:** high for the finite certificate.

A 34-element four-term-progression-free root block produces the same terminal label `234` in a middle-fiber shell and a spanning-component shell.

**Consequence:** universal one-layer sibling collapse is false for the older component recursion even after shell resolution.

**Primary note:** `docs/dyadic-shell-compatible-sibling-sharpness.md`.

**Verifier:** `src/verify_dyadic_shell_sibling_sharpness.py`.

---

# Superseded quantitative results

The raw binary factors

```math
\frac76,
\qquad
\frac43,
\qquad
\frac{16}{9},
\qquad
\frac83
```

remain valid but are superseded by CL-004.

The multiplicity-resolving factor `5/3` remains valid but is superseded by CL-006.

---

# Explicitly false or corrected targets

Do not use the following without new hypotheses:

1. uniformly bounded depth-two affine-lift overlap;
2. universal uncorrected local `8/3` packing;
3. naive recursive density increment in the inherited three-dilate class;
4. universal one-layer sibling collapse;
5. universal one-copy-per-anchor persistence;
6. the original 31-element overlap as a shell-resolved recursive terminal example.

---

# Open bottleneck OB-001: Same-anchor predecessor convergence

After CL-005, CL-009, and CL-010, the unresolved multiplicity is

```math
\boxed{
\text{one identical local progression repeated across incomparable states with the same root anchor.}
}
```

CL-011 gives

```math
\lambda(a-t)\le a,
```

and local multiplicity two is realizable by CL-012.

Multiplicity larger than two requires several parent states to converge to the same new anchor and preserve the same local progression.

Approved targets:

1. export predecessor-anchor convergence diamonds to additional lower-scale difference children;
2. prove that repeated aligned convergence forces a forbidden affine configuration;
3. combine the short-anchor-interval tail with parent density;
4. construct a stopping-time potential for one local progression;
5. search for shell-compatible self-replicating aligned diamonds.

No current theorem closes this gap.