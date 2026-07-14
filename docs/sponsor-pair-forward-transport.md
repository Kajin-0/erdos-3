# Sponsor-pair forward transport

## Status

Symbolic one-step and iterated pair-token transport theorem for a completed coordinated deletion schedule.

The theorem does not prove the required global activation bound. It replaces the full sponsor-core energy by three explicit residual terms:

1. backward obstruction pairs;
2. collisions of transported pair tokens;
3. transported pairs that terminate entirely inside the three-AP-free residual.

This is the next analytical interface for the residual/sponsor refinement.

---

## 1. Deletion schedule

Let `P` be a finite root set. At deletion step `j`, the current set contains a three-term progression

```math
s_j,
\qquad
m_j=s_j+\epsilon_j q_j,
\qquad
o_j=s_j+2\epsilon_j q_j,
```

where

```math
q_j>0,
\qquad
\epsilon_j\in\{-1,+1\}.
```

The coordinated rule deletes the sponsor endpoint `s_j` and retains `m_j,o_j` at that step.

Let

```math
\tau(x)=j
```

when `x=s_j`, and let `\tau(x)=\infty` for roots in the final residual `Q`.

The sponsor set is

```math
\Sigma=P\setminus Q.
```

Every selected action contributes the two direct sponsor edges

```math
\{s_j,m_j\},
\qquad
\{s_j,o_j\},
```

with total pair weight

```math
\frac1{q_j}+\frac1{2q_j}
=
\frac3{2q_j}.
```

---

## 2. Pair owner

For an unordered pair token

```math
e=\{x,y\}
```

with at least one sponsor endpoint, define its owner to be the endpoint deleted first:

```math
s(e)
=
\operatorname*{argmin}_{z\in e}\tau(z).
```

The other endpoint is denoted `t(e)`.

At the deletion time of `s=s(e)`, the root `t=t(e)` is still present. The selected action of `s` therefore supplies a middle root `m` and opposite root `o` that are also still present.

The pair weight is

```math
w(\{x,y\})
=
\frac1{|x-y|}.
```

---

## 3. Direct, forward, and backward pairs

Fix an owned pair `e={s,t}` and the selected action

```math
m=s+\epsilon q,
\qquad
o=s+2\epsilon q.
```

There are three cases.

### Direct

If

```math
t\in\{m,o\},
```

then `e` is one of the two selected-action edges and transport stops.

### Forward-transportable

If

```math
|t-m|\le |t-s|,
```

transport the pair by replacing the deleted sponsor with the surviving middle root:

```math
\Phi(e)=\{m,t\}.
```

Equivalently,

```math
\epsilon
\left(
 t-s-\frac{\epsilon q}{2}
\right)
\ge 0.
```

Thus the forward region begins at the midpoint between the sponsor and the selected middle root, not at the middle root itself.

### Backward obstruction

If

```math
|t-m|>|t-s|,
```

then `e` is a backward obstruction pair and transport stops.

These are precisely the roots lying on the sponsor side of the perpendicular bisector of `s` and `m`.

---

## 4. One-step transport theorem

For every forward-transportable pair,

```math
\boxed{
w(e)
\le
w(\Phi(e)).
}
```

Indeed,

```math
|t-m|\le |t-s|
```

implies

```math
\frac1{|t-s|}
\le
\frac1{|t-m|}.
```

Both endpoints of `\Phi(e)` survive the deletion of `s`. Therefore

```math
\min_{z\in\Phi(e)}\tau(z)
>
\tau(s).
```

The minimum finite deletion rank strictly increases under every forward transport.

---

## 5. Iterated transport

Starting from any pair token with at least one sponsor endpoint, repeatedly apply `\Phi` whenever the current pair is forward-transportable.

The rank increase proves termination after at most `|\Sigma|` transports. Every initial pair terminates in exactly one of the following classes:

1. a direct selected-action edge;
2. a backward obstruction pair;
3. a residual pair in `\binom Q2`.

Let

```math
T(e)
```

be the terminal pair token. Monotonicity at every step gives

```math
\boxed{
w(e)\le w(T(e)).
}
```

No arithmetic-progression hypothesis beyond the existence of the selected deletion actions is needed for this inequality.

---

## 6. Set-valued transport inequality

Let `A` be any finite set of activated sponsor-core pair tokens. Define the terminal multiplicity

```math
\mu_A(z)
=
|\{e\in A:T(e)=z\}|.
```

Then

```math
\sum_{e\in A}w(e)
\le
\sum_z \mu_A(z)w(z).
```

Separate first use from transport collision reuse:

```math
\sum_z \mu_A(z)w(z)
=
\sum_{z:\mu_A(z)>0}w(z)
+
\sum_z(\mu_A(z)-1)_+w(z).
```

Define

```math
R_{\rm trans}(A)
=
\sum_z(\mu_A(z)-1)_+w(z).
```

Let `D(A)`, `B(A)`, and `Q(A)` be the distinct terminal targets that are respectively direct, backward, and residual. Since every distinct direct target is one of the selected-action edges,

```math
\sum_{z\in D(A)}w(z)
\le
\frac32\sum_j\frac1{q_j}.
```

Therefore

```math
\boxed{
\sum_{e\in A}w(e)
\le
\frac32\sum_j\frac1{q_j}
+
\sum_{z\in B(A)}w(z)
+
\sum_{z\in Q(A)}w(z)
+
R_{\rm trans}(A).
}
```

This is a state-independent activation-transfer inequality.

---

## 7. What the theorem accomplishes

The full sponsor-core pair energy is no longer the indivisible object. For the pair tokens that are actually activated, payment separates into:

```text
selected-action incidence
+ backward obstruction mass
+ residual target mass
+ transport collision reuse.
```

The first term has an exact local expression. The other three terms have explicit pair-token definitions and can be tested independently.

The transport theorem also supplies the required path-aware coordinate: the deletion rank of the owned sponsor increases strictly along every transported lineage.

---

## 8. Remaining proof obligations

A complete transfer lemma still requires bounds for:

1. **backward obstruction mass** — likely through four-AP completion, rectangle transport, valuation-side constraints, or cheap-extension exclusion;
2. **transport collision reuse** — likely through selected-middle incidence and the existing middle-fiber overlap ledger;
3. **residual target mass** — either show that activated lineages rarely terminate in `\binom Q2`, or connect those targets to a terminal first-appearance resource that telescopes globally.

The next exact probe should classify every activated pair on the certified retained frontiers by:

- terminal class `direct/backward/residual`;
- transport path length;
- source and terminal weight;
- terminal-target multiplicity;
- selected step and sponsor side;
- current versus latent resource type.

No further retained generation is needed for this test.
