# Gemma 4 31B (NIM) — tool_calling/multi_tool_sequential

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 7.98 | quality: 7.38
- latency_total: 2.457s | tokens_per_second: 40.3
- input_tokens: 493 | output_tokens: 99
- judge_score: 4.2 | justificación: 

## Respuesta completa

[tool_call] create_task({"due_date": "2026-05-10", "priority": "urgent", "title": "Revisar contrato cliente ABC"})
[tool_call] send_email({"body": "Hola, necesitamos la revisión del contrato del cliente ABC antes del 10 de mayo. Saludos.", "subject": "Contrato ABC - Revision urgente", "to": "legal@empresa.com"})