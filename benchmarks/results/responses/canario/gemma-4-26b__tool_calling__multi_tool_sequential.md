# Gemma 4 26B MoE (3.8B activos) — tool_calling/multi_tool_sequential

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 5.3 | quality: 5.0
- latency_total: 6.602s | tokens_per_second: 14.8
- input_tokens: 509 | output_tokens: 98

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito que hagas lo siguiente:
1. Crea una tarea urgente titulada 'Revisar contrato cliente ABC' con fecha limite 2026-05-10
2. Envia un email a legal@empresa.com con asunto 'Contrato ABC - Revision urgente' explicando que necesitamos revision antes del 10 de mayo


## Respuesta completa

[tool_call] create_task({"due_date": "2026-05-10", "priority": "urgent", "title": "Revisar contrato cliente ABC"})
[tool_call] send_email({"body": "Hola, necesitamos la revisión del contrato del cliente ABC antes del 10 de mayo. Gracias.", "subject": "Contrato ABC - Revision urgente", "to": "legal@empresa.com"})