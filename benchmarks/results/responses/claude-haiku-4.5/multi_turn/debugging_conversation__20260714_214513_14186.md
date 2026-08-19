# Claude Haiku 4.5 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-haiku-4.5`
- success: True  | final: 7.24 | quality: 7.5
- latency_total: 4.862s | tokens_per_second: 139.9
- input_tokens: 393 | output_tokens: 680
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución detallada con ejemplos de código para manejar errores 429 mediante reintentos con backoff exponencial, incluyendo una alternativa robusta con la biblioteca tenacity.

## Respuesta completa

Ah, eso explica todo. Aquí está la forma correcta de hacer retries con exponential backoff:

```python
import time
import random
from typing import Any

def call_openrouter_with_retry(
    client,
    model: str,
    messages: list,
    max_retries: int = 3,
    base_delay: float = 1.0
) -> Any:
    """
    Llama OpenRouter con reintentos exponenciales
    """
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model=model,
                messages=messages
            )
            return response
            
        except Exception as e:
            # Extraer el status code si es posible
            status_code = getattr(e, 'status_code', None)
            
            # 429 = rate limit, 5xx = server error (reintentar)
            # 4xx otros = no reintentar (auth, bad request, etc)
            if status_code not in [429, 500, 502, 503, 504]:
                raise  # No reintentar errores de cliente
            
            if attempt == max_retries - 1:
                raise  # Ultimo intento, lanzar error
            
            # Exponential backoff + jitter
            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
            print(f"Intento {attempt + 1}/{max_retries} falló. Esperando {delay:.1f}s...")
            time.sleep(delay)
    
    return None
```

**Puntos clave:**

- **Max retries**: 3-5 es suficiente, no infinito
- **Exponential backoff**: 1s → 2s → 4s (evita sobrecargar)
- **Jitter**: `random.uniform(0, 1)` para evitar "thundering herd"
- **Selectivo**: Solo reintentar 429 y 5xx, no otros 4xx

**Alternativa con `tenacity` (más robusta):**

```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((RateLimitError, ServerError))
)
def call_openrouter(client, model, messages):
    return client.messages.create(model=model, messages=messages)
```

¿Cuál prefieres implementar? ¿Necesitas que sea async también?