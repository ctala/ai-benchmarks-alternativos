# Llama 3.3 70B — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `meta-llama/llama-3.3-70b-instruct`
- success: True  | final: 4.73 | quality: 2.9
- latency_total: 0.484s | tokens_per_second: 49.6
- input_tokens: 727 | output_tokens: 24
- judge_score: 1 | justificación: La respuesta es incorrecta porque inventa un parámetro de consulta no soportado, no responde a la solicitud original, y carece de profundidad y utilidad.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})