# Grok 4.20 — tool_calling/multi_tool_sequential

- model_id: `x-ai/grok-4.20`
- success: True  | final: 7.58 | quality: 7.66
- latency_total: 4.474s | tokens_per_second: 14.8
- input_tokens: 657 | output_tokens: 66
- judge_score: 4.4 | justificación: 

## Respuesta completa

[tool_call] create_task({"title":"Revisar contrato cliente ABC","priority":"urgent","due_date":"2026-05-10"})
[tool_call] send_email({"to":"legal@empresa.com","subject":"Contrato ABC - Revision urgente","body":"Necesitamos revisión antes del 10 de mayo."})