# GPT-6 Luna Pro — multi_turn/debugging_conversation

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 26.684s | tokens_per_second: 116.1
- input_tokens: 4784 | output_tokens: 3099

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

Implementa **reintentos limitados**, con espera creciente y aleatoria (*exponential backoff + jitter*). Respeta `Retry-After` si la respuesta lo incluye; no reintentes en un bucle inmediato.

Ejemplo en Python con `requests`:

```python
import random
import time
import requests

MAX_ATTEMPTS = 5  # incluye la llamada inicial

def call_openrouter(payload, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    for attempt in range(MAX_ATTEMPTS):
        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=(5, 60),  # conexión, respuesta
            )
        except (requests.Timeout, requests.ConnectionError):
            if attempt == MAX_ATTEMPTS - 1:
                raise
            delay = min(30, 2 ** attempt) + random.uniform(0, 1)
            time.sleep(delay)
            continue

        # Solo reintenta errores que podrían ser temporales.
        if response.status_code not in (429, 500, 502, 503, 504):
            response.raise_for_status()
            return response.json()

        if attempt == MAX_ATTEMPTS - 1:
            response.raise_for_status()

        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                delay = float(retry_after)
            except ValueError:
                delay = min(30, 2 ** attempt) + random.uniform(0, 1)
        else:
            delay = min(30, 2 ** attempt) + random.uniform(0, 1)

        time.sleep(delay)

    raise RuntimeError("Se agotaron los reintentos")
```

Puntos importantes:

- `MAX_ATTEMPTS = 5` significa **como máximo cinco llamadas**, no cinco reintentos más la inicial.
- No reintentes errores como `400`, `401`, `402` o `403`: normalmente requieren corregir la petición, la clave o la cuenta.
- Si el `429` persiste, detente y revisa el cuerpo de la respuesta: puede indicar un límite temporal, pero también un límite de cuenta, modelo o proveedor. No aumentes los reintentos para solucionarlo.
- Si varias partes de tu programa pueden llamar a la API, limita también la **concurrencia**; de lo contrario, cada una podría reintentar a la vez.
- Un timeout puede ocurrir después de que el servidor haya procesado la petición. Reintentar en ese caso podría generar una segunda ejecución; tenlo en cuenta si la operación tiene coste o efectos secundarios.