# SQL

> ACID: Atomicity, Consistency, Isolation, Durability.

## Languages

- Data Definition Language (DDL)  
- Data Manipulation Language (DML)  
- Data Control Language (DCL)  
- Data Query Language (DQL)  
- Transaction Control Language (TCL)  

## Common Frustrations

- It’s **not** a standard when it *should* be one.  
- Powerful functions can be performance killers; they should be used sparingly.

## Tips

- In MSSQL & MySQL < 5.8, multiple `NULL` values are allowed on a unique constraint.  
- Avoid wrapping column references in functions within `WHERE` clauses.  

  **Bad:** `WHERE ISNULL(sales.enddate, '2999‑12‑31') > @enddate`  
  **Good:** `WHERE sales.enddate IS NULL OR sales.enddate > @enddate`

- Break complex queries into temporary tables:

```sql
SELECT b, SUM(a) INTO #temp1 FROM source WHERE a > 2 GROUP BY b;
SELECT * FROM c JOIN #temp1 ON c.b = temp1.b;
```

- Ensure filter values have the same data type as the column.  
- Query from the smallest result set to the largest; let the optimizer do its job.  

### Index Usage

- **Clustered index** – stores rows physically in order of the key.  
- **Non‑clustered index** – separate structure that points to rows.  
- **Covering index** – non‑clustered index that includes all needed columns.

### Common Operators

| Operator          | Description                              |
|-------------------|------------------------------------------|
| Table Scan        | Full scan of the table (slow)            |
| Index Scan        | Reads every page in an index             |
| Index Seek        | Directly fetches qualifying pages       |
| Key Lookup        | Retrieves remaining columns after a seek |
| Nested Loop Join  | Cursor‑based, often fastest for small sets|
| Merge Join        | Sorted merge; fast but CPU‑intensive     |
| Hash Join         | Builds hash table; CPU intensive         |
| Stream Aggregate  | Requires sorted input                    |
| Hash Aggregate    | Blocking operation                       |

### Maintenance

- Single‑user mode vs. offline mode: be cautious when taking a database offline.  

## Under the Hood

- The query optimizer builds an execution plan that is “good enough.”  
- Plans are cached for reuse.  
- Cardinality estimator generates table statistics.

# MSSQL

> Jokes: “It says all in the name, it’s **MY** SQL, NOT yours!”

### Gotchas

- Indexes that support foreign keys can cause locking on all indexed columns during FK updates.  
- DDL statements are not rolled back by transactions.  
- Triggers do not fire when a foreign‑key column changes.

```sql
sp_who2 active;
KILL <session_id>;

SELECT conn.session_id, host_name, program_name,
       nt_domain, login_name, connect_time, last_request_end_time 
FROM sys.dm_exec_sessions AS sess
JOIN sys.dm_exec_connections AS conn
  ON sess.session_id = conn.session_id;

-- Window function example
SELECT original_uid,
       version,
       ROW_NUMBER() OVER (PARTITION BY original_uid ORDER BY version DESC) AS row_num
FROM template;
```

- `TempDB` is configurable since SQL 2016.  
- PolyBase allows querying external data sources such as MongoDB, Oracle, Spark.

# MySQL

```sql
CREATE PROCEDURE x_proc(IN xxx VARCHAR(255), OUT tt INT)
BEGIN
    DECLARE _xx INT(5);
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE xx_cursor CURSOR FOR SELECT xx FROM YY WHERE zz = xxx;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN xx_cursor;
    read_loop: LOOP
        FETCH xx_cursor INTO _xx;
        IF done THEN
            LEAVE read_loop;
        ELSE
            -- do something with _xx
        END IF;
    END LOOP read_loop;
    CLOSE xx_cursor;
    SET tt = 2;
END;

CALL x_proc('test', @tt);
SELECT @tt;
```

# SQLite

```sql
SELECT Column1, GROUP_CONCAT(Column2) FROM Table GROUP BY Column1;
```
