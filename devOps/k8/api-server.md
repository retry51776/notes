# API Server

> Takes 20–40 seconds for an api‑server restart.

> Configuration is stored on the master node at `/etc/kubernetes/manifests/kube-apiserver.yaml`.
- Prefer versioned store format.

## Commands

```bash
# List resources
kubectl api-resources

# Access API Server
# 1. Using certificates
curl http://localhost:6443 -k \
    --key admin.key \
    --cert admin.crt \
    --cacert ca.crt

# 2. Via kubectl proxy
kubectl proxy   # Serves at localhost:8001
```

### API Groups

- `/api`
  - `/v1` – core groups (e.g., `ns`, `pod`, `rc`, `event`, `ep`, `nodes`, `bindings`, `pv`, `pvc`, `cm`, `secrets`, `service`)
    - v1 – core group version
      - resources: *(list omitted)*
- `/apis`
  - `/v1` – additional API groups (`apps`, `extensions`, `networking.k8s.io`, `storage.k8.io`, `authentication.k8s.io`)
    - v1 – resources: *(list omitted)*

### Add an Extra Parameter to the API Server

```bash
sudo cp /etc/kubernetes/manifests/kube-apiserver.yaml /kube-apiserver-backup
```
