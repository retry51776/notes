## Install Cert-Manager TLS
> https://cert-manager.io/docs/installation/
```bash
# Step 1: Install cert-manager
helm repo add jetstack https://charts.jetstack.io
kubectl create ns cert-manager
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.8.2 \
  --set installCRDs=true

# Step 2: Create Issuer & Certificate
kubectl apply -f setup.yaml
kubectl get secrets
kubectl get certificates
```
