# Claude Haiku 5.5 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 8.802s | tokens_per_second: 216.9
- input_tokens: 541 | output_tokens: 1909

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

Primero, **detén el loop**. Mientras siga activo, cada 429 seguirá generando más requests y tu cuenta no podrá recuperarse.

También debo corregir algo: dije que el límite de DeepSeek en OpenRouter es 300 RPM, y no tengo certeza de ese número. Los límites de OpenRouter dependen del modelo, del proveedor y de tu cuenta, así que conviene revisar la documentación actual o los headers de respuesta. Además, un 429 puede venir del proveedor upstream que está saturado, no solo de tu cuenta, y en ese caso reintentar agresivamente empeora las cosas.

## Cómo implementar los reintentos bien

Estas son las reglas:

1. **Limita el número de intentos** (3 a 5 es suficiente).
2. **Usa backoff exponencial con jitter**: cada espera es más larga que la anterior, con un componente aleatorio para que varios clientes no reintenten al mismo tiempo.
3. **Respeta el header `Retry-After`** si viene en la respuesta.
4. **Reintenta solo errores temporales** (429, 500, 502, 503, 504 y timeouts). No reintentes 400, 401 o 403, porque fallarán igual.

### Ejemplo en Python

```python
import os
import time
import random
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ["OPENROUTER_API_KEY"]

RETRYABLE_STATUS = {429, 500, 502, 503, 504}
MAX_RETRIES = 4
BASE_DELAY = 1.0   # segundos
MAX_DELAY = 30.0   # tope de espera

def call_openrouter(payload: dict) -> dict:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    for attempt in range(MAX_RETRIES + 1):
        try:
            resp = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        except requests.RequestException as e:
            # Error de red o timeout
            if attempt == MAX_RETRIES:
                raise
            wait = min(MAX_DELAY, BASE_DELAY * 2 ** attempt) + random.uniform(0, 1)
            print(f"Error de red ({e}). Reintento {attempt + 1} en {wait:.1f}s")
            time.sleep(wait)
            continue

        if resp.status_code == 200:
            return resp.json()

        if resp.status_code not in RETRYABLE_STATUS or attempt == MAX_RETRIES:
            # Error no reintentable o se agotaron los intentos
            resp.raise_for_status()

        # Calcular espera: Retry-After si existe, si no backoff exponencial
        retry_after = resp.headers.get("Retry-After")
        if retry_after and retry_after.isdigit():
            wait = float(retry_after)
        else:
            wait = min(MAX_DELAY, BASE_DELAY * 2 ** attempt)
        wait += random.uniform(0, 1)  # jitter

        print(f"HTTP {resp.status_code}. Reintento {attempt + 1} en {wait:.1f}s")
        time.sleep(wait)

    raise RuntimeError("Se agotaron los reintentos")
```

### Puntos clave

- El `for` tiene un número fijo de iteraciones, así que nunca es infinito.
- Cada reintento espera más (1s, 2s, 4s, 8s...), lo que da tiempo a que se libere el límite.
- Si tu código usa un `while True` o un retry recursivo sin contador, ese era probablemente el origen del problema.

### Verificación

Después de corregirlo, prueba con una sola llamada y registra los headers de respuesta (especialmente `x-ratelimit-*` y `Retry-After`). Así verás los límites reales de tu cuenta y modelo, en lugar de adivinarlos.

Si me muestras tu código actual del loop, puedo indicarte exactamente dónde cambiarlo.