# Ministral 14B (NIM) — tool_calling/tool_with_reasoning

- model_id: `mistralai/ministral-14b-instruct-2512`
- success: True  | final: 5.88 | quality: 7.38
- latency_total: 2.294s | tokens_per_second: 28.8
- input_tokens: 559 | output_tokens: 66
- judge_score: 4.2 | justificación: 

## Respuesta completa

[tool_call] create_task({"title": "Repasar slides de la presentacion", "due_date": "2023-10-25", "priority": "urgent", "assignee": "usuario"})
[tool_call] search_web({"query": "mejores prácticas para presentaciones ejecutivas"})