# Nemotron 3 Nano 30B — tool_calling/multi_tool_sequential

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.93 | quality: 7.38
- latency_total: 22.949s | tokens_per_second: 96.8
- input_tokens: 894 | output_tokens: 2221
- judge_score: 4.2 | justificación: 

## Respuesta completa

[tool_call] create_task({"title": "Revisar contrato cliente ABC", "due_date": "2026-05-10", "priority": "urgent"})
[tool_call] send_email({"subject": "Contrato ABC - Revision urgente", "body": "Se requiere la revisi\u00f3n del contrato ABC antes del 10 de mayo. Por favor, realicen la revisi\u00f3n con urgencia.", "to": "legal@empresa.com"})