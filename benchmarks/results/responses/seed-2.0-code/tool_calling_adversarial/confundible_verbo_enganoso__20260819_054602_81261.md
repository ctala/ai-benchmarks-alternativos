# Seed 2.0 Code — tool_calling_adversarial/confundible_verbo_enganoso

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 6.99 | quality: 7.1
- latency_total: 2.113s | tokens_per_second: 47.8
- input_tokens: 777 | output_tokens: 101
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, identificando correctamente la herramienta adecuada para la tarea. Aunque no ofrece insights profundos, es práctica y útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito ver qué le facturamos a la constructora Andes el mes pasado. La factura es la F-0398.


## Respuesta completa

El usuario quiere ver los detalles de la factura F-0398 de la constructora Andes. La herramienta adecuada para buscar una factura por número es `buscar_factura`. Debo usar esa función con el número de factura proporcionado.