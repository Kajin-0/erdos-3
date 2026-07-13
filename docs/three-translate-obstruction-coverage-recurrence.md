# Exact three-translate obstruction classes and coverage recurrence

## Status

Elementary state-independent theorem with exact symbolic verification.

This note replaces candidate-by-candidate factor-four exploration as the active theorem-discovery layer. It classifies every possible layer pattern of a four-term arithmetic progression in a three-translate parent and derives an exact recurrence for those obstruction patterns under another three-translate replication.

The result does **not** prove whole-tree Bellman compensation and does not prove `N_10,4=0`. It supplies the finite symbolic state space and exact recurrence in which a contamination reserve can be sought.

**Verifier:** `src/verify_three_translate_obstruction_classes.py`  
**Certificate:** `data/three_translate_obstruction_classes_certificate_2026-07-13.txt`

---

## 1. Three-translate parent

Let

```math
G_R(B)=B\cup(B+R)\cup(B+2R).
```

Suppose

```math
z_i=b_i+\lambda_iR,
\qquad
b_i\in B,
\qquad
\lambda_i\in\{0,1,2\},
```

for `i=0,1,2,3`. The word

```math
\lambda=(\lambda_0,\lambda_1,\lambda_2,\lambda_3)
```

records the translate layer used by the four terms.

Adding the same integer to all four layer indices translates the entire progression by a multiple of `R`. Every word can therefore be normalized by subtracting its minimum layer.

There are

```math
3^4-2^4=65
```

normalized words. The word `0000` lies entirely in `B`. Removing it leaves `64` nonconstant normalized words.

Reversing a progression reverses its layer word. Quotienting the `64` words by reversal gives exactly

```math
\boxed{34}
```

nonconstant layer-pattern classes:

```text
30 two-word reversal classes
4 self-reversing classes
```

The four self-reversing classes are

```text
0110  0220  1001  2002.
```

This classification is independent of `B`, `R`, dyadic scale, contamination history, and the numerical identity of `S_10`.

---

## 2. Correct affine signature

A four-term progression requires two equal-difference equations, not merely vanishing third difference. Define

```math
r_\lambda=\lambda_1-\lambda_0,
```

```math
a_\lambda=\lambda_0-2\lambda_1+\lambda_2,
```

and

```math
b_\lambda=\lambda_1-2\lambda_2+\lambda_3.
```

The triple

```math
\boxed{(r_\lambda,a_\lambda,b_\lambda)}
```

uniquely reconstructs the normalized layer word. Indeed, before normalization its layers are

```math
0,
\quad r_\lambda,
\quad 2r_\lambda+a_\lambda,
\quad 3r_\lambda+2a_\lambda+b_\lambda.
```

Under reversal,

```math
(r,a,b)
\longmapsto
(-(r+a+b),b,a).
```

---

## 3. Exact one-scale parameterization

Write the first base point as `x` and the first base increment as `d`. A layer word with signature `(r,a,b)` produces a four-term progression in `G_R(B)` exactly when

```math
x,
\quad x+d,
\quad x+2d-aR,
\quad x+3d-(2a+b)R
```

all belong to `B`, and

```math
\boxed{d+rR\ne0.}
```

The projected common difference is

```math
q=d+rR.
```

Therefore define the master affine-incidence function

```math
\mathcal F_B(A,C;Q)
=
\#\left\{
(x,d):
\begin{array}{l}
x,\ x+d,\ x+2d-A,\\
x+3d-(2A+C)\in B,\\
d+Q\ne0
\end{array}
\right\}.
```

The coverage of the layer class `lambda` at separation `R` is

```math
\boxed{
\Gamma_\lambda(B;R)
=
\mathcal F_B(a_\lambda R,b_\lambda R;r_\lambda R).
}
```

If `B` is four-term-progression-free, then

```math
G_R(B)
```

is four-term-progression-free if and only if all `34` nonconstant class coverages vanish.

This is the exact obstruction decomposition required for the contaminated cheap-step setting. Named witnesses such as completion, `0011`, `1001`, and `2002` are particular classes or factorizations inside this list; they are not an exhaustive taxonomy by themselves.

---

## 4. The `0011` coverage function

For signed `d`, define the pair-start set

```math
P_d(B)=\{x\in B:x+d\in B\}.
```

The class `0011` has signature

```math
(r,a,b)=(0,1,-1).
```

Its base points are

```math
x,
\quad x+d,
\quad x+2d-R,
\quad x+3d-R.
```

Writing

```math
y=x+2d-R,
```

gives the exact separation-coverage function

```math
\boxed{
C_B(R)
=
\sum_{d>0}
\#\{(x,y)\in P_d(B)^2:R=x+2d-y\}.
}
```

Thus

```math
C_B(R)>0
```

is exactly a labeled `0011` witness at separation `R`.

---

## 5. Exact pair-start recurrence

For every signed difference `d`,

```math
\boxed{
P_d(G_S(B))
=
\bigcup_{i,j\in\{0,1,2\}}
\left(P_{d+(i-j)S}(B)+iS\right).
}
```

Proof: if

```math
z=b+iS,
\qquad
z+d=c+jS,
```

then

```math
c-b=d+(i-j)S.
```

The converse is immediate. The set identity is valid even when translate layers overlap. Treating `(i,j)` as labels makes the union disjoint as a multiset and preserves exact multiplicities.

Substituting this identity into `C_B` gives an explicit finite autocorrelation expansion for `0011` coverage after replication. This is the precise recurrence suggested by the repeated rectangle witnesses in the finite certificates.

---

## 6. Exact two-scale obstruction recurrence

Let the current state be

```math
B'=G_S(B),
```

and test a new candidate separation `T`. Fix a candidate layer word `lambda` and choose layer representations `mu` for the four base points inside `B'`.

Set

```math
A=a_\lambda T+a_\mu S,
```

```math
C=b_\lambda T+b_\mu S,
```

and

```math
Q=r_\lambda T+r_\mu S.
```

Then the four original points in `B` must be

```math
x,
\quad x+d,
\quad x+2d-A,
\quad x+3d-(2A+C),
```

and their final projected common difference is

```math
d+Q.
```

Consequently the labeled class coverage satisfies the exact recurrence

```math
\boxed{
\widetilde\Gamma_\lambda(G_S(B);T)
=
\sum_{\mu\in\{0,1,2\}^4}
\mathcal F_B(
 a_\lambda T+a_\mu S,
 b_\lambda T+b_\mu S;
 r_\lambda T+r_\mu S
).
}
```

The left side counts layer representations, so one projected progression may be counted more than once when layers overlap. This causes no problem for obstruction detection:

```math
\widetilde\Gamma_\lambda(G_S(B);T)>0
```

if and only if a progression of class `lambda` exists.

This formula is the state-independent obstruction-coverage recurrence. It shows that replication closes naturally on the three-parameter affine spectrum `mathcal F_B`, rather than on scalar additive energy.

---

## 7. Consequence for the research program

The next theorem should not enumerate more contiguous `S_10` candidates. It should find a normalized reserve built from the affine spectrum, for example a functional of the form

```math
\Phi(B)
=
\frac{P}{L}
\Psi(\mathcal F_B,\text{ slack},\text{ imported prefixes},\text{ overlap}).
```

The required transition statement must be branching-compatible. A plausible target is

```math
W(B)
+
\sum_{B'\in\operatorname{Child}(B)}
\left(\mathfrak B(B')+\Phi(B')\right)
\le
\mathfrak B(B)+\Phi(B)
+
\text{controlled error}.
```

This is stronger than pathwise summability and is the appropriate form for whole-tree compensation.

The immediate computational use of `S_10` is now diagnostic:

1. classify sampled witnesses by the 34 exact layer classes;
2. record their `(r,a,b)` signatures and ancestor origins;
3. identify which terms of the two-scale recurrence generate most coverage;
4. search for a small closed subsystem or monotone zero-set contraction;
5. test candidate reserves against all children, not only one distinguished path.

---

## 8. Caveat

The classification and recurrence are exact. They do not yet prove that cheap steps increase a monotone reserve, that factor-four continuation must terminate, or that the deletion tree has finite total weighted mass.

The full Erdős problem remains open.
