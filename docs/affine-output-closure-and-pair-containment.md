# Affine closure of coordinated deletion and universal pair-resource containment

## Status

Symbolic theorem for the coordinated side-anchor deletion construction, exact middle-fiber resolution, and dyadic shelling used throughout this repository.

The theorem is independent of the recorded `S_7` policy and of the maximum-harmonic retained quotient. It applies to every complete coordinated deletion schedule whose sponsor side is fixed by the progression step, as in the repository construction.

It proves:

1. terminal residuals, backbone shells, and middle-fiber shells of an affine parent are affine;
2. every child current pair and every child latent pair is already a parent pair resource;
3. union-valued pair capacity is nonincreasing under arbitrary output selection and retention;
4. occurrence-valued expansion is exactly pair-resource reuse.

The theorem does not bound the entering pair-resource universe.

---

## 1. Affine parent state

Let `P` be a finite set of root labels and let

```math
r<\min P.
```

Define the affine state

```math
S_r(P)
=
\{p-r:p\in P\}.
```

Every current point `u=p-r` carries root provenance `p`.

Define the complete pair-resource universe

```math
\mathcal U_r(P)
=
\{(r,p):p\in P\}
\cup
\binom{P}{2}.
```

The first class consists of **current pairs**. The second class consists of **latent pairs**.

Give each pair `(x,y)`, `x<y`, weight

```math
w(x,y)=\frac1{y-x}.
```

Then

```math
w(\mathcal U_r(P))
=
H(S_r(P))+J(P),
```

where

```math
J(P)
=
\sum_{x<y,\ x,y\in P}\frac1{y-x}.
```

---

## 2. Terminal residual closure

A coordinated deletion schedule removes selected sponsor points and leaves a residual subset

```math
R\subseteq S_r(P).
```

Let

```math
P_R
=
\{p\in P:p-r\in R\}.
```

Then

```math
\boxed{R=S_r(P_R).}
```

Thus the terminal residual remains affine with the same reference root `r`.

Its current resources are

```math
\{(r,p):p\in P_R\}
\subseteq
\mathcal U_r(P).
```

Because the residual is three-AP-free in the coordinated deletion construction, it is terminal and carries no recursive latent-pair obligation.

---

## 3. Backbone closure

Let

```math
a=\min P.
```

The minimum current label is `a-r`. The minimum-translation backbone is

```math
\begin{aligned}
\mathcal B(S_r(P))
&=
\{(p-r)-(a-r):p\in P,\ p>a\}\\
&=
\{p-a:p\in P\setminus\{a\}\}\\
&=
S_a(P\setminus\{a\}).
\end{aligned}
```

Hence the backbone is affine with reference `a`.

After dyadic shelling, every shell is

```math
S_a(Q)
```

for some subset

```math
Q\subseteq P\setminus\{a\}.
```

Its current resources are

```math
\{(a,p):p\in Q\}
\subseteq
\binom P2,
```

and its latent resources are

```math
\binom Q2
\subseteq
\binom P2.
```

Thus every backbone child resource is a parent latent pair.

---

## 4. Middle-fiber closure

Fix a selected progression step `q`. The sponsor side is determined only by `q`; write

```math
\varepsilon(q)\in\{-1,+1\}
```

so that a selected progression with current center `c` has sponsor

```math
s=c+\varepsilon(q)q.
```

Let the selected centers for step `q` be

```math
c_0<c_1<\cdots<c_m.
```

Because the parent is affine, write

```math
c_j=p_j-r
```

for center roots `p_j\in P`. The sponsor root corresponding to `c_j` is

```math
t_j
=
s_j+r
=
p_j+\varepsilon(q)q.
```

Every `t_j` belongs to `P`, because every sponsor is a parent point.

The exact middle-fiber resolution used in the repository subtracts the minimum center and assigns each positive difference the provenance of its sponsor. Therefore the fiber values are

```math
c_j-c_0
=
p_j-p_0
=
t_j-t_0,
\qquad 1\le j\le m.
```

Let

```math
T_q=\{t_0,t_1,\ldots,t_m\}.
```

Then the complete middle fiber is

```math
\boxed{
\Xi_q
=
S_{t_0}(T_q\setminus\{t_0\}).
}
```

Thus every middle fiber is affine. Its reference root is the omitted sponsor associated with the minimum center.

After dyadic shelling, every fiber shell is

```math
S_{t_0}(Q)
```

for some

```math
Q\subseteq T_q\setminus\{t_0\}.
```

Its current resources

```math
\{(t_0,t):t\in Q\}
```

and latent resources

```math
\binom Q2
```

are all parent latent pairs in `\binom P2`.

---

## 5. Affine closure theorem

Combining the three output types gives:

```math
\boxed{
\text{every raw terminal or recursive output of an affine parent is affine.}
}
```

Exact-state quotienting, selection of provenance representatives, conflict-graph retention, and passage to a subfamily do not change this conclusion. They only discard output occurrences.

Therefore, if the initial parent is represented as

```math
S_0(P)=P,
```

then every descendant carrying the repository's root-provenance convention admits affine root coordinates.

No finite-generation observation is required for this closure statement.

---

## 6. Universal pair-resource containment

Let `\mathcal C` be any collection of terminal residuals, backbone shells, and middle-fiber shells emitted by one affine parent `S_r(P)`. For a terminal child include only its current pairs. For a recursive child include its current and latent pairs.

Then

```math
\boxed{
\bigcup_{C\in\mathcal C}\mathcal U(C)
\subseteq
\mathcal U_r(P).
}
```

More precisely:

- terminal residual current pairs come from parent current pairs;
- backbone and middle-fiber current pairs come from parent latent pairs;
- every recursive child latent pair comes from parent latent pairs.

This remains true after arbitrary retained-child selection.

---

## 7. Family-level union inequality

Let `\mathcal F` be any family of affine parent occurrences, possibly with overlapping root resources. Define the union resource set

```math
\mathcal U_\cup(\mathcal F)
=
\bigcup_{S_r(P)\in\mathcal F}\mathcal U_r(P).
```

Let `\operatorname{Child}(\mathcal F)` be any retained simultaneous child family obtained by applying coordinated deletion to the parents.

Then

```math
\boxed{
\mathcal U_\cup(\operatorname{Child}(\mathcal F))
\subseteq
\mathcal U_\cup(\mathcal F).
}
```

Consequently,

```math
\boxed{
W_\cup(\operatorname{Child}(\mathcal F))
\le
W_\cup(\mathcal F),
}
```

where `W_\cup` is the total weight of distinct pair resources.

This is a state-independent whole-family Bellman inequality. It handles duplicate states, containment, partial overlap, terminal-recursive overlap, and cross-generation numerical regeneration by identifying the underlying pair token.

---

## 8. Occurrence mass and exact reuse decomposition

Let `m_\mathcal F(e)` be the occurrence multiplicity of pair token `e` in a family and define

```math
W_{\rm occ}(\mathcal F)
=
\sum_e m_\mathcal F(e)w(e).
```

Also define

```math
W_\cup(\mathcal F)
=
\sum_{e:m_\mathcal F(e)>0}w(e).
```

The repeated-payment mass is

```math
\boxed{
R_{\rm pair}(\mathcal F)
=
W_{\rm occ}(\mathcal F)-W_\cup(\mathcal F)
=
\sum_e(m_\mathcal F(e)-1)_+w(e).
}
```

Thus

```math
W_{\rm occ}(\mathcal F)
=
W_\cup(\mathcal F)+R_{\rm pair}(\mathcal F).
```

Any occurrence-valued expansion beyond the parent union capacity is exactly pair-resource reuse. Immediate provenance can classify the repeated occurrences, but it does not create new pair capacity.

---

## 9. Global first-appearance theorem

Starting from one affine root state `S_r(P)`, assign every pair token to its first occurrence in a deterministic traversal of the complete retained tree.

By universal containment, every descendant token belongs to `\mathcal U_r(P)`. Therefore

```math
\boxed{
\sum_{\text{first pair appearances}}w(e)
\le
H(S_r(P))+J(P).
}
```

Terminal first-appearance mass and recursive first-appearance current mass are both sub-sums of this resource ledger.

This proves global no-double-payment semantics for the complete affine deletion tree.

---

## 10. What remains open

The treewise overlap problem is resolved at the level of distinct pair resources. The remaining analytical problem is the size and origin of the entering pair universe.

For an initial dyadic block `D\subseteq[N,2N)`, the natural affine representation is

```math
S_0(D)=D
```

with entering capacity

```math
H(D)+J(D).
```

The unrestricted pair energy `J(D)` can be much larger than `H(D)`. The theorem therefore does not yet yield dyadic density summability.

The active analytical questions are:

1. can the pair universe be restricted to pairs actually exposed by coordinated deletion?
2. can large entering pair energy be charged to three-AP incidence, terminal output, completion, rectangle support, or cheap-extension exclusion?
3. does four-AP-freeness impose a summable multiscale bound on exposed pair energy?
4. can a stopping-time rule avoid prepaying every latent pair?
5. can pair resources be activated only when their smaller endpoint becomes a pivot?

The decisive shift is:

```math
\boxed{
\text{overlap and reuse are now exact bookkeeping problems already solved by pair tokens;}
}
```

```math
\boxed{
\text{the remaining obstacle is an economical activation bound for those tokens.}
}
```
