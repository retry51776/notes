# Network Admin
> Things a network admin should know.

## Hypervisors
> Type 1 hypervisor: installed directly on top of physical hardware.

**Type 1 hypervisors / vendors**
- VMware vSphere with ESX/ESXi  
- KVM (Kernel‑Based Virtual Machine)  
- Microsoft Hyper‑V – “Microsoft grants Hyper‑V independence from OS access”  
- Oracle VM  
- Citrix Hypervisor (formerly XenServer)

> Type 2 hypervisor (hosted): installed on top of a host OS.

**Type 2 hypervisors**
- VirtualBox  
- Windows Virtual PC  
- Parallels  

## HashiCorp
> They were the cool kids before Kubernetes; Terraform & Vault remain popular.

- Packer – builds OS images (not Docker images)  
- [Terraform](./cloud/terraform.md)  
- Nomad – workload orchestrator  
- Vault – secrets management  
- Consul – service discovery and configuration
