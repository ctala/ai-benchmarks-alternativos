# Mistral Large 3 675B — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 4.39 | quality: 2.9
- latency_total: 0.821s | tokens_per_second: 17.0
- input_tokens: 478 | output_tokens: 14
- judge_score: 1 | justificación: La respuesta inventa un parámetro 'query' que no es parte de la instrucción original, lo que indica una alucinación. No aborda la solicitud de filtrar facturas impagas y ordenarlas por monto, lo que la hace irrelevante y poco útil.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})