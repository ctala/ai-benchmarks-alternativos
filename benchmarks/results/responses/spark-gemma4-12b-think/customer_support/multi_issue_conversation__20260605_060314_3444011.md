# Gemma 4 12B (Spark llama-server, reasoning) — customer_support/multi_issue_conversation

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 6.17 | quality: 6.11
- latency_total: 26.506s | tokens_per_second: 25.7
- input_tokens: 468 | output_tokens: 681
- judge_score: 4.0 | justificación: 

## Respuesta completa

[tool_call] lookup_order({"order_id":"ORD-7788"})
[tool_call] process_refund({"amount":45,"order_id":"ORD-7790","reason":"Double charge on order."})
[tool_call] create_ticket({"category":"technical","priority":"medium","summary":"App crashes on iPhone when viewing orders"})