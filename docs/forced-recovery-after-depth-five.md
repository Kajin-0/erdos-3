# Finite forced recovery after the depth-five contaminated burst

## Status

Exact finite computer-assisted result.

This note continues the contaminated-backbone chain ending at

```math
S_5\subseteq[32768,65536),
\qquad
|S_5|=1092.
```

It proves that the cheap burst cannot continue immediately at dyadic scale factor `2` or `4`. It then selects the first valid exact-backbone factor-eight recovery and proves that the recovered state again admits no factor-`2` or factor-`4` continuation.

The result is finite. It does not prove a universal recovery theorem for every contaminated genealogy or every factor-eight continuation.

**Verifier:** `src/verify_forced_recovery_after_depth5.py`.

**Certificate:** `data/forced_recovery_after_depth5_certificate_2026-07-11.txt`.

---

## 1. Search model

Let

```math
S\subseteq[L,2L)
```

be a recorded replay state and put

```math
A=\{0\}\cup S.
```

For an integer separation `R`, form

```math
G_R
=
A\cup(A+R)\cup(A+2R).
```

A candidate is accepted only if:

1. `v_2(R)` is even, giving the coordinated left-sponsor orientation;
2. the three translate layers are disjoint;
3. `G_R` is four-term-progression-free;
4. `G_R` fits below the requested next dyadic scale `L'`;
5. the backbone shell
   ```math
   G_R\cap[L,2L)
   ```
   contains the replay state `S`.

The fit condition gives the finite candidate bound

```math
R
\le
\left\lfloor
\frac{L'-1-\max S}{2}
\right\rfloor.
```

Thus every search below is finite and exhaustive within the stated model.

---

## 2. No cheap continuation from `S_5`

The depth-five state has

```math
L_5=32768,
\qquad
|S_5|=1092,
\qquad
\min S_5=32768,
\qquad
\max S_5=63668.
```

Its canonical hash is

```text
a315deca0997d946ca9bb5058d2a04bfe3e585332d4db5260e7d9edc9142f841
```

### Factor two

For

```math
L'=2L_5=65536,
```

the fit bound is

```math
R\le933.
```

There are exactly `622` positive candidates in this range with even `v_2(R)`. None satisfies all acceptance conditions:

```math
\boxed{N_{5,2}=0.}
```

### Factor four

For

```math
L'=4L_5=131072,
```

the fit bound is

```math
R\le33701.
```

There are exactly `22467` sponsor-compatible candidates. None is valid:

```math
\boxed{N_{5,4}=0.}
```

Consequently every continuation of this recorded state in the standard-dyadic disjoint three-translate replay model must have

```math
\boxed{L'/L_5\ge8.}
```

This is a finite forced-recovery statement for `S_5`; it is not a universal theorem for arbitrary contaminated states.

---

## 3. First exact factor-eight recovery

Exact backbone reproduction requires

```math
G_R\cap[L_5,2L_5)=S_5.
```

In particular, it is enough to take `R>=2L_5`. Exhaustive checking of sponsor-compatible exact candidates from `2L_5` upward shows that the first valid one is

```math
\boxed{R_5^*=65547.}
```

For this separation,

```math
G_6
=
(\{0\}\cup S_5)
\cup
(\{0\}\cup S_5+65547)
\cup
(\{0\}\cup S_5+2\cdot65547)
```

is four-term-progression-free, has `3279` points, and satisfies

```math
0\le G_6\le194762<262144.
```

The raw-state hash is

```text
fd54f32a858cf81b0236aa992447d99d91710193623948cb23ecf77466a2660c
```

Define

```math
S_6=262144+G_6.
```

Then

```math
S_6\subseteq[262144,524288),
\qquad
|S_6|=3279,
```

with hash

```text
ff10f8482f475206eba84c4cbbcef48ec0402ec1870edf81575495b9aae7d463
```

and exact backbone identity

```math
G_6\cap[32768,65536)=S_5.
```

---

## 4. No immediate cheap continuation from the recovered state

The recovered state has

```math
L_6=262144,
\qquad
\max S_6=456906.
```

### Factor two

The finite search range is

```math
R\le33690.
```

Among the `22459` candidates with even `v_2(R)`, none is valid:

```math
\boxed{N_{6,2}=0.}
```

### Factor four

The finite search range is

```math
R\le295834.
```

Among the `197222` sponsor-compatible candidates, none is valid:

```math
\boxed{N_{6,4}=0.}
```

Therefore any further continuation from this selected recovered state either terminates or must again have dyadic scale factor at least `8`.

---

## 5. Two-generation weighted-density compensation

Let

```math
W_h
=
P_h^{\mathrm{cert}}\frac{|S_h|}{L_h}.
```

At depth five,

```math
W_5
=
32\frac{1092}{32768}
=
\frac{273}{256}.
```

The selected factor-eight recovery gives

```math
W_6
=
64\frac{3279}{262144}
=
\frac{3279}{4096},
```

so

```math
\boxed{
\frac{W_6}{W_5}
=
\frac{1093}{1456}
\approx0.750687.
}
```

For any disjoint three-translate continuation of `S_6`, cardinality changes from `3279` to

```math
3(3279+1)=9840
```

and certified persistence doubles. Since factors `2` and `4` are impossible, any continuation has scale factor `c_6>=8`. Hence

```math
\frac{W_7}{W_6}
=
\frac{6}{c_6}
\left(1+\frac1{3279}\right)
\le
\frac{820}{1093}.
```

Combining the two generations,

```math
\boxed{
\frac{W_7}{W_5}
\le
\frac{1093}{1456}
\cdot
\frac{820}{1093}
=
\frac{205}{364}
\approx0.563187.
}
```

Equivalently, if a seventh state exists in this model,

```math
\boxed{
W_7\le\frac{615}{1024}.
}
```

Thus the selected recovery path forces at least a `43.7%` reduction in multiplicity-weighted density over the two generations after the cheap depth-five burst.

---

## 6. Consequences

This result supplies the first explicit finite compensation block after the contaminated-backbone growth segment:

```math
4,8,4,4
\quad\longrightarrow\quad
8,\ge8
```

along the selected exact recovery.

It establishes:

1. the depth-five cheap burst cannot extend immediately with factor `2` or `4`;
2. the first exact factor-eight recovery is explicit and certified;
3. the selected recovered state also cannot extend with factor `2` or `4`;
4. any next continuation contracts multiplicity-weighted density enough that the two recovery generations reduce `W` by a factor at most `205/364`.

It does **not** establish:

1. that every factor-eight continuation from `S_5` has the same recovery property;
2. that every contaminated burst is followed by two expensive generations;
3. a uniform long-run average scale factor exceeding `6`;
4. convergence of the full reciprocal-mass recursion.

---

## 7. Revised immediate target

The next computational target is to classify all valid factor-eight continuations of `S_5` by whether they admit a factor-two or factor-four successor.

The next proof target is a state-independent recovery principle: quantify a contamination debt accumulated during cheap steps and prove that it must be repaid by termination, expensive scale jumps, exportable difference structure, or a forbidden four-term progression.
