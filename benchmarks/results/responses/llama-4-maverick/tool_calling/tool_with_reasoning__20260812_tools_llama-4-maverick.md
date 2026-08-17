# Llama 4 Maverick — tool_calling/tool_with_reasoning

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 6.7 | quality: 7.1
- latency_total: 10.756s | tokens_per_second: 5.7
- input_tokens: 828 | output_tokens: 61
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, cumpliendo con las instrucciones proporcionadas. Aunque la profundidad es solo aceptable, ya que no ofrece insights adicionales más allá de las instrucciones, sigue siendo altamente útil para un emprendedor.

## Respuesta completa

[tool_call] create_calendar_event({"title": "Repasar slides", "date": "2024-03-13", "time": "17:00", "duration_minutes": 60, "description": "Repasar slides para la presentacion de manana"})
[tool_call] search_web({"query": "mejores practicas para presentaciones ejecutivas"})