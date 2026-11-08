# Mistral Large 3 675B — multi_turn/debugging_conversation

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.92 | quality: 10.0
- latency_total: 6.799s | tokens_per_second: 96.9
- input_tokens: 325 | output_tokens: 659

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

¡Ah, el clásico "retry storm"! Vamos a implementar un sistema de retries robusto pero seguro. Aquí tienes la solución paso a paso:

### 1. **Estructura básica de retry con backoff exponencial**
```python
import time
import random
import requests
from requests.exceptions import RequestException

MAX_RETRIES = 5
INITIAL_DELAY = 1  # segundos
MAX_DELAY = 60     # segundos máximo entre retries

def call_api_with_retry(url, headers, payload):
    retry_count = 0

    while retry_count < MAX_RETRIES:
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Lanza excepción para 4XX/5XX

            # Si es 429, respetamos el retry-after
            if response.status_code == 429:
                retry_after = float(response.headers.get('Retry-After', INITIAL_DELAY))
                time.sleep(retry_after)
                retry_count += 1
                continue

            return response.json()  # Éxito

        except RequestException as e:
            # Backoff exponencial con jitter
            delay = min(INITIAL_DELAY * (2 ** retry_count) + random.uniform(0, 1), MAX_DELAY)
            print(f"Intento {retry_count + 1} falló. Reintentando en {delay:.2f}s...")
            time.sleep(delay)
            retry_count += 1

    raise Exception(f"Fallo después de {MAX_RETRIES} intentos")
```

### 2. **Cómo usarlo con OpenRouter**
```python
url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {YOUR_API_KEY}",
    "Content-Type": "application/json"
}
payload = {
    "model": "deepseek/deepseek-chat",
    "messages": [{"role": "user", "content": "Hola"}]
}

try:
    result = call_api_with_retry(url, headers, payload)
    print(result)
except Exception as e:
    print(f"Error final: {e}")
```

### 3. **Claves del sistema**:
- **Backoff exponencial**: `delay = initial_delay * (2^retry_count)`
- **Jitter**: `random.uniform(0, 1)` evita que todos los clientes reintenten al mismo tiempo
- **Respeto a Retry-After**: Si OpenRouter devuelve `Retry-After: 10`, esperamos 10 segundos
- **Límite de retries**: Máximo 5 intentos (ajustable)

### 4. **Para casos avanzados**:
Si usas asyncio:
```python
import asyncio

async def async_call_with_retry(url, headers, payload):
    # Similar a la versión síncrona pero con asyncio.sleep()
    pass
```

¿Necesitas que adapte este código a algún lenguaje/framework específico?