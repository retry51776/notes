# Kind
> running k8 image inside docker, k8 image have docker runtime, so it's docker runtime(control plane) inside docker container(host docker)
> 
> Allow multi k8 cluster, minikube can't do multi cluster in same host!
> But can NOT stop or restart cluster! only load image
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

# Pause Cluster
docker start kind-control-plane && docker exec kind-control-plane sh -c 'mount -o remount,ro /sys; kill -USR1 1'
docker start kind-worker && docker exec kind-worker sh -c 'mount -o remount,ro /sys; kill -USR1 1'
docker pause kind-control-plane
docker pause kind-worker

# Resume Cluster
docker unpause kind-control-plane
docker unpause kind-worker
```

# Yml
```yml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
certificate-authority-data: ooooo
server: https://1.1.1.1:1234
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    listenAddress: "0.0.0.0" # Optional, defaults to "0.0.0.0"
- role: worker
```