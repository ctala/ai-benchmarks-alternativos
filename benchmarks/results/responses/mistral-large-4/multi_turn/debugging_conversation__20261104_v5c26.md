# Mistral Large 4.0 — multi_turn/debugging_conversation

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 30.259s | tokens_per_second: 89.5
- input_tokens: 310 | output_tokens: 2708

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

Eso confirma el diagnóstico: tienes un **"retry storm"** (tormenta de reintentos). Cada 429 genera 100 requests más, que generan más 429s, y OpenRouter te bloquea más agresivamente.

Aquí tienes la implementación correcta con **exponential backoff + jitter** y respeto al header `Retry-After`:

## 1. Código robusto (Python async con `httpx`)

```python
import asyncio
import random
import httpx
from typing import Optional

API_KEY = "tu-api-key"
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

async def call_with_retry(
    client: httpx.AsyncClient,
    payload: dict,
    max_retries: int = 4,
    base_delay: float = 1.0
) -> dict:
    """
    Reintentos inteligentes:
    - Solo reintenta en 429 y 5xx
    - Backoff exponencial con jitter (evita sincronización de clientes)
    - Respeta el header Retry-After si existe
    """
    last_exception = None

    for attempt in range(max_retries + 1):
        try:
            response = await client.post(
                BASE_URL,
                json=payload,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                timeout=30.0
            )

            # Éxito
            if response.status_code == 200:
                return response.json()

            # Rate limit (429) - reintentar con backoff
            if response.status_code == 429:
                if attempt >= max_retries:
                    raise Exception(f"429 persistente después de {max_retries} reintentos. Headers: {dict(response.headers)}")

                # 1. Respetar Retry-After si lo envía el servidor (en segundos)
                retry_after = response.headers.get("retry-after")
                if retry_after:
                    wait_time = float(retry_after)
                    print(f"⏳ Servidor pide esperar {wait_time}s (Retry-After)")
                else:
                    # 2. Backoff exponencial con FULL JITTER (AWS best practice)
                    # wait = random(0, base * 2^attempt)
                    wait_time = random.uniform(0, base_delay * (2 ** attempt))
                    print(f"⏳ 429 recibido. Backoff: {wait_time:.2f}s (intento {attempt + 1}/{max_retries})")

                await asyncio.sleep(wait_time)
                continue

            # Errores de servidor (5xx) - reintentar
            if 500 <= response.status_code < 600:
                if attempt >= max_retries:
                    response.raise_for_status()
                wait_time = random.uniform(0, base_delay * (2 ** attempt))
                print(f"⚠️ Error {response.status_code}. Reintentando en {wait_time:.2f}s...")
                await asyncio.sleep(wait_time)
                continue

            # Otros 4xx (400, 401, 403, etc.) - NO reintentar, es error nuestro
            response.raise_for_status()

        except httpx.RequestError as e:
            # Errores de red (timeout, DNS, etc.)
            last_exception = e
            if attempt >= max_retries:
                raise
            wait_time = random.uniform(0, base_delay * (2 ** attempt))
            print(f"🌐 Error de red: {e}. Reintentando en {wait_time:.2f}s...")
            await asyncio.sleep(wait_time)

    raise Exception(f"Falló después de {max_retries} reintentos") from last_exception

# Uso
async def main():
    async with httpx.AsyncClient() as client:
        payload = {
            "model": "deepseek/deepseek-chat",
            "messages": [{"role": "user", "content": "Hola"}]
        }
        result = await call_with_retry(client, payload)
        print(result)

asyncio.run(main())
```

## 2. Versión síncrona (con `requests`)

Si no usas async, cambia `await asyncio.sleep()` por `time.sleep()` y usa `requests.Session()`:

```python
import time
import random
import requests

def call_sync(payload, max_retries=4):
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {API_KEY}"})

    for attempt in range(max_retries + 1):
        response = session.post(BASE_URL, json=payload, timeout=30)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 429:
            if attempt >= max_retries:
                raise Exception("Max retries alcanzado")

            retry_after = response.headers.get("retry-after")
            wait = float(retry_after) if retry_after else random.uniform(0, 2 ** attempt)
            time.sleep(wait)
            continue

        response.raise_for_status()
```

## 3. Prevención: Rate Limiter local

Para no llegar al límite en primer lugar, limita tus requests localmente (ej: máximo 5 por minuto si tu tier es bajo):

```python
import time
from collections import deque

class RateLimiter:
    def __init__(self, max_calls: int, period: int):
        self.max_calls = max_calls
        self.period = period
        self.calls = deque()

    def wait_if_needed(self):
        now = time.time()
        # Eliminar llamadas fuera de la ventana
        while self.calls and self.calls[0] < now - self.period:
            self.calls.popleft()

        if len(self.calls) >= self.max_calls:
            sleep_time = self.period - (now - self.calls[0])
            if sleep_time > 0:
                print(f"🚦 Rate limit local alcanzado. Esperando {sleep_time:.1f}s...")
                time.sleep(sleep_time)
                self.calls.popleft()

        self.calls.append(time.time())

# Uso: limiter = RateLimiter(max_calls=5, period=60)  # 5 por minuto
```

## 4. Debug: Loggea los headers de rate limit

Añade esto temporalmente para ver qué te dice OpenRouter exactamente:

```python
print(f"Limit: {response.headers.get('x-ratelimit-limit-requests')}")
print(f"Remaining: {response.headers.get('x-ratelimit-remaining-requests')}")
print(f"Reset: {response.headers.get('x-ratelimit-reset-requests')}")
```

## Checklist para arreglar tu código ahora:

1. **Elimina el loop infinito** - pon un `max_retries` (3-5 máximo)
2. **Añade sleep entre reintentos** - mínimo 1s, idealmente exponencial (1s, 2s, 4s, 8s...)
3. **Añade jitter** (`random.uniform`) para que si tienes 10 workers, no todos reintenten al mismo tiempo
4. **No reintentes errores 4xx** (excepto 429) - si te da 400 (bad request), reintentar no ayuda
5. **Respeta `Retry-After`** si viene en la respuesta 429

¿Usas Python, Node.js o otro lenguaje? Te puedo dar el código específico en tu stack si lo prefieres.