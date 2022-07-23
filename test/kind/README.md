# Kind
> Stuff that I needs to do

## Create Cluster
1.  `kind create cluster --config demo.yml`

## Install k8s dashboard w helm
```bash
# Add kubernetes-dashboard repository
helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
# Deploy a Helm Release named "kubernetes-dashboard" using the kubernetes-dashboard chart
helm install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard

# Post /api/v1/namespaces/{namespace}/serviceaccounts/{name}/token

kubectl get secret $(kubectl get sa kubernetes-dashboard -o jsonpath="{ secrets[0].name}") -o jsonpath="{.data.token}" | base64 --decode

# Create Token to access
kubectl apply -f dashboard-admin.yaml

export POD_NAME=$(kubectl get pods -n default -l "app.kubernetes.io/name=kubernetes-dashboard,app.kubernetes.io/instance=kubernetes-dashboard" -o jsonpath="{.items[0].metadata.name}")
echo https://127.0.0.1:8443/
kubectl -n default port-forward $POD_NAME 8443:8443
```

## Install Nginx Ingress
1.  `kubectl apply -f usage.yaml`
2.  `kubectl apply -f nginx-ingress.yaml`
3.  ``

## Install TLS

## Test Endpoint
> do simple ping or curl to make sure endpoint works inside k8s
```bash
# ep only exposed to k8s, so you must exec into k8 pod to test
kubectl exec -it some_pod sh
# get ep's k8 internal ip & port
kubectl get ep
# -k insecure
curl -k https://10.244.1.2:8443
```


## Test Service
```bash
kubectl exec -it some_pod sh
wget bar-service:5678
# systemctl status firewalld
```

## Test by NodePort Forward
```bash
# Get Node IP
kubectl get nodes -o wide

# Get POD ID
kubectl -n ingress-nginx get pods

# Start NodePort Forward
kubectl -n ingress-nginx port-forward ingress-nginx-controller-86b6d5756c-xtskx 8000:80

# Test in browser http://127.0.0.1:8000

```

## Test /etc/hosts
```bash
cd /etc
sudo vi /etc/host
#127.0.0.1      k8-dashboard.local

ping k8-dashboard.local
```