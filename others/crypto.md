# Crypto
- merkle tree
- block header
- consensus
  - proof of work
  - proof of stake
- transaction ledger vs balance ledger
- scability trilemma: security, decentralized, scalable
  
> cryptoeconomics is use economic incentives to provider guarantee about application

enc(m, p) = big_ran() * p + 2 * small_rand() + m

dec(ct, p) = (ct % p) % 2


## BTC
- block header (80 bytes)
  - block version (4)
  - prev block hash (32)
  - merkle root (32)
  - timestamp (4)
  - target (4)
  - nonce (4)
- Transaction Counter (1-9)
- Trans
  - version number (4)
  - input counter (1-9)
  - inputs
    - prev trans hash
    - prev trans index
    - tran sign length
    - tran sign
    - seq
  - output counter
  - output
    - value
    - trans out len
    - trans out scipt
  - lock time (4)

- private key is 1 to 1 with public key
- 160 bit address = `ripemd160(sha256(256_bit_public_key))`
- secp256k1 elipcal curve

- Unspent Transaction Output (UTXO)
- Lighting network is a protocal uses BTC as bank reservor note.
- longest chain


## Eth
- Account Based model
- OPs codes 32bit
- How Chainlink works?
- LMD phost & FFG finalization
- heavest chain
- Node Discovery Protocol

Scale
  - main chain
    - shard
  - side chain
    - Matic
    - Has its own security
  - layer 2
    - application specific
      - state channel(application specific, not premissionless)
      - plasma project, batch trans, main net must assume data is avaiable for audit
    - rollup
      - optimistic rollup (support smart contract, with judge system, delay withdraw)
      - zk rollup (long term solution, instance withdraw, but snark proof takes 3s to generate)
      > submit small signature every state changes, main net don't need offline data to audit

# Buzzword Zoo
## Private Computation
- zk proof
- secure multiparty computation
- zk-snarks
- homomorphic Encryption
- Secure Functions Evaluation
- Trusted Execution Environments

## Private Communication
- Asy encryption
- Proxy Re-encryption
- Access Control


zk snark 2 way
1. map computation to polynomial equation
2. Verifier choose secret evaluation point
3. Prover eval polynomials
4. Verifier checks(Homomorphic Encryption allow compute on encrypted data without decryption)


Prover know w()
a(x) * w(x) = b(x) * c(x)

zk snark 1 way
We don't needs to decrypt Homomorphic, we just care about equality


  - Pinocchio protocol
  - Convert to polynomials
  > because different polynomials only coincide at n(degree) points
  - Homomorphic Encryption
  - Knowledge of Coefficient Test force single point commitment
> balance proofer time, verifier time, proof size
Baselines:
  - BCCGP-sqrt
  - Bulletproofs
  - ZKB++
  - Ligero
  - libSTARK
  - Hyrax-1/3
  - Hyrax-native


## Solana
- separate transaction throughput from consensus?


# Resource
Ariel Gabizon - https://www.youtube.com/watch?v=yNS_ttTj1KE&t=2952s

- Explaining SNARKs Part I: Homomorphic Hidings
- Explaining SNARKs Part II: Blind Evaluation of Polynomials
- Explaining SNARKs Part III: The Knowledge of Coefficient Test and Assumption
- Explaining SNARKs Part IV: How to make Blind Evaluation of Polynomials Verifiable
- Explaining SNARKs Part V: From Computations to Polynomials
- Explaining SNARKs Part VI: The Pinocchio Protocol
- Explaining SNARKs Part VII: Pairings of Elliptic Curves


Byzantine-Fault Tolerate(BFT) POS
best fault torlerat n = 3f + 1
tendermint - most mature BFT algorithm


**Compound**
2019-Feb launch
Interest Rate is calculate every block, no fix rates

**Elliptic-curve cryptography (ECC)**
one-way function
Ex: multiple is easy, divide is hard

Why do it in elliptic-curve surface?
security equivalent to classical systems (like RSA)
more difficult/secure compute than normal 2D coordinate

EX: y^2 = x^3 - 2x + 15
1. imagine 2D Integer coordinate fold on donut (mod fold plane back to itself, there for 2D plan have [x, y] range that is limited)
2. draw a elliptic-curve line on donut, as cure hit edge curve line will cutoff(won't loop around)
3. pick a random points on curve-line as The Generator Point, G;
4. New Math here
   1. Negative Operation = Flip across y axis
   2. Addition Operation = draw a line hits 2 points, should have 3rd point hit curve, then take Negative of new point
   3. Point Double = Addition Operation, use tangle line(Key shortcut)
   4. Special Case: 2 points parallel to x or y axis, when addition = infinty point
   5. Special Case: infinty point + point = itself
   6. Scalar Multiplication = reapt Addition Operation on itself
   7. Any Operation can chain together just like algebra operation 13G = 8G + 4G + G
5. Any Generator Point with Addition Operation will creates a limited set points (group structure)


Inifinty Point is 0, therefore M_point + Inifinty = M_point
All group structure will eventually hit Inifinty Point, then back to itself.


Share secrets = prive_key * other_public_key = private_A * public_B = private_B * public_A
Sign Transaction


**Sign message**
digest value (z) same bit size order of curve
modular arithmetic, order of curve as modulus
1. pick a random number k, then calculate K = Generator * k, K's x value = r uses for verfication
2. then calculate k^-1

z = 10 digest value, 1 < z < N, hash of message?
k = 19 random number, must  
a = 3 private key
r = 9 (Generator * k's x axis)
N = 23 (order of curve)
s = k^-1(z + ra) % N

(r, s) = signed

**Verification**
w = s^-1 % N (s from signature)
u1 = zw % N (z is from message)
u2 = rw % N (r is from signature)
S = u1G + u2A (A is sender's public key)
(S's x value should match r from message)


if k is same, r will always be same

RLP (Recurrsive Length Prefix) generate z from message
SSZ (Simple serialize) Eth 2 generate z from message