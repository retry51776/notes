## Ethereum Structure
- Account‑based model
- Opcodes are 32 bits
- How Chainlink works
- LMD GHOST & FFG finalisation
- Heaviest chain rule
- Node Discovery Protocol

**Core developers**
- Vitalik Buterin
- Justin Drake
- Andrew Ashikhmin
- Adrian Sutton
- Tim Beiko
- Micah Zoltu

### Gas fees
- Base fee
- Create contract: 530,000 gas
- Use contract: 21,000 gas

```
tx_fee = (non_zero_bytes * 16) + (zero_bytes * 4)
```

### Scaling solutions
- **Layer 1 (main chain)**
  - Sharding
- **Layer 2 (side chains)**
  - Polygon/Matic – has its own security
- **Layer 2 (application‑specific)**
  - State channels – not permissionless
  - Plasma – batches transactions; the main net must assume data is available for audit
  - Rollups
    - Optimistic rollup – supports smart contracts, uses a fraud‑proof system with delayed withdrawals.
    - zk‑rollup – long‑term solution; instant withdrawals, but generating SNARK proofs can take several seconds.

> In rollups, a small signature is submitted on each state change, allowing the main net to verify without storing all off‑chain data.

## FAQ
1. Geth uses the most disk space because the Ethereum state grows with every block. Syncing takes a long time because Geth must execute blocks sequentially.
2. *(additional questions can be added here)*

