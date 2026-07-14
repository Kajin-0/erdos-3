# Base-six three-AP-rich no-go theorem

## Status

Explicit symbolic obstruction to any sublinear-in-scale upper bound of weighted
three-AP load by parent harmonic mass inside four-AP-free dyadic blocks.

The construction shows that the entering scale-critical three-AP potential can
be linearly larger in ambient scale than the harmonic mass it is meant to
control. Collision and first-appearance structure are indispensable.

---

## 1. Digit family

For `n>=1`, define

```math
A_n
=
\left\{
\sum_{j=0}^{n-1}a_j6^j:
 a_j\in\{0,1,2\}
\right\}.
```

Then

```math
|A_n|=3^n
```

and

```math
\max A_n
=
2\sum_{j=0}^{n-1}6^j
=
\frac{2(6^n-1)}5
<
\frac25 6^n.
```

---

## 2. Four-AP-freeness

Suppose

```math
x_0,x_1,x_2,x_3\in A_n
```

form a four-term arithmetic progression. The two identities are

```math
x_0+x_2=2x_1,
\qquad
x_1+x_3=2x_2.
```

Every base-six digit on either side of either equation lies between `0` and
`4`. Hence no carry occurs. Both identities hold coordinatewise in the digit
set `{0,1,2}`.

A four-term arithmetic progression entirely contained in `{0,1,2}` has common
difference zero. Thus all four digits agree in every coordinate, and

```math
x_0=x_1=x_2=x_3.
```

Therefore

```math
\boxed{A_n\text{ is four-AP-free}.}
```

---

## 3. Explicit three-AP families

Choose a nonempty coordinate set

```math
S\subseteq\{0,\ldots,n-1\}.
```

On every coordinate in `S`, use the digit progression

```text
0,1,2.
```

On every coordinate outside `S`, choose one constant digit from `{0,1,2}`.
This produces an increasing three-term progression in `A_n` with step

```math
d_S
=
\sum_{j\in S}6^j.
```

For fixed `S`, there are

```math
3^{n-|S|}
```

choices of the constant digits. Hence this explicit subfamily contains

```math
\sum_{\varnothing\ne S\subseteq[n]}
3^{n-|S|}
=
4^n-3^n
```

three-term progressions.

Every step satisfies

```math
d_S<\frac{6^n}{5},
```

so the weighted load obeys the general lower bound

```math
\mathcal L_3(A_n)
>
5\frac{4^n-3^n}{6^n}.
```

### Unit-step subfamily

The much stronger obstruction comes from the single choice

```math
S=\{0\}.
```

The least-significant digit runs through `0,1,2`, while the other `n-1`
digits are arbitrary. This gives exactly

```math
3^{n-1}
```

pairwise-disjoint three-APs of step `1`. Therefore

```math
\boxed{
\mathcal L_3(A_n)
\ge
3^{n-1}.
}
```

The remaining digit-coordinate progressions only increase the load.

---

## 4. Standard dyadic placement

Let `N_n` be the least power of two satisfying

```math
N_n\ge6^n
```

and put

```math
B_n=N_n+A_n.
```

Since `max A_n<2N_n/5`,

```math
B_n\subseteq[N_n,2N_n).
```

Translation preserves arithmetic progressions and all progression steps, so
`B_n` is four-AP-free and

```math
\mathcal L_3(B_n)=\mathcal L_3(A_n).
```

Its harmonic mass satisfies

```math
H(B_n)
\le
\frac{|A_n|}{N_n}
=
\frac{3^n}{N_n}.
```

Using only the unit-step subfamily gives

```math
\boxed{
\frac{\mathcal L_3(B_n)}{H(B_n)}
\ge
\frac{N_n}{3}.
}
```

Thus the load-to-harmonic ratio grows at least linearly in the ambient dyadic
scale. Since `N_n<2\cdot6^n`, this is sharp up to the distinction between
linear and linear-logarithmic crude bounds.

The earlier aggregate estimate also remains valid:

```math
\frac{\mathcal L_3(B_n)}{H(B_n)}
>
5\left[
\left(\frac43\right)^n-1
\right],
```

but it is much weaker than the unit-step bound.

---

## 5. Consequences

There is no universal constant `C` such that every four-AP-free dyadic block
satisfies

```math
\mathcal L_3(B)
\le
C H(B).
```

More strongly, there is no bound

```math
\mathcal L_3(B)
\le
o(N)H(B)
```

valid for all four-AP-free `B\subseteq[N,2N)`.

The following routes are invalid:

```text
control full-edge recursion by proving weighted 3-AP load is comparable to
parent harmonic mass;

treat a large weighted 3-AP load as evidence that a 4-AP is near;

use the critical scale-weighted AP row without collision or first-appearance
structure;

expect an entering AP-load coefficient smaller than linear ambient scale.
```

The base-six family is summable as an infinite digit construction, so it is an
obstruction to a proof method rather than a counterexample to Erdős Problem
#3. Its unit-step triples are massively repeated across high-digit reference
configurations. This is precisely the collision-fiber phenomenon that the
reference-gap and rectangle-aspect ledgers are designed to resolve.

---

## 6. Literature context

The broader phenomenon that four-AP-free sets can remain extremely rich in
three-APs is consistent with the constructions of Cosmin Pohoata and Oliver
Roche-Newton, *Four-term progression free sets with three-term progressions in
all large subsets*, arXiv:1905.08457.

The present theorem is a simpler explicit weighted no-go tailored to the
scale-critical recursion in this repository.
