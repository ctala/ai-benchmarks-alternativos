# Claude Haiku 5.5 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.0 | quality: 10.0
- latency_total: 10.345s | tokens_per_second: 214.2
- input_tokens: 541 | output_tokens: 2216

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

Antes de implementar los retries, detén el loop para que no siga consumiendo cuota. Y una corrección: te di "300 RPM" como si fuera un dato fijo, pero no lo es. Los límites de OpenRouter dependen del modelo, de tu cuenta y del proveedor upstream, así que no debes asumir un número concreto. Los headers de la respuesta son la fuente más fiable.

## Cómo debe funcionar un retry bien hecho

- **Límite máximo de intentos**, para que nunca sea infinito.
- **Backoff exponencial**: esperar más en cada intento (2s, 4s, 8s...).
- **Respetar `Retry-After`** si el servidor lo envía.
- **Jitter** (un poco de aleatoriedad) para no reintentar todos a la vez.
- **Reintentar solo errores temporales** (429, 5xx). Un 400 o 401 no se arregla reintentando.

## Ejemplo en Python

```python
import os
import random
import time
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MAX_RETRIES = 5
BASE_DELAY = 2      # segundos
MAX_DELAY = 60      # tope de espera entre intentos

RETRYABLE = {429, 500, 502, 503, 504}

def call_openrouter(payload: dict) -> dict:
    headers = {
        "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
        "Content-Type": "application/json",
    }

    for attempt in range(MAX_RETRIES + 1):
        resp = requests.post(API_URL, headers=headers, json=payload, timeout=60)

        if resp.status_code == 200:
            return resp.json()

        # Error no recuperable (400, 401, 403...): fallar de inmediato
        if resp.status_code not in RETRYABLE:
            resp.raise_for_status()

        # Se agotaron los intentos
        if attempt == MAX_RETRIES:
            raise RuntimeError(
                f"Fallo tras {MAX_RETRIES} reintentos (último status: {resp.status_code})"
            )

        # Calcular espera: Retry-After si existe, si no backoff exponencial
        retry_after = resp.headers.get("Retry-After")
        if retry_after and retry_after.isdigit():
            delay = float(retry_after)
        else:
            delay = min(MAX_DELAY, BASE_DELAY * (2 ** attempt))

        delay += random.uniform(0, 1)  # jitter
        print(f"[{resp.status_code}] reintento {attempt + 1}/{MAX_RETRIES} en {delay:.1f}s")
        time.sleep(delay)

    raise RuntimeError("Inalcanzable")
```

Uso:

```python
result = call_openrouter({
    "model": "deepseek/deepseek-chat",
    "messages": [{"role": "user", "content": "Hola"}],
})
print(result["choices"][0]["message"]["content"])
```

## Para diagnosticar después

1. **Loguea los headers `x-ratelimit-*` y `Retry-After`** en cada 429. Te dirán qué límite estás tocando.
2. **Revisa el cuerpo del error.** OpenRouter suele indicar si el 429 viene del proveedor upstream (DeepSeek congestionado) o de tu cuenta. En ese caso, probar más tarde o usar otro proveedor puede ser la solución, no reducir requests.
3. **Asegúrate de que no haya dos procesos** (o dos contenedores) usando la misma key.

Si quieres, comparte el código del loop original y te ayudo a integrar este patrón en él.