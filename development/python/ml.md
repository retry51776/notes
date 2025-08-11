# Machine Learning (ML)

> Find data correlations using Pearson's coefficient.  

ANOVA stands for Analysis of Variance.

## Libraries
- NumPy
- pandas
- scikit‑learn

## Core Components
- **Loss functions**
  - Squared error  
  - Accuracy score
- **Feature engineering**
- **Algorithms**
  - LinearRegression
  - DecisionTree
    - RandomForest

# Artificial Intelligence (AI)

## Libraries
- PyTorch
- TensorFlow

```python
# Feature selection: recursive feature elimination
```

### KubeFlow Decorators
```python
@component()
def get_df(project_id):
    ddf.to_csv(data_out.path)
```
> A pipeline is compiled into JSON.

```python
@kfp.dsl.pipeline(name="", pipeline_root=xxx)
def pipeline():
    xxxx = xxx  # define steps here
```

## Model Types
- Dropout  
- Convolutional Neural Network (CNN)  
- Recurrent Neural Network (RNN)  
- Bidirectional RNN  
- Residual Networks (ResNet)  
- LSTM  
- Transformer (generates embeddings)  
- BERT (Bidirectional Encoder Representations from Transformers)

> Applications: Question Answering, Sentiment Analysis, Text Summarization

## Data Sampling
- Ensemble sampling

## Training Objectives
- Masked Language Modeling (MLM) – fill‑in‑the‑blank  
- Next Sentence Prediction (NSP) – infer context  

## Vertex AI

### Setup a Pipeline
```python
from kfp.v2 import compiler
import kfp.dsl as dsl

@dsl.pipeline(name="my-pipeline", pipeline_root="gs://my-bucket/pipelines")
def pipeline():
    df = xxx  # already cleaned
    step1_out = step1.do_x(df)
    step2_out = step2.do_y(step1_out.outputs['out'])

compiler.Compiler().compile(pipeline_func=pipeline, package_path="pipeline.json")
```

```python
from kfp.v2.dsl import component, Dataset, Input, Output, Artifact

@component(
    base_image='python:3.9',
    packages_to_install=['pandas']
)
def step1(num1: float, x_in: Input[Dataset], out: Output[Artifact]):
    import pandas as pd
    with open(out.path, 'w') as f:
        f.write('xxx')
```

```python
from sqlalchemy.sql import select, text
```

# Tesla AI Networks

- Occupancy Network  
- Lane Network  
- Traffic Control  
- Road Sign Network  
- Moving Object Network  
- Path Planning Network  

## Occupancy
> Converts raw sensor data into a base geometry layer (i.e., things near the vehicle without identifying them).  
> Produces a 3‑D vector space, determines whether objects are static or moving, and predicts motion of unidentified objects. Runs every 10 ms.

### Dataflow
1. 8 camera streams → raw data.  
2. RegNets & BiFPNs extract features.  
3. Spatial Attention focuses on selected features (spatial & multi‑camera query embeddings).  
4. Temporal Alignment joins vehicle telemetry to create spatio‑temporal features.  
5. Occupancy & Occupancy Flow generate volumetric output via deconvolution networks (current surroundings + predictions).  
6. Drivable Surface & Queryable Output feed downstream processes.  

*NeRF*: 3‑D reconstruction from occupancy data.

## Lane & Object Detection
- Predict lanes and future object behavior.  
- Lane connectivity uses satellite maps to generate lane graphs; these can produce training data or serve as input for planning.  
- Tesla aggregates global lane maps (world‑scale) by merging trips, performing pairwise matching, surface refinement, and auto‑detecting new routes.  

### Dataflow
1. 8 camera streams → geometry extraction.  
2. Combine with navigation map → Lane Guidance Module.  
3. World tensor → lane graphs & adjacency matrix.

## Path Planning (Decision Layer)
> Makes decisions every 50 ms.

- Considers all possible interactions and aligns planning to interaction cost (~10 ms).  
- **Goal Candidates**: most likely solutions.  
- **Seed Trajectories**: predicted trajectories of other agents.  
- **Interaction Search**: combines seed trajectories with goal candidates; scores each interaction and selects the best goal candidate using a neural planner.  

## Auto‑Labeling
> Labels lanes, planners, objects, shapes, occupancy, etc., similar to a factory line (yield, quality, quantity, inventory).

## Simulation Inputs
- Lane graph  
- Weather conditions  
- Road participants  
- Scenarios (e.g., trophies)

## Data Management
> Identify problematic prediction datasets (“challenge cases”) and find similar examples.  

Vehicle signals are detected by sub‑networks that infer car status.

