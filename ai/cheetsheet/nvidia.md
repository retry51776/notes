# Nvidia

- AI Enterprise
  - DGX OS / Base OS
    - GPU Driver
    - CUDA Toolkit
    - NCCL
    - Mellanox OFED Driver
    - GPU Direct Storage (GDS)
    - NVIDIA® System Management (NVSM)
  - DGX EL (Enterprise Linux)
  - Base Command Platform (BCP)
    - Dynamo
      - NV GPU Operator
        - K8s ClusterPolicy
      - DCGM Exporter
  - NVIDIA Mission Control
    - Simple Linux Utility for Resource Management (SLURM) `workflow manager`

LTS

- DGX Spark @ 7.2.3
- DGX H100 640 GB @ 6.0.11
- DGX A100 640 GB @ 5.5.1

## K8s

Pods:

- container-toolkit
- cuda-validator
- dcgm-exporter
- driver-daemonset
- mig-manager
- operator-validator

K8s `GPU Operator`'s `ClusterPolicy` set `RuntimeClass` default uses `runc`, for NV GPU Operator default changes to `nvidia`.

Runtime `nvidia` does

 1. Detects if the container requests GPUs (e.g., via NVIDIA_VISIBLE_DEVICES or nvidia.com/gpu limit).
 2. Mounts the GPU device nodes (/dev/nvidia0, /dev/nvidiactl, etc.) into the container.
 3. Injects necessary libraries (libcuda.so, libnvidia-ml.so, etc.) from the host into the container’s filesystem.
 4. Sets up environment variables
 5. Then calls runc underneath to actually launch the container process.

K8s `GPU Operator`'s `nvidia-driver-daemonset` will install driver on HOST, so all other containers has GPU drivers.

## Flow

Pre Hopper
    nvsm > telemetry > Prometheus(HTTP GET) > Grafana
Post DGX H100
    BMC (Baseboard Management Controller) > telemetry(HTTP POST) > InfluxDB > Grafana

## Resources

- <https://catalog.ngc.nvidia.com/search?filters=resourceType|Container|container>

- NVIDIA Enterprise Support Portal - <https://www.nvidia.com/en-us/support/enterprise/>

- <https://docs.nvidia.com/datacenter/nvsm/nvsm-user-guide/latest/nvsm-user-guide.pdf>

## NVSM CLI

> `nvsm` syntax very similar to `kubectl`, but install on HOST/Node level to capture Hardware stats, not k8s/helm.

> `nvsm-aggregator` are containers deployed in k8s.

```ini
# ===============================================================
# NVIDIA System Management (NVSM) Configuration File
# ===============================================================

[general]
# Enable the HTTPS management API and web UI
enable_https = true

# Certificates for secure communication
ca_cert        = /pki/ca.crt
https_cert     = /pki/node1.crt
https_priv_key = /pki/node1.key

# Port for NVSM web server (default 8443)
https_port = 8443

# Optional: if you want both HTTP and HTTPS for testing
enable_http = false
http_port   = 8080

# NVSM internal log level: info | warning | error | debug
log_level = info

# Directory where NVSM stores persistent state
data_dir = /var/lib/nvsm

# ===============================================================
# Notification / Email (optional)
# ===============================================================
[notification]
enable_email = true

smtp_server   = smtp.mycompany.com
smtp_port     = 587
use_tls       = true
sender_email  = nvsm@mycompany.com
recipients    = admin@mycompany.com,ops@mycompany.com

# Optional: environment variable expansion supported by systemd
smtp_user     = ${NVSM_SMTP_USER}
smtp_pass     = ${NVSM_SMTP_PASS}

# ===============================================================
# Policy / Automation (optional)
# ===============================================================
[policy]
# Directory for user-defined policies (YAML)
policy_dir = /etc/nvsm/policies
```

```bash
# Check
sudo systemctl status nvsm-core
sudo systemctl status -all nvsm*

# Config
## Only root can view nvsm.conf
chmod 600 /etc/nvsm/nvsm.conf
/etc/nvsm/nvsm.conf

# Required services
nvsm-mqtt.service
nvsm-core.service
nvsm-api-gateway.service
nvsm-notifier.service

# Auto send logs to NV Cloud
sudo nvsm set ∕policy callhome_enable=true
# Disable
# offline_callhome_enable=true

sudo nvsm

nvsm list components
nvsm list sensors

systemctl enable nvsm-exporter
nvsm enable telemetry
# Dump data for NV diagnose <hostname>-<timestamp>.tar.xz
sudo nvsm dump health

sudo nvsm show alsm show storage
sudo nvsm show controllers
sudo nvsm show volumes
sudo nvsm show networkadapters
sudo nvsm show networkinterfaces
```

### Monitor

GPU → DCGM Exporter (:9400/metrics
) → Prometheus(ServiceMonitor
) → Grafana

Tools:

- SLURM
- nvidia-smi pmon
- gpustat `nvidia-smi wrapper`
- Triton metrics
- <https://github.com/NVIDIA/dcgm-exporter>
- NVIDIA GPU Operator `K8s monitor`
  - `node-role.kubernetes.io/gpu=true:NoSchedule`
  - `mig & config.yaml` shard GPUs

```bash
# SLURM View All Running / Queued Jobs
squeue

sinfo -N -l
```

```bash
# GPU Operator
sudo docker run --rm -d \
  --gpus all \
  -p 9400:9400 \
  nvidia/dcgm-exporter:3.3.6-3.6.0-ubuntu22.04
```

Tips:

- Scheduled stress testing, trace baseline, degradation

- dcgmi `Data Center GPU Manager`

common errors:

- Error correction code memory (ECC memory)
- Power Supply Unit(PSU)
- nvidia-persistenced crash (driver crashed)

XID error

```bash

# Check for GPU/NVIDIA errors

sudo dmesg | grep -i nvidia

# or

sudo journalctl | grep -i nvidia

# Ex:
# NVRM: Xid (PCI:0000:07:00): 31, Ch 00000035, engmask 00000101, intr 10000000
  
```

### Cluster Monitor

OpenFabrics Enterprise Distribution (OFED)
Subnet Manager

Cluster Dashboard containers

1. NVSM-Aggregator.
2. NVMS-Provision.
3. NVSM-Grafana.
4. NVSM-Prometheus.

## Support
