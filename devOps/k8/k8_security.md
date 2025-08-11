# K8s Security

> TLS/SSL certificates, service mesh.

## Add‑ons

### cert‑manager
Simplifies obtaining, renewing, and using certificates.

1. Create a CA certificate & key.
2. Create a `ClusterIssuer`.
3. Create a `Certificate`.
4. Create a Secret.
5. Configure Ingress.

```yaml
kind: Secret
data:
  tls.crt: $(cat xxx.pem | base64 | tr -d '\n')
  tls.key: $(cat xxx-key.pem | base64 | tr -d '\n')
```

### keycloak
Client‑application authorization.

### Kubernetes Dashboard

## Secrets
Application‑layer encryption for secrets.

## HashiCorp Vault Add‑on

| Built‑in Type                     | Usage                                            |
|-----------------------------------|--------------------------------------------------|
| Opaque                            | Arbitrary user‑defined data                      |
| kubernetes.io/service-account-token | ServiceAccount token                           |
| kubernetes.io/dockercfg           | Serialized `~/.dockercfg` file                  |
| kubernetes.io/dockerconfigjson    | Serialized `~/.docker/config.json` file         |
| kubernetes.io/basic-auth          | Credentials for basic authentication            |
| kubernetes.io/ssh-auth           | SSH credentials                                 |
| kubernetes.io/tls                | TLS client or server data                       |
| bootstrap.kubernetes.io/token     | Bootstrap token data                            |

## Authentication

Normal users are managed by independent services such as user/client certificates.  
Service accounts communicate with the API server to perform various operations.

> Users/clients now connect to a Service via its `ClusterIP`, which forwards traffic to one of the Pods attached to it. A Service provides load balancing by default while selecting the Pods for traffic forwarding.

### Methods

1. **Certificates** – CA certificates are stored on control‑plane nodes at `/etc/kubernetes/pki`.

   ```bash
   # Step 1: Create client key & sign with CA
   openssl req -new -key xxx.key -out xxx.csr "/CN=fname lname/O=HR"
   openssl x509 -req -in xxx.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out xxx.crt -days 500

   # Alternative: use kubectl to approve
   kubectl certificate approve xxx.csr
   kubectl get csr/xxx -o yaml
   kubectl get csr xxx -o jsonpath='{.status.certificate}' | base64 -d > xxx.crt

   # Step 2: Add to kubeconfig
   kubectl config set-cluster xxx-cluster --server=https://1.1.1.1:52807 \
       --certificate-authority=ca.crt --embed-certs=true
   kubectl config set-credentials xxx --client-certificate=xxx.crt \
       --client-key=xxx.key --embed-certs=true
   kubectl config set-context dev --cluster=dev --namespace=default --user=xxx
   kubectl config use-context dev

   # Step 3: Create Role & RoleBinding
   # (example role YAML omitted)
   kubectl apply -f xxx_role.yml
   ```

2. **OAuth** – Kubernetes receives a `group_id` and an OAuth token.

   ```bash
   # Retrieve the default ServiceAccount secret
   kubectl get secret default-token-2mfqv --namespace={namespace} -o yaml

   # New since v1.24
   kubectl create token SERVICE_ACCOUNT_NAME

   # Old method
   kubectl get secret "$(kubectl get serviceaccount default -o jsonpath='{.secrets[0].name}')"
   ```

   ```yaml
   kind: Pod
   spec:
     containers:
       - image: nginx
         name: nginx
     serviceAccountName: nginx-service
   ```

### Authentication Modules

- X509 client certificates (standard)
- Static token file
- Bootstrap tokens
- Service account tokens
- OpenID Connect tokens
- Webhook token authentication
- Authenticating proxy

## Identity & Access Management (IAM)

> Who (`serviceaccount`)? What can they do (`action`)? On which `resource`?

### Alternatives to Keycloak

- Google Account
- Service accounts
- Groups
- Cloud IDs

Roles → permissions → service, resource, verb.

# Cert‑Manager

Problem: Too many certificates, varying expiration dates, manual creation leads to security risks and human error.

Solution: Use Let’s Encrypt (free) or alternatives like Vault or Venafi. `certbot` can create a CSR in a pod and request signing from Let’s Encrypt.

Certificate resolvers retrieve certificates from an Automatic Certificate Management Environment (ACME) server. ACME challenges are either HTTP‑01 or DNS‑01.

```yaml
# Install cert-manager (example)

apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: selfsigned-issuer
spec:
  selfSigned: {}

---
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: xxx@gmail.com
    privateKeySecretRef:
      name: letsencrypt-cluster-issuer-key
    solvers:
      - http01:
          ingress:
            class: nginx

---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: test-tls
spec:
  dnsNames:
    - test.com
  secretName: test-tls
  issuerRef:
    name: letsencrypt-prod
```
