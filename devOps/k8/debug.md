# Debug
> 80% K8s problems are networking, configMap, secrets;
> 
> 1. Looks though events, k8s object status;
> 2. Check Pod Logs;
> 3. Test around inside POD;
> 4. Check permission
> 5. Check sidecar

### Commons Errors
- Error Validating data
- SchedulingDisabled
- ImagePullBackoff
- CashLoopBackoff
- CreateContainerError
- Probe Failing
- RunContainerError
- Exceed CPU Limits
- FailedScheduling
- Failed Mount
- Kubelet crash

## Debugging Inside POD
```bash
kubectl -n shopping exec -it shopping-api -- bash
# command: ["sleep", "infinity"]
chmox +x xxx.sh

# Read more in Networking.md
ping xxx-service
curl -k 1.1.1.1
nslookup xxx
```

## Debugging Inside Node
```bash
systemctl restart kubelet

# Directly ssh into node; $HOME/.ssh/kube_rsa
ssh -i <path of the private key file> admin@<ip of the aws kube instances>

# Read more in kubelet.md
```

## Debugging On Client Side / Node
#### Common Debug
```bash
# Did you forget some secrets or configMap?
kubectl get events
# What is deployment status?
kubectl describe deploy xxx
# Test selector
kubectl get pods --selector=xxx=xxx_label


# Often apply -f won't overwrite
kubectl replace --force -f xxx.yaml
# Delete Old Ingress, then recreate ingress
kubectl delete -f <filename>
# Rollback deployment
kubectl rollout undo deployment my-application

# Use kubectl convert yml to different k8 versions
kubectl convert --help
# Admin testing
kubectl --as=xxxx_user get all
kubectl --as-group=xxx get all
```

#### Client Side Networking
```bash
# Check host DNS
systemd-resolve --status | grep 'DNS Servers' --after 5
# Add IP routing in Host
sudo ip route add 10.96.0.0/12 via 172.18.0.2

# Show all process
ps auxww

# Lazy way
# chrome://flags/#allow-insecure-localhost

# Generate k8 secets
htpasswd -nb [ -m | -B | -d | -s | -p ] [ -C cost ] username password

#  see what used address
Get-Process -Id (Get-NetTCPConnection -LocalPort YourPortNumberHere).OwningProcess
```

directly access api_server
```bash
# Point to the internal API server hostname
APISERVER=https://kubernetes.default.svc

# Path to ServiceAccount token
SERVICEACCOUNT=/var/run/secrets/kubernetes.io/serviceaccount

# Read this Pod's namespace
NAMESPACE=$(cat ${SERVICEACCOUNT}/namespace)

# Read the ServiceAccount bearer token
TOKEN=$(cat ${SERVICEACCOUNT}/token)

# Reference the internal certificate authority (CA)
CACERT=${SERVICEACCOUNT}/ca.crt

# List pods through the API
curl --cacert ${CACERT} --header "Authorization: Bearer $TOKEN" -s ${APISERVER}/api/v1/namespaces/shopping/pods/ 

# Insecure way
curl --header "Authorization: Bearer $TOKEN" -s ${APISERVER}/api/v1/namespaces/shopping/pods/ --insecure
```


# Create Token for Dashboard
```yml
apiVersion: v1
kind: Secret
metadata:
 name: kubernetes-dashboard-token
 annotations:
   kubernetes.io/service-account.name: kubernetes-dashboard
type: kubernetes.io/service-account-token
# Get Token
kubectl get secrets/kubernetes-dashboard-token -o yaml
# base64 decoded start with e
echo xxxx | base64 -d
# base64 encoded start with LS 
# echo xxxx | base64 -w 0
npm install -g jwt-cli
jwt xxxxx
```