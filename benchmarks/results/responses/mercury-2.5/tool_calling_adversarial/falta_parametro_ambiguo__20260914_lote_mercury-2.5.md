# Mercury 2.5 — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `inception/mercury-2.5`
- success: True  | final: 5.86 | quality: 4.3
- latency_total: 0.981s | tokens_per_second: 482.3
- input_tokens: 772 | output_tokens: 473
- judge_score: 2.0 | justificación: La respuesta es precisa al buscar al cliente Rodríguez, pero no resuelve el problema de desambiguación necesario para emitir la factura, lo que la hace menos relevante y útil.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})