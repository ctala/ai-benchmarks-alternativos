# Claude Fable 5.2 — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 3.64 | quality: 2.9
- latency_total: 2.485s | tokens_per_second: 52.3
- input_tokens: 910 | output_tokens: 130
- judge_score: 1 | justificación: La respuesta inventa un parámetro 'buscar_cliente' que no está soportado, lo que la hace incorrecta y no relevante para la instrucción dada.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

I need to find unpaid invoices for "Andes" sorted by amount, so I'll start by calling buscar_cliente to see whether the account status shows outstanding invoices.

