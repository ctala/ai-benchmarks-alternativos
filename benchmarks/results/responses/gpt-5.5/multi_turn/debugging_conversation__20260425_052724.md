# GPT-5.5 — multi_turn/debugging_conversation

- model_id: `gpt-5.5`
- success: True  | final: 6.8 | quality: 9.44
- latency_total: 22.755s | tokens_per_second: 101.0
- input_tokens: 312 | output_tokens: 2299
- judge_score: 4.6 | justificación: 

## Respuesta completa

Sí: el problema clásico es que el retry sin límite convierte un 429 en una tormenta de requests.

La regla general:

1. **Nunca hagas retry infinito**
2. **Respeta `Retry-After` si viene en la respuesta**
3. **Usa exponential backoff + jitter**
4. **Pon un máximo de intentos**
5. **Solo reintenta errores recuperables**
6. **Si el error es de autenticación, saldo, request inválida, etc., no reintentes**

---

## Qué errores deberías reintentar

Normalmente sí:

- `429 Too Many Requests`
- `500`
- `502`
- `503`
- `504`
- errores de red / timeout

Normalmente no:

- `400 Bad Request`
- `401 Unauthorized`
- `402 Payment Required`
- `403 Forbidden`
- `404`
- errores de validación del payload

---

## Estrategia recomendada

Ejemplo de tiempos:

```txt
Intento 1: request normal
Intento 2: esperar ~1s
Intento 3: esperar ~2s
Intento 4: esperar ~4s
Intento 5: esperar ~8s
Luego fallar
```

Con jitter:

```txt
delay = backoff + random(0, 1000ms)
```

Esto evita que muchas requests se reintenten exactamente al mismo tiempo.

---

# Ejemplo en JavaScript / TypeScript con `fetch`

```js
const OPENROUTER_API_KEY = process.env.OPENROUTER_API_KEY;

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function getRetryAfterMs(response) {
  const retryAfter = response.headers.get("retry-after");

  if (!retryAfter) return null;

  // Retry-After puede venir como segundos
  const seconds = Number(retryAfter);
  if (!Number.isNaN(seconds)) {
    return seconds * 1000;
  }

  // O como fecha HTTP
  const dateMs = Date.parse(retryAfter);
  if (!Number.isNaN(dateMs)) {
    return Math.max(0, dateMs - Date.now());
  }

  return null;
}

function shouldRetry(status) {
  return (
    status === 429 ||
    status === 500 ||
    status === 502 ||
    status === 503 ||
    status === 504
  );
}

async function callOpenRouterWithRetry(payload, options = {}) {
  const maxRetries = options.maxRetries ?? 4;
  const baseDelayMs = options.baseDelayMs ?? 1000;
  const maxDelayMs = options.maxDelayMs ?? 30000;

  let lastError;

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${OPENROUTER_API_KEY}`,
          "Content-Type": "application/json",
          "HTTP-Referer": "https://tu-sitio.com", // opcional pero recomendado
          "X-Title": "Tu App" // opcional
        },
        body: JSON.stringify(payload)
      });

      if (response.ok) {
        return await response.json();
      }

      const errorText = await response.text();

      // Si no es un error reintentable, falla inmediatamente
      if (!shouldRetry(response.status)) {
        throw new Error(`OpenRouter error ${response.status}: ${errorText}`);
      }

      // Si ya no quedan intentos, falla
      if (attempt === maxRetries) {
        throw new Error(`OpenRouter error ${response.status} after retries: ${errorText}`);
      }

      let delayMs = getRetryAfterMs(response);

      if (delayMs == null) {
        const exponentialDelay = baseDelayMs * Math.pow(2, attempt);
        const jitter = Math.floor(Math.random() * 1000);
        delayMs = Math.min(exponentialDelay + jitter, maxDelayMs);
      }

      console.warn(
        `OpenRouter ${response.status}. Retry ${attempt + 1}/${maxRetries} en ${delayMs}ms`
      );

      await sleep(delayMs);
    } catch (err) {
      lastError = err;

      // Errores de red también pueden reintentarse
      if (attempt === maxRetries) {
        throw lastError;
      }

      const exponentialDelay = baseDelayMs * Math.pow(2, attempt);
      const jitter = Math.floor(Math.random() * 1000);
      const delayMs = Math.min(exponentialDelay + jitter, maxDelayMs);

      console.warn(
        `Network/error retry ${attempt + 1}/${maxRetries} en ${delayMs}ms:`,
        err.message
      );

      await sleep(delayMs);
    }
  }

  throw lastError;
}
```

Uso:

```js
const result = await callOpenRouterWithRetry({
  model: "deepseek/deepseek-chat-v3-0324",
  messages: [
    { role: "user", content: "Hola" }
  ]
});
```

---

# Ejemplo en Python con `requests`

```python
import os
import time
import random
import requests
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone

OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]

def should_retry(status_code):
    return status_code in [429, 500, 502, 503, 504]

def get_retry_after_ms(response):
    retry_after = response.headers.get("Retry-After")

    if not retry_after:
        return None

    # Puede ser segundos
    try:
        return int(retry_after) * 1000
    except ValueError:
        pass

    # O fecha HTTP
    try:
        retry_date = parsedate_to_datetime(retry_after)
        now = datetime.now(timezone.utc)
        return max(0, int((retry_date - now).total_seconds() * 1000))
    except Exception:
        return None

def call_openrouter_with_retry(payload, max_retries=4, base_delay_ms=1000, max_delay_ms=30000):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://tu-sitio.com",
        "X-Title": "Tu App"
    }

    last_error = None

    for attempt in range(max_retries + 1):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)

            if response.ok:
                return response.json()

            if not should_retry(response.status_code):
                raise Exception(f"OpenRouter error {response.status_code}: {response.text}")

            if attempt == max_retries:
                raise Exception(f"OpenRouter error {response.status_code} after retries: {response.text}")

            delay_ms = get_retry_after_ms(response)

            if delay_ms is None:
                exponential_delay = base_delay_ms * (2 ** attempt)
                jitter = random.randint(0, 1000)
                delay_ms = min(exponential_delay + jitter, max_delay_ms)

            print(f"OpenRouter {response.status_code}. Retry {attempt + 1}/{max_retries} en {delay_ms}ms")
            time.sleep(delay_ms / 1000)

        except requests.RequestException as e:
            last_error = e

            if attempt == max_retries:
                raise

            exponential_delay = base_delay_ms * (2 ** attempt)
            jitter = random.randint(0, 1000)
            delay_ms = min(exponential_delay + jitter, max_delay_ms)

            print(f"Network retry {attempt + 1}/{max_retries} en {delay_ms}ms: {e}")
            time.sleep(delay_ms / 1000)

    raise last_error
```

Uso:

```python
result = call_openrouter_with_retry({
    "model": "deepseek/deepseek-chat-v3-0324",
    "messages": [
        {"role": "user", "content": "Hola"}
    ]
})
```

---

## Importante: también limita la concurrencia

Aunque hagas 5 requests/minuto en promedio, si las mandas todas al mismo tiempo o tienes varios workers, puedes disparar 429.

Ejemplo de mala situación:

```txt
Worker 1: 5 req/min
Worker 2: 5 req/min
Worker 3: 5 req/min
Retry bug: x100
```

Resultado: cientos de requests reales.

Te conviene tener:

- límite de concurrencia, por ejemplo máximo 1-3 requests simultáneas
- cola de requests
- retries centralizados en una sola función

---

## Configuración práctica recomendada

Para empezar usa algo así:

```txt
maxRetries: 3 o 4
baseDelayMs: 1000
maxDelayMs: 30000
timeout: 60s
retry solo en: 429, 500, 502, 503, 504, errores de red
```

Y loguea siempre:

```txt
status code
retry-after
x-ratelimit-limit
x-ratelimit-remaining
x-ratelimit-reset
modelo usado
intento actual
delay antes del retry
```

---

## Anti-patrón que debes evitar

Algo como esto está mal:

```js
while (true) {
  try {
    return await callApi();
  } catch (e) {
    // retry inmediato infinito
  }
}
```

Eso es lo que te está causando la cascada de 429.

---

## Patrón correcto resumido

```js
for intentos hasta maxRetries:
  llamar API
  si OK: devolver resultado
  si error no reintentable: fallar
  si 429 y Retry-After existe: esperar eso
  si no: esperar exponential backoff + jitter
fallar definitivamente
```

Con eso deberías dejar de amplificar el problema y OpenRouter debería volver a responder normalmente una vez se calme el rate limit.