# Prometheus

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