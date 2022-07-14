
# GCP
GKE

Google Cloud’s containers as a service (CaaS)

StackDriver

Cloud Storage

Cloud Functions

## Setup
```
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