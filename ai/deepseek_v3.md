# DeepseekV3ForCausalLM

<https://huggingface.co/deepseek-ai/DeepSeek-V3-0324/blob/main/modeling_deepseek.py>

> This architecture implementation in python published by Deepseek. It can either come from the open source community or from the Model Publisher.

Original LLM head (for generation)

`lm_head = nn.Linear(hidden_size, vocab_size)`

Convert the last hidden state to logits via lm_head

- `model.generate()` <https://github.com/huggingface/transformers/blob/0ef339ff1b63bb03a388c79bfbebec9085e10564/src/transformers/generation/utils.py#L2105>
- `while self._has_unfinished_sequences:`
  - `self..forward()`

> nn.Module/self() is equivalent to calling self.forward()

## DeepseekV3ForSequenceClassification

Classification head (for sentiment/toxicity/etc.)

`classifier_head = nn.Linear(hidden_size, num_labels)`

> Need manual retrain with custom labels & data

## DeepseekV3Config

## DeepseekV3MoE

MoEGate & experts

## MoEGate

Every TOKEN from Attention_Head_Out will route to its own FFN expert.

Divide experts into groups (e.g., 8 groups of 256 experts).

First, select the top-𝑘 groups (e.g., top-1 group/32 experts) per token.

Then, choose the top-𝑘(top 8 experts from of 32 experts group) experts only within those groups.

- Device Balance vs Expert Balance - one expert group ~ one device, find group with highest top-k match overall, prevent route request to experts in many devices.

> V3 expert load balance is NOT Real-Time Tracking from previous token experts.

## Expert (DeepseekV3MLP)

MLP with 2 nn layers

    - self.act_fn(self.gate_proj(x)) * self.up_proj(x)
    - self.down_proj(first_layer_output)

Each expert assigns to a GPU by `ep_rank` aka GPU group;
Each expert are MLP with 2048

# DeepseekV3Attention

- past_key_value `kv_cache`

# DeepseekV3FlashAttention2

## OpenAI OSS

<https://github.com/huggingface/transformers/blob/main/src/transformers/models/gpt_oss/modeling_gpt_oss.py>
