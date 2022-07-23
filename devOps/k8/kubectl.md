# Kubectl

## Setting
```bash
kubectl config view
# Overwrite Default Config Paths
# ~/.kube/config or /Users/<user_name>/.kube/config
export KUBECONFIG=~/.kube/new-config
```

## Control / Deployment
```bash
# Manually scale
kubectl scale deploy/xxx --replicas 3
# Drain pods from node
kubectl drain <node name> --ignore-daemonsets --force --delete-local-data

# Port forward Pod to test locally: Ex: nginx-8f458dc5b-bn4dr
export POD_NAME=$(kubectl get pods -n default -l "app.kubernetes.io/name=kubernetes-dashboard,app.kubernetes.io/instance=kubernetes-dashboard" -o jsonpath="{.items[0].metadata.name}")
#                               pod_name        host_port:pod_port
kubectl -n default port-forward ingress-nginx-controller-76d4b989c5-dhqbr 1111:80
# Access through browser
echo http://localhost:1234

```

## Basic Example
```bash
# get more detail/status on k8 objects, common 1st step to debug
kubectl describe node xxx

kubectl create deployment nginx --image nginx
kubectl expose deploy nginx --port 80 --type LoadBalancer

kubectl create job --from=cronjob/mycronjob name-of-one-off-job
kubectl run XXXX --images=XXXX --port=80  
kubectl exec -it pod-name sh
kubectl rollout restart deployment xyz
kubectl rollout undo deployment myapp
kubectl rollout history deploy myapp --revision=2

# Almost never do this in Production, will create service & ingress
kubectl expose deployment XXXX --type="LoadBalancer" service "XXXX" exposed  

# verbs: [create delete deletecollection patch update get list watch]
# k8 object [
#   always: ing(ingress), pod, svc(service), deploy(deployments), no(node), secrets, cj(cronjob)
#   often: cm(configmaps), ep(endpoint), sa(service account), ns(namespace), role/clusterRole, roleBinding/clusterRoleBinding, dm(daemonset)
#   looked: csr(CertSignReq), hpa(horizatialPodAutoscale), NetworkPolicy, 
#   never: cs(componentstatuses), ev(events), pdb(poddisruptionbudgets), psp(podsecuritypolicies), pc(priorityclasses)
# ]

kubectl api-resources
# Expose api-service locally
kubectl proxy

kubectl explain deployment.spec.template

# Admin testing
kubectl --as=xxxx_user get all
kubectl --as-group=xxx get all
```

```
```