# Prometheus
```bash
# Step 1. Install metrics-service addon
helm repo add metrics-server https://kubernetes-sigs.github.io/metrics-server/
helm upgrade --install \
    metrics-server metrics-server/metrics-server \
    --set args={--kubelet-insecure-tls} 

https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack
```