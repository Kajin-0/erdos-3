# Scale-normalized provenance mass

## Status

Exact finite two-generation theorem for the retained `S_7` local-optimum family.

For every retained point, let:

- `u` be its current numerical label;
- `p` be its root provenance label in the original `S_7` transition.

Define

```math
K(R)
=
\sum_{(u,p)\in R}
\frac{u}{p}\frac1u.
```

Pointwise,

```math
\frac{u}{p}\frac1u=\frac1p,
```

so `K` is exactly root-provenance occurrence mass. The factor `u/p` removes the harmonic growth caused solely by contraction from `p` to `u`.

**Verifier:** `src/verify_scale_normalized_provenance_mass.py`.

**Certificate:** `data/scale_normalized_provenance_mass_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
15824a4eb3a07b3a6d4a620446b2e518d358a27dbb518079af96d57dc65c74fa
```

---

## 1. Exact contraction after scale normalization

Let `K_1` and `K_2` be the scale-normalized provenance masses of the first and second retained generations.

Exact arithmetic gives

```math
\boxed{
\frac{644}{1000}
<
\frac{K_2}{K_1}
<
\frac{645}{1000}
}.
```

Thus exact `u/p` normalization changes the raw retained harmonic ratio from approximately `6.82863` to approximately `0.64422`.

This confirms that the large raw growth is predominantly a scale-contraction effect rather than provenance multiplicity alone.

---

## 2. Persistence remains unpaid

If the recursive branch carries a factor-two persistence weight, the normalized ratio becomes

```math
\boxed{
\frac{1288}{1000}
<
2\frac{K_2}{K_1}
<
\frac{1289}{1000}
}.
```

The excess over the first-generation capacity is therefore between `28.8%` and `28.9%` of `K_1`.

Scale normalization removes the raw harmonic expansion, but it does **not** by itself pay the persistence increase.

---

## 3. Interpretation

The candidate coordinate

```math
K(R)=\sum_{(u,p)\in R}\frac1p
```

has three useful properties:

1. it is exactly provenance-aware;
2. it is invariant under the numerical contraction from `p` to `u` for each occurrence;
3. it contracts in the recorded unweighted propagation.

But it is not yet a Bellman potential. With the expected factor-two persistence, the recorded transition still expands.

A closing coordinate must combine `K` with at least one source of repayment:

```text
completion or affine obstruction credit
future cheap-extension exclusion
terminal residual credit
bounded multi-generation provenance reuse.
```

The exact missing payment on this propagation is the positive quantity

```math
2K_2-K_1,
```

whose ratio to `K_1` lies between `0.288` and `0.289`.

This provides a concrete target for the next obstruction calculation rather than another unconstrained policy search.