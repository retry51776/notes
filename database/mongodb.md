# MongoDB
> Is's not very fast on aggregation
**Python**
```js
self.mongodb = MongoClient(MONGODB_URI)[DB]
self.mongodb[COLLECTION].update_one(
    {'_id': ObjectId('123123')},
    {
        '$addToSet': {'users': user_id}
    }
)

.find_one({'_id': ObjectId('123123')}, {"_id": 1, "uid": 1})
.count()
.insert_one(XX).inserted_id
.delete_many()


```


**JS**
```js

mgCols = {
  $project: {
    company_uid: true,
    new_residents: { $size: '$new_residents' },
  },
}

// aggregate can do nested sub buckets, read offical docs
.db()
.collection(ZZ)
.aggregate([
  mgCols,
  { $match: { deleted: { $ne: true } } },
])

Promise.all(threePromises).spread((xx, yy, zz) => whatever(xx, yy, xx));
```
