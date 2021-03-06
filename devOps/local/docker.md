
# Docker 

Build, push, pull, run image 
```bash
docker build -t docker.xxx/repo_name:terry . 
docker push docker.xxx/repo_name:terry 
sudo docker pull docker.xxx/repo_name:terry
sudo docker pull docker.xxx/repo_name:terry
sudo docker run -d --name container-name -v /var/log/xxx:/app/logs docker.xxx/repo-name:terry python3 start.py app-name --deploy --restart --net=host
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


Docker each container has its namespaces
Control groups proect host resources
SELinux  deal with containers communacation, between containers or to host

## Docker Multi Stage Build
Runtime Stage vs Build Stage

- can create temp image to do unit test, compile code
```
From python AS test
Add . /src
WorkDIR /src

From python As final
COPY --from=test /src /src
```

## Debug
	VS plugin, mount VS code into container (Remote - Containers)
	Python plugin, (debugpy)

```
docker run -it --rm [images-tag] sh

docker-compose build --no-cache
docker-compose -f docker-compose.dev.yml up

docker cp sltc-dashboard:/opt/app/node_modules .

```

# Clean UP
```
docker rm $(docker ps --filter status=exited -q)
docker stats
docker image prune
docker volume prune

dokcer scan image_name
```

# Adv
Mulyi-Stage Build
```
From xxx AS build

build CMDs


FROM xxx
COPY --from=build /app /app

```

Avoid Root User
```
USER node

RUN groupadd -r tom && useradd -g tom tom
RUN chown -r tom:tom /app
USER tom

CMD node index.js

```

# Other
- Codacy Badge `Codacy/repo/Setting/General`
- Github Action Badge `Github/repo/action/xxx_action/.../Create Action Badge`