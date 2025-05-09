# IMO
>
> Collection of my thoughts & guess. No evident needs, just a crazy person's notes here.
>
> Break my opinions into:

- strong opinions
- weak opinions `require many conditions to be true`
- random ideas
- crazy notes
- industrial opinion

## Strong Opinions
>
> I don't beveled human brain is the only way to achieve intelligent. Many ppl still consider llm just auto complete, just evident by llm failed simple human task. But that assumes intelligent must follow human path.

> Verifiable is most important, both AI training, & life in general. Ex: development coding style, KPI
>> The fact that LLM still programming in higher languages only because human verification.

> IMO: most important in AI is right question `aka desire` & measurement of progress `aka value`.

> My opinion of neural network is a lossy compression model.

> Every human ability requires a decoder from context token? So hands movement needs hand decoder, speak needs speech decoder, running need leg decoder?

> NN connection is too static. Human neurons can create new connection. Need dynamic connection ability in NN.

- AI is similar to Chemistry/Physical in 1800. There's some set logic/mechanism(usable metal); We play around data(Iron Ore) with some computation process(refine ore). Maybe the remaining data AKA model(Iron/steel) is what we desire. So value of the data is NOT determent by amount, but the data contains logic/mechanism we desires.
  - Mining & Extraction = Data Collection & Scraping
  - Computation = Heat
  - Data Center = Blast Furnace
  - Data = Iron Ore
  - Model = Iron
  - Fine-Tuning (Specialized Model Training) = Alloying (Adding Carbon to Make Steel)
  - Inference & Deployment = Rolling & Shaping Steel
  - AI Evaluation (Benchmarks, Alignment, RLHF) = Quality Testing & Hardening
  - AI Applications = Bridges, Cars, Tools
  - Smart AI answer's is info density = Purity Iron weight more `Same As Human`

  - Text data -> logic
  - ?? -> physical mechanism
  - DNA -> biology mechanism
  - social data -> human society mechanism?

- I think we need more localized, more parallel algorithms. I think back propagation is too global. My guess is unfired neuron stack up voltage cause correction.

- Most likely llm's problem is there is a single intermediate state that holds though, planning, intentions, understanding,

- Seems like building AGI requires many "components/skills", we need AI able to count, 2D understanding, 3D understanding, read, listen, speak, write ....etc. Just achieved one doesn't mean others are so easily done. We need to look deep into ourself what are fundamental skills we have.

- Healthy people are more flexible movement; Won't trick by trick questions; A key measurement for AI should be same thing, how hard to trick AI.

- AI can think of compression algorithm. In fact it may be too good. A lot knowledge able to compress into 20GB model. Maybe the problem is we COMPRESS too much! That's why bigger model shows better intelligence.

> Quantization indicate LLM understand by relativity comparison; Aka we understand by contrast, not absolute value.

> Why AI need so much computation? Interesting to compare traditional Lossy Compression Algorithms which uses very few computation.
>> Compression Algorithms start from data to away from data, AI start from randomness to target. Perception Coding

> We are environment feedback; AI is same; AI can easily traversal through digital world; But in physical world, AI will just be like us, only experience subset of reality. AI most likely will experience more than any single human, but AI still limited by its experience ability.
> > Most important thing is feedback system.
>
> People lives in a house; Sames for AI, AI lives on hardware; Some AI can squeeze in small PC, of course can't do as much.

> Not only in Training there is a lot redundancy computation, also during inference phrase.
>> Maybe runtime compute will be faster if we store key layer's state, & forward to next compute cycle. Ex: if there are 2 opinion words/route with similar probability, compute both, or if rejected first opinion by user, use next one.

**OPENAI**

> OpenAI can be think of "University for AI"; How OpenAI measure/test AI, what course they teach/train AI, how OpenAI get feedback from AI?
>
> It's NOT graduated student from University makes University valuable. It's graduated student proven University's education process.
>
> Diff: OPENAI can design student. I don't know if AI design matter a lot or little.

> My guess OpenAI train AI with more output layers; More output layers force AI to have deeper understanding.

> efficiency & flexibility trade off are fundamental. In AI, in memory compute are fast but not flexible. GPU & CPU are more flexible, but slower.
>> Also there are indicator in human too. 3 year old we have most neurons, can learn anything. Yet as we get older, we process fast, yet not able to learn/adapt. We have less neurons, bigger neurons.
>> We should research how brain neuron replace  surrounding neurons, that give us clubs to have same size LLM but smarter/faster(in  expense of flexibility because we break matrix size).

> Right now LLM still small that most new models are train from scratch. But at some point model will be so big that training from scratch is too expensive. At that point(EX: deepseek v3 -> R1), we will see similar to evolution methods to improve models.

> RNN = (hidden_state * reflection + read_component + output_component)
>> (transformer - softmax) = (RNN - reflection) = Linear Attention
>
>> key `which part of memory(hidden_state) to write`
>> value `what to store in memory(hidden_state)`
>> query `what to read from memory`

> Brain neurons doesn't do multiplication, seems like brain proves only addition should enough. My intuition seems like softmax layers & multiplication layers counter each other.

## Weak Opinions
>
> Another cue is human train to response faster, rational thinking is slower. Seem like AI just have "instinct" right now.

> Language Model is statical model of large text db. AI usually very agreeable/static basie.

> True Negative is SO HARD for LLM. True Positive is very easy.

> We need to increase embedding token size, width of network, not the deep of network.

> Attention has fundamental bottleneck(maybe no work around): when one token relationship has high attention score, other relationships ALWAYS reduces attentions. (Maybe build many to many relationship matrix to support complex relationship attention?)

### Analogy

- Weights = binary of programs.
- Activation = memory/state of programs.
- Neuron = assembly instructions.
- Architecture = VM/compiler/Runtime of program.

> Think of AI as a kid, we are designing games to see which game `architecture` help AI `kid` grow;

> LLM is similar to foreigner that can see & draw picture with 1409 points;

## Crazy notes
>
> Best way measure understanding(both human & AI) is operation/alteration after compression.

- pick radom top weight neurons, take input from (important & far away) neuron's output; repeat winning lottery?
- prune combines with quantized? or can we quantized only subset network? Proven Idea now! haha

- distilled LLM is similar how pet display intelligent response yet not fully understand the reasoning

- It's very interesting that LLM & Human has internal mechanism to be lazy(stop work early). That needs multiple agent/llm, or some kind prompt injection to force (human & llm) to finish the task. All llm api should have parameter to control llm stop work's probability.

> We need a multi model AI that can generate text/speech/diagram for documentation.
>> Or is text a fundamental unit to derivate speech & diagram?
 • If speed & efficiency → Text wins.
 • If long-form engagement → Audio is easier to consume.
 • If complex ideas → Diagrams & multimedia work best.

> Assume answer = step_n(step_2(step_1(prompt))); Often time LLM output the wrong answer because answer_1 = step_1(prompt) is decoded too late.  Ex: NN has 100 layers, answer_1 if decoded before layer_10, then final_answer is correct, but if answer_1 was decoded after layer_20, then most likely final_answer will be wrong.
>> <https://arxiv.org/abs/2406.12775>

> We really need to look deep into Query, Key, Value system in transformer. And look into how human brain works in similar way according book Atomic Habit(Cue"Query" -> craving"Past Key?" -> reward"Future Key?" -> action"Value")

> Human Brain seems stores selected experiences(filtered input), but most thoughts at the process/event(output of LLM) aren't store. Brain seems like stores feelings(internal hidden state).

> Soon we will need SEO but for LLM. The content needs to be format that easier to convince LLM.

> LLM external knowledge vs internal knowledge is important topic. Also conclusion will be very useful on people too.
>> There are research shows LLM seems beveled more on LLM's text than human text.

> Maybe transformer just predict the next token has leakage. During batching training, llm will have foresee result before it suppose to. Ex: 2 + 3 = 5; 4 + 7 = 11; in 7th batch(2 + 3 = 5; 4) as input, llm learned 2 + 3 = 5; Maybe info leakage here?

## Physical Intelligent

> What are components/abilities of physical intelligence?

- Object Movement Prediction
- Vision -> Internal World Modeling
- Animals Behavior Prediction
- Audio -> Object Detection & Location Tracking
- Movement Control
- Balance & Gravity Center
- Classify Object
  - Size
  - Shape
  - Volume
  - Mass distribution
  - Strength/Texture
  - Reflectivity/Transparency
  - Wetness/Dryness
  - Material
  - Hardness/Softness
  - Temperature
  - Fragility
  - Stiffness
  - Chemical Properties

> Break into 4 types

- Classic `Great Improvement`
- New Research `Not proven`
- Tech Improve `Small improvement`

### Classic

- "Scaling Laws for Neural Language Models" by OpenAI

- "Toy Models of Superposition” by Anthropic (2022)

- "Explaining and Harnessing Adversarial Examples" by Ian Goodfellow, et al. (2014)

- "Human-level performance in multi-task reinforcement learning" by Volodymyr Mnih, et al. (2015)

- "Attention Is All You Need" by Vaswani, et al. (2017):
  > This paper did NOT invent attention, rather it said only attention mechanism is what matters.
  > Position encoding is similar how external ear changes noise a little for brain detect position.
  > Position encoding solve the Transpose bias  problem in attention head, where x*y = y*x;
  > GPT4 has 220 billions parameters; 16 way mixture model; 8 set of weights;

  > Filter query step:
  The idea is embedding layer encoded w position info. Then train attention matrix(n^2) to capture relationship weights; Then attention matrix times embedding layer to get filtered input.

- "The Lottery Ticket Hypothesis" `reuses pruned large network's connection & weights; iterator pruning; some network only need 3% weights same performance.`

  > Deconstructing Lottery Tickets: magitude_increase is best, large final is easy & pretty good.

- The Dark Matter of Neural Networks `By Chris Olah; explore NN features.`

- [Deepseek V3 Tech Report]<https://arxiv.org/pdf/2412.19437>
  - Multi-Head Latent Attention (MLA) `Combine token_d's key & value of Attention into c*d(c is < 1) single embedding; Aka 2d -> 0.7d; c*d concatenated(NOT Add) RoPE -> Attention Head`
  - 8/32 MOE auxiliary-loss-free strategy `Load balance without loss`
  - Multi-Token Prediction (MTP) `Use next_token_prediction (expect_token) + next_token(reality_token) to predict new_token`

- Distilling the Knowledge in a Neural Network
  - Hard Label(Human label) doesn't capture reality, Soft Label(LLM statical probability) capture more detail/relationship of reality.
  - Label Smoothing have another model learn from Soft Label instead Hard Label.
  - 64 experts

- On the Biology of a Large Language Model <https://transformer-circuits.pub/2025/attribution-graphs/biology.html> `LLM works by givens context to each world, in here context includes relevant info & logic`

### Tech Improve

- KV Cache `Query(latest token) change every token, but Key(past sentences) & Value(of past sentences' meaning) are static`

- "GPT-3: Language Models are Few-Shot Learners" by Alec Radford, et al. (2021)

- Tree of Through

- Anthropic’s “Scaling Monosemanticity”

- “Position Interpolation for Extending Context Window in Transformers” by OpenAI (2023)

> instead of using positions [1, 2, 3, 4, 5, 6, 7, 8, 9 … L] where L is the pre-trained sequence length, we use [1, 1, 1, 1, 2, 2, 2, 2,… L, L, L, L]

- <https://omnihuman-lab.github.io/>

### New Research

- Leave no Context behind. `Google extend context`

- Just forward passes

- Dynamic Routing Between Capsules `Capsule Networks`

- TransformerFAM: Feedback attention is working memory

- Attention with Linear Biases (ALiBi) `ALiBi addresses this problem by adding a linear bias to the attention scores between each query and key. The bias is inversely proportional to the distance between the query and key, so that closer tokens have a higher attention weight than more distant tokens. This helps to ensure that the model focuses on the most relevant tokens, even when the sequence is very long.`

- Flash Attention achieves its speed and memory efficiency by using a number of techniques, including:

  > Tiling: The attention computation is divided into smaller tiles, which are computed in parallel.
  Sparse matrix multiplication: The attention scores are computed using sparse matrix multiplication, which is more efficient than dense matrix multiplication.
  IO-awareness: The attention computation is carefully designed to minimize the number of memory reads and writes.

- Retrieval Enhanced Transformers (RETRO) are a type of language model that combines the strengths of both retrieval-based and generative models. RETRO models first retrieve a set of relevant documents from a large corpus, and then use a generative model to generate text that is consistent with the retrieved documents.

- SynFlow prune network connection by assign score to each connection. score = dervitity_lose / dervitity_weight * weight; Because we want to prune connection auto balance between layers(I am not 100% agrees here.)

- Quantized is normalized weight & activation input & output. But outlier weight is problem. maybe need split out outlier process.

- generative agents interactive simulacra of human behavior `Agent with remember, plan, react, and reflect interact with other agents with some environment`

## OpenAI Opinion

> The age of pre-training is over.

Open AI Imagines AGI in 5 phrases:

- Conversation LLM
- Reasoning and Planning
- Agent able analysis & take actions
- Innovation
- Organization

Reinforcement Learning for "Open AI Strawberry" components

1. Policy Initialization
2. Reward Design
3. Search
4. Learning

- Goal qualification
  - Outcome Reward Maximization (ORM) `reward by final outcome`
  - Process Reward Maximization (PRM) `reward per step, good for Math, coding`
- Task Decomposition
- Alternative proposal
- Solution generation `llm bad at`
  - Best of n sample | Beam Search | Monte Carlo Tree Search | Sequential Revision
  - self evaluation `llm good at`
  - Solution Level Search, Step Level Search, Token Level Search
- self correction

Training more likely Beam Search, inference more likely Sequential Revision

- Scaling of Search and Learning: A Roadmap to Reproduce o1 from Reinforcement Learning Perspective

> <https://docs.neuronpedia.org/> inspect llm neuron meaning.
