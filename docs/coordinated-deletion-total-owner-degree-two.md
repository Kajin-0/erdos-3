# Coordinated-deletion total owner degree two

## Status

State-independent ownership theorem for the coordinated-deletion output architecture.

For every physical parent root pair, the total number of retained current and recursive latent owners is at most two:

```math
\boxed{c_f+\ell_f\le2.}
```

The ownership theorem is unchanged. Its former scale-critical corollary is corrected: coordinated middle children may occur at parent half-scale, so the exponent-one latent-latent residual can equal one full parent pair unit.

---

## 1. Output architecture

Fix one completed coordinated deletion schedule on a finite parent root set `P`, and let

```math
a=\min P.
```

### Backbone children

Every backbone child has affine reference `a`. Shelling and retention place one parent root in at most one retained backbone root set.

### Middle-fiber children

Every selected action has one sponsor root. A sponsor is removed immediately after selection and therefore sponsors at most one action. The base sponsor is the affine reference of its middle fiber and is omitted from that middle root set. Every other sponsor at the same step appears at most once, followed by shell resolution and retention.

Hence one parent root belongs to at most one middle child root set.

---

## 2. Current and latent ownership

For one physical parent pair

```math
f=\{r,p\},
```

a current owner is an affine child with reference `r` and root `p`. A latent owner is a recursive child whose root set contains both endpoints.

Point-disjoint numerical child supports imply

```math
c_f\le1.
```

The latent degree theorem gives

```math
\ell_f\le2,
```

with equality possible only for one backbone latent owner and one middle latent owner.

---

## 3. Current backbone owner

If the current owner is a backbone child, its reference is the pivot `a`.

The pivot is omitted from every backbone child root set, so no backbone child owns the pair latently. The pivot can sponsor at most one selected action and therefore belongs to at most one middle root set.

Thus

```math
c_f=1
\quad\Longrightarrow\quad
\ell_f\le1.
```

---

## 4. Current middle owner

If the current owner is a middle child, its reference is that step fiber's base sponsor.

The base sponsor is omitted from its own middle root set and cannot sponsor a second action. It may occur in at most one retained backbone root set.

Again,

```math
c_f=1
\quad\Longrightarrow\quad
\ell_f\le1.
```

---

## 5. Total owner theorem

If `c_f=0`, the latent degree theorem gives `ell_f<=2`. If `c_f=1`, the previous cases give `ell_f<=1`.

Therefore

```math
\boxed{c_f+\ell_f\le2.}
```

The only repeated profiles are:

```text
one current owner + one latent owner;
one backbone latent owner + one middle latent owner.
```

One current owner plus two latent owners is impossible.

---

## 6. Raw branching consequence

The row-star branching excess count is

```math
(c_f+\ell_f-1)_+.
```

Hence

```math
\boxed{
(c_f+\ell_f-1)_+\in\{0,1\}.
}
```

One physical parent resource creates at most one additional raw occurrence after first appearance.

The two possible extra occurrences are mutually exclusive:

```text
current-latent profile -> one additional current occurrence;
latent-latent profile  -> one additional middle occurrence unless a reserve pays it.
```

---

## 7. Correct owner-exponent coefficients

Let the parent shell base be `N` and define

```math
\Theta_p(f;N)=\frac{N^p}{\operatorname{gap}(f)}.
```

Every child shell base satisfies only

```math
L\le\frac N2.
```

Therefore:

```text
one current occurrence coefficient <= 2^{-p};
one latent occurrence coefficient  <= 2^{1-p}.
```

For the two repeated profiles,

```math
q_{\rm cur-lat}(p)\le3\,2^{-p},
```

and

```math
q_{\rm lat-lat}(p)\le2^{2-p}.
```

At exponent one:

```text
current-latent complete load <= 3/2;
latent-latent complete load  <= 2;
current-latent residual      <= 1/2;
latent-latent residual       <= 1.
```

The latent-latent residual coefficient one is attained by an exact retained-policy witness.

At exponent two:

```text
current-latent complete load <= 3/4;
latent-latent complete load  <= 1.
```

Thus all owner multiplicity fits inside the original parent pair capacity at exponent two.

Primary correction:

```text
docs/coordinated-middle-half-scale-critical-no-go.md
```

---

## 8. Strategic consequence

The local ownership architecture is binary, but not critical-contracting at exponent one:

```text
no extra owner;
one current continuation at scale at most N/2;
one middle continuation at scale at most N/2;
or physical reserve termination.
```

The exact threshold for collision-free owner packing is

```math
\boxed{p=2.}
```

Any exponent-one proof must therefore use an additional occurrence, depth, terminal, or arithmetic-obstruction ledger. The total owner theorem alone does not provide a subcritical critical coefficient.
