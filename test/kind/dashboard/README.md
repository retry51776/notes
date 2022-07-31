## Install k8s dashboard w helm
```bash
kubectl create ns dashboard
kubectl config set-context --current --namespace=dashboard

# Add kubernetes-dashboard repository
helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
# Deploy a Helm Release named "kubernetes-dashboard" using the kubernetes-dashboard chart
helm install \
    kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard
    # --set ingress.enabled=true \
    # --set metricsScraper.enable=true
    # --namespace dashboard \
    # --set metrics-server.enabled=true

# Create Token to access
kubectl apply -f setup.yaml

# sudo vi /etc/hosts  & add
127.0.0.1   https://kubernetes-dashboard.domain.com/
# Force MacOS reload /etc/hosts
sudo killall -HUP mDNSResponder

# Check out UI
https://kubernetes-dashboard.domain.com/

# Post /api/v1/namespaces/{namespace}/serviceaccounts/{name}/token
kubectl get secret -n dashboard kubernetes-dashboard-token -o jsonpath="{.data.token}" | base64 --decode

# By NodePort
# kubectl -n dashboard port-forward service/kubernetes-dashboard 8443:443
# echo https://127.0.0.1:8443/
```