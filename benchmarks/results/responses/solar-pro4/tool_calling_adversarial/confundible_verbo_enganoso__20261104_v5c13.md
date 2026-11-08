# Solar Pro 4 — tool_calling_adversarial/confundible_verbo_enganoso

- model_id: `upstage/solar-pro4`
- success: True  | final: 6.09 | quality: 5.7
- latency_total: 1.758s | tokens_per_second: 12.5
- input_tokens: 616 | output_tokens: 22
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante al buscar la factura especificada, pero carece de profundidad y no proporciona insights adicionales o contexto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito ver qué le facturamos a la constructora Andes el mes pasado. La factura es la F-0398.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0398"})