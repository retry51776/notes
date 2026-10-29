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
  - B200 ~ 1kw; so at lease 50+ kW rack

## Frontend Networking

- HPU trays connect to storage server

## Backend Networking

**Interconnect Protocols**:
- Accelerator Scale-Up
  - NVLink
  - UALink
- Coherent Memory Interconnect
  - CXL
  - CCIX
- Scale-Out Networking
  - InfiniBand
  - RoCE
  - Ultra Ethernet
- General I/O
  - PCIe
  - USB / Thunderbolt
- Storage Interconnect
  - SATA
  - SAS
  - NVMe
    - PCIe
    - Fabrics
  - Fibre Channel

Physical Connections:
- Octal Small Form-factor Pluggable (OSFP)

> We don't want traffic go through typical k8s ingress or service routing, we route traffic through pod's sidecar.

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


### IB
> IB covers first 4 ISO layers: Physical, Data Link, Network, Transport.
- Protocol:
  - IB Reliable Connection(IBRC): relies on a CPU proxy thread
  - IB GPUDirect Async(IBGDA): faster by bypass CPU
  - DeepEP protocol: DeepEP Dispatch hacked version of NVSHMEM, reduce synchronization base off some assumptions.
- Terms:
  - Verbs: low-level instruction interface for network/RDMA operations.
  - CUDA VMM (Virtual Memory Management)
  - NVLink pointers: UVA + peer access
  - NVLink domain: group of GPUs within single fabric
- Scope:
  - Intra
    - NVLink Bridge
    - NVSwitch Board
  - Server to Server
    - NVLink Domain rack-scale
  - Rack to Rack
    - InfiniBand switch

> Hyperconverged Infrastructure alternative NVLink

OCS:
> Google assume spine switch connections are stable at min time scale. Palomar uses mirror switch.

### NVLink
> Hardware, need NCCL/NVSHMEM softwares to operate. UALink is open protocol alternative.

- NVLink Bridge: 2 GPUs bridge hardware, for PCIe cards
  - PCIe H100 has NVLink bridge connectors(3 slot section for single connection)
- NVSwitch Board: 8 GPUs hardware; Interconnect NVLink Hybrid Riser Board;
- NVLink Domain rack-scale: 72 GPUs

- NVLink 1 @ P100 ~160 GB/s per GPU
  - `cudaDeviceEnablePeerAccess()`
  - communicate through NCCL
- NVLink 3
  - add NVSwitch support
- NVLink 4 @ H100 ~900 GB/s per GPU
  - Multicast PTX instructions `multimem`
- NVLink 5 @ B200 1.8 TB/s per GPU
  - `multimem.cp.async.bulk`
  - `multimem.cp.reduce.async.bulk`
  - `multimem.st.async`
  - new datatypes / vector forms

> **Multicast** one virtual GPU address that represents multiple physical memory locations.

### Communication Library
> Developer control IO through Communication Libraries. NCCL is most popular, second is NVSHMEM.

#### UCX
> Unified Communication X(UCX) primarily a host-side (CPU) communication framework/API.

#### MPI
> Message Passing Interface(MPI) is old CPU Library, its problem has too many abstraction/optimization.
> > No built-in **flow control**. Simple Pub/Sub message system.

#### NCCL
> NCCL (NVIDIA Collective Communications Library) - specialize protocol for GPU, open source, focus collective communication operations, less control than NVSHMEM. Think CUTLASS -> CUDA -> GPU, NCCL -> ISA Primitives -> NVLink
>
> AMD uses RCCL.

Transports:
- PCIe
- NVLink P2P
- NVLink SHARP/NVLS mechanisms

Kernel/ISA Primitives:
- `multimem.load`
- `multimem.st.async`
- `multimem.cp.async.bulk`

Collective Operations:
- Synchronization
- Data movement
  - Broadcast
  - Scatter: each rank gets subset of data
  - Gather: collect all ranks into single rank
  - All-gather: every rank broadcast & gather;
- Reduction
  - Reduce
  - Reduce-scatter: every rank get op(sub_set)
  - All-reduce: reduce-scatter + all-gather
- Ordered collective: cumulative transforms
  - Scan (Prefix Sum)
  - Exclusive Scan

Communication Patterns:
- Ring
- Halo: Neighbor exchange
- Tree
- Butterfly
- Torus


> NCCL 2.x device APIs now converge toward NVSHMEM.
>
> NCCL built-in flow control (auto batch optimization) network IO. NV devs recommend NOT to finetune it.

#### NVSHMEM
> **GPU kernel directly** put/get/update data in remote GPU memory without CPU involvement.
> > Built-in support memory partition.
>
> > One sided control! similar pub/sub
>
> NVSHMEM enable interleaving between compute & io transfer within kernel, while NCCL will support similar soon.

- Partitioned Global Address Space (PGAS)
- memory symmetry: assume/prerequisite every node same memory allocation.
- DeepEP Dispatch: customize version from NVSHMEM

### Optical
> Physical often not stable(FAB defect, or interference); common solution is add monitor module & compensate mechanism.

Optical Components:
- Digital Signal Processor (DSP): signal adjustment
- Optical-to-Electrical (OE): light shutter.
- External Laser Source (ELS): light source, most energy intense & breakable module.

Optical Industry Trend @ 2026:
- Pluggable Optics: (DSP + OE + ELS) 2026 standard.
- Linear Pluggable Optics (LPO): integrate DSP workload into switch chip
- Near-Packaged Optics (NPO): Move OE to near switch chip
- Co-Packaged Optics (CPO): integrate OE workload into switch chip
  - CPO Switch: Broadcom 3rd gen Davisson @ 102Tbps & 16 OE
  - CPO GPUs: at least 2028 Feynman
- Optical I/O: GPU integrate CPO switch chip


Problems:
- Link Flap 链路闪断
- MMean Time Between Failures (MTBF)

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

## Qualcomm Topology

- **QTM-X800** — NVIDIA Quantum-X800 InfiniBand switch plus BlueField-3 DPUs and ConnectX-8 SuperNICs
- **QTM-2** — NVIDIA Quantum-2 InfiniBand switch plus BlueField-3 DPUs and ConnectX-7 NICs
- **SPTMX** — NVIDIA Spectrum-X Ethernet switch and SuperNICs plus BlueField-3 DPUs

## Transfer Engine

> Often framework will use some engine to give comprehensive support to different hardwares, different protocols, different modes.

https://kvcache-ai.github.io/Mooncake/design/transfer-engine/index.html

System V shared memory (shm) - Linux allow multi processes map the same physical memory pages.

## Uptime
> SLA don't guaranty uptime, just vendor promise. Just like house backup circuit needs different routing. We needs to mark critical LLM service vs none-critical service. Only backup capacity for critical LLM service.