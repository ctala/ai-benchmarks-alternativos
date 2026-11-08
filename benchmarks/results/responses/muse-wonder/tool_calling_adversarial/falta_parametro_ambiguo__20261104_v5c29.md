# Muse Wonder — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `meta/muse-wonder`
- success: True  | final: 5.84 | quality: 5.7
- latency_total: 2.089s | tokens_per_second: 100.1
- input_tokens: 844 | output_tokens: 209
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al buscar el cliente correcto, pero no proporciona información adicional o insights más allá de la acción inmediata requerida.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Rodríguez"})