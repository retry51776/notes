# Security

### Linux
1. gen ssh key `ssh-keygen -b 4096`
2. create user in remote linux server
3. copy public key into /home/user_name/.ssh


### Windows
ssh-rsa is Developer Public Keys
1. PuTTYgen -> .ppk -> .ssh
2. Publish SSH to Admin
3. Add ssh key to github


### Setup VPN
Microsoft Management Console `Run > mmc > Enter` export LDAP certificate for VPN

## File Types
```

*.ppk = encrypted private key by puttyGen
.cer <--> .crt(Microsoft) -> .pfx

.PFX is Personal Exchange Format, windows user certificate
.cer - certificate with public and private keys.
.cer & .key is OpenSSL generated files for OpenVPN, Pageant

*.crt = Windows certificate  for SSL
*.pem = subset of *.crt, just rename extension to *.crt
//pem can be private key or public key
*.key = private key
*.pub = public key
```

## Tech Terms
- Certificate Authority(CA)
  - who issued
  - who issued to
  - valid to
  - public key
  - digital signature
  

**Create TLS**
1. Create .csr with openssl

```
openssl req -new -sha256 -out terry.test.local.csr -newkey rsa:2048 -keyout "$1.key" -nodes -reqexts SAN - config <cat /some_ssl.cnf <(printf("[SAN]\nsubjectAltName=DNS:terry.test.local"))>> -out terry.test.local.csr
```

2. Request AD to signed .csr, created .crt
  a) https://gcp-dns-1.test.local (usually MS AD)
  b) download Base-64

3. Install crt
  a) Install in K8
    1. kubectl create secret tls terry-tls --cert=terry.test.local.cer --key=terry.test.local.key
    2. In Ingress file add tls property
  b) Install in server
    1. ssh into server
    2. copy .crt and key to /etc/test/conf/nginx/data/ssl