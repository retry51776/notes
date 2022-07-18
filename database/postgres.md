# Postgres

**Funny Things**
- when create new table in SCHEMA, existing user won't auto get premission
- premission is very hard to manage in postgres
- limit connections, very easy to blow up, avoid connection leak
- 

## Query
```
create role xxx with login;
create database xxx_db with owner xxx;

GRANT [usage | create | all] ON DATABASE [DB] TO [USER]
GRANT [premission] ON SCHEMA [SM] TO [USER]
GRANT [permission] ON ALL TABLES IN SCHEMA [SM] TO [USER]
GRANT [premission] ON ALL SEQUENCES IN SCHEMA [SM] TO [USER]
```

## Setup
```bash
# Step 1: Create DB
init -D 9.4/data
pg_ctl -D 9.4/data -l logfile start

# Step 2: create crt to DB folder
# 1. mkdir /var/lib/CA & put (rootCA.crt, server.crt, server.key)
# 2. openssl generate key & .crt that signed by CA
# Go to /security.md for more details

# Step 3
# vi postgresql.conf
listen_address="*"
ssl=on
ssl_ciphers = 
ssl_cert_file = "server.crt"
ssl_key_file = "server.key"
ssl_ca_file = "rootCA.crt"

# Step 4
# vi pg_hba.conf
# Type     Database        User        Address          Method
hostssl    xxx_db          xx_user      192.168.1.1/32  trust clientcert=1

# Step 5
# Copy CA, server, client crt & client.key to client side
scp root@192.168.x.x:/var/lib/CA/rootCA.crt ~/.postgresql/root.crt

# Step 6
# Login
psql -h 192.168.x.x -U xxx xx_db
```

