# ML

> Find data correlation
Pearson's coefficient

ANOVA stands for Analysis of Variance


## Libraries
numpy
pandas
scikit learn

## Components
Loss function
    - square error
    - accuracy_score
Feature Engineer
Alg.
    LinearRegression
    DecisionTree
        - RandomForest

# AI
## Libraries
pyTorch
Tensorflow

```py
# take out feature at a time
recursive feature removal

# KubeFlow decorator
@component()
def get_df(project_id):
	ddf.to_csv(data_out.path)

pipeline is compile into json

@kfp.dsl.pipeline(name="", pipeline_root=xxx):
	xxxx = xxx.
```
## Models
- dropout
- Convolution Neural Network (CNN)
- (RRN)
- BiDirection
- ResNetwork

- LSTM
Transformer generate embedding
Bidirectional Encoder Representation Transformers(BERT)
> Question Answering
> Sentiment Analysis
> Text Summarization

# Dats Sample
Ensemble Sampling

# Trainning
- Masked Language Modeling (MLM) fill in blank
- Next Sentence Prediction (NSP) figure context

## Vertex AI
### Setup Pipeline
```py
from kfp.v2 import compiler
@kfp.dsl.pipeline(name, pipeline_root)
def pipeline():
    df = xxx; // already clean
    step1_out = step1.do_x(df)
    step2_out = step2.do_y(step1_out.outputs['out'])

compiler.Compiler().compile(pipeline_func=pipeline, package_path)
```

```py
from kfp.v2.dsl import component, Dataset, Input, Output
@component(case_image='', packages_to_install=[])
def step1(num1: float, x_in: Input[Dataset], out: Output[Artifact]):
    import pandas as pd
    with open(out.path, 'w') as f:
        f.write('xxx')

from sqlalchemy.sql import select, text
```

# Tesla AI Networks
- Occupancy Network
- Lane Network
- Traffic Control 
- Road Sign Network
- Moving Object Network
- Path Planning Network

## Occupancy - `Level convert Raw data to base geometry layer; aka things near me, but don't identify things`
> roduce 3d vector_space, determent object is stable or in motion; Also predict motion of object without determent object; Runs every 10ms;

#### Dataflow
- 8 Camera raw data input
- RegNets & BiFPNs `get features`
- Spatial Attention `focus on select features; spatial query & mutlicam query embedding`
- Temporal Alignment `Join w car's own telemetry generate spatiotemporal features`
- Occupancy & Occupancy Flow `using deconvolutions_network generate volume output; aka my current surrounding & surrounding prediction`
- Drivable Surface & Queryable Output `For downstream processes`

NeRF State `3D reconstruction from Occupancy`

## Lane & Object - `Identify things & predict future motion`
- predict lane & predict future behavior
- Lane Connectivity `Tesla uses satellite & drive path to generate lane connectivity; Lane Connectivity can generate tranning data, or input data for Planning;`
- Tesla has world lanes Connectivity `join multi-trip, aka answer, or world map, too big embed into car; Course Alignment, Pairwise Matching; Joint Optimization; Surface Refinement; Auto Detect new trips;`
- car has smaller Lane Detection Network with 12 mil params `High precision Trajectory`
- Embedding Table * One_hot_encoding = token

#### Dataflow
- 8 camera row data input -> Geometry
- Mix w Navigation Map -> Lane Guidance Module
- World Tensor -> Lanes Graphs & Adjacency Matrix

## Path Planning - `Decision layer makes decision every 50ms`
> Think all possible interactions, align planning to interaction cost 10ms
> Goal Candidates `most likely solution`
> Seed Trajectories `other subject's most likely trajectories; aka predict others`
> Interaction Search `Seed_Trajectories join Goal_Candidates produces many Interactions; Planning needs to score each Interactions & pick a Goal_Candidate; That needs Interaction search engine(Neural Planner); Seed_Trajectories will predict Ghost_Object that car can't see but able to predict`

## Auto Label
> label lanes, planner, object, shape, Occupancy, just like factory, has yield, quality, quantity, inventory

## Simulation
inputs
- lane graph
- weather
- things in road
- trophy

## Data
> Find wrong prediction dataset(Challenge Case), find similar dataset
Vehicle Signal `Sub network detect car status`