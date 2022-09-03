# Auth
> Stuff about client authentication, authorization.

> Too many tools in this space. Some are lib just do one thing, then there are service just do Authentication or Authorization; Then there are platforms does both.

# Authentication
> Who?
> 
> Authentication standard does exists & most company uses similar / industry standard tool / platform.

### 3 ways:
- What you know?
  - Password
  - Token
    - Single sign-on (SSO)
- Who you are?
  - Biometric
- What you have?

### protocols:
- Kerberos
- SSL/TLS

# Authorization
> Can you? access control or client privilege.

> There are SO SO SO many lib, platform, tools, etc. IDK what is industry standard.


## Common Solutions
- okta
- Auth0
- [SSL/TLS](/devOps/network/security.md)
- [DNS](/devOps/network/dns.md)
- [Keycloak](/test/keycloak/README.md)

# Technology or Buzzwords
- OpenID Connect Standard (OAuth 2) `delegate client auth`
  - refresh token flow
  - refresh token rotation `out of order refresh token will invalid tokens family`
    - sliding expiration/windows `max refresh`
    - fix lifetime `lock max lifetime when access token created`
    - none `until revoke`
- MFA