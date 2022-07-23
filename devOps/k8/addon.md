# addon

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
- Helm intellisense

// other CMDs
- kubectl
- helm
- kustomize `less feature of helm`
- https://www.datree.io/
- CloudFlare PKI/TLS toolkit

// K8 addons
- kubenete dashboard
- cert-manager
- traefik
- DNS server

// Logging
- ELK `elasticseach, Logstash, Kibana`
- zipkin `distributed tracing system, keep stack trace`


## kubenete dashboard
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.5.0/aio/deploy/recommended.yaml

// expose api_service locally
kubectl proxy

kubectl create serviceaccount dashboard -n default
kubectl create clusterrolebinding dashboard-admin -n default --clusterrole=cluster-admin --serviceaccount=default:dashboard
kubectl get secret $(kubectl get serviceaccount kubernetes-dashboard -o jsonpath="{ secrets[0].name}") -o jsonpath="{.data.token}" | base64 --decode
```

### Service Mesh Addons:
> Service mesh is similar to use cloud proxy, do network trafik through sidcar
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

Advance Deployement
Canary - 2 different version at same time
Blue/Green - Completed switch over
> Create another service with selector able select both version PODs
