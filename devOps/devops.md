# DevOps
> Fancy words goes here, because DevOps have tons of them.

# Operational Burdens
- CI / CD
- Production Stability (CT)
- Meeting
- Stack Maintain
- Documentation
- Unit test


# DevOps Metrics
- Deployment Freq
- Lead Time `committed to master to deployment`
- Mean Time Recovery
- Change Failure Rate `hotfix/deployment`
- Cycle time `aka dev time, most mgr care about`

## Four Fundamental Topologies
- Stream-aligned team: `Aligned to a flow of work from (usually) a segment of the business domain.`
- Enabling team: `Helps a stream-aligned team to overcome obstacles. Also detects missing capabilities.`
- Complicated subsystem team: `Where significant mathematics/calculation or hard to-find niche technical expertise is needed full-time.`
- Platform team: `A grouping of other team types that provide a compelling internal product to accelerate delivery by stream-aligned teams.`

## Project CheckList
- install
- config `devs always forgets to tell devOps`
- provision
- deploy

- security
- monitor
- backup & restore

- network
- HA
- scalability
- performance

- cost
- documentation
- test


---
## Deployment strategy
- Blue Green
  > swaps all at once; K8s service mesh VirtualService
- Rolling update
  >  Different Version at same time
- Recreate
  > Offline gap
- Canary
  > some user, slowly move over; K8s service mesh VirtualService
- A/B
  > target subject get updates 
- Shadow

