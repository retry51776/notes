# Elasticsearch

## Cluster Settings (POST)

```http
/_cluster/settings?include_defaults=true
/_delete_by_query
{
  "persistent": {
    "indices.breaker.request.limit": "70%"
  },
  "settings": {
    "index": {
      "mapping": {
        "total_fields": { "limit": 3000 },
        "nested_fields": { "limit": 100 }
      }
    }
  }
}
```

## Queries

```json
{ "exists": { "field": "test" } }

{
  "nested": {
    "path": "stays",
    "query": {}
  }
}
```

### Bulk Operations

**Insert**

```json
{
  "_routing": doc['CompanyUID'] || -1,
  "_source": doc
}
```

**Upsert**

```json
{
  "_op_type": "update",
  "_routing": quarter['company_uid'],
  "_id": `${quarter['provider_uid']}_${quarter['quarter_name']}`,
  "doc": quarter,
  "doc_as_upsert": true
}
```

### Dynamic Templates

```json
{
  "dynamic_templates": [{
    "XXXX_pattern": {
      "path_match": "*.crazy_pattern",
      "mapping": { "type": "double" }
    }
  }]
}
```

### Scripted Queries (Painless)

```json
{
  "script": {
    "lang": "painless",
    "source": "doc['cc.xx'] != doc['cc.xx']",
    "params": { "multiplier": 2 }
  }
}
```

## Boolean Logic

- `filter` – always executed, does not affect scoring  
- `must` – required clause (affects score)  
- `must_not` – must not match  
- `should` – optional; use `minimum_should_match` to control  

## Aggregations

- **terms** – can have sub‑aggregations  
- **reverse_nested** – move back to root level  
- **top_hits** – cannot have sub‑aggregations beneath it  
- Metric aggregations cannot contain sub‑aggs.  
- **collapse** – simple field collapsing without full aggregation cost  

### Important Notes

- Non‑indexed fields cannot be used in filters.  
- Text fields are tokenized; keyword (string) fields are not.  
- Deleted documents remain until segment merging.  
- In ES 7, only a single `_type` per index is allowed.  
- `track_total_hits: true` returns the full hit count (default is 10 000).  

## Breaking Changes in ES 7

- `hits.total` → `hits.total.value`  
- Mappings allow only one type per index.  
- Use `helpers.bulk(..., index=index)` for bulk operations.  

### Python Example

```python
from elasticsearch import helpers

for doc in helpers.scan(es, index=index, query=query):
    # process each document
    pass
```

#### Scripted Metric Aggregation (Painless)

```json
{
  "scripted_metric": {
    "params": { "x_agg": {} },
    "init_script": "params._agg.x_agg = []",
    "map_script": "params._agg.x_agg.add(params._source.x)",
    "combine_script": "",   // runs on each shard
    "reduce_script": ""     // runs on the coordinating node
  }
}
```
