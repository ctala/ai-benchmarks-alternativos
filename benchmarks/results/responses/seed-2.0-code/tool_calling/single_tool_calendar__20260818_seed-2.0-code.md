# Seed 2.0 Code — tool_calling/single_tool_calendar

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 6.73 | quality: 7.1
- latency_total: 5.525s | tokens_per_second: 49.8
- input_tokens: 828 | output_tokens: 275
- judge_score: 4.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Agenda una reunion de proyecto para el 15 de mayo de 2026 a las 10:00 AM, duracion 60 minutos. Titulo: 'Sprint Planning Q2'.


## Respuesta completa

Got it, let's see. The user wants to schedule a meeting. The details are: date 2026-05-15, time 10:00 AM, duration 60 minutes, title 'Sprint Planning Q2'. The create_calendar_event function needs title, date, time, duration_minutes, and description is optional. Let me check the parameters. The required ones are title, date, time, duration_minutes. The user provided all required. Date is YYYY-MM-DD: 2026-05-15, time 10:00 (since 10:00 AM is HH:MM 10:00), duration 60. Description isn't given, so we can omit it. So the function call should be create_calendar_event with those parameters.