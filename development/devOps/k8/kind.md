# Kind
> running k8 image inside docker, k8 image have docker, so it's docker runtime(control plane) inside docker container(host docker)
> 
> Allow multi k8 cluster, minikube can't do multi cluster in same host
> 
> https://kind.sigs.k8s.io/docs/
> 
> https://kind.sigs.k8s.io/docs/user/loadbalancer/


## Setup
```bash
kind create cluster --config demo.yml

# Load image
docker build -t my-custom-image:unique-tag ./my-image-dir
kind load docker-image my-custom-image:unique-tag
kubectl apply -f my-manifest-using-my-image:unique-tag
```