# Deployment (Area Inside the Mall)

> Includes Deployments, DaemonSets, Pods, CronJobs, and Jobs.

> Lists the most commonly used attributes that are easy to forget.

## Containers / InitContainers (Workers in the Store)

Used everywhere; they are the smallest Kubernetes unit.

- `args`
- `volumeMounts` – where to mount volumes
- `livenessProbe`, `readinessProbe`, `startupProbe`
- `ports` – list of application ports exposed to a Service
- `resources`
- `image`
- `imagePullPolicy`
- `securityContext`

## Template (Worker’s Access)

Used in Deployments, DaemonSets, CronJobs, and Jobs.

- **metadata** – allows different labels for the Pods created by a Deployment, DaemonSet, etc.
- **spec** – `Deployment.spec.template.spec` equals `Pod.spec`
  - `volumes` – list of volumes available to the Pod
  - `containers` – see above
  - `initContainers` – run before the main application containers start
  - `serviceAccountName`
  - `securityContext`
  - `nodeSelector`
  - `affinity`
  - `tolerations`

## Deployment (Chain Stores)

- **spec** – the Deployment’s spec
  - `replicas` – number of pod replicas
  - `strategy` – deployment strategy
  - `template` – see above

## DaemonSet (Building’s Bathroom, Security Office)

Enforces a single Pod per node on all nodes (useful for log collection, storage, networking).

```yaml
nodeSelector:
  name: xxx_node_name
tolerations:
  - key: node.kubernetes.io/unschedulable
    operator: Exists
    effect: NoSchedule   # Prevents new Pods until the DaemonSet is ready
```

## Pods (Store)

- Quality of Service classes: `Guaranteed`, `Burstable`, `BestEffort`
- PriorityClass
- **Naked Pods** – plain Pod objects (`kind: Pod`)
- **Static Pods** – part of the Kubernetes system, defined in `/etc/kubernetes/manifests/`
- `initContainers` – run before main containers start
- See also [containers](#containers)

## CronJobs (Scheduled Tasks)

- `startingDeadlineSeconds` – deadline for starting a Job if the scheduled time was missed
- `concurrencyPolicy` – allow, forbid, or replace concurrent Jobs

## Jobs (One‑Time Tasks)

- `parallelism` – number of Pods allowed to run in parallel
- `completions` – expected number of successful completions
- `activeDeadlineSeconds` – maximum duration for the Job
- `backoffLimit` – retries before marking the Job as failed
- `ttlSecondsAfterFinished` – delay cleanup after completion

All of the above use the same **template** structure.
