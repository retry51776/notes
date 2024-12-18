# AI
> My opinion of neural network is a lossy compression model.

> Best way measure understanding(both human & AI) is operation/alteration after compression.

## CICD
- Modeling
- Deployment
- Versioning
- Orchestration
- Compute
- Data

## Workflow
- 1. What are we modeling?
  - Study human? or Study physic? Ex: color is only human biology, in reality just wave freq.
- 2. Curate Data
  - The biggest bottleneck; Both human & robot data collection limited by reality.
- 3. Design AI Architecture
  - Dark magic? Ask AI expert
  - Symmetry within model (Ex: time, left vs right, position,)
  - Kind like structure engineer
- 4. Craft Loss Function
  - Relates to #1, from which perspective?
  - Physic law can embed within lost function to ensure Model learn physic law.
- 5. Optimization
  - This solution may be another AI itself?

- Identify object
- Assign object properties
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
- Auto Model Compression `pruning as reinforcement learning problem`
- Physics Informed Machine Learning

## Architecture
> Think of AI as a kid, we are designing games to see which game `architecture` help AI `kid` grow;

- Stable diffusion: add noise to image, let AI recover image;

- Language Model is statical model of large text db. AI usually very agreeable/static basie.

- Sparse Auto Encoders
> Brain uses Sparse Repr, it save energy, resilient to noise

### Sparse Modeling
> The goal is reduce input dimensional space to reduce noise.
> The lose function of Sparse Modeling has extra Regularization to encourage sparsity in the network

x = D * α
- x `input signal`
- Dictionary (D) `n(input size) by k matrix; Think as collection of basic feature sets;`
- n `flatten input(x) size; also dictionary's width`
- k `dictionary's columns, usually bigger n`
- α `multi hot encoding vector;`
- l0 `norm is counting the non-zero in α`
- atom `a column from dictionary; think as a basic feature set;`
> input = collection of atoms from Dictionary 

> The goal is find a dictionary where each data will repr by a few atoms from dictionary.

Relaxation (Basic Pursuit)
Go Greedy (Matching Pursuit)

Predefined dictionary: steerable, wavelet, curvelet, contourlets, bandlets.

Sparse Identification of NoneLinear Dynamics(SINDy) converts time-series data to sparse model

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
- https://app.suno.ai/ `music ai`


## OPENAI
> OpenAI can be think of "University for AI"; How OpenAI measure/test AI, what course they teach/train AI, how OpenAI get feedback from AI?
>
> It's NOT graduated student from University makes University valuable. It's graduated student proven University's education process.
>
> Diff: OPENAI can design student. I don't know if AI design matter a lot or little.

> My guess OpenAI train AI with more output layers; More output layers force AI to have deeper understanding.
- Virtual World Output
  - Language Output
    - Token => Token
    - Speech Output(Converted from text)
  - Image Output
    - Recover corruption
  - Video
    - frames => Caption
    - frame + caption => next frame
  - Game
    - Game Movement Output
    - Game Controller Output
  - Abstract Count
    - Subject Count
    - Subject Grouping
- Robot Output
  - Sound(Ex: Music, talk w motional)
  - Facial Expression
  - Movement(Ex: from point A to point B)
  - Action(Ex: Pick up Apple)
  - Object manipulation
  - Social Awareness
  - Social manipulation

## IMO
- I think we need more localized, more parallel algorithms. I think back propagation is too global. My guess is unfired neuron stack up voltage cause correction.

- Healthy people are more flexible movement; Won't trick by trick questions; A key measurement for AI should be same thing, how hard to trick AI. 

- AI can think of compression algorithm. In fact it may be too good. A lot knowledge able to compress into 20GB model. Maybe the problem is we COMPRESS too much! That's why bigger model shows better intelligence.

> Why AI need so much computation? Interesting to compare traditional Lossy Compression Algorithms which uses very few computation.
>> Compression Algorithms start from data to away from data, AI start from randomness to target. Perception Coding

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

# Tech
- Tiling `calculation by smaller block, uses scaler to rescale each row to combine whole`
- Recomputation `Don't store, recompute to save RAM`

- compute is NOT the bottleneck, rather is Memory size.

- Mixture of Expert(MOE) `combine smaller models`
- Multi Query Attention `reduce attention head to output to increase speed

- L1 regularization `L1 regularization penalizes the sum of the absolute values of the weights in the network. This encourages the network to use a smaller number of weights, and it can also help to prevent over fitting.`
- L2 regularization `L2 regularization penalizes the sum of the squares of the weights in the network. This also encourages the network to use a smaller number of weights, and it can also help to improve the generalization performance of the network.`

- Parameter Efficient Fine Tuning(PEFT)
- LoRa `Attach extra weight to original model feed forward layer, then train these extra weight; usually mb size`
- Prefix Tuning
- P tuning
- Prompt Tuning

- https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard