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
    - trans out script
  - lock time (4)

- private key is 1 to 1 with public key
- 160 bit address = `ripemd160(sha256(256_bit_public_key))`
- secp256k1 elliptical curve

- Unspent Transaction Output (UTXO)
- Lighting network is a protocol uses BTC as bank reserves note.
- longest chain
- 10 min per block, block body 1mb
- calculate difficulty every 2 week (2,016 blocks)
- timestamp is NOT reliable in blockchain

## vulnerability
- 51% attack `stop all trans, double spent, `
- time wrap attack

- OP_CHECKMULTISIG extra 1 pop off stack

# Source Code Structure
> . h files, or header files, are used to list the publicly accessible instance variables

> .cpp files, or implementation files, are used to actually implement those methods and use those instance variables

- /src
  - /validation.cpp `5000 lines logics, TODO: break down methods`
  - /index
    - /base.cpp
  - /node
    - /miner.cpp
  - /secp256k1
    - /include/secp256k1_preallocated.h
  - /consensus
    - /consensus.h
    - /validation.h
    - tx_verify.cpp
    - merkle.cpp