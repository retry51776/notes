## Bitcoin Structure
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
- 10 min per block, block body 1mb
- calculate difficulty every 2 week (2,016 blocks)
- timestamp is NOT relable in blockchain

## vulnerability
- 51% attack `stop all trans, double spent, `
- time wrap attack

- OP_CHECKMULTISIG extra 1 pop off stack