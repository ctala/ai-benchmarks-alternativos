# Llama 4 Maverick — tool_calling/multi_tool_sequential

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 6.63 | quality: 7.1
- latency_total: 11.387s | tokens_per_second: 5.4
- input_tokens: 1300 | output_tokens: 62
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, cumpliendo con las instrucciones dadas. Aunque no ofrece profundidad adicional más allá de las instrucciones, es altamente útil para un emprendedor.

## Respuesta completa

[tool_call] create_task({"title": "Revisar contrato cliente ABC", "priority": "urgent", "due_date": "2026-05-10"})
[tool_call] send_email({"to": "legal@empresa.com", "subject": "Contrato ABC - Revision urgente", "body": "Necesitamos revisar el contrato antes del 10 de mayo"})