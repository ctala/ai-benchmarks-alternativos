# Bonsai 2 27B — multi_turn/debugging_conversation

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 8.65 | quality: 10.0
- latency_total: 66.545s | tokens_per_second: 44.3
- input_tokens: 386 | output_tokens: 2951

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



El problema principal es que tu **retry loop infinito convierte un 429 en una tormenta de requests**. Para arreglarlo bien, no debes reintentar de forma infinita ni con delay fijo.

## Cómo deberían ir los retries

Para un error **429** en OpenRouter, lo recomendado es:

1. **No reintentar infinitamente**
   - Máximo 3 a 5 intentos.
   - Si sigue fallando, para y reporta el error.

2. **Usar exponential backoff**
   - Espera más tiempo después de cada intento.
   - Ejemplo: 1s → 2s → 4s → 8s → 16s

3. **Agregar jitter**
   - Evita que varios workers/retries golpeen la API al mismo tiempo.
   - Ejemplo: esperar 1.2s, 2.8s, 4.1s, etc.

4. **Respetar `Retry-After` si existe**
   - Si la respuesta trae `Retry-After`, úsalo.
   - Suele indicar cuánto esperar antes de reintentar.

5. **No reintentar todos los errores**
   - Reintentar normalmente solo:
     - `429 Too Many Requests`
     - `502`
     - `503`
     - `504`
     - timeouts / errores de red
   - No reintentar:
     - `400`
     - `401`
     - `403`
     - `404`
     - `422`
     - errores de validación

6. **Poner timeout en la request**
   - Si no pones timeout, tu código puede quedarse colgado y multiplicar el problema.

7. **Limitar concurrencia**
   - Si haces muchos requests en paralelo, limita el número de peticiones simultáneas.
   - En tu caso, 5 por minuto es muy bajo, así que probablemente solo falta quitar el retry infinito.

---

## Ejemplo correcto en Python

Aquí tienes una versión simple y robusta:

```python
import random
import time
import httpx


def call_openrouter(
    url: str,
    headers: dict,
    payload: dict,
    max_attempts: int = 4,
    base_delay: float = 1.0,
    max_delay: float = 30.0,
    timeout: float = 30.0
):
    last_error = None

    for attempt in range(max_attempts):
        try:
            response = httpx.post(
                url=url,
                headers=headers,
                json=payload,
                timeout=timeout
            )

            # 429: Too Many Requests
            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After")

                if retry_after:
                    try:
                        delay = float(retry_after)
                    except ValueError:
                        delay = min(max_delay, base_delay * (2 ** attempt))
                else:
                    delay = min(max_delay, base_delay * (2 ** attempt))

                # Jitter: agrega un poco de aleatoriedad
                delay += random.uniform(0, delay * 0.2)

                if attempt == max_attempts - 1:
                    raise RuntimeError(
                        f"Rate limit exceeded after {max_attempts} attempts"
                    )

                time.sleep(delay)
                continue

            # Otros errores HTTP
            if response.status_code >= 400:
                raise httpx.HTTPStatusError(
                    f"HTTP {response.status_code}",
                    request=response.request,
                    response=response
                )

            return response.json()

        except httpx.HTTPStatusError as exc:
            last_error = exc

            # Reintentar solo errores temporales
            if exc.response.status_code in (429, 502, 503, 504):
                if attempt == max_attempts - 1:
                    raise

                delay = min(max_delay, base_delay * (2 ** attempt))
                delay += random.uniform(0, 1.0)
                time.sleep(delay)
                continue

            # Si es 4xx permanente, no reintentar
            raise

        except (httpx.TimeoutException, httpx.ConnectError, httpx.NetworkError) as exc:
            last_error = exc

            if attempt == max_attempts - 1:
                raise

            delay = min(max_delay, base_delay * (2 ** attempt))
            delay += random.uniform(0, 1.0)
            time.sleep(delay)
            continue

    raise last_error
```

---

## Ejemplo de uso

```python
url = "https://api.openrouter.ai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "deepseek/deepseek-v3",
    "messages": [
        {
            "role": "user",
            "content": "Hola"
        }
    ],
    "max_tokens": 100
}

try:
    result = call_openrouter(url, headers, payload)
    print(result["choices"][0]["message"]["content"])
except Exception as e:
    print("Error:", e)
```

---

## Si usas un SDK

Si estás usando el SDK oficial de OpenAI u OpenRouter, revisa que no tengas un loop propio encima.

Lo ideal es:

```python
client = OpenAI(
    base_url="https://api.openrouter.ai/v1",
    api_key=api_key
)
```

Y si el SDK permite configurar retries:

```python
client = OpenAI(
    base_url="https://api.openrouter.ai/v1",
    api_key=api_key,
    max_retries=3
)
```

Pero si el SDK ya hace retries y tú también haces un `while True`, eso es lo que está multiplicando las peticiones.

---

## Regla práctica

Para tu caso, con **5 requests por minuto** y **DeepSeek V3**, un retry correcto debería ser:

- Máximo **3 o 4 intentos**
- Delay inicial: **1 segundo**
- Delay máximo: **15 o 30 segundos**
- Jitter: **sí**
- Respetar `Retry-After`: **sí**
- Timeout: **30 segundos**

Con eso no deberías generar 100 requests extra por cada 429.

---

## Lo que debes cambiar ahora mismo

Tu código probablemente se parece a esto:

```python
while True:
    response = make_request()
    if response.status_code == 429:
        continue
    return response
```

O algo similar.

Cámbialo por algo con:

- contador de intentos
- backoff exponencial
- jitter
- `Retry-After`
- timeout

---

Si me pegas el fragmento de código donde estás haciendo la llamada y el retry, te lo dejo corregido exactamente para tu caso.