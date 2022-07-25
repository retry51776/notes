# DevOps
> Common reference terms in devOps that I understand.


# DevOps Metrics
- Deployment Freq
- Lead Time `commited to master to deployment`
- Mean Time Recovery
- Change Failure Rate `hotfix/deployment`
- Cycle time `aka dev time, most mgr care about`

## Four Fundamental Topologies
- Stream-aligned team: `Aligned to a flow of work from (usually) a segment of the business domain.`
- Enabling team: `Helps a stream-aligned team to overcome obstacles. Also detects missing capabilities.`
- Complicated subsystem team: `Where significant mathematics/calculation or hardto-find niche technical expertise is needed full-time.`
- Platform team: `A grouping of other team types that provide a compelling internal product to accelerate delivery by stream-aligned teams.`

## CheckList
- install
- config
- provision
- deploy

- security
- monitor
- backup & restore

- network
- HA
- scalibity
- performance

- cost
- documentation
- test


---
## Deployment strategy
- Blue Green
  > swape all at once 
- Rolling update
  >  Different Version at same time
- Recreate
  > Offline gap
- Canary
  > some user, slowly move over
- A/B
  > target subject get updates 
- Shadow


---
**Github Action**
> These should moved to /test or /example folder
.github/workflows/docker-publish.yml

{{ github.event.release.tag_name }}
```yml
- id: get_branch
shell: bash
run: echo "##[set-output name=branch;]$(echo ${GITHUB_REF#refs/heads/})"
---
- name: Build and push
uses: docker/build-push-action@v2.7.0
with:
  context: .
  build-args: |
    ENV=prod
  platforms: linux/amd64
  tags: |
    terry.test.local/hello:${{ steps.get_branch.outputs.branch }}${{ github.run_number }}
---
clean-working-directory:
  runs-on: []
  needs: build
  steps:
    -name: Clean
      shell: bash
      run: |
        cd $RUNNER_WORKSPACE
        cd ..
        rm -r *


---
generate_docu:
  image: node
  stage: deploy
  script:
  - npm install -g redoc-cli
  - redoc-cli bundle -o /public/doc.html xxx_swagger.yml
  artifacts:
    paths:
    -public
  only:
  - master
```



### Jenkinsfile.develop
```

```
