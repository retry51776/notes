# minikube
> On windows hypervisor platform
>
> is single cluster single node k8 dev env without img reg, ability to build image
> 
> minikube.sigs.k8s.io/docs/


## Setup
```bash
brew install minikube
minikube addons enable ingress
minikube addons enable ingress-dns

# to access k8 service
minikube tunnel
minikube service --namespace kube-system --all


/var/lib/minikube/certs/
# to test ClustIP
minikube ssh | gcloud compute ssh <NODE_NAME> --zone <ZONE>
# endpoint is POD's IP
curl endpoint:port
# Each Service has kubeproxy virtual IP
curl service_ip
```