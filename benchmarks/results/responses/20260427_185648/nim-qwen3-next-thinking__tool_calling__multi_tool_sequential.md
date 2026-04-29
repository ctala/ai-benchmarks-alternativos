# Qwen 3-Next 80B Thinking (NIM) — tool_calling/multi_tool_sequential

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 7.83 | quality: 7.66
- latency_total: 12.625s | tokens_per_second: 101.3
- input_tokens: 642 | output_tokens: 1279
- judge_score: 4.4 | justificación: 

## Respuesta completa

[tool_call] create_task({"title": "Revisar contrato cliente ABC", "due_date": "2026-05-10", "priority": "urgent"})
[tool_call] send_email({"to": "legal@empresa.com", "subject": "Contrato ABC - Revision urgente", "body": "Se requiere revisión del contrato del cliente ABC antes del 10 de mayo de 2026. Por favor, asegúrense de completar la revisión a tiempo."})