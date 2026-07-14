# Retained provenance scale profile

## Status

Exact finite two-generation theorem for the certified retained `S_7` family.

The calculation uses exactly the same objects as `docs/retained-provenance-second-generation.md`:

- the `21` first-generation point-disjoint retained states from policy `local37`;
- lexicographic coordinated deletion on each retained state;
- global exact-state quotienting;
- the same maximum-harmonic point-conflict rule;
- the resulting `27` second-generation retained states and `7,925` retained points.

For every retained descendant point `u`, the certificate records its original `S_7` root-provenance label `p`, its immediate provenance, retained state, source type, source step, and dyadic shell.

**Verifier:** `src/verify_retained_provenance_scale_profile.py`.

**Certificate:** `data/retained_provenance_scale_profile_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
a38089295cec338b9155ea15bccff0a70dd55f1fea46c4a8deb2e13f390fd012
```

---

## 1. Exact scale records

The canonical point-level record contains `7,925` rows and `1,287,870` bytes, with SHA-256

```text
904b0b9f8906d196ea02369cb60153341eda5a562340ba8615dbcdb769dc92e3.
```

For each pair `(p,u)`, define

```math
d_{\rm shell}(p,u)
=
\lfloor\log_2p\rfloor-\lfloor\log_2u\rfloor,
```

and the exact integer lower and upper logarithmic contractions

```math
d_-(p,u)=\left\lfloor\log_2\frac pu\right\rfloor,
\qquad
d_+(p,u)=\left\lceil\log_2\frac pu\right\rceil.
```

The observed contraction range is

```math
\frac{505417}{112004}
\le
\frac pu
\le
1354066.
```

The largest contraction is the middle-fiber point

```text
u = 1,
p = 1,354,066,
source step = 5.
```

It has `d_-=20` and `d_+=21`.

---

## 2. Unit depth and logarithmic charges fail

Let

```math
H_1=\text{first retained harmonic mass},
\qquad
H_2=\text{second retained harmonic mass},
```

and let the intergeneration debt be

```math
D=H_2-H_1.
```

Weight scale contraction at the root label by

```math
C_{\rm shell}
=
\sum_{(p,u)}\frac{d_{\rm shell}(p,u)}p,
```

```math
C_-
=
\sum_{(p,u)}\frac{d_-(p,u)}p,
\qquad
C_+
=
\sum_{(p,u)}\frac{d_+(p,u)}p.
```

Exact arithmetic gives

```math
86
<
\frac{D}{C_{\rm shell}}
<
87,
```

```math
99
<
\frac{D}{C_-}
<
100,
```

and even for the optimistic upper logarithmic charge,

```math
77
<
\frac{D}{C_+}
<
78.
```

Therefore a unit dyadic-depth charge, a unit floor-log charge, and a unit ceil-log charge all fail by large factors. Any charge of the form

```math
\kappa\sum_{(p,u)}\frac{\log_2(p/u)}p
```

would require `kappa>77` on this recorded transition, even before proving that such stored capacity is reusable or monotone.

---

## 3. Repeated provenance contains the scale tail

The retained point family has:

```text
272 repeated root-provenance labels
549 retained occurrences carrying repeated provenance
7,376 retained occurrences carrying unique provenance.
```

The concentration is exact:

```math
d_-(p,u)\ge 8
\quad\Longrightarrow\quad
p\text{ is repeated provenance}.
```

There are `196` retained points with `d_- >= 8`, and only `4` with `d_- >= 16`.

Repeated provenance carries only

```math
0.076
<
\frac{H_{\rm root,repeat}}{H_{\rm root,all}}
<
0.077
```

of occurrence-weighted root mass, but it produces

```math
0.948
<
\frac{H_{\rm descendant,repeat}}{H_2}
<
0.949
```

of the retained descendant harmonic mass.

Its descendant-to-root expansion satisfies

```math
4928
<
\frac{H_{\rm descendant,repeat}}{H_{\rm root,repeat}}
<
4929,
```

whereas unique provenance satisfies only

```math
22
<
\frac{H_{\rm descendant,unique}}{H_{\rm root,unique}}
<
23.
```

Thus the dangerous harmonic growth is highly localized: repeated root provenance has a small root-mass footprint but carries almost the entire descendant harmonic output.

---

## 4. Tail concentration

The points with at least eight binary orders of contraction contribute

```math
0.943
<
\frac{H_2[d_-\ge8]}{H_2}
<
0.944.
```

The four points with at least sixteen orders contribute

```math
0.698
<
\frac{H_2[d_-\ge16]}{H_2}
<
0.699.
```

The single point with `d_-=20`, namely `u=1`, contributes

```math
0.512
<
\frac{1}{H_2}
<
0.513.
```

More than half of the entire second retained harmonic mass therefore lies in one repeated-provenance descendant point.

---

## 5. Consequence for the proof program

The previous theorem showed that provenance multiplicity is modest while harmonic mass expands by `6.828`–`6.829`. The new profile identifies where that expansion resides:

```text
repeated provenance × extreme scale contraction.
```

This rules out treating either coordinate independently:

- multiplicity alone misses the factor-of-thousands expansion on repeated labels;
- depth or logarithmic contraction alone requires a coefficient greater than `77`;
- an unconditioned root-occurrence charge is weaker still, since `H_2/H_root` lies between `399` and `400`.

The next finite Bellman feature should be tail-sensitive and provenance-aware, for example a charge supported only when a root label is reused and its descendant crosses a specified dyadic-depth threshold. Such a feature remains a candidate until it is shown to be stored, bounded under further propagation, and compatible with obstruction credit.

This theorem is finite and path-specific. It does not establish whole-tree contraction or validate any particular scale-aware potential globally.
