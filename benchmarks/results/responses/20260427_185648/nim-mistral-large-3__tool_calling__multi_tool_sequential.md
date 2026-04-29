# Mistral Large 3 675B (NIM) — tool_calling/multi_tool_sequential

- model_id: `mistralai/mistral-large-3-675b-instruct-2512`
- success: True  | final: 6.96 | quality: 7.38
- latency_total: 26.889s | tokens_per_second: 5.6
- input_tokens: 566 | output_tokens: 151
- judge_score: 4.2 | justificación: 

## Respuesta completa

[tool_call] create_task({"title": "Revisar contrato cliente ABC", "due_date": "2026-05-10", "priority": "urgent"})
[tool_call] send_email({"to": "legal@empresa.com", "subject": "Contrato ABC - Revisión urgente", "body": "Estimado equipo legal,\n\nNecesitamos que revisen con urgencia el contrato del cliente ABC. La fecha límite para completar la revisión es el **10 de mayo de 2026**. \n\nPor favor, confirmen una vez que lo hayan revisado o si necesitan información adicional.\n\nGracias,\nSaludos."})