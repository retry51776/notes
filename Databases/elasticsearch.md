# Elasticsearch
Post Ops
```
/_cluster/settings?include_defaults=true
/_delete_by_query
```
Query
```
exists: {"field": "test"}

"nested" : {
    "path": "stays",
    "query": {}
}

bulk insert
{
    '_routing': doc['CompanyUID'] or -1,
    '_source': doc,
}

bulk upsert
{
    '_op_type': 'update',
    '_routing': quarter['company_uid'],
    '_id': f"{quarter['provider_uid']}_{quarter['quarter_name']}",
    'doc': quarter,
    'doc_as_upsert': True
}


"dynamic_templates" : [{
    "XXXX_pattern" : {
          "path_match": "*.crazy_pattern",
          "mapping": {
                "type": "double"
          }
    }
}]

{
	"script": {
      "script": {
        "lang":   "expression",
        "inline": "doc['cc.xx'] != doc['cc.xx'] ",
        "params": {
          "multiplier": 2
        }
    }
}
				}


```

bool => boolean logic wraper
- filter (NPL will be different)
- must
- must_not
- should
  - 'minimum_should_match' : 1,

aggs
- terms: allow sub_aggregation, very powerful
- reverse_nested: back to root level
- top_hit: not allow sub_aggregation below top_hit
- metric aggregation can't have sub aggs.
- collapse: simple way to achieve first level field collapsing without the cost of running a full aggregation on it

**Notes**
- Not indexed field can't be use in filter
- Text will tokenized but String won't
- delete won't physical gone until Lucien document get merge
- In ES7, only allow single _type per index

# ES7 breaking changes

- ['hits']['total'] => ['hits']['total']['value']
- mappings only allow single type
- _send_bulk_operations(index=index)

https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-metrics-scripted-metric-aggregation.html

# Tech stack

splunk is similar to logstash. bank of America use splunk store its logs
