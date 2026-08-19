# GPT-5.5 — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `gpt-5.5`
- success: True  | final: 6.62 | quality: 7.1
- latency_total: 3.085s | tokens_per_second: 37.3
- input_tokens: 255 | output_tokens: 115
- judge_score: 4.0 | justificación: La respuesta es relevante al abordar el problema de desambiguación necesario antes de emitir la factura, pero carece de profundidad ya que no proporciona un plan de acción o pasos adicionales más allá de la búsqueda inicial.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Rodríguez"})