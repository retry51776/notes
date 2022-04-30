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
## Setup Domain Controller
1. Create VM
   a. rename PC name to (DomainController or something)
   b. config network adpator properties, disable IPv6, IPv4 with static IP
2. Server Manager -> Add roles & features -> check
   a. Active Directory Domain Service
3. Promote this service to a donmain controller
4. Add role DNS Service (conver url to ip)
5. Add role DHCP (manage IP adress assignment)


## Add PC to Domain
1. Control Panel / System and Security / System / change setting
2. rename PC name & domain
3. change DNS service to DC ip


**Github Action**
.github/workflows/docker-publish.yml

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
```