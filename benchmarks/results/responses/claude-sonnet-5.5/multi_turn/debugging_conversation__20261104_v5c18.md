# Claude Sonnet 5.5 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 14.957s | tokens_per_second: 134.8
- input_tokens: 541 | output_tokens: 2016

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

Ese loop explica el problema: cada 429 dispara más requests, que generan más 429, y nunca sales. Además, corrijo algo: dije que el límite de DeepSeek era 300 RPM, pero no lo tengo confirmado, así que no te fíes de ese número. Lo importante es que el 429 puede venir también del proveedor upstream, no solo de OpenRouter.

## Primero, apaga el loop
Detén el proceso y espera unos minutos para que se enfríe el rate limit. Si lo dejas corriendo, seguirás bloqueado.

## Reglas para un buen retry

1. **Máximo de intentos** (3-5), nunca infinito.
2. **Exponential backoff**: esperar 1s, 2s, 4s, 8s...
3. **Jitter**: aleatoriedad en la espera para no sincronizar reintentos.
4. **Respetar el header `Retry-After`** si viene en la respuesta.
5. **Reintentar solo errores transitorios**: 408, 429, 5xx y timeouts. Los 400, 401, 402 y 403 no se arreglan reintentando.

## Ejemplo en Python

```python
import random
import time
import requests

URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}
RETRYABLE = {408, 429, 500, 502, 503, 504}

session = requests.Session()  # reutiliza la conexión

def call_with_retry(payload, max_retries=5, base=1.0, cap=60.0):
    for attempt in range(max_retries + 1):
        r = None
        try:
            r = session.post(URL, json=payload, headers=HEADERS, timeout=60)
            if r.status_code == 200:
                return r.json()
            if r.status_code not in RETRYABLE:
                r.raise_for_status()  # error no recuperable: falla ya
        except (requests.ConnectionError, requests.Timeout):
            pass  # error de red: se reintenta

        if attempt == max_retries:
            raise RuntimeError(f"Falló tras {max_retries + 1} intentos")

        # backoff exponencial con full jitter
        delay = random.uniform(0, min(cap, base * 2 ** attempt))

        # respetar Retry-After si existe
        if r is not None and "Retry-After" in r.headers:
            try:
                delay = max(delay, float(r.headers["Retry-After"]))
            except ValueError:
                pass

        print(f"Intento {attempt + 1} falló, reintentando en {delay:.1f}s")
        time.sleep(delay)
```

## Mejoras opcionales
- **Librería `tenacity`**: hace lo mismo con decoradores y menos código.
- **Limitador del lado cliente**: si procesas muchas requests, usa un semáforo o token bucket para no pasarte de X req/min desde el origen.
- **Circuit breaker**: si fallan N llamadas seguidas, pausa todo durante un rato en vez de seguir intentando.

¿Qué lenguaje usas? Si no es Python, te lo adapto. Si tras arreglar el loop y esperar sigues viendo 429, pásame el body de la respuesta, porque suele indicar si el límite viene de OpenRouter o del proveedor.