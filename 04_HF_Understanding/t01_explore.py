from transformers import AutoConfig

model_id = "mistralai/Ministral-3-3B-Base-2512"
# model_id = "Qwen/Qwen3-0.6B"
cfg = AutoConfig.from_pretrained(model_id)
print(cfg)
exit()
text = cfg.text_config

print("model_id", model_id)
print("model_type", cfg.model_type)
print("text_model_type", text.model_type)
print("layers", text.num_hidden_layers)
print("hidden_size", text.hidden_size)
print("num_attention_heads", text.num_attention_heads)
print("num_key_value_heads", text.num_key_value_heads)
print("head_dim", text.head_dim)
print("intermediate_size", text.intermediate_size)
print("sliding_window", text.sliding_window)
print("vocab_size", text.vocab_size)
print("tie_word_embeddings", text.tie_word_embeddings)
print("max_position_embeddings", text.max_position_embeddings)
