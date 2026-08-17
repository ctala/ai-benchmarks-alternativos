# Nex-N2-Mini — multi_turn/debugging_conversation

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 9.18 | quality: 10.0
- latency_total: 19.842s | tokens_per_second: 223.6
- input_tokens: 339 | output_tokens: 4436

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

Correcto: el problema no es DeepSeek V3 ni tus $20 de saldo; tu loop está multiplicando cada 429 en ~100 peticiones. La solución es cambiar el retry a un **retry limitado con backoff exponencial + jitter**, y no a un loop infinito.

## Reglas recomendadas para retries

1. **Retry solo errores temporales**
   - `408` Timeout
   - `429` Too Many Requests
   - `500`, `502`, `503`, `504`

2. **No reintentes errores de cliente**
   - `400`, `401`, `403`, `404`, `422` normalmente no se retryean.

3. **Respeta `Retry-After` si OpenRouter lo devuelve**
   - Si el header existe, espera ese tiempo.

4. **Usa backoff exponencial**
   - Ejemplo: 0.5s, 1s, 2s, 4s, 8s.

5. **Agrega jitter aleatorio**
   - Evita que muchas requests reintenten exactamente al mismo tiempo.

6. **Pon un límite máximo**
   - Ejemplo: `3 a 5 reintentos`.
   - Después de eso, falla claramente.

---

## Ejemplo en JavaScript/TypeScript

```js
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function isRetryableStatus(status) {
  return [408, 429, 500, 502, 503, 504].includes(status);
}

function parseRetryAfter(value) {
  if (!value) return null;

  const seconds = Number(value);
  if (Number.isFinite(seconds) && seconds > 0) {
    return seconds * 1000;
  }

  const date = Date.parse(value);
  if (!Number.isNaN(date)) {
    return Math.max(0, date - Date.now());
  }

  return null;
}

async function callOpenRouterWithRetry(makeCall, options = {}) {
  const {
    maxRetries = 4,
    baseDelayMs = 500,
    maxDelayMs = 10000,
  } = options;

  let delayMs = baseDelayMs;

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await makeCall();
    } catch (err) {
      const status = err.status ?? err.response?.status;
      const headers = err.headers ?? err.response?.headers;

      if (!isRetryableStatus(status)) {
        throw err;
      }

      if (attempt === maxRetries) {
        throw err;
      }

      const retryAfterMs = parseRetryAfter(
        headers?.get?.("retry-after") ?? headers?.["retry-after"]
      );

      const jitterMs = Math.random() * delayMs * 0.3;

      const waitMs = Math.min(
        maxDelayMs,
        retryAfterMs ?? delayMs + jitterMs
      );

      await sleep(waitMs);

      delayMs = Math.min(maxDelayMs, delayMs * 2);
    }
  }
}
```

Y tu llamada a OpenRouter podría verse así:

```js
async function openRouterRequest(payload) {
  const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.OPENROUTER_API_KEY}`,
      "Content-Type": "application/json",
      // Si tu SDK o endpoint soporta idempotency keys:
      // "Idempotency-Key": crypto.randomUUID(),
    },
    body: JSON.stringify(payload),
  });

  const text = await response.text();

  if (!response.ok) {
    const err = new Error(`OpenRouter ${response.status}: ${text}`);
    err.status = response.status;
    err.headers = response.headers;
    err.body = text;
    throw err;
  }

  return JSON.parse(text);
}
```

Uso:

```js
const result = await callOpenRouterWithRetry(() => {
  return openRouterRequest({
    model: "deepseek/deepseek-chat",
    messages: [
      { role: "user", content: "Hola" }
    ]
  });
}, {
  maxRetries: 4,
  baseDelayMs: 500,
  maxDelayMs: 10000
});

console.log(result);
```

---

## Importante

Si OpenRouter devuelve un 429 después de tus reintentos, no sigas intentando infinitamente. Muestra algo claro como:

```txt
OpenRouter rate limit exceeded after 4 retries.
Status: 429
Retry-After: 120
Request ID: xxx
```

También te recomiendo registrar estos headers cuando falte:

```txt
x-ratelimit-remaining
x-ratelimit-reset
x-request-id
retry-after
```

---

## Recomendación adicional

Aunque ahora estás en `5 requests/min`, implementa un pequeño rate limiter propio si haces llamadas en batch o en paralelo. Por ejemplo:

- Máximo 3-4 requests/min por API key/modelo.
- Máximo 2-5 concurrencias simultáneas.
- Espera antes de enviar la siguiente request si se acerca el límite.

En resumen: **quita el retry infinito**, usa `Retry-After`, backoff exponencial con jitter, máximo 3-5 reintentos y falla claramente si OpenRouter sigue devolviendo 429.