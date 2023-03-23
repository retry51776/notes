# SQL
> atomicity, consistency, isolation, durability (ACID)

## Tips
- IN MSSQL & MySQL before 5.8 will NOT multiple NULL values on unique constrain.
- in where caluse, avoid using function on table columns
    - Bad: `where ISNULL(sales.enddate, '2999-12-31') > @enddate` 
    - Good: `where sales.enddate is NULL or sales.enddate > @enddate`
- break nested query into temp table SQL
```sql
select b, sum(a) into #temp1 where a > 2 group by b;
select * from c join #temp1 on c.b = temp1.b;
```
- make sure filter value is excatly same type as column
- always query from smallest result set(not always smallest table) to largest;
- Query Planner often can opitmized it, but not guarante

- Avoid Wild card is beginning, cost table scan EX `like %12`
- Query plan Tips
    - If cost above 5, SQL will try parellarism
    - Right click select check memory usage
    - Don't use table variable

- Implicit conversion
- TempDB spill


**Temp table|CTE|Var table**
- Table variable is RAM only, can rewrite, no session, but needs more code
- Temp table less code, requires drop, but lives within session


## Index
- Cluster index is unique index, row is store by cluster index
- None cluster index(index storage) is always store cluster index(reduce look up)
- Cover index is none cluster index including other columns


## Common Operators
- Table scan is slow
- Index Scan is touch every pages
- Index Seek is get qualified pages 
- Key Lookup is get other columns

- Nested Loop is cursor, fastest
- Merge Join is fast, but slightly CPU
- Hash Match cost a lot CPU

- Stream Aggregate required sorted
- Hash aggregate is blocking op

## Maintain
> single user mode vs offline mode
> 
> I'd remote into DB server, turn to offline mode
> 
> be careful on single user mode, no recommend


## Under the hood
> Query optimizer builds a good enough query plan
> 
> Plan cache story query plans
> 
> Cardinality Estimator Is generate table stats

# MSSQL

```sql
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


DECLARE @InsertQmId int
SELECT @InsertQmId = @@IDENTITY
```

- TempDB is configable since 2016
- Polyphase will allow mssql query other dB, ex: mongodb, Oracle, spark

# MySQL
```sql
create
    definer = terry@`%` procedure x_proc(IN xxx varchar, OUT tt int)
BEGIN
    declare _xx int(5);
    declare done int default false;
    declare xx_cursor CURSOR FOR
        SELECT xx FROM YY WHERE zz = xxx;
    declare continue handler for not found set done = TRUE;

    open xx_cursor;
    xx_loop: LOOP
        fetch xx_cursor INTO _xx;

        if done THEN
            LEAVE xx_loop
        else
            //whatever
        end if;
    end loop xx_loop;
    close xx_cursor;
    set tt = 2
    leave x_proc;
END;

call x_proc('test', @tt)
select @tt
```

# SQLlite
```sql
SELECT Column1, group_concat(Column2) FROM Table GROUP BY Column1
```