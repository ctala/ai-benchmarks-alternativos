# Ministral 14B — customer_support/multi_issue_conversation

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 8.98 | quality: 9.4
- latency_total: 2.52s | tokens_per_second: 92.5
- input_tokens: 527 | output_tokens: 233
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, abordando cada problema con acciones específicas, incluyendo la creación de tickets y el procesamiento de un reembolso, lo que la hace altamente útil para un emprendedor.

## Respuesta completa

[tool_call] lookup_order({"order_id": "ORD-7788"})
[tool_call] lookup_order({"order_id": "ORD-7790"})
[tool_call] create_ticket({"category": "shipping", "priority": "high", "summary": "El pedido ORD-7788 no ha llegado en los 3 días esperados"})
[tool_call] create_ticket({"category": "billing", "priority": "urgent", "summary": "Cobro doble por el pedido ORD-7790 ($45 cada cargo)", "customer_email": "cliente@example.com"})
[tool_call] create_ticket({"category": "technical", "priority": "medium", "summary": "La app se cierra al intentar ver los pedidos en iPhone"})
[tool_call] create_ticket({"category": "shipping", "priority": "low", "summary": "Consulta sobre disponibilidad de envío express para próximo pedido"})
[tool_call] process_refund({"order_id": "ORD-7790", "amount": 45, "reason": "Cobro doble por error"})