# Gemma 4 26B MoE (3.8B activos) — tool_calling_adversarial/confundible_verbo_enganoso

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 7.52 | quality: 7.1
- latency_total: 0.692s | tokens_per_second: 34.7
- input_tokens: 422 | output_tokens: 24
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, identificando correctamente la herramienta para buscar la factura especificada. Aunque no ofrece profundidad adicional o insights, es clara y directamente útil para un emprendedor que necesita acceder a información de facturación.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito ver qué le facturamos a la constructora Andes el mes pasado. La factura es la F-0398.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0398"})