# Muse Spark 1.2 — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 4.32 | quality: 2.9
- latency_total: 1.224s | tokens_per_second: 116.9
- input_tokens: 910 | output_tokens: 143
- judge_score: 1 | justificación: La respuesta es incorrecta y no relevante porque el modelo inventó un comando de herramienta que no existe en el esquema dado, ignorando la instrucción de buscar facturas impagas del cliente Andes ordenadas por monto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})