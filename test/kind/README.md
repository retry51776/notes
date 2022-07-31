# Kind
> Follow steps to create k8s cluster with kind, setup example NakePods, Service, Ingress, & External LoadBalancer

## Setup Cluster
1.  `kind create cluster --config cluster.yml`
2.  Install Ingress Nginx Controller`kubectl apply -f nginx-ingress.yaml`
3.  Deploy example bar-app & bar-service `kubectl apply -f example.yaml`


## Test Endpoint
> do simple ping or curl to make sure endpoint works inside k8s
```bash
# get ep's k8 internal ip & port
kubectl get ep
# ep only exposed to k8s, so you must exec into k8 pod to test
kubectl exec -it bar-app sh
# -k insecure
curl <foo_service_ip>
```

## Test Service
```bash
kubectl exec -it foo-app sh
wget foo-service:5678
# systemctl status firewalls
```
## Edit /etc/hosts
```bash
# Edit /etc/hosts
cd /etc
sudo vi /etc/hosts
# Add record into /etc/hosts
# 127.0.0.1      k8.local

# Force MacOS reload /etc/hosts
sudo killall -HUP mDNSResponder
# Test in browser http://k8.local/
``` 



## Setup NodePort Forward, Reverse Proxy (Optional)
> Only do this when you can't setup extraPortMappings.
```bash
# Get Node IP
kubectl get nodes -o wide

# Get POD ID
kubectl -n ingress-nginx get pods

# Start Port Forward on Ingress Service                       host_port:service_port 
kubectl -n ingress-nginx port-forward service/ingress-nginx-controller 8000:80
# Most the time Port Forward Service or Pod.
# Start Port Forward on Deployment or Daemonset
# kubectl port-forward deployment/xxx <host_port>:<pod_port>
# Start Port Forward on Single Ingress Controller             host_port:pod_port
# kubectl -n ingress-nginx port-forward ingress-nginx-controller-gftjn 8000:88

# Test in browser http://127.0.0.1:8000

# Setup Reverse Proxy
brew install nginx
vi /opt/homebrew/etc/nginx/nginx.config
# create reverse proxy to ingress port forwarding
    server {
        listen       80;
        server_name  localhost k8.local www.k8.local;

        location / {
            proxy_pass  http://localhost:8000;
            proxy_set_header Host       localhost:8000;
        }
    }

sudo brew services start nginx
sudo brew services restart nginx
```