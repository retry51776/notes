# Prometheus

3 types:
- counter
- Gauge
- Histogram

## Components
- alert manager
- kube state metrics
- node exporter
- pushgateway
- prometheus server

```bash
# Data sample
kubectl get --raw /metrics

# Install Metric Server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# https://docs.aws.amazon.com/eks/latest/userguide/prometheus.html
kubectl create namespace prometheus
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm upgrade -i prometheus prometheus-community/prometheus \
    --namespace prometheus \
    --set alertmanager.persistentVolume.storageClass="gp2",server.persistentVolume.storageClass="gp2"

# localhost:9090
```


Exporters: convert data into Prometeus understand format, then expose it /metrics endpoint

Push system, defined by prometheus.yml
PromQL

https://github.com/google/re2/wiki/Syntax

```js
metrix_name{
    [label]=[value],
    label=~"text1|text2"
    label!="text"
    label=~"text[1-9]"
} offset 1w

count by (label_x) ( rate(mextrix_name {
    label = "xxx"
} [5m])) > 500 //range vector

rate() * 60 default is by seconds,
# Series <op>
() > 1
```

constMetrics
## Exporter
> don't do match to create metrics

> don't put unit in metric name, put it in metrics's label
```py
# Pyramid Service: Metric Configuration
# mapping is DB
def configure_metrics(mapping):
    registry = CollectorRegistry() # Defined Schema
    mapping['prometheus_registry'] = registry # Tight Schema to DB
    mapping['level'] = Gauge( # Defined metrics/column
        'level',
        'The Level',
        registry= registry
    ) 

def updater(request):

    request.resigtry['hits'].inc()
    request.resigtry['level'].set(x)
    registry = request.resigtry['prometheus_registry']
    return Response(
        generate_latest(resistry),
        content_type=xxx
    )
```
# Grafana
```
{{server}}_{{label}}
```