# Self-replicating aligned diamond

## Status

Exact recursive counterexample to any absolute or polylogarithmic bound on identical-anchor-history persistence derived from four-term-progression-freeness alone.

There are finite four-term-progression-free blocks in which one exact local three-term progression is emitted

```math
2^h
```

times by recursive states sharing the same complete root-anchor history.

The construction uses the minimum-translation backbone and middle multiplicity-fiber recursion. Its size is

```math
\Theta(3^h).
```

Thus identical-history persistence can grow at least like

```math
|D|^{\log_3 2}.
```

The construction is sparse in its ambient interval and does not solve Erdős Problem #3. It proves that the remaining theorem must be density-sensitive.

---

## 1. Base aligned gadget

Let

```math
H
=
\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

and define

```math
S_1=32+H.
```

Then

```math
S_1\subseteq[32,64)
```

and `S_1` is four-term-progression-free.

Select the four step-one progressions with sponsors

```math
32,
\quad48,
\quad53,
\quad58.
```

The representative sponsor is the minimum `32`.

The middle multiplicity-fiber child is

```math
\Xi_1=\{16,21,26\}.
```

The minimum-translation backbone of `S_1` also contains

```math
16,21,26.
```

Both children have root anchor `32`, and both emit terminal step

```math
q_0=5.
```

Hence `S_1` produces two terminal copies of the same exact local progression with the same complete anchor history.

---

## 2. No-carry three-translate lemma

Let

```math
A\subseteq[0,M]
```

be finite and four-term-progression-free. Let `R` be an integer satisfying

```math
R>2M.
```

Define

```math
A^{(R)}
=
A
\cup
(A+R)
\cup
(A+2R).
```

Then

```math
\boxed{
A^{(R)}
\text{ is four-term-progression-free}.
}
```

### Proof

Suppose

```math
z_0,z_1,z_2,z_3
```

formed a nontrivial four-term progression in `A^(R)`. Write

```math
z_i=a_i+\varepsilon_iR,
\qquad
a_i\in A,
\qquad
\varepsilon_i\in\{0,1,2\}.
```

The progression equations are

```math
z_0-2z_1+z_2=0
```

and

```math
z_1-2z_2+z_3=0.
```

The low-order parts satisfy

```math
|a_0-2a_1+a_2|\le2M<R
```

and

```math
|a_1-2a_2+a_3|\le2M<R.
```

Therefore the coefficients of `R` in both equations must vanish:

```math
\varepsilon_0-2\varepsilon_1+\varepsilon_2=0,
```

```math
\varepsilon_1-2\varepsilon_2+\varepsilon_3=0.
```

Thus `epsilon_0,...,epsilon_3` is a length-four arithmetic progression taking values in `{0,1,2}`. The only possibility is that it is constant.

The low-order values `a_0,...,a_3` would then form a four-term progression in `A`, contradiction.

---

## 3. Recursive lift

Assume that

```math
S_h\subseteq[L_h,2L_h)
```

is four-term-progression-free and has a certified recursion producing

```math
2^h
```

terminal copies of step `q_0=5` from the same exact local progression and with the same complete anchor history.

Put

```math
A_h=\{0\}\cup S_h
```

and let

```math
M_h=\max S_h.
```

The set `A_h` is four-term-progression-free. Indeed, any four-term progression containing `0` would have the form

```math
0,d,2d,3d.
```

But `d in S_h` would imply `d>=L_h`, hence `3d>=3L_h>2L_h`, outside `S_h`.

Choose an odd integer

```math
R_h>2M_h.
```

The oddness ensures that the coordinated side-anchor orientation for step `R_h` is positive.

Define the raw outer gadget

```math
G_{h+1}
=
A_h
\cup
(A_h+R_h)
\cup
(A_h+2R_h).
```

By the no-carry lemma, `G_{h+1}` is four-term-progression-free.

Choose a power of two `L_{h+1}` larger than `max G_{h+1}` and define

```math
S_{h+1}=L_{h+1}+G_{h+1}.
```

Then

```math
S_{h+1}\subseteq[L_{h+1},2L_{h+1})
```

and `S_{h+1}` is four-term-progression-free.

---

## 4. The two identical child states

In `S_{h+1}`, select the step-`R_h` progression sponsored by

```math
L_{h+1}+a
```

for every

```math
a\in A_h.
```

Because `R_h>M_h`, the sponsor layer, center layer, and endpoint layer are disjoint. All sponsors can be deleted while their centers and endpoints remain.

The representative sponsor is the minimum

```math
L_{h+1}.
```

### Middle multiplicity-fiber child

The selected centers are

```math
L_{h+1}+a+R_h,
\qquad a\in A_h.
```

Translating the nonrepresentative centers by the minimum center `L_{h+1}+R_h` gives exactly

```math
S_h.
```

Thus one recursive child is `S_h`.

### Minimum-translation backbone child

Translate the parent by its minimum `L_{h+1}`. The backbone is

```math
G_{h+1}\setminus\{0\}.
```

Since

```math
R_h>2M_h>2L_h,
```

the standard dyadic shell

```math
[L_h,2L_h)
```

of the backbone contains exactly `S_h` and no point from the `R_h`- or `2R_h`-translate layers.

Thus the backbone produces a second child equal to `S_h`.

Both children have the same root anchor

```math
L_{h+1}.
```

---

## 5. Doubling identical-history persistence

The two child states are identical copies of `S_h` with the same root anchor. Apply the certified recursion of `S_h` inside each copy.

Each copy emits

```math
2^h
```

terminal copies of the same exact local progression and with the same continuation anchor history.

Therefore `S_{h+1}` emits

```math
\boxed{2^{h+1}}
```

copies with the same complete anchor history.

This completes the induction.

---

## 6. Cardinality growth

Let

```math
n_h=|S_h|.
```

The three translate layers are disjoint, and

```math
|A_h|=n_h+1.
```

Therefore

```math
n_{h+1}=3(n_h+1),
\qquad
n_1=12.
```

Solving the recurrence gives

```math
\boxed{
n_h
=
\frac{9\cdot3^h-3}{2}.
}
```

The terminal persistence multiplicity is

```math
\boxed{2^h}.
```

Consequently

```math
\boxed{
2^h
\asymp
n_h^{\log_3 2}.
}
```

Thus no bound of the form

```math
O(|D|^\theta)
```

with

```math
\theta<\log_3 2
```

can hold for identical-anchor-history persistence in general four-term-progression-free blocks.

In particular, absolute, logarithmic, and polylogarithmic persistence bounds are false.

---

## 7. Ambient scale

The construction can be made quantitatively explicit.

Choose

```math
R_h=2M_h+1.
```

Then

```math
\max G_{h+1}
=
M_h+2R_h
=
5M_h+2.
```

Choose `L_{h+1}` as the least power of two greater than `5M_h+2`. Since `M_h<2L_h`,

```math
L_{h+1}
<
20L_h+8.
```

Hence

```math
L_h=O(20^h).
```

For infinitely many block scales,

```math
\boxed{
\text{identical-history persistence}
\ge
cL_h^{\log_{20}2}.
}
```

This scale exponent is not claimed to be optimal. The cardinality exponent `log_3 2` is the intrinsic statement of the construction.

---

## 8. Explicit depth-two instance

Take the base state

```math
S_1
=
\{32,33,34,48,49,50,53,54,55,58,59,60\}.
```

Put

```math
A_1=\{0\}\cup S_1
```

and choose

```math
R_1=67.
```

Although `67` is smaller than the no-carry choice `2 max(S_1)+1`, a direct exhaustive check shows that

```math
G_2
=
A_1
\cup
(A_1+67)
\cup
(A_1+134)
```

is four-term-progression-free.

It has

```math
|G_2|=39
```

and maximum `194`. Translating by `256` places it in `[256,512)`.

The outer step-`67` middle fiber and backbone shell `[32,64)` both equal `S_1`. Each copy of `S_1` then produces two copies of terminal progression

```math
16,21,26.
```

Thus the 39-point depth-two gadget produces four terminal copies with the same complete anchor history.

A companion verifier is provided in

```text
src/verify_self_replicating_aligned_diamond_depth2.py
```

---

## 9. Consequence for the active proof program

The following targets are false without additional density-sensitive hypotheses:

1. bounded exact-progression persistence;
2. polylogarithmic same-anchor persistence;
3. subpower persistence with exponent below `log_3 2` in terms of parent cardinality;
4. a theorem forbidding repeated aligned diamonds solely from four-term-progression-freeness.

The remaining theorem must compare persistence with the ambient scale, density, or reciprocal mass of the parent block.

The construction has cardinality `Theta(3^h)` while its scale grows faster than `3^h`. It remains sparse and does not provide a divergent reciprocal-sum counterexample.

The correct target is now:

```math
\boxed{
\text{prove that high-density blocks cannot sustain the self-replicating aligned-diamond mechanism efficiently across scales.}
}
```
