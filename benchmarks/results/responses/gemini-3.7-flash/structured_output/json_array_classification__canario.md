# Gemini 3.7 Flash — structured_output/json_array_classification

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.99 | quality: 10.0
- latency_total: 7.256s | tokens_per_second: 124.3
- input_tokens: 162 | output_tokens: 902

## Entrada exacta (lo que recibió el modelo)

**system:**

Responde SOLO con un JSON array valido. Sin explicaciones ni markdown.

**user:**

Clasifica estos emails de soporte. Para cada uno devuelve: category (billing/shipping/technical/general), priority (low/medium/high/urgent), sentiment (positive/negative/neutral).

1. "Mi pedido no ha llegado y ya pasaron 10 dias. Necesito una solucion YA."
2. "Hola, queria saber si tienen envio internacional. Gracias!"
3. "Me cobraron dos veces en mi tarjeta. EXIJO un reembolso inmediato."
4. "La app no carga desde la actualizacion. Error 500 al iniciar sesion."

Formato: [{"id": 1, "category": "", "priority": "", "sentiment": ""}, ...]


## Respuesta completa

[{"id": 1, "category": "shipping", "priority": "urgent", "sentiment": "negative"}, {"id": 2, "category": "shipping", "priority": "low", "sentiment": "neutral"}, {"id": 3, "category": "billing", "priority": "urgent", "sentiment": "negative"}, {"id": 4, "category": "technical", "priority": "high", "sentiment": "negative"}]