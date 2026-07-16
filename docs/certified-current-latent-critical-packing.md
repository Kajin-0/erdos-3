# Certified current-latent critical-scale packing

## Status

Exact finite theorem for the four recorded point-disjoint retained transitions through the split fifth frontier.

Every repeated current-latent parent resource has a terminal current owner and one recursive latent owner. Their combined critical child load fits inside the single parent pair critical unit. Consequently the recorded chain has no recursive current-overlap correction.

This is not yet a state-independent theorem for every coordinated-deletion retained quotient.

---

## 1. Critical resource load

Let one repeated physical parent resource be

```math
f=\{x,y\},
\qquad g=y-x,
```

inside a parent state with standard dyadic shell base `N`.

Suppose `f` has:

```text
one current owner in a child shell of base L_cur;
one recursive latent owner in a child shell of base L_lat.
```

The current occurrence contributes

```math
\frac{L_{\rm cur}}g
```

to critical child harmonic mass. The latent occurrence contributes

```math
\frac{2L_{\rm lat}}g
```

to the doubled critical pair potential. Their complete critical load is therefore

```math
\frac{L_{\rm cur}+2L_{\rm lat}}g.
```

The parent pair critical unit is

```math
\frac Ng.
```

Thus one parent unit pays both owners whenever

```math
L_{\rm cur}+2L_{\rm lat}\le N.
```

---

## 2. Exact certified profile

The executable reconstructs the actual retained state objects, resolves the parent and child standard dyadic shell bases, and checks every current-latent repeated resource.

```text
transition             resources   current terminal   current recursive   maximum ratio
historical F1 -> F2        9              9                   0              17/64
R2 -> F3                   8              8                   0              33/64
R3 -> F4                  13             13                   0               5/16
R4 -> F5 split             3              3                   0               5/16
------------------------------------------------------------------------------------------------
total                     33             33                   0              33/64
```

Here `maximum ratio` means

```math
\max_f
\frac{L_{\rm cur}(f)+2L_{\rm lat}(f)}{N(f)}.
```

The exact maximum is

```math
\boxed{\frac{33}{64}}.
```

No tested resource reaches the critical boundary.

---

## 3. Maximizing configuration

The maximum occurs on the historical `R2 -> F3` transition. The repeated resources have gaps

```text
147, 152, 153.
```

For each one:

```text
parent shell base       N      = 8192
terminal current base   L_cur  = 128
recursive latent base   L_lat  = 2048
```

Therefore

```math
\frac{L_{\rm cur}+2L_{\rm lat}}N
=
\frac{128+4096}{8192}
=
\boxed{\frac{33}{64}}.
```

On the split fifth frontier the corresponding ratio is

```math
\frac{128+2(256)}{2048}
=
\frac5{16}.
```

---

## 4. Structural identities checked

For every repeated current-latent resource of gap `g`, the executable also verifies:

```math
L_{\rm cur}\le g
```

because the current child contains the numerical label `g`, and

```math
g<L_{\rm lat}
```

because two points inside one standard shell of base `L_lat` have difference strictly below `L_lat`.

These identities are state-independent. The stronger combined inequality is currently certified only on the recorded transitions.

---

## 5. Bellman consequence for the recorded chain

All 33 current owners are terminal. Hence none contributes to the recursive overlap queue.

For each repeated resource, the parent critical pair unit simultaneously pays:

```text
one terminal current harmonic occurrence;
one recursive latent pair occurrence.
```

Thus on the recorded chain:

```math
\boxed{\mathcal R_{\rm current-latent}^{\rm recursive}=0.}
```

The terminal current value remains on the terminal side of the Bellman inequality; it is not discarded. The point is that it requires no additional collision capacity beyond the parent pair unit already assigned to the latent occurrence.

---

## 6. Remaining universal question

The universal total-owner theorem allows a recursive current-latent profile in principle. The present exact chain does not realize one.

The next structural question is therefore:

```math
\boxed{
\text{Can a recursive current owner coexist with a recursive latent owner
under the actual retained policy?}
}
```

If impossible, current-latent overlap never creates a recursive correction. If possible, the smallest witness should be tested against

```math
L_{\rm cur}+2L_{\rm lat}\le N
```

rather than bounded by the separate coarse factor `1/2`.

Primary executable:

```text
src/probe_current_latent_critical_scale.py
```
