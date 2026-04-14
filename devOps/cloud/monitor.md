
# Monitor
>
> Common DevOps monitoring tools

## Grafana & Its Components

- **Prometheus** – time‑series database  
- **Loki** – log storage (similar to Elasticsearch)  
- **PromQL** – query language for Prometheus  
- **Grafana** – UI, similar to Kibana  

Additional ecosystem:

- **Tempo** – trace backend storage; provides 100% trace retention

`opentelemetry → prometheus → grafana`

## opentelemetry

> **OpenTelemetry** – standard for tracing front‑end services, do NOT include backend storage system.

- 1. Instrumentation API	`how your app reports data (traces, metrics, logs)`
  - `trace_id` = global request ID
  - `span_id`  = per-service step
  - Upstream Service inject `traceparent` to downstream service, or manually inject into request's header
- 2. SDK `collects + batches + processes data`
- 3. Exporter `sends data to a backend in OTLP format`
  - Traces `request flow, tree structured`
  - Metrics `numeric time series`
  - Logs `raw events, annotation json`

Common backends(Observability Platforms):

- Managed:
  - Datadog
  - New Relic
  - Honeycomb
- Open Source:
  - Grafana stack
    - Tempo (traces)
    - Mimir (metrics)
    - Loki (logs)
  - Zipkin (traces)
  - SigNoz
- Neocloud internal:
  - Stackdriver / Google Cloud Operations
  - Amazon CloudWatch
  - Azure Monitor


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

## Langfuse

- Backend
  - Organization
    - Project
      - session (group by user_id or session_id)
        - trace (one request / workflow) `OpenTelemetry trace`
          - spans (workflow step)
            - generation

- Client
  - SDK
    - Client Instance
      - Trace
        - Observation (span / generation)
          - input
          - output
          - model
          - usage
          - metadata
          - score

```py
npx skills add langfuse/skills --skill "langfuse"

LANGFUSE_PUBLIC_KEY
LANGFUSE_BASE_URL

# langfuse Wrapper
from langfuse.openai import openai
```
