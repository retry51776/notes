# Azure
> https://azure.microsoft.com/en-us/services/

# Computation
- VM `$70/month general vm 2CPU, 8GB, 16GB disk`
- App Service `old name: Web App`
- Container Instances `single container`
- Batch
- Azure Kubernetes Service (AKS)
- Web App for Containers

- Service Fabric
- Cloud Services
- Mobile App

- Logic App `Is it step function?`
- Azure Functions `Similar cloud function`
- Azure LoadBalancer `very basic, don't support regex routing, throttle req`

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
  - Data Lake Storage `specialize for hadoop`

# Security
- Azure AD

# Network
- VNet `Microsoft Account Scope`
  - VNet peering `similar to VPN tunnel but allow 2 VNets communicate`
  - VPN `Encrypt Traffic to VNet through public internet`
  - ExpressRoute `Dedicated connection to VNet, usually offer by data center`
- Load balancer `Expose VNet to public`

- Available Region `1 data center`
- Available Zone `more than 3 data centers`

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

## Development
```bash
# dot sdk default C:\program files(x86)\dotnet; Add to path env

npm install -g azurite
azurite start

# download & install Microsoft Azure Storage Explore
# click connect/local storage emulator/connect
```

## App Service
> Kind like VM w [C#, php, java, javascript, Python, Ruby, Docker] already installed; AD supported; default path `/home/site/www.root/`

- App Service Plan `resource limit; auto scale up & out; pick runtime;`
  - Service (host machine that run webapp or container)
  - DeploymentSlot `kind like BlueGreen`
  - Application Configuration `config`
    - Key Vault Reference `secrets`
  - Custom Domain  `attach domain`
  - w3wp process