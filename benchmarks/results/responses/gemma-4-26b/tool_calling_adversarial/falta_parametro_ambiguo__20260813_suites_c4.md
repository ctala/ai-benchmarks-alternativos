# Gemma 4 26B MoE (3.8B activos) — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 6.39 | quality: 5.7
- latency_total: 0.806s | tokens_per_second: 21.1
- input_tokens: 415 | output_tokens: 17
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al intentar desambiguar el nombre del cliente, pero carece de profundidad ya que no ofrece insights adicionales o soluciones. La claridad es buena, ya que la acción es clara y directa. La utilidad práctica es aceptable, ya que un emprendedor podría usar esta acción como un paso inicial para resolver el problema de desambiguación.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})