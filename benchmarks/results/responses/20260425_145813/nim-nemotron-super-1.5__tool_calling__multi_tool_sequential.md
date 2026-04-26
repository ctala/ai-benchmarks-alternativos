# Nemotron Super 49B v1.5 (NIM) — tool_calling/multi_tool_sequential

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 7.63 | quality: 7.66
- latency_total: 10.685s | tokens_per_second: 36.4
- input_tokens: 679 | output_tokens: 389
- judge_score: 4.4 | justificación: 

## Respuesta completa

[tool_call] create_task({"due_date": "2026-05-10", "priority": "urgent", "title": "Revisar contrato cliente ABC"})
[tool_call] send_email({"body": "Necesitamos realizar una revisión urgente del contrato del cliente ABC antes del 10 de mayo de 2026.", "to": "legal@empresa.com", "subject": "Contrato ABC - Revision urgente"})