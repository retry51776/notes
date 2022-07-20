# Debug
> I needs to collect all network debugging cmds here.
```bash
# Lazy way
chrome://flags/#allow-insecure-localhost

# Delete bad install
kubectl delete -f <filename>
# Rollback deployment
kubectl rollout undo deployment my-application
```
# curl API_Service 
```bash
# Debug
kubectl -n shopping exec -it shopping-api -- bash

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

```

# Release used address
```powershell
Get-Process -Id (Get-NetTCPConnection -LocalPort YourPortNumberHere).OwningProcess

# Create Token
apiVersion: v1
kind: Secret
metadata:
 name: kubernetes-dashboard-token
 annotations:
   kubernetes.io/service-account.name: kubernetes-dashboard
type: kubernetes.io/service-account-token
# Get Token
kubectl get secrets/kubernetes-dashboard-token -o yaml
echo xxxx | base64 -d
npm install -g jwt-cli
jwt xxxxx
```