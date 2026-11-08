# Llama 4 Maverick — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 7.48 | quality: 7.1
- latency_total: 1.154s | tokens_per_second: 56.3
- input_tokens: 1100 | output_tokens: 65
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante al abordar la necesidad de desambiguar el cliente antes de emitir la factura, y está claramente estructurada. Ofrece un enfoque práctico, aunque no profundiza en detalles adicionales más allá de la desambiguación básica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

To emit the invoice, we first need to find the client ID for Rodríguez. Then, we can use that ID to emit the invoice.

[buscar_cliente(query="Rodríguez"), emitir_factura(cliente_id=buscar_cliente(query="Rodríguez").id, monto=450000, concepto="mantenimiento")]