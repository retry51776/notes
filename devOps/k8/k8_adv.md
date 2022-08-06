# K8 Adv
> Stuff I consider beyond basic k8s objects. There are way too many, but we restrict to common CRD.
<hr />

# Scaling
> https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/

![](/static/k8_auto_scale.jpg)



## Cluster Autoscaling
> https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler
> Vendor specific, can be very expensive.


## Horizontal Pod Autoscaling (HPA)
> https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2beta2/#HorizontalPodAutoscalerSpec

> can't scale to 0, bad metrics

> keda is better alternative: https://keda.sh/docs/2.7/deploy/

### Preq
1. check metrics_server `kubectl -n kube-system get pods`
2. if not already install, install it `kubectl -n kube-system -f .\metricserver.yaml`
3. check node allocated resources
4. make sure deployment set resources: requests [always set limited too]
5. check not already hpa `kubectl get hpa`

```yml
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
    name: xxx
spec:
    scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: xxx
    minReplicas: 1
    maxReplicas: 5
    metrics:
    - type: [Resource, External, Pod]
        resource:
            name: [cpu, memory, packets-per-second]
            target:
                type: [AverageValue, Utilization]
                AverageValue: [100Mi, 40]
    behavior:
      scaleDown:
        stabilizationWindowSeconds: 300
        policies:
        - type: Percent
          value: 100
          periodSeconds: 15
      scaleUp:
        stabilizationWindowSeconds: 0
        policies:
        - type: Percent
          value: 100
          periodSeconds: 15
        - type: Pods
          value: 4
          periodSeconds: 15
        selectPolicy: Max
```

`kubectl autoscal deployment xxx --cpu-percent=40 --min=1 --max=5`

## Custom Metrics
1. `custom.metrics.k8s.io`

## Admission Webhook / Admission Controller
> 2 types: intercepts or validate
> Required tls

```yml
kind: MetatingWebhookConfiguration
webhooks:
  - name: "xxx"
  # What k8_objects can trigger
  objectSelector:
    matchLabels:
      webhook-enabled: "xyz"
  clientConfig:
    service:
      name: xxx
      path: '/xxx'
    caBundle: "{CA_PEM_B64}"
  # What event trigger
  rules:
  - operations: [ "CREATE" ]
    apiGroups: [""]
    apiVersions: ["v1"]
    resources: ["pods"]
```

> keep at least some pod running
```yml
apiVersion: policy/v1beta1
kind: PodDisruptionBudget
metadata:
  name: nginx-pdb
spec:
  maxUnavailable: 1
  selector:
    matchLabels:
      app: nginx
```

## CRD
```yml
apiversion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
spec:
  versions:
    - name: v1
      served: true
  scope: namespaced
  names:
    plural: xxxs
    singluar: xxx
    kind: haha
    shortNames:
    - x
```


## ServiceMesh, Network Police & Network Agent
> Network Police is basic In/Out traffic control. Similar to Ingress Rule to Ingress Controller, there is a controller to implement polices, network agent is not install by default. Popular is calico
> Read more [AddOn.md](./addon.md)

> https://kubernetes.io/docs/concepts/services-networking/network-policies/

> Why? Aren't we have Ingress, LB, Service already?
> 
> Because network go through sidecar enables:
>> Metric Monitor Solutions
>> Network Police for finnier/secure traffic control. (Ex: Retry, Restrict)
>> Fancy Deployment (Ex: Canary, BlueGreen)
```yml
# NetworkPolicy.spec.policyTypes.ingress.from [ipBlock, namespaceSelector, podSelectore]
kind: NetworkPolicy
spec:
  podSelectore:
    matchLabels:
  policeTypes:
  - Ingress
  ingress:
  -from:
  - Egress
```

## Other good posts:
- Share cert across namespaces https://github.com/cert-manager/cert-manager/issues/494
- 