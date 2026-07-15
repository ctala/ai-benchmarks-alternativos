# Qwen3-Coder-Next (OpenRouter FP8) — tool_calling/multi_tool_sequential

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.22 | quality: 7.1
- latency_total: 2.649s | tokens_per_second: 47.9
- input_tokens: 914 | output_tokens: 127
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, aunque carece de profundidad adicional más allá de las instrucciones dadas.

## Respuesta completa

[tool_call] create_task({"title": "Revisar contrato cliente ABC", "priority": "urgent", "due_date": "2026-05-10"})
[tool_call] send_email({"to": "legal@empresa.com", "subject": "Contrato ABC - Revision urgente", "body": "Necesitamos que revisen el contrato del cliente ABC antes del 10 de mayo."})