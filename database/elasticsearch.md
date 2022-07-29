# Elasticsearch
Post Ops
```js
/_cluster/settings?include_defaults=true
/_delete_by_query

{
  "persistent": {
    "indices.breaker.request.limit": "70%"
  },
  "setting": {
    "index": {
      "mapping": {
        "total_fields": {
          "limit": 3000
        },
        "nested_fields": {
          "limit": 100
        }
      }
    }
  }
}
```
Query
```bash
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

bool => boolean logic wrapper
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
- `track_total_hits`: true, # by default only 10,000

# ES7 breaking changes

- ['hits']['total'] => ['hits']['total']['value']
- mappings only allow single type
- _send_bulk_operations(index=index)

https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-metrics-scripted-metric-aggregation.html

# Tech stack

splunk is similar to logstash. bank of America use splunk store its logs

> Data loss can happen in a number of ways, you need to be able to recreate the data if needed. True, Elasticsearch has a snapshot/restore feature, but this process will only ever partially recover you in the event of data loss. Updates made between the most recent snapshot and the outage will be lost unless you have another system in place to queue them. Snapshot/restore will also not help in the event of split-brain, because there’s no mechanism for reconciling updates to each partition. Updates will just be lost.

# Python
```py
from elasticsearch import helpers
for doc in helpers.scan(
  es,
  index,
  query,
  scroll,
  routing
)

{
  "script": {
    "script": {
      "land": "expression",
      "params": {
        "ppp": [1,2,3]
      }
      "source": '''
        for (int i=0; i< params.ppp.length; i++) {
          if (doc['xxx'] > 123 && doc['yyy'] == params.ppp[i]) return true;
          return false;
        }
      '''
    }
  }
}

{
  "scripted_metric": {
    "params": {
      "x_agg": {}
    },
    "init_script": "params._agg.x_agg = []",
    "map_script": "params._agg.x_agg.add(params._source.x)", // pick values
    "combine_script": "", // run shard level
    "reduce_script": "",// run node level
  }
}
```