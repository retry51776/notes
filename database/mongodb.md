# MongoDB

> It's not very fast for aggregation.

## Python
```python
self.mongodb = MongoClient(MONGODB_URI)[DB]
self.mongodb[COLLECTION].update_one(
    {'_id': ObjectId('123123')},
    {
        '$addToSet': {'users': user_id}
    }
)

self.mongodb[COLLECTION].find_one({'_id': ObjectId('123123')}, {"_id": 1, "uid": 1})
self.mongodb[COLLECTION].count_documents({})
self.mongodb[COLLECTION].insert_one(XX).inserted_id
self.mongodb[COLLECTION].delete_many(filter)
```

## JavaScript
```javascript
const mgCols = {
  $project: {
    company_uid: true,
    new_residents: { $size: '$new_residents' },
  },
};

// Aggregation can do nested sub‑buckets; see the official docs.
db()
  .collection(ZZ)
  .aggregate([
    mgCols,
    { $match: { deleted: { $ne: true } } },
  ]);

Promise.all(threePromises).spread((xx, yy, zz) => whatever(xx, yy, zz));
```
