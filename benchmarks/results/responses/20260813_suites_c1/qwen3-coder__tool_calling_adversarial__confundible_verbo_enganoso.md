# Qwen3 Coder — tool_calling_adversarial/confundible_verbo_enganoso

- model_id: `qwen/qwen3-coder`
- success: True  | final: 5.69 | quality: 5.7
- latency_total: 6.6s | tokens_per_second: 4.5
- input_tokens: 731 | output_tokens: 30
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante al buscar la factura especificada, pero no aborda la confusión del verbo 'facturar' y no proporciona insights adicionales o contexto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito ver qué le facturamos a la constructora Andes el mes pasado. La factura es la F-0398.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0398"})