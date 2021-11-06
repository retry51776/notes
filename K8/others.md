# HashiCorp/ Nomad
Similar to k8, Nomad is a single binary, both for clients and servers.

wrote by Golang, opensource, 3 or 5 server

Agent
Job > Group > Task

# Orchestration

---
## Deployment strategy
- Blue Green
  > swape all at once 
- Rolling update
  >  Different Version at same time
- Recreate
  > Offline gap
- Canary
  > some user, slowly move over
- A/B
  > target subject get updates 
- Shadow