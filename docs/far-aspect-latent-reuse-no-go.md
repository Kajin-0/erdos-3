# Far-aspect latent-reuse no-go

## Status

Explicit infinite-family counterexample to any theorem that attempts to pay latent-latent reuse from two point-disjoint recursive affine children by one unweighted reference-pair capacity.

The latent residual remains fixed while the reference separation tends to infinity.

---

## 1. Parent family

For every integer

```math
\delta\ge6,
```

define

```math
P_\delta
=
\{1,\delta+1,\delta+2,\delta+4,\delta+6\}.
```

Translate by `-1` for the proof. The normalized set is

```math
\{0,\delta,\delta+1,\delta+3,\delta+5\}.
```

The upper cluster

```math
\{\delta,\delta+1,\delta+3,\delta+5\}
```

is a translate of

```math
\{0,1,3,5\},
```

which is four-AP-free.

Any four-AP using the isolated point `0` would have to be

```math
0,d,2d,3d
```

with all three positive points inside an interval of length `5`. This would give

```math
2d=3d-d\le5,
```

while

```math
d\ge\delta\ge6,
```

a contradiction.

Therefore

```math
\boxed{P_\delta\text{ is four-AP-free for every }\delta\ge6.}
```

---

## 2. Two point-disjoint recursive children

Choose references

```math
r_1=1,
\qquad
r_2=\delta+1,
```

and common recursive root set

```math
Q_\delta
=
\{\delta+2,\delta+4,\delta+6\}.
```

The two right-oriented affine children are

```math
S_1
=Q_\delta-r_1
=
\{\delta+1,\delta+3,\delta+5\},
```

and

```math
S_2
=Q_\delta-r_2
=
\{1,3,5\}.
```

Both are three-term arithmetic progressions of step `2`, hence recursively continuing.

Since `delta>=6`,

```math
\boxed{S_1\cap S_2=\varnothing.}
```

---

## 3. Fixed latent residual

The common latent root-pair family is

```math
\binom{Q_\delta}{2}.
```

Its gaps are

```text
2, 2, 4.
```

Each pair has exactly two latent owners and no current owner. Therefore the genuine latent-latent residual is

```math
\begin{aligned}
R_{\rm latent-latent}
&=
\frac12+rac12+rac14\\
&=
\boxed{\frac54}.
\end{aligned}
```

This value is independent of `delta`.

---

## 4. Reference-pair capacity fails

The reference pair is

```math
\{r_1,r_2\}
=
\{1,\delta+1\}
```

with gap `delta`. Its physical pair capacity is

```math
\frac1\delta.
```

Hence

```math
\boxed{
\frac{R_{\rm latent-latent}}{1/\delta}
=
\frac54\delta
\longrightarrow\infty.
}
```

No universal constant `C` can satisfy

```math
R_{\rm latent-latent}
\le
\frac C\delta
```

for all point-disjoint recursive affine pairs.

---

## 5. Rectangle aspects

Every shared latent gap `D` is `2` or `4`, while the reference gap is `delta`. The aspect ratios are

```math
\frac\delta2,
\qquad
\frac\delta2,
\qquad
\frac\delta4.
```

They move arbitrarily far from the near regime. The exact aspect identity remains valid:

```math
\frac1D
=
\frac\delta D\frac1\delta.
```

The obstruction is precisely the unbounded aspect coefficient.

---

## 6. What the example does not rule out

The two child states lie at very different numerical scales:

```text
S2 is fixed near 1;
S1 lies near delta.
```

Thus the family does not defeat a scale-sensitive theorem that charges the far-aspect coefficient to:

1. dyadic shell separation;
2. logarithmic depth release;
3. first appearance of the distant state;
4. terminal or production ownership;
5. a higher-order rectangle token.

It rules out only unweighted reference-pair payment.

---

## 7. Strategic consequence

The genuine latent-latent theorem must retain at least three coordinates:

```text
shared latent gap D;
reference gap delta;
child shell scales.
```

A scalar depending only on the physical reference pair is impossible.

Verifier:

```text
src/verify_far_aspect_latent_reuse_no_go.py
```