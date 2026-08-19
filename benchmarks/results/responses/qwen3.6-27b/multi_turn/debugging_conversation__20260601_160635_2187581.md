# Qwen 3.6 27B base (OpenRouter FP8) — multi_turn/debugging_conversation

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 5.96 | quality: 6.24
- latency_total: 35.933s | tokens_per_second: 57.0
- input_tokens: 340 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando una guía clara sobre cómo manejar errores de API, especialmente el error 429, con buenas prácticas de reintento, lo que es útil para un emprendedor.

## Respuesta completa

¡Exacto! Un loop infinito que reintenta **cualquier** error es la causa clásica de este problema. Cada `429` se convierte en una avalancha que satura tus límites y congela tu cuenta.

Aquí tienes la forma correcta de implementarlo, paso a paso:

### 🔑 Reglas de oro para retries en APIs
1. **Solo reintentar errores transitorios**: `429` (rate limit) y `5xx` (errores del servidor).
2. **Nunca reintentar `4xx`**: `400`,