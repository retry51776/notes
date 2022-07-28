# Azure
> https://azure.microsoft.com/en-us/services/

# Computation
- VM `$70/month general vm 2CPU, 8GB, 16GB disk`
- Container Instances `single container`
- Batch
- Azure Kubernetes Service (AKS)
- Web App for Containers

- Service Fabric
- Cloud Services
- Mobile App
- Web App

- Logic App `Is it step function?`
- Azure Functions `Similar cloud function`

## Storage
- Online Transactional Procesing (OLTP)
  - Azure SQL DB `microsoft's product`
  - Other Opensource DBs

  - Azure Cosmos DB `Nosql DB, microsoft product`
  - Azure Cache for Redis

  - Azure Storage `aka S3`
    - File `alt S3`
    - Blob `flat folder`
    - Disk
    - Queue
- Online Analytical Processing (OLAP)
  - SQL Warehouse
  - Data Lake Storen `speciallize for hadoop`

# Security
- Azure AD

# Network
- VNet `Microsoft Account Scope`
  - VNet peering `similar to VPN tunnel but allow 2 VNets communicate`
  - VPN `Encrypt Traffic to VNet through public internet`
  - ExpressRoute `Dedicated connection to VNet, usually offer by data center`
- Load balancer `Expose VNet to public`

- Avaiable Region
- Avaiable Zone `more than 3 data centers`

### Private Link
> https://docs.microsoft.com/en-us/azure/private-link/


## Billing
- Billing Account `Company Account`
  - Subscription `By Dept, or By Team, By brand`
    - Resource Group `Functions, VMs, DBs; or By Product `

> Spot `save money by let microsoft shut down whenever`

```bash
az group list 
az group delete --name xxx
```