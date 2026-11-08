# Kimi K2.7 Code — multi_turn/debugging_conversation

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 18.701s | tokens_per_second: 61.7
- input_tokens: 384 | output_tokens: 1154

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

Perfecto, encontraste el verdadero culpable. Un retry infinito es el peor enemigo del 429 porque convierte un pequeño rate limit en un ataque masivo a la API. La regla de oro: **no reintentes errores 429 de forma inmediata y agresiva**.

## Principios de un buen retry

1. **Maximo fijo de intentos**: nunca infinito. Tipicamente 3-5.
2. **Backoff exponencial**: espera cada vez mas entre intentos.
3. **Jitter**: agrega aleatoriedad a la espera para evitar thundering herd.
4. **No reintentes todo**: 400, 401, 403, 422 no se reintentan. Solo 429, 5xx y errores de red.
5. **En 429, respeta el header `Retry-After`** si viene.
6. **Circuit breaker opcional**: si falla mucho, deja de intentarlo por un rato.

## Implementacion en Python

```python
import random
import time
import httpx
from openai import OpenAI, APIError, RateLimitError

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-...",
)

MAX_RETRIES = 3
BASE_DELAY = 1.0  # segundos
MAX_DELAY = 60.0

def with_retry(func, *args, **kwargs):
    last_exception = None
    
    for attempt in range(MAX_RETRIES):
        try:
            return func(*args, **kwargs)
        except RateLimitError as e:
            last_exception = e
            
            # Si es el ultimo intento, no esperamos mas
            if attempt == MAX_RETRIES - 1:
                break
            
            # Intentar obtener Retry-After del header (en segundos)
            retry_after = None
            if hasattr(e, 'response') and e.response is not None:
                retry_after = e.response.headers.get('retry-after')
            
            if retry_after:
                delay = float(retry_after)
            else:
                # Backoff exponencial con jitter
                delay = min(BASE_DELAY * (2 ** attempt), MAX_DELAY)
                delay = delay * (0.5 + random.random() * 0.5)  # jitter 0.5x - 1.0x
            
            print(f"Rate limit (intento {attempt + 1}/{MAX_RETRIES}). Esperando {delay:.1f}s...")
            time.sleep(delay)
            
        except APIError as e:
            # Errores de cliente (4xx excepto 429) no se reintentan
            if e.status_code and 400 <= e.status_code < 500 and e.status_code != 429:
                raise
            # Otros errores de API: reintentar solo si es 5xx
            if e.status_code and e.status_code >= 500:
                last_exception = e
                if attempt == MAX_RETRIES - 1:
                    break
                delay = min(BASE_DELAY * (2 ** attempt), MAX_DELAY)
                time.sleep(delay * (0.5 + random.random()))
            else:
                raise
        except (httpx.TimeoutException, httpx.NetworkError) as e:
            last_exception = e
            if attempt == MAX_RETRIES - 1:
                break
            delay = min(BASE_DELAY * (2 ** attempt), MAX_DELAY)
            time.sleep(delay * (0.5 + random.random()))
    
    raise last_exception


# Uso
response = with_retry(
    client.chat.completions.create,
    model="deepseek/deepseek-chat",
    messages=[{"role": "user", "content": "Hola"}]
)
```

## Si usas la libreria oficial con retry integrado

La libreria `openai` ya trae retries automaticos, pero **por defecto usa hasta 2 intentos con backoff**. Puedes desactivarlos o configurarlos:

```python
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-...",
    max_retries=2,  # numero de reintentos automaticos
    timeout=30,
)
```

Pero cuidado: los retries automaticos de la libreria no respetan bien `Retry-After` en todos los casos. Para control total, usa tu propia funcion como la de arriba.

## Verificacion importante

Antes de corregir tu codigo, haz una pausa de 1-2 minutos. Es posible que OpenRouter haya temporalmente bloqueado o reducido tu rate limit por el bombardeo de requests. Despues de implementar el retry correcto, las 5 requests/min originales deberian funcionar sin problemas.

Dime en que lenguaje/framework estas escribiendo tu codigo y te doy una version mas especifica.