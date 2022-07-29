# Deployment
> We includes Deployment, Daemonset, Pods, CronJobs, Jobs here

> List most common used attributes, I never able to remember them.

## containers
> Uses everywhere, smallest k8s unit
- args
- volumeMounts `where mount to`
- livenessProbe / readinessProbe / startupProbe
- ports
- resources
- image
- imagePullPolicy
- securityContext

## template
> uses in [Deployment, Daemonset, CronJobs, Jobs]
- metadata: `allow [Deployment, Daemonset, CronJobs, Jobs] add different label to its pods`
- spec: `Deployment.spec.template.spec = pod.spec`
  - volumes `list of volumes POD have access to`
  - [containers](#containers)
  - initContainers: `to do xxx before main application containers start`
  - serviceAccountName
  - securityContext
  - nodeSelector
  - affinity
  - tolerations

# Deployment
- spec: `Deployment's spec`
  - replicas `deployment replicas`
  - strategy `deployment strategy`
  - [template](#template)
# Daemonset
> enforce single pod per node on all nodes (for monitor logs, storage, network) 
- [template](#template)
```yml
nodeSelector:
  name: xxx_node_name
tolerations:
- key: node.kubernetes.io/unschedulable
  operator: Exists
  effect: NoSchedule   # No new pod until daemonset ready
```

# Pods
- Quality of Service ['Guaranteed', 'Burstable', 'BestEffort']
- PriorityClass 
- naked Pods `Kind: POD deployment`
- Static Pods `PODs part of k8s system, /etc/kubernetes/manifests/`
- initContainers: `spec.initContainers: to do xxx before main application containers start`
- [containers](#containers)
# CronJobs
- startingDeadlineSeconds `to set the deadline to start a Job if scheduled time was missed;`
- concurrencyPolicy `to allow or forbid concurrent Jobs or to replace old Jobs with new ones. `
- [template](#template)
# Jobs
- parallelism `to set the number of pods allowed to run in parallel;`
- completions `to set the number of expected completions;`
- activeDeadlineSeconds `to set the duration of the Job;`
- backoffLimit `to set the number of retries before Job is marked as failed;`
- ttlSecondsAfterFinished `to delay the clean up of the finished Jobs.`
- [template](#template)