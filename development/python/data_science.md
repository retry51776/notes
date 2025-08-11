## Data Warehouse Tools

- Amazon Redshift
- Google BigQuery
- Snowflake
- Teradata
- Micro Focus
- Cloud Data Platforms (store data in the cloud, process with Spark, elastic processing)

### ETL Challenges

1. Different source formats
2. Schema mismatches
3. Varying representations
4. Corrupted data
5. Scalability concerns
6. Schema evolution

## Databricks Components

- Web App
- Notebooks
- Jobs & Queues
- Cluster Management (Spark)

```
/Workspace
    * Shared Folder
    * Jupyter Notebook
    * Users
    * Cluster
    * Jobs
    * Experiments
```

Delta Lake is an open‑format storage layer (ACID). Databricks uses Delta Lake to store historical results.

### Messaging Systems

- Apache Pulsar / BookKeeper vs. Kafka

## Hive Tables

1. Enable task orchestration and install the Spark library.
2. Create startup/setup folders:
   - account_name
   - file_system
   - mount_point_path
   - dbutil.widgets
   - use widgets to pull secrets & tenant ID
3. Mount data lake (e.g., `abfs`).

### Data Flow

- Create streaming/engine folder
- Create Delta tables
- Convert streams into DataFrames (`spark.readStream`, body is binary)
- Define the DataFrame schema (convert body to string or JSON)
- Hook up a processor to the DataFrame:

```python
df = spark.readStream.format("delta").load("/path/to/delta")
processed = df.withColumn("value", some_transform(df["value"]))
query = (
    processed.writeStream
    .option("checkpointLocation", "/path/to/checkpoint")
    .foreachBatch(lambda batch_df, batch_id: some_process(batch_df))
    .start()
)
```

## Feature Selection Methods

> **​**  



###  S ? 



































































































































...

(The content appears ... ).