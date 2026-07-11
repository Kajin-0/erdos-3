# Scale-eight self-replicating aligned diamonds

## Status

Computer-assisted exact construction and finite-state certificate.

This note improves the ambient-scale estimate in the self-replicating aligned-diamond construction. There are four-term-progression-free blocks

```math
S_h\subseteq[L_h,2L_h)
```

with identical complete-anchor-history persistence `2^h`, cardinality `Theta(3^h)`, and now the exact scale law

```math
\boxed{L_h=8^{h+1}.}
```

Consequently

```math
\boxed{
\text{persistence}(S_h)
=
2^h
=
\frac12L_h^{1/3}.
}
```

The previous general no-carry construction only gave `L_h=O(20^h)`. The new family uses alternating base-eight separations and is certified as four-term-progression-free by a 34-state digit automaton and an exact product/carry search.

Two companion elementary notes prove that this construction is quantitatively sharp inside the exact standard-dyadic three-translate model:

- `docs/three-translate-dyadic-scale-barrier.md` proves `L' >= 8L` at every exact replication step;
- `docs/exact-three-translate-weighted-density-theorem.md` proves the sharp decay
  ```math
  P\alpha(P)\ll P^{\log_2 3-2}.
  ```

All theorem-style conclusions remain awaiting independent expert review.

---

## 1. Base state

Let

```math
H
=
\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

and put

```math
L_1=64,
\qquad
S_1=L_1+H.
```

The translation from `32+H` to `64+H` does not change the local aligned-diamond mechanism. The block remains four-term-progression-free and lies in

```math
S_1\subseteq[64,128).
```

As in the original base gadget, four selected step-one progressions produce the middle multiplicity fiber

```math
\{16,21,26\},
```

while the minimum-translation backbone contains the same progression. Both copies have the same root anchor. Thus `S_1` produces two terminal copies of step `5` with identical anchor history.

---

## 2. Alternating separations

For `h>=1`, define

```math
L_h=8^{h+1}
```

and

```math
k_h
=
\begin{cases}
6,&h\text{ odd},\\
1,&h\text{ even}.
\end{cases}
```

Set

```math
R_h
=
2L_h+k_h\frac{L_h}{8}.
```

Equivalently,

```math
R_h
=
\begin{cases}
22\cdot8^h,&h\text{ odd},\\
17\cdot8^h,&h\text{ even}.
\end{cases}
```

The two choices are the base-eight two-digit coefficients

```text
26_8
```

and

```text
21_8.
```

Their two-adic valuations are

```math
v_2(R_h)
=
\begin{cases}
3h+1,&h\text{ odd},\\
3h,&h\text{ even},
\end{cases}
```

and are therefore always even. Under the coordinated side-anchor deletion rule, every selected step-`R_h` progression deletes its left endpoint. This preserves the sponsor orientation required by the aligned-diamond recursion.

Also,

```math
2L_h<R_h<3L_h.
```

Since `S_h subseteq[L_h,2L_h)`, the three translate layers below are disjoint.

---

## 3. Recursive construction

Put

```math
A_h=\{0\}\cup S_h
```

and define

```math
G_{h+1}
=
A_h
\cup
(A_h+R_h)
\cup
(A_h+2R_h).
```

Then set

```math
L_{h+1}=8L_h
```

and

```math
S_{h+1}=L_{h+1}+G_{h+1}.
```

Because `max S_h<2L_h` and `R_h<=11L_h/4`,

```math
\max G_{h+1}
<
2L_h+2\left(\frac{11}{4}L_h\right)
=
\frac{15}{2}L_h
<
8L_h.
```

Hence

```math
S_{h+1}\subseteq[L_{h+1},2L_{h+1}).
```

The scale recurrence is exact:

```math
\boxed{L_{h+1}=8L_h.}
```

The companion scale-barrier theorem shows that no smaller standard-dyadic jump is possible for an exact three-translate replication step with uncontaminated backbone reproduction.

---

## 4. Two identical recursive children

Inside `S_{h+1}`, select the step-`R_h` progression

```math
L_{h+1}+a,
\quad
L_{h+1}+a+R_h,
\quad
L_{h+1}+a+2R_h
```

for every

```math
a\in A_h.
```

Since `v_2(R_h)` is even, the coordinated sponsor is the left endpoint. The sponsor, center, and endpoint layers are disjoint because `R_h>max S_h`.

The selected middle centers are

```math
L_{h+1}+R_h+a,
\qquad
a\in A_h.
```

The center-difference multiplicity fiber obtained by subtracting the center corresponding to `a=0` is exactly

```math
S_h.
```

The minimum-translation backbone is

```math
G_{h+1}\setminus\{0\}.
```

Its standard dyadic shell `[L_h,2L_h)` contains exactly the unshifted copy `S_h`, because

```math
R_h>2L_h.
```

Thus the backbone also produces exactly `S_h`.

Both children inherit the same new root anchor `L_{h+1}`. Therefore each occurrence of the certified recursion inside `S_h` is duplicated with the same complete anchor history.

Inductively,

```math
\boxed{
\text{identical-history persistence}(S_h)=2^h.
}
```

---

## 5. Cardinality and density

The translate layers are disjoint and

```math
|A_h|=|S_h|+1.
```

Writing `n_h=|S_h|`,

```math
n_{h+1}=3(n_h+1),
\qquad
n_1=12.
```

Therefore

```math
\boxed{
n_h
=
\frac{9\cdot3^h-3}{2}.
}
```

Since

```math
L_h=8^{h+1}
```

and persistence `P_h=2^h`,

```math
\boxed{P_h=\frac12L_h^{1/3}.}
```

The dyadic density is

```math
\alpha_h
=
\frac{|S_h|}{L_h}
=
\frac{9\cdot3^h-3}{2\cdot8^{h+1}}.
```

In terms of persistence,

```math
\alpha_h
\asymp
P_h^{\log_2 3-3}.
```

The multiplicity-weighted density therefore satisfies

```math
P_h\alpha_h
\asymp
P_h^{\log_2 3-2},
```

where

```math
\log_2 3-2\approx-0.4150375.
```

Thus this efficient replication family still spends a geometrically summable amount of multiplicity-weighted dyadic density.

The exact-model weighted-density theorem shows that the same exponent is an upper bound for every exact standard-dyadic three-translate genealogy, and that

```math
\sum_hP_h\alpha_h<\infty
```

with an explicit root-dependent bound.

---

## 6. Exact finite-state certificate

The companion verifier is

```text
src/verify_scale_eight_aligned_diamond.py
```

Run

```bash
python src/verify_scale_eight_aligned_diamond.py --depth 5
```

The recursive construction has a finite least-significant-digit-first base-eight description. At each level, the two alternating coefficients `26_8` and `21_8` replace the terminal digit pair by one of three possible transformed pairs. This gives a finite nondeterministic automaton. Determinization produces a complete DFA recognizing

```math
\bigcup_{h\ge1}S_h.
```

The verifier then applies the standard product/carry certificate for

```math
x_0-2x_1+x_2=0,
\qquad
x_1-2x_2+x_3=0.
```

The exact certificate metrics are

```text
dfa_states=34
accepting_states=6
product_states=17238
dfa_signature=e08c121adfee8cfa635ccb11d65c8519604611865ba504237f84896f908d757d
```

No accepting nontrivial four-term-progression state is reachable.

The script additionally checks finite shells through the requested depth, including:

1. exact equality between each recursive `S_h` and the automaton language inside `[L_h,2L_h)`;
2. four-term-progression-freeness of each explicitly generated shell;
3. the cardinality formula;
4. disjoint translate layers;
5. even `v_2(R_h)` and therefore the correct coordinated sponsor orientation.

Expected output:

```text
verified: recursive shells match the automaton
verified: every checked finite shell is 4-AP-free
verified: v2(R_h) is even at every checked replication level
verified: the full automaton language is 4-AP-free
depth_checked=5
dfa_states=34
accepting_states=6
product_states=17238
dfa_signature=e08c121adfee8cfa635ccb11d65c8519604611865ba504237f84896f908d757d
```

---

## 7. Consequences for the active program

This improves the known ambient-scale lower construction from

```math
\text{persistence}\gtrsim L^{\log_{20}2}
```

to

```math
\boxed{
\text{persistence}\gtrsim L^{1/3}.
}
```

The companion barrier theorem proves that `1/3` is also the matching upper exponent inside the exact standard-dyadic three-translate model.

Likewise, the companion weighted-density theorem proves sharply within that model that

```math
\boxed{
P\alpha(P)
\ll
P^{\log_2 3-2}
}
```

and that the total weighted density along one exact genealogy is summable.

Therefore the canonical exact obstruction is now quantitatively classified. A full theorem must control mechanisms outside the exact model: overlapping or approximate replication, several interacting parent states, nonuniform branching, or persistence distributed across several dyadic shells.

The scale-eight family does not produce a divergent reciprocal-sum counterexample. Its densities decay geometrically:

```math
\alpha_h
\asymp
\left(\frac38\right)^h.
```

The construction is instead a sharp test case for any proposed density-sensitive persistence theorem.
