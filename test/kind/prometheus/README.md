#
```bash
helm repo add metrics-server https://kubernetes-sigs.github.io/metrics-server/
helm upgrade --install --set args={--kubelet-insecure-tls} metrics-server metrics-server/metrics-server

https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack
```