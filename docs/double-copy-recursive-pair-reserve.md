# Double-copy recursive pair reserve

## Status

State-independent pair-energy theorem for every recursively continuing completion-step shell.

A recursive heavy shell has two affine physical copies in the ambient root set. Each copy, considered with the appropriate affine scaling, contains enough internal pair energy to pay the complete recursive shell debt by itself.

This converts the universal packing question into a two-choice capacitated orientation problem on physical pair resources. The full ordered pair of copies is injective even when either projected copy is reused.

---

## 1. Recursive step shell

Let

```math
T=\{d_1<\cdots<d_n\}\subseteq[M,2M)
```

be recursively continuing. Then `T` contains a three-term progression, so

```math
n\ge3.
```

Define

```math
H(T)=\sum_{d\in T}\frac1d
```

and complete pair energy

```math
J(T)=\sum_{1\le i<j\le n}\frac1{d_j-d_i}.
```

---

## 2. First-copy reserve

The adjacent horizontal chain is a subfamily of the complete pair set. By the horizontal-chain theorem,

```math
J(T)
\ge
\sum_{i=1}^{n-1}\frac1{d_{i+1}-d_i}
>
H(T).
```

Therefore every unscaled affine copy

```math
c+\sigma T
```

contains internal physical pair energy strictly greater than `H(T)`.

All first-copy pair gaps are less than `M`, so this reserve has strict gap descent.

---

## 3. Adjacent-role second-copy reserve

For a right or left adjacent completion role, the second affine copy is

```math
c+2\sigma T.
```

Scaling doubles every pair gap, hence its physical pair energy is

```math
\frac12J(T).
```

We prove

```math
\boxed{
\frac12J(T)>H(T).
}
```

### Case `n>=4`

The adjacent chain gives

```math
J(T)
>
\frac{(n-1)^2}{M}.
```

Therefore

```math
\frac12J(T)
>
\frac{(n-1)^2}{2M}
\ge
\frac nM
\ge
H(T),
```

because

```math
(n-1)^2\ge2n
```

for every `n>=4`.

### Case `n=3`

Since `T` is recursive, it must itself be a three-AP:

```math
T=\{d,d+q,d+2q\}.
```

The dyadic-shell condition gives

```math
d+2q<2M\le2d,
```

so

```math
q<d/2.
```

The complete pair energy is

```math
J(T)=\frac1q+\frac1q+\frac1{2q}=\frac5{2q}.
```

Using `d>2q`,

```math
\begin{aligned}
H(T)
&=
\frac1d+\frac1{d+q}+\frac1{d+2q}\\
&<
\frac1{2q}+\frac1{3q}+\frac1{4q}\\
&=
\frac{13}{12q}
<
\frac5{4q}
=
\frac12J(T).
\end{aligned}
```

Thus the second-copy reserve also pays the full adjacent-role debt in all cases.

Its pair gaps are less than `2M`, so its dyadic gap scale is nonincreasing and can equal the state scale.

---

## 4. Outer-role second-copy reserve

For an outer completion role, the two affine copies are

```math
c-T,
\qquad
c+T.
```

Both are unscaled, and each has pair energy `J(T)`. The weighted outer-role debt is only

```math
\frac12H(T).
```

Therefore either copy satisfies

```math
\boxed{
J(T)>H(T)>\frac12H(T).
}
```

Both copies have strict gap descent.

---

## 5. Two-choice resource formulation

For every recursive embedded state `s`, define two physical pair sets:

```math
E_1(s)=\binom{c+\sigma T}{2}
```

and the role-dependent second-copy set

```math
E_2(s)
=
\begin{cases}
\binom{c+2\sigma T}{2},&\text{adjacent role},\\
\binom{c-\sigma T}{2},&\text{outer opposite copy}.
\end{cases}
```

The theorem gives

```math
J(E_1(s))>\operatorname{debt}(s)
```

and

```math
J(E_2(s))>\operatorname{debt}(s).
```

Thus every recursive state has two independently sufficient resource neighborhoods.

---

## 6. Injective ordered double lift

The complete ordered configuration

```math
(E_1(s),E_2(s))
```

or, equivalently, the two ordered affine point copies, determines:

```text
completion reference;
completion role and orientation;
numerical step state T.
```

Therefore distinct embedded state occurrences have distinct ordered double-copy configurations.

Either projection may collide:

```text
many states may share E_1;
many states may share E_2.
```

But they cannot share the same ordered pair of copies.

---

## 7. Universal Hall target

Let `mathcal S` be any finite family of recursive embedded states. Construct a capacitated incidence system in which each state may send its demand to physical pairs in either `E_1(s)` or `E_2(s)`, with every physical pair receiving at most its one reciprocal-gap capacity after earlier allocations are subtracted.

The desired theorem is the Hall inequality

```math
\boxed{
\sum_{s\in\mathcal F}\operatorname{debt}(s)
\le
J\!\left(
\bigcup_{s\in\mathcal F}
(E_1(s)\cup E_2(s))
\right)
}
```

for every subfamily `mathcal F`, under the four-AP-free double-affine geometry.

The present theorem proves all singleton Hall inequalities with strict surplus and proves injectivity before projection. What remains is to use four-AP-freeness to control simultaneous collisions of both projections.

---

## 8. Relation to known unbounded reuse

The unbounded latent-pair construction permits arbitrarily many child states to share one latent root configuration. In double-copy language this creates high multiplicity in one projection, while the reflected or translated second copies vary with the references.

Therefore unbounded one-copy reuse is not a counterexample to the two-choice formulation. It is the motivating extremal case:

```text
shared first copy
    -> distinct second copies carrying the repeated demand.
```

A genuine counterexample must force simultaneous capacity congestion in both affine projections.

---

## 9. Strategic consequence

The universal recursive-heavy problem is narrower than a general path-packing problem. It is a two-choice affine pair-energy orientation problem with:

1. two individually sufficient resource neighborhoods per state;
2. strict gap descent in the first copy;
3. nonincreasing gap scale in the adjacent second copy;
4. an injective ordered double lift;
5. forbidden four-AP rectangle ratios;
6. lower-scale reference-difference reserves whenever one projection repeats.

The exact `S7` frontier already packs using only first-copy horizontal pairs. The universal theorem may use the second copy precisely where first-copy Hall fails.