# Llama 4 Maverick — tool_calling_adversarial/confundible_verbo_enganoso

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 6.53 | quality: 5.7
- latency_total: 0.494s | tokens_per_second: 28.3
- input_tokens: 1110 | output_tokens: 14
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante al buscar la factura especificada, pero carece de profundidad y no proporciona información adicional o insights útiles.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito ver qué le facturamos a la constructora Andes el mes pasado. La factura es la F-0398.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0398"})