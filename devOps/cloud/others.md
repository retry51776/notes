
# Others

HashiCorp Vault – generate dynamic credentials.

Morpheus – GUI for non‑technical users to scale projects.

## Buzzwords

- Role‑Based Access Control (RBAC)  
- Operational maturity  

### Service Models

- Infrastructure as a Service (IaaS)  
- Platform as a Service (PaaS)  
- Logic as a Service (LaaS)  

### Processing Types

- Online Transactional Processing (OLTP)  
- Online Analytical Processing (OLAP)  

### Reliability Terms

- Service‑Level Agreement (SLA)  
- Service‑Level Objective (SLO)  
- Service‑Level Indicator (SLI)  

**Runbook** – predefined procedures to achieve a specific outcome.

## Firecracker
> Popular hypervisor stack, similar to Docker but for VM.
> > Pros: More isolation; support different host OS;
>
> Each VM has its own Firecracker api process.

- Jailer: wrapper of Firecracker for extra security.

```bash
ls -l /dev/kvm

# Step 1: Start firecracker API demo
# Step 2: download kernel & rootfs
# Step 3: make http PUT request w pointer to kernel & rootfs, to start VM.


https://github.com/firecracker-microvm/firecracker/blob/main/docs/getting-started.md

# Docker Network ~ Host TAP device
curl --unix-socket /tmp/firecracker.socket \
  -X PUT 'http://localhost/network-interfaces/eth0' \
  -H 'Content-Type: application/json' \
  -d '{
    "iface_id": "eth0",
    "guest_mac": "AA:FC:00:00:00:01",
    "host_dev_name": "tap0"
  }'

```

### firecracker-containerd
> Wrapper like docker.