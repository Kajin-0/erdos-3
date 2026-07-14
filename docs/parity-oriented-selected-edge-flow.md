# Parity-oriented selected-edge flow

## Status

Symbolic edge-resource conservation theorem for a coordinated deletion schedule
whose sponsor side is fixed globally by the two-adic parity of the selected
three-AP step.

The theorem aligns the deletion schedule with full-edge coordinated branching.
It converts selected-action edge reuse into an exact creation/termination path
ledger.

---

## 1. Parity-oriented deletion rule

At every deletion step choose any current three-term progression

```math
x,
\qquad
x+q,
\qquad
x+2q,
\qquad q>0.
```

Delete the sponsor endpoint prescribed by

```math
\epsilon(q)=v_2(q)\pmod2.
```

For definiteness:

```text
even v_2(q): delete the left endpoint x;
odd  v_2(q): delete the right endpoint x+2q.
```

The opposite convention is equivalent. Repeated deletion terminates at a
three-AP-free residual because every step removes one root from a selected
three-AP.

The rule fixes one and only one sponsor orientation for every numerical step.

---

## 2. Direct and survivor edges

Write the selected progression in sponsor orientation as

```math
s,
\qquad
m=s+\varepsilon q,
\qquad
o=s+2\varepsilon q,
```

where `s` is deleted and `m,o` survive the action.

The two sponsor edges are

```math
\{s,m\},
\qquad
\{s,o\},
```

with total weight

```math
\frac1q+\frac1{2q}
=
\frac3{2q}.
```

The survivor edge is

```math
\{m,o\}
```

with weight

```math
\frac1q.
```

Thus the complete selected-AP edge energy splits exactly as

```math
\boxed{
\frac5{2q}
=
\frac3{2q}
+
\frac1q.
}
```

The first term is sponsor-edge release; the second is continuing pair
capacity.

---

## 3. Sponsor edges are globally distinct

Let `D` be the set of all sponsor edges over the schedule.

Every sponsor edge contains the sponsor root deleted at its action. Suppose the
same unordered pair were a sponsor edge at two different actions.

- If the sponsor endpoint were the same, one root would be deleted twice.
- If the sponsor endpoints were different, the sponsor deleted at the earlier
  action would have to remain present at the later action.

Both are impossible. Therefore

```math
\boxed{
|D|=2\times\text{number of selected actions}
}
```

at the occurrence level, and every pair token in `D` has multiplicity one.

---

## 4. Survivor edges are globally distinct

Let `S` be the set of all survivor edges.

Fix one unordered pair

```math
e=\{u,v\},
\qquad u<v,
\qquad q=v-u.
```

There are only two three-APs in which `e` is the adjacent survivor pair of an
endpoint deletion:

```math
u-q,\ u,\ v
```

and

```math
u,\ v,\ v+q.
```

The first deletes the left endpoint; the second deletes the right endpoint.
The parity rule permits exactly one of these sponsor orientations for step
`q`.

Hence at most one selected action can create `e` as its survivor edge:

```math
\boxed{
\operatorname{mult}_S(e)\le1.
}
```

Thus `S` is also a distinct physical-pair set.

---

## 5. Ordered overlap between survivor and sponsor edges

A pair may belong to both `S` and `D`, but its temporal order is forced.

If `e` first appears as a sponsor edge, one endpoint is deleted immediately,
so `e` cannot later become a survivor edge.

Therefore

```math
\boxed{
e\in S\cap D
\quad\Longrightarrow\quad
\text{the survivor creation occurs before the sponsor release}.}
```

Such a pair is created as continuing capacity and later terminates when one of
its endpoints becomes a sponsor.

No pair has a sponsor-release-then-survivor history.

---

## 6. Exact creation/release ledger

Define

```math
J(E)=\sum_{e\in E}w(e)
```

for a distinct pair set `E`.

The selected-action survivor mass is

```math
J(S)
=
\sum_j\frac1{q_j}.
```

The sponsor-edge release mass is

```math
J(D)
=
\frac32\sum_j\frac1{q_j}.
```

Because both sets are internally distinct,

```math
J(S)+J(D)
=
J(S\cup D)+J(S\cap D).
```

Thus

```math
\boxed{
\frac52\sum_j\frac1{q_j}
=
J(S\cup D)
+
J(S\cap D).
}
```

The union is pair first appearance. The intersection is exact later release of
capacity created earlier.

The repeated occurrence term is not unpaid overlap; it has a monotone temporal
meaning.

---

## 7. Relation to sponsor-pair forward transport

Every direct terminal target of sponsor-pair forward transport is a member of
`D`. Therefore direct transport targets are paid by sponsor-edge release.

If a direct target also belongs to `S`, its capacity was created by an earlier
selected action and is now released. If it does not belong to `S`, the direct
edge first appears only at its terminal sponsor action.

This removes double-payment ambiguity between:

```text
selected-action edge production;
direct sponsor-pair transport termination.
```

Both are one pair path with first appearance and later release.

---

## 8. Relation to full-edge branching

Full-edge branching assigns all three physical edges of every selected
three-AP:

```text
sponsor-middle edge;
sponsor-opposite edge;
middle-opposite survivor edge.
```

The parity-oriented deletion rule uses exactly the same side choice as the
coordinated full-edge construction. Hence the local factor `5/2` has the exact
resource interpretation

```text
3/2 sponsor-edge terminal release
+
1 survivor-edge continuing capacity.
```

No role edge is unassigned.

---

## 9. Strategic consequence

The selected-action term in the master activated-pair/fiber transfer need not
be treated as a recurring scalar cost. It is an edge-flow ledger:

```text
selected action
-> one distinct survivor pair carried forward
   + two distinct sponsor edges released;

survivor pair later selected as sponsor edge
-> exact terminal release of the same capacity.
```

The remaining proof obligations are transport collisions, backward/residual
terminal targets, lower-scale recursive fibers, and external-completion/hole
release. Direct selected-action capacity itself has exact no-double-payment
semantics under the parity-oriented schedule.
