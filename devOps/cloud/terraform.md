
# Terraform
> HashiCorp Configuration Language (HCL)  
> Implemented in Go.

```hcl
# comments start with #
terraform {
  required_providers = {
    google = {
      source  = "xxxx"
      version = "zzz"
    }
  }
}
```

```hcl
provider "google" {
  credentials = file("xxx.json")
  project     = "XXX"
  region      = "us-central1"
  zone        = "us-central1-c"
}
```

```hcl
# Example resource declaration
resource "google_compute_instance" "test_ec2" {
  name = ""
}
```

### Terraform Life Cycle
```bash
# 1. Initialise the project
terraform init

# 2. Show the execution plan (similar to `git diff`)
terraform plan

# 3. Apply the desired state (similar to `git commit`)
terraform apply --auto-approve

# 4. Clean up (use with caution – destroys all managed resources)
terraform destroy   # only for testing
```

**Key concepts**
- `terraform refresh` – synchronises state with real infrastructure  
- `terraform plan` – shows the desired state  
- `terraform apply` – enforces the desired state  

## Example Terraform Files
```hcl
terraform {
  required_version = ">= 0.13.0"

  required_providers {
    gcloud = {}
    helm = {
      source  = "hashicorp/helm"
      version = ""
    }
  }
}
```

```hcl
provider "helm" {
  kubernetes {
    host                   = "${yamldecode(xxx_cluster.name.kubeconfig).clusters.0.server}"
    client_certificate     = "${base64decode()}"
    client_key             = ""
    cluster_ca_certificate = ""
  }
}
```

```hcl
resource "kubernetes_namespace" "traefik" {
  metadata {
    name = "traefik"
  }
}
```

```hcl
resource "helm_release" "traefik" {
  depends_on = [
    kubernetes_namespace.traefik
  ]

  name      = "traefik"
  namespace = "traefik"

  repository = "https://xxx"
  chart      = "traefik"

  set {
    name  = "ingressClass.enable"
    value = "traefik"
  }
}
```

```hcl
module "webserver" {
  source = "./modules/webserver"
}
```

```hcl
locals {
  fixed_recordsets = [
    {
      name    = "www"
      type    = "CNAME"
      ttl     = 3600
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
```

```hcl
module "dns_records" {
  # Can be git::xxx?ref=v2.0.0, hashicorp/xxx
  source = "./modules/route53-dns-records"

  route53_zone_id = var.route53_zone_id
  recordsets      = concat(local.fixed_recordsets, local.server_recordsets)
}
```
