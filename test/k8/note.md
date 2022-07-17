# Stepup Traefik
> https://doc.traefik.io/traefik/getting-started/install-traefik/#use-the-helm-chart

> https://www.devtech101.com/2019/03/02/using-traefik-as-your-ingress-controller-combined-with-metallb-on-your-bare-metal-kubernetes-cluster-part-2/
> 
1. `helm repo add traefik https://helm.tra
efik.io/traefik`
1. `helm install traefik traefik/traefik --set dashboard.enabled=true,serviceType=LoadBalancer,rbac.enabled=true,dashboard.domain=traefik.local`
NAME: traefik`
3. `kubectl port-forward $(kubectl get pods --selector "app.kubernetes.io/name=traefik" --output=name) 9000:9000`
4. > http://127.0.0.1:9000/dashboard/
