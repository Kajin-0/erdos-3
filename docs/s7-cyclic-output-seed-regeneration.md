# Regeneration of the canonical contaminated seed from `S_7` output

## Status

Exact fixed-policy path theorem and exact finite uniqueness result.

A novel shell-resolved middle-fiber child emitted by the `S_7` cyclic
terminal-fiber component regenerates the canonical state `S_1` in one valid
factor-four step. It therefore has the complete previously certified
continuation through `S_10` and into the exact scale-eight tail.

Among all `62` exact cyclic-source shell states and both factor-two and
factor-four extensions, this is the unique exact regeneration of any canonical
state `S_1,...,S_10`.

This is a structural recurrence inside the replay genealogy. It is not yet a
whole-tree theorem because the retention quotient for simultaneous raw outputs
has not been proved.

**Verifier:** `src/verify_s7_scc_seed_regeneration.py`.

**Certificate:** `data/s7_scc_seed_regeneration_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
b05c5b91ba5b148a1dbe999edc0617a5370889f4244cd66553c9d7a8c6ee9679
```

---

## 1. The emitted seed

The `S_7` lexicographic transition contains exactly one middle-fiber shell
occurrence with

```math
q=1,
\qquad
L=16,
\qquad
X=\{16,21,26\}.
```

None of these three labels belongs to the `S_7` minimum-translation backbone,
so this occurrence is novel relative to the parent.

The state is also the first size-at-least-three survivor of the complete
small-state affine test for both factor two and factor four.

---

## 2. Exact return to `S_1`

Adjoin the global anchor zero and take three translates with separation

```math
R=1.
```

Then

```math
G_1(X)
=
(\{0\}\cup X)
\cup
(\{0\}\cup X+1)
\cup
(\{0\}\cup X+2)
```

is exactly

```math
\boxed{
\{0,1,2,16,17,18,21,22,23,26,27,28\}.
}
```

This is the repository's canonical `BASE_PATTERN`, and it is four-term-
progression-free.

Because the next factor-four scale is

```math
4L=64,
```

translation into the standard dyadic shell gives

```math
64+G_1(X)=S_1.
```

Thus

```math
\boxed{
X\xrightarrow[f=4]{R=1}S_1.
}
```

The equality is numerical, not merely affine-isomorphic.

---

## 3. Uniqueness on the certified cyclic-source frontier

The verifier groups the `63` cyclic-source shell occurrences into `62` exact
numerical states. For every state `Y` and each factor

```math
f\in\{2,4\},
```

it checks whether the next scale `fL(Y)` equals a canonical scale and whether
some admissible separation produces exactly one of `S_1,...,S_10`.

The complete regeneration catalog is

```text
state={16,21,26}, factor=4, separation=1, target=S1.
```

No other exact cyclic-source state returns to a canonical chain state under a
factor-two or factor-four extension.

This does not rule out regeneration of a noncanonical translated shape or a
return after more than one intervening generation.

---

## 4. Certified continuation

Appending the recorded contaminated-chain transitions gives the exact scale
word

```text
4,4,8,4,4,8,4,8,8,8
```

and separation word

```text
1,61,303,1597,8195,93476,230164,2097164,16777217,134217729.
```

The path is

```math
X
\longrightarrow
S_1
\longrightarrow
S_2
\longrightarrow
\cdots
\longrightarrow
S_{10},
```

followed by the certified exact infinite tail from `S_10`.

This path remains summable. Its significance is that a novel child emitted at
depth seven restarts the entire contaminated seed geometry at a lower local
scale.

---

## 5. Exact normalized charge

Assign the seed occurrence persistence one. Then

```math
W(X)=\frac{|X|}{L}=\frac3{16}.
```

The first factor-four step creates Bellman debt

```math
\Delta_4(X)
=
\frac{3|X|+4}{L}
\left(\frac84-1\right)
=
\boxed{\frac{13}{16}}.
```

The certified future charge beginning at `S_1` is

```math
\sum_{h=1}^{9}W_h
+
\sum_{n\ge0}W_{10+n}
=
\frac{36185}{4096}.
```

Including the seed itself gives

```math
\boxed{
W(X)+\text{future charge}
=
\frac{36953}{4096}.
}
```

These are pathwise accounting data, not a simultaneous-child Bellman estimate.

---

## 6. Consequence

The small-state residual is not explained by weak additive structure. The
state `{16,21,26}` is a compressed precursor of the base pattern. One cheap
extension unfolds it into the original contaminated genealogy.

A valid retention theorem therefore cannot classify all small surviving states
as negligible terminal errors. At least one is a **regenerative seed**.

The mechanism is

```text
S7 cyclic terminal output
    -> novel shell child {16,21,26}
    -> factor-four separation 1
    -> exact regeneration of S1
    -> contaminated chain through S10
    -> exact summable tail.
```

This explains one concrete part of the residual left by complete
one-generation affine obstruction testing.

---

## 7. Scope

The theorem does not prove:

1. that this occurrence is retained after a valid overlap quotient;
2. that multiple regenerated copies may be counted independently;
3. that the return path causes divergent whole-tree mass;
4. that every surviving child has a comparable continuation;
5. or that the full four-term Erdős problem is solved.

The retention question remains essential because this occurrence may overlap
other simultaneous children or share provenance with them.

---

## 8. Revised target

The next question is:

> How many provenance-distinct regenerative or near-regenerative seeds survive
> simultaneously, and can their restarted-chain charge be bounded by parent
> SCC output, overlap, or obstruction capacity?

The immediate finite tasks are:

1. identify near-regenerations up to translation, scaling, and bounded defects;
2. retain origin provenance for each regeneration;
3. compute containment and partial overlap among regenerative occurrences;
4. test whether regenerative multiplicity obeys a Carleson packing estimate;
5. incorporate restarted-chain charge into the branching LP only after the
   retention rule is justified.
