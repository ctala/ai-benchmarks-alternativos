# GLM 5.3 — multi_turn/debugging_conversation

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 24.701s | tokens_per_second: 72.8
- input_tokens: 331 | output_tokens: 1798

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

Buen hallazgo - eso explica todo. Un 429 genera mas requests, que generan mas 429s: avalancha clasica de retries. Un retry bien implementado necesita 4 cosas:

1. **Limite de intentos** (3-5 max)
2. **Backoff exponencial** (esperar 1s, 2s, 4s...)
3. **Respetar el header `Retry-After`** si el server lo envia
4. **Solo reintentar errores reintentables** (429, 5xx, errores de red) - nunca 400, 401, 403, porque esos van a fallar igual siempre

**Opcion A: Si usas el SDK de OpenAI (OpenRouter es compatible)**

El SDK ya trae esto implementado, solo configuralo:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-...",
    max_retries=3,  # backoff exponencial incluido
)
```

**Opcion B: Implementacion manual (con requests)**

```python
import time
import random
import requests

def call_openrouter(payload, max_retries=4):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer sk-or-...",
        "Content-Type": "application/json",
    }

    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=60)
        except requests.RequestException:
            if attempt == max_retries:
                raise
            time.sleep(2 ** attempt)
            continue

        if resp.status_code == 200:
            return resp.json()

        # Reintentables: 429 y errores de servidor
        if resp.status_code == 429 or resp.status_code >= 500:
            if attempt == max_retries:
                resp.raise_for_status()  # ya no hay mas intentos, propaga el error

            # Prioridad al Retry-After del server
            retry_after = resp.headers.get("Retry-After")
            if retry_after:
                delay = int(retry_after)
            else:
                # Backoff exponencial + jitter
                delay = (2 ** attempt) + random.uniform(0, 1)

            time.sleep(delay)
            continue

        # No reintentable (400, 401, 403, 404...): fallar ya
        resp.raise_for_status()
```

Puntos clave:

- **El jitter** (`random.uniform`) evita que multiples workers se sincronicen y golpeen el server todos a la vez.
- **El cap de intentos** es tu red de seguridad: si despues de 4 intentos con backoff sigues en 429, el problema es otro (saldo, key, limite de cuenta) y reintentar no lo va a arreglar.
- **Timeout en el request**: sin el, un request colgado tambien puede disparar retries innecesarios.

En que lenguaje esta tu codigo? Si no es Python te adapto el ejemplo.