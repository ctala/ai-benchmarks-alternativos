# Qwen 3-Next 80B Thinking (NIM) — tool_calling/multi_tool_sequential

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 7.73 | quality: 7.38
- latency_total: 10.486s | tokens_per_second: 118.1
- input_tokens: 642 | output_tokens: 1238
- judge_score: 4.2 | justificación: 

## Respuesta completa

[tool_call] create_task({"title": "Revisar contrato cliente ABC", "due_date": "2026-05-10", "priority": "urgent"})
[tool_call] send_email({"to": "legal@empresa.com", "subject": "Contrato ABC - Revision urgente", "body": "Necesitamos revisar el contrato antes del 10 de mayo de 2026. Por favor, asegúrense de completar la revisión a tiempo."})