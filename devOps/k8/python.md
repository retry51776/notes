# python
```python
from kuberneres import client, config

config.load_incluster_config()
v1 = client.CoreV1Api()
ret = v1.list_pod_for_all_namespaces(watch=False)
for x in ret.items:
    print(x.status.pod_ip)
```