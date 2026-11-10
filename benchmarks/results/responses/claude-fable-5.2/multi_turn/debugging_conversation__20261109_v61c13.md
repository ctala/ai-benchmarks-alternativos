# Claude Fable 5.2 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 15.217s | tokens_per_second: 105.1
- input_tokens: 541 | output_tokens: 1599

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

Ese loop explica el 429: cada error dispara mas requests, que generan mas errores. Un retry bien hecho sigue cuatro reglas:

1. **Limite de intentos**: maximo 3-5, nunca infinito.
2. **Backoff exponencial**: esperar 1s, 2s, 4s, 8s... entre intentos.
3. **Jitter**: agregar aleatoriedad a la espera para que los retries no salgan sincronizados.
4. **Reintentar solo errores transitorios**: 429 y 5xx. Un 400, 401 o 402 va a fallar siempre, asi que reintentar no sirve.

Ademas, si la respuesta trae el header `Retry-After`, conviene usar ese valor en lugar del calculado.

Un ejemplo en Python (asumo que es tu lenguaje; si usas otro, dime y lo adapto):

```python
import random
import time
import requests

RETRYABLE = {429, 500, 502, 503, 504}

def call_openrouter(payload, api_key, max_retries=5, base_delay=1.0, max_delay=60.0):
    for attempt in range(max_retries + 1):
        resp = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json=payload,
            timeout=60,
        )

        if resp.ok:
            return resp.json()

        # Error no reintentable o se acabaron los intentos: fallar
        if resp.status_code not in RETRYABLE or attempt == max_retries:
            resp.raise_for_status()

        # Respetar Retry-After si viene; si no, backoff exponencial con jitter
        try:
            delay = float(resp.headers.get("Retry-After"))
        except (TypeError, ValueError):
            delay = random.uniform(0, min(max_delay, base_delay * 2 ** attempt))

        time.sleep(delay)
```

Si usas el SDK de OpenAI apuntando a OpenRouter, ya trae backoff integrado y no necesitas escribirlo a mano:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="tu-key",
    max_retries=5,
)
```

Antes de probar el codigo nuevo, deten el script actual y espera un par de minutos para que se resetee el rate limit. Si no, puedes seguir viendo 429 aunque el codigo ya este bien.