# GPT-5.4 Mini — multi_turn/debugging_conversation

- model_id: `gpt-5.4-mini`
- success: True  | final: 9.06 | quality: 10.0
- latency_total: 5.407s | tokens_per_second: 133.4
- input_tokens: 312 | output_tokens: 721
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una estrategia detallada para manejar errores 429, incluyendo ejemplos de código, lo que la hace extremadamente útil y clara para un emprendedor.

## Respuesta completa

Sí: el problema es el retry infinito. La forma correcta es:

- **limitar el número de reintentos**
- **usar backoff exponencial**
- **respetar `Retry-After` si viene en la respuesta**
- **no reintentar errores que no son transitorios** (por ejemplo 401, 403, 400)
- opcionalmente **meter jitter** para evitar que varios workers reintenten al mismo tiempo

## Reglas prácticas

Reintenta solo en:
- `429`
- `500`
- `502`
- `503`
- `504`

No reintentes en:
- `400`
- `401`
- `403`
- `404`
- errores de validación

## Estrategia recomendada

1. Primer intento normal.
2. Si falla con error transitorio:
   - espera `Retry-After` si existe
   - si no existe, espera `base * 2^attempt + jitter`
3. Repite hasta un máximo de, por ejemplo, `3` a `5` retries.
4. Si sigue fallando, aborta y registra el error.

## Ejemplo de lógica

Pseudocódigo:

```text
max_retries = 5
base_delay = 1 segundo

for attempt in 0..max_retries:
    response = hacer_request()

    if response OK:
        return response

    if status no es reintentable:
        fail inmediato

    if attempt == max_retries:
        fail

    delay = retry_after_header o (base_delay * 2^attempt)
    delay = delay + random(0, 0.5 * delay)   # jitter
    sleep(delay)
```

## Ejemplo en Python

```python
import time
import random
import requests

RETRYABLE_STATUS = {429, 500, 502, 503, 504}

def call_api(url, headers=None, json=None, max_retries=5, base_delay=1.0):
    for attempt in range(max_retries + 1):
        resp = requests.post(url, headers=headers, json=json)

        if resp.ok:
            return resp.json()

        if resp.status_code not in RETRYABLE_STATUS:
            resp.raise_for_status()

        if attempt == max_retries:
            resp.raise_for_status()

        retry_after = resp.headers.get("Retry-After")
        if retry_after:
            try:
                delay = float(retry_after)
            except ValueError:
                delay = base_delay * (2 ** attempt)
        else:
            delay = base_delay * (2 ** attempt)

        jitter = random.uniform(0, delay * 0.5)
        time.sleep(delay + jitter)

    raise RuntimeError("Unreachable")
```

## Importante
Si estás haciendo varias requests en paralelo, los retries pueden empeorar el 429. En ese caso conviene además:

- limitar concurrencia
- poner una cola
- aplicar rate limiting del lado cliente

## Recomendación concreta para tu caso
Para OpenRouter, yo haría:

- `max_retries = 3`
- `base_delay = 1s`
- respetar `Retry-After`
- reintentar solo `429/5xx`
- añadir jitter
- cortar inmediatamente si es `401/403/400`

Si quieres, te puedo dar la implementación exacta en **Python**, **Node.js** o en el lenguaje que estés usando.