
# GCP
GKE

Google Cloud’s containers as a service (CaaS)

StackDriver

Cloud Storage

Cloud Functions

## Setup
```bash
gcloud init
gcloud components update
gcloud components list
gcloud components install XXXX
gcloud components install kubectl
gcloud components install docker-credential-gcr

source ~/.bashrc
gcloud auth login
gcloud config set project XXX
gcloud auth configure-docker // Warning doesn't matter

// Test by pulling gcp image & container
gcloud docker -- ls

// Create K8 context @ ~/.kube/config, I never manually create context
gcloud container clusters get-credentials XXX-cluster --zone us-central1-a

ps auxww // Show all process

// cmd prefix project
// edit ~/Documents/PowerShell/profile.ps1
function Prompt {
    $k8context = kubectl config current-context
    Write-Host("`r`n[$PWD]($k8context)")
    return "> ";
}
```
## DB Auth
> [Configure public IP](https://cloud.google.com/sql/docs/mysql/configure-ip)
> [Configure SSL](https://cloud.google.com/sql/docs/mysql/configure-ssl-instance)
### Cloud SQL Auth proxy
> allows sidecar container for deployment to access DB without SSL
`cloud_sql_proxy -instances=proj_id:zone:db_instance_id=tcp:3306 -credential_file=/secrets_path.json` 

## Daemonset
- fluentbit
- metrics-agent
- traefik-ingress-controller
- pdcsi `google presistent disk`