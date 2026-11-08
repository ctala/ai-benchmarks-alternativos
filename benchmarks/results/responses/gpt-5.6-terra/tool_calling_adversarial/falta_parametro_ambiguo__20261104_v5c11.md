# GPT-5.6 Terra — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 6.08 | quality: 5.7
- latency_total: 1.492s | tokens_per_second: 31.5
- input_tokens: 255 | output_tokens: 47
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al buscar al cliente correcto, pero carece de profundidad ya que no proporciona información adicional o insights. La claridad es buena, y la utilidad práctica es aceptable, ya que un emprendedor podría usar esta acción como un paso inicial para desambiguar el cliente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Rodríguez"})