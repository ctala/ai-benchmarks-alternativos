# Seed 2.0 Code — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.09 | quality: 8.5
- latency_total: 2.872s | tokens_per_second: 50.5
- input_tokens: 769 | output_tokens: 145
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, abordando adecuadamente el problema de desambiguación antes de emitir la factura, lo que la hace altamente útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

El usuario quiere emitir una factura para Rodríguez, de $450.000 por mantenimiento. Primero, necesito buscar al cliente "Rodríguez" para obtener su ID, ya que la función emitir_factura requiere el cliente_id. No tengo el ID del cliente, así que primero debo usar buscar_cliente con el query "Rodríguez". Luego, con el ID obtenido, podré emitir la factura. Así que el primer paso es llamar a buscar_cliente.