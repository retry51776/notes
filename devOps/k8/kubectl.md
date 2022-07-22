# Kubectl

## Control / Deployment
```bash
# Manually scale
kubectl scale deploy/xxx --replicas 3

# Port forward Pod to test locally: Ex: nginx-8f458dc5b-bn4dr
export POD_NAME=$(kubectl get pods -n default -l "app.kubernetes.io/name=kubernetes-dashboard,app.kubernetes.io/instance=kubernetes-dashboard" -o jsonpath="{.items[0].metadata.name}")
#                               pod_name        host_port:pod_port
kubectl -n default port-forward nginx-8f458dc5b-bn4dr 1234:80
# Access through browser
echo http://localhost:1234

```

## Basic Example
```bash
# get more detail/status on k8 objects, common 1st step to debug
kubectl describe node xxx

kubectl create deployment nginx --image nginx
kubectl expose deploy nginx --port 80 --type LoadBalancer


# Admin testing
kubectl --as=xxxx_user get all
kubectl --as-group=xxx get all
```

```
```