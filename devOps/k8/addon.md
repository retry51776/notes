# Addons

> Addons / plugins / modules that are not installed by Kubernetes itself and require additional setup.

## Installation Tools

- **kubeadm** – Install production‑grade Kubernetes.
- **kubespray / kargo** – Based on Ansible.
- **kops**
- **k9s**

### Local Development Environments

- **minikube** – Full single‑node cluster.
- **kind** – Run Kubernetes in Docker.
- **k3s** – Lightweight distribution (less common).

### IDE Plugins

- Kubernetes
- Kubernetes Support
- Kubernetes Template
- Helm IntelliSense

### Command‑Line Tools

- `kubectl`
- `helm`
- `kustomize` – Fewer features than Helm but useful for customization.

## Networking Addons

- **Istio** – Service mesh.
- [Node affinity](https://kubernetes.io/docs/reference/scheduling/config/) (`spec.affinity.nodeAffinity`)
- DNS server
- cert‑manager
- Traefik
- NGINX Ingress

## Monitoring Addons

- Kubernetes Dashboard
- Grafana – Monitoring platform.
- Fluentd – Data collector.
- Open Policy Agent (OPA) – Access control.
- Datadog – Enterprise monitoring.
- PagerDuty

## Backup & Restore

- Kasten K10
- Velero

## Other Addons

- Longhorn – Distributed block storage.
- Fleet – Large‑scale deployment of Kubernetes clusters.
- [Datree](https://www.datree.io/) – Deployment file checker.
- Cloudflare PKI/TLS toolkit
- HashiCorp Vault – Secrets management.
- Travis CI

---

## Kubernetes Dashboard

```bash
# Deploy the dashboard
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.5.0/aio/deploy/recommended.yaml

# Expose the API server locally
kubectl proxy

# Create a service account and bind it to the cluster‑admin role
kubectl create serviceaccount dashboard -n default
kubectl create clusterrolebinding dashboard-admin \
  --clusterrole=cluster-admin \
  --serviceaccount=default:dashboard

# Retrieve the access token
kubectl get secret $(kubectl get serviceaccount kubernetes-dashboard \
  -o jsonpath="{.secrets[0].name}") \
  -o jsonpath="{.data.token}" | base64 --decode
```

### Service Mesh Addons

> A service mesh provides advanced networking features, similar to using a cloud proxy, by routing traffic through sidecars.

- **Consul**
- **Envoy**
- **Istio**  
  - `VirtualService` – Similar to an Ingress rule.  
  - `DestinationRule`  
  - `IstioGateway` – Alternative to the built‑in ingress gateway.
- **Kuma**
- **Linkerd**
- **Maesh**
- **Tanzu Service Mesh**

## Advanced Deployment Strategies with VirtualService

- **Canary** – Run two different versions simultaneously.  
- **Blue/Green** – Switch traffic from one version to another after validation.

> Create a service whose selector matches pods of both versions, then use `VirtualService` rules to direct traffic as needed.
