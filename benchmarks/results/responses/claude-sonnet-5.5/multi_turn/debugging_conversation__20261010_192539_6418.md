# Claude Sonnet 5.5 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 13.273s | tokens_per_second: 122.3
- input_tokens: 541 | output_tokens: 1623

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un asistente tecnico experto en APIs y automatizacion. Ayuda a diagnosticar problemas paso a paso.

**user:**

Mi API de OpenRouter me da error 429 todo el tiempo. No puedo hacer ni una llamada.

**assistant:**

Error 429 es 'Too Many Requests' - significa que estas excediendo el rate limit. Vamos a diagnosticarlo:

1. Cuantas requests/minuto estas haciendo aproximadamente?
2. Que modelo estas usando? (algunos tienen limites mas bajos)
3. Estas usando la API key correcta? (las keys gratuitas tienen limites muy bajos)

**user:**

Estoy haciendo como 5 requests por minuto, usando DeepSeek V3. Tengo una API key con creditos pagados, unos $20 de saldo.

**assistant:**

5 req/min con DeepSeek deberia funcionar sin problemas - el limite es 300 RPM. Algo mas esta pasando. Vamos a verificar:

1. Estas reutilizando la misma instancia del cliente o creando una nueva por cada request?
2. Tienes algun retry automatico que podria estar multiplicando los requests?
3. Me puedes mostrar el header completo de la respuesta 429? Especificamente los headers `x-ratelimit-*`

**user:**

Acabo de revisar y resulta que tengo un loop en mi codigo que hace retry infinito cuando recibe un error. Asi que cada 429 genera como 100 requests mas. Pero no se como arreglarlo bien, como deberia implementar los retries?


## Respuesta completa

Encontraste la causa probable: un retry infinito convierte un 429 en una avalancha de requests, y el límite nunca se libera porque sigues golpeando la API. Antes de nada, **detén el script** y espera uno o dos minutos para que se enfríe.

También una corrección: antes dije que el límite de DeepSeek era 300 RPM, pero no tengo ese dato confirmado. Los límites en OpenRouter dependen del modelo, del proveedor upstream y de si usas una variante `:free`. Revisa los headers de la respuesta 429 para ver el límite real. Aun con el retry arreglado, un 429 puede venir del proveedor y no de tu cuenta.

## Cómo implementar retries correctamente

Reglas clave:
1. **Número máximo de intentos** (3-5), nunca infinito.
2. **Backoff exponencial con jitter**: esperas 1s, 2s, 4s... más un componente aleatorio.
3. **Respetar el header `Retry-After`** si viene.
4. **Reintentar solo errores transitorios**: 429, 500, 502, 503, 504. Nunca 400, 401, 402 o 403, porque reintentar no los arregla.

```python
import time
import random
import requests

RETRYABLE = {429, 500, 502, 503, 504}

def call_openrouter(payload, api_key, max_retries=4):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}

    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=60)
        except (requests.ConnectionError, requests.Timeout):
            if attempt == max_retries:
                raise
            resp = None

        if resp is not None:
            if resp.status_code == 200:
                return resp.json()

            if resp.status_code not in RETRYABLE:
                resp.raise_for_status()  # error no recuperable, falla de inmediato

            if attempt == max_retries:
                resp.raise_for_status()

        # calcular espera
        retry_after = resp.headers.get("Retry-After") if resp is not None else None
        if retry_after and retry_after.isdigit():
            delay = int(retry_after)
        else:
            delay = min(2 ** attempt, 30) + random.uniform(0, 1)

        print(f"Intento {attempt + 1} fallido, reintentando en {delay:.1f}s")
        time.sleep(delay)
```

## Extras recomendados

- **Librería `tenacity`** (Python): hace esto con un decorador si prefieres no escribirlo a mano.
- **Rate limiter del lado cliente**: si haces muchas llamadas, limita tú mismo la cadencia en vez de depender del 429.
- **Loguea los headers** (`x-ratelimit-*`, `Retry-After`) cuando falle, para saber de dónde viene el límite.

Si usas otro lenguaje (JS, Go, etc.) o el SDK de OpenAI apuntando a OpenRouter, dime y te lo adapto. Ese SDK ya trae `max_retries` configurable, así que quizá ni necesites tu propio loop.