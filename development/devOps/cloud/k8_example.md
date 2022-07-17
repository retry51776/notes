# Deployment
```
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: blue-app
  name: blue-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: blue-app
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: blue-app
        type: canary
    spec:
      volumes:
      - name: host-volume # Where host folder
        hostPath:
          path: /home/docker/blue-shared-volume
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 80
        volumeMounts:
        - mountPath: /usr/share/nginx/html # Where folder inside container
          name: host-volume # Which host folder
      - image: debian
        name: debian
        volumeMounts:
        - mountPath: /host-vol # Where folder inside container
          name: host-volume
        command: ["/bin/sh", "-c", "echo Welcome to BLUE App! > /host-vol/index.html ; sleep infinity"]
```

# Basic Example
> Manually scale `kubectl scale deploy/xxx --replicas 3`
> 
> Desc `kubectl describe node xxx`
```
apiVersion: v1 # Required
kind: [Service|other k8 resources] # Required
metadata: # Required: uniquely identify the object
	name: # Required: k8 object id
	labels: # Optional
		app: # Important: must match to selector
		type:
spec: # Required: desire state
```

# Ingress
> To expose service to public

> Delete Old Ingress, then recreate ingress. Often apply -f won't overwrite

> Or try kubectl replace --force -f xxx.yaml
> 
> layer 7 tcp load balancer
> 
> redirect traffic to different services
> 
> redirect different ip to matching service (nodePort doesn't matter anymore)
> 
> Ingress type: [Custom | External LB | Internal LB]
```
Ingress spec:
metadata:
  annotations:
    kubernetes.io/ingress.class: traefik
spec:
  rules:
  - host: stage.local
    http:
      paths:
      - path: /
        backend:
          serviceName: stage
          servicePort: web
  - host: terry.internal-service.local
    http:
      paths:
      - path: /app1
        backend:
          serviceName: terry-app1
          servicePort: web
      - path: /app2
        backend:
          serviceName: terry-app2
          servicePort: web
  tls:
  - secretName: terry.internal-service.local
```
# Service
> Must declare to expose other services
```
Service spec:
	type: [NodePort|ClusterIP|LoadBalancer] # usually ClusterIP
	ports:
	# ClusterIP: accessable within k8 network
		- port: 80
		- targetPort: 80
		- protocol: TCP
	# NodePort: each pod is accessable by public_ip:port
		- targetPort: 80
		- port: 80
		- nodePort: [30000-32767]
    # LoadBalancer: publish service by single public ip, will ask CLOUD provider for public ip address
	selector:
		app: # Important: Match from metadata.labels
		type: # Important: Match from metadata.labels

# Test by `curl https://node_ip:nodePort/`
```


# Mount Volumn
1. Add volumes to deployment
2. Tell where volumns mount to `volumeMounts`
```
  containers:
  - name: myapp-vol-container
    image: myapp
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
  volumes:
  - name: config-volume
    configMap:
      name: vol-config-map



volumes:
  - gcePersistentDisk
    fsType: ext4
    pdName: test_file
    readOnly: true
containers:
  ...
  name: volume_name 
    volumeMounts:
    - mountPath: /container_folder
      name: volume_name
```


# Add K8 User
```
sudo useradd -s /bin/bash bob
sudo passwd bob

openssl genrsa -out bob.key 2048
openssl req -new -key bob.key -out bob.csr -subj "/CN=bob/O=learner"
// Convert csr to base64
cat bob.csr | base64 | tr -d '\n','%'

vim signing-request.yaml
below is asking k8 premission for certificate we just created
---
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: bob-csr
spec:
  groups:
  - system:authenticated
  request: <assign encoded value from next cat command>
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - digital signature
  - key encipherment
  - client auth

---
// Aprovel Signning Request
kubectl get csr
certificatesigningrequest.certificates.k8s.io/bob-csr approved

// Export Certificate
kubectl get csr bob-csr -o jsonpath='{.status.certificate}' | base64 -d > bob.crt

// Assign bob's credential to key & cert
kubectl config set-credentials bob --client-certificate=bob.crt --client-key=bob.key

// Create context just for bob
kubectl config set-context bob-context --cluster=minikube --namespace=lfs158 --user=bob
kubectl config use-context bob-context
kubectl config set-context --current --namespace=kube-system

//kubectl config view
---
// Give bob role access
vim role.yaml

apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: lfs158
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]

~/rbac$ kubectl create -f role.yaml
```
