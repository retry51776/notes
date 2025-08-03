# Docker
>
> Docker each container has its namespaces
>
> Control groups protect host resources
>
> SELinux  deal with containers communication, between containers or to host

## Podman
>
> rootless docker replacement, can mount multiple containers into same pod; docker-compose just spin multiple pods, not containers inside same pod.

```ps
podman run -d --pod my-pod --name mongodb docker.io/library/mongo-express

# generate docker-compose file
podman generate kube my-pod>my-pod.yaml

# aka docker-compose up
podman paly kube my-pod.yaml 
```

## Frustration

- Docker will complicate about port conflict within containers; But if host machine have process took port, docker will silently continue; without warning!
- libseccomp `Docker component` will block container system api calls; default `seccomp profile`
- Docker error `invalid signature was encountered` when disk is full, so misleading!

## Docker Scripts

```bash
# Image Ops: Build, push, pull, list
docker build -t docker.xxx/repo_name:terry . 
docker push docker.xxx/repo_name:terry
docker pull docker.xxx/repo_name:terry
docker ps -a

# Run image
docker run -d --name container-name -v /var/log/xxx:/app/logs docker.xxx/repo-name:terry python3 start.py app-name --deploy --restart --net=host --env-file /xxx.config -e xxx=ggg

# start temp container
docker run -it --rm [images-tag] sh sleep infinity

```

## Debug
>
> VS plugin, mount VS code into container (Remote - Containers)
> Python plugin, (debugpy)

```bash
# Restart
docker-compose build --no-cache --pull
# Extract File from container
docker cp container-name:/opt/app/node_modules .
```

## Maintain

```bash
sudo docker container rm $(docker container ls -aq)
docker system prune
docker image prune
docker volume prune

docker rm $(docker ps --filter status=exited -q)
docker stats

docker scan image_name
```

## Dockerfile

```dockerfile
# aka localhost for docker network
host.docker.internal 
COPY [^n]* # All files that don't start with 'n'
COPY n[^o]* # All files that start with 'n', but not 'no' 
COPY no[^d]* # All files that start with 'no', but not 'nod'
```

> Docker Multi Stage Build `can create temp image to do unit test, compile code`
> Runtime Stage vs Build Stage

-

```dockerfile
From python AS test
Add . /src
WorkDIR /src

From python As final
COPY --from=test /src /src
```

> Avoid Root User

```dockerfile
USER node

RUN groupadd -r tom && useradd -g tom tom
RUN chown -r tom:tom /app
USER tom

CMD node index.js
```

## docker-compose

```yaml
# docker-compose -f docker-compose.dev.yml up
version: '3.9'
services:
    my-app:
        build:
   context: ./dockerfile
   target: runtime
        command: python3 start.py api-service -d
  restart: unless-stopped
        container_name: my-app
        image: python10
        ports:
            - '4000:80'
        volumes:
            - .:/app
  environment:
   xx: xx
  healthcheck:
   test: ["curl" "google.com"]
   interval: 10
   timeout: 10s
   retries: 3
  depends_on:
   xx-db:
    condition: service_healthy
  # only trigger when docker-compose up -d xx-profile
  profiles:
   - xx-profile
   - yyyy
networks:
    default:
        name: local-network
  external: true

```

```yml
--env normal_start=19500000
-v /home/terry/tensorflow/app:/app
depends_on:
 - redis
networks:
 - simple-network
```

# Other

- Codacy Badge `Codacy/repo/Setting/General`
- Github Action Badge `Github/repo/action/xxx_action/.../Create Action Badge`

# Full Virtual OS

- VirtualBox (not support m1)
- VMware Fusion Player (not usable)
- UTM (free, usable)
- Parallel desktop (pay, best)
