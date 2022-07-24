# Terrform vs Ansible

resource
Hash(HCL)
### Terrform Life Cycle:
```bash
# 1. Init Project
terraform init
# 2. Similar to git diff
terraform plan
# 3. Similar to git commit
terraform apply --auto-approve



```
##
```tf
terraform {
    required_version = ">= 0.13.0"

    required_providers {
        gcloud = {}
        helm = {
            source = "hashicorp/helm"
            version = ""
        }
    }
}

provider "helm" {
    kubernetes {
        host = "${yamldecode(xxx_cluster.name.kubeconfig).clusters.0.server}"
        client_certificate ="${base64decode()}"
        client_key =
        cluster_ca_certificate = 
    }
}
```

```
resource "kubernetes_namespace" "traefik" {
    metadata {
        name = "traefik"
    }
}

resource "helm_release" "traefik" {
    depends_on [
        kubernetes_namespace.traefik
    ]

    name = "traefik"
    namespace = "traefik"

    repository = "https://xxx"
    chart = "traefik"

    set {
        name = "ingressClass.enable"
        value = "traefik"
    }
}
```
TF config
TF refresh (kublet)
TF Plan (desire state)
TF Apply
