# Postgres

## Funny Things

- Creating a new table in a schema does **not** automatically grant permissions to existing users.  
- Permissions are notoriously hard to manage.  
- Connection limits are easy to exceed; avoid connection leaks.  
- Up to version 14, `NULL` values are considered distinct for unique constraints; PostgreSQL 15 introduces `NULL NOT DISTINCT`.

## PSQL Cheat Sheet

```bash
psql -U postgres          # connect as user postgres
\l                        # list databases
\c <dbname>               # connect to a database
\dn                       # list schemas
SELECT * FROM information_schema.schemata;
\dt+                      # list tables with details
SELECT * FROM <table>;
```

### Show Configuration

```bash
psql -U postgres -c 'SHOW config_file';
```

## Common Queries

```sql
CREATE ROLE xxx WITH LOGIN;
CREATE DATABASE xxx_db WITH OWNER xxx;

GRANT USAGE, CREATE, ALL ON DATABASE xxx TO user_x;
GRANT SELECT, INSERT, UPDATE, DELETE ON SCHEMA public TO user_x;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO user_x;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO user_x;

ALTER USER xyz WITH PASSWORD 'xyz';
SELECT * FROM information_schema.role_table_grants WHERE table_name = 'xyz';
```

## Setup Steps

```bash
# Step 1: Initialise data directory (example version 9.4)
initdb -D /path/to/9.4/data

# Step 2: Start the server
pg_ctl -D /path/to/9.4/data -l logfile start

# Step 3: Install certificates
mkdir -p /var/lib/CA
# copy rootCA.crt, server.crt, server.key into that directory
# generate key and cert signed by your CA (openssl)

# Step 4: Edit postgresql.conf
listen_addresses = '*'
ssl = on
ssl_ciphers = 'HIGH:!aNULL:!MD5'
ssl_cert_file = 'server.crt'
ssl_key_file = 'server.key'
ssl_ca_file = 'rootCA.crt'

# Step 5: Edit pg_hba.conf
# TYPE  DATABASE   USER       ADDRESS          METHOD
hostssl xxx_db    xx_user    192.168.1.1/32   trust clientcert=1

# Step 6: Distribute CA and certificates to clients
scp root@192.168.x.x:/var/lib/CA/rootCA.crt ~/.postgresql/root.crt

# Step 7: Connect from a client
psql -h 192.168.x.x -U xxx xxx_db
```

## Debugging

```sql
SELECT pg_reload_conf();               -- reload config without restart
SELECT * FROM pg_available_extensions;
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

SELECT datname, pid, query FROM pg_stat_activity;
SELECT * FROM pg_stat_statements;

EXPLAIN ANALYZE UPDATE tenk1 SET hundred = hundred + 1 WHERE unique1 < 100;
```

### Configuration for pg_stat_statements

```conf
shared_preload_libraries = 'pg_stat_statements'   # requires restart
pg_stat_statements.max = 10000
pg_stat_statements.track = all
```
