# kubernetes
**Setup gcloud**

```
gcloud init
gcloud auth login
gcloud config set project XXX
gcloud components update
gcloud components install docker-credential-gcr  
gcloud auth configure-docker

// Test by pulling gcp image & container
gcloud docker -- ls
docker pull [gcr.io/XXX/YOUR_PROJECT_NAME:develop](http://gcr.io/XXX/YOUR_PROJECT_NAME:develop)

source ~/.bashrc 

```
**Setup gcloud kubectl**
```
gcloud container clusters get-credentials XXX-cluster --zone us-central1-a
```

`kubectl [create|edit|get|delete]`
- job
- cronjob
- deployment
- pods
- service
- ingress
- event
- secrets


all k8 resources types: https://kubernetes.io/docs/reference/kubectl/overview/#resource-types
https://crontab.guru/

Commons K8 CMD
```

kubectl create job --from=cronjob/mycronjob name-of-one-off-job
kubectl run XXXX --images=XXXX --port=80  
kubectl exec -it pod-name sh
  
kubectl expose deployment XXXX --type="LoadBalancer" service "XXXX" exposed  
  
ps auxww // Show all process
```
# Docker 

Build, push, pull, run image 
```
docker build -t docker.xxx/repo_name:terry . 
docker push docker.xxx/repo_name:terry 
sudo docker pull docker.xxx/repo_name:terry
sudo docker pull docker.xxx/repo_name:terry
sudo docker run -d --name container-name -v /var/log/xxx:/app/logs docker.xxx/repo-name:terry python3 start.py app-name --deploy --restart
```

start temp container
`docker run -it --rm [images-tag] sh`
`sudo docker start container-name sh sleep infinity`

`docker-compose build --no-cache --pull`
`docker ps -a`
`docker cp container-name:/opt/app/node_modules .`

**Clean Docker**
```
sudo docker container rm $(docker container ls -aq)
docker system prune
docker image prune
docker volume prune
```

**docker-compose.yml**
```
--env normal_start=19500000
-v /home/terry/tensorflow/app:/app
depends_on:
	- redis
networks:
	- simple-network
```

**linux**
`htop` //Similar to task manager in Windows 
`free -h` //Memory
`chmod -R 660 /app`
```
COPY [^n]* # All files that don't start with 'n'
COPY n[^o]* # All files that start with 'n', but not 'no' 
COPY no[^d]* # All files that start with 'no', but not 'nod'
```


# Tech terms
containerD and cri-o are container runtime
open container initiative


ingress is K8 build in route control traefik similar to ingress, but more features nginx

  
application layer encryption  for secrets

  
components:
- Mater Node
  - Scheduler
    - Trigger Cron Jobs
  - Control Mgr
    - Compare Active State vs Desired State
  - etcd
    - key/value DB
  - API service
    - Supports cmds
- Worker Node
  - Container Run Time
    - Pods //smallest k8 unit
  - Kubproxy
    - route & selector
  - Kubelet
    - communicate with API-service


**Deployment File**

https://kubernetes.io/docs/concepts/overview/working-with-objects/

```
apiVersion: v1 # Required
kind: [Service|other k8 resources] # Required
metadata: # Required: uniquely identify the object
	name: # Required: k8 object id
	labels: # Optional
		app: # Important: must match to selector
		type:
spec: # Required: desire state

# layer 7 tcp load balancer
# redirect traffic to different services
# redirect different ip to matching service (nodePort doesn't matter anymore)
Ingress spec:
  rules:
  - host: stage.local
    http:
      paths:
      - path: /
        backend:
          serviceName: stage
          servicePort: web
  - host: terry.internal-service.local
    http:
      paths:
      - path: /app1
        backend:
          serviceName: terry-app1
          servicePort: web
      - path: /app2
        backend:
          serviceName: terry-app2
          servicePort: web
  tls:
  - secretName: terry.internal-service.local

Service spec:
	type: [NodePort|ClusterIP|LoadBalancer] # usually ClusterIP
	ports:
	# ClusterIP
		- port: 80
		- targetPort: 80
		- protocol: TCP
	# NodePort
		- targetPort: 80
		- port: 80
		- nodePort: [30000-32767]
	selector:
		app: # Important: Match from metadata.labels
		type: # Important: Match from metadata.labels

# Test by `curl https://node_ip:nodePort/`
```
