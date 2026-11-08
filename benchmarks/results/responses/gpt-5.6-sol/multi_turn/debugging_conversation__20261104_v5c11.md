# GPT-5.6 Sol — multi_turn/debugging_conversation

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 12.335s | tokens_per_second: 111.4
- input_tokens: 312 | output_tokens: 1374

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

El problema es un **retry storm**: cada 429 dispara inmediatamente más solicitudes, impidiendo que se recupere el límite. Primero detén el proceso unos minutos y luego implementa:

- Máximo de 3–5 reintentos.
- Respetar `Retry-After` si existe.
- Backoff exponencial con jitter.
- Reintentar solo errores temporales: `429`, `408` y algunos `5xx`.
- No reintentar errores permanentes como `400`, `401`, `403` o `404`.
- Limitar también la concurrencia.

### Ejemplo en JavaScript/TypeScript con `fetch`

```js
const MAX_RETRIES = 4;
const MAX_DELAY_MS = 30_000;

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function getRetryAfterMs(response) {
  const value = response.headers.get("retry-after");
  if (!value) return null;

  // Retry-After puede ser segundos...
  const seconds = Number(value);
  if (Number.isFinite(seconds)) {
    return Math.max(0, seconds * 1000);
  }

  // ...o una fecha HTTP.
  const dateMs = Date.parse(value);
  if (Number.isFinite(dateMs)) {
    return Math.max(0, dateMs - Date.now());
  }

  return null;
}

function isRetryable(status) {
  return status === 408 ||
         status === 429 ||
         status === 500 ||
         status === 502 ||
         status === 503 ||
         status === 504;
}

async function callOpenRouter(messages) {
  const totalAttempts = MAX_RETRIES + 1;

  for (let attempt = 0; attempt < totalAttempts; attempt++) {
    let response;

    try {
      response = await fetch(
        "https://openrouter.ai/api/v1/chat/completions",
        {
          method: "POST",
          headers: {
            "Authorization": `Bearer ${process.env.OPENROUTER_API_KEY}`,
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            model: "deepseek/deepseek-chat",
            messages
          }),
          signal: AbortSignal.timeout(60_000)
        }
      );
    } catch (error) {
      // Error de red o timeout.
      if (attempt === totalAttempts - 1) throw error;

      const maxBackoff = Math.min(
        MAX_DELAY_MS,
        1000 * 2 ** attempt
      );

      // Full jitter: espera aleatoria entre 0 y maxBackoff.
      const delayMs = Math.random() * maxBackoff;

      console.warn(`Error de red. Retry en ${Math.round(delayMs)} ms`);
      await sleep(delayMs);
      continue;
    }

    if (response.ok) {
      return response.json();
    }

    const errorBody = await response.text();

    if (!isRetryable(response.status)) {
      throw new Error(
        `OpenRouter ${response.status}: ${errorBody}`
      );
    }

    if (attempt === totalAttempts - 1) {
      throw new Error(
        `OpenRouter sigue fallando después de ${totalAttempts} intentos. ` +
        `Status ${response.status}: ${errorBody}`
      );
    }

    const retryAfterMs = getRetryAfterMs(response);

    const maxBackoff = Math.min(
      MAX_DELAY_MS,
      1000 * 2 ** attempt
    );

    const delayMs = retryAfterMs ??
      Math.random() * maxBackoff;

    console.warn(
      `OpenRouter respondió ${response.status}. ` +
      `Retry ${attempt + 1}/${MAX_RETRIES} en ${Math.round(delayMs)} ms`
    );

    await sleep(delayMs);
  }
}
```

### Comportamiento esperado

Sin `Retry-After`, las esperas máximas serían aproximadamente:

- Primer retry: entre 0 y 1 s.
- Segundo: entre 0 y 2 s.
- Tercero: entre 0 y 4 s.
- Cuarto: entre 0 y 8 s.

El jitter evita que varias instancias vuelvan a llamar simultáneamente.

### Recomendaciones adicionales

1. **No hagas retries anidados**: si tu SDK ya reintenta automáticamente, no añadas otra capa sin desactivar o contabilizar sus retries.
2. **Limita la concurrencia**: por ejemplo, máximo 2–5 solicitudes simultáneas.
3. **Registra**:
   - código HTTP;
   - cuerpo del error;
   - `Retry-After`;
   - headers de rate limit;
   - número de intento;
   - identificador de solicitud, si aparece.
4. **Aplica un circuit breaker**: si recibes varios 429 seguidos, pausa todas las llamadas durante 30–60 segundos.
5. **No registres la API key**.
6. Tras tu loop infinito, **detén todas las instancias/workers y espera un poco** antes de probar; si alguna sigue activa, continuará renovando el problema.

El saldo disponible no evita necesariamente los 429: también pueden venir de límites de concurrencia, del proveedor subyacente, de un modelo concreto o de límites asociados a la cuenta/key. El cuerpo de la respuesta 429 suele indicar cuál de estos casos es.