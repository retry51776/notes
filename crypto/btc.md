## Bitcoin Structure
- Block header (80 bytes)
  - Version (4 bytes)
  - Previous block hash (32 bytes)
  - Merkle root (32 bytes)
  - Timestamp (4 bytes)
  - Target (4 bytes)
  - Nonce (4 bytes)
- Transaction counter (1–9 bytes, varint)
- Transactions
  - Version number (4 bytes)
  - Input counter (1–9 bytes, varint)
  - Inputs
    - Previous transaction hash
    - Previous output index
    - Script length
    - Signature script
    - Sequence
  - Output counter (varint)
  - Outputs
    - Value (8 bytes)
    - Pubkey script length
    - Pubkey script
  - Lock time (4 bytes)

- Private key ↔ public key (1‑to‑1 mapping)
- Address = `RIPEMD160(SHA256(public_key))` (160 bits)
- secp256k1 elliptic curve

- Unspent Transaction Output (UTXO) model
- Lightning Network – a protocol that uses BTC as bank reserve notes.
- Longest chain rule
- ~10 minutes per block; block size ≈ 1 MB
- Difficulty adjusts every two weeks (2,016 blocks)
- Timestamp is **not** reliable in blockchain consensus

## Vulnerabilities
- 51 % attack – can halt transactions and enable double‑spending.
- Time‑warp attack.
- `OP_CHECKMULTISIG` consumes an extra stack element.

# Source Code Structure
> `.h` files (header files) list publicly accessible variables.  
> `.cpp` files implement the methods and use those variables.

```
src/
├─ validation.cpp   # ~5,000 lines of logic – TODO: break into smaller functions
├─ index/
│  └─ base.cpp
├─ node/
│  └─ miner.cpp
├─ secp256k1/
│  └─ include/secp256k1_preallocated.h
└─ consensus/
   ├─ consensus.h
   ├─ validation.h
   ├─ tx_verify.cpp
   └─ merkle.cpp
```

