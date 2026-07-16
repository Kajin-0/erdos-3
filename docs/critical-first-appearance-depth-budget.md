# Critical first-appearance depth budget

## Status

State-independent logarithmic refinement of the established scale-weighted first-appearance transport bound.

The scale exponent `p=1` is critical: first-appearance capacity is conserved. The derivative at the critical exponent records a positive dyadic-depth release. The established majorant releases exactly `7/4` shell levels per unit of parent critical capacity.

This theorem applies only to first appearances. Collision excess is excluded and still requires its own ownership or transfer mechanism.

---

## 1. Established scale profile

For one parent target three-AP of step `h` in a dyadic block of base `N`, the established first-appearance scale majorant is

```math
\frac{N^p}{h}
\left(
\frac{3}{4^p}
+
\frac{1}{2^{p+1}}
\right).
```

Write

```math
c_p
=
\frac{3}{4^p}
+
\frac{1}{2^{p+1}}.
```

Then

```math
c_1=1
```

and

```math
c_p<1
```

for every `p>1`.

The critical parent capacity is

```math
C_N(h)=\frac Nh.
```

---

## 2. Virtual critical slots

The majorant may be written as four virtual scale slots:

```math
\frac{3(N/4)^p}{h}
+
\frac{1}{2}\frac{(N/2)^p}{h}.
```

At `p=1`, these have capacities

```math
\frac{C_N(h)}4,
\quad
\frac{C_N(h)}4,
\quad
\frac{C_N(h)}4,
\quad
\frac{C_N(h)}4.
```

The first three slots lie two dyadic levels below `N`; the fourth lies one level below `N` and carries the half multiplicity already present in the established majorant.

Thus the critical first-appearance mass is exactly conserved:

```math
3\frac{C_N(h)}4
+
\frac{C_N(h)}4
=
C_N(h).
```

---

## 3. Exact depth release

Let

```math
\ell(N)=\log_2N.
```

The parent depth moment is

```math
C_N(h)\ell(N).
```

The virtual child depth moment is

```math
3\frac{C_N(h)}4\bigl(\ell(N)-2\bigr)
+
\frac{C_N(h)}4\bigl(\ell(N)-1\bigr).
```

Subtracting gives

```math
\boxed{
C_N(h)\ell(N)
-
\operatorname{Depth}_{\rm child}
=
\frac74C_N(h).
}
```

Equivalently, the expected dyadic shell drop under the normalized critical majorant is

```math
\boxed{\frac74.}
```

---

## 4. Derivative form

Differentiate the scale coefficient:

```math
c_p'
=
-3\log(4)\,4^{-p}
-
\frac{\log2}{2^{p+1}}.
```

At `p=1`,

```math
c_1'
=
-\frac74\log2.
```

Therefore

```math
\boxed{
-\frac{c_1'}{\log2}
=
\frac74.
}
```

The virtual-slot and derivative computations are the same critical logarithmic reserve.

---

## 5. Missing first appearances

If a virtual slot is not occupied by an actual first preimage, its complete capacity remains released. If an actual child lies below the slot's maximal scale, the additional shell drop gives extra depth release.

Thus `7/4` is the baseline release of the established majorant. Absence or deeper descent only improves it.

---

## 6. Collision exclusion

The theorem does not assign this reserve to collision excess. Several child preimages may share one parent target, and their additional load is not represented by the four first-appearance slots.

In particular, unbounded collision-reference families cannot be paid by a fixed `7/4` coefficient without additional output.

The admissible use is:

```text
first-appearance transport
    -> critical capacity conservation
    + 7/4 depth release;

collision transport
    -> separate physical pair, reference-difference,
       maximality-witness, or incidence ledger.
```

---

## 7. Ownership interpretation

The depth budget belongs to the parent target occurrence, not merely to its numerical target progression. If occurrence ownership is discarded by physical union projection, the budget can be counted incorrectly.

A valid critical Bellman potential must therefore retain:

```text
production owner;
current dyadic shell level;
first-appearance versus collision status.
```

This is precisely the information lost in the physical-union Hall no-go families.

---

## 8. Strategic consequence

The scale-critical row contains a genuine logarithmic reserve even though its mass coefficient is exactly one. Any successful critical proof should use this derivative coordinate before introducing another fitted scalar feature.

The remaining theorem must show that collision output either:

1. consumes owned depth reserve from additional production tokens;
2. creates lower-scale reference or pair tokens carrying their own future depth;
3. terminates into maximality or arithmetic-obstruction output;
4. activates a higher-order incidence resource.

The `7/4` identity is exact, universal, and compatible with the existing scale-weighted transport theorem. It is not a complete collision bound.