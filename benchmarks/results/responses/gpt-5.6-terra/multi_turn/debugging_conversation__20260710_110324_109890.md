# GPT-5.6 Terra — multi_turn/debugging_conversation

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.07 | quality: 9.55
- latency_total: 11.522s | tokens_per_second: 148.6
- input_tokens: 312 | output_tokens: 1712
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y prácticamente útil, abordando directamente el problema del error 429 con una solución detallada y bien estructurada.

## Respuesta completa

El problema es un **retry storm**: recibes un 429, reintentas inmediatamente, generas más 429 y el bucle se retroalimenta.

Implementa estas reglas:

1. **Máximo de reintentos**: por ejemplo 3 a 5, nunca infinito.
2. **Backoff exponencial**: espera cada vez más (`1s`, `2s`, `4s`, `8s`...).
3. **Jitter aleatorio**: añade una variación para evitar que varios procesos reintenten a la vez.
4. **Respeta `Retry-After`** si OpenRouter lo devuelve; tiene prioridad sobre tu cálculo.
5. **Reintenta solo errores transitorios**:
   - Sí: `429`, `500`, `502`, `503`, `504`, errores de red/timeouts.
   - No: `400`, `401`, `403`, `404`, `422`, etc. Son errores de request/configuración.
6. Tras agotar los intentos, falla de forma controlada y registra el error.

## Ejemplo en Python

```python
import random
import time
import requests

RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}
MAX_RETRIES = 4

def get_retry_delay(response, attempt):
    # Si el servidor indica cuánto esperar, respetarlo.
    retry_after = response.headers.get("Retry-After")
    if retry_after:
        try:
            return float(retry_after)
        except ValueError:
            pass

    # Backoff exponencial: 1, 2, 4, 8 segundos
    base_delay = 2 ** attempt

    # Jitter de hasta 25%; evita reintentos sincronizados.
    jitter = random.uniform(0, base_delay * 0.25)

    return base_delay + jitter


def call_openrouter(payload, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    last_error = None

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=60,
            )

            if response.ok:
                return response.json()

            # No reintentar errores permanentes.
            if response.status_code not in RETRYABLE_STATUS_CODES:
                raise RuntimeError(
                    f"Error no reintentable {response.status_code}: {response.text}"
                )

            last_error = RuntimeError(
                f"OpenRouter respondió {response.status_code}: {response.text}"
            )

            # Ya no quedan reintentos.
            if attempt == MAX_RETRIES:
                break

            delay = get_retry_delay(response, attempt)

            print(
                f"Intento {attempt + 1}/{MAX_RETRIES}: "
                f"status={response.status_code}. Reintentando en {delay:.2f}s..."
            )
            time.sleep(delay)

        except (requests.Timeout, requests.ConnectionError) as exc:
            last_error = exc

            if attempt == MAX_RETRIES:
                break

            delay = (2 ** attempt) + random.uniform(0, 0.5)
            print(f"Error de red. Reintentando en {delay:.2f}s...")
            time.sleep(delay)

    raise RuntimeError(
        f"No se pudo completar la llamada tras {MAX_RETRIES + 1} intentos"
    ) from last_error
```

Uso:

```python
result = call_openrouter(
    payload={
        "model": "deepseek/deepseek-chat",
        "messages": [
            {"role": "user", "content": "Hola"}
        ],
    },
    api_key="TU_API_KEY",
)
```

## Ejemplo en JavaScript / Node.js

```js
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

function getRetryDelay(response, attempt) {
  const retryAfter = response.headers.get("retry-after");

  if (retryAfter && !Number.isNaN(Number(retryAfter))) {
    return Number(retryAfter) * 1000;
  }

  const baseMs = 1000 * (2 ** attempt); // 1s, 2s, 4s, 8s
  const jitterMs = Math.random() * baseMs * 0.25;

  return baseMs + jitterMs;
}

async function callOpenRouter(payload, apiKey, maxRetries = 4) {
  const retryableStatuses = new Set([429, 500, 502, 503, 504]);
  let lastError;

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(
        "https://openrouter.ai/api/v1/chat/completions",
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${apiKey}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        }
      );

      if (response.ok) {
        return await response.json();
      }

      const body = await response.text();

      if (!retryableStatuses.has(response.status)) {
        throw new Error(`Error no reintentable ${response.status}: ${body}`);
      }

      lastError = new Error(`OpenRouter ${response.status}: ${body}`);

      if (attempt === maxRetries) break;

      const delay = getRetryDelay(response, attempt);
      console.warn(
        `Intento ${attempt + 1}/${maxRetries}; ` +
        `status=${response.status}. Esperando ${Math.round(delay)} ms`
      );

      await sleep(delay);
    } catch (error) {
      // No reintentes errores explícitamente marcados como permanentes.
      if (error.message?.startsWith("Error no reintentable")) {
        throw error;
      }

      lastError = error;

      if (attempt === maxRetries) break;

      const delay = 1000 * (2 ** attempt) + Math.random() * 500;
      await sleep(delay);
    }
  }

  throw new Error(
    `La llamada falló después de ${maxRetries + 1} intentos`,
    { cause: lastError }
  );
}
```

## Además: limita la concurrencia

Aunque tú inicies “5 requests por minuto”, un worker, una cola o varios usuarios pueden dispararlas simultáneamente. Pon un límite de concurrencia, por ejemplo 1–3 llamadas activas por API key/modelo.

La idea es:

```text
429 → esperar Retry-After o backoff → reintentar pocas veces
429 repetido → dejar de intentar → devolver error / encolar para más tarde
```

No hagas:

```python
while True:
    try:
        return call_api()
    except Exception:
        pass  # Esto genera una tormenta de requests
```

Y registra siempre: código HTTP, número de intento, espera aplicada y headers `Retry-After` / `x-ratelimit-*`. Eso permite distinguir un rate limit real de un fallo de autenticación, saldo, proveedor o configuración.