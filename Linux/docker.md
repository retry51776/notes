
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

## Dockerfile
```
COPY [^n]* # All files that don't start with 'n'
COPY n[^o]* # All files that start with 'n', but not 'no' 
COPY no[^d]* # All files that start with 'no', but not 'nod'
```