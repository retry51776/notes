# DevOps
> Fancy words go here, because DevOps has tons of them.

## Operational Burdens
- CI / CD  
- Production stability (CT)  
- Meetings  
- Stack maintenance  
- Documentation  
- Unit testing  

## DevOps Metrics
- Deployment frequency  
- Lead time *from commit to master to deployment*  
- Mean Time to Recovery  
- Change Failure Rate *hotfixes / deployments*  
- Cycle time *aka development time, which most managers care about*

### Four Fundamental Topologies
- **Stream‑aligned team**: aligned to a flow of work from a specific business domain.  
- **Enabling team**: helps a stream‑aligned team overcome obstacles and fills missing capabilities.  
- **Complicated subsystem team**: required for areas needing deep expertise (e.g., complex mathematics).  
- **Platform team**: provides an internal product that accelerates delivery for stream‑aligned teams.

## Project Checklist
- Install  
- Config *developers often forget to document*  
- Provision  
- Deploy  

- Security  
- Monitoring  
- Backup & restore  

- Network  
- High availability  
- Scalability  
- Performance  

- Cost  
- Documentation  
- Testing  

### Deployment Strategies
- **Blue‑Green** – swap all at once; K8s service mesh VirtualService.  
- **Rolling update** – run different versions simultaneously.  
- **Recreate** – offline gap during deployment.  
- **Canary** – roll out to a small subset of users, then increase.  
- **A/B** – target specific subjects for updates.  
- **Shadow** – duplicate traffic to a test version.

## JIRA
- RELEASE MANAGEMENT – auto‑generate release notes
