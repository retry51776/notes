# Training

## Pretrain

## Supervise Finetune Training(SFT)

> SFT can't scale, generate the whole distribution is too expensive. Also too hard to judge/score SFT solution.

Existed human generated data often without human's COT, but SFT is more stable than RL.

Most labs uses **seed prompts** generate **synthetic reasoning traces**. Often acts as warn up checkpoint before RL.

RL signal to noise ratio is higher than SFT. SFT dense but poorly credit-assigned signal. vs RL often has sparse, higher-variance supervision, more aligned with the objective!

SFT success does not imply every step was good.


## Reinforcement Learning

> Think of it as outer loop of learning.

> @ 2026 industrial direction is scale RL to be generalize.

> The limitation of supervise learning is teacher HAS answer, and student will NEVER out smart teacher, teacher requires build large teaching exercise.

> The limitation of RL is reward sparsity, which it's why important to have small achievable goal.

> RL requires baseline policy already has SOME success rate. This only works on medium difficulty problems.

> RL is mostly close source, with many diverse approaches.
>> Often SFT warn up, then small LORA check effectiveness, then continues RL.

> RL need diverse data, (mixed public RL dataset, average again with original weights, increase reward functions) avoid forgetting.

> Update gradient should consider = success - baseline

https://github.com/NVIDIA-NeMo/RL

Good LLM RL practices:

- LLM self aware its known & unknown
- LLM self aware its context window. (Context Anxiety)
- Learn HF preference
- LLM self aware compute & RAM usage
- introspective awareness: LLM should self aware injected thoughts(by path activation).

- Solve/Predict/Explain/Counter/Coherence/Confidence

RL Types:

- Preference RL
- RL from AI Feedback (cheap)
- Process-based RL
- Outcome RL with Verifiers (scalable)
- Self-Play / Debate / Multi-Agent RL (improve reasoning)
- Online RL with Real Usage
- R-Zero as a "Generative Adversarial Network (GAN) for Reasoning"

RL frameworks:
- areal
- Magistral
- streamrl
- asyncflow

Keys:
- high-throughput verification
- stable policy updates
- efficient sampling

Thinking should be categorical, not effector base.
Ex: argentic think - progress; Reasoning think - static-monologue thinking;

- off-policy problem - Policy drifted away from behavior policy.
- reward model
  - score's absolute scale doesn’t matter, relative differences matter
- policy
- environment
- LLM judge
  - partial credit
  - reward hacking detection
- goal instruction -> LLM generated artifacts -> grader(python logic includes `parser -> validator -> executor`) -> update LLM -> repeat.

### Recursive Self Improvement
Optimization within a fixed search space vs RSI modifying the search space/search procedure itself.


### Agentic Thinking

Just like interview person, we not only need smart guy, but resilient, consistent, planning, agency.

DIFFER(Agentic vs Reasoning) Traits:

- Deciding when to stop thinking and take an action. (Ex: Musk test to fail)
- Choosing tool & order
- ignore failed path, revising plans
- maintain coherence
- action consistent with planning

Harness:

- tool servers
- browsers
- terminals
- search engines
- simulators
- execution sandboxes
- api layers
- persistent memory system
- orchestration framework

- Environment-building

**PPO components**:

> reinforcement learning human feedback with Proximal Policy Optimization(PPO), just promote subset response probability over undesired responses.

> Collect set of complete responses, each token calculate its advantage estimate(from reward_model) & baseline_value(from ref_model)

- police_model/SFT model/rollout - AI that takes input & generate output action.
- ref_model - Frozen SFT model, uses to calculate lose by compare new action vs old action
- reward_model - LLM with LORA(attach head) trained with ranking loss.
  - Learn from human how to rate LLM output
- value_function - How much value does solution sub step worth
- policy gradient
  - Kullback‑Leibler divergence (KL) - measure difference between 2 distributions `normalize by log(observation^(1/n))`;
    - KL = Cross Entropy - Entropy
  - advantage estimate = total_discount_reward - baseline_value
    - total discounted reward $G_t$ is from time step t; `aka future reward needs discount rate`
      - discount factory - how much future reward needs to discount
    - baseline value = ref_model

**GRPO**

> Group Relative Policy Optimization(GRPO) from deepseek
>> Replace ref_model to calculate baseline with generic baseline(per question, excludes answer);
>> Replace per step reward with final reward.

**Direct Preference Optimization**


### Self Distillation

Combine LLM rollout({prompt}{solution}{runtime_result}), correct_solution, unsuccessful_feedback, prompt_again. Ask teacher LLM resolve question given previous failure. Use in-context learning with RL.

Then calculate KL loss between teacher's answer vs student's answer.

- **Latent consistency** is NOT enough for distillation. Network has some build-in circuit that also enforce causation.
  - Trajectory level `broadcasts that same scalar across tokens.`
  - Token level `raise or lower the probability of this chosen token, ignore other candidate tokens.`
  - Logit level - KL/JSD `reshape the full distribution to match the teacher’s beliefs`
  - ?? expert level ??
- causal circuit distillation

policy-side package:

- actor/trainer = the trainer who calculate loss & updates policy
  - reprompted richer context + the same old response.
  - teacher's reprompt NOT generate new response; rather run prefill generate old response logits, find out how much teacher DISLIKE old response when given right answer; The assumption/reason is right answer will generate strong deterrent force on wrong tokens.
    - This IS same phenomenon when senior developer HATES read his older code!! Those mistakes he noticed generate strong dislike.
- rollout/policy = the generation/sampling side used to collect
  trajectories
- ref = a frozen/reference policy used for KL-style regularization
  or SDPO paths
- model = shared model config for those components

algorithm handles the RL math and training-rule side, not the policy model itself. No need train critic module like PPO.

  In this repo, algorithm is the top-level config for things like:

  - reward shaping / KL-in-reward
  - advantage estimation method
  - discounting and GAE parameters
  - off-policy rollout correction
  - a few PPO-variant switches like PF-PPO

```py
# compute advantages
batch = critic.compute_values(batch)
batch = reference.compute_log_prob(batch)
batch = reward.compute_reward(batch)
batch = compute_advantages(batch)
```

- Flex-KD


### R-zero

> Assume logical truth is more self-consistent than random errors. But some tasks naturally has diverse answers, we exclude them by set Challenger uncertainty score preference.

- uncertainty score ~ answer's consistency.
- Challenger max reward when its generate question is 50% uncertainty score.
- Advantage(A) - GRPO's advantage score. `Relative Signal`