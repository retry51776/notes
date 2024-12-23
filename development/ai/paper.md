# Paper
"Explaining and Harnessing Adversarial Examples" by Ian Goodfellow, et al. (2014): This paper introduces the concept of "adversarial examples," which are inputs to machine learning models that have been specifically designed to cause the model to make mistakes. The paper has had a significant impact on the field of adversarial machine learning, and it has spurred the development of many techniques for defending against adversarial examples.

"Human-level performance in multi-task reinforcement learning" by Volodymyr Mnih, et al. (2015): This paper presents the "DQN" algorithm, which was able to achieve human-level performance on a suite of Atari 2600 games using reinforcement learning. This was a significant achievement in the field of reinforcement learning, and it laid the foundation for many subsequent advances in the area.

"Attention Is All You Need" by Vaswani, et al. (2017): This paper introduces the "Transformer" model, which is a type of neural network that is particularly well-suited for natural language processing tasks. The Transformer model has had a significant impact on the field of NLP, and it has been used in a variety of applications, including machine translation and language modeling.
> Position encoding is similar how external ear changes noise a little for brain detecte position.
> GPT4 has 220 billions parameters; 16 way mixture model; 8 set of weights;

"Scaling Laws for Neural Language Models"

Filter query step:
The idea is embedding layer encoded w position info. Then train attention matrix(n^2) to capture relationship weights; Then attention matrix times embedding layer to get filtered input.

"DeepMind and Blizzard Entertainment are working to build the definitive version of Starcraft II for AI research" by David Silver, et al. (2017): This paper describes the collaboration between DeepMind and Blizzard Entertainment to create a version of the Starcraft II video game that is optimized for use in AI research. The game has since become a popular benchmark for AI algorithms, and it has been used in a number of research papers and competitions.

"GPT-3: Language Models are Few-Shot Learners" by Alec Radford, et al. (2021): This paper introduces the "GPT-3" language model, which is one of the largest and most powerful language models to date. GPT-3 has been able to achieve state-of-the-art results on a variety of NLP tasks, and it has been used in a number of interesting applications, including machine translation, text summarization, and question answering.

- The Lottery Ticket Hypothesis `reuses pruned large network's connection & weights; iterator pruning; some network only need 3% weights same performance.`

> Deconstructing Lottery Tickets: magitude_increase is best, large final is easy & pretty good. 

- Dynamic Routing Between Capsules `Capsule Networks`

- TransformerFAM: Feedback attention is working memory

- Attention with Linear Biases (ALiBi) `ALiBi addresses this problem by adding a linear bias to the attention scores between each query and key. The bias is inversely proportional to the distance between the query and key, so that closer tokens have a higher attention weight than more distant tokens. This helps to ensure that the model focuses on the most relevant tokens, even when the sequence is very long.`

- Flash Attention achieves its speed and memory efficiency by using a number of techniques, including:

Tiling: The attention computation is divided into smaller tiles, which are computed in parallel.
Sparse matrix multiplication: The attention scores are computed using sparse matrix multiplication, which is more efficient than dense matrix multiplication.
IO-awareness: The attention computation is carefully designed to minimize the number of memory reads and writes.

- Retrieval Enhanced Transformers (RETRO) are a type of language model that combines the strengths of both retrieval-based and generative models. RETRO models first retrieve a set of relevant documents from a large corpus, and then use a generative model to generate text that is consistent with the retrieved documents.

- SynFlow prune network connection by assign score to each connection. score = dervitity_lose / dervitity_weight * weight; Because we want to prune connection auto balance between layers(I am not 100% agrees here.)

- Quantized is normalized weight & activation input & output. But outlier weight is problem. maybe need split out outlier process.


# Ideas
- pick radom top weight neurons, take input from (important & far away) neuron's output; repeat winning lottery?
- prune combines with quantized? or can we quantized only subset network?



> The age of pre-training is over.