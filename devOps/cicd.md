# CI & CD
> Examples of stuff in CI/CD. There are many tools in this space.

> Funny thing about CI/CD is that it automates processes and testing code to be more reliable, yet the CI/CD pipeline itself is often the most unreliable component.

## [Bash](/devOps/local/bash.md)
> Works with Linux.

## [Go](/development/go.md)
> Many DevOps tools are written in Go.

## [Python](/development/python/python.md)
> The duct‑tape of DevOps.

## [Terraform](/cloud/terraform.md)
> Industry‑standard tool; probably the most widely used in the DevOps toolbox.

## Ansible
> Old, but similar in purpose to Terraform.

## GitHub Actions
> Default path: `/.github/workflows/docker-publish.yml`

```yaml
# TODO: Move these examples to /test or /example folder
{{ github.event.release.tag_name }}
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
    - name: Clean
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
      - public
  only:
    - master
```

## Bitbucket Pipelines
- Define conditions & order of steps  
  - Step (aka `docker-compose.yml`)  
    - Services (containers)  
    - Memory allocation per service  
    - Script (commands)  
    - Artifacts (volumes)  

- Definitions – reusable templates

### Jenkinsfile.develop
```bash
# TODO: Add example content from the web
```
