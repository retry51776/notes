# Docker

```
docker run -it --rm [images-tag] sh

docker-compose build --no-cache

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
