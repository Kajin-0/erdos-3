# Bellman potential for exact equal-translate tails

## Status

Elementary algebraic theorem. This note packages the summable exact-tail calculation as a dynamic-programming identity suitable for a future continuation-tree argument.

---

## 1. Constant-scale exact continuation

Suppose a replay state has:

```math
N=|S|,
\qquad
P=\text{certified replay multiplicity},
\qquad
L=\text{dyadic shell scale}.
```

Its current weighted density is

```math
W(N,P,L)=\frac{PN}{L}.
```

Under one exact disjoint three-translate replication step with constant scale factor `c`,

```math
N'=3(N+1),
\qquad
P'=2P,
\qquad
L'=cL.
```

Assume

```math
c>6,
```

so the asymptotic multiplicity-weighted growth factor `6/c` is subcritical.

---

## 2. Exact future-cost function

Define

```math
\boxed{
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(
N+\frac{6}{c-2}
\right).
}
```

Then

```math
\boxed{
\mathfrak B_c(N,P,L)
=
W(N,P,L)
+
\mathfrak B_c(N',P',L').
}
```

### Verification

The child charge is

```math
\mathfrak B_c(N',P',L')
=
\frac{2P}{(c-6)L}
\left(
3(N+1)+\frac{6}{c-2}
\right).
```

Adding the current charge `PN/L` and simplifying gives

```math
\frac{PN}{L}
+
\frac{2P}{(c-6)L}
\left(
3N+3+\frac{6}{c-2}
\right)
=
\frac{cP}{(c-6)L}
\left(
N+\frac{6}{c-2}
\right).
```

Thus `B_c` is exactly the total weighted density of the infinite constant-`c` exact tail, including its entry state.

---

## 3. Uniqueness among affine potentials

Consider an affine scale-normalized candidate

```math
F(N,P,L)
=
\frac{P}{L}(aN+b).
```

The Bellman equation

```math
F(N,P,L)
=
\frac{PN}{L}
+
F(3(N+1),2P,cL)
```

forces

```math
a=1+\frac{6a}{c},
```

```math
b=\frac{6a+2b}{c}.
```

Therefore

```math
a=\frac{c}{c-6},
\qquad
b=\frac{6c}{(c-6)(c-2)}.
```

Hence `B_c` is the unique affine potential satisfying the exact continuation identity.

---

## 4. Factor-eight basin

For the sharp exact dyadic scale factor

```math
c=8,
```

one obtains

```math
\boxed{
\mathfrak B_8(N,P,L)
=
\frac{4P(N+1)}{L}.
}
```

If `S'` is the scheduled factor-eight child, then

```math
\boxed{
\mathfrak B_8(S,L,P)
=
W(S,L,P)
+
\mathfrak B_8(S',8L,2P).
}
```

For the recorded `S_10`,

```math
\mathfrak B_8(S_{10},L_{10},P_{10})
=
\frac{33215}{16384}.
```

---

## 5. Continuation-tree interpretation

A state carrying an exact-tail basin certificate can be treated as an absorbing node with terminal value `B_8`. The infinite scheduled descendant path need not be expanded explicitly.

This suggests a Bellman or supermartingale strategy for the whole continuation tree:

1. assign exact basin nodes their terminal charge;
2. prove a suitable parent potential dominates current weight plus the aggregate potential of non-basin children;
3. conclude summability by iterating the inequality over the tree.

The unresolved step is constructing such a dominating potential for contaminated states and for branching among multiple possible continuations.
