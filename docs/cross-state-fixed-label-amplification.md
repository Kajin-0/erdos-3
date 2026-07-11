# Cross-state fixed-label amplification

## Status

Exact finite-avoidance amplification of the sibling two-layer sharpness example.

The explicit gadget in

```text
docs/sibling-two-layer-sharpness-counterexample.md
```

produces the same terminal label

```math
q_0=18
```

in two sibling layers. This note proves that arbitrarily many translated copies of that gadget can coexist inside one finite four-term-progression-free set.

Consequently, fixed-label cross-state terminal multiplicity is not bounded. Quantitatively, one can obtain multiplicity at least

```math
cN^{1/2}
```

inside a block of diameter `N`.

---

## 1. Translation gadget

Let `G` be the 31-element four-term-progression-free set from the sharpness example:

```math
\begin{aligned}
G=\{&309,324,342,360,365,386,419,434,438,440,452,453,460,466,470,475,\\
&490,494,498,510,514,515,529,540,543,544,550,560,562,580,585\}.
\end{aligned}
```

Inside `G`, the valid side-anchor deletion sequence and chosen spanning tree produce terminal label `18` in both

1. the middle multiplicity-fiber child `Xi_110`, and
2. the spanning-forest component child `Theta`.

For every integer shift `L`, the translated set

```math
G+L
```

has exactly the same internal difference structure. Therefore it remains four-term-progression-free and carries the same deletion-DAG certificate and the same duplicated terminal label `18`.

---

## 2. Finite-avoidance lemma

Let `U` be a finite four-term-progression-free set. Then there are only finitely many shifts `L` for which

```math
U\cup(G+L)
```

fails to be four-term-progression-free or fails to be disjoint.

### Proof

Disjointness fails only if

```math
u=g+L
```

for some `u in U` and `g in G`. This forbids finitely many values

```math
L=u-g.
```

Now consider a four-term progression

```math
z_0,z_1,z_2,z_3
```

in `U union (G+L)` that uses points from both sets. Write

```math
z_i=w_i+\varepsilon_iL,
```

where

```math
\varepsilon_i\in\{0,1\},
```

and `w_i` is chosen from `U` when `epsilon_i=0` and from `G` when `epsilon_i=1`.

The four-term progression equations are

```math
z_0-2z_1+z_2=0,
```

and

```math
z_1-2z_2+z_3=0.
```

The coefficients of `L` are

```math
\varepsilon_0-2\varepsilon_1+\varepsilon_2
```

and

```math
\varepsilon_1-2\varepsilon_2+\varepsilon_3.
```

They cannot both vanish for a nonconstant binary vector

```math
(\varepsilon_0,\varepsilon_1,\varepsilon_2,\varepsilon_3).
```

Indeed, if both vanish, the binary sequence `epsilon_i` is an arithmetic progression of length four. The only such sequence taking values in `{0,1}` is constant.

Therefore at least one progression equation has a nonzero coefficient of `L`. Once the membership pattern and the points `w_i` are fixed, that equation determines at most one value of `L`.

There are finitely many membership patterns and point choices, so only finitely many shifts are forbidden.

Hence some shift `L` makes `U union (G+L)` disjoint and four-term-progression-free.

---

## 3. Arbitrarily many copies

Apply the lemma inductively.

Start with

```math
U_1=G+L_1.
```

Given a disjoint four-term-progression-free union

```math
U_m=\bigcup_{j=1}^{m}(G+L_j),
```

choose `L_{m+1}` outside the finite forbidden set for `U_m`.

Then

```math
U_{m+1}=U_m\cup(G+L_{m+1})
```

is again a disjoint four-term-progression-free union.

Thus, for every positive integer `k`, there is a finite four-term-progression-free set containing `k` translated copies of `G`.

Run the certified deletion sequence independently inside each copy. Each copy produces two sibling terminal occurrences of label `18`. Therefore

```math
\boxed{\mu(18)\ge 2k.}
```

In particular, no absolute or polylogarithmic bound on fixed-label cross-state multiplicity can follow from four-term-progression-freeness alone.

---

## 4. Quadratic diameter bound

The induction can be made quantitative.

Suppose `U_m` contains `m` copies, so

```math
|U_m|=m|G|.
```

Fix a nonconstant membership pattern

```math
\varepsilon\in\{0,1\}^4
```

and fix the gadget offsets in every position with `epsilon_i=1`.

If exactly one progression point lies in `G+L`, then three positions lie in `U_m`. The two progression equations have rank two in the three old values and `L`. After choosing any two old values, the remaining old value and `L` are determined. Thus these patterns forbid at most

```math
O(|U_m|^2)
```

shifts.

If exactly two progression points lie in `G+L`, there are only two old values, so the number of assignments is already

```math
O(|U_m|^2).
```

If exactly three progression points lie in `G+L`, there is one old value, giving only

```math
O(|U_m|)
```

possibilities.

The gadget `G` and the 14 nonconstant membership patterns are fixed. Adding the disjointness exclusions, the total number of forbidden shifts at stage `m` is therefore

```math
O(m^2).
```

Choose `L_{m+1}` among the first one more than the number of forbidden nonnegative integers. Inductively, all `k` shifts can be chosen in an interval of length

```math
O(k^2).
```

After one final common translation, the union lies in a dyadic interval

```math
[N,2N)
```

with

```math
N=O(k^2).
```

Since `mu(18)>=2k`, this gives

```math
\boxed{\mu(18)\ge cN^{1/2}}
```

for an absolute constant `c>0` and infinitely many `N`.

---

## 5. Consequence for the active proof program

The sibling two-layer theorem is sharp, and the sharp event can be repeated polynomially many times across unrelated parent components.

Therefore the remaining multiplicity theorem cannot assert any of the following without additional global hypotheses:

1. bounded fixed-label multiplicity;
2. polylogarithmic fixed-label multiplicity;
3. universal one-layer sibling collapse;
4. elimination of the component-child duplication mechanism.

The correct target must charge repeated fixed-label events to the amount or scale distribution of the parent set. The finite-avoidance construction has density only

```math
O(N^{-1/2}),
```

so it does not approach a divergent reciprocal-sum counterexample. It does, however, show that the missing theorem must be genuinely quantitative and density-sensitive.
