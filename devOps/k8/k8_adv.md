# Advanced Kubernetes Topics

> Stuff I consider beyond basic Kubernetes objects. There are many, but this focuses on common CRDs.

---

## Scaling

- Horizontal Pod Autoscaling (HPA) – see the official docs: <https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/>

![Horizontal Pod Autoscaling](./static/k8_auto_scale.jpg)

### Cluster Autoscaling
<https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler>  
Vendor‑specific and can be expensive.

### Horizontal Pod Autoscaling (HPA)
<https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2beta2/#HorizontalPodAutoscalerSpec>

- Cannot scale to zero.
- Metrics may be unreliable.
- KEDA is a better alternative: <https://keda.sh/docs/2.7/deploy/>

#### Prerequisites

1. Verify `metrics-server` is running: `kubectl -n kube-system get pods`.
2. Install it if missing: `kubectl -n kube-system -f ./metricserver.yaml`.
3. Ensure the Deployment defines resource requests and limits.
4. Confirm no existing HPA: `kubectl get hpa`.

```yaml
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
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 40
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

```bash
kubectl autoscale deployment xxx --cpu-percent=40 --min=1 --max=5
```

### Custom Metrics

Use the `custom.metrics.k8s.io` API.

## Admission Webhook / Admission Controller

Two types: **mutating** or **validating**. Both require TLS.

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration   # or ValidatingWebhookConfiguration
metadata:
  name: xxx
webhooks:
  - name: "xxx.example.com"
    objectSelector:
      matchLabels:
        webhook-enabled: "xyz"
    clientConfig:
      service:
        namespace: default
        name: webhook-service
        path: "/validate"
      caBundle: "<BASE64_ENCODED_CA>"
    rules:
      - operations: ["CREATE"]
        apiGroups: [""]
        apiVersions: ["v1"]
        resources: ["pods"]
```

### Pod Disruption Budget

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: nginx-pdb
spec:
  maxUnavailable: 1
  selector:
    matchLabels:
      app: nginx
```

## Custom Resource Definition (CRD)

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: hahas.example.com
spec:
  group: example.com
  versions:
    - name: v1
      served: true
      storage: true
  scope: Namespaced
  names:
    plural: hahas
    singular: haha
    kind: Haha
    shortNames:
      - x
```

## Service Mesh

Enables service‑level authorization.

### Network Policies & Network Agents

Network policies provide basic inbound/outbound traffic control. They are similar to Ingress rules but enforced by a controller (the “network agent”). Popular implementations include Calico.

- Official docs: <https://kubernetes.io/docs/concepts/services-networking/network-policies/>

Why use them when you already have Ingress, LoadBalancers, and Services?

Because sidecar proxies enable:

* Metric collection
* Fine‑grained traffic control (e.g., retries, restrictions)
* Advanced deployment strategies (canary, blue/green)

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-ingress
spec:
  podSelector: {}
  policyTypes:
    - Ingress
  ingress:
    - from:
        - ipBlock:
            cidr: 10.0.0.0/24
```

## Additional Resources

- Share certificates across namespaces: <https://github.com/cert-manager/cert-manager/issues/494>
