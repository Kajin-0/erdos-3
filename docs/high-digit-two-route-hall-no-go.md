# High-digit two-route Hall no-go

## Status

Symbolic infinite-family counterexample to the proposed universal two-route recursive pair reserve.

Even after combining:

```text
first-copy horizontal chains;
adjacent off-diagonal staircases,
```

one cannot pack every maximal direct-discharge recursive family. A high-digit restriction of the carry-free digit grid has `10^(m-1)` recursive states, but only `4^(m-1)` first-chain occurrences and at most `9^m` physical staircase pairs.

For `m>=15`, total recursive debt exceeds the complete physical union capacity of both routes.

---

## 1. Carry-free digit set

Let

```math
D_m
=
\left\{
\sum_{i=0}^{m-1}\varepsilon_i10^i:
\varepsilon_i\in\{0,1,2\}
\right\},
```

with

```math
m\ge15.
```

As in the digit-grid off-diagonal no-go,

```math
|D_m|=3^m
```

and `D_m` is four-AP-free.

Put

```math
Q=10^{m-1}
```

and

```math
L=\operatorname{diam}(D_m)
=
\frac{2(10^m-1)}9
<
\frac{20}{9}Q.
```

Choose the least power of two `M` satisfying

```math
M>8L.
```

Then

```math
M<16L<\frac{320}{9}Q.
```

Put

```math
\Delta=\frac{3M}{2},
```

and define the two four-AP-free physical layers

```math
X=4M+D_m,
```

```math
Y=4M+\Delta+2D_m.
```

Their union lies in `[4M,8M)` and is four-AP-free.

---

## 2. High-digit steps only

For every subset

```math
R\subseteq\{0,\ldots,m-2\},
```

define

```math
S_R=R\cup\{m-1\}
```

and

```math
q_R
=
\sum_{i\in S_R}10^i.
```

Every selected step satisfies

```math
q_R\ge Q.
```

The number of valid three-AP starts in `D_m` at this step is

```math
A_R=3^{m-1-|R|}.
```

Pair every first-copy start `x` with every second-copy start `y` of the same step. The number of recursive embedded states is

```math
\sum_R A_R^2
=
\sum_{r=0}^{m-1}\binom{m-1}{r}9^{m-1-r}
=
10^{m-1}.
```

As before, every state is

```math
T_{x,y,R}
=
\Delta+2y-x+\{0,q_R,2q_R\}
\subseteq[M,2M).
```

Protected maximal extension forces all selected completion fibers to remain heavy and recursive.

---

## 3. Recursive debt

Each state has three points below `2M`. Therefore

```math
H(T_{x,y,R})
>
\frac3{2M}.
```

The total debt satisfies

```math
\boxed{
D_m^{\rm high}
>
\frac{3\cdot10^{m-1}}{2M}.
}
```

---

## 4. First-route horizontal-chain capacity

One first-copy three-AP contributes exactly two horizontal-chain pairs, both of gap `q_R`.

The number of first-copy three-AP occurrences over all selected steps is

```math
\sum_R A_R
=
\sum_{r=0}^{m-1}\binom{m-1}{r}3^{m-1-r}
=
4^{m-1}.
```

Counting occurrences gives an upper bound for the physical union capacity. Since every selected step is at least `Q`,

```math
\boxed{
J(R_{1,\rm union})
\le
\frac{2\cdot4^{m-1}}{Q}.
}
```

Using `M/Q<320/9`,

```math
M J(R_{1,\rm union})
<
\frac{640}{9}4^{m-1}.
```

---

## 5. Second-route staircase capacity

Every staircase pair has one endpoint in `X` and one endpoint in `Y`. Thus the complete physical staircase union contains at most

```math
|X||Y|=9^m
```

pairs.

Every cross-layer gap is at least

```math
\Delta-L
>
\frac{11M}{8},
```

because `L<M/8`. Hence

```math
\boxed{
J(R_{2,\rm union})
<
\frac{8}{11M}9^m.
}
```

---

## 6. Failure of the combined Hall inequality

If the two-route Hall target were valid, then

```math
D_m^{\rm high}
\le
J(R_{1,\rm union})+J(R_{2,\rm union}).
```

Multiplying the proved estimates by `M`, this would require

```math
\frac32\,10^{m-1}
<
\frac{640}{9}4^{m-1}
+
\frac8{11}9^m.
```

Divide by `10^(m-1)`. The right side becomes

```math
\frac{640}{9}\left(\frac25\right)^{m-1}
+
\frac{72}{11}\left(\frac9{10}\right)^{m-1}.
```

At `m=15` this is already less than `3/2`, and it decreases thereafter. Therefore

```math
\boxed{
D_m^{\rm high}
>
J(R_{1,\rm union})+J(R_{2,\rm union})
\qquad(m\ge15).
}
```

The proposed universal two-route Hall theorem is false.

---

## 7. Resources omitted by the no-go

The construction does not bound or remove:

1. all internal pair energy of the complete digit layers, including short pairs unrelated to the selected high-step chains;
2. off-diagonal cross pairs outside the canonical staircase;
3. parent full-edge production-token ownership;
4. maximality witness gadgets;
5. the matched activated-pair lineage tokens themselves;
6. higher-order digit/grid incidence potential.

A stronger theorem may combine these resources. The no-go proves that the two canonical sparse routes alone are insufficient.

---

## 8. Strategic consequence

The sequence of failed universal targets is now:

```text
one projected copy;
two projected copies;
off-diagonal cross pairs alone;
first-chain plus staircase two-route union.
```

Each target is locally sufficient for one state and succeeds on the exact `S7` frontier, but dense affine incidence defeats its physical union globally.

The next admissible potential must retain either:

```text
complete pair energy of the physical parent;
production ownership of pair occurrences;
matched lineage tokens with a scale recurrence;
maximality-witness output;
or a higher-order incidence coordinate.
```

Another finite-choice physical pair projection without such ownership should not be pursued.