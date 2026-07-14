# Unbounded shell-valid latent-pair reuse

## Status

Symbolic infinite-family no-go theorem for oriented full-edge recursion.

For every positive integer `m`, there is a finite four-AP-free parent in one
standard dyadic block whose full-edge output contains `m` recursive side
shells sharing the same three latent root pairs. Consequently, no uniform
finite bound on one-generation latent-pair multiplicity is possible.

---

## 1. Reference set

Fix `m>=1` and define

```math
R_m=\{2\cdot3^j:0\le j<m\}.
```

The set `R_m` is three-AP-free. Indeed, if

```math
3^i+3^k=2\cdot3^j,
\qquad i<j<k,
```

then division by `3^i` gives a left-hand side congruent to `1 mod 3` and a
right-hand side divisible by `3`, a contradiction. Therefore `R_m` is also
four-AP-free.

Put

```math
L=\max R_m=2\cdot3^{m-1}.
```

Choose a power of two `d>L`, put `c=L+1`, and choose a power of two `K`
satisfying

```math
K>4c+8d.
```

Define the common root progression

```math
Q=\{K+c,K+c+d,K+c+2d\}.
```

All roots in `Q` are odd, while all references in `R_m` are even.

---

## 2. Parent support

Define

```math
B_m
=
R_m
\cup
Q
\cup
(2Q-R_m).
```

For every `r in R_m` and `q in Q`, the three points

```math
r,
\qquad q,
\qquad 2q-r
```

form a parent three-term progression. Since `q-r` is odd, every one of these
progressions belongs to the parity-even first-side class.

---

## 3. Four-AP-freeness of the reflected layer

The reflected part is

```math
2Q-R_m
=
(2K+2c-R_m)
\cup
(2K+2c+2d-R_m)
\cup
(2K+2c+4d-R_m).
```

It is three translates of `-R_m`, separated by `2d`.

Suppose four points from this union formed an arithmetic progression. Write
them as

```math
2K+2c+2j_i d-r_i,
\qquad j_i\in\{0,1,2\},
\quad r_i\in R_m.
```

The two second-difference equations have the form

```math
2d\,(j_0+j_2-2j_1)
=
r_0+r_2-2r_1
```

and its shifted analogue. The right-hand side has absolute value less than
`2L`, while `2d>2L`. Hence both integer coefficients of `2d` vanish. The
indices `j_0,j_1,j_2,j_3` form a four-term progression in `{0,1,2}`, so they
are constant. The four `r_i` would then form a four-AP in `R_m`, impossible.

Thus `2Q-R_m` is four-AP-free.

---

## 4. Four-AP-freeness of the whole parent

Every point of `B_m` can be written as

```math
aK+b,
\qquad a\in\{0,1,2\},
```

where all offsets `b` lie in an interval of width less than

```math
2c+4d.
```

The choice `K>4c+8d` makes `K` larger than twice that offset width. Therefore,
if four points of `B_m` formed an arithmetic progression, their two
second-difference equations would force the layer coefficients `a_i` to form
a four-term progression in `{0,1,2}`. They must all be equal.

Each individual layer is four-AP-free:

1. `R_m` is three-AP-free;
2. `Q` has only three points;
3. `2Q-R_m` was handled above.

Consequently

```math
\boxed{B_m\text{ is four-AP-free}.}
```

---

## 5. The shared recursive shell

For each `r in R_m`, the first-side child with reference `r` contains the
three labels

```math
Q-r
=
\{K+c-r,K+c+d-r,K+c+2d-r\}.
```

They form a three-AP of step `d`.

The smallest possible label is

```math
K+c-L=K+1,
```

and the largest is less than `2K` because `K>c+2d`. Hence every `Q-r` lies in
the same standard dyadic shell

```math
[K,2K).
```

Each reference therefore produces a recursive side shell. Every shell has
root set containing the same progression `Q`, so all three pairs in

```math
\binom Q2
```

have multiplicity at least `m` among the recursive latent-pair resources.
Thus

```math
\boxed{
\max_e\operatorname{mult}_{\rm latent}(e)\ge m.
}
```

Since `m` is arbitrary, one-generation latent-pair multiplicity is unbounded.

---

## 6. Standard dyadic parent placement

The support `B_m` lies below `5K/2` because the offset width is less than
`K/2`. Translating by `4K` gives

```math
4K+B_m\subseteq[4K,8K),
```

one standard dyadic parent block. Translation preserves four-AP-freeness,
child differences, shell assignment, and root-pair multiplicity.

The parent-to-child scale ratio is exactly `4`, independent of `m`. The
absolute scale `K` grows with the reference-set diameter.

---

## 7. Consequences for the proof program

The following candidate statements are false:

```text
recursive full-edge shells are latent-pair-disjoint;
latent-pair multiplicity is bounded by two;
latent-pair multiplicity has any universal finite bound;
scale ratio four alone forces bounded reuse.
```

Large reuse is not free, however. It forces the parent to contain

```math
R_m,
\qquad Q,
\qquad 2Q-R_m,
```

where the last term is a three-translate copy of the reference set. The
collision-fiber theorem shows that this architecture is universal for fixed
transport witnesses.

The admissible next target is therefore a weighted three-translate exposure
bound. It must charge multiplicity to the size, scale, or later termination of
the forced reference-set layers rather than attempt to cap multiplicity by a
constant.
