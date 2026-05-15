# Networking

> Networking is quite expensive, mostly matter during training.

> Hopefully inference within node, cross nodes communication will way slower.

- Vera ETL256 reference rack architecture
  - NVLink Cartridge + NV Switch + Backplane ~ Hardware for NVLink Fabric


## Rack

Terms:
- Rack Units (RU) 1.72inch; 42RU / 48RU per Rack;
  - H200 DGX 8 RU
- default Superpod Reference Architecture

Rack Components:
- Network Trays (TOR)
- General Compute Trays
- HPU Trays
- NVLink switch
- Power Shelves

## Frontend Networking

- HPU trays connect to storage server

## Backend Networking

Octal Small Form-factor Pluggable (OSFP)

- Network Topology
  - Direction Connections
    - Top of Rack (ToR) switch `optical switch`
  - two tier 8-rail optimized fat tree `different GPUs in same node points to different switches, smooth peak traffic`
    - leaf switch often need optical switch
  - Dragonfly
  - multi-dimensional Torus 
  - Ring P2P
- Network stacks
  - none-blocking network
  - network isolation
    - Partition Keys / VLAN
    - Unified Fabric Manager (UFM)
  - oversubscription ~ more upload links to spine(TOR) than spine's capacity
- Hardwares
  - NCCL
  - UCX
  - UCCL
  - Mooncacke

## OBB

- SN2201 OBB switch 48 ports * 8
  - Baseboard Management Controller (BMC)
    - Remote Power Control
    - Hardware Monitoring


## Driver

- fabricmanager for NVLink
- Mellanox OpenFabrics Enterprise Distribution (MLNX_OFED)
- Nvidia HPC-X for NIC driver

- ipmi-exporter monitor fan speed
- Nvidia Datacenter Manager

## Configs
- /etc/nccl.conf


## Head Node

Also call Login Node / Submit Node; Always `hostname` to confirm current terminal node.

The environment is default consistent across the login and compute nodes.

- open-source hypervisor: qemu-kvm for fast recovery
- k8s
- SLURM `sbatch script ≈ job YAML`
  - `sinfo`
  - `srun --pty` because we don't want head node execute this, rather let partition nodes runs
  - `sbatch xxx.sh` where `xxx.sh` uses `#SBATCH --mem=2G` define job requirements
    - default NOT to exit on error
    - `$SLURM_ARRAY_TASK_ID`
  - `squeue` check current job queue
  - `seff <job_id>` check job resource usage
- Sun Grid Engine
- Portable Batch System
- `import ray` python distributed application runtime

- Environment Module system `apt install environment-modules`

### Email

```bash
# /usr/bin/mail only the front-end
# config @ ~/.mailrc

echo "hello local" | mail -s "test" $USER # send local email
mail -H # check local email


# backend postfix
# config @ /etc/postfix/main.cf

relayhost = [smtp.example.com]:587
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
smtp_sasl_security_options = noanonymous
smtp_use_tls = yes
smtp_tls_security_level = encrypt
myorigin = example.com
smtp_generic_maps = hash:/etc/postfix/generic
```
