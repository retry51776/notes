# Security
> Network admin security stuff. Most about Cert

> $300 to $2000 to get root_ca signed

> root_ca_authority signed internal db & micro-service certs 

> public_ca_authority signed root_ca_authority

> cert is configured in loadbalancer, ingress, or however db loads cert

> wildcard cert `allows easy to manage & single cert for internal reverse proxy`
> single cert `hard to manage, but more secure`

## Basic Terms
- X.509 certificate `is a digital certificate, contains both pub & pri keys`
  - Transport Layer Security (TLS) `Newer than SSL`
  - Secure Sockets Layer (SSL) `Similar as TLS`
- Certificate Authority(CA)
  - who issued
  - who issued to
  - valid to
  - public key
  - digital signature
- Decision Strategy `Authorization`

## Add Certificate
  ## Windows
   1. Microsoft Management Console `Run > mmc > Enter` 
   2. Add or Remove Snap-ins/Certificate/next/Console Root/Certificates/Third-Party Root/All Task/Import

  ## MacOS
    1. Keychain Access/System/add/Always Trust
  
  ## Linux
    ## Create Cert
    1. genkey www.xxxx.local
    2. going to take a while generate randomness
    3. Input Meta: (Country, State, Locality, Organization, Unit, domain_name)
    4. Generated xxx.crt & xxx.key

    ## Request CA to Sign Cert
    1. Generated xxx.csr from xxx.key
    2. go to CA `ca.xxxx/certsrv`/Request a certificate/advanced certificate request, copy xxx.csr text & past to form.
    3. download Base 64 encoded version xxx.cer

    ## Install crt into Service
    1. ssh into xxx server, copy crt
    2. `vi /etc/httpd/conf.d/ssl.conf` to edit `SSLCertificateKeyFile` & `SSLCertificateFile`
    3. `service httpd restart`

    ## Client Trust CA
    1. go to CA `ca.xxxx/certsrv`/Install CA Certificate & Download & Install CA Certificate
    2. Add DNS A record OR edit `/etc/hosts`

## SSL/TLS cert Files
> .cer & .key is OpenSSL generated files for OpenVPN, Pageant
- *.key `private key`
- *.pub `public key`
- *.cer `certificate only with public keys`
- *.csr `certificate Signed Request`
- *.crt `signed Certificate`
- *.ppk `encrypted private key by puttyGen`
  
> Windows
- *.cer <--> .crt(Microsoft) -> .pfx `file conversion`
- *.PFX `is Personal Exchange Format, windows user certificate(with private key)`
- *.pem `can be private key or public key; subset of *.crt, just rename extension to *.crt`
- *.der `(Distinguished Encoding Rules) binary format`
- *.p12 `(Public Key Cryptography Standard) can have private key, password lock` <--> *.PFX
- *.p7b `public key only, for Tomcat`

**Create SSL/TLS**
> Remember to restart loadbalancer when renew cert to take effect
1. Create .csr with openssl (Certificate Signed Request)

```bash
openssl req -new -sha256 -out terry.test.local.csr -newkey rsa:2048 -keyout "$1.key" -nodes -reqexts SAN - config <cat /some_ssl.cnf <(printf("[SAN]\nsubjectAltName=DNS:terry.test.local"))>> -out terry.test.local.csr
```

2. Request AD to signed .csr, created .crt
  a) https://gcp-dns-1.test.local (usually MS AD)
  b) download Base-64

3. Install crt
  a) Install in K8
    1. `kubectl create secret tls terry-tls --cert=terry.test.local.cer --key=terry.test.local.key`
    2. In Ingress file add tls property
  b) Install in server
    1. ssh into server
    2. copy .crt and key to /etc/test/conf/nginx/data/ssl


# CMDs
```bash
# General Certificate Sign Request from key
openssl req -new -key xxx.key -out xxx.csr
```

## Install CA Service
1. open Server Manager/manage/Add Roles & feature/.../Active Directory Certificate Services/
2. Install both `Certification Authority` & `Certification Authority Web Enrollment`
3. Generate CA private key, w name domain_name-server_name-CA
4. Configuare

## Interface w CA Service
1. open Server Manager/Tools/Certification Authority

`http://localhost/certsrv` or `http://pc_name.domain_name.local/certsrv`

# Generate Developer VPN cert
## by Microsoft UI
Microsoft Management Console `Run > mmc > Enter` export LDAP certificate for VPN
default config path `C:\Users\xxx\OpenVPN\config`
> xxx.ovpn
```bash
ca xxx_ca.crt
cert xxx.crt # Musted signed by CA
key xxx.key
```

## by Powershell
```powershell
Get-Certificate -Template XXX -CertStoreLocation cert:\xxx
Export-PfxCertificate -Cert cert:\xxx -FilePath yyy -Password 123
Remove-Item yyy
```

# Client login
## Single Sign-on (SSO)
1. save some shared secret/pub_key into DB
2. user used private_key to Generate JWT w user_name, time_of_sign, unqiue_id
3. we vertify JWT w pub_key & create session

## Initiative for Open Authentication (OATH)
> Think of OATH2.0 as JWT standard

### SAML
> Identity Provider(IDP) create jwt w user_id & Service Provider(internetal service)

> Tool: SAML tracer

# Secure Shell (SSH)
### Linux SSH
1. gen ssh key `ssh-keygen -b 4096`
2. create user in remote linux server
3. copy public key into /home/user_name/.ssh


### Windows
ssh-rsa is Developer Public Keys
1. PuTTYgen -> .ppk -> .ssh
2. Publish SSH to Admin
3. Add ssh key to github


# Buzzwords
- Man-in-the-middle (MITM)