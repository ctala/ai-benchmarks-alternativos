# Qwen 3-Next 80B Thinking — tool_calling/tool_with_reasoning

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.86 | quality: 7.1
- latency_total: 13.865s | tokens_per_second: 178.0
- input_tokens: 628 | output_tokens: 2468
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, cumpliendo con las instrucciones dadas. Aunque la profundidad es aceptable, no ofrece insights adicionales más allá de las instrucciones, pero es altamente util para un emprendedor.

## Respuesta completa

<tools>
{"name": "create_calendar_event", "arguments": {"title": "Repasar slides para presentación", "date": "2023-10-05", "time": "17:00", "duration_minutes": 30}}
</tools>

<tools>
{"name": "search_web", "arguments": {"query": "mejores practicas para presentaciones ejecutivas"}}
</tools>