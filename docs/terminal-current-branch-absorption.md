# Terminal-current absorption of row-star branching

## Status

State-independent partial payment theorem for the row-star branching excess of a point-disjoint affine retained family.

Whenever a repeated parent resource is a current pair of a terminal child, that terminal harmonic term pays one excess occurrence of the same parent resource. Point-disjointness makes the payment injective across terminal current terms.

---

## 1. Point-disjoint owner forest

Let `F` be a point-disjoint retained affine child family. For every parent root-pair resource `f`, let

```math
I(f)
```

be its set of child owners and

```math
m(f)=|I(f)|.
```

The row-star branching excess is

```math
R_{\rm branch}
=
\sum_f\frac{(m(f)-1)_+}{D(f)}.
```

By the point-disjoint affine owner-forest theorem, child-side resource identities are unique and there is no simultaneous child recreation or cycle correction.

---

## 2. Terminal current owners

A terminal child with affine reference `r` and label `u` has parent current resource

```math
f=\{r,r+u\}
```

of gap

```math
D(f)=u.
```

The corresponding terminal harmonic term is exactly

```math
\frac1u
=
\frac1{D(f)}.
```

Call `f` terminal-covered if one of its child owners is a current occurrence in a terminal retained child.

---

## 3. Uniqueness of terminal current coverage

Two distinct point-disjoint retained children cannot both contain the same positive numerical label `u`.

Every current resource of gap `u` maps numerically to

```math
\{0,u\}.
```

Therefore at most one retained child can be a current owner of any fixed-gap child resource identity. In particular, one parent resource `f` has at most one terminal current owner in the point-disjoint family.

Moreover different terminal current resources correspond to different terminal child labels or different parent-pair identities. Thus the map

```text
terminal-covered parent resource
    -> terminal current harmonic term
```

is injective.

---

## 4. Absorbing one excess branch

If `f` is terminal-covered and `m(f)>=2`, reserve one of its `m(f)-1` excess owner occurrences and charge it to the terminal current term of `f`.

The paid mass is exactly

```math
\frac1{D(f)}.
```

Let

```math
\mathcal C_{\rm term}
=
\{f:m(f)\ge2\text{ and }f\text{ has a terminal current owner}\}.
```

Then the terminal-covered branching mass is

```math
R_{\rm term-cover}
=
\sum_{f\in\mathcal C_{\rm term}}
\frac1{D(f)}.
```

Injectivity gives

```math
\boxed{
R_{\rm term-cover}
\le
H(\mathcal T_{\rm retained}),
}
```

where the right side is the complete harmonic mass of the terminal retained children.

No terminal term pays two different parent resources.

---

## 5. Residual branching term

After terminal absorption, the remaining branching excess is

```math
\boxed{
R_{\rm branch,res}
=
\sum_f
\frac{
(m(f)-1-\mathbf 1_{\mathcal C_{\rm term}}(f))_+
}{D(f)}.
}
```

Only this residual term requires reference-pair rectangles or state-overlap payment.

Consequences:

1. every degree-two row star with one terminal current owner is closed completely;
2. a row star of degree `m` with one terminal current owner is reduced from `m-1` excess copies to `m-2`;
3. row stars with no terminal current owner are unchanged.

---

## 6. Terminal-recursive overlap geometry

Suppose the second owner of a terminal-covered pair is a recursive latent occurrence.

Let the terminal child have reference `r_T` and roots `Q_T`. Its current resource star is

```math
\{\{r_T,p\}:p\in Q_T\}.
```

If these pairs occur latently in one recursive child, then

```math
\{r_T\}\cup Q_T
```

is contained in that recursive child's root set. The complete overlap is the terminal current star, and its mass is exactly the terminal child harmonic mass:

```math
\boxed{
\sum_{p\in Q_T}\frac1{|p-r_T|}
=
H(S_T).
}
```

Thus a terminal child can be viewed as an explicit boundary face of a recursive augmented-root complete graph.

---

## 7. Exact `S7` closure

On the certified residual-sponsor split `R4 -> F5` retained transition, exactly three parent resources are repeated. All have degree two and the profile

```text
terminal current owner: backbone_sponsor;
recursive latent owner: middle_fiber.
```

They lie in parent class `65`:

```text
{1455716,1455863}, gap 147;
{1455716,1455868}, gap 152;
{1455716,1455869}, gap 153.
```

The terminal child has labels

```math
\{147,152,153\}.
```

Hence

```math
\boxed{
R_{\rm branch}
=
\frac1{147}+\frac1{152}+\frac1{153}
=
H(\{147,152,153\})
=
\frac{22697}{1139544}.
}
```

Numerically,

```text
R_branch = 0.019917616169...
```

The residual branching term is exactly zero on this transition.

The same three overlaps also generate one reference pair of gap `317`, reused three times. That rectangle ledger is valid but unnecessary for payment once terminal-current absorption is recognized.

---

## 8. Strategic consequence

The exact `S7` branching anomaly is not an unpaid far-aspect rectangle. It is terminal mass already present in the retained output.

The surviving global branching problem excludes all degree-two terminal-current/recursive-latent overlaps. It consists only of:

```text
row stars of degree at least three after one terminal credit;
repeated resources with no terminal current owner;
terminal-sink recreation across later generations;
loss incurred by selecting a point-disjoint retained quotient.
```

This substantially narrows the rectangle ledger that must be propagated.