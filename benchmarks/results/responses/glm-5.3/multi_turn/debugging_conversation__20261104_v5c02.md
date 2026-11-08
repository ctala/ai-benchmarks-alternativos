# GLM 5.3 — multi_turn/debugging_conversation

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 22.692s | tokens_per_second: 82.3
- input_tokens: 331 | output_tokens: 1867

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

Ese loop explica todo: cada 429 disparaba mas requests, que generaban mas 429s, en cascada. La regla de oro es: **el retry debe esperar, no insistir inmediatamente**.

Los 4 principios de un retry bien hecho:

1. **Exponential backoff**: espera 1s, 2s, 4s, 8s... duplicando cada vez. Asi le das tiempo al rate limit a resetearse.
2. **Respeta el header `Retry-After`**: cuando OpenRouter te lo envia, usa ese valor en vez de tu propio calculo.
3. **Limite de intentos**: maximo 3-5 reintentos, despues falla y reporta el error. Nunca infinito.
4. **Solo reintenta errores reintentables**: 429, 500, 502, 503, 504. Un 401 o 400 va a fallar siempre - reintenterlo es inutil.

Ejemplo en Python:

```python
import time
import random
import requests

RETRYABLE = {429, 500, 502, 503, 504}

def call_openrouter(payload, max_retries=5):
    for attempt in range(max_retries):
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": "Bearer TU_KEY"},
            json=payload,
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code not in RETRYABLE:
            response.raise_for_status()  # error no reintentable, falla ya

        if attempt == max_retries - 1:
            response.raise_for_status()  # se acabaron los intentos

        # Prioridad al header del servidor
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            delay = float(retry_after)
        else:
            delay = (2 ** attempt) + random.uniform(0, 1)  # backoff + jitter

        print(f"{response.status_code}, reintento en {delay:.1f}s ({attempt + 1}/{max_retries})")
        time.sleep(delay)
```

Tip extra: si usas el SDK de OpenAI apuntando a OpenRouter (patron comun), ya trae retries con exponential backoff integrados - solo configura:

```python
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="tu-key",
    max_retries=3,
)
```

En que lenguaje esta tu codigo? Te adapto el ejemplo si no es Python.