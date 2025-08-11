# Math

**Encryption example**

```
enc(m, p) = big_rand() * p + 2 * small_rand() + m
dec(ct, p) = (ct % p) % 2
```

## Elliptic‑Curve Cryptography (ECC)

- One‑way function: multiplication is easy; division (discrete log) is hard.
- Why use an elliptic curve?  
  Security comparable to RSA but with smaller key sizes and higher efficiency.

### Curve basics
Consider the curve `y² = x³ - 2x + 15`.

1. Imagine a 2‑D integer grid folded onto a torus (donut). The coordinate range becomes limited.
2. Draw an elliptic‑curve line on the torus; when it reaches the edge, it wraps around.
3. Choose a random point on the curve as the **generator** `G`.

### Group operations
1. **Negation** – reflect across the x‑axis.  
2. **Addition** – draw a line through two points; it intersects the curve at a third point; take the negation of that point.  
3. **Doubling** – add a point to itself (special case of addition).  
4. **Infinity point** – acts as the identity element (`∞ + P = P`).  

Repeated addition yields scalar multiplication: `k·G = G + … + G` (k times).

Any generator together with these operations forms a finite abelian group.

## Signing a message

1. Compute a digest `z` of the message (same bit‑size as the curve order).  
2. Choose random `k`, compute `K = k·G`; let `r` be the x‑coordinate of `K`.  
3. Compute `s = k⁻¹ (z + r·a) mod N`, where `a` is the private key and `N` is the curve order.  

The signature is `(r, s)`.

### Verification
1. Compute `w = s⁻¹ mod N`.  
2. `u₁ = z·w mod N`, `u₂ = r·w mod N`.  
3. Calculate `S = u₁·G + u₂·A` (where `A` is the signer’s public key).  
4. The signature is valid if the x‑coordinate of `S` equals `r`.

> Reusing the same `k` makes `r` identical across signatures, leaking the private key.

## Homomorphic Encryption (brief)

Allows computation on encrypted data without decryption.

## ZK‑SNARKs

- Byzantine Fault Tolerant (BFT) Proof‑of‑Stake systems.
- Minimum number of nodes for tolerance: `n = 3f + 1`.

### Notable protocols
- Tendermint – mature BFT algorithm.  
- Historical developments:
  - Kilian 92, Micali 94 → high prover time.  
  - GGPR 13, Groth16 → trusted setup required.  
  - Sonic 19, Marlin 19 → improved efficiency.  
  - Halo 19, STARK 19 → no trusted setup.

### DSLs for circuits
- Circom
- ZoKrates
- Leo
- Zinc
- Cairo
- Snarky

## Infinity point

The identity element (`∞`). For any point `M`, `M + ∞ = M`. Repeated addition eventually reaches `∞` and cycles.

## Resources
- Ariel Gabizon – *Explaining SNARKs* (YouTube series).  
- Various lectures on homomorphic hiding, blind evaluation of polynomials, knowledge‑of‑coefficient tests, Pinocchio protocol, etc.

## FAQ

**What is a ZK‑SNARK?**  
A proof that a computation was performed correctly without revealing inputs or intermediate steps.

**Why/How are polynomials converted to linear algebra?**  
(See the referenced videos for detailed explanations.)

### Example: Converting an equation to R1CS
Given `x³ + x + 5 = 35`:

| Step | Operation                | L‑vector            | R‑vector            | O‑vector |
|------|--------------------------|---------------------|---------------------|----------|
| 1    | `a = x * x`              | `[0,1,0,0,0,0]`     | `[0,1,0,0,0,0]`     | `[0,0,1,0,0,0]` |
| 2    | `b = a * x`              | `[0,0,1,0,0,0]`     | `[0,1,0,0,0,0]`     | `[0,0,0,1,0,0]` |
| 3    | `c = b + x`              | `[0,1,0,1,0,0]`     | `[1,0,0,0,0,0]`     | `[0,0,0,0,1,0]` |
| 4    | `d = c + 5`              | `[5,0,0,0,1,0]`     | `[1,0,0,0,0,0]`     | `[0,0,0,0,0,1]` |

These vectors are later transformed into a Quadratic Arithmetic Program (QAP) and finally into a SNARK proof.

