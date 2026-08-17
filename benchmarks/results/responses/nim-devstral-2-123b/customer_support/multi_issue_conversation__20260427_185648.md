# Devstral 2 123B (NIM) — customer_support/multi_issue_conversation

- model_id: `mistralai/devstral-2-123b-instruct-2512`
- success: True  | final: 6.98 | quality: 6.66
- latency_total: 2.459s | tokens_per_second: 39.8
- input_tokens: 527 | output_tokens: 98
- judge_score: 3.8 | justificación: 

## Respuesta completa

[tool_call] lookup_order({"order_id": "ORD-7788"})
[tool_call] lookup_order({"order_id": "ORD-7790"})
[tool_call] create_ticket({"category": "technical", "priority": "high", "summary": "App se cierra sola al ver pedidos en iPhone"})
[tool_call] create_ticket({"category": "shipping", "priority": "urgent", "summary": "Envio express para proximo pedido"})