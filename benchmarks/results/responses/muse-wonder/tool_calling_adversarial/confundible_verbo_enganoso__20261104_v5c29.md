# Muse Wonder — tool_calling_adversarial/confundible_verbo_enganoso

- model_id: `meta/muse-wonder`
- success: True  | final: 5.98 | quality: 5.7
- latency_total: 1.966s | tokens_per_second: 116.0
- input_tokens: 854 | output_tokens: 228
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante al buscar la factura especificada, pero carece de profundidad y no proporciona insights adicionales o contexto sobre la factura.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito ver qué le facturamos a la constructora Andes el mes pasado. La factura es la F-0398.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura":"F-0398"})