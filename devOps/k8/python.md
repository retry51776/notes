# Python Kubernetes Client Example

```python
from kubernetes import client, config

config.load_incluster_config()
v1 = client.CoreV1Api()
ret = v1.list_pod_for_all_namespaces(watch=False)
for pod in ret.items:
    print(pod.status.pod_ip)
```
