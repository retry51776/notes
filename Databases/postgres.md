# Postgres

**Funny Things**
- when create new table in SCHEMA, existing user won't auto get premission
- premission is very hard to manage in postgres
- limit connections, very easy to blow up, avoid connection leak
- 

```
GRANT [usage | create | all] ON DATABASE [DB] TO [USER]
GRANT [premission] ON SCHEMA [SM] TO [USER]
GRANT [permission] ON ALL TABLES IN SCHEMA [SM] TO [USER]
GRANT [premission] ON ALL SEQUENCES IN SCHEMA [SM] TO [USER]
```

