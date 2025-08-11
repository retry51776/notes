# Graph

> Query complexity really impacts LLM‑generated queries.

## Neo4j

- **NeoDash** – UI management tool for Neo4j  
- **Cypher** – query language  
- **APOC** – Awesome Procedures On Cypher  

### FAQ

> The Community Edition of Neo4j does not support multiple databases.  
> Important order of operations: `peek()` → `.data()` → `consume()`

```sql
CALL db.schema.visualization() YIELD nodes, relationships
RETURN nodes, relationships;

CALL db.labels();
CALL db.relationshipTypes();
CALL db.propertyKeys();

-- Step 1: Create Author nodes
MATCH (b:Book)
WITH DISTINCT b.author AS authorName
WHERE authorName IS NOT NULL
CREATE (:Author {name: authorName});

-- Step 2: Link Books to Authors
MATCH (b:Book)
MATCH (a:Author {name: b.author})
MERGE (b)-[:WRITTEN_BY]->(a);

-- Step 3: Remove the author property from Book nodes
MATCH (b:Book)
REMOVE b.author;

MATCH (ds:document_sheet)
WHERE 'Quality Measures' IN ds.keywords
RETURN DISTINCT ds;
```
