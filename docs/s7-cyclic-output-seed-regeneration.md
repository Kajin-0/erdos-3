# Regeneration of the canonical contaminated seed from `S_7` output

## Status

Exact fixed-policy path theorem.

A novel shell-resolved middle-fiber child emitted by the `S_7` cyclic
terminal-fiber component regenerates the canonical state `S_1` in one valid
factor-four step. It therefore has the complete previously certified
continuation through `S_10` and into the exact scale-eight tail.

This is a structural recurrence inside the replay genealogy. It is not yet a
whole-tree theorem because the retention quotient for simultaneous raw outputs
has not been proved.

**Verifier:** `src/verify_s7_scc_seed_regeneration.py`.

**Certificate:** `data/s7_scc_seed_regeneration_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
2d6296a1f161ef2b971681ad7ce967720c530c65298169a664e1983644f4fac3
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

The state was already identified as the first size-at-least-three survivor of
the complete small-state affine test for both factor two and factor four.

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

This is the repository's canonical `BASE_PATTERN`. It is four-term-
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

The equality is numerical, not merely isomorphic after an affine change of
variables.

---

## 3. Certified continuation

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

This does not create a divergent path: the complete recorded continuation is
summable. Its significance is that a novel child emitted at depth seven can
restart the entire contaminated seed geometry at a lower local scale.

---

## 4. Exact normalized charge

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

These values are pathwise accounting data. They are not a simultaneous-child
Bellman estimate.

---

## 5. Consequence for the proof program

The small-state residual is not explained by weak additive structure. The
state `{16,21,26}` is precisely a compressed precursor of the base pattern.
One cheap extension unfolds it into the original contaminated genealogy.

Therefore a valid retention theorem cannot simply classify small surviving
states as negligible terminal errors. At least one such state is a
**regenerative seed**.

The relevant mechanism is now

```text
S7 cyclic terminal output
    -> novel shell child {16,21,26}
    -> factor-four separation 1
    -> exact regeneration of S1
    -> contaminated chain through S10
    -> exact summable tail.
```

This explains why complete one-generation affine obstruction coverage does not
close the cyclic output: part of the residual is structured to reproduce an
already known difficult state.

---

## 6. Scope

The theorem proves an exact continuation path under the restricted replay
model. It does not prove:

1. that this occurrence is retained after a valid overlap quotient;
2. that multiple regenerated copies may be counted independently;
3. that the return path causes divergent whole-tree mass;
4. that every surviving child has a comparable continuation;
5. or that the full four-term Erdős problem is solved.

The retention question is essential because the seed occurrence may overlap
other simultaneous children or share provenance with them.

---

## 7. Revised target

The next structural question is no longer only whether residual candidates
gain obstruction support in one generation. It is:

> How many provenance-distinct regenerative seeds can survive simultaneously,
> and can their total restarted-chain charge be bounded by the parent SCC
> output, overlap, or obstruction capacity?

The immediate finite tasks are:

1. identify every exact cyclic-source child that regenerates a previous
   certified state or a translated copy of one;
2. retain origin provenance for each regeneration;
3. compute overlap and containment among regenerative occurrences;
4. test whether regenerative multiplicity is bounded by forced-fork output,
   SCC capacity, or a Carleson packing estimate;
5. incorporate the exact restarted-chain charge into the branching-reserve LP
   only after the retention rule is justified.
