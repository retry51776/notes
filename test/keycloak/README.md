
### Keycloak
> Open source IAM, since 2014
>
> Realm `similar to OU in LDAP`

- Resource `EX: files on google drive`
- Owner `EX: u`
- Resource Server `EX: google drive`
- Client `EX: Draw.io`
- Authorization Server `EX: grant access`

### Auth Code FLow
1. Owner Request Client
2. Client gen request to Auth Server
3. Auth Server Ask user cred
4. Auth Server give Auth Token to Client
5. Client send Auth Token w their pub key, to get Access Token from Auth Server
6. Client request Resource Server w Access Token

### Auth Implicit Flow
1 - 4. same
5. Auth Server send Access Token directly to Client `Without Client pub key`
6. Same

### Client Cred Flow
1. service1 get access token from auth server
2. service1 send req w access token(JWT) to service2


### Keycloak features
- Single Sign-on (SSO)
- OAuth 2
- Social Login
- LDAP
- Management
- User Federation `either link to LDAP or Kerberos`

# UI
## Admin Portal
http://localhost:8080/admin/master/console/#/realms/xxx_realm
http://localhost:8080/admin/master/console/#/realms/Terryland
- /Realm Setting
    - /General `Login page style`
    - /Login `Can User reset password?`
    - /Keys `Private keys`
    - /Email `Forget Password, Confirm Email Setting`
    - /Themes `styles`
    - /Localization `idk?`
    - /Cache
    - /Tokens `Session TTL setting`
	- /Client `Authorization`
		- /Resource `resource label`
		- /Authorization scopes `action label; verbs;`
		- /Policies `logic return boolean, can be nested`
    		- Role `user tag`
    		- client `3rd party`
    		- Time `only xxx time`
    		- User `specific user`
    		- Aggregated `nested policies, combine logic`
    		- group `group policies`
		- /Permissions
			- resource based `only resource`
			- scope based `both resource & verb`
    	-  /Evaluate `Testing tool`
## User Portal
http://localhost:8080/realms/xxx_realm/account/
http://localhost:8080/realms/Terryland/account/

