# AI
> I think the fundamental idea of AI is past determent future.
> > What I mean is AI extract pattern from past data, assumes those pattern will most likely works in future problem.

## Basic Terms:
- Learning Workflow
  - Forward Propagation
  - Backward Propagation
    - Lost
- Neuron `fundamental unit in a neural network that performs a simple mathematical operation on input data and passes the result to other neurons or output units`
  - Activation function
  - Weight
  - Bias `a value that is added to the output of a neuron before it is passed to the next layer.`
- Prompt Engineering `aka use beginning statement to set context for AI`

## Architecture
> Think of AI as a kid, we are designing games to see which game `architecture` help AI `kid` grow;

- Stable diffusion: add noise to image, let AI recover image;

- Language Model is statical model of large text db. AI usually very agreeable/static basie.

- Sparse Autoencoders
> Brain uses Sparse Repr, it save energy, residliant to noise

### Sparse Modeling
> The goal is reduce input dimensional space to reduce noise.
> The lose function of Sparse Modeling has extra Regularization to encourage sparsity in the network

x = D * α
- x `input signal`
- Dictionary (D) `n(input size) by k matrix; Think as collection of basic feature sets;`
- n `flaten input(x) size; also dictionary's width`
- k `dictionary's columns, usually bigger n`
- α `multi hot encoding vector;`
- l0 `norm is counting the non-zero in α`
- atom `a column from dictionary; think as a basic feature set;`
> input = collection of atoms from Dictionary 

> The goal is find a dictionary where each data will repr by a few atoms from dictionary.

Relaxation (Basic Pursuit)
Go Greedy (Matching Pursuit)

Predefined dictionary: steerable, wavelet, curvelet, contourlets, bandlets.

Sparse Indentification of NoneLinear Dynamics(SINDy) converts time-series data to sparse model

sparse optimization algorithm
- Least Absolute Shrinkage and Selection Operator(Lasso)
- Orthogonal Matching Pursuit (OMP)
- Basis Pursuit (BP)
- Matching Pursuit (MP)
- Elastic Net
- Hard Thresholding


## Cool AIs
- CodeFormer `Image/movie recover & enhance AI`
- ChatGPT `Everyone knows`
- Quillbot `Rephrase text`
- https://beta.elevenlabs.io/voice-lab
- https://you.com/
- midjourney
- Heygen.com `video generation ai`


## IMO
- There isn't a correct hidden state, rather these problem has similar feature sets. `CNN first layer recognized edges, then lines, then organs.`

- I think we need more localized, more parrell algorthims. I think back propergation is too global. My guess is unfired neuron stack up voltage cause correction. 

- List of Human ability/skills that AI need to learn
  - Not much progress
    - Desire `do we want AI has its own desire?`
    - Taste & Smell `it's hardware thing, very hard`

  - In progress to match human
    - Mobility `hard to achieve, Boston Dynamics`
        - Touch `hard`
        - Proprioception `body position`
        - Body Language Expression `latency problem`
        - Stamina `easy, just different energy source`
    - Understanding `AI already does; But we don't even know how brain makes conclusion, how we jude AIs' conclusions? Is it computation or storage?`
      - AIs self conclusion
      - human conclusion
      - physical world conclusion `will soon better than human`
      - visual understanding `But not understand yet; One day a AI watch all Youtube Videos will smarter than any human`

  - Better than human `AI has hardware advantage over human`
    - Visual Perception
        - Body Language Perception
        - Surrounding Awareness `Tesla already achieved`
    - Listen & Speak
    - Read/Write
- Biology System AIs doesn't need
  - Digest System
  - Circulation System
  - Nociception `pain`


> > IMO: most important in AI is right question `aka desire` & measurement of progress `aka value`.

> We are environment feedback; AI is same; AI can easily traversal through digital world; But in physical world, AI will just be like us, only experience subset of reality. AI most likely will experience more than any single human, but AI still limited by its experience ability.
> > Most important thing is feedback system.
>
> People lives in a house; Sames for AI, AI lives on hardware; Some AI can squeeze in small PC, of course can't do as much.


## Datastore
> high-dimensional vector search; Similar to pandas specialized libraries for data process;

- pinecone
- milvus
- qdrant
- redis
- weaviate
- zilliz

## Plugin

PluginFlask server
- /upsert `convert info into openapi format; Then convert text to openapi text-embedding-ada-002; Last store in Datastore format(pinecone) in our DB`
- /query `convert query_str into openapi embedding; Then use Datastore find top related records; Then return to ChatGPT`


Zero-shot learning: In zero-shot learning, a model is trained to recognize objects or classes that it has never seen before. This is done by providing the model with some prior knowledge about the classes, such as their attributes or relationships to other classes. The model can then use this knowledge to make predictions about new classes without any specific training data for those classes.

One-shot learning: In one-shot learning, a model is trained to recognize objects or classes based on a single example of each class. This is typically achieved using techniques such as metric learning or siamese networks, which learn to compare and contrast different examples to identify similarities and differences between classes.

Few-shot learning: In few-shot learning, a model is trained to recognize objects or classes based on a small number of examples of each class. This typically involves training the model on a small subset of the available training data, and then fine-tuning the model on new examples as they become available.


LLM is similar to foreigner that can see & draw picture with 1409 points;

We translate 4096 words/tokens to a LLM picture(1049 points), then let LLM draw a response picture(1049 points), then translate back.

Different LLM draw different points(embedding similar to language);

ChatGPT don't READ or WRITE word or paragraph;

only after 15+ interaction, summary memory will reduce token length.

AI sucks at Abbreviation. 

- Chain: predetermine workflow
- Agent: undetermined workflow

Once major differences is NN can do backward propagation. But neuron synapse only fire single direction.

what is some top news happens in recent months? to check when AI model trained at