# Gemma 4 12B (Spark llama-server, reasoning) — tool_calling/multi_tool_sequential

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.1 | quality: 7.66
- latency_total: 10.38s | tokens_per_second: 25.3
- input_tokens: 507 | output_tokens: 263
- judge_score: 4.4 | justificación: 

## Respuesta completa

[tool_call] create_task({"due_date":"2026-05-10","priority":"urgent","title":"Revisar contrato cliente ABC"})
[tool_call] send_email({"body":"Necesitamos la revisión del contrato del cliente ABC antes del 10 de mayo.","subject":"Contrato ABC - Revision urgente","to":"legal@empresa.com"})