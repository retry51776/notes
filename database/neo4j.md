# Neo4j

```cypher
MATCH (e:Entity)
RETURN e,
       size([(e)<--() | 1]) AS in_degree,
       size([(e)-->() | 1]) AS out_degree,
       size([(e)--() | 1]) AS total_degree
ORDER BY total_degree DESC;
```
