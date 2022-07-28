# CI & CD
> Example of stuff in CI/CD. A lots tools in this space.

> Funny thing about CI & CD is automate process, testing code to be more reliable. Yet CI & CD itself is the MOST UNRELIABLE thing ever.
## [Bash](/devOps/local/bash.md)
> Works w linux.
## [GO](/development/go.md)
> A lots devOps tools written in GO.
## [Python](/development/python/python.md)
> Duct tape of devOps
## [Terraform](./cloud/terraform.md)
> It's industry standard tool. Most likely the biggest coverage devOps toolbox.
## Ansible
> Old, but similar tools to Terraform

## Github Action
> default path `/.github/workflows/docker-publish.yml`

```yml
# TODO: These should moved to /test or /example folder
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
```bash
# TODO: needs to find some examples from Web
```