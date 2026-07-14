# Terminal-pair arithmetic-progression witness bound

## Status

State-independent symbolic refinement of sponsor-pair forward transport.

For a set of activated pair tokens, forward transport reduces the payment problem to distinct terminal pair targets plus transport-collision reuse. This note proves that every terminal target possessing an in-parent arithmetic completion is paid by the parent's weighted three-AP load with universal coefficient `5/2`.

Targets whose specified completion lies outside the parent must be split into:

1. external ambient completions lying in the counterexample but outside the current parent lineage;
2. genuine ambient holes, to which maximal four-AP-free saturation applies.

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
\frac1d
+
\frac1d
+
\frac1{2d}
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
s,
\qquad
m=s+\epsilon q,
\qquad
o=s+2\epsilon q.
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
\qquad
x,y\in Q.
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

## 3. Completed and parent-external targets

Call a direct target completed automatically. Call a backward or residual target completed when the completion specified above belongs to `P`.

Let

```math
Z_{\rm comp}(A)
```

be the set of distinct completed terminal targets and let

```math
Z_{\rm out}(A)
```

be the remaining distinct targets, whose specified completion lies outside `P`.

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
M_{\rm out}(A)
+
R_{\rm trans}(A),
}
```

where

```math
M_{\rm out}(A)
=
\sum_{z\in Z_{\rm out}(A)}w(z).
```

Thus full activated pair energy has been reduced to:

```text
weighted parent three-AP load
+ pair-labeled parent-external completion mass
+ transport-collision reuse.
```

---

## 5. Ambient-set decomposition

Let `B` be the ambient four-AP-free counterexample and suppose `P\subseteq B` is the current parent root set.

For each target in `Z_out(A)`, let `c(z)` be its specified reflection or right completion. Split

```math
Z_{\rm ext}(A)
=
\{z\in Z_{\rm out}(A):c(z)\in B\setminus P\},
```

and

```math
Z_{\rm hole}(A)
=
\{z\in Z_{\rm out}(A):c(z)\notin B\}.
```

Correspondingly,

```math
M_{\rm out}(A)
=
M_{\rm ext}(A)
+
M_{\rm hole}(A).
```

The two terms require different payment mechanisms.

### External ambient completions

```math
M_{\rm ext}(A)
=
\sum_{z\in Z_{\rm ext}(A)}w(z)
```

is an external-root or omitted-lineage term. Its completion exists in the counterexample, but not in the current parent. It must be exported through provenance, completion support, or rectangle transport.

### Genuine ambient holes

```math
M_{\rm hole}(A)
=
\sum_{z\in Z_{\rm hole}(A)}w(z)
```

contains genuine missing integers. After enlarging the ambient set to an inclusion-maximal four-AP-free set, every such completion integer carries a four-AP witness with three ambient-set points.

Different pair targets may request the same external root or missing integer, so neither maximality nor ambient membership alone removes multiplicity. The ledger must retain:

```text
terminal pair target
specified completion integer
ambient status: external or hole
chosen provenance or four-AP witness
```

The corrected activation inequality is therefore

```math
\boxed{
\sum_{e\in A}w(e)
\le
\frac52\mathcal L_3(P)
+
M_{\rm ext}(A)
+
M_{\rm hole}(A)
+
R_{\rm trans}(A).
}
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

A complete proof now requires three bounds:

1. **external completion reuse**

   ```math
   M_{\rm ext}(A);
   ```

2. **genuine-hole witness reuse**

   ```math
   M_{\rm hole}(A);
   ```

3. **transport-target collision reuse**

   ```math
   R_{\rm trans}(A).
   ```

The cross residual-minimum star subfamily is sharper: its parent-completion map is injective, and its backward mass satisfies the dedicated completion-charge theorem. Its parent-external term must still be split into ambient external roots and genuine holes.

The next exact probe should report, on the certified fourth-to-fifth refined frontier:

- completed versus parent-external terminal-target mass;
- external ambient completions versus genuine holes;
- three-AP witness edge occupancy;
- multiplicity of each completion integer;
- transport-collision mass;
- residual-minimum stars versus internal sponsor pairs.

No sixth retained generation is required.
