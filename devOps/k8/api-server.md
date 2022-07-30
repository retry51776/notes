# API Server
> takes 20-40 seconds for api-server restart

> config is store in master node `/etc/kubernetes/manifests/kube-apiserver.yaml`
- Prefer Version `store format`

## CMDs
```bash
# list resources
kubectl api-resources

# Access ApiServer
# 1. By cert
curl http://localhost:6443 -k
    --key admin.key
    --cert admin.crt
    --cacert ca.crt
# 2. By kubectl proxy
kubectl proxy 
localhost:8001
```
# api-groups
- /api
  - /v1 `k8s version`
    - core groups `[ns, pod, rc, event, ep, nodes, bindings, pv, pvc, cm, secrets, service]`
      - v1 `core group version`
        - resource ``
- /apis
  - /v1
    - api groups `[apps, extensions, networking.k8s.io, storage.k8.io, authentication.k8s.io]`
      - v1
        - resource
# Add extra param to apiserver
`sudo cp /etc/kubernetes/manifests/kube-apiserver.yamml /kube-apiserver-backup`

