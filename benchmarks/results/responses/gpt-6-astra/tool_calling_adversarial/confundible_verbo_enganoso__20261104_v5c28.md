# GPT-6 Astra — tool_calling_adversarial/confundible_verbo_enganoso

- model_id: `openai/gpt-6-astra`
- success: True  | final: 5.68 | quality: 5.7
- latency_total: 1.44s | tokens_per_second: 16.7
- input_tokens: 264 | output_tokens: 24
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante al buscar la factura especificada, pero carece de profundidad y no ofrece insights adicionales.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito ver qué le facturamos a la constructora Andes el mes pasado. La factura es la F-0398.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura":"F-0398"})