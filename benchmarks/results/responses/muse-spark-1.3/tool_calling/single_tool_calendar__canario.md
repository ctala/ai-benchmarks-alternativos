# Muse Spark 1.3 — tool_calling/single_tool_calendar

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 5.53 | quality: 5.0
- latency_total: 2.618s | tokens_per_second: 170.0
- input_tokens: 970 | output_tokens: 445

## Entrada exacta (lo que recibió el modelo)

**user:**

Agenda una reunion de proyecto para el 15 de mayo de 2026 a las 10:00 AM, duracion 60 minutos. Titulo: 'Sprint Planning Q2'.


## Respuesta completa

[tool_call] create_calendar_event({"date":"2026-05-15","description":"Reunion de proyecto Sprint Planning Q2","duration_minutes":60,"time":"10:00","title":"Sprint Planning Q2"})