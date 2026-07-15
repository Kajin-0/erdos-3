# Heavy-shell horizontal-star transfer

## Status

State-independent transfer lemma for recursive completion-step fibers.

Every non-singleton step shell in one dyadic block is paid by a physical horizontal star already present in its double-affine completion lift. All star-pair gaps lie strictly below the step-shell base. Therefore recursive heavy-fiber harmonic mass can be converted into smaller-gap physical pair capacity.

The lemma is occurrencewise. Reuse of the same horizontal pair across distinct completion fibers remains a first-appearance/reference-gap packing problem.

---

## 1. Dyadic step shell

Let

```math
T\subseteq[M,2M)
```

be finite with at least two elements. Write

```math
d_0=\min T.
```

For every

```math
d\in T\setminus\{d_0\},
```

one has

```math
0<d-d_0<M.
```

Moreover,

```math
d-d_0<d.
```

If `d_1` is the second-smallest element, then

```math
d_1-d_0<d_0,
```

because `d_1<2M` and `d_0>=M`.

---

## 2. Harmonic star domination

Define the difference star

```math
\operatorname{Star}(T)
=
\{d-d_0:d\in T\setminus\{d_0\}\}.
```

For the second-smallest element,

```math
\frac1{d_1-d_0}
>
\frac1{d_0}.
```

For every remaining `d`,

```math
\frac1{d-d_0}
>
\frac1d.
```

Assign the first star term to `1/d_0` and every other star term to its corresponding `1/d`. This gives

```math
\boxed{
H(T)
<
H(\operatorname{Star}(T)).
}
```

Equivalently,

```math
\boxed{
\sum_{d\in T}\frac1d
<
\sum_{d\in T\setminus\{d_0\}}
\frac1{d-d_0}.
}
```

No arithmetic-progression hypothesis is required.

---

## 3. Physical horizontal lift

A completion-step fiber has one of the three double-affine forms.

### Right adjacent role

```math
c+T,
\qquad
c+2T.
```

### Left adjacent role

```math
c-T,
\qquad
c-2T.
```

### Outer role

```math
c-T,
\qquad
c+T.
```

All displayed points belong to the ambient root set because every `d in T` indexes one physical target pair.

Choose the first displayed copy deterministically. Its minimum-step horizontal star is

```math
E_{c,T}
=
\bigl\{
\{c+\sigma d_0,c+\sigma d\}:
 d\in T\setminus\{d_0\}
\bigr\}
```

with the evident sign convention for the role. Each pair has gap

```math
|d-d_0|.
```

Therefore

```math
J(E_{c,T})
=
H(\operatorname{Star}(T))
>
H(T).
```

For an outer role the recursive debt is only `H(T)/2`, so the same star also pays it.

Writing the role coefficient as

```math
\alpha\in\{1,1/2\},
```

one obtains

```math
\boxed{
\alpha H(T)
<
J(E_{c,T}).
}
```

---

## 4. Strict gap descent

Every horizontal star pair satisfies

```math
\operatorname{gap}(e)<M.
```

After standard dyadic resolution, its gap shell base is at most

```math
M/2.
```

Thus the transfer has strict pair-gap descent:

```text
recursive step shell at base M
    -> horizontal physical pairs of gap below M.
```

This is stronger than merely re-emitting the same recursive shell.

---

## 5. Terminal and recursive cases

A singleton heavy shell has no horizontal star. Such a shell is automatically three-AP-free and belongs to the terminal ledger.

Any recursive heavy shell contains a three-AP and hence at least three elements. The horizontal-star transfer therefore applies to every recursively continuing heavy shell.

Consequently the direct maximal-discharge row may replace

```math
\sum_{T\in\mathcal R_{\rm heavy}}\alpha(T)H(T)
```

by horizontal pair occurrences of strictly smaller gap.

---

## 6. Multiplicity interface

For a fixed embedded fiber `(c,role,T)`, the horizontal star is a physical pair set and contains no internal duplicate.

Across different embedded fibers, the same horizontal pair may reappear. This is a genuine pair-resource collision. It must not be hidden by summing occurrence energies.

Repeated horizontal stars have the same affine rectangle structure as the earlier collision fibers. For a fixed numerical state and orientation, varying completions produce translated copies; their reference set and reference-difference reserve are four-AP-free and lie below the parent scale.

Therefore the approved packing interface is:

```text
first horizontal-pair appearance
    -> carried smaller-gap physical pair;
repeated horizontal-pair occurrence
    -> reference-difference / rectangle token;
```

The present lemma proves the local mass transfer and strict gap descent. The reference-gap theorem supplies the multiplicity object.

---

## 7. Strategic consequence

After direct maximal completion, every activated pair has one of four outcomes:

```text
local three-AP edge token;
cross-shell new pair;
light canonical support pair;
heavy-shell horizontal star.
```

The last three are physical pair resources. For recursive heavy shells, their gaps are strictly smaller than the shell base that generated them.

Thus the remaining treewise problem can be formulated entirely as first appearance and reuse of physical pairs, together with terminal sinks. No free-standing recursive harmonic state is necessary once the horizontal-star lift is applied.