# DevOps Metrics
- Deployment Freq
- Lead Time `commited to master to deployment`
- Mean Time Recovery
- Change Failure Rate `hotfix/deployment`
- Cycle time `aka dev time, most mgr care about`

# HashiCorp/ Nomad
Similar to k8, Nomad is a single binary, both for clients and servers.

wrote by Golang, opensource, 3 or 5 server

Agent
Job > Group > Task

# Orchestration

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
.github/workflows/docker-publish.yml

{{ github.event.release.tag_name }}
```
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

paloalto
> monitor network traffic & firewall

# Terraform
Hashicorp Configuration Language(HCL)
written in GO

terraform plan
terraform apply
terraform destroy # Avoid it, it destroy everything
```
# comments
#
#
terraform { 
  required_providers: {
    google = {
      source = "xxxx",
      version = "zzz",
    }
  }
}

provider "google" {
  credentials = file("xxx.json")
  project = "XXX"
  region = "us-central1"
  zone = "us-central1-c"
}

resource [resource_type] [name]
resource "google_compute_instance" "test_ec2" {
  name = ""
}
```

### Jenkinsfile.develop
```

```
Config Management DB(CMDB) a file list csp servers
Jenkin Cronjob tigger Ansiable playbook call APIs
ServiceNow
Rapid7
System Center Configuration Manager
RedHat Satellite
CrowdStrike
Prisma
Infoblox
Zabbix
