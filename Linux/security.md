# Security

- Certificate Authority(CA)
  - who issued
  - who issued to
  - valid to
  - public key
  - digital signature

ssh-rsa is Developer Public Keys
1. PuTTYgen -> .ppk -> .ssh
2. Publish SSH to Admin
3. Add ssh key to github
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

### Setup VPN
Microsoft Management Console `Run > mmc > Enter` export LDAP certificate for VPN