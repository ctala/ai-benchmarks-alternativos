# Qwen3-Coder-Next (OpenRouter FP8) — tool_calling/tool_with_reasoning

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 8.5 | quality: 8.5
- latency_total: 1.77s | tokens_per_second: 73.4
- input_tokens: 889 | output_tokens: 130
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, proporcionando acciones concretas y una búsqueda útil, aunque la profundidad podría mejorarse con más detalles sobre las mejores prácticas.

## Respuesta completa

[tool_call] create_calendar_event({"title": "Repasar slides para presentación", "date": "2023-10-25", "time": "17:00", "duration_minutes": 60, "description": "Repasar las diapositivas de la presentación importante de mañana a las 3 PM."})
[tool_call] search_web({"query": "mejores prácticas para presentaciones ejecutivas"})