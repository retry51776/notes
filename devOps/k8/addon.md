# addon
> Addons / Plugins / Modules not installed by k8s & needs setups.

### Install tools
- kubeadm `Install production k8`
- kubespray/kargo (base off Ansible)
- kops

// K8 local dev
- minikube `Full k8 single cluster single node`
- kind `Run k8 in docker`
- k3s `not common`

// IDE plugins
- kubernetes
- Kubernetes Support
- Kubernetes Template
- Helm intellisense

// CMDs
- kubectl
- helm
- kustomize `less feature of helm`

// K8 Networking addons
- istio `service mesh`
- [spec.affinity.nodeAffinity](https://kubernetes.io/docs/reference/scheduling/config/)
- DNS server
- cert-manager
- traefik
- nginx-ingress


// K8 Monitor addons
- kubenete dashboard
- grafana `monitor platform`
- fluentd `data collector`
- Open Policy Agent(OPA) `access control`
- Datadog `Enterprise monitor`
- pager duty `idk`

// Backup & restore
- Kasten's K10
- Velero

// K8 others addons
- Longhorn `distributed block storage`
- fleet `large scale deployment of Kubernetes clusters`
- https://www.datree.io/ `deployment file checker`
- CloudFlare PKI/TLS toolkit
- hashcorp vault `Secrets Management`
- travis ci





## kubernetes dashboard
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.5.0/aio/deploy/recommended.yaml

// expose api_service locally
kubectl proxy

kubectl create serviceaccount dashboard -n default
kubectl create clusterrolebinding dashboard-admin -n default --clusterrole=cluster-admin --serviceaccount=default:dashboard
kubectl get secret $(kubectl get serviceaccount kubernetes-dashboard -o jsonpath="{ secrets[0].name}") -o jsonpath="{.data.token}" | base64 --decode
```

### Service Mesh Addons:
> Service mesh is similar to use cloud proxy, do network traefik through sidcar
- Consul
- Envoy
- Istio
>> VirtualService `similar to IngressRule`
>> DestinationRule ``
>> IstioGateway `alternate to buildin ingress gateway`
- Kuma
- Linkerd
- Maesh
- Tanzu Service Mesh

Advance Deployments w VirtualService
- Canary `2 different version at same time`
- Blue/Green `Completed switch over`
> Create another service with selector able select both version PODs
