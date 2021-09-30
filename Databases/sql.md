# SQL general

- in where caluse, avoid using function on table columns
    - Bad: `where ISNULL(sales.enddate, '2999-12-31') > @enddate` 
    - Good: `where sales.enddate is NULL or sales.enddate > @enddate`
- break nested query into temp table SQL
```
select b, sum(a) into #temp1 where a > 2 group by b;
select * from c join #temp1 on c.b = temp1.b;
```
- make sure filter value is excatly same type as column
- always query from smallest result set(not always smallest table) to largest;
  - Query Planner often can opitmized it, but not guarante

**Temp table|CTE|Var table**
- Table variable is RAM only, can rewrite, no session, but needs more code
- Temp table less code, requires drop, but lives within session


**Index**
- Cluster index is unique index, row is store by cluster index
- None cluster index(index storage) is always store cluster index(reduce look up)
- Cover index is none cluster index including other columns


Common Operators
    - Table scan is slow
    - Index Scan is touch every pages
    - Index Seek is get qualified pages 
    - Key Lookup is get other columns

    - Nested Loop is cursor, fastest
    - Merge Join is fast, but slightly CPU
    - Hash Match cost a lot CPU

    - Stream Aggregate required sorted
    - Hash aggregate is blocking op
**Maintain**

- single user mode vs offline mode
- I'd remote into DB server, turn to offline mode
- be careful on single user mode, no recommend


# MSSQL

```
sp_who2 active
KILL session_id

SELECT conn.session_id, host_name, program_name,
    nt_domain, login_name, connect_time, last_request_end_time 
FROM sys.dm_exec_sessions AS sess
JOIN sys.dm_exec_connections AS conn
   ON sess.session_id = conn.session_id;

Windows Function Example:
select
original_uid,
version,
row_number() over
    (partition by original_uid order by version desc) row_num
from template
where template.provider_uids <@ ARRAY[{}]::integer[]
group by 1, 2
```

- TempDB is configable since 2016
- Polyphase will allow mssql query other dB, ex: mongodb, Oracle, spark

# MySQL
