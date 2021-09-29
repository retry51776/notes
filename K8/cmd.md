# kubernetes
**CMDs**

```
gcloud init  
gcloud config set project XXX  
gcloud components update
gcloud components install docker-credential-gcr  
gcloud auth configure-docker

```
**Setup Google in remote server**
```
source ~/.bashrc  
gcloud auth login  
gcloud config set project XXX
gcloud auth configure-docker  
docker pull [gcr.io/XXX/YOUR_PROJECT_NAME:develop](http://gcr.io/XXX/YOUR_PROJECT_NAME:develop)  

gcloud docker -- ls
gcloud container clusters get-credentials XXX-cluster --zone us-central1-a
```

```
  
kubectl get services XXXXX  
image level  
kubectl get deployment  
container level  
kubectl get pods  
kubectl run XXXX --images=XXXX --port=80  
  
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

  
application layer encryption  
  
components:  
1. ingress  
2. service  
3. cronjobs  
4. deployment/StatefulSet  
5. etcd  
6. ConfigMap  
7. Secrets