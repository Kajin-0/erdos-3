# Cross-state fixed-label amplification

## Corrected status

This note amplifies the dyadic-shell-compatible sibling sharpness construction from

```text
docs/dyadic-shell-compatible-sibling-sharpness.md
```

The resulting family proves that raw fixed-label terminal multiplicity can grow polynomially inside four-term-progression-free blocks. The repeated copies occur at different lifted centers, so the global lifted-center layer theorem exports this multiplicity into lower-scale difference children.

Thus the construction rules out bounded raw multiplicity, but it does not contradict the current reduced target of controlling repeated use of one exact lifted progression.

---

## 1. Shell-compatible translation gadget

Let

```math
D_0=\{309,324,342,360,365,386,419,434,438,440,452,453,460,466,470,475,
490,494,498,510,514,515,529,540,543,544,550,560,562,580,585\}.
```

Put

```math
D_1=D_0\cup\{284,394,504\}
```

and define

```math
G=13D_1+4500.
```

Then

```math
G\subseteq[8192,16384)
```

and `G` is four-term-progression-free.

The certified deletion sequence and spanning forest produce terminal label

```math
q_0=234
```

in two sibling dyadic shells:

1. the middle multiplicity-fiber shell `[512,1024)`;
2. the spanning-component shell `[2048,4096)`.

For every integer shift `L`, the translated set

```math
G+L
```

has the same internal differences, deletion certificate, child differences, and duplicated terminal label `234`.

---

## 2. Finite-avoidance lemma

Let `U` be a finite four-term-progression-free set. Only finitely many shifts `L` make

```math
U\cup(G+L)
```

non-disjoint or create a mixed four-term progression.

For a possible mixed progression write

```math
z_i=w_i+\varepsilon_iL,
\qquad
\varepsilon_i\in\{0,1\}.
```

The progression equations are

```math
z_0-2z_1+z_2=0,
```

and

```math
z_1-2z_2+z_3=0.
```

For a nonconstant binary membership vector `epsilon`, the coefficients of `L` cannot vanish in both equations. Otherwise `epsilon_0,epsilon_1,epsilon_2,epsilon_3` would itself be a length-four arithmetic progression in `{0,1}`, which forces it to be constant.

Thus every fixed membership pattern and fixed point assignment forbids at most one shift. Since there are finitely many assignments, only finitely many shifts are excluded.

Inductively, arbitrarily many translated copies of `G` can coexist in one four-term-progression-free union.

---

## 3. Arbitrarily large raw multiplicity

For every positive integer `k`, choose shifts

```math
L_1,\ldots,L_k
```

such that

```math
U_k=\bigcup_{j=1}^{k}(G+L_j)
```

is a disjoint four-term-progression-free union.

Run the certified internal deletion sequence in each copy. Every copy produces two shell-resolved sibling terminal occurrences of label `234`. Therefore

```math
\boxed{
\mu(234)\ge2k.
}
```

Hence no absolute or polylogarithmic upper bound on raw fixed-label terminal multiplicity follows from four-term-progression-freeness alone.

---

## 4. Quadratic diameter bound

Suppose `U_m` contains `m` copies. For each nonconstant membership pattern, fix the gadget offsets in the positions belonging to the new copy.

If exactly one progression position lies in `G+L`, the two independent progression equations leave at most two freely chosen old values; the remaining old value and `L` are determined. Hence these patterns forbid

```math
O(|U_m|^2)=O(m^2)
```

shifts.

Patterns with two or three new-copy positions forbid no more. Adding disjointness exclusions, the total number of forbidden shifts at stage `m` is

```math
O(m^2).
```

Choose the next shift among the first one more than the number of forbidden nonnegative shifts. Then `k` copies fit in diameter

```math
O(k^2).
```

After one common translation, the union lies in a ratio-two block

```math
[N,2N)
```

with

```math
N=O(k^2).
```

Therefore, for infinitely many `N`,

```math
\boxed{
\mu(234)\ge cN^{1/2}
}
```

for an absolute constant `c>0`.

The construction has density only

```math
O(N^{-1/2}),
```

so its dyadic densities are summable.

---

## 5. Interpretation after global center layering

The copies `G+L_j` produce the same numerical label `234`, but their lifted progression centers differ by the shifts `L_j`.

The global lifted-center layer construction groups these distinct centers and exports all but one representative per layer into lower-scale four-term-progression-free difference children.

Therefore this amplified family shows:

1. raw fixed-label multiplicity can be polynomially large;
2. a useful theorem must distinguish repeated labels at different lifted centers from repeated use of the same lifted progression;
3. the active unresolved quantity is
   ```math
   L(q)=\max_x\nu_q(x),
   ```
   not the total raw multiplicity `mu(q)`.

The correct next target is an exact-progression persistence theorem, not a universal fixed-label multiplicity bound.