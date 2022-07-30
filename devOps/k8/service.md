# Service
> We are talking about k8s Service & its sub components

> Production clusters should enable Kubelet authentication and authorization.

> Service.targetPort = Pod.spec.containerPort

> default url `my-svc.my-namespace.svc.cluster.local`

> Services, complex encapsulations of network routing rule definitions stored in iptables on cluster nodes and implemented by kube-proxy agents.

> https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/
## External LoadBalancer
> https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/

After you enable GKE Loadbalancer API, add this to ingress
`Ingress.metadata.annotations.kubernetes.io/ingress.class: "gce"`


# PODs
> endpoints is auto created by k8, Ex:(10.1.1.1:5000, 10.1.1.2:5000)