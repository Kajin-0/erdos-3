# Terminal-pair arithmetic-progression witness bound

## Status

State-independent symbolic refinement of sponsor-pair forward transport.

For a set of activated pair tokens, forward transport reduces the payment problem to distinct terminal pair targets plus transport-collision reuse. This note proves that every terminal target possessing an in-parent arithmetic completion is paid by the parent's weighted three-AP load with universal coefficient `5/2`.

The only remaining target mass consists of pair-labeled missing completions.

---

## 1. Weighted three-AP load

For a finite root set `P`, define

```math
\mathcal L_3(P)
=
\sum_{x,d:\ x,x+d,x+2d\in P}
\frac1d.
```

Every three-term progression of step `d` has three unordered pair edges:

```math
\{x,x+d\},
\qquad
\{x+d,x+2d\},
\qquad
\{x,x+2d\}.
```

Their total pair weight is

```math
\frac1d+rac1d+rac1{2d}
=
\frac5{2d}.
```

Hence the total edge weight of all root three-APs, with each distinct pair edge counted at most once per progression, is

```math
\frac52\mathcal L_3(P).
```

---

## 2. Terminal targets from forward transport

Let `A` be a finite set of activated sponsor-core pair tokens in one affine parent. Apply sponsor-pair forward transport to each token.

Let

```math
T(e)
```

be the terminal target of `e`, and let

```math
Z(A)=\{T(e):e\in A\}
```

be the distinct target set.

The terminal targets have three types.

### Direct targets

A direct target is one of the two sponsor edges of a selected action

```math
s,\ m=s+\epsilon q,\ o=s+2\epsilon q.
```

It is therefore an edge of the three-AP `{s,m,o}`.

### Backward targets

A backward target has an owned orientation `(s,t)`, where `s` is the first-deleted endpoint. Define its reflection completion

```math
c=2s-t.
```

If `c\in P`, then

```math
t,\ s,\ c
```

is a three-AP, and the target pair `{s,t}` is one of its adjacent edges.

### Residual targets

A residual target has endpoints

```math
x<y,
\qquad x,y\in Q.
```

Define the right completion

```math
c=2y-x.
```

If `c\in P`, then `c\notin Q` because `Q` is three-AP-free, and

```math
x,\ y,\ c
```

is a parent-root three-AP. The residual target is its first adjacent edge.

---

## 3. Completed and missing targets

Call a direct target completed automatically. Call a backward or residual target completed when the completion specified above belongs to `P`.

Let

```math
Z_{\rm comp}(A)
```

be the set of distinct completed terminal targets and let

```math
Z_{\rm miss}(A)
```

be the remaining distinct targets.

Assign every completed target to one containing three-AP as follows:

1. direct target: its selected action;
2. backward target: its reflection triple;
3. residual target: its right-completion triple.

Each target pair is assigned exactly once.

For any fixed three-AP of step `d`, the assigned targets can use at most its three distinct pair edges. Therefore their total weight is at most

```math
\frac5{2d}.
```

Summing over all root three-APs gives

```math
\boxed{
\sum_{z\in Z_{\rm comp}(A)}w(z)
\le
\frac52\mathcal L_3(P).
}
```

No injectivity from targets to progressions is required; the three-edge capacity of each progression handles all collisions at the witness level.

---

## 4. Activation-transfer inequality

Let

```math
\mu_A(z)=|\{e\in A:T(e)=z\}|
```

and define transport-collision reuse

```math
R_{\rm trans}(A)
=
\sum_z(\mu_A(z)-1)_+w(z).
```

Forward-transport monotonicity gives

```math
\sum_{e\in A}w(e)
\le
\sum_z\mu_A(z)w(z).
```

Separating distinct target capacity from reuse and applying the completed-target bound yields

```math
\boxed{
\sum_{e\in A}w(e)
\le
\frac52\mathcal L_3(P)
+
M_{\rm pair}(A)
+
R_{\rm trans}(A),
}
```

where

```math
M_{\rm pair}(A)
=
\sum_{z\in Z_{\rm miss}(A)}w(z).
```

Thus full activated pair energy has been reduced to:

```text
weighted parent three-AP load
+ pair-labeled missing-completion mass
+ transport-collision reuse.
```

---

## 5. Maximal four-AP-free interpretation

Assume the ambient counterexample has been enlarged to an inclusion-maximal four-AP-free set.

Every missing completion integer attached to a target in `Z_miss(A)` then has a four-AP witness with three ambient-set points. Hence `M_pair(A)` is not unsupported absence; it is a weighted family of pair-labeled four-AP obstruction witnesses.

Different pair targets may request the same missing completion integer, so maximality alone does not remove multiplicity. The missing-completion ledger must retain both:

```text
terminal pair target
missing completion integer
chosen four-AP witness.
```

---

## 6. Relation to coordinated valuation compression

The established coordinated role theorem produces retained side/middle three-AP incidence of total weight at least

```math
\frac43\mathcal L_3(P).
```

The present theorem uses `\mathcal L_3(P)` in the opposite direction: it upper-bounds completed terminal pair capacity.

This does not yet close a Bellman inequality, because weighted three-AP incidence may recur across descendants. It does, however, replace arbitrary latent pair activation by a lower-dimensional incidence object already equipped with:

1. fixed-step disjointness;
2. parity and `v_2-v_3` role compression;
3. root-forced progression subledgers;
4. explicit middle-fiber output.

---

## 7. Remaining obligations

A complete proof now requires two bounds:

1. **missing-completion witness reuse**

   ```math
   M_{\rm pair}(A);
   ```

2. **transport-target collision reuse**

   ```math
   R_{\rm trans}(A).
   ```

The cross residual-minimum star subfamily is already sharper: its missing completion map is injective, and its backward mass satisfies the dedicated completion-charge theorem.

The next exact probe should therefore report, on the certified fourth-to-fifth refined frontier:

- completed versus missing terminal-target mass;
- three-AP witness edge occupancy;
- multiplicity of each missing completion integer;
- transport-collision mass;
- separation of residual-minimum stars from internal sponsor pairs.

No sixth retained generation is required.
