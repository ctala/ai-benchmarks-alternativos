# Gemma 4 26B MoE (3.8B activos) — tool_calling/single_tool_calendar

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 6.2 | quality: 5.0
- latency_total: 0.99s | tokens_per_second: 52.5
- input_tokens: 481 | output_tokens: 52

## Entrada exacta (lo que recibió el modelo)

**user:**

Agenda una reunion de proyecto para el 15 de mayo de 2026 a las 10:00 AM, duracion 60 minutos. Titulo: 'Sprint Planning Q2'.


## Respuesta completa

[tool_call] create_calendar_event({"date": "2026-05-15", "duration_minutes": 60, "time": "10:00", "title": "Sprint Planning Q2"})