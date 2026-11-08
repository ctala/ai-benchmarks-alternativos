# Claude Fable 5.1 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 8.02 | quality: 10.0
- latency_total: 18.067s | tokens_per_second: 81.3
- input_tokens: 541 | output_tokens: 1469

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

Bien, encontraste la causa raíz: un retry infinito sin espera convierte un 429 en una tormenta de requests que te mantiene bloqueado. Es un patrón muy común. La solución tiene tres piezas:

## Principios de un retry correcto

1. **Límite de intentos** – nunca infinito. 3-5 reintentos es lo típico.
2. **Backoff exponencial** – espera 1s, 2s, 4s, 8s... entre intentos. Así le das tiempo al rate limit para resetearse.
3. **Jitter** – añade un poco de aleatoriedad a la espera para que múltiples clientes no reintenten todos al mismo tiempo.
4. **Respetar `Retry-After`** – si el servidor te dice cuánto esperar, hazle caso.
5. **Solo reintentar errores recuperables** – 429, 500, 502, 503, 504 y errores de red. Un 400 o 401 no se arregla reintentando.

## Ejemplo en Python

```python
import time
import random
import requests

RETRYABLE_STATUS = {429, 500, 502, 503, 504}

def call_openrouter(payload, api_key, max_retries=5, base_delay=1.0, max_delay=60.0):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=60)
        except requests.exceptions.RequestException as e:
            if attempt == max_retries:
                raise
            delay = min(base_delay * (2 ** attempt), max_delay)
            delay += random.uniform(0, delay * 0.3)  # jitter
            print(f"Error de red ({e}), reintentando en {delay:.1f}s...")
            time.sleep(delay)
            continue

        if resp.status_code == 200:
            return resp.json()

        if resp.status_code not in RETRYABLE_STATUS:
            # Error no recuperable: no reintentar
            resp.raise_for_status()

        if attempt == max_retries:
            raise RuntimeError(f"Fallo tras {max_retries} reintentos: {resp.status_code} {resp.text}")

        # Respetar Retry-After si viene
        retry_after = resp.headers.get("Retry-After")
        if retry_after:
            delay = float(retry_after)
        else:
            delay = min(base_delay * (2 ** attempt), max_delay)
            delay += random.uniform(0, delay * 0.3)

        print(f"HTTP {resp.status_code}, reintento {attempt + 1}/{max_retries} en {delay:.1f}s...")
        time.sleep(delay)
```

## Si usas el SDK de OpenAI (compatible con OpenRouter)

Ya trae retries con backoff incorporados, solo configúralos:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
    max_retries=3,   # por defecto son 2
    timeout=60,
)
```

Si eliges esta opción, **quita tu loop de retry manual** — si no, tendrás retries anidados (3 × tus N intentos).

## Dos cosas más que te recomiendo

- **Pre-throttling**: si sabes que vas a hacer varias llamadas seguidas, añade un pequeño `sleep` entre ellas o usa un semáforo/token bucket. Es mejor no llegar al 429 que recuperarse de él.
- **Logging**: registra cada reintento con el código de error y el tiempo de espera. Así la próxima vez verás el problema en segundos en lugar de tener que buscarlo.

¿En qué lenguaje está tu código? Si no es Python te adapto el ejemplo.