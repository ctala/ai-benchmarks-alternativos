# GPT-6.1 Terra — multi_turn/debugging_conversation

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 14.904s | tokens_per_second: 81.6
- input_tokens: 312 | output_tokens: 1216

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

El loop explica por qué el problema se perpetúa: cada 429 genera más tráfico y puede prolongar la limitación. Primero detén ese proceso para cortar la ráfaga.

También corrijo mi respuesta anterior: **no debí afirmar un límite de 300 RPM**. Los límites pueden depender del modelo, el proveedor y la cuenta; tener saldo tampoco garantiza que una llamada no reciba un 429.

Para los retries, usa estos principios:

- Limita los intentos: por ejemplo, **1 llamada inicial + 3 reintentos**.
- Para errores temporales, usa **espera exponencial con aleatoriedad** (*jitter*).
- Si llega el header `Retry-After`, respétalo.
- No reintentes errores como 400, 401 o 403 sin corregir la causa.
- Define un timeout y evita tener retries activos en varias capas a la vez.

Ejemplo en Python con `requests`:

```python
import os
import random
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

import requests

URL = "https://openrouter.ai/api/v1/chat/completions"
MAX_ATTEMPTS = 4  # 1 intento inicial + hasta 3 retries
MAX_WAIT = 60     # No esperar automáticamente más de 60 segundos

def retry_after_seconds(value):
    """Interpreta Retry-After en segundos o como fecha HTTP."""
    if not value:
        return None

    try:
        return max(0, float(value))
    except ValueError:
        try:
            date = parsedate_to_datetime(value)
            if date.tzinfo is None:
                date = date.replace(tzinfo=timezone.utc)
            return max(0, (date - datetime.now(timezone.utc)).total_seconds())
        except (TypeError, ValueError, OverflowError):
            return None

def call_openrouter(messages):
    headers = {
        "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "deepseek/deepseek-chat",
        "messages": messages,
    }

    for attempt in range(MAX_ATTEMPTS):
        try:
            response = requests.post(
                URL, headers=headers, json=payload, timeout=30
            )
        except (requests.Timeout, requests.ConnectionError):
            if attempt == MAX_ATTEMPTS - 1:
                raise
            delay = random.uniform(0, min(2 ** attempt, MAX_WAIT))
        else:
            if response.ok:
                return response.json()

            retryable = response.status_code in (429, 500, 502, 503, 504)
            if not retryable or attempt == MAX_ATTEMPTS - 1:
                response.raise_for_status()

            delay = retry_after_seconds(response.headers.get("Retry-After"))
            if delay is None:
                delay = random.uniform(0, min(2 ** attempt, MAX_WAIT))

            if delay > MAX_WAIT:
                # No reintentar antes de lo indicado por el servidor.
                response.raise_for_status()

        time.sleep(delay)

result = call_openrouter([{"role": "user", "content": "Hola"}])
print(result)
```

Si ejecutas varias llamadas en paralelo, limita también la concurrencia: cada llamada puede tener pocos retries, pero juntas aún pueden producir una ráfaga. Y ten en cuenta que, tras un timeout, la solicitud podría haberse procesado aunque no hayas recibido la respuesta; reintentar podría duplicar trabajo o cargos.

Si después de detener el loop sigues recibiendo 429 en una sola llamada, comparte el **cuerpo del error y los headers relevantes**, ocultando tu API key, para distinguir si el límite viene de OpenRouter o del proveedor del modelo.