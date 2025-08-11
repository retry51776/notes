
# Monitor
> Common DevOps monitoring tools

## Grafana & Its Components
- **Prometheus** – time‑series database  
- **Loki** – log storage (similar to Elasticsearch)  
- **PromQL** – query language for Prometheus  
- **Grafana** – UI, similar to Kibana  

Additional ecosystem:
- **OpenTelemetry** – standard for tracing front‑end services  
- **Tempo** – trace backend storage; provides 100 % trace retention  

`opentelemetry → prometheus → grafana`

## Zabbix
Older, smaller‑scale monitoring solution compared with Grafana stacks.

## ELK
Elasticsearch, Logstash, Kibana – used for logging, similar to Stackdriver.

## Zipkin
Distributed tracing system that keeps stack traces.

## Sentry.io
Web‑based runtime error tracking.

## Datadog
Infrastructure monitoring tool with complex alerts and many integrations (e.g., Jira).

**Datadog components**
- **Datadog Agent** – collects CPU, disk I/O, latency, etc. (default interval 15 s, auto backfill)  
- **API** – programmatic access  
- **Integrations** – built‑in connectors for many services  

## Opsgenie
Simple alert manager.

### Other Tools
- Stackdriver
