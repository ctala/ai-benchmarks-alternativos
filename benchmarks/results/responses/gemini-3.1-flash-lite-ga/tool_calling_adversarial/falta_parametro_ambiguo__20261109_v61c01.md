# Gemini 3.1 Flash Lite (GA) — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 6.24 | quality: 5.7
- latency_total: 1.031s | tokens_per_second: 17.5
- input_tokens: 263 | output_tokens: 18
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al buscar el cliente correcto, pero carece de profundidad ya que no proporciona información adicional o insights. La claridad es buena, y la utilidad práctica es aceptable, ya que un emprendedor podría usar esta acción como un paso inicial.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Rodríguez"})