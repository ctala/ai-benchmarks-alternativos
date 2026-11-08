# Seed 2.0 Code — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.09 | quality: 8.5
- latency_total: 2.646s | tokens_per_second: 52.9
- input_tokens: 769 | output_tokens: 140
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, abordando adecuadamente la necesidad de desambiguar el cliente antes de emitir la factura.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

El usuario quiere emitir una factura a Rodríguez por $450.000 por mantenimiento. Primero, necesito buscar al cliente Rodríguez para obtener su cliente_id, ya que emitir_factura requiere ese parámetro. El usuario solo dio el apellido "Rodríguez", así que usaré buscar_cliente con query "Rodríguez" para encontrar su ID. No puedo emitir la factura sin el cliente_id, así que el primer paso es buscar al cliente.