# Qwen 3.5 397B (NIM) — tool_calling/multi_tool_sequential

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 7.33 | quality: 7.38
- latency_total: 20.311s | tokens_per_second: 6.6
- input_tokens: 752 | output_tokens: 135
- judge_score: 4.2 | justificación: 

## Respuesta completa

[tool_call] create_task({"title": "Revisar contrato cliente ABC", "due_date": "2026-05-10", "priority": "urgent"})
[tool_call] send_email({"to": "legal@empresa.com", "subject": "Contrato ABC - Revision urgente", "body": "Necesitamos revisión antes del 10 de mayo."})