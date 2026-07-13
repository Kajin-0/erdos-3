# Terminal-fiber SCC spectral-growth obstruction

## Status

Exact fixed-policy finite theorem.

The terminal-fiber SCC quotient shows that graph cycles cannot be removed by ordering individual labels. The next natural proposal is a positive linear internal capacity vector `w` satisfying

```math
Aw\le\lambda w,
```

where `A` is the internal adjacency matrix of a cyclic component. The smallest possible factor `lambda` is the Perron spectral radius.

For the recorded `S_7` component, exact integer inequalities prove

```math
\boxed{
\frac{23}{9}<\rho(A)<\frac83.
}
```

Thus no positive linear internal capacity is nonexpanding or even factor-two contractive.

**Verifier:** `src/verify_terminal_fiber_scc_spectral_growth.py`.

**Certificate:** `data/terminal_fiber_scc_spectral_growth_certificate_2026-07-13.txt`.

---

## 1. Two-label component through `S_6`

From `S_3` through `S_6`, the unique cyclic component is

```math
C=\{61,303\}.
```

In the ordered basis `(61,303)`, its adjacency matrix is

```math
A=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
```

Therefore

```math
A^2=I
```

and

```math
\boxed{\rho(A)=1.}
```

This explains the exact unit-capacity balance observed in the harmonic SCC ledger through `S_6`.

---

## 2. Seven-label component at `S_7`

At `S_7`, the cyclic component is

```math
C=\{1,5,61,303,1597,8195,323640\}.
```

In that ordered basis, the exact adjacency matrix is

```math
A=
\begin{pmatrix}
0&0&1&1&1&1&1\\
1&0&1&1&1&1&1\\
0&0&0&1&1&1&1\\
0&0&1&0&1&1&1\\
0&0&0&0&0&1&1\\
0&0&0&0&0&0&1\\
0&1&0&0&0&1&0
\end{pmatrix}.
```

Its canonical adjacency hash is

```text
41d9402acc277af39e3dcd83b91d043d2bef565698fd84ec8d75fa670dc49407
```

---

## 3. Exact Collatz-Wielandt witness

Take the positive integer vector

```math
w=
\begin{pmatrix}
43\\59\\31\\31\\14\\10\\26
\end{pmatrix}.
```

Direct multiplication gives

```math
Aw=
\begin{pmatrix}
112\\155\\81\\81\\36\\26\\69
\end{pmatrix}.
```

The exact lower residual is

```math
9Aw-23w
=
\begin{pmatrix}
19\\38\\16\\16\\2\\4\\23
\end{pmatrix}
>0.
```

Hence

```math
Aw>\frac{23}{9}w.
```

The exact upper residual is

```math
8w-3Aw
=
\begin{pmatrix}
8\\7\\5\\5\\4\\2\\1
\end{pmatrix}
>0,
```

so

```math
Aw<\frac83w.
```

Because the component is strongly connected, `A` is irreducible. Collatz-Wielandt therefore yields

```math
\boxed{
\frac{23}{9}<\rho(A)<\frac83.
}
```

No floating-point eigenvalue calculation is needed for the certificate.

---

## 4. Consequence for internal capacity

Suppose a positive linear component capacity were represented by weights `c>0` and required to satisfy

```math
Ac\le\lambda c.
```

Then necessarily

```math
\lambda\ge\rho(A)>rac{23}{9}.
```

Therefore all of the following are impossible on the recorded `S_7` component:

```math
Ac\le c,
```

```math
Ac\le\frac32c,
```

and even

```math
Ac\le2c.
```

The component cannot be controlled by a positive linear internal capacity with a contraction factor compatible with ordinary one-step telescoping.

---

## 5. Revised structural requirement

The cyclic component must discharge most of its internal branching by a mechanism outside the raw terminal-label adjacency. Plausible mechanisms are:

1. export into nonterminal recursive labels;
2. affine-obstruction growth;
3. completion or rectangle-support growth;
4. provenance capacity consumed across repeated cycles;
5. multi-generation amortization with sufficient scale gain;
6. a nonlinear component potential.

Any proposed linear SCC capacity should first be checked against the exact lower bound

```math
\rho(A)>rac{23}{9}.
```

---

## 6. Scope

This theorem concerns the internal terminal-fiber adjacency of the recorded lexicographic `S_7` schedule. It does not prove:

- that every schedule has the same component;
- that every branch has spectral radius above one;
- that nonlinear capacity fails;
- that external obstruction export is insufficient;
- a retained-child quotient;
- a branching Bellman inequality;
- or the four-term Erdős conjecture.

---

## 7. Reproduction

Run

```bash
python3 src/verify_terminal_fiber_scc_spectral_growth.py \
  /tmp/terminal_fiber_scc_spectral_growth_certificate.txt
```

The certificate SHA-256 is

```text
aa753127d2d0adbcb124b0a9f6e5c053350d422cd66fe2a4c73d1045b2917bf4
```
