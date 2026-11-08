# Gemma 4 26B MoE (3.8B activos) — tool_calling_adversarial/confundible_verbo_enganoso

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 6.54 | quality: 5.7
- latency_total: 0.657s | tokens_per_second: 36.5
- input_tokens: 422 | output_tokens: 24
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante al contexto, pero carece de profundidad y no proporciona insights adicionales.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito ver qué le facturamos a la constructora Andes el mes pasado. La factura es la F-0398.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0398"})