# Qwen 3-Next 80B Instruct (NIM) — customer_support/multi_issue_conversation

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 6.67 | quality: 5.77
- latency_total: 2.386s | tokens_per_second: 44.4
- input_tokens: 608 | output_tokens: 106
- judge_score: 3.2 | justificación: 

## Respuesta completa

[tool_call] lookup_order({"order_id": "ORD-7788"})
[tool_call] lookup_order({"order_id": "ORD-7790"})
[tool_call] create_ticket({"category": "technical", "priority": "high", "summary": "La app se cierra sola al intentar ver pedidos en iPhone", "customer_email": "usuario@example.com"})