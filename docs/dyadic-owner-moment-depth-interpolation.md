# Dyadic owner-moment and excess-depth interpolation

## Status

State-independent algebraic bridge from a supercritical owner-scale moment to raw occurrence mass, with one explicit excess-depth coordinate.

For every owner exponent `p>0`, raw mass at a dyadically lower child scale is bounded by:

```text
one normalized p-moment term;
one excess-depth term beyond the mandatory first scale drop.
```

At the five-quarter threshold

```math
p_0=\log_2\!\left(\frac52\right),
```

the exact coefficients are `5/2` and `3/5`.

---

## 1. One dyadic descendant

Fix a parent owner scale `N` and a child standard dyadic shell base

```math
L=\frac{N}{2^s},
\qquad
s\in\mathbb Z_{\ge1}.
```

Let one source-owned occurrence carry raw mass

```math
m\ge0.
```

Define its normalized owner-exponent mass

```math
m_p
=
m\left(\frac LN\right)^p
=
m\,2^{-ps},
```

and its excess depth beyond the mandatory first level

```math
\delta_+(m)
=
m(s-1).
```

---

## 2. General interpolation inequality

Put

```math
q=2^{-p}\in(0,1).
```

Then

```math
2^p\left(\frac LN\right)^p
=
q^{s-1}.
```

For every integer

```math
n=s-1\ge0,
```

the geometric-sum identity gives

```math
1-q^n
=
(1-q)(1+q+\cdots+q^{n-1})
\le
n(1-q).
```

Therefore

```math
1
\le
q^n+n(1-q).
```

Substituting `n=s-1` yields

```math
\boxed{
1
\le
2^p\left(\frac LN\right)^p
+
\left(1-2^{-p}\right)(s-1).
}
```

Multiplying by the raw occurrence mass gives

```math
\boxed{
m
\le
2^p m\left(\frac LN\right)^p
+
\left(1-2^{-p}\right)m(s-1).
}
```

Equality holds for `s=1` and `s=2`. For `s>=3`, the inequality is strict unless `m=0`.

---

## 3. Finite occurrence family

Let `mu` be a finite source-owned occurrence family whose child scales are

```math
L_e=\frac N{2^{s_e}},
\qquad s_e\ge1.
```

Define raw mass

```math
W(\mu)=\sum_e\mu(e),
```

normalized owner-exponent moment

```math
M_p(\mu;N)
=
\sum_e
\mu(e)
\left(\frac{L_e}{N}\right)^p,
```

and excess-depth mass

```math
\Delta_+(\mu;N)
=
\sum_e\mu(e)(s_e-1).
```

Summing the one-occurrence inequality gives

```math
\boxed{
W(\mu)
\le
2^p M_p(\mu;N)
+
\left(1-2^{-p}\right)
\Delta_+(\mu;N).
}
```

Equivalently, in unnormalized owner units,

```math
\boxed{
N^pW(\mu)
\le
2^p\sum_e\mu(e)L_e^p
+
\left(1-2^{-p}\right)N^p\Delta_+(\mu;N).
}
```

---

## 4. Five-quarter threshold specialization

Let

```math
p_0=\log_2\!\left(\frac52\right).
```

Then

```math
2^{p_0}=\frac52
```

and

```math
1-2^{-p_0}
=
1-\frac25
=
\frac35.
```

Therefore

```math
\boxed{
W(\mu)
\le
\frac52M_{p_0}(\mu;N)
+
\frac35\Delta_+(\mu;N).
}
```

At a half-scale child (`s=1`), the moment term alone equals the raw mass.

At a quarter-scale child (`s=2`), the moment term pays `2/5` of the raw mass and one excess-depth unit pays the remaining `3/5`.

For every deeper child, the same two coordinates have positive slack.

---

## 5. Exact first-appearance consistency

The established virtual first-appearance majorant has:

```text
three full-mass quarter-scale slots;
one half-mass half-scale slot.
```

Per unit source pair mass, its raw output mass is

```math
3+\frac12=\frac72.
```

At `p=p_0`, its normalized moment is

```math
3\,4^{-p_0}
+
\frac12\,2^{-p_0}
=
\frac{12}{25}
+
\frac15
=
\frac{17}{25}.
```

Its excess-depth mass is

```math
3(2-1)+\frac12(1-1)=3.
```

The interpolation row is exact:

```math
\frac52\cdot\frac{17}{25}
+
\frac35\cdot3
=
\frac{17}{10}
+
\frac{18}{10}
=
\boxed{\frac72}.
```

Thus the coefficients `5/2` and `3/5` reconstruct the complete raw virtual first-appearance load with no loss.

---

## 6. Interpretation

The five-quarter owner-exponent Bellman row controls the normalized `p_0` moment. The present lemma shows exactly what additional information is required to recover raw occurrence mass:

```text
excess dyadic depth beyond the first mandatory child level.
```

No arbitrary interpolation coefficient is needed. The boundary cases `s=1` and `s=2` determine the sharp coefficients.

The lemma does not itself bound the total excess-depth ledger across a branching tree. It converts the remaining global problem into the explicit target

```math
\boxed{
\text{control }\Delta_+
\text{ with production-owned depth release.}
}
```

---

## 7. Remaining interface

A complete treewise proof must combine:

1. the collision-free `p_0` owner-moment Bellman row;
2. the exact interpolation inequality above;
3. a source-owned bound for accumulated excess depth;
4. terminal and recreation occurrence accounting;
5. the free edge-token ledger;
6. the final raw dyadic reciprocal-density comparison.

The supercritical-to-raw bridge is therefore no longer qualitative. Its missing coordinate is the explicit excess-depth mass `Delta_+`.
