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


// take out feature at a time
recursive feature removal

KubeFlow decorator
@component()
def get_df(project_id):
	ddf.to_csv(data_out.path)

pipleline is compile into json

@kfp.dsl.pipeline(name="", pipeline_root=xxx):
	xxxx = xxx.

## Models
dropout
Convolutional Neural Network (CNN)
(RRN)
BiDirection
ResNetwork

LSTM
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
```
from kfp.v2 import compiler
@kfp.dsl.pipeline(name, pipeline_root)
def pipeline():
    df = xxx; // already clean
    step1_out = step1.do_x(df)
    step2_out = step2.do_y(step1_out.outputs['out'])

compiler.Compiler().compile(pipeline_func=pipeline, package_path)
```

```
from kfp.v2.dsl import component, Dataset, Input, Output
@component(case_image='', packages_to_install=[])
def step1(num1: float, x_in: Input[Dataset], out: Output[Artifact]):
    import pandas as pd
    with open(out.path, 'w') as f:
        f.write('xxx')

from sqlalchemy.sql import select, text
```