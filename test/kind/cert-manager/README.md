# Secure Service by SSL
> [example.yaml](../example.yaml) just setup k8s pods through http; Let's secure network traffic w https & SSL.

## Create namespace
> Why? namespace is a small step to divide Mall into subsections. Again, why?
1. Organization `Too many objects inside same namespace will cause name conflicts`
2. Security `By default all namespace pods are able to talk to others, but later on you can add security to block it. Roles, NetworkPolice, `
3. ResourceQuota by namespace
4. Easy to clean up `Deleted namespace will delete everything under it`

```bash
kubectl create namespace cert-manager
```

> Wait? Why is `cert-manager`? It's k8s addon to manage SSL certs. Remember in analogy share maintains? One of them is cert management! cert-manager can auto renew SSL/TLS for all ingress. Network admin will love it!

> https://cert-manager.io/docs/installation/
```bash
helm repo add jetstack https://charts.jetstack.io
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --version v1.8.2 \
  --set installCRDs=true

# Create Another Ingress with https support
kubectl apply -f setup.yaml

# Now you should able to https://k8.local
```

> What just happened? Quite a lot, here is the list
1. Install cert-manager created a lot custom resource definition (CRD) [Issuer, Certificate]
2. Created cert-manager Roles, ServiceAccount, Binding, Deployment, Service
3. We tell cert-manager create SSL cert
4. We create another secure-ingress(host: k8.local) uses SSL generated from step 3