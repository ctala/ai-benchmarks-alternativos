# GPT-6 Luna — multi_turn/debugging_conversation

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.24 | quality: 10.0
- latency_total: 8.838s | tokens_per_second: 100.8
- input_tokens: 312 | output_tokens: 891

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

Usa **reintentos limitados**, con espera creciente y algo de aleatoriedad. Para empezar: 4 intentos en total (la llamada inicial + 3 reintentos), y luego devuelve el error en vez de seguir intentando.

Reglas prácticas:

- Reintenta `429` y errores temporales `5xx`.
- Si la respuesta trae `Retry-After`, respétalo.
- Si no, espera, por ejemplo, 1, 2 y 4 segundos, con una pequeña variación aleatoria.
- No reintentes errores permanentes como `400`, `401` o `402`.
- Si el `429` sigue ocurriendo, revisa el cuerpo de la respuesta: puede indicar un límite de uso o un problema de cuota/créditos, no solo demasiadas solicitudes.

Ejemplo en Python con `requests`:

```python
import random
import time
import requests

MAX_ATTEMPTS = 4

def call_openrouter(payload, headers):
    for attempt in range(MAX_ATTEMPTS):
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=60,
            )
        except requests.RequestException:
            # Error de red: reintentos limitados también.
            if attempt == MAX_ATTEMPTS - 1:
                raise
            delay = min(2 ** attempt, 8) + random.uniform(0, 0.5)
            time.sleep(delay)
            continue

        if response.status_code not in (429, 500, 502, 503, 504):
            response.raise_for_status()
            return response.json()

        if attempt == MAX_ATTEMPTS - 1:
            # Conserva el cuerpo para diagnosticar la causa concreta.
            raise RuntimeError(
                f"OpenRouter devolvió {response.status_code}: {response.text}"
            )

        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                delay = float(retry_after)  # Retry-After expresado en segundos
            except ValueError:
                delay = min(2 ** attempt, 8)
        else:
            delay = min(2 ** attempt, 8)

        time.sleep(delay + random.uniform(0, 0.5))
```

Ajusta la lista de errores temporales a lo que indique la respuesta de OpenRouter. Y evita lanzar varios reintentos simultáneos: si tienes varias tareas, limita también la concurrencia. Si me dices qué lenguaje y biblioteca usas, te lo adapto a tu código.