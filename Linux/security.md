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