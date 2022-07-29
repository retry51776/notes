# Service
> We are talking about k8s Service & its sub components

> Production clusters should enable Kubelet authentication and authorization.


## External LoadBalancer
> https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/

After you enable GKE Loadbalancer API, add this to ingress
`Ingress.metadata.annotations.kubernetes.io/ingress.class: "gce"`