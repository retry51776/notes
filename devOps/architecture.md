# Architecture
> I worked for a small company. We don't have everything listed here. I wish we had at least half of the stuff.

## Web Service

DNS → Load Balancer → Gunicorn instance → Gunicorn workers → Flask

## CI / CD / Continuous Tracking (CT)

1. **Source**
   1. Linting  
   2. Unit tests  
      1. Code coverage  
   3. Branch protection  
   4. Branch strategies  
      1. Trunk‑based (committing directly to main is discouraged)  
      2. Feature branching (most common)  
      3. Fork branching (common in open source)  
      4. Release branching (waterfall or multi‑version support)  
      5. Git flow (release branch, requires a release manager)  
      6. Environment branching (both environment and release branches)

2. **Build** (GitHub Actions)
   1. Build image (multi‑stage if compilation is needed)  
   2. Publish image/package with an alpha tag  
   3. Send a message (image name / package name & version, related tests) to the test engine

3. **Test Engine** (consumer engine)
   1. Rebuild and run affected services (K8s deployment update? or single‑box environment?)  
   2. Integration, behavior, UI tests  
      - Selenium  
      - Custom Python scripts?  
   3. Store test results  
   4. Deploy image / publish package

4. **Develop Environment**
   1. Create a release branch  
   2. QA team fixes bugs  
   3. Merge master & develop  

5. **Production Environment**
   1. Rollback alarm (auto‑rollback)  
   2. Canary or A/B deployment  
      - DNS weight  
      - Baking period  
   3. Deployment patterns  
      - Recreate (for SAP, resources with hash, okay with downtime)  
      - Rolling update (engine, microservice)  
      - Blue‑green (HA, resources with hash)  
      - Canary  
      - A/B  
      - Shadow (Android app, critical engine & service)  
      - Geo‑based rollout  

6. **Monitoring / Tracking** ([monitor.md](./cloud/monitor.md))
   1. Logs (ELK)  
   2. Capture runtime errors (Sentry.io)  
   3. Alerts (Opsgenie)  
   4. Metrics (Grafana / Zabbix)  
   5. Tracing (Zipkin)

7. **Support**
   1. ServiceNow or Zendesk  

> Put all integration tests in a Python package.

### Black‑box Metrics

#### Response Metrics
- Mean Time to Detect (MTTD)  
- Mean Time to Acknowledge (MTTA)  
- Mean Time to Recovery (MTTR)  
- Mean Time to Contain (MTTC)  
- System availability  
- SLA compliance  
- Mean Time Between Failures (MTBF)

#### Performance Metrics
1. Requests per minute (RPM)  
2. Average and max latency  
3. Errors per minute  
4. API usage growth  
5. Uptime / Availability  
6. CPU usage  
7. Memory usage  
8. Unique API consumers  

### Log Databases
- Prometheus `time‑series database`  
- Elasticsearch `search engine, fast aggregation, supports many languages`  
- Splunk `used by large enterprises`  
- MongoDB `slower aggregation because single‑thread map‑reduce`

## Testing Strategies
- Top‑down  
- Bottom‑up  
- Big Bang  
- Sandwich  

## Migration Strategy
- Rehost `Lift & Shift`  
- Refactor `minor app changes`  
- Revise `medium app changes`  
- Rebuild `major rewrite`  
- Replace `potentially better solution`

## API Versioning Strategies
- URL pattern  
- Custom header  
- Query‑parameter versioning  

## Buzzwords
- Access Pattern  
  - Random  
  - Sequential  
- Product Hygiene `features not essential to core function but reduce problems (platform management, input validation)`  

- Direct Memory Access (DMA)  
- Proximity service `common business request`

### Collaborative Editing
- Multi‑user mode (e.g., Google Docs, Etherpad)

> **Pessimistic Control** `aka lock`  

> **Optimistic Concurrency Control** `versioning & merge`  

>> Operational Transformation / Event Passing `each operation is an event; client converts other events into op_delta before merging`  

>> Differential Sync `aka Git`
