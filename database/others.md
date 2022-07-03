Prometheus
3 types:
- counter
- Gauge
- Histogram

Exporters: convert data into Prometeus understand format, then expose it /metrics endpoint

Push system, defined by prometheus.yml
PromQL

https://github.com/google/re2/wiki/Syntax

```
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
```
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