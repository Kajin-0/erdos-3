# GT31 extracted parameter rows

## Status

Concrete rows extracted from Green--Tao Part III.  These are proof-audit rows, not a new theorem.

## Extracted rows

| Stage | Extracted bound | Interpretation |
|---|---|---|
| Reachable-path length | k <= 8 eta^{-2 C2} | The refinement process is allowed polynomially many steps in eta^{-1}. |
| Linear dimension | d1(v) <= 8 eta^{-3 C2} | Local frequency complexity grows polynomially in eta^{-1}. |
| Quadratic dimension | d2(v) <= 8 eta^{-2 C2} | Quadratic complexity also grows polynomially in eta^{-1}. |
| Radius | rho(v) >= exp(-eta^{-2 C5}) | Radius loss is already exponential in a polynomial of eta^{-1}. |
| Volume | vol(v) <= exp(eta^{-2 C3}) | Volume/thickness bookkeeping has exponential polynomial cost. |
| Waste | waste(v) <= eta^{C3/2} | Error waste remains polynomially small. |
| Energy decrement step | Energy(v') <= Energy(v)-eta^{C2} | Bad approximation forces polynomial energy decrease. |
| Step complexity cost | d(v') <= d(v)+eta^{-C2} | Each energy-decrement step adds polynomial frequency complexity. |
| Radius step cost | rho(v') >= exp(-eta^{-C5}) rho(v) | Each refinement multiplies radius by an exponential polynomial factor. |
| Volume step cost | vol(v') <= exp(eta^{-C3}) vol(v) | Each refinement increases volume by an exponential polynomial factor. |
| Thickness corollary | P(r_v=0) << exp(eta^{-C5^2})/p | The final r=0 bound is controlled by accumulated radius/dimension/Bohr thickness. |

## Interpretation

The eta^{-O(1)} in the thickness term is not just an abstract byproduct of a few Cauchy--Schwarz squarings.  The visible path contains polynomially many refinement steps and exponential radius/volume losses depending on eta^{-1}.

The main candidate bottleneck is therefore structural: dimension growth plus Bohr radius/thickness loss under repeated refinement.

## Consequence for the reciprocal-sum target

The reciprocal-sum route needs an effective bound

```math
P(r=0) << exp(-c eta^{-gamma})/p
```

with gamma < 1/4.

The extracted rows show that the published proof has constants C2,C3,C5 arranged so that the final hidden gamma is some large positive constant, not obviously close to 1/4.  Any improvement attempt must reduce the radius/thickness exponent, not merely remove cosmetic losses.

## Next audit target

Trace exactly how C2,C3,C5 are chosen and ordered.  The key question becomes:

```math
Can the path length, dimension growth, and radius shrinkage be reorganized so that the final thickness exponent gamma is below 1/4?
```
