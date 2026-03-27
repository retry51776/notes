# Data Science

## Table of Contents

- [Data Warehouse Tools](#data-warehouse-tools)
- [Databricks Components](#databricks-components)
- [Hive Tables](#hive-tables)
- [Feature Selection Methods](#feature-selection-methods)

## Data Warehouse Tools

- Amazon Redshift
- Google BigQuery
- Snowflake
- Teradata
- Micro Focus
- Cloud data platforms:
  store data in the cloud, process with Spark, and scale elastically.

### ETL Challenges

1. Different source formats
2. Schema mismatches
3. Varying representations
4. Corrupted data
5. Scalability concerns
6. Schema evolution

## Databricks Components

- Web app
- Notebooks
- Jobs and queues
- Cluster management for Spark

```text
/Workspace
    * Shared Folder
    * Jupyter Notebook
    * Users
    * Cluster
    * Jobs
    * Experiments
```

Delta Lake is an open-format storage layer with ACID guarantees.
Databricks uses Delta Lake to store historical results.

### Messaging Systems

- Apache Pulsar / BookKeeper vs. Kafka

## Hive Tables

1. Enable task orchestration and install the Spark library.
2. Create startup/setup folders:
   - `account_name`
   - `file_system`
   - `mount_point_path`
   - `dbutils.widgets`
   - Use widgets to pull secrets and tenant IDs.
3. Mount the data lake, for example with `abfs`.

### Data Flow

- Create a streaming or engine folder.
- Create Delta tables.
- Convert streams into DataFrames. `spark.readStream` often starts with
  a binary body.
- Define the DataFrame schema, then convert the body to string or JSON.
- Hook up a processor to the DataFrame.

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

- Filter methods:
  rank features with statistics such as correlation, chi-square, or
  mutual information before model training.
- Wrapper methods:
  evaluate subsets directly, for example forward selection or recursive
  feature elimination.
- Embedded methods:
  let the model learn importance during training, such as L1
  regularization or tree-based feature importance.
