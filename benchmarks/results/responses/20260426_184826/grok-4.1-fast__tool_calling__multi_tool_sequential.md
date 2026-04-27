# Grok 4.1 Fast — tool_calling/multi_tool_sequential

- model_id: `x-ai/grok-4.1-fast`
- success: True  | final: 8.08 | quality: 7.66
- latency_total: 5.037s | tokens_per_second: 90.3
- input_tokens: 699 | output_tokens: 455
- judge_score: 4.4 | justificación: 

## Respuesta completa

[tool_call] create_task({"title":"Revisar contrato cliente ABC","due_date":"2026-05-10","priority":"urgent"})
[tool_call] send_email({"to":"legal@empresa.com","subject":"Contrato ABC - Revision urgente","body":"Necesitamos que el equipo legal revise el contrato del cliente ABC de manera urgente antes del 10 de mayo de 2026."})