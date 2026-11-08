# GPT-5.6 Terra — multi_turn/debugging_conversation

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 11.266s | tokens_per_second: 128.9
- input_tokens: 312 | output_tokens: 1452

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

La solución es aplicar **retries limitados con backoff exponencial y jitter**, respetando `Retry-After` cuando el servidor lo envíe.

Reglas recomendadas:

- Reintentar solo errores transitorios: `429`, `500`, `502`, `503`, `504` y errores de red/timeouts.
- **No** reintentar automáticamente `400`, `401`, `403`, `404`, etc.
- Limitar los intentos, por ejemplo a 3–5.
- Esperar más en cada intento: 1 s, 2 s, 4 s, 8 s…
- Añadir un pequeño valor aleatorio (*jitter*) para evitar que todos los procesos reintenten simultáneamente.
- Si llega `Retry-After`, usarlo como espera mínima.
- Registrar el error final, código, request ID y número de intentos.

Ejemplo en JavaScript con `fetch`:

```js
const TRANSIENT_STATUS_CODES = new Set([429, 500, 502, 503, 504]);

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function getRetryAfterMs(response) {
  const value = response.headers.get("retry-after");

  if (!value) return null;

  // Puede venir como segundos: Retry-After: 5
  const seconds = Number(value);
  if (!Number.isNaN(seconds)) {
    return seconds * 1000;
  }

  // O como fecha HTTP
  const date = new Date(value).getTime();
  if (!Number.isNaN(date)) {
    return Math.max(0, date - Date.now());
  }

  return null;
}

async function callOpenRouter(payload, options = {}) {
  const {
    maxRetries = 4,       // 1 intento inicial + hasta 4 reintentos
    baseDelayMs = 1000,
    maxDelayMs = 30000,
    timeoutMs = 60000,
  } = options;

  let lastError;

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), timeoutMs);

    try {
      const response = await fetch(
        "https://openrouter.ai/api/v1/chat/completions",
        {
          method: "POST",
          headers: {
            "Authorization": `Bearer ${process.env.OPENROUTER_API_KEY}`,
            "Content-Type": "application/json",
            // Opcionales, recomendados por OpenRouter:
            "HTTP-Referer": "https://tu-app.example",
            "X-Title": "Mi aplicación",
          },
          body: JSON.stringify(payload),
          signal: controller.signal,
        }
      );

      clearTimeout(timeout);

      if (response.ok) {
        return await response.json();
      }

      const body = await response.text();

      // No reintentar errores no transitorios.
      if (!TRANSIENT_STATUS_CODES.has(response.status)) {
        throw new Error(
          `OpenRouter devolvió ${response.status}: ${body}`
        );
      }

      lastError = new Error(
        `Intento ${attempt + 1}: OpenRouter devolvió ${response.status}: ${body}`
      );

      // Ya agotamos los reintentos.
      if (attempt === maxRetries) {
        break;
      }

      const retryAfterMs = getRetryAfterMs(response);

      // Backoff exponencial: 1s, 2s, 4s, 8s...
      const exponentialDelay = Math.min(
        baseDelayMs * (2 ** attempt),
        maxDelayMs
      );

      // Jitter entre 0 y 500 ms.
      const jitter = Math.floor(Math.random() * 500);

      // Si el servidor pidió esperar, respetarlo como mínimo.
      const delayMs = Math.max(
        retryAfterMs ?? 0,
        exponentialDelay + jitter
      );

      console.warn(
        `OpenRouter respondió ${response.status}. ` +
        `Reintentando en ${delayMs} ms ` +
        `(intento ${attempt + 2}/${maxRetries + 1})`
      );

      await sleep(delayMs);

    } catch (error) {
      clearTimeout(timeout);

      // AbortError suele representar un timeout local.
      const isNetworkOrTimeoutError =
        error.name === "AbortError" ||
        error instanceof TypeError; // fetch suele usar TypeError para fallos de red

      if (!isNetworkOrTimeoutError || attempt === maxRetries) {
        throw error;
      }

      lastError = error;

      const delayMs = Math.min(
        baseDelayMs * (2 ** attempt) + Math.floor(Math.random() * 500),
        maxDelayMs
      );

      console.warn(
        `Error de red/timeout: ${error.message}. ` +
        `Reintentando en ${delayMs} ms.`
      );

      await sleep(delayMs);
    }
  }

  throw lastError ?? new Error("No se pudo completar la llamada a OpenRouter.");
}
```

Uso:

```js
const result = await callOpenRouter({
  model: "deepseek/deepseek-chat",
  messages: [
    { role: "user", content: "Explica qué es un rate limit." }
  ]
});

console.log(result.choices[0].message.content);
```

Además, conviene corregir dos cosas en tu arquitectura:

1. **Evita disparar varias peticiones simultáneas sin control.**  
   Aunque tu flujo normal sea 5 RPM, un lote o varios usuarios podrían generar picos. Usa una cola o un límite de concurrencia.

2. **Cuidado con reintentar POSTs tras un timeout.**  
   Si tu cliente pierde la respuesta por red, el servidor podría haber procesado la petición igualmente. Reintentar puede generar una segunda generación y un segundo coste. Para tareas importantes, guarda el estado de cada trabajo antes de enviarlo y usa IDs de trabajo/idempotencia en tu propia aplicación.

Configuración práctica inicial:

```js
maxRetries: 4
baseDelayMs: 1000
maxDelayMs: 30000
timeoutMs: 60000
```

Con eso, un `429` ya no se convierte en cientos de requests: se convierte, como máximo, en unas pocas solicitudes espaciadas y controladas.