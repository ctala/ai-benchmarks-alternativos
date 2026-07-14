# Ministral 14B — tool_calling/tool_with_reasoning

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 7.22 | quality: 7.1
- latency_total: 2.267s | tokens_per_second: 39.3
- input_tokens: 559 | output_tokens: 89
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con acciones directas que un emprendedor podría usar, aunque la profundidad es solo aceptable ya que no ofrece insights adicionales más allá de las instrucciones.

## Respuesta completa

[tool_call] create_calendar_event({"title": "Repasar slides de presentación", "date": "2023-10-27", "time": "17:00", "duration_minutes": 60, "description": "Repasar las slides para la presentación importante de mañana a las 3 PM"})
[tool_call] search_web({"query": "mejores prácticas para presentaciones ejecutivas"})