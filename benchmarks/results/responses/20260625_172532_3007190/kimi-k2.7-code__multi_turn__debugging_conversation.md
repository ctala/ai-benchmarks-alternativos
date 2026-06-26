# Kimi K2.7 Code — multi_turn/debugging_conversation

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 7.1 | quality: 8.74
- latency_total: 30.462s | tokens_per_second: 21.7
- input_tokens: 385 | output_tokens: 660
- judge_score: 4.8 | justificación: 

## Respuesta completa

 Ese es el problema tipico: el propio retry te genera el rate limit. Necesitas backoff exponencial con jitter, un maximo de intentos, y **no reintentar errores 4xx excepto 429**.

Aqui tienes una implementacion correcta:

### Opcion 1: Con `tenacity` (recomendada)

```python
import openai
from tenacity import retry, stop_after_attempt, wait_exponential_jitter, retry_if_exception_type

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-v1-..."
)

@retry(
    stop=stop_after_attempt(4),                    # max 4 intentos
    wait=wait_exponential_jitter(initial=1, max=10), # 1s, 2s, 4s, ~8s + jitter
    retry=retry_if_exception_type(openai.RateLimitError),
)
def call_api(messages):
    return client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=messages,
    )
```

### Opcion 2: Implementacion manual (sin librerias)

```python
import random
import time
from openai import RateLimitError, APIError, APIConnectionError

def call_with_retry(client, messages, max_retries=4):
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(
                model="deepseek/deepseek-chat",
                messages=messages,
            )
        except RateLimitError:
            wait = min(2 ** attempt, 10) + random.uniform(0, 1)
            time.sleep(wait)
        except (APIConnectionError, APIError) as e:
            # solo reintentar 5xx, no 4xx
            if e.status_code and e.status_code >= 500:
                time.sleep(2 ** attempt)
            else:
                raise
    raise Exception("Max retries excedido")
```

### Reglas clave

- **Nunca reintentes 400, 401, 403, 404**: son errores del request, no de capacidad
- **429 y 5xx si**: pero con backoff exponencial
- **Maximo fijo de intentos**: nunca infinito
- **Jitter**: evita que todos tus workers golpeen al mismo tiempo cuando se recupera el servicio

Con esto pasarias de 100 requests por error a maximo 4.

Quieres que lo adapte a tu framework o lenguaje actual?