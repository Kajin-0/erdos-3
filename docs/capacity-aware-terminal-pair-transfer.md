# Capacity-aware terminal-pair transfer

## Status

State-independent collision-sound refinement of the edge-first terminal-pair
light/heavy transfer.

The theorem removes the only local double-spend in the earlier master row. A
source pair retained as collision capacity cannot simultaneously pay a light
completion fiber. Such supports are declared reserved and their fibers are
routed to the heavy lower-scale class instead.

---

## 1. Source first use and collision reserve

Let `A` be a finite set of distinct activated physical pairs in a four-AP-free
root universe `P`. Let

```math
T:A\to Z
```

be any terminal transport map satisfying

```math
w(e)\le w(T(e)).
```

For every target `z in Z`, choose one deterministic maximum-weight source

```math
e_z^*\in T^{-1}(z).
```

Define

```math
F_{\rm src}=\{e_z^*:z\in Z\}
```

and the collision-source set

```math
C_{\rm src}=A\setminus F_{\rm src}.
```

Because the activated source family is a physical set rather than an occurrence
multiset,

```math
\boxed{
J(A)=J(F_{\rm src})+J(C_{\rm src}).
}
```

Also

```math
J(F_{\rm src})
\le
J(Z).
```

Therefore

```math
\boxed{
J(A)
\le
J(Z)+J(C_{\rm src}).
}
```

The former source-weighted collision scalar is exactly the physical pair energy
`J(C_src)`. It is carried as pair capacity; it is not an anonymous error term.

---

## 2. Edge-first target partition

Partition the physical target union into

```math
Z
=
Z_{\rm edge}
\sqcup
Z_{\rm hole}
\sqcup
Z_{\rm amb}.
```

Here:

- `Z_edge` consists of pairs that are edges of three-APs lying entirely in the
  charged root universe `P`;
- `Z_hole` consists of the remaining targets assigned certified same-shell
  completion holes;
- `Z_amb` is the true ambient, outside-shell, or uncertified remainder.

Then

```math
J(Z_{\rm edge})
\le
\frac52\mathcal L_3(P)
```

and, writing

```math
M_{\rm amb}=J(Z_{\rm amb}),
```

one has

```math
J(A)
\le
\frac52\mathcal L_3(P)
+
J(Z_{\rm hole})
+
M_{\rm amb}
+
J(C_{\rm src}).
```

---

## 3. Reserved-support light/heavy rule

Assign every selected certified hole `c` its canonical adjacent witness support
pair `f(c)`. For each completion and orientation form the four-AP-free step
fiber

```math
S_{c,\sigma}
=
\{d:\{c+\sigma d,c+2\sigma d\}\in Z_{\rm hole}\}.
```

For one physical support pair `f`, let

```math
m(f)
```

be the number of nonempty oriented fibers assigned to it. The canonical
hole-support theorem gives

```math
m(f)\le4.
```

Call `f` reserved when

```math
f\in C_{\rm src}.
```

Use the capacity-aware threshold

```math
\tau(f)
=
\begin{cases}
0,&f\in C_{\rm src},\\[2mm]
\dfrac1{m(f)\operatorname{gap}(f)},&f\notin C_{\rm src}.
\end{cases}
```

A fiber is light when

```math
H(S_{c,\sigma})\le\tau(f(c))
```

and heavy otherwise.

Consequently every fiber on a reserved support is heavy. Let

```math
F_{\rm light}
```

be the physical union of supports carrying at least one light fiber. Then

```math
\boxed{
F_{\rm light}\cap C_{\rm src}=\varnothing.
}
```

For every unreserved support, the adaptive-share proof gives

```math
\sum_{\substack{(c,\sigma):f(c)=f\\S_{c,\sigma}\text{ light}}}
H(S_{c,\sigma})
\le
w(f).
```

Hence

```math
\boxed{
J(Z_{\rm hole})
\le
J(F_{\rm light})
+
\sum_{S\in\mathcal H_{\rm cap}}H(S),
}
```

where `H_cap` is the capacity-aware heavy fiber family.

---

## 4. Collision-sound master row

Since `F_light` and `C_src` are disjoint physical pair sets,

```math
J(C_{\rm src})+J(F_{\rm light})
=
J(C_{\rm src}\cup F_{\rm light}).
```

Combining the preceding sections gives

```math
\boxed{
J(A)
\le
\frac52\mathcal L_3(P)
+
J(C_{\rm src}\cup F_{\rm light})
+
\sum_{S\in\mathcal H_{\rm cap}}H(S)
+
M_{\rm amb}.
}
```

This is a genuine pair-capacity Bellman row:

```text
entering activated pair union A;
completed parent edge expenditure;
disjoint outgoing physical pair union C_src union F_light;
lower-scale heavy fibers;
true ambient remainder.
```

No physical pair is both spent and carried in the same row.

---

## 5. Terminal/recursive refinement

Resolve every capacity-aware heavy fiber into standard dyadic shells and split
it into terminal and recursive shells:

```math
\mathcal H_{\rm cap}
=
\mathcal T_{\rm cap}
\sqcup
\mathcal R_{\rm cap}.
```

Then

```math
\boxed{
J(A)
\le
\frac52\mathcal L_3(P)
+
J(C_{\rm src}\cup F_{\rm light})
+
\operatorname{TermSink}_{\rm cap,first}
+
\sum_{R\in\mathcal R_{\rm cap}}H(R)
+
M_{\rm amb}
+
\operatorname{TermRecreate}_{\rm cap}.
}
```

Only the three-AP-containing heavy shells remain recursive.

---

## 6. Exact `S7` profile

On the certified residual-sponsor fourth-to-fifth diagnostic frontier:

```text
collision source pairs            = 34,735
collision source pair mass        = 229.736806990201...
reserved canonical supports       = 2,147
```

The capacity-aware completion split is

```text
light fibers                       = 2,214
capacity-aware heavy fibers        = 7,243
light support pairs                = 1,900
```

with

```math
L_{\rm light}
=
68.054224557837\ldots,
```

```math
L_{\rm heavy}
=
145.553283523695\ldots,
```

and

```math
J(F_{\rm light})
=
310.382378225571\ldots.
```

The outgoing physical pair union is disjoint and has mass

```math
\boxed{
J(C_{\rm src}\cup F_{\rm light})
=
540.119185215772\ldots.
}
```

After dyadic resolution, all `10,941` capacity-aware heavy shells are
three-AP-free. Thus

```math
\boxed{
\mathcal R_{\rm cap}=\varnothing
}
```

on this exact frontier, and the full heavy mass enters the terminal first-
appearance ledger.

---

## 7. Strategic consequence

The source-weighted collision term should no longer be treated as a scalar
obstruction. It is an exact carried subset of physical pair energy.

The remaining universal obligations are now:

1. pair-energy first appearance for the outgoing union
   `C_src union F_light` across different parents;
2. terminal first appearance and recreation for capacity-aware heavy shells;
3. recursive control only when a heavy shell contains a three-AP;
4. the true ambient completion term `M_amb`;
5. payment of entering pair energy before the affine pair forest begins.
