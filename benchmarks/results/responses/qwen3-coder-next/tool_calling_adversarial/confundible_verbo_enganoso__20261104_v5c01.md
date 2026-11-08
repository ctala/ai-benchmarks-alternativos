# Qwen3-Coder-Next (OpenRouter FP8) — tool_calling_adversarial/confundible_verbo_enganoso

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 6.39 | quality: 5.7
- latency_total: 1.012s | tokens_per_second: 30.6
- input_tokens: 731 | output_tokens: 31
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante al buscar la factura especificada, pero no proporciona información adicional o insights más allá de la acción básica de buscar la factura.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito ver qué le facturamos a la constructora Andes el mes pasado. La factura es la F-0398.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0398"})