# Canonical hole-witness pair reuse

## Status

State-independent bounded-reuse theorem for four-AP hole witnesses.

The theorem applies after a missing completion integer has been certified by
three points of a four-AP-free ambient subset. It does not bound sponsor-pair
transport multiplicity. Instead, it assigns every certified hole to one
adjacent support pair in its four-term witness and proves that this canonical
support pair is used by at most two distinct holes.

---

## 1. Four-AP hole witnesses

Let `P` be a set of integers. A hole witness for `c notin P` is a four-term
progression

```math
A_c=(a,a+h,a+2h,a+3h),
\qquad h>0,
```

such that exactly one point of `A_c` is missing from `P`, and that missing point
is `c`.

Write `j(c)` for the missing position in `{0,1,2,3}`. Choose one witness
deterministically when a hole has several witnesses.

Every witness contains at least one adjacent pair of present points. Define the
canonical support pair to be the first adjacent present pair:

```math
f(c)=
\begin{cases}
\{a+h,a+2h\},&j(c)=0,\\
\{a+2h,a+3h\},&j(c)=1,\\
\{a,a+h\},&j(c)=2,\\
\{a,a+h\},&j(c)=3.
\end{cases}
```

In every case,

```math
w(f(c))=\frac1h.
```

---

## 2. At most two holes per canonical pair

Fix one canonical support pair

```math
f=\{x,x+h\}.
```

A hole assigned to `f` can have only the following values.

### Left hole

For missing position `0`, the pair is `{a+h,a+2h}`, so

```math
c=x-h.
```

For missing position `1`, the pair is `{a+2h,a+3h}`, and again

```math
c=x-h.
```

Thus both left-oriented witness types request the same hole integer.

### Right holes

For missing position `2`,

```math
c=x+2h,
```

and its witness requires `x+3h in P`.

For missing position `3`,

```math
c=x+3h,
```

and its witness requires `x+2h in P`.

These two distinct right holes cannot both occur: the first requires `x+2h` to
be absent and `x+3h` present, while the second requires the opposite.

Therefore one canonical support pair can serve at most one left hole and at
most one right hole:

```math
\boxed{
|\{c:f(c)=f\}|\le2.
}
```

No arithmetic-progression hypothesis beyond the witness definition is needed
for this multiplicity bound.

---

## 3. Aspect-weighted target payment

Suppose a terminal pair target `e_c` requests the certified hole `c`. Let

```math
D_c
```

be the target pair gap, while `h_c` is the witness step. Then

```math
\boxed{
w(e_c)
=
\frac1{D_c}
=
\frac{h_c}{D_c}w(f(c)).
}
```

This is an exact pointwise aspect identity.

For the near regime

```math
h_c\le D_c,
```

one has

```math
w(e_c)\le w(f(c)).
```

Since every canonical support pair receives at most two holes,

```math
\boxed{
\sum_{c:\ h_c\le D_c}w(e_c)
\le
2\sum_{f\in F_{\rm near}}w(f),
}
```

where `F_near` is the union of canonical support pairs used in the near regime.

More generally, in the dyadic aspect band

```math
2^{k-1}D_c<h_c\le2^kD_c,
```

one has

```math
w(e_c)\le2^k w(f(c)),
```

and hence

```math
\boxed{
\sum_{c\text{ in band }k}w(e_c)
\le
2^{k+1}
\sum_{f\in F_k}w(f).
}
```

Thus certified-hole first-target mass has a bounded-reuse transport into actual
physical pairs of the witness support. The remaining issue is not multiplicity
at this map; it is how the support-pair union is paid or transported without
double spending existing pair capacity.

---

## 4. Certified S7 frontier profile

For the `9334` certified `S7` holes on the terminal-payment frontier, the
canonical assignment uses

```text
8301 distinct support pairs;
1033 support pairs used by two holes;
maximum support-pair multiplicity = 2.
```

The complete canonical support-pair masses are

```text
support-pair union mass       = 392.983106001285...
support-pair occurrence mass  = 513.150748986601...
support-pair reuse mass       = 120.167642985316...
```

The certified-hole completion-first target mass is

```math
218.754197271041\ldots.
```

After choosing one maximum-weight target for every canonical support pair, only

```math
6.230106721495\ldots
```

of that mass is repeated at the support-pair assignment layer.

In the near regime `h<=D`, the `4452` certified holes use

```text
3847 distinct support pairs;
605 support pairs used by two holes;
maximum multiplicity = 2.
```

Their first-target mass is

```math
128.373650251777\ldots.
```

The state-independent coefficient `2` is sharp on this frontier: some support
pairs receive two near targets each having weight equal to the support-pair
weight.

---

## 5. Relation to existing no-go results

The repository proves that recursive sponsor-pair and latent-pair multiplicity
has no universal finite bound. The present theorem does not contradict that
result.

The two maps are different:

```text
recursive source pair -> terminal transport target
```

can have unbounded multiplicity in general, while

```text
certified completion hole -> canonical adjacent witness pair
```

has multiplicity at most two by the four-point witness geometry.

This is precisely why the completion layer is useful: saturation converts an
unbounded branching object into a bounded-reuse local support object.

---

## 6. Remaining transfer obligation

The next theorem must connect the canonical support-pair union to one of the
already approved resources:

1. parent three-AP edge capacity when the support pair belongs to a completed
   parent witness;
2. affine pair first appearance when the support pair is already activated;
3. rectangle-aspect or reference-gap transport when the support pair is reused;
4. terminal first appearance when the support pair is new to the active
   lineage.

The support-pair multiplicity is now controlled. What remains is a
collision-sound first-appearance rule preventing the same physical support pair
from paying both the original sponsor-pair ledger and the new hole-witness
ledger without an explicit release.
