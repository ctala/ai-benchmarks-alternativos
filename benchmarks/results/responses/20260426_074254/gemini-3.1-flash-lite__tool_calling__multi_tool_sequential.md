# Gemini 3.1 Flash Lite — tool_calling/multi_tool_sequential

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 8.08 | quality: 7.66
- latency_total: 2.276s | tokens_per_second: 44.4
- input_tokens: 492 | output_tokens: 101
- judge_score: 4.4 | justificación: 

## Respuesta completa

[tool_call] create_task({"title":"Revisar contrato cliente ABC","priority":"urgent","due_date":"2026-05-10"})
[tool_call] send_email({"to":"legal@empresa.com","subject":"Contrato ABC - Revision urgente","body":"Hola, necesitamos la revisión del contrato del cliente ABC antes del 10 de mayo. Gracias."})