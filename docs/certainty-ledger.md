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

For a four-term-progression-free block `D subseteq[N,2N)`, coordinated side-anchor deletion removes

```math
K=|D|-s
```

sponsors and leaves a three-term-progression-free residual of size

```math
s\le r_3(N).
```

Every deleted sponsor creates one selected middle-step occurrence `q<=N/2`.

---

## CL-003: Minimum-translation backbone

**Status:** proved in repository.

**Certainty:** high internally.

**Audit state:** awaiting independent review.

For `m=min D`,

```math
\mathcal B(D)
=
\{d-m:d\in D,\ d>m\}
```

is four-term-progression-free, lies in `[1,N)`, has size `|D|-1`, and every associated label satisfies

```math
d-m\le d/2.
```

**Primary note:** `docs/minimum-translation-backbone-recursion.md`.

---

## CL-004: Raw binary factor three

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

The full middle family and minimum-translation backbone give

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

**Caveat:** equal numerical labels are counted repeatedly.

**Consequence:** raw factors `7/6`, `4/3`, `16/9`, and `8/3` are superseded.

---

## CL-005: Exact within-state middle multiplicity fibers

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

For distinct selected steps `Q` and center-difference children `Xi_q`,

```math
\boxed{
|Q|+
\sum_q|\Xi_q|
=K.
}
```

Every additional copy of a selected middle step becomes a lower-scale four-term-progression-free child.

---

## CL-006: Binary multiplicity-resolving factor two

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

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

**Consequence:** the previous multiplicity-resolving factor `5/3` is superseded.

---

## CL-007: Half-contraction and positive moments

**Status:** proved in repository.

**Certainty:** medium-high for one step; medium for the full multigeneration use.

**Audit state:** awaiting independent review.

Every parent creates at most two outputs, each at most half its label. Therefore

```math
\boxed{
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p
\qquad(p\ge1).
}
```

If `mu(q)` is total terminal multiplicity, then

```math
\boxed{
\sum_q\mu(q)q^p
\le
2^{1-p}
\sum_{a\text{ root}}a^p.
}
```

Recursive depth is logarithmic.

---

## CL-008: Shell resolution is mandatory

**Status:** required interface condition.

**Certainty:** high.

Every child in `[1,N)` must be partitioned into standard dyadic shells before deletion is reapplied. A progression crossing shell boundaries is not a recursive terminal event.

---

## CL-009: Global lifted-center layer decomposition

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

Let `nu_q(x)` count terminal copies of step `q` lifting to center `x`. Define

```math
L(q)=\max_x\nu_q(x)
```

and

```math
X_{q,k}=\{x:\nu_q(x)\ge k\}.
```

Translating each nonempty center layer gives four-term-progression-free children `Omega_{q,k}` satisfying

```math
\boxed{
\mu(q)
=
L(q)
+
\sum_{k=1}^{L(q)}|\Omega_{q,k}|.
}
```

**Consequence:** every repeated label occurring at a different lifted center is exported.

---

## CL-010: Root-anchor layer decomposition

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

Let `lambda_{x,q}(t)` count copies of one exact lifted progression produced in states with root anchor `t`. Put

```math
M_{x,q}
=
\max_{t\in D}\lambda_{x,q}(t).
```

Nested anchor layers give four-term-progression-free children `Gamma_{x,q,k}` with

```math
\boxed{
\sum_{t\in D}\lambda_{x,q}(t)
=
M_{x,q}
+
\sum_{k=1}^{M_{x,q}}|\Gamma_{x,q,k}|.
}
```

**Consequence:** every exact-progression copy occurring with a different root anchor is exported.

---

## CL-011: Same-anchor antichain budget

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

Let `a=x-sigma(q)q` be the root sponsor. Copies produced in states with one anchor `t` have equal local sponsor label `a-t` and form an antichain. Therefore

```math
\boxed{
\lambda_{x,q}(t)(a-t)
\le a.
}
```

High multiplicity implies

```math
\lambda_{x,q}(t)\ge m
\quad\Longrightarrow\quad
 t\ge a\left(1-\frac1m\right).
```

Thus unresolved persistence is concentrated in a short interval immediately below the sponsor.

---

## CL-012: Predecessor-anchor layer decomposition

**Status:** proved in repository.

**Certainty:** medium-high.

**Audit state:** awaiting independent review.

For one target anchor `t`, let `c_{x,q,t}(p)` count copies whose immediate parent state has anchor `p`. Define

```math
C_{x,q}(t)
=
\max_{p\in D}c_{x,q,t}(p).
```

Nested predecessor layers produce four-term-progression-free children `Lambda_{x,q,t,k}` satisfying

```math
\boxed{
\sum_{p\in D}c_{x,q,t}(p)
=
C_{x,q}(t)
+
\sum_{k=1}^{C_{x,q}(t)}|\Lambda_{x,q,t,k}|.
}
```

Predecessor anchors satisfy

```math
p\le2t-a<t,
```

and one fixed transition obeys

```math
\boxed{
c_{x,q,t}(p)(a-p)\le a.
}
```

The construction iterates backward through the complete anchor history.

**Primary note:** `docs/predecessor-anchor-layer-resolution.md`.

---

## CL-013: Sharp one-step aligned diamond

**Status:** proved in repository and computationally verified.

**Certainty:** high for the finite certificate.

For every `N>=32`,

```math
D_N
=
N+
\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

is four-term-progression-free.

The middle multiplicity fiber and minimum-translation backbone both produce the progression

```math
16,21,26
```

with the same root anchor.

**Consequence:** one parent can create two identical local copies; the one-parent bound `2` is sharp.

**Primary note:** `docs/minimum-backbone-aligned-diamond-counterexample.md`.

**Verifier:** `src/verify_minimum_backbone_aligned_diamond.py`.

---

## CL-014: Self-replicating aligned diamonds

**Status:** proved in repository.

**Certainty:** medium-high for the recursive construction; depth-two certificate computationally verified.

**Audit state:** awaiting independent review.

There are four-term-progression-free states `S_h` producing

```math
\boxed{2^h}
```

terminal copies of the same exact local progression with the same complete anchor history.

Their cardinalities are

```math
\boxed{
|S_h|
=
\frac{9\cdot3^h-3}{2}.
}
```

Therefore

```math
\boxed{
\text{identical-history persistence}
\asymp
|S_h|^{\log_3 2}.
}
```

The construction uses a no-carry union of three widely separated translates and duplicates the previous gadget simultaneously in a middle multiplicity fiber and a backbone shell.

**Consequence:** absolute, logarithmic, polylogarithmic, and subpower bounds below exponent `log_3 2` are false in terms of parent cardinality.

**Primary note:** `docs/self-replicating-aligned-diamond.md`.

**Verifier:** `src/verify_self_replicating_aligned-diamond-depth2.py`.

---

## CL-015: Supporting deletion-DAG structural balance

**Status:** proved in repository.

**Certainty:** medium.

**Audit state:** awaiting independent review.

Merge and spanning-component children satisfy

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

These results remain supporting overlap geometry but are no longer required for the strongest one-generation constants.

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
6. bounded or polylogarithmic identical-anchor-history persistence;
7. a subpower persistence bound with exponent below `log_3 2` in terms of parent cardinality;
8. the original 31-element overlap as a shell-resolved recursive terminal example.

---

# Open bottleneck OB-001: Density-sensitive aligned replication

CL-014 shows that four-term-progression-freeness alone allows polynomially growing exact persistence.

The construction remains sparse in its ambient interval. Its point count grows like `3^h`, while the scale required for `h` replication levels grows faster.

The active closing target is

```math
\boxed{
\text{prove that blocks with substantial reciprocal mass cannot sustain aligned-diamond replication efficiently across scales.}
}
```

Approved targets:

1. prove a lower bound on ambient scale required for `h` replication levels;
2. establish a tradeoff between persistence and dyadic density;
3. build a potential coupling reciprocal mass to the `3`-for-`2` replication law;
4. classify constructions approaching minimum scale growth;
5. show that nonsummable dyadic density is incompatible with indefinite efficient replication.

No current theorem closes this gap.