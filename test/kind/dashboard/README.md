## Install k8s dashboard w helm
```bash
# Add kubernetes-dashboard repository
helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
# Deploy a Helm Release named "kubernetes-dashboard" using the kubernetes-dashboard chart
helm install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard

# Create Token to access
kubectl apply -f dashboard-setup.yaml

# Post /api/v1/namespaces/{namespace}/serviceaccounts/{name}/token
kubectl get secret kubernetes-dashboard-token -o jsonpath="{.data.token}" | base64 --decode

kubectl port-forward kubernetes-dashboard-7d6c98b5d4-ffnmj 8443:8443
echo https://127.0.0.1:8443/
```