# Sponsor-star parity corollary

## Statement

Let

```math
S_r(P)=\{p-r:p\in P\},
\qquad
a=\min P,
```

and run the coordinated deletion schedule on the affine parent. Assume the minimum root survives in the final residual:

```math
a\in Q.
```

For a deleted sponsor root `s\in\Sigma`, the residual/sponsor backbone exposes the cross pair

```math
\{a,s\}.
```

Write the selected action that deletes `s` as

```math
m=s+\epsilon q,
\qquad
o=s+2\epsilon q,
```

with `\epsilon=+1` when the left endpoint is deleted and `\epsilon=-1` when the right endpoint is deleted.

Then:

```math
\boxed{
\{a,s\}
\text{ is forward-transportable }
\iff
\epsilon=-1.
}
```

Equivalently, under the repository's coordinated side rule,

```math
\boxed{
\{a,s\}
\text{ is backward }
\iff
v_2(q)\equiv0\pmod2.
}
```

Thus every cross residual-sponsor star obstruction belongs to one explicit valuation side class.

---

## Proof

Because `a` is residual, the owner of the pair `\{a,s\}` is `s`.

### Right-sponsored action

If `\epsilon=-1`, then

```math
m=s-q.
```

The middle root belongs to `P`, and `a=\min P`, so

```math
a\le m<s.
```

Hence

```math
|a-m|=m-a<s-a=|a-s|.
```

Therefore replacing `s` by `m` strictly increases pair weight:

```math
\frac1{s-a}
<
\frac1{m-a}.
```

The pair is forward-transportable.

### Left-sponsored action

If `\epsilon=+1`, then

```math
m=s+q>s\ge a.
```

Therefore

```math
|a-m|=m-a>s-a=|a-s|.
```

The pair is backward.

The coordinated side rule deletes the left endpoint exactly when `v_2(q)` is even and the right endpoint exactly when `v_2(q)` is odd. This gives the valuation formulation.

---

## Consequence for the activation program

When `a\in Q`, the only recursively available pairs involving a residual root are the sponsor-backbone star pairs `\{a,s\}`. Their transport obstruction is not arbitrary:

```text
odd v2(q):  forward transport into the surviving middle root;
even v2(q): backward star obstruction.
```

Accordingly, the cross residual-sponsor term in the pair-activation inequality can be split as

```math
\sum_{s\in\Sigma}\frac1{s-a}
=
\sum_{\substack{s\in\Sigma\\v_2(q_s)\text{ odd}}}\frac1{s-a}
+
\sum_{\substack{s\in\Sigma\\v_2(q_s)\text{ even}}}\frac1{s-a}.
```

The odd-valuation part enters the monotone forward-transport ledger. Only the even-valuation part remains as immediate backward debt.

This connects the sponsor-core program directly to the established coordinated valuation compression: the same parity coloring that assigns every selected progression to one side role also identifies exactly which residual-minimum star pairs resist forward transport.

The remaining analytical question is to bound the even-valuation star mass by retained first-role incidence, terminal first appearance, or a dyadic completion obstruction. No generation-six computation is needed.
