# Devstral 2 123B (NIM) — tool_calling/multi_tool_sequential

- model_id: `mistralai/devstral-2-123b-instruct-2512`
- success: True  | final: 7.88 | quality: 7.38
- latency_total: 3.822s | tokens_per_second: 25.6
- input_tokens: 565 | output_tokens: 98
- judge_score: 4.2 | justificación: 

## Respuesta completa

[tool_call] create_task({"title": "Revisar contrato cliente ABC", "due_date": "2026-05-10", "priority": "urgent"})
[tool_call] send_email({"to": "legal@empresa.com", "subject": "Contrato ABC - Revision urgente", "body": "Hola, necesitamos que revisen el contrato del cliente ABC antes del 10 de mayo. Es urgente. Gracias."})