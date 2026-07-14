# Terminal-basin overflow transfer

## Status

State-independent refinement of sponsor-pair forward transport for a distinct
activated physical-pair set.

The theorem eliminates transport-target multiplicity completely. One activated
pair per deterministic terminal basin is transported to the terminal target;
all other activated pairs are exported at their original owner as strictly
lower-scale four-AP-free distance fibers.

---

## 1. Deterministic terminal map

Let `P` be a finite root set with a complete coordinated deletion schedule.
For every unordered pair `e` with at least one sponsor endpoint, apply the
monotone forward-transport rule until the pair reaches one of:

1. a direct selected-action edge;
2. a backward obstruction pair;
3. a residual pair in `binom(Q,2)`.

Pairs already in `binom(Q,2)` are terminal with path length zero.

Denote the deterministic terminal target by

```math
T(e).
```

Forward transport gives

```math
\boxed{w(e)\le w(T(e)).}
```

---

## 2. Terminal basins of an activated pair set

Let

```math
E\subseteq\binom P2
```

be a distinct activated pair set. Partition `E` by terminal target:

```math
E_z
=
\{e\in E:T(e)=z\}.
```

For every nonempty basin choose one deterministic representative

```math
\rho(z)\in E_z.
```

Define

```math
E_{\rm rep}=\{\rho(z):E_z\ne\varnothing\}
```

and

```math
E_{\rm over}=E\setminus E_{\rm rep}.
```

The terminal targets of representatives are distinct. Therefore

```math
\sum_{e\in E_{\rm rep}}w(e)
\le
\sum_{z:E_z\ne\varnothing}w(z).
```

No terminal multiplicity coefficient appears.

---

## 3. Overflow pairs always have an owner

Suppose

```math
e\in E_{\rm over}.
```

Then its basin contains another distinct pair with the same terminal target.
The pair `e` cannot already be residual-residual: a residual pair has
`T(e)=e`, so no distinct pair with path length zero has the same target unless
it transports into `e`, in which case the residual pair itself may be chosen
as representative and every other basin member has a sponsor endpoint.

Choose representatives with the rule:

```text
if the terminal target itself belongs to E, choose it;
otherwise choose the lexicographically first basin member.
```

Under this rule every overflow pair has at least one sponsor endpoint and
therefore a unique owner: the endpoint deleted first.

---

## 4. Owner-distance fibers

Assume the affine root state is represented in a shell of base `M`, so

```math
\operatorname{diam}(P)<M.
```

For every sponsor root `s`, split its overflow counterparts by side:

```math
F_s^+
=
\{t-s:\{s,t\}\in E_{\rm over},\ t>s,\ s\text{ owns }\{s,t\}\},
```

```math
F_s^-
=
\{s-t:\{s,t\}\in E_{\rm over},\ t<s,\ s\text{ owns }\{s,t\}\}.
```

Each fiber is four-AP-free. For example,

```math
s+F_s^+
```

is a subset of the four-AP-free root set `P`; the other case follows by
reflection and translation.

Every token satisfies

```math
0<d<M.
```

After standard dyadic resolution, every nonempty fiber shell has base at most

```math
\boxed{M/2.}
```

The overflow mass is represented exactly:

```math
\boxed{
J(E_{\rm over})
=
\sum_s
\left(
H(F_s^+)+H(F_s^-)
\right).
}
```

No pair overlap or inequality is used in this identity.

---

## 5. Distinct terminal-target row

Let

```math
Z_D,
\qquad
Z_B,
\qquad
Z_Q
```

be the distinct direct, backward, and residual terminal targets reached by the
activated basins.

Combining representative transport with the exact overflow identity gives

```math
\boxed{
\begin{aligned}
J(E)
\le{}&
J(Z_D)
+
J(Z_B)
+
J(Z_Q)\\
&+
\sum_s
\left(
H(F_s^+)+H(F_s^-)
\right).
\end{aligned}
}
```

Every terminal target appears once. Transport-target collision reuse has been
replaced by genuine lower-scale four-AP-free fibers.

---

## 6. Direct target capacity

Every direct target is one of the two sponsor edges of a selected action.
Sponsor edges are globally distinct. Therefore

```math
J(Z_D)
\le
\frac32\sum_j\frac1{q_j}.
```

Under the parity-oriented selected-edge schedule, these direct edges belong to
the exact selected-edge creation/release ledger. They are not an external
recurring scalar cost.

---

## 7. Refined master row

Apply the exact activated-pair union transfer to a selected three-AP occurrence
family `A`. It gives a distinct activated pair set `E_act` and lower-scale AP
fibers `F_AP`:

```math
L(\mathcal A)
\le
J(E_{\rm act})+H(\mathcal F_{\rm AP}).
```

Apply terminal-basin overflow transfer to `E_act`. Then

```math
\boxed{
\begin{aligned}
L(\mathcal A)
\le{}&
J(Z_D)
+
J(Z_B)
+
J(Z_Q)\\
&+
H(\mathcal F_{\rm AP})
+
H(\mathcal F_{\rm over}).
\end{aligned}
}
```

where:

```text
AP fibers descend by at least two dyadic levels;
overflow distance fibers descend by at least one dyadic level.
```

There is no transport-collision term.

---

## 8. Why basin selection is preferable to first coalescence

A first-coalescence construction tracks the detailed intersection geometry of
transport paths. That is unnecessary for mass accounting.

The terminal map already partitions the distinct starting pair set into
basins. One representative exhausts the distinct terminal capacity; all other
starting pairs retain their original pair weights and owner provenance. Their
owner-distance fibers are canonical lower-scale states.

This avoids weight inflation from charging every basin member at the terminal
target weight.

---

## 9. Remaining theorem

After this refinement, the only terminal pair terms are distinct:

```text
direct selected-action targets;
backward obstruction targets;
residual terminal targets.
```

The only recursive terms are explicit four-AP-free fibers with strict scale
descent.

The remaining whole-tree problem is therefore:

1. first-appearance/release accounting for distinct backward and residual
   terminal pairs;
2. external-completion and genuine-hole obstruction export;
3. packing the AP and owner-distance recursive fibers across parent states.

Transport-target multiplicity is no longer an independent obstruction.
