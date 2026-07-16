# Completion-step heavy terminal split

## Status

State-independent terminal/recursive partition for the heavy outputs of the
completion-step light/heavy transfer.

The theorem is elementary but essential for bookkeeping: a heavy
completion-step fiber is not automatically persistent recursive debt. After
standard dyadic resolution, every shell with no three-term progression is a
terminal sink and leaves the recursive ledger immediately.

---

## 1. Heavy completion-step output

Let

```math
S_{c,\sigma}
```

be one heavy completion-step fiber from a parent shell `[N,2N)`. It is
four-AP-free and lies below `N/2`.

Resolve it into standard dyadic shells:

```math
S_{c,\sigma}
=
\bigsqcup_M S_{c,\sigma;M},
\qquad
S_{c,\sigma;M}\subseteq[M,2M).
```

Every nonempty shell has

```math
M\le N/4.
```

The harmonic mass is exactly additive:

```math
H(S_{c,\sigma})
=
\sum_M H(S_{c,\sigma;M}).
```

---

## 2. Terminal and recursive shells

Partition the resolved shells into

```math
\mathcal T_{\rm comp}
=
\{S_{c,\sigma;M}:S_{c,\sigma;M}\text{ is three-AP-free}\}
```

and

```math
\mathcal R_{\rm comp}
=
\{S_{c,\sigma;M}:S_{c,\sigma;M}\text{ contains a three-AP}\}.
```

Then

```math
\boxed{
\sum_{S\in\mathcal H_{\rm comp}}H(S)
=
\sum_{T\in\mathcal T_{\rm comp}}H(T)
+
\sum_{R\in\mathcal R_{\rm comp}}H(R).
}
```

Only `R_comp` remains in the recursive Bellman child family. The terminal
family enters the terminal first-appearance ledger.

---

## 3. Affine terminal token

A resolved shell retains its completion reference and orientation. Its natural
terminal token is

```math
\theta(T)
=
(c,\sigma,M,T),
```

or equivalently the ordered double affine image

```math
\bigl(c+\sigma T,c+2\sigma T\bigr).
```

The double-affine lift theorem makes this representation injective within one
selected completion-step family. Numerical equality of the abstract shell `T`
alone is not a token collision.

Across the complete tree, deterministic first appearance of `theta(T)` gives a
disjoint terminal-sink union. Any later recurrence of the same affine token is
recorded as terminal recreation rather than persistent recursive mass.

---

## 4. Refined terminal-payment row

The edge-first terminal-pair light/heavy inequality becomes

```math
\boxed{
J(A)
\le
\frac52\mathcal L_3(P)
+
J(F_{\rm light})
+
\operatorname{TermSink}_{\rm comp,first}
+
\sum_{R\in\mathcal R_{\rm comp}}H(R)
+
M_{\rm amb}
+
R_{\rm src}(A)
+
\operatorname{TermRecreate}_{\rm comp}.
}
```

The two terminal terms distinguish first appearance from recreation. No
three-AP-free shell is retained as recursive debt.

---

## 5. Exact `S7` consequence

On the certified refined fourth-to-fifth terminal frontier:

```text
heavy completion fibers       = 6420
resolved heavy shell outputs  = 9944
```

Every resolved shell is three-AP-free. Therefore

```math
\boxed{
\mathcal R_{\rm comp}=\varnothing
}
```

on this finite frontier, and the complete heavy mass

```math
138.392594202054\ldots
```

enters the affine terminal-sink ledger.

This is a state-specific exact result. Arbitrary completion-step fibers need
not be three-AP-free; explicit small counterexamples exist.

---

## 6. Scope

The theorem does not prove that heavy shells are always terminal. It proves the
correct universal partition and prevents terminal mass from being propagated
as if it were recursive.

The remaining global work is:

1. prove a collision-sound bounded terminal token across generations;
2. control terminal recreation when the same affine shell returns;
3. apply recursive analysis only to the genuinely three-AP-containing heavy
   shells;
4. combine this terminal split with light-support first appearance and the
   ambient completion ledger.
