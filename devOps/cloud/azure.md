
# Azure
> https://azure.microsoft.com/en-us/services/

## Computation
- **VM** – `$70/month` for a general‑purpose VM (2 CPU, 8 GB RAM, 16 GB disk)  
- **App Service** – formerly “Web App”  
- **Container Instances** – single container  
- **Batch**  
- **Azure Kubernetes Service (AKS)**  
- **Web App for Containers**  

- **Service Fabric**  
- **Cloud Services**  
- **Mobile Apps**  

- **Logic Apps** – similar to Step Functions  
- **Azure Functions** – serverless functions  
- **Azure Load Balancer** – basic; does not support regex routing or request throttling  

## Storage
### Online Transactional Processing (OLTP)
- Azure SQL DB – Microsoft’s relational database service  
- Other open‑source databases  

- Azure Cosmos DB – NoSQL offering from Microsoft  
- Azure Cache for Redis  

- **Azure Storage** (S3 equivalent)  
  - File – alternative to S3  
  - Blob – flat‑folder storage  
  - Disk  
  - Queue  

### Online Analytical Processing (OLAP)
- SQL Warehouse  
- Data Lake Storage – specialised for Hadoop workloads  

## Security
- Azure Active Directory (AD)

## Network
- **VNet** – Microsoft account scope  
  - VNet peering – similar to a VPN tunnel but allows two VNets to communicate directly  
  - VPN – encrypts traffic to a VNet over the public internet  
  - ExpressRoute – dedicated private connection to a VNet, usually offered by data‑center providers  

- Load Balancer – exposes a VNet to the public  

- **Availability**  
  - Region – one data centre location  
  - Zone – multiple data centres within a region (typically > 3)  

### Private Link
> https://docs.microsoft.com/en-us/azure/private-link/

## Billing
- **Billing Account** – company‑level account  
  - **Subscription** – can be organised by department, team, or brand  
    - **Resource Group** – logical container for functions, VMs, databases, etc.  

> Spot instances – cheaper; Azure may shut them down at any time.

```bash
az group list 
az group delete --name xxx

az webapp config appsettings list --name xxxx --resource-group xxx
az webapp config container show --name xxx --resource-group xxx
```

### VM Pricing Tiers
- **Shared** (e.g., F1, D1) – cannot scale out; shared VM resources  
- **Dedicated** (e.g., B1, B2, B3) – own VM; can scale out  
- **Isolated** – dedicated virtual network with maximum scaling  

## Development
```bash
# .NET SDK default path: C:\Program Files (x86)\dotnet
# Add to PATH environment variable

npm install -g azurite
azurite start

# Download & install Microsoft Azure Storage Explorer
# Click “Connect” → “Local storage emulator” → Connect
```

## App Service
> Provides a managed runtime for languages such as C#, PHP, Java, JavaScript, Python, Ruby, and Docker. AD integration is supported. Default path: `/home/site/wwwroot/`.

- **App Service Plan** – defines resource limits; supports auto‑scale up & out; selects runtime  
  - Service (the host machine that runs the web app or container)  
  - Application Insights – analytics (similar to Google Analytics)  
  - Deployment Slots – e.g., blue‑green deployments  
  - Application Configuration – environment settings  
    - Key Vault reference – secret management  

- **Custom Domain** – attach a domain name  
- **Configuration** – environment variables, etc.  

Advanced tools:
- SSH  
- Logs (host log, container default log, MSI proxy log)  

Process: `w3wp` (IIS worker process)
