SQL Server Integration Services (SSIS)

Data Warehouse Tool
- Amazone RedShift
- Google BigQuery
- SnowFlake
- TeraData
- MicroFocus

SnowFlake
cloud data warehouse platform

Warehouse - Already format
DataLake - Just store it, format it later
Cloud Data Platform - Store in Cloud, Spark Process, Elastic Process
Spark SQL flexible APIs support different sources

Hadoop runs slow because on disk; writen in Java
Spark runs faster because on RAM; written in Scalar
Pandas run on single machine
PySpark run on multiple machines

ETL Problems:
1. different source/format
2. Schema mismatch
3. Different representation
4. Corrupted data
5. Scalability
6. Schema evolution


# Databrick
Data analytics platform base off Apache Spark

## Components
- Web App
- Notebooks
- Job & Queues
- Cluster Managerment(Spark)

/Workspace
    * Shared Folder
    * Jupitor Notebook
    * Users
    * Cluster
    * Jobs
    * Experiments

Delta Lake is open Format Storage Layer(ACID), Databrick use delta lake to store historical result

Apache Pulsar/BookKeeper vs Kafka

Hive Tables
1. Enable Task Orchestration & Install event spark library
2. Create StartUp/SetUp Folder
    * account_name
    * file_system
    * mount_point_path

    * dbutil.widgets
    * use widgets pull secrets & tenant_id

    * Mount Data Lake
    * Setup abfs for data lake
3. Create Streaming/Engine Folder
    * Create Delta Tables
    * Convert Stream into DataFrame (spark.readStream, body is binary)
    * define dataFrame schema, it will convert body to string or json
    * Hook up proceessor to DataFrame (message_df.writeStream.option().foreachBatch(some_process).start())
Data Table for ETL, can uplaod example.json let databrick auto create schema;
4. 


Workspace/Data Science View
    - Workspace
    - Repos
    - Data
    - Cluster
    - Job
    - Model
SQL Analytics (BI view)
    - SQL Endpoint // Think of it as K8 job
    - Queries // Shared query or views
    - Alert // Tigger some scipt
    - History



/Overview
    /Blobs
        /Project_Name
            /output
                /aggergate.csv (store meta during exe cution)
                    


Databrick Runtime
- spark
- others?


1. Create Work Cluster(Amount resource to do the work, which Python, which Databrick Version)
2. Create Resource Group to save dataset & control premission
3. Create Notebook & Design workflow
4. Let Databrick control scale 


# Buzzword Zoo
- Shared Disk Architecture
- Shared Nothing Architecture
- Confusion Matrix

want low False possitity
Predict Analytics & Prescriptive Analytics 