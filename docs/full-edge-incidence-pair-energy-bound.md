# Full-edge incidence bound by physical pair energy

## Status

Historical coefficient-two incidence theorem, retained for its elementary local-multiplicity proof.

The bound

```math
\frac52\mathcal L_3(P)\le2J(P)
```

is valid but superseded by the stronger state-independent theorem

```math
\boxed{
\frac52\mathcal L_3(P)\le\frac54J(P).
}
```

Primary current reference:

```text
docs/five-quarter-full-edge-incidence-bound.md
```

---

## 1. Physical pair energy

For a finite four-AP-free set `P`, define

```math
J(P)
=
\sum_{x<y\atop x,y\in P}
\frac1{y-x}.
```

For a physical pair

```math
e=\{x,y\},
\qquad D=y-x,
```

let `m_3(e)` be the number of three-term progressions in `P` containing `e` as an edge.

---

## 2. Pair incidence is at most two

The possible completion roots are:

```text
x-D;
y+D;
x+D/2, when D is even.
```

The two adjacent endpoint completions cannot both lie in `P`, because

```math
x-D,\ x,\ y,\ y+D
```

would form a four-term progression.

Therefore one pair belongs to:

```text
at most one adjacent-edge three-AP;
at most one midpoint/outer-edge three-AP.
```

Hence

```math
\boxed{m_3(e)\le2.}
```

---

## 3. Exact full-edge incidence identity

For one three-AP

```math
\{a,a+d,a+2d\},
```

the three physical edge weights sum to

```math
\frac1d+\frac1d+\frac1{2d}
=
\frac5{2d}.
```

Thus

```math
\boxed{
\frac52\mathcal L_3(P)
=
\sum_{e\in\binom P2}
\frac{m_3(e)}{D(e)}.
}
```

---

## 4. Historical coefficient-two bound

Using only `m_3(e)<=2`,

```math
\begin{aligned}
\frac52\mathcal L_3(P)
&=
\sum_e\frac{m_3(e)}{D(e)}\\
&\le
2\sum_e\frac1{D(e)}\\
&=
2J(P).
\end{aligned}
```

Therefore

```math
\boxed{
\frac52\mathcal L_3(P)\le2J(P).
}
```

This remains a valid immediate corollary of the pair-incidence multiplicity theorem.

---

## 5. Why the coefficient is superseded

The coefficient-two proof treats every multiplicity-two pair independently. Four-AP-freeness imposes additional compatibility among those duplicated pairs.

A duplicated pair must be one adjacent edge and one outer edge. Mapping each duplicated outer pair to its two adjacent half pairs is globally injective. The two half pairs have four times the duplicated pair's energy, so duplicated incidence energy is at most one quarter of `J(P)`.

This yields

```math
\frac52\mathcal L_3(P)
\le
J(P)+\frac14J(P)
=
\frac54J(P).
```

See:

```text
docs/five-quarter-full-edge-incidence-bound.md
src/verify_full_edge_incidence_five_quarter_bound.py
```

---

## 6. Bellman consequence

The historical coefficient two required pair coefficient `lambda>=2` to pay complete future production. Combined with two half-scale latent owners, that forced the simple monomial owner exponent to satisfy `p>=2`.

The improved coefficient `5/4` lowers the certified monomial requirement to

```math
\lambda=\frac54,
\qquad
p\ge\log_2\!\left(\frac52\right).
```

Thus the coefficient-two threshold should no longer be used in the active proof program.

---

## 7. Validation

Historical verifier:

```text
src/verify_full_edge_incidence_pair_energy_bound.py
```

Current stronger verifier:

```text
src/verify_full_edge_incidence_five_quarter_bound.py
```
