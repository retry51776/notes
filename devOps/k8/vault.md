# Vault
> default 5 unseal_keys & 1 root_token, 3 out 5 can unencrypts; default port 8200;

> https://www.sobyte.net/post/2022-01/expirence-of-vault/
## Mode
- HA
- Stand Along
- Dev sever
## Storage
- Seal
- Unseal

## Vault Core
1. Authentication
2. Get Policies
3. Access Token Store
    - lease id
    - expired time

## Secret Engine
- Auth Secrets `Proven Who, can revoke`
- Access Secrets `secret value, if auto generate by vault, can auto rotate & expire`
## Client
> Admins defines polices & token holders
## Server
- /Secrets
- /Access
- /Policies
- /Tools
## Config
1. exec into vault pod
2. get key by `vault operator init`
3. unseal by `vault operator unseal`
```yml
# config.hcl; maybe mount cert-manager crt as volumevau
ui = true

storage "file" {
  path    = "/vault/file"
}

listener "tcp" {
  address = "[::]:8200"

  tls_disable = false
  tls_cert_file = "/certs/server.crt"
  tls_key_file  = "/certs/server.key"
}
```

## vault agent, sdk
- vault agent `sidecar pod inject secrets as /vault/secrets/config.json`
  - export xxx_
- SDK
## Buzzwords
- Shamir's Secret Sharing
- access-control list (ACL) 