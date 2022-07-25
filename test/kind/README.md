# Kind
> Follow steps to create k8s cluster with kind, setup example NakePods, Service, Ingress, & External LoadBalancer

## Setup Cluster
1.  `kind create cluster --config cluster.yml`
2.  Install Ingress Nginx Controller`kubectl apply -f nginx-ingress.yaml`
3.  Deploy example bar-app & bar-service `kubectl apply -f example.yaml`


## Test Endpoint
> do simple ping or curl to make sure endpoint works inside k8s
```bash
# ep only exposed to k8s, so you must exec into k8 pod to test
kubectl exec -it bar-app sh
# get ep's k8 internal ip & port
kubectl get ep
# -k insecure
curl -k https://10.244.1.2:8443
```

## Test Service
```bash
kubectl exec -it some_pod sh
wget bar-service:5678
# systemctl status firewalld
```

## Test Ingress
> Setup Ingress NodePort Forward
```bash
# Get Node IP
kubectl get nodes -o wide

# Get POD ID
kubectl -n ingress-nginx get pods

# Start NodePort Forward
kubectl -n ingress-nginx port-forward ingress-nginx-controller-66n8m 8000:80

# Test in browser http://127.0.0.1:8000
```

## Setup Reverse Proxy & Edit /etc/hosts
```bash
# Setup Reverse Proxy
brew install nginx
vi /opt/homebrew/etc/nginx/nginx.config
# create reverse proxy to ingress port fortwarding
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

# Edit /etc/hosts
cd /etc
sudo vi /etc/hosts
# Add record into /etc/hosts
# 127.0.0.1      k8.local

sudo killall -HUP mDNSResponder
# Test in browser http://k8.local/
```