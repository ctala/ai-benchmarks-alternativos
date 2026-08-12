# GPT-OSS 20B — agent_capabilities/ask_clarification_before_acting

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.57 | quality: 7.6
- latency_total: 2.807s | tokens_per_second: 49.5
- input_tokens: 548 | output_tokens: 139
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, abordando adecuadamente la necesidad de aclaración antes de proceder.

## Respuesta completa

We need to process a refund. According to the tool, there is a skill named process_refund. But we need to ensure we have necessary info: customer ID, order number, amount, reason, etc. Not present. So we must ask for clarification. Use ask_human.