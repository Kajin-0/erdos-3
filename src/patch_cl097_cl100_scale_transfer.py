#!/usr/bin/env python3
"""Record CL-097 through CL-100 after the collision-frontier patch."""
from __future__ import annotations

from pathlib import Path

import patch_cl089_cl096_collision_frontier as base

ROOT = Path(__file__).resolve().parents[1]

CL096 = "| CL-096 | Fixing one transported parent three-AP `T` and one child type, all colliding child witness progressions are exactly three affine translates of the collision reference set: side `(R_T+T)/2`, middle `2R_T-T`, doubled side `2T-R_T`. The fixed-step witnesses are pairwise disjoint, so the forced layer family has size `3|R_T|`; child witness-edge occurrence energy is respectively `2mE(T)`, `mE(T)`, or `(m/2)E(T)`. | Symbolic collision-fiber theorem. The active target is weighted three-translate exposure, not constant multiplicity. |"
CL097 = "| CL-097 | If one oriented root configuration `Q` of span `Delta` is carried by `m` references inside a shell `[M,2M)`, the references lie in an interval of length `<M-Delta`. The translated positive reference-difference set `D(R)` is four-AP-free, lies strictly below scale `M`, and satisfies `(m-1)/D_e < ((M-Delta)/D_e)H(D(R))` for every repeated pair gap `D_e` in `Q`. For a root three-AP of step `d`, `(m-1)J(Q) < (5/2)(M/d-2)H(D(R))`. | Symbolic lower-scale reference-gap collision-charge theorem. Reuse of the reserve across configurations remains open. |"
CL098 = "| CL-098 | Every extra occurrence of a physical pair `e` under references `r_0,r` determines an affine completion rectangle and the exact aspect identity `w(e)=(|r-r_0|/|e|)w({r_0,r})`. Side, middle, and doubled rectangles exclude the aspect gaps `{D,4D}`, `{D/4,D}`, and `{D/2,2D}` respectively. Choosing one base reference makes extra branches injective rectangle tokens. | Symbolic pointwise collision-rectangle theorem. Whole-tree rectangle-token reuse remains open. |"
CL099 = "| CL-099 | For a fixed full-edge child type, completion transport preserves weighted three-AP load with coefficients `alpha_side=1/2`, `alpha_middle=1`, `alpha_double=2`: `alpha_t/d(Q)=1/h(T)`. Hence `alpha_t sum_C L_3(C) <= L_3(P)+X_t`, where `X_t=sum_T(m_t(T)-1)_+/h(T)` is exactly a first-appearance rectangle-aspect collision ledger. | State-independent type-weighted three-AP transport row. A three-type scalar allocation is supplied by CL-100. |"
CL100 = "| CL-100 | Weighting a child three-AP by its shell base gives one scalar first-appearance allocation. For a parent target of step `h` in base `N`, first side, middle, and doubled preimages consume at most `N/(2h)`, `N/(4h)`, and `N/(4h)`, exactly partitioning parent capacity `N/h`. Thus scale-weighted load `Psi_1=sum M(C)L_3(C)` is critical: first appearances satisfy `Psi_1<=N L_3(P)`. More generally `Psi_p<=c_pN^pL_3(P)` with `c_p=3/4^p+1/2^{p+1}`, so `c_1=1` and `c_p<1` for `p>1`; collision excess is the sole unresolved term. | Symbolic scale-critical three-AP Bellman row. Global summability of collision exposure is open. |"

SECTION = r"""## Scale-critical three-AP transfer

The collision frontier admits an exact scalar first-appearance allocation.
For a child three-AP `Q` transported to a parent target `T`, use

```math
\alpha_{\rm side}=\frac12,
\qquad
\alpha_{\rm middle}=1,
\qquad
\alpha_{\rm double}=2.
```

Then

```math
\frac{\alpha_t}{d(Q)}
=
\frac1{d(T)}.
```

For one fixed type this gives

```math
\alpha_t\sum_C\mathcal L_3(C)
\le
\mathcal L_3(P)+X_t,
```

where `X_t` is exactly the excess target multiplicity written as
rectangle-aspect tokens.

Shell scale removes the apparent triple spending. Weight each child witness by
`M(C)/d(Q)`. For a parent target of step `h` in a block of base `N`, one first
preimage of each type costs at most

```math
\frac{N}{2h},
\qquad
\frac{N}{4h},
\qquad
\frac{N}{4h}.
```

Therefore

```math
\boxed{
\Psi_1(\text{first child witnesses})
\le
N\mathcal L_3(P).
}
```

At general scale moment `p`, the first-appearance coefficient is

```math
c_p
=
\frac3{4^p}
+
\frac1{2^{p+1}}.
```

The exponent-one row is exactly critical and every `p>1` row contracts before
collision excess.

Unbounded collision multiplicity is transferred to a strictly lower-scale
reference reserve. If one root configuration `Q` of span `Delta` is carried by
references `R` in `[M,2M)`, then

```math
\operatorname{diam}(R)<M-\Delta
```

and

```math
D(R)=\{r-r_0:r\in R,\ r>r_0\}
```

is four-AP-free below scale `M`. For every repeated pair gap `D_e`,

```math
\frac{|R|-1}{D_e}
<
\frac{M-\Delta}{D_e}H(D(R)).
```

Pointwise, each extra reference gives the exact rectangle identity

```math
\frac1{D_e}
=
\frac\delta{D_e}\frac1\delta.
```

The sole unresolved scalar term is the scale-critical collision excess
`Y(P)`: reuse of reference-difference and rectangle tokens across distinct
root configurations. This is the next theorem. It is narrower than the former
full pair-activation problem and has explicit first-appearance, scale, and
aspect coordinates.

Primary references:

- `docs/reference-gap-collision-charge.md`;
- `docs/collision-rectangle-aspect-identity.md`;
- `docs/type-weighted-ap-transport.md`;
- `docs/scale-weighted-ap-load-criticality.md`.

---

"""

TARGETS = r"""## 9. Approved next targets

1. Define a first-appearance ledger for collision rectangle tokens `(T,{r_0,r},type,M)` and reference-difference tokens `(delta,D_e,k)`.
2. Prove a bound for the critical excess `Y(P)` in the scale-weighted row, using unused role capacity, strict shell slack, and terminal/external-completion release.
3. Quantify reuse of one reference pair across distinct repeated root configurations; this is now the only unidentified multiplicity layer.
4. Use the exact aspect identity `1/D=(delta/D)(1/delta)` to separate near rectangles, far rectangles, and dyadic aspect bands.
5. Merge sponsor direct/backward/residual targets into the same rectangle/external-completion ledger rather than maintaining a separate scalar pair-energy reserve.
6. Resolve the independent CL-087 generation-consistency audit before using those finite metrics.
7. Do not propagate the corrected second frontier, and do not generate generation six.

The predeclared transfer architecture now exists. Further finite propagation remains deferred because the scale-critical collision excess has not yet been proved summable."""

HISTORY = r"""### Scale-critical three-AP transfer

Completion transport preserves three-AP load after the exact type weights
`1/2,1,2`. Dyadic shell scale then allocates one first preimage of each type
with fractions `1/2,1/4,1/4` of one parent target. The exponent-one
scale-weighted row is exactly critical; all higher scale moments contract
before collision excess.

Unbounded collision multiplicity is converted to a lower-scale four-AP-free
reference-difference set. Each extra branch has an exact completion rectangle
and aspect ratio. The unresolved object is no longer pair activation itself,
but reuse of reference-gap and rectangle tokens across different repeated root
configurations.

"""


def replace_section(text: str, heading: str, next_heading: str, block: str) -> str:
    start = text.find(heading)
    end = text.find(next_heading, start + len(heading))
    if start < 0 or end < 0:
        raise AssertionError(f"cannot locate section {heading!r}")
    return text[:start] + block.rstrip() + "\n\n---\n\n" + text[end:]


def patch_ledger() -> None:
    path = ROOT / "docs/certainty-ledger.md"
    text = path.read_text(encoding="utf-8")
    rows = {CL097, CL098, CL099, CL100}
    text = "\n".join(line for line in text.splitlines() if line not in rows) + "\n"
    if CL096 not in text:
        raise AssertionError("missing CL-096 marker")
    text = text.replace(CL096 + "\n", CL096 + "\n" + "\n".join((CL097, CL098, CL099, CL100)) + "\n", 1)
    marker = "Primary latest references:\n\n"
    refs = (
        "- `docs/reference-gap-collision-charge.md`;\n"
        "- `docs/collision-rectangle-aspect-identity.md`;\n"
        "- `docs/type-weighted-ap-transport.md`;\n"
        "- `docs/scale-weighted-ap-load-criticality.md`;\n"
    )
    for line in refs.splitlines():
        text = text.replace(line + "\n", "")
    if marker not in text:
        raise AssertionError("missing latest-reference marker")
    text = text.replace(marker, marker + refs, 1)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def patch_program() -> None:
    path = ROOT / "docs/current-proof-program.md"
    text = path.read_text(encoding="utf-8")
    heading = "## Scale-critical three-AP transfer"
    next_heading = "## Latest exact refinement: backbone-anchor transfer"
    if heading in text:
        text = replace_section(text, heading, next_heading, SECTION)
    else:
        if next_heading not in text:
            raise AssertionError("missing scale-transfer insertion marker")
        text = text.replace(next_heading, SECTION + next_heading, 1)
    text = replace_section(text, "## 9. Approved next targets", "## 10. Stop list", TARGETS)
    old = "The active program combines terminal stopping, oriented full-edge branching, affine active-pair transport, and dyadic shell descent. The local current-edge coefficient is closed, but recursive latent-pair multiplicity is unbounded. The remaining theorem is a weighted three-translate collision-fiber exposure law, together with external-completion and terminal first-appearance bookkeeping."
    new = "The active program now has a scale-critical three-AP transfer row. First side, middle, and doubled preimages partition one parent target with capacities `1/2,1/4,1/4`; unbounded collisions transfer to lower-scale reference-gap and rectangle-aspect tokens. The remaining theorem is global first-appearance control of the critical collision excess, plus external-completion and terminal release."
    text = text.replace(old, new)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def patch_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    items = [
        "28. a lower-scale reference-gap collision charge for every repeated oriented root configuration;",
        "29. a pointwise rectangle-aspect identity naming the exact resource behind every extra branch;",
        "30. a type-weighted three-AP transport row with coefficients `1/2,1,2`;",
        "31. a scale-critical scalar allocation in which first side, middle, and doubled witnesses consume `1/2,1/4,1/4` of one parent target.",
    ]
    lines = [line for line in text.splitlines() if line not in items]
    text = "\n".join(lines) + "\n"
    marker = "27. a collision-fiber theorem identifying every fixed-witness reuse family as three affine translates of its reference set.\n"
    if marker not in text:
        raise AssertionError("missing README claim-27 marker")
    text = text.replace(marker, marker + "\n".join(items) + "\n", 1)
    old = "Uniform bounded reuse is false: shell-valid latent-pair multiplicity is unbounded. Every fixed-witness collision fiber is instead three affine translates of its reference set, while normalized pair gap grows geometrically along each lineage. The active theorem is a weighted three-translate exposure law that pays branch multiplicity through these forced layers. Generation six and propagation of the corrected second frontier remain blocked."
    new = "Uniform bounded reuse is false, but a scale-critical transfer row now exists. First side, middle, and doubled preimages use `1/2`, `1/4`, and `1/4` of one parent target; every extra preimage becomes a lower-scale reference-gap and rectangle-aspect token. The active theorem is global first-appearance control of this collision excess. Generation six and propagation of the corrected second frontier remain blocked."
    text = text.replace(old, new)
    link_marker = "- [`docs/unbounded-shelled-latent-pair-reuse.md`](docs/unbounded-shelled-latent-pair-reuse.md) — arbitrary one-generation latent-pair multiplicity.\n"
    links = (
        "- [`docs/reference-gap-collision-charge.md`](docs/reference-gap-collision-charge.md) — lower-scale harmonic payment for unbounded reuse.\n"
        "- [`docs/collision-rectangle-aspect-identity.md`](docs/collision-rectangle-aspect-identity.md) — pointwise rectangle token and aspect factorization.\n"
        "- [`docs/type-weighted-ap-transport.md`](docs/type-weighted-ap-transport.md) — first-appearance plus collision three-AP row.\n"
        "- [`docs/scale-weighted-ap-load-criticality.md`](docs/scale-weighted-ap-load-criticality.md) — critical `1/2+1/4+1/4` shell allocation.\n"
    )
    for line in links.splitlines():
        text = text.replace(line + "\n", "")
    if link_marker not in text:
        raise AssertionError("missing README unbounded-reuse link")
    text = text.replace(link_marker, link_marker + links, 1)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def patch_history() -> None:
    path = ROOT / "docs/research-decision-history.md"
    text = path.read_text(encoding="utf-8")
    heading = "### Scale-critical three-AP transfer"
    if heading in text:
        start = text.index(heading)
        end = text.index("**Decisions:**", start)
        text = text[:start] + text[end:]
    marker = "**Decisions:**\n"
    stop = text.find("## 11. Permanent stop list")
    position = text.rfind(marker, 0, stop)
    if position < 0:
        raise AssertionError("missing history decision marker")
    text = text[:position] + HISTORY + text[position:]
    decisions = [
        "- the three full-edge types are allocated by shell-scaled capacities `1/2,1/4,1/4`, not by spending parent three-AP load three times;",
        "- collision multiplicity transfers to lower-scale reference differences and explicit rectangle-aspect tokens;",
        "- the remaining scalar obstruction is the critical excess `Y(P)`, not the local branching coefficient;",
        "- higher scale moments contract before collisions but do not by themselves prove reciprocal summability;",
    ]
    dmark = "- the active reserve is weighted three-translate exposure, not scalar overlap multiplicity;\n"
    for line in decisions:
        text = text.replace(line + "\n", "")
    if dmark not in text:
        raise AssertionError("missing scale-transfer decision marker")
    text = text.replace(dmark, dmark + "\n".join(decisions) + "\n", 1)
    old_start = "## 12. Active closing target"
    protocol = "## 13. Documentation protocol"
    active = r"""## 12. Active closing target

The active scalar row is

```math
\Psi_1(\text{child witnesses})
\le
N\mathcal L_3(P)
+
Y(P),
```

where first appearances are paid by exact role capacities `1/2,1/4,1/4` and
`Y(P)` is the scale-critical collision excess.

Every term of `Y(P)` has two exact exports:

```text
lower-scale four-AP-free reference-difference reserve;
completion rectangle with aspect ratio delta/D.
```

The immediate task is a first-appearance theorem for those exported tokens,
including unused shell slack, terminal release, and ambient
external-completion/genuine-hole separation. CL-087 must be audited before its
finite values are used. Corrected-third-frontier and generation-six
propagation remain blocked."""
    text = replace_section(text, old_start, protocol, active)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    base.main()
    patch_ledger()
    patch_program()
    patch_readme()
    patch_history()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
