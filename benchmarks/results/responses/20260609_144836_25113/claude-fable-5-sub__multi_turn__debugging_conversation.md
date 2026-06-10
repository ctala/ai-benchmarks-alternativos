# Claude Fable 5 (suscripción) — multi_turn/debugging_conversation

- model_id: `claude-fable-5`
- success: True  | final: 7.71 | quality: 10.0
- latency_total: 18.009s | tokens_per_second: 71.7
- input_tokens: 2 | output_tokens: 1291

## Respuesta completa

¡Ahí está el problema! Tu retry infinito convierte cada 429 en una avalancha de requests, lo que a su vez genera más 429s. Es un círculo vicioso clásico.

Así se implementan retries correctamente:

## Principios clave

1. **Límite máximo de reintentos** (3-5, nunca infinito)
2. **Exponential backoff**: cada reintento espera el doble que el anterior
3. **Jitter**: agregar aleatoriedad para evitar que múltiples procesos reintenten al mismo tiempo
4. **Respetar el header `Retry-After`** si el servidor lo envía
5. **Solo reintentar errores recuperables** (429, 500, 502, 503) — nunca 400, 401, 404

## Implementación en Python

```python
import time
import random
import httpx

def call_openrouter(payload, max_retries=4):
    base_delay = 1.0  # segundos

    for attempt in range(max_retries + 1):
        response = httpx.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json=payload,
            timeout=120,
        )

        # Éxito
        if response.status_code == 200:
            return response.json()

        # Errores NO recuperables: fallar inmediatamente
        if response.status_code not in (429, 500, 502, 503):
            response.raise_for_status()

        # Si agotamos los reintentos, fallar
        if attempt == max_retries:
            response.raise_for_status()

        # Calcular espera
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            delay = float(retry_after)
        else:
            # Exponential backoff: 1s, 2s, 4s, 8s...
            delay = base_delay * (2 ** attempt)
            # Jitter: ±50% aleatorio
            delay = delay * (0.5 + random.random())

        print(f"Error {response.status_code}, reintento {attempt + 1}/{max_retries} en {delay:.1f}s")
        time.sleep(delay)
```

## Alternativa: usar una librería

Si no quieres mantener este código a mano, `tenacity` lo hace bien:

```python
from tenacity import retry, stop_after_attempt, wait_exponential_jitter, retry_if_exception

@retry(
    stop=stop_after_attempt(4),
    wait=wait_exponential_jitter(initial=1, max=60),
    retry=retry_if_exception(lambda e: isinstance(e, httpx.HTTPStatusError)
                              and e.response.status_code in (429, 500, 502, 503)),
)
def call_openrouter(payload):
    response = httpx.post(...)
    response.raise_for_status()
    return response.json()
```

## Bonus: prevenir en vez de reaccionar

Con 5 req/min legítimas no deberías necesitar retries casi nunca. Pero si escalas el volumen, considera:

- **Rate limiting del lado cliente**: un semáforo o token bucket que limite tus requests ANTES de enviarlas
- **Circuit breaker**: si recibes N errores seguidos, pausar todo por 1-2 minutos en vez de seguir golpeando la API

Una vez que arregles el loop, espera 5-10 minutos antes de probar — OpenRouter puede tener tu key temporalmente penalizada por el burst de requests que generaste. ¿Quieres que revisemos juntos el código actual de tu loop para integrar el fix?