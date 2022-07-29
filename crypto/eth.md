## Ethereum Structure
- Account Based model
- OPs codes 32bit
- How Chainlink works?
- LMD phost & FFG finalization
- heaviest chain
- Node Discovery Protocol

**Core Devs**
- Vitalik
- Justin Drake
- Andrew Ashikhmin
- Adrian Sutton
- Tim Beiko
- Micah Zoltu

**Gas fee**
base fee
create contract 530000
use contract 21000

tx fee = none_zero * 16 + zero * 4

**Scale Soluction**
  - main chain
    - shard
  - side chain
    - Matic/Polygon
    - Has its own security
  - layer 2
    - application specific
      - state channel(application specific, not permissionless)
      - plasma project, batch trans, main net must assume data is available for audit
    - rollup
      - optimistic rollup (support smart contract, with judge system, delay withdraw)
      - zk rollup (long term solution, instance withdraw, but snark proof takes 3s to generate)
      > submit small signature every state changes, main net don't need offline data to audit