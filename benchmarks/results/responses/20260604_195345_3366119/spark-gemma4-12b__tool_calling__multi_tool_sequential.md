# Gemma 4 12B (Spark llama-server Q4_K_M) — tool_calling/multi_tool_sequential

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.4 | quality: 7.66
- latency_total: 4.354s | tokens_per_second: 24.3
- input_tokens: 509 | output_tokens: 106
- judge_score: 4.4 | justificación: 

## Respuesta completa

[tool_call] create_task({"due_date":"2026-05-10","priority":"urgent","title":"Revisar contrato cliente ABC"})
[tool_call] send_email({"body":"Hola, necesitamos la revisión del contrato del cliente ABC antes del 10 de mayo. Por favor, procedan con la revisión urgente.","subject":"Contrato ABC - Revision urgente","to":"legal@empresa.com"})