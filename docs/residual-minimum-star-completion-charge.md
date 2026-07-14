# Residual-minimum star completion charge

## Status

State-dependent symbolic theorem for the repository's lexicographic coordinated deletion schedule on a four-AP-free affine parent.

It bounds the entire backward pair mass of the residual-minimum sponsor-backbone star by:

1. at most two copies of selected-action step incidence;
2. an explicit missing-completion obstruction.

This removes the cross residual-sponsor star from the unrestricted sponsor-core energy problem.

---

## 1. Setup

Let `P` be a finite four-AP-free root set, let

```math
a=\min P,
```

and run the lexicographic coordinated deletion schedule. Progressions are ordered by

```text
(step, left, middle, right).
```

Assume

```math
a\in Q,
```

so the minimum root survives in the final three-AP-free residual.

For every deleted sponsor `s\in\Sigma`, let `q_s` be the step of the selected action that deletes `s`. The sponsor-backbone cross pair is

```math
e_s=\{a,s\},
\qquad
d_s=s-a.
```

By the sponsor-star parity corollary, `e_s` is backward exactly when the selected action deletes its left endpoint, equivalently

```math
v_2(q_s)\equiv0\pmod2.
```

Let `L` be this set of left-sponsored roots.

Define the selected-action incidence

```math
I(P)=\sum_{j}\frac1{q_j}.
```

---

## 2. Trichotomy for a backward star

Fix `s\in L` and abbreviate

```math
d=s-a,
\qquad
q=q_s.
```

Exactly one of the following occurs.

### Far star: `d>q`

Then

```math
\frac1d<\frac1q,
```

so the pair is paid directly by the incidence of the action that deletes `s`.

### Equal scale: `d=q`

This is impossible. The four roots

```math
a,\ s,\ s+q,\ s+2q
```

would form a four-term arithmetic progression in `P`.

### Close star: `d<q`

Define the doubling completion

```math
c=2s-a=a+2d.
```

If `c\notin P`, record the missing-completion obstruction `(a,s,c)`.

Suppose instead that `c\in P`. The progression

```math
(a,s,c)
```

has step `d<q`, so its tuple precedes the selected action that eventually deletes `s`.

At the time this progression is processed, both `a` and `s` are still present:

- `a` is residual;
- `s` is deleted only by its later step-`q` action.

There are two possibilities.

1. **`c` is still present.** Then `(a,s,c)` is selected. Because `a` survives, the coordinated side rule cannot delete the left endpoint `a`; it deletes `c`. The selected action has step exactly `d`.
2. **`c` is absent.** Then `c` was deleted by an earlier selected action. Since that action's tuple precedes `(d,a,s,c)`, its step `q_c` satisfies

   ```math
   q_c\le d.
   ```

In both cases the close star is assigned to one selected action with step `q_*\le d`, and therefore

```math
\frac1d\le\frac1{q_*}.
```

---

## 3. Injectivity of the close-star charge

For fixed residual minimum `a`, the completion map

```math
s\longmapsto c=2s-a
```

is injective.

Every root is deleted as sponsor at most once. Hence two distinct close stars cannot be assigned through the same completion root to the same selected deletion action.

Therefore the total non-missing close-star mass is bounded by one copy of the selected-action incidence:

```math
\sum_{\substack{s\in L\\d_s<q_s\\2s-a\in P}}
\frac1{d_s}
\le
I(P).
```

The far-star assignment is also injective: each far star is charged to its own selected action. Thus

```math
\sum_{\substack{s\in L\\d_s>q_s}}
\frac1{d_s}
\le
I(P).
```

---

## 4. Completion-charge inequality

Define the missing-completion mass

```math
M_a(P)
=
\sum_{\substack{s\in L\\d_s<q_s\\2s-a\notin P}}
\frac1{d_s}.
```

Combining the far, equal, and close cases gives

```math
\boxed{
\sum_{s\in L}\frac1{s-a}
\le
2I(P)+M_a(P).
}
```

The left side is exactly the backward star-pair mass involving the residual minimum.

Consequently, all cross residual-sponsor star pairs satisfy

```math
\boxed{
W_{\rm star}
\le
W_{\rm star}^{\rm forward}
+
2I(P)
+
M_a(P),
}
```

where the forward part enters the monotone sponsor-pair transport ledger.

---

## 5. Interpretation

The troublesome star debt is no longer an arbitrary subset of

```math
\{\{a,s\}:s\in\Sigma\}.
```

It has an exact decomposition:

```text
odd-v2 sponsor actions  -> monotone forward transport;
even-v2 far stars       -> own selected-action incidence;
even-v2 close stars     -> earlier selected-action incidence;
missing 2s-a            -> explicit completion obstruction.
```

The coefficient `2` has a transparent source: one selected action can pay once for its own far star and once as the deletion action assigned to an earlier close-star completion. No action receives two close-star charges.

---

## 6. Remaining obstruction

The only unpaid cross residual-sponsor term is

```math
M_a(P).
```

Each term certifies that the root

```math
2s-a
```

is absent even though `a,s` survive together until the action deleting `s` and `s` participates as the left sponsor of a larger-step progression.

This is an extension/completion obstruction rather than latent pair energy. The next target is to connect `M_a(P)` to one of:

1. the existing completion-support ledger;
2. cheap-extension exclusion;
3. terminal first appearance of the missing doubled root;
4. a dyadic packing bound for the injective missing-completion map.

Internal sponsor-sponsor pairs and transport-collision reuse remain separate obligations.
