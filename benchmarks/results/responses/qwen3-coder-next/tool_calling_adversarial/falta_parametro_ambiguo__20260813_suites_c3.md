# Qwen3-Coder-Next (OpenRouter FP8) — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.52 | quality: 7.1
- latency_total: 0.557s | tokens_per_second: 44.9
- input_tokens: 724 | output_tokens: 25
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante al abordar el problema de desambiguación al buscar al cliente 'Rodríguez'. La claridad es alta ya que la acción es directa y fácil de entender. Sin embargo, la profundidad es limitada ya que no ofrece más allá de la acción inmediata de búsqueda, y la utilidad práctica es moderada ya que, aunque útil, no proporciona pasos adicionales o consideraciones para manejar múltiples resultados.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})