# Muse Glimmer 30B — multi_turn/debugging_conversation

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 9.29 | quality: 10.0
- latency_total: 2.999s | tokens_per_second: 56.3
- input_tokens: 334 | output_tokens: 169
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando un ejemplo práctico de manejo de errores con backoff exponencial y jitter, lo cual es útil para resolver el problema de errores 429.

## Respuesta completa

Ah, claro. Eso es un loop de muerte: 429 -> retry -> 429 -> retry... necesitas un backoff exponencial con jitter. Te dejo un ejemplo basico en Python:

```python
import time, random
import openai

client = openai.OpenAI(base_url="https://openrouter.ai/api/v1", api_key="...")

def call_with_retry(prompt, max_retries=3):
    for i in range(max_retries):
        try:
            return client.chat.completions.create(...)
        except Exception as e:
            if i == max_retries - 1: raise
            wait = (2 ** i) + random.uniform(0, 1)
            time.sleep(wait)
```

Tambien revisa los headers de respuesta para ver el `Retry-After`