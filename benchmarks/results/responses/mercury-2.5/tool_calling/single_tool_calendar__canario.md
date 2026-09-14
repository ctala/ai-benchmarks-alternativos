# Mercury 2.5 — tool_calling/single_tool_calendar

- model_id: `inception/mercury-2.5`
- success: True  | final: 6.2 | quality: 5.0
- latency_total: 1.305s | tokens_per_second: 441.3
- input_tokens: 842 | output_tokens: 576

## Entrada exacta (lo que recibió el modelo)

**user:**

Agenda una reunion de proyecto para el 15 de mayo de 2026 a las 10:00 AM, duracion 60 minutos. Titulo: 'Sprint Planning Q2'.


## Respuesta completa

[tool_call] create_calendar_event({"title": "Sprint Planning Q2", "date": "2026-05-15", "time": "10:00", "duration_minutes": 60})