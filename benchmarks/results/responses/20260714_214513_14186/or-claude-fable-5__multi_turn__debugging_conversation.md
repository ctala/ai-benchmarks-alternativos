# Claude Fable 5 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 15.427s | tokens_per_second: 59.7
- input_tokens: 539 | output_tokens: 921
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y prácticamente útil, abordando directamente el problema del error 429 con una solución detallada y ejemplos de código.

## Respuesta completa

Ahi esta el problema - tu retry loop crea un efecto avalancha: cada 429 genera mas requests, que generan mas 429s. El fix correcto es **exponential backoff con jitter**:

## Principios clave

1. **Limite maximo de reintentos** (3-5 tipico)
2. **Espera exponencial**: cada retry espera el doble (1s, 2s, 4s, 8s...)
3. **Jitter aleatorio**: evita que multiples clientes reintenten al mismo tiempo
4. **Respetar el header `Retry-After`** si el servidor lo envia

## Ejemplo en Python

```python
import time
import random
import requests

def call_with_retry(url, payload, headers, max_retries=4):
    for attempt in range(max_retries + 1):
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 429:
            if attempt == max_retries:
                raise Exception("Rate limit persistente tras todos los retries")

            # Respetar Retry-After si existe
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                wait = float(retry_after)
            else:
                # Backoff exponencial: 1s, 2s, 4s, 8s + jitter
                wait = (2 ** attempt) + random.uniform(0, 1)

            print(f"429 recibido. Esperando {wait:.1f}s (intento {attempt + 1}/{max_retries})")
            time.sleep(wait)
        else:
            # Errores no-retriables (400, 401, etc): fallar inmediato
            response.raise_for_status()
```

## Puntos importantes

- **Solo reintenta errores retriables**: 429, 500, 502, 503. Un 400 o 401 nunca se arreglara reintentando
- **Si usas librerias**, `tenacity` (Python) o `p-retry` (Node.js) ya implementan esto bien:

```python
from tenacity import retry, wait_exponential, stop_after_attempt

@retry(wait=wait_exponential(multiplier=1, max=30), stop=stop_after_attempt(4))
def mi_llamada():
    ...
```

Con esto, un 429 puntual genera maximo 4 requests adicionales espaciados, no 100 instantaneos. Prueba el fix y avisame si el 429 persiste - si sigue apareciendo con backoff correcto, habria que mirar otra cosa.