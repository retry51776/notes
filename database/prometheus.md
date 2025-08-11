# Prometheus

## Types of Metrics
- Counter  
- Gauge  
- Histogram  

## Components
- Alertmanager  
- kube‑state‑metrics  
- node exporter  
- pushgateway  
- Prometheus server  

```bash
# Sample data
kubectl get --raw /metrics
```

### Install Metric Server
```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### Deploy Prometheus with Helm
```bash
# Create namespace
kubectl create namespace prometheus

# Add Helm repo
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

# Install / upgrade
helm upgrade -i prometheus prometheus-community/prometheus \
    --namespace prometheus \
    --set alertmanager.persistentVolume.storageClass="gp2",server.persistentVolume.storageClass="gp2"
```

The UI is available at `http://localhost:9090`.

## Exporters
Exporters convert data into a format Prometheus understands and expose it on a `/metrics` endpoint.

## Pushgateway
Used for short‑lived jobs that cannot be scraped directly.

## PromQL Basics

```promql
metric_name{
    label="value",
    other_label=~"regex|alternatives",
    another_label!="excluded"
} offset 1w
```

### Example Queries
```promql
count by (label_x) (
    rate(metric_name{label="xxx"}[5m])
) > 500
```

* `rate()` returns per‑second values; multiply by 60 to get per‑minute.
* Use range vectors (`[5m]`) for rates over a time window.

## Writing Exporter Code (Python example)

```python
from prometheus_client import CollectorRegistry, Gauge

def configure_metrics(mapping):
    registry = CollectorRegistry()
    mapping['prometheus_registry'] = registry
    mapping['level_gauge'] = Gauge(
        'level',
        'The level metric',
        registry=registry
    )

def updater(request):
    request.registry['hits'].inc()
    request.registry['level_gauge'].set(x)
    registry = request.registry['prometheus_registry']
    return Response(
        generate_latest(registry),
        content_type='text/plain; version=0.0.4'
    )
```

## Grafana
Use the following pattern for metric names:

```
{{server}}_{{label}}
```
