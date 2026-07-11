# Dyadic-shell-compatible sibling two-layer sharpness

## Status

Exact correction and strengthening of the earlier sibling sharpness example.

The earlier 31-element gadget proved an algebraic overlap between a middle multiplicity-fiber child and a spanning-forest component child. However, one of the two displayed three-term progressions crossed every ratio-two shell and therefore did not by itself certify duplicated terminal production after dyadic shell decomposition.

This note gives a 34-element four-term-progression-free root block for which both copies of the duplicated terminal step survive standard power-of-two shelling.

---

## 1. Base set

Start with the earlier 31-element set

```math
\begin{aligned}
D_0=\{&309,324,342,360,365,386,419,434,438,440,452,453,460,466,470,475,\\
&490,494,498,510,514,515,529,540,543,544,550,560,562,580,585\}.
\end{aligned}
```

Adjoin one additional selected progression of step `110`:

```math
284,
\qquad 394,
\qquad 504.
```

Because

```math
v_2(110)=1,
```

the coordinated side anchor is the right endpoint `504`, the center is `394`, and the opposite endpoint is `284`.

Put

```math
D_1=D_0\cup\{284,394,504\}.
```

A direct exhaustive check shows that `D_1` is four-term-progression-free.

---

## 2. Scale and translate into one standard dyadic block

Define

```math
D=13D_1+4500.
```

Since `13` is odd, multiplication by `13` preserves the parity of every two-adic valuation and therefore preserves every coordinated side-anchor orientation.

The minimum and maximum of `D` are

```math
8192
\qquad\text{and}\qquad
12105.
```

Hence

```math
\boxed{D\subseteq[8192,16384).}
```

Affine scaling and translation preserve four-term-progression-freeness, so `D` is four-term-progression-free.

---

## 3. Valid deletion sequence

Use the base-coordinate deletion sequence

```text
(504,110),
(494,54),
(386,52),
(490,25),
(515,35),
(540,20),
(585,110),
(440,13),
(560,50),
(453,45),
(466,48),
(514,15),
(529,110),
(544,110),
(562,110),
(580,110).
```

After applying `x -> 13x+4500` to sponsors and multiplying every common difference by `13`, this is a valid coordinated side-anchor deletion sequence in `D`.

The five old selected occurrences of step `110` and the new occurrence at sponsor `504` become selected occurrences of step

```math
R=1430.
```

Their base-coordinate centers are

```math
394,
\quad 475,
\quad 419,
\quad 434,
\quad 452,
\quad 470.
```

The minimum center is `394`.

---

## 4. Middle multiplicity-fiber shell

The full center-difference fiber for selected step `110` in base coordinates is

```math
\{25,40,58,76,81\}.
```

After scaling by `13`, the middle multiplicity-fiber child contains

```math
\{325,520,754,988,1053\}.
```

Its standard dyadic shell

```math
[512,1024)
```

contains

```math
520,
\qquad 754,
\qquad 988.
```

These form a three-term progression of common difference

```math
q=234.
```

Thus the shell-resolved middle child genuinely emits terminal step `234`.

---

## 5. Spanning-component shell

Keep the original spanning-tree component on the translated copy of `D_0`. Its numerical minimum is the image of `309`.

The old nonrepresentative sponsors

```math
544,
\qquad 562,
\qquad 580
```

have component-translation coordinates

```math
235,
\qquad 253,
\qquad 271
```

in base scale. After multiplying by `13`, the component child contains

```math
3055,
\qquad 3289,
\qquad 3523.
```

All three lie in the standard dyadic shell

```math
[2048,4096)
```

and form a three-term progression of the same common difference

```math
q=234.
```

Thus the shell-resolved spanning-component child also emits terminal step `234`.

---

## 6. Consequence

The same parent block produces terminal numerical label `234` in two distinct sibling branches after standard dyadic shell decomposition:

1. a middle multiplicity-fiber shell;
2. a spanning-forest component shell.

Therefore the sibling two-layer theorem is genuinely sharp in the actual recursive scheme, not merely before shell resolution.

The corrected conclusion is

```math
\boxed{
\text{one-layer sibling collapse is false even after standard dyadic shelling.}
}
```

---

## 7. Status of the earlier example

The earlier 31-element example remains a valid algebraic overlap certificate. Its middle-fiber progression

```math
15,33,51
```

has ratio greater than two and does not survive a single ratio-two shell. It should therefore not be cited alone as a recursive terminal-duplication example.

The present 34-element scaled construction supersedes it for all statements involving recursive terminal production.