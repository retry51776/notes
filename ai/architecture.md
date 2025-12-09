# Architecture
>
> AI Architecture notes, from old to newer. Fork off academic.md

## MLP

Adv:

- memorization capacity

Con:

- compute intensive
- Fixed function, can't dynamic adjust according length of input

## CNN

Assumptions:

- Locality `make NN prefer texture over outline`
- Location Invariance
- Hierarchical Structure

## Transformer

<https://poloclub.github.io/transformer-explainer/>

- x `input tokens`
- len(x) `input length`
- Q `Q = x * Wq, positional specific`
- K `K = x * Wk, position agnostic`
- V `V = x * Wv, position agnostic; each token possible meanings(need filter by contextual score)`
- H `Number of attention heads`
- d_head `often 128, len(x) * d_head`
- d_model = `d_head * H` is residual stream size.
- $ QK^T $ `d_model * len(x), contextual score`

ROPE:

Rely on:

- Relative Position matters more than Absolute Position
- factorization is grounded in the geometry of rotation able to preserves relative position
- Any N Dimension Rotation can Broken Down into N numbers 1D Rotations; at the cost of collision (ambiguity)

RoPE can be viewed as wrapping each embedding vector around a set of circular phases.
 • The token position moves the rotation forward linearly (one step per token).
 • The channel dimension controls the rotation speed exponentially (fast at low dims, slow at high dims).

- Rotation dimension options
  - 1D - can't rotate, only slide.
  - 2D - Euler’s formula $e^{i\theta} = \cos\theta + i\sin\theta$ is fast, efficient; but with 2 problems
    - only can apply to 2 points: Therefore we break d_model into 2 pair chunks;
    - increase dimensions of RS: We can let Q, K absorb increased dimensions;
    - easy & fast; only cos & sin & sum ops;
  - 3D+ - It's mathematical possible to rotate in 3D+(in fact advantage avoid subchannel), but we don't have those mathematical tools, and too compute intensive;

- theta - controls rotation decay at different layers of d_model
  - is unique for each pair of d_model
  - start from max(theta) = 1r ~ 57°; ends with min(theta) ~ 0; theta = 2pi ~ 6.28 = full rotation;
  - is linear scale with seq_position
  - is proportional to its pair position
  - determines amount rotation

```py
# Ex: d_model = 10; seq = 3; base = 10000;
# RS = [
#   [t1_c1, t1_c2, t1_c3 ... t1_c10], // first token w 10 d_model
#   [t2_c1, t2_c2, t2_c3 ... t2_c10],
#   [t3_c1, ................ t3_c10]
#];
#
#    = [
#   [t1_o1, t1_e1, t1_o2, t1_e2 ... t1_o5, t1_e5], // first token w 5 pairs sub_channel
#   [t2_o1, t2_e1, t2_o2, t2_e2 ... t2_o5, t2_e5], // even -> cos() - sin()
#   [t3_o1, t3_e1, t3_o2, t3_e2 ... t3_o5, t3_e5], // odd -> sin() + cos()
#]

# W_k is a column of different rotation angles freq, that will apply to different layers of d_model.
# k is the index for the pair of d_model (ranging from 0 to d/2 - 1).
# d is the total number of d_model (in the example, 10).
# 2k/d → 1, but never reach 1.
# theta_j from large(high rotation) to small; early d_model focus locally, deeper d_model focus globally
# W_k = 1/theta^(2k/d); 
# W_k = [r1, r2, ... r5]

# when theta = 10,000;
# W_k = [1, 0.158489319, 0.025118864, 0.003981072, 0.000630957] (radian unit)
#     = [57°, 9°, 1.4°, 0.23°, 0.036°] (degree unit)

# theta_j large -> rotate fast, but LLM can't distinguished already rotated full cycle.
# theta_j small -> rotate slow, but LLM can't distinguished small gap.
# Ensure coverage across many orders of magnitude. W_k = 1/theta^(2k/d); uses exponent instead linear.

# Rotated_RS = [
# [t1_c1 * 1r1, t1_c2 * 1r1, t1_c3 * 1r2, t1_c4 * 1r2, t1_c5 * 1r3, t1_c6 * 1r3, .... t1_c10 * 1r5],
# [t2_c1 * 2r1, t2_c2 * 2r1, t2_c3 * 2r2, t2_c4 * 2r2, t2_c5 * 2r3, t2_c6 * 2r3, .... t2_c10 * 2r5],
# [t3_c1 * 3r1, t3_c2 * 3r1, t3_c3 * 3r2, t3_c4 * 3r2, t3_c5 * 3r3, t3_c6 * 3r3, .... t3_c10 * 3r5],
#]

```

> t1_c1 & t1_c2 is not simply * 1r1; But for easy pattern recognition; Here are detail ops:
$\begin{cases} t'_{1,c1} = t_{1,c1} \cos(1 \cdot r1) - t_{1,c2} \sin(1 \cdot r1) \\ t'_{1,c2} = t_{1,c1} \sin(1 \cdot r1) + t_{1,c2} \cos(1 \cdot r1) \end{cases}$

$$\theta_{\text{min}} \approx \text{base}^{-1} = \frac{1}{10000} = 0.0001$$

Intuition steps:

- we converts embedding(d_model) into many **pair 2** sub_channel;
- Each sub_channel rotate proportional to its position(by theta);
  - j_theta = base^(-2j/D)
- Each token @ each channel will linear scale rotate by its unique theta

```py
x_rot_even =  x_even *cos - x_odd* sin;
x_rot_odd  =  x_even *sin + x_odd* cos;
```

Problems:

- High-frequency bands(later position j_theta has higher rotation -> higher freq) become useless after a few thousand tokens;
  - research shows ablating high frequency has less catastrophic impact

- Float precision failure: sin(10^9) and cos(10^9) cannot be computed accurately

- NTK stretches RoPE uniformly; YaRN stretches RoPE selectively(split into 2 distinct scale sections);

Ideas:

- multi-scale encoding hypothesis
- diversity in positional encoding scales within a single attention head
- Problem with Transformer is too high variance/freedom, too low bias/doesn't align with human bias.

YaRN allows RoPE to use non-integer (fractional) token positions

deepseek:

- Multi-Head Latent Attention (MLA)
  - Find common denominator matrix C for in KV matrix, so when store KV cache, store KV/C to save storage.
- Cross-Layer Attention (CLA)
- Due Pipeline - Decouple backprops into 2 components; Only run 2nd part when GPU is free
  - Calculate backprops for early layer
  - Calculate weight update

```py
model.model.layers ModuleList(
  (0-63): 64 x Qwen2DecoderLayer(
    (self_attn): Qwen2Attention(
      (q_proj): Linear(in_features=5120, out_features=5120, bias=True)
      (k_proj): Linear(in_features=5120, out_features=1024, bias=True)
      (v_proj): Linear(in_features=5120, out_features=1024, bias=True)
      (o_proj): Linear(in_features=5120, out_features=5120, bias=False)
    )
    (mlp): Qwen2MLP(
      (gate_proj): Linear(in_features=5120, out_features=27648, bias=False)
      (up_proj): Linear(in_features=5120, out_features=27648, bias=False)
      (down_proj): Linear(in_features=27648, out_features=5120, bias=False)
      (act_fn): SiLU()
    )
    (input_layernorm): Qwen2RMSNorm((5120,), eps=1e-05)
    (post_attention_layernorm): Qwen2RMSNorm((5120,), eps=1e-05)
  )
)
```

## Diffusion

> Diffusion train data by noise sample both variances(gaussian noise) & mean(drift direction toward 0/normal distribution).
>> **Drift** is known deterministic force, **variance** is random force.

Forward SDE is mathematical model diffusion process, but surprisingly there is mathematical model REVERSE SDE.

> Reverse SDE break into 2 components: **variance** assume cancel by **variance**; **Drift** is -1/2 *beta(t)* x for DDPM;

> Score Function - For any given point in the data space, it tells you the direction in which the probability density of the distribution increases the fastest.
>> Once Score-Diffusion compute diffusion score, it ues reverse SDE formula to denoise input. Then iteratively repeat until diffusion score reach threshold.

> Diffusion Model generate all tokens, then mask tokens with low logit, regenerate again.

DDMP paper by Johnathan Ho @ 2020
(Evidence Lower Bound)ELBO

- scored diffusion - `llm learn score noised sample`

## MAMBA

rely associative ops only(op order doesn't matter)

Adv:

- fixed memory size
- fast compute: Log(n)*n;

But softmax is not associative

 Not dense attention.

## Hub

Brain neuron's connection distribution is NOT normal distribution, rather power log curve(small numbers neuron acts as hub with large amount connections);

Designs:

- 1. token will attends near by tokens & few far away tokens & some random tokens
- 2. Residual Stream cross layers flow

Cluster coefficient - node's neighbor / node's neighbor directly connected %

FFN is lattice network. Local connection is good, but far away connection are bad.
Random connection network is good global connection, but bad local connection.

Small-word network is what we want.
