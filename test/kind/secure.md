# Secure Service by SSL
> ./example.yaml just setup k8s pods through http; Let's secure network traffic w https & SSL.

## Create namespace
> Why? namespace is a small step to divide Mall into subsections. Again, why?
1. Organization `Too many objects inside same namespace will cause name conflicts`
2. Security `By default all namespace pods are able to talk to others, but later on you can add security to block it. Roles, NetworkPolice, `
3. ResourceQuota by namespace
4. Easy to clean up `Deleted namespace will delete everything under it`

```bash
kubectl create namespace cert-manager
```

> Wait? Why is `cert-manager`? It's k8s addon to manage SSL certs. Remember in analogy share maintains? One of them is cert management!

> https://cert-manager.io/docs/installation/
```bash
helm repo add jetstack https://charts.jetstack.io
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --version v1.8.2 \
  --set installCRDs=true
```

> What just happened? Quite a lot, here is the list
1. Install cert-manager created a lot custom resource definition (CRD) [Issuer, Certificate, ]

```bash
nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
```