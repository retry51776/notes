## Data Warehouse Tool
- Amazone RedShift
- Google BigQuery
- SnowFlake
- TeraData
- MicroFocus
- SnowFlake `cloud data warehouse platform`
- Cloud Data Platform `Store in Cloud, Spark Process, Elastic Process`
- Spark SQL `flexible APIs support different sources`
- Hadoop `runs slow because on disk; writen in Java`
- Spark `runs faster because on RAM; written in Scalar`
- Pandas `run on single machine`
- PySpark `run on multiple machines`
- Databrick `Data analytics platform base off Apache Spark`


### ETL Problems:
1. different source/format
2. Schema mismatch
3. Different representation
4. Corrupted data
5. Scalability
6. Schema evolution


## Databrick Components
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

## Feature Selection Methods
> Too much feature can distract model accuracy and increase cost
### Filter Method
   - Pearson Correlation `static Correlation`
   - Chi-Squared `static Correlation`
   - ANOVA Test `static Correlation for category`
### Wrapper Method
   - Forward Selection `Add feature 1 at a time`
   - Backward Elimination `Model accuracy less than 0.05 change`
   - Recursive Feature Elimination (RFE) `I think of this approch similar greedy method`
### Embedded Method
   - Lasso: selectFromModel ?
   - Tree-Based: selectFromModel ?
   - I know some 3rd platform have build in param search, even come with UI visual result.

# Buzzword Zoo
- Warehouse `Already format & agged`
- DataLake `Just store it, format it later`
- Shared Disk Architecture
- Shared Nothing Architecture
- Confusion Matrix
- SQL Server Integration Services (SSIS)
- Predict Analytics & Prescriptive Analytics 

# Pandas
pandas.pydata.org/pandas-docs/
```
import pandas as pd
df = pd.read_csv('xx.csv')
df = pd.read_sql(query, con)
df = pd.DataFrame.from_dict()
del df['Company1']
def.loc[['row1', 'row2']] // get 2 rows
def.loc[['C1', 'C2']] // get 2 cols
def.loc[['row1', 'C2']] // get value
df.column_name.to_list()
df.head() // view dataset
df.nlargest(10, 'x_col') // view 10 rows sort by x_col
df.apply()
df = df.dropna(subset=['Company2'])
df = df.rename(
    {
        'Company2': 'Google',
        'Company3': 'FB',
    },
    axis=1
)
```

# sklearn
```
from sklearn.preprocessing import RobustScaler
normilizer = RobustScaler().fix(df)
normilizer.transform(X)


from sklearn.feature_selection import chi2, SelectKBest
best_features = SelectKBest(score_func=chi2, k=5)
select_features = best_features.fix(X, Y).columns
```

# ray
```
import modin.pandas # pandas that using ray
import ray
ray.init()
res = [xx.remote(1), xx.remote(2)]
ray.get(res)

@ray.remote()
def xx(p):
    pass

from sklearn.feature_selection import RFECV
from sklearn.metrics import mean_squared_error


```