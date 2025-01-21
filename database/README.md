# Database
> POV from application developer;


### TODO
- common DB data structure, b tree
- common algo
- common bad query & fixes
- list of tradeoffs on different dbs

## Data

- Things to consider:
    - Data Structure
    - Data Volume
    - Ephemeral `last very short`
    - Latency Tolerance
    - Security
    - Aggregation & Query Demand

## NoSQL DB

- BloomFilter `common algorithm search data contain some element, either no, or most likely yes; hash all set into single bit arrays, store all hashed dataset into array bits; check hashed target bits are on in array bits;`