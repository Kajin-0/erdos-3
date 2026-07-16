# Coordinated-deletion total owner degree two

## Status

State-independent ownership theorem for the coordinated-deletion output architecture consisting of dyadically resolved backbone children and selected middle-fiber children.

For every physical parent root pair, the total number of retained current and recursive latent owners is at most two.

---

## 1. Output architecture

Fix one completed coordinated deletion schedule on a finite parent root set `P`.

Let

```math
a=\min P.
```

The output architecture has two child types.

### Backbone children

Every backbone child has reference root `a`. The remaining parent roots are partitioned by role and dyadic shell before retention. Consequently one parent root belongs to at most one retained backbone root set.

### Middle-fiber children

Every selected action has one sponsor root. A root sponsors at most one selected action because it is deleted immediately after selection.

For one selected step `d`, choose the deterministic base action used to translate its centers. The base sponsor is the affine reference of the middle fiber and is omitted from the middle child root set. Every other sponsor at step `d` appears once as a middle child root, subject to shell resolution and retention.

Sponsor uniqueness therefore implies:

```math
\boxed{
\text{one parent root belongs to at most one middle child root set.}
}
```

---

## 2. Current and latent ownership

Fix one physical parent pair

```math
f=\{r,p\}.
```

A current owner of `f` is an affine child with reference `r` and root `p`.

A latent owner is a recursive child whose root set contains both `r` and `p`.

Point-disjoint numerical child supports imply that `f` has at most one current owner:

```math
c_f\le1.
```

The latent degree theorem gives

```math
\ell_f\le2,
```

with equality possible only for one backbone owner and one middle owner.

The remaining question is whether one current owner can coexist with two latent owners.

---

## 3. Current backbone owner

Suppose the current owner is a backbone child. Then its reference is

```math
r=a.
```

The pivot root `a` is omitted from every backbone child root set, so no backbone child can own `f` latently.

The root `a` can sponsor at most one selected action and hence can belong to at most one middle child root set. Therefore

```math
\ell_f\le1.
```

Thus

```math
c_f=1
\quad\Longrightarrow\quad
c_f+\ell_f\le2
```

in the backbone-current case.

---

## 4. Current middle owner

Suppose the current owner is a middle-fiber child generated at step `d`. Then `r` is the base sponsor for that step.

The base sponsor is omitted from its own middle child root set. Since one root sponsors at most one selected action, `r` cannot belong to any other middle child root set.

The root `r` may belong to one retained backbone root set, but the backbone partition places it in at most one such child. Hence again

```math
\ell_f\le1.
```

Therefore

```math
c_f=1
\quad\Longrightarrow\quad
c_f+\ell_f\le2
```

in the middle-current case.

---

## 5. Total owner theorem

If `c_f=0`, the latent degree theorem gives `ell_f<=2`.

If `c_f=1`, the preceding case analysis gives `ell_f<=1`.

Hence for every physical parent pair,

```math
\boxed{
c_f+\ell_f\le2.
}
```

Equivalently, the only repeated-owner profiles are

```text
one current + one latent;
or
one backbone latent + one middle latent.
```

The profile

```text
one current + two latent
```

is impossible.

---

## 6. Exact branching consequence

The row-star branching excess count is

```math
(c_f+\ell_f-1)_+.
```

The total degree theorem implies

```math
\boxed{
(c_f+\ell_f-1)_+\in\{0,1\}.
}
```

Thus one physical parent resource creates at most one additional occurrence after first appearance.

Moreover, the two possible extra occurrences are mutually exclusive:

```text
current-latent profile: one current occurrence;
latent-latent profile: one middle occurrence if no reserve is matched.
```

---

## 7. Critical owner-scale contraction

Let the parent shell base be `N`.

### Current-latent profile

The extra current occurrence lies in a child shell of base at most `N/2`. Therefore

```math
\Theta_1(\text{extra current})
\le
\frac12\Theta_1(f;N).
```

### Latent-latent profile

If a center/opposite reserve pays the duplicate, no occurrence recurses. Otherwise the extra original middle occurrence lies at scale at most `N/4`, so

```math
\Theta_1(\text{middle export})
\le
\frac14\Theta_1(f;N).
```

Since the profiles cannot occur together,

```math
\boxed{
\Theta_1(\text{complete overlap residue of }f)
\le
\frac12\Theta_1(f;N).
}
```

This improves the coarse `3/4` bound obtained by treating the two residual types as simultaneously possible.

---

## 8. Strategic consequence

The economical activation row has a binary local structure:

```text
no extra owner;
one current continuation at half owner scale;
one middle continuation at quarter owner scale;
or physical reserve termination.
```

No physical pair can branch into both a current-overlap lineage and a middle-export lineage. The remaining global first-appearance tree therefore has residual critical reproduction coefficient at most `1/2` per physical parent resource.
