# Kubectl Cheat Sheet

`kubectl` has many parameters and sub‑commands. Since each Kubernetes object is split into its own file, related `kubectl` commands are scattered throughout the repository.

## Control / Deployment

> See more in [basic k8s sample](./../../test/kind/README.md).

## Debug

> See more in [debug tips & commands](./debug.md).

## Client Settings

```bash
# View current kubeconfig
kubectl config view

# Override default config path
# Default: ~/.kube/config or /Users/<user>/ .kube/config
export KUBECONFIG=~/.kube/new-config
```

### Namespace Management

```bash
# List namespaces
kubectl get ns

# Switch namespace
kubectl config set-context --current --namespace=kube-system
```

## Manage / Operations

```bash
# Scale a deployment manually
kubectl scale deploy/xxx --replicas 3

# Drain pods from a node
kubectl drain <node-name> --ignore-daemonsets --force --delete-local-data

# Port‑forward a Pod (example: nginx)
export POD_NAME=$(kubectl get pods -n default -l "app.kubernetes.io/name=kubernetes-dashboard,app.kubernetes.io/instance=kubernetes-dashboard" -o jsonpath="{.items[0].metadata.name}")

kubectl -n default port-forward $POD_NAME 1111:80

# Expose the API server locally
kubectl proxy
# Directly view deployments via the API:
# http://127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments
```

## Basic Examples

### Imperative Commands

```bash
kubectl run myapp --image=myimage --port=80
kubectl expose deploy nginx --port 80 --type LoadBalancer
kubectl autoscale deployment foo --min=2 --max=10 --cpu-percent=80
```

### Declarative Commands

```bash
# Get detailed status of a node
kubectl describe node xxx

# Create resources from a manifest
kubectl create -f mymanifest.yaml

# Create a job from an existing CronJob
kubectl create job --from=cronjob/mycronjob name-of-one‑off-job

# Execute a command in a Pod
kubectl exec -it pod-name -- sh

# Rollout operations
kubectl rollout restart deployment xyz
kubectl rollout undo deployment myapp
kubectl rollout history deploy myapp --revision=2
```

### Resource Types

```bash
kubectl api-resources
```

```bash
kubectl explain deployment.spec.template
```

## Verb‑list (for **`kubectl get`**)

| Verb   | Description |
|-------|--------------|
| create | Create a **new** resource |
| delete | Delete **existing** ​​​  ?  ?  ?  ?  ?  ?  ? ?  ? … 



```

devOps/k8/vault.md
