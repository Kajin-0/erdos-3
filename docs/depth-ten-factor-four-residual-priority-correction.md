# Correction: active `S_10` factor-four residual

## Status

Research-program correction.

The exact lifted `S_9` completion theorem was already present in the repository but was omitted from the later obstruction-coverage overview. It is valid and must be distinguished from the subsequently rejected anchor reduction.

---

## Certified reduction

The genuinely new layer-disjoint factor-four domain from `S_10` has

```math
314986450
```

candidates.

The certified lifted completion support removes

```math
137142200
```

of them, leaving the exact residual count

```math
\boxed{177844250}.
```

The residual begins at

```text
R = 97474324
```

and ends at

```text
R = 613454687.
```

Its ordered-list FNV-64 hash is

```text
00369694f2d70526
```

Primary references:

- `docs/depth-ten-lifted-s9-completion-reduction.md`;
- `src/verify_depth10_lifted_s9_completion.cpp`;
- `src/run_verify_depth10_lifted_s9_completion.sh`;
- `data/depth10_lifted_s9_completion_certificate_2026-07-12.txt`.

---

## Distinction from the invalid anchor rule

The lifted-completion reduction is an explicit structural-witness theorem. It transports certified depth-nine completion coordinates and completion-to-base differences through the three embedded `A_9` copies.

The later exploratory anchor rule attempted to reduce

```math
177844250
```

to a much smaller set using only relations of the form `x=3d` and `R=s-d` or `2R=s-d`. That rule did not itself construct four equally spaced points and remains rejected.

Therefore the rigorous status is:

```text
valid residual after inherited interval and lifted completion: 177844250
invalid further anchor reduction:                              rejected
```

---

## Relation to the rectangle-transport profile

The `128`-sample top-quartile rectangle certificate in

`docs/depth-ten-factor-four-rectangle-transport-profile.md`

was sampled from the full genuinely new domain before filtering by lifted completion. Its exact `k=4` transport lemma remains state-independent and valid, and all `128` stored witnesses are correct. However, the sample may include candidates already removed by lifted completion.

Consequently it is theorem-discovery evidence about the upper domain, not yet a profile of the rigorous `177844250`-candidate residual.

---

## Correct next target

The next computation should:

1. regenerate the exact lifted-completion residual;
2. select equal-rank samples from those `177844250` candidates;
3. classify their witnesses by outer word `lambda`, parent word `mu`, and affine effective separation;
4. measure how much of the residual is covered by the exact `k=4` rectangle transport channel;
5. compute the remaining zero set before proposing another bulk reduction.

No further sequential prefix certification is needed.
