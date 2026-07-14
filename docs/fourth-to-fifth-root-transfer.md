# Fourth-to-fifth root-lineage transfer

## Purpose

The fifth-generation failure shows that current-generation repeated-root mass is not persistent capacity. At the fourth and fifth recursive levels, every retained recursive point has a distinct original `S7` root provenance.

The relevant question is therefore not how repeated roots branch, but how harmonic mass changes along **unique surviving root lineages**.

## General identity

Let `F_g` be a retained recursive family whose points carry inherited root provenance. For each root `p`, let

```math
D_g(p)=\{u\in F_g:\operatorname{root}(u)=p\}.
```

Suppose every active root occurs once at generations `g` and `g+1`. Write `u_g(p)` for the unique current label. Partition the roots active at generation `g` into:

```text
S = roots that survive recursively to generation g+1
E = roots that exit the recursive family.
```

Because provenance is inherited, generation `g+1` cannot introduce a new root. Therefore

```math
\begin{aligned}
H_{g+1}^{\mathrm{rec}}-H_g^{\mathrm{rec}}
&=
\sum_{p\in S}
\left(
\frac1{u_{g+1}(p)}-
\frac1{u_g(p)}
\right)
-
\sum_{p\in E}\frac1{u_g(p)}.
\end{aligned}
```

Define

```math
G_{g\to g+1}
=
\sum_{p\in S}
\left(
\frac1{u_{g+1}(p)}-
\frac1{u_g(p)}
\right)
```

and

```math
L_{g\to g+1}
=
\sum_{p\in E}\frac1{u_g(p)}.
```

Then

```math
\boxed{
H_{g+1}^{\mathrm{rec}}-H_g^{\mathrm{rec}}
=G_{g\to g+1}-L_{g\to g+1}.
}
```

This is an exact lineage-transfer identity. It does not fit a potential or assume a particular coefficient.

## Certified fourth-to-fifth decomposition

For the baseline retained transition:

```text
fourth recursive roots = 1,717
surviving recursive roots = 1,015
exiting recursive roots = 702
```

The exiting roots split as:

```text
exit to fifth-generation terminal output = 17
exit from the retained family entirely = 685
```

No root appears in both fifth recursive and fifth terminal output. Across the complete fifth retained family:

```text
repeated root labels = 0
maximum root multiplicity = 1.
```

The exact mass decomposition is

```text
surviving-lineage scale gain = 1.816777911848...
exiting parent release        = 1.310139720502...
recursive mass increase       = 0.506638191346...
```

and

```math
\boxed{
1.816777911848\ldots
-
1.310139720502\ldots
=
0.506638191346\ldots
}
```

The scale-gain-to-release ratio satisfies

```math
\boxed{
\frac{277341}{200000}
<
\frac{G_{4\to5}}{L_{4\to5}}
<
\frac{693353}{500000}
}
```

or

```text
G_4→5 / L_4→5 = 1.386705466156...
```

The 17 terminalized roots release only `0.330617984540...` of fourth recursive parent mass but generate `2.043863226048...` of first-appearance terminal mass. That terminal mass belongs in the separate terminal ledger; it is not recursive debt.

## Structural conclusion

The fourth-to-fifth recursive expansion is caused by scale contraction along unique surviving lineages:

```text
unique-lineage scale gain > released parent mass.
```

It is not caused by repeated-root multiplicity, because repeated-root multiplicity is absent on both sides of the transition.

This eliminates current-generation multiplicity as the primary missing mechanism. A viable whole-tree potential must retain information about the future scale-gain capacity of an ancestor path and release that capacity when the path:

1. terminates into a first-appearance terminal token;
2. is removed by the retained quotient;
3. creates completion or rectangle obstruction;
4. or otherwise loses the ability to contract further.

The next theorem target is therefore a cumulative ancestor-path capacity `A` satisfying a transition inequality of the form

```math
H_{g+1}^{\mathrm{rec}}
+A_{g+1}
+T_{g+1}^{\mathrm{first}}
\le
H_g^{\mathrm{rec}}
+A_g
+\Phi_{\mathrm{obs},g}
+\varepsilon_g,
```

where `A` is defined independently of a finite fitted transition matrix.

## Reproduction

```bash
python3 src/run_exact_python.py \
  src/verify_fourth_to_fifth_root_transfer.py \
  /tmp/fourth_to_fifth_root_transfer_certificate.txt

cmp \
  data/fourth_to_fifth_root_transfer_certificate_2026-07-14.txt \
  /tmp/fourth_to_fifth_root_transfer_certificate.txt
```

Recorded certificate SHA-256:

```text
460bbf1a5b21a662353041b8e576fc8809a4823553fa63cc8ae7dc9ce469564a
```
