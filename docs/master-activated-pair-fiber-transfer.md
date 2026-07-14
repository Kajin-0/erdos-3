# Master activated-pair / recursive-fiber transfer

## Status

State-independent composition of:

1. exact activated-pair union transfer for selected three-AP occurrences;
2. sponsor-pair forward transport;
3. direct/backward/residual terminal classification.

The theorem is a complete one-generation interface. It does not yet prove that
the backward, residual, transport-collision, and recursive-fiber terms are
globally summable.

---

## 1. Parent root state and deletion schedule

Let `P` be a finite four-AP-free root set equipped with a complete coordinated
deletion schedule. Let

```math
P=Q\sqcup\Sigma
```

where `Q` is the final three-AP-free residual and `Sigma` is the set of deleted
sponsor roots.

At deletion step `j`, the selected progression is

```math
s_j,
\qquad
s_j+\epsilon_jq_j,
\qquad
s_j+2\epsilon_jq_j,
```

with sponsor `s_j` and step `q_j>0`.

Let `A` be any selected family of distinct three-AP occurrences inside `P`.

---

## 2. Activated-union decomposition

Apply the exact activated-pair union theorem to `A`. It produces:

```text
E_act: a distinct unordered physical-pair set in P;
F(A): a family of strictly lower-scale four-AP-free fibers.
```

Write

```math
H(\mathcal F(\mathcal A))
=
\sum_{F\in\mathcal F(\mathcal A)}H(F).
```

Then

```math
\boxed{
L(\mathcal A)
\le
J(E_{\rm act})
+
H(\mathcal F(\mathcal A)).
}
```

Every pair in `E_act` is paid once, and every fiber shell descends by at least
two dyadic levels relative to the parent block.

---

## 3. Initial residual pairs

Split the activated pair union into

```math
E_{QQ}
=
E_{\rm act}\cap\binom Q2
```

and

```math
E_\Sigma
=
E_{\rm act}\setminus E_{QQ}.
```

Pairs in `E_QQ` are already terminal residual targets. Every pair in
`E_Sigma` has at least one sponsor endpoint and is eligible for monotone
forward transport.

---

## 4. Sponsor-pair terminal transport

Apply deletion-rank forward transport to every pair in `E_Sigma`.
Every pair terminates at exactly one of:

1. a direct selected-action edge;
2. a backward obstruction pair;
3. a residual pair in `binom(Q,2)`.

Let

```math
D(E_{\rm act}),
\qquad
B(E_{\rm act}),
\qquad
R(E_{\rm act})
```

be the distinct direct, backward, and residual terminal targets after adding
the initial `E_QQ` pairs to the residual class.

Let

```math
\mu(z)
```

be the number of activated pairs transported to terminal target `z`, and put

```math
C_{\rm trans}(E_{\rm act})
=
\sum_z(\mu(z)-1)_+w(z).
```

Monotonicity of pair weight along transport gives

```math
J(E_{\rm act})
\le
\sum_{z\in D}w(z)
+
\sum_{z\in B}w(z)
+
\sum_{z\in R}w(z)
+
C_{\rm trans}(E_{\rm act}).
```

---

## 5. Direct selected-action capacity

Every selected action of step `q_j` has two sponsor edges of weights

```math
\frac1{q_j}
```

and

```math
\frac1{2q_j}.
```

Hence the distinct direct terminal targets satisfy

```math
\sum_{z\in D}w(z)
\le
\frac32\sum_j\frac1{q_j}.
```

Define

```math
I_{\rm sel}(P)
=
\sum_j\frac1{q_j}.
```

---

## 6. Master transfer inequality

Combining the activated-union row with terminal pair transport gives

```math
\boxed{
\begin{aligned}
L(\mathcal A)
\le{}&
\frac32 I_{\rm sel}(P)\\
&+
J(B(E_{\rm act}))\\
&+
J(R(E_{\rm act}))\\
&+
C_{\rm trans}(E_{\rm act})\\
&+
H(\mathcal F(\mathcal A)).
\end{aligned}
}
```

Every term has exact semantics:

```text
selected-action incidence;
backward obstruction targets;
residual terminal targets;
transport-target collision reuse;
strictly lower-scale recursive fibers.
```

There is no entering full pair energy `J(P)` and no unnamed overlap
coefficient.

---

## 7. Completed-target refinement

Apply the terminal-pair arithmetic-progression witness theorem to the backward
and residual target union.

The targets whose specified completion belongs to `P` have total distinct
weight at most

```math
\frac52\mathcal L_3(P).
```

The remaining targets split into:

```text
completion roots in the ambient set but outside the current lineage P;
genuine ambient holes carrying four-AP saturation witnesses.
```

Thus the master row can be refined to

```math
\boxed{
\begin{aligned}
L(\mathcal A)
\le{}&
\frac32 I_{\rm sel}(P)
+
\frac52\mathcal L_3(P)\\
&+
M_{\rm external}(P)
+
M_{\rm hole}(P)\\
&+
C_{\rm trans}(E_{\rm act})
+
H(\mathcal F(\mathcal A)).
\end{aligned}
}
```

This version is structurally complete but not numerically contracting because
`L_3(P)` itself may be large. The base-six no-go theorem shows that this term
must be handled by the same occurrence-family transpose rather than by a
scalar bound in terms of `H(P)`.

---

## 8. Recursive closure of the AP-load terms

Every selected-action or completed-target three-AP family is itself a selected
family of distinct three-AP occurrences in `P`. Therefore the exact
activated-pair union theorem may be reapplied to those AP families.

This gives a recursive normal form:

```text
any weighted AP occurrence term
-> distinct activated physical pairs
   + strictly lower-scale four-AP-free fibers.
```

The master row is therefore closed under its own AP-load outputs. The only
nonrecursive terminal interfaces are:

```text
backward/external/hole obstruction witnesses;
residual terminal pairs;
transport target collisions;
terminal first appearance.
```

---

## 9. Active whole-tree obligation

The remaining theorem is to prove a global first-appearance ledger for:

1. direct selected-action pair targets;
2. backward and residual terminal pair targets;
3. transport-collision target pairs;
4. lower-scale recursive fibers generated by near/far incidence transfer;
5. external completion roots and genuine hole witnesses.

All local production, activation, transport, and recursive-fiber maps are now
explicit and state-independent. Further finite frontier propagation is not the
bottleneck and remains deferred.
