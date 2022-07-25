
# Terraform
> Hashicorp Configuration Language(HCL)
> written in GO

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

### Terrform Life Cycle:
```bash
# 1. Init Project
terraform init
# 2. Similar to git diff
terraform plan
# 3. Similar to git commit
terraform apply --auto-approve
# 4. Clean up
terraform destroy # Avoid it, only used in testing, it destroy everything

TF config
TF refresh (kublet)
TF Plan (desire state)
TF Apply

```
## Example TF files
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

module "webserver" {
  source = "./modules/webserver"
}

locals {
  fixed_recordsets = [
    {
      name = "www"
      type = "CNAME"
      ttl  = 3600
      records = [
        "webserver01",
        "webserver02",
        "webserver03",
      ]
    },
  ]
  server_recordsets = [
    for i, addr in module.webserver.public_ip_addrs : {
      name    = format("webserver%02d", i)
      type    = "A"
      records = [addr]
    }
  ]
}

module "dns_records" {
  # Can be git::xxx?ref=v2.0.0, hashicrop/xxx
  source = "./modules/route53-dns-records"

  route53_zone_id = var.route53_zone_id
  recordsets      = concat(local.fixed_recordsets, local.server_recordsets)
}

```
