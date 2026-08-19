# Llama 3.1 8B Instant (Groq) — tool_calling/multi_tool_sequential

- model_id: `llama-3.1-8b-instant`
- success: True  | final: 8.58 | quality: 7.66
- latency_total: 0.489s | tokens_per_second: 186.1
- input_tokens: 624 | output_tokens: 91
- judge_score: 4.4 | justificación: 

## Respuesta completa

[tool_call] create_task({"due_date":"2026-05-10","priority":"urgent","title":"Revisar contrato cliente ABC"})
[tool_call] send_email({"body":"Necesitamos revision del contrato antes del 10 de mayo, por favor priorice esto","subject":"Contrato ABC - Revision urgente","to":"legal@empresa.com"})