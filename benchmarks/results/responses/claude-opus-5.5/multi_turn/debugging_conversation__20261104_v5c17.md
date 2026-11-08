# Claude Opus 5.5 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 20.345s | tokens_per_second: 107.8
- input_tokens: 541 | output_tokens: 2193

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

Encontraste la causa: un retry infinito genera una **tormenta de reintentos**. Cada 429 produce más requests, lo que produce más 429, y nunca sales del límite.

Antes de seguir, una corrección: te dije que el límite era 300 RPM y no debí afirmarlo con tanta seguridad. Los límites de OpenRouter dependen del tipo de cuenta y del modelo, y además **el 429 puede venir del proveedor upstream** (el servidor que realmente corre DeepSeek), no de OpenRouter. Revisa la documentación actual de OpenRouter para los números exactos. Eso no cambia el diagnóstico, pero no quiero que te bases en una cifra incorrecta.

## Cómo implementar retries correctamente

Una buena estrategia de reintentos sigue 5 reglas:

1. **Límite máximo de intentos** (3-5 es razonable)
2. **Backoff exponencial**: esperar 1s, 2s, 4s, 8s...
3. **Jitter**: añadir aleatoriedad para que varios procesos no reintenten al mismo tiempo
4. **Respetar el header `Retry-After`** si el servidor lo envía
5. **Solo reintentar errores transitorios**: 429, 5xx y timeouts. Nunca 400, 401 o 402.

### Ejemplo en Python

```python
import time
import random
import requests

RETRYABLE_STATUS = {429, 500, 502, 503, 504}

def call_openrouter(payload, api_key, max_retries=4, base_delay=1.0, max_delay=30.0):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}

    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=60)
        except (requests.Timeout, requests.ConnectionError) as e:
            if attempt == max_retries:
                raise
            delay = min(max_delay, base_delay * 2 ** attempt) + random.uniform(0, 1)
            print(f"Error de red ({e}), reintento {attempt + 1} en {delay:.1f}s")
            time.sleep(delay)
            continue

        if resp.ok:
            return resp.json()

        # Errores no recuperables: fallar inmediatamente
        if resp.status_code not in RETRYABLE_STATUS:
            raise RuntimeError(f"Error {resp.status_code}: {resp.text}")

        if attempt == max_retries:
            raise RuntimeError(f"Agotados los reintentos. Último error {resp.status_code}: {resp.text}")

        # Respetar Retry-After si existe
        retry_after = resp.headers.get("Retry-After")
        if retry_after and retry_after.isdigit():
            delay = float(retry_after)
        else:
            delay = min(max_delay, base_delay * 2 ** attempt) + random.uniform(0, 1)

        print(f"Status {resp.status_code}, reintento {attempt + 1}/{max_retries} en {delay:.1f}s")
        time.sleep(delay)
```

### Alternativa con `tenacity` (más limpia)

```python
from tenacity import retry, stop_after_attempt, wait_random_exponential, retry_if_exception_type

class RetryableError(Exception):
    pass

@retry(
    retry=retry_if_exception_type(RetryableError),
    wait=wait_random_exponential(multiplier=1, max=30),
    stop=stop_after_attempt(5),
    reraise=True,
)
def call_api(payload):
    resp = requests.post(URL, json=payload, headers=HEADERS, timeout=60)
    if resp.status_code in {429, 500, 502, 503, 504}:
        raise RetryableError(f"{resp.status_code}: {resp.text}")
    resp.raise_for_status()
    return resp.json()
```

## Errores comunes a revisar

- **Retries duplicados**: si usas el SDK de `openai` apuntando a OpenRouter, el cliente **ya reintenta automáticamente** (2 veces por defecto). Si además tienes tu propio loop, los intentos se multiplican. Usa uno u otro, por ejemplo `OpenAI(base_url=..., max_retries=0)` si prefieres tu lógica.
- **Lee el cuerpo del error**: el JSON del 429 suele indicar si el límite es de OpenRouter o del proveedor. Si es del proveedor, puedes configurar fallback a otros proveedores en las opciones de routing de OpenRouter.
- **Concurrencia**: si tienes varios workers o hilos, cada uno con sus retries, considera un semáforo o una cola para limitar las requests simultáneas.

## Siguiente paso

1. Elimina el loop infinito y pon la versión con límite.
2. Espera unos minutos para que se limpie el rate limit acumulado.
3. Haz una sola request de prueba y mira si funciona.

Si después de esto sigues recibiendo 429 con solo 5 req/min, pégame el cuerpo completo de la respuesta de error y vemos de dónde viene el límite.