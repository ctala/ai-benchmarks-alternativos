# Qwen 3-Next 80B Instruct (NIM) — tool_calling/multi_tool_sequential

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 7.68 | quality: 7.38
- latency_total: 4.663s | tokens_per_second: 30.2
- input_tokens: 640 | output_tokens: 141
- judge_score: 4.2 | justificación: 

## Respuesta completa

[tool_call] create_task({"title": "Revisar contrato cliente ABC", "due_date": "2026-05-10", "priority": "urgent"})
[tool_call] send_email({"to": "legal@empresa.com", "subject": "Contrato ABC - Revision urgente", "body": "Estimado equipo legal,\n\nNecesitamos que revisen el contrato del cliente ABC antes del 10 de mayo. Por favor, haganlo lo antes posible ya que es una tarea urgente.\n\nGracias por su atención."})