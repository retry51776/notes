# Graph

> Query complexity really impact LLM generate query.

## Neo4j

- NeoDash `UI management tool for neo4j`

- Cypher `query language`

- Awesome Procedures On Cypher (APOC)

FAQ:

> Community Edition of Neo4j does not support multiple databases

> Important Orders: peek() > .data() > consume()

```sql
CALL db.schema.visualization() YIELD nodes, relationships
RETURN nodes, relationships

CALL db.labels()
CALL db.relationshipTypes()
CALL db.propertyKeys()


// Step 1: Create Author nodes
MATCH (b:Book)
WITH DISTINCT b.author AS authorName
WHERE authorName IS NOT NULL
CREATE (:Author {name: authorName});

// Step 2: Link Books to Authors
MATCH (b:Book)
MATCH (a:Author {name: b.author})
MERGE (b)-[:WRITTEN_BY]->(a);

// Step 3: Remove the author property from Book nodes
MATCH (b:Book)
REMOVE b.author;

MATCH (ds:document_sheet)
WHERE 'Quality Measures' IN ds.keywords
RETURN DISTINCT ds
```
