# Llama 4 Scout 17B (Groq preview) — customer_support/multi_issue_conversation

- model_id: `meta-llama/llama-4-scout-17b-16e-instruct`
- success: True  | final: 7.61 | quality: 7.6
- latency_total: 1.281s | tokens_per_second: 212.4
- input_tokens: 1036 | output_tokens: 272
- judge_score: 4.2 | justificación: 

## Respuesta completa

[tool_call] lookup_order({"order_id":"ORD-7788"})
[tool_call] lookup_order({"order_id":"ORD-7790"})
[tool_call] process_refund({"amount":45,"order_id":"ORD-7790","reason":"cobro doble"})
[tool_call] create_ticket({"category":"shipping","customer_email":"","priority":"urgent","summary":"Pedido ORD-7788 no ha llegado"})
[tool_call] create_ticket({"category":"billing","customer_email":"","priority":"high","summary":"App se cierra sola al ver pedidos en iPhone"})
[tool_call] create_ticket({"category":"other","customer_email":"","priority":"low","summary":"Envio express para proximo pedido"})