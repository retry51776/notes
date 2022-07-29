# K8s Security
> TLS/SSL certs, Service mesh
## Addons
> cert-manager 
>> `simplifies the process of obtaining, renewing and using those certificates`
>> 1. Create CA cert & key
>> 2. Create clusterissuer
>> 3. Create Certificate
>> 4. Create Secret
>> 5. Set Ingress
```yml
kind: Secret
data:
  tls.crt: $(cat xxx.pem | base64 | tr -d '\n')
  tls.key: $(cat xxx-key.pem | base64 | tr -d '\n')
```
> keycloak `client application authorization`

> Kubernetes Dashboard
## Secrets
|  Built-in Type	  |  Usage |
|---|---|
| Opaque |   arbitrary user-defined data |
| kubernetes.io/service-account-token| ServiceAccount token |
| kubernetes.io/dockercfg | serialized ~/.dockercfg file |
| kubernetes.io/dockerconfigjson | serialized ~/.docker/config.json file |
| kubernetes.io/basic-auth | credentials for basic authentication |
| kubernetes.io/ssh-auth | credentials for SSH authentication |
| kubernetes.io/tls | data for a TLS client or server|
| bootstrap.kubernetes.io/token | bootstrap token data |

## Auth
> Normal Users manage by independent services like User/Client Certificates
> Service Accounts communicate with the API server to perform various operations.


> The user/client now connects to a Service via its ClusterIP, which forwards traffic to one of the Pods attached to it. A Service provides load balancing by default while selecting the Pods for traffic forwarding.

> 1. by certificates
>> CA certificates store at Control Plane node default path `/etc/kubernetes/pki`

```bash
# Step 1. Create client key & sign by CA
openssl req -new -key xxx.key -out xxx.csr "/CN=fname lname/O=HR"
openssl x509 -req -in xxx.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out xxx.crt -day 500

# Alternativy: use kubectl sign
kubectl certificate approve xxx.csr
kubectl get csr/xxx -o yaml
kubectl get csr xxx -o jsonpath='{.status.certificate}'| base64 -d > xxx.crt


# Step 2. Add ~/.kube/config
kubectl config set-cluster xxx-cluster --server=https://1.1.1.1:52807 --certificate-authority=ca.crt --embed-certs=true
kubectl config set-credentials xxx --client-certificate=xxx.crt --client-key=xxx.key --embed-certs=true
kubectl config ser-context dev --cluster=dev --namespace=default --user=xxx
kubectl config use-context dev

# Step 3. Create Role & BindRole
---
check how to create k8 role yaml file
kind: Role
---
kind: RoleBinding
subjects:
- kind: User
  name: "fname lname"
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: xxx_Role
  apiGroup: rbac.authorization.k8s.io
---
kubectl apply -f xxx_role.yml


```
> 2. by OAUTH
>> K8 will send group_id and OAUTH token;
>> Example: ServiceAccount Bearer Token default `/var/run/secrets/kubernetes.io/serviceaccount`
>> 
```bash
kubectl get secret default-token-2mfqv --namespace={namespace} -o yaml


# New since 1.24
kubectl create token SERVICE_ACCOUNT_NAME
# Old 
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
### authentication modules:
- X509 Client Certificates standard
- Static Token File
- Bootstrap Tokens
- Service Account Tokens
- OpenID Connect Tokens
- Webhook Token Authentication
- Authenticating Proxy

### Identity Access Management (IAM)
> Who`service account`? Do what `action`? On What `resource`?
Identity
>
> Opensource alt keycloak
> 
- Google Account
- Service Account
- Group
- Cloud ID

Police -> roles -> permission [service. resource. verb]

# Cert-Manager
> Problem to Solve: Too many cert, expired different time, manual create cert creates security risk, human errors

> Let's Encrypt https://letsencrypt.org/ `allows create free cert, alt: vault-prod, venafi-tpp`

> certbot `k8s pod create csr & ask let's encrypt to sign`

Certificate Resolvers `retrieving certificates from an Automatic Certificate Management Environment (ACME) server.`
ACME challenge will either http or dns
kubernetes.io/ingress.class: "nginx"
nginx.ingress.kubernetes.io/force-ssl-redirect: "true" 
```yml
# Install cert-manager

# Setup let's encrypt through issuer.yaml
apiVersion: cert-manager.io/v1
kind: Issuer
spec:
  selfSigned: {}
  # can be selfSigned, CA, Vault, ExternalLoadBalancer, Venafi, External, ACME
---
spec:
  acme:
    server: https://acme-xxx.letsencrypt.org/directory
    email: xxx@gmail.com
    privateKeySecretRef:
      name: letsencrypt-cluster-issuer-key
    solvers:
    - http01:
      ingress:
        class: nginx
---
kind: Certificate
spec:
  dnsName:
    - test.com
    secretName: test-tls
    issuerRef:
      name: selfsign
```

