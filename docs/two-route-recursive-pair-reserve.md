# Two-route recursive pair reserve

## Status

State-independent local resource theorem and proposed universal packing target for recursive completion-step shells.

Every recursive state has two independently sufficient physical pair routes chosen to address complementary extremal obstructions:

```text
adjacent role:
  first-copy horizontal chain;
  off-diagonal staircase.

outer role:
  horizontal chain in the left copy;
  horizontal chain in the right copy.
```

The theorem proves singleton capacity and scale behavior. A universal two-route Hall theorem is not yet proved.

---

## 1. Recursive state

Let

```math
T=\{d_1<\cdots<d_n\}\subseteq[M,2M)
```

be recursively continuing, so `n>=3`.

Let the role-weighted debt be

```math
\operatorname{debt}(T)
=
\alpha H(T),
```

with

```math
\alpha=1
```

for adjacent roles and

```math
\alpha=1/2
```

for the outer role.

---

## 2. Adjacent role: route one

The first affine copy is

```math
X=\{c+\sigma d_i\}.
```

Its adjacent horizontal chain has gaps

```math
r_i=d_{i+1}-d_i,
```

with total span less than `M`. Therefore

```math
\boxed{
J(R_1(T))
=
\sum_{i=1}^{n-1}\frac1{r_i}
>
H(T).
}
```

Every route-one gap is strictly below `M`; this is shell-scale descent.

---

## 3. Adjacent role: route two

Write the two copies as

```math
x_i=c+\sigma d_i,
\qquad
y_i=c+2\sigma d_i.
```

The canonical off-diagonal staircase consists of

```math
\{x_{i+1},y_i\},
\qquad1\le i<n,
```

and

```math
\{x_1,y_2\}.
```

After reflection if necessary, its gaps are

```math
2d_i-d_{i+1}
<d_i
```

for `i<n`, and

```math
2d_2-d_1
<d_n
```

for the final pair. Consequently

```math
\boxed{
J(R_2(T))>H(T).
}
```

Every route-two pair has gap pointwise smaller than the harmonic term assigned to it. The dyadic gap shell may remain the same, but the integer gap strictly decreases.

---

## 4. Outer role: two internal routes

The outer copies are

```math
X=\{c-d_i\}
```

and

```math
Y=\{c+d_i\}.
```

Both are unscaled copies of `T`. Their horizontal chains have the same adjacent gaps `r_i`, and each satisfies

```math
J(R_j(T))
>
H(T)
>
\frac12H(T)
=
\operatorname{debt}(T),
\qquad j\in\{1,2\}.
```

Both routes have shell-scale gap descent.

---

## 5. Singleton Hall inequalities

For every recursive embedded state `s`, define its two physical pair neighborhoods

```math
R_1(s),
\qquad
R_2(s)
```

as above. Then

```math
\boxed{
J(R_1(s))>\operatorname{debt}(s)
}
```

and

```math
\boxed{
J(R_2(s))>\operatorname{debt}(s).
}
```

The two routes are not treated as two copies of spendable capacity. They are alternative neighborhoods in a capacitated assignment problem.

---

## 6. Why both routes are necessary

### Complete-bipartite translation grid

Many states share one first-copy chain. The off-diagonal staircase remains state-specific across the first-copy/second-copy incidence grid and supplies quadratic capacity.

### Carry-free digit grid

The complete off-diagonal physical grid has insufficient capacity. The digit layers contain abundant short internal horizontal pairs, so the internal-chain route supplies the missing reserve.

Thus the known extremal families defeat opposite routes.

---

## 7. Proposed universal Hall target

For every finite family `mathcal F` of recursive states emitted by direct maximal-ambient discharge, let

```math
\mathcal R(\mathcal F)
=
\bigcup_{s\in\mathcal F}
(R_1(s)\cup R_2(s)).
```

After subtracting earlier physical pair allocations, the desired theorem is a fractional assignment satisfying every state demand using capacities on its two route neighborhoods.

Equivalently, every subfamily should satisfy

```math
\boxed{
\sum_{s\in\mathcal F}\operatorname{debt}(s)
\le
J_{\rm residual}(\mathcal R(\mathcal F)).
}
```

This statement is not established. It is narrower and better motivated than the false projected-copy or off-diagonal-only Hall targets.

---

## 8. Scale-aware alternative

If the unweighted Hall inequality fails, the route structure still supplies a scale-aware transition:

```text
internal chain:
  dyadic gap shell drops;

adjacent staircase:
  individual integer gap drops;

outer second chain:
  dyadic gap shell drops.
```

A valid potential may therefore orient each state to the route that gives the better local scale decrease, while recording collisions as affine incidence tokens.

---

## 9. Exact S7 interface

The certified `S7` frontier already packs completely using only route one:

```text
278 recursive state demands;
991 first-copy chain pairs;
206 allocated lower-gap pairs;
unmet demand zero.
```

A separate exact probe should test the union of both canonical routes with entering-pair capacity treated as lower-gap Bellman child capacity, not as a new disjoint reserve.

The test is diagnostic for the recorded frontier. Universal validity remains open.