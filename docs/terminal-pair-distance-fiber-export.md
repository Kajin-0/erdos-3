# Terminal-pair distance-fiber export

## Status

State-independent export theorem for distinct backward and residual terminal
pair targets of sponsor-pair transport.

Every non-direct terminal pair is converted exactly into a strictly lower-scale
four-AP-free distance fiber. Completion and maximality witnesses remain useful
optional refinements, but are not required for local pair-mass accounting.

---

## 1. Distinct terminal target sets

Let

```math
Z_B
```

be a distinct set of backward terminal pairs arising from one coordinated
deletion schedule, and let

```math
Z_Q\subseteq\binom Q2
```

be a distinct set of residual terminal pairs.

Assume the affine root set lies in a shell coordinate system of base `M`, so

```math
\operatorname{diam}(P)<M.
```

---

## 2. Backward owner-distance fibers

Every backward pair has a unique owner: the endpoint deleted first at the
terminal action. For each sponsor root `s`, define

```math
B_s^+
=
\{t-s:\{s,t\}\in Z_B,\ t>s,\ s\text{ owns }\{s,t\}\},
```

and

```math
B_s^-
=
\{s-t:\{s,t\}\in Z_B,\ t<s,\ s\text{ owns }\{s,t\}\}.
```

Each fiber is four-AP-free. For example,

```math
s+B_s^+
```

is a subset of the four-AP-free root set `P`; reflection handles `B_s^-`.

The pair-to-distance map is injective inside each owner/side fiber, and the
fibers partition `Z_B`. Therefore

```math
\boxed{
J(Z_B)
=
\sum_s
\left(
H(B_s^+)+H(B_s^-)
\right).
}
```

---

## 3. Residual left-anchor fibers

Every residual pair has a unique increasing orientation

```math
\{x,y\},
\qquad x<y.
```

For each residual root `x`, define

```math
R_x
=
\{y-x:\{x,y\}\in Z_Q,\ x<y\}.
```

Since

```math
x+R_x\subseteq Q\subseteq P,
```

`R_x` is four-AP-free.

The increasing orientation partitions the residual pair set, giving

```math
\boxed{
J(Z_Q)
=
\sum_{x\in Q}H(R_x).
}
```

No residual pair multiplicity remains.

---

## 4. Strict scale descent

Every distance token in a backward or residual fiber is the difference of two
roots in `P`. Hence

```math
0<d<\operatorname{diam}(P)<M.
```

After standard dyadic resolution, every nonempty distance-fiber shell has base
at most

```math
\boxed{M/2.}
```

All shells remain four-AP-free.

---

## 5. Completion witness metadata

The distance export does not discard arithmetic obstruction information.
Every backward pair retains:

```text
owner sponsor;
selected action and step;
forward/backward inequality;
reflection completion integer;
ambient external-root or genuine-hole status.
```

Every residual pair retains its chosen right or left completion integer.

These fields may be attached to the fiber token as metadata. They are not
needed to prove the exact harmonic identity, but they may supply terminal
release or bounded-reuse refinements later.

---

## 6. Consequence for terminal-basin transport

Apply terminal-basin overflow transfer to a distinct activated pair set `E`.
It produces:

```text
distinct direct targets Z_D;
distinct backward targets Z_B;
distinct residual targets Z_Q;
owner-distance overflow fibers F_over.
```

Export `Z_B` and `Z_Q` by the present theorem. Then

```math
\boxed{
J(E)
\le
J(Z_D)
+
H(\mathcal F_{\rm over})
+
H(\mathcal F_B)
+
H(\mathcal F_Q).
}
```

Every recursive fiber descends by at least one dyadic level. Every direct
target is a distinct sponsor edge.

---

## 7. Complete pair transport normal form

The pair-transport layer now has the normal form

```text
distinct activated physical pairs
-> distinct direct sponsor-edge release
   + lower-scale four-AP-free distance fibers.
```

There is:

```text
no transport-target multiplicity term;
no scalar backward-pair term;
no scalar residual-pair term;
no need to prepay the full latent pair energy.
```

Backward/residual completion theorems remain optional strengthening tools for
classifying or terminating particular fibers.
