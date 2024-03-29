# Postgres

**Funny Things**
- when create new table in SCHEMA, existing user won't auto get permission
- permission is very hard to manage in postgres
- limit connections, very easy to blow up, avoid connection leak
- 14 & older Postgres treat NULL as unique; Only 15 has new clause NULL NOT DISTINCT

## PSQL
```bash
psql -U postgres

# show DB
\l
# switch DB
\c postgres
# show schemas
\dn
select * from information_schema.schemata;
# show table
\dt+
select * from xxx;

# show config
psql -U postgres -c 'SHOW config_file'
```
## Query
```sql
create role xxx with login;
create database xxx_db with owner xxx;

GRANT [usage | create | all] ON DATABASE [DB] TO [USER]
GRANT [permission] ON SCHEMA [SM] TO [USER]
GRANT [permission] ON ALL TABLES IN SCHEMA [SM] TO [USER]
GRANT [permission] ON ALL SEQUENCES IN SCHEMA [SM] TO [USER]

ALTER USER xyz WITH PASSWORD 'xyz';
SELECT * FROM information_schema.role_table_grants WHERE table_name = 'xyz';
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


## Debug
```sql
psql -U postgres -c 'SHOW config_file'

select * from pg_available_extensions;
create extension pg_stat_statements;

SELECT datname,procpid,current_query FROM pg_stat_activity;
select * from pg_stat_statements;

EXPLAIN ANALYZE UPDATE tenk1 SET hundred = hundred + 1 WHERE unique1 < 100;

```


```config
# Require Restart
# postgresql.conf
shared_preload_libraries = 'pg_stat_statements'

pg_stat_statements.max = 10000
pg_stat_statements.track = all
```