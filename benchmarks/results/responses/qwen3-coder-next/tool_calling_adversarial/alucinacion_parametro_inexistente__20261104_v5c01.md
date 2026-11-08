# Qwen3-Coder-Next (OpenRouter FP8) — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 8.5 | quality: 8.5
- latency_total: 1.776s | tokens_per_second: 55.7
- input_tokens: 723 | output_tokens: 99
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, proporcionando un enfoque paso a paso sin inventar parámetros inexistentes.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

El asistente no puede buscar facturas directamente por nombre de cliente, ni filtrarlas por estado de pago ni ordenarlas por monto. Primero se debe identificar al cliente mediante la herramienta `buscar_cliente`, y luego buscar las facturas individualmente por su número con `buscar_factura`.

A continuación te muestro cómo proceder:

