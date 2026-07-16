# Current-latent overlap decomposition

## Status

State-independent exact decomposition of row-star branching after point-disjoint affine retention.

At most one retained child can own a fixed parent resource as a current pair. After assigning current-pair mass to the current harmonic ledger, the complete residual pair-activation collision is exactly latent-pair reuse among recursive children.

---

## 1. Current and latent owner counts

Fix one parent root-pair resource

```math
f=\{p,q\},
\qquad
D(f)=|p-q|.
```

In a point-disjoint retained affine child family define:

```math
c_f
=
\#\{\text{current owners of }f\},
```

and

```math
\ell_f
=
\#\{\text{recursive latent owners of }f\}.
```

A current owner maps `f` numerically to the child pair

```math
\{0,D(f)\}.
```

Point-disjoint child supports therefore imply

```math
\boxed{c_f\in\{0,1\}.}
```

The total owner multiplicity is

```math
m(f)=c_f+\ell_f.
```

---

## 2. Row-star branching excess

The parent-pair first-appearance ledger provides one copy of `f` whenever `m(f)>0`. The raw row-star branching excess is

```math
\frac{(c_f+\ell_f-1)_+}{D(f)}.
```

Because `c_f` is zero or one, the exact integer identity is

```math
\boxed{
(c_f+\ell_f-1)_+
=
c_f\mathbf 1_{\ell_f>0}
+
(\ell_f-1)_+.
}
```

Indeed:

- if `c_f=0`, both sides equal `(ell_f-1)_+`;
- if `c_f=1` and `ell_f=0`, both sides vanish;
- if `c_f=1` and `ell_f>=1`, both sides equal `ell_f`.

---

## 3. Current-latent overlap term

The term

```math
c_f\mathbf 1_{\ell_f>0}\frac1{D(f)}
```

is present only when one current occurrence and at least one latent occurrence share the parent resource.

The current occurrence is already one current harmonic term of its child:

```math
\frac1{D(f)}.
```

Assign this occurrence to the current harmonic ledger rather than treating it as a second latent-pair activation.

Point disjointness makes the assignment injective because every numerical current pair `{0,D}` has at most one retained owner.

The current owner may be terminal or recursive:

- terminal current owner: the term enters the terminal sink ledger;
- recursive current owner: the term remains in the recursive current/harmonic ledger.

In neither case should it also be charged as anonymous pair-activation collision.

---

## 4. Exact latent-only residual

After separating current-latent overlap, the residual pair-activation collision for `f` is

```math
\boxed{
R_{\rm latent}(f)
=
\frac{(\ell_f-1)_+}{D(f)}.
}
```

Summing over parent resources gives

```math
\boxed{
R_{\rm branch}
=
R_{\rm current-latent}
+
R_{\rm latent-latent},
}
```

where

```math
R_{\rm current-latent}
=
\sum_f
c_f\mathbf 1_{\ell_f>0}\frac1{D(f)},
```

and

```math
R_{\rm latent-latent}
=
\sum_f
\frac{(\ell_f-1)_+}{D(f)}.
```

Only `R_latent-latent` is a genuine repeated activation of latent pair energy.

---

## 5. Relation to terminal-current absorption

If the unique current owner is terminal, its current term can be recorded in the terminal first-appearance ledger. This is the special case proved in

```text
docs/terminal-current-branch-absorption.md.
```

The present theorem is broader. It separates current-latent overlap even when the current owner is recursive.

The theorem is a bookkeeping reduction, not a claim that recursive current harmonic mass is free. That mass must still be handled by direct discharge and pair-lineage termination. The gain is that it is not counted a second time as latent activation collision.

---

## 6. Latent-latent state overlap

Every residual unit has at least two recursive latent owners. For recursive affine children with augmented root sets

```math
A_i=\{r_i\}\cup Q_i,
```

latent resources are the pairs inside `Q_i`. Hence one residual parent pair lies in

```math
\binom{Q_i\cap Q_j}{2}
```

for at least one recursive state pair `i,j`.

Consequently the residual is bounded by recursive root-intersection energy:

```math
\boxed{
R_{\rm latent-latent}
\le
\sum_{i<j\atop i,j\text{ recursive}}
J(Q_i\cap Q_j).
}
```

As before, this pairwise envelope may overcount resources with three or more latent owners.

---

## 7. Exact `S7` consequence

On the certified residual-sponsor split `R4 -> F5` retained transition, the only repeated parent resources are

```text
{1455716,1455863};
{1455716,1455868};
{1455716,1455869}.
```

Each has exactly:

```text
c_f   = 1  terminal current owner;
ell_f = 1  recursive latent owner.
```

Therefore

```math
(\ell_f-1)_+=0
```

for every repeated resource, and

```math
\boxed{
R_{\rm latent-latent}=0.
}
```

The raw branching excess

```math
\frac1{147}+\frac1{152}+\frac1{153}
```

is entirely current-latent overlap and is exactly the harmonic mass of the terminal state `{147,152,153}`.

---

## 8. Strategic consequence

After point-disjoint retention, the pair-activation problem is narrower than row-star multiplicity suggests.

The genuine residual excludes:

```text
all unique parent resources;
all current-only resources;
one latent owner paired with a current owner;
all degree-two terminal-current/recursive-latent overlaps.
```

What remains is precisely:

```text
one parent root pair occurring latently in two or more recursive retained children.
```

This is the correct target for reference-gap and common-root-intersection analysis.