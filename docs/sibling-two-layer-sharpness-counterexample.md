# Sibling two-layer algebraic sharpness precursor

## Corrected status

This 31-element construction is an explicit algebraic overlap between:

1. a middle multiplicity-fiber child;
2. a spanning-forest component child.

It proves that the proposed universal intersection statement

```math
A_r^+\cap C^+\text{ is always three-term-progression-free}
```

is false.

However, the middle-fiber progression displayed below is

```math
15,33,51,
```

whose largest-to-smallest ratio exceeds two. It does not survive a single ratio-two shell. Therefore this file must not be cited by itself as a recursive terminal-duplication counterexample after dyadic shell decomposition.

The shell-compatible recursive sharpness construction is now:

```text
docs/dyadic-shell-compatible-sibling-sharpness.md
```

with verifier:

```text
src/verify_dyadic_shell_sibling_sharpness.py
```

---

## 1. Parent set

Take

```math
\begin{aligned}
D=\{&309,324,342,360,365,386,419,434,438,440,452,453,460,466,470,475,\\
&490,494,498,510,514,515,529,540,543,544,550,560,562,580,585\}.
\end{aligned}
```

A direct exhaustive check shows that `D` is four-term-progression-free.

---

## 2. Valid deletion sequence

Use the coordinated side-anchor deletion sequence

```text
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

At every deletion, both surviving points of the selected progression remain present.

The chosen forest edges listed in the companion verifier form one rooted spanning tree. Its numerical minimum is `309`.

---

## 3. Middle-fiber overlap

The selected step `110` has centers

```math
419,434,452,470
```

in the relevant subfamily. Translating by the minimum center gives

```math
\Xi_{110}=\{15,33,51\},
```

which contains a three-term progression of step `18`.

The corresponding nonrepresentative sponsors are

```math
544,562,580.
```

Translating the spanning component by its numerical minimum `309` gives

```math
235,253,271,
```

also a three-term progression of step `18`.

Thus the same algebraic step occurs in both child constructions before shell resolution.

---

## 4. Exact conclusion

This example proves:

```math
\boxed{
A_r^+\cap C^+\text{ need not be three-term-progression-free.}
}
```

It does not alone prove that both progressions are processed as recursive terminal events under ratio-two shell decomposition.

The augmented and scaled 34-element construction in

```text
docs/dyadic-shell-compatible-sibling-sharpness.md
```

repairs that interface and proves genuine two-layer terminal duplication in standard dyadic shells.

---

## 5. Reproducibility

The companion script

```text
src/verify_sibling_two_layer_sharpness.py
```

checks the original algebraic overlap. The shell-compatible verifier is

```text
src/verify_dyadic_shell_sibling_sharpness.py
```.