# GPT-5.6 Sol — multi_turn/debugging_conversation

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 7.85 | quality: 9.55
- latency_total: 17.133s | tokens_per_second: 69.6
- input_tokens: 312 | output_tokens: 1193
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y prácticamente útil, abordando el problema de manera exhaustiva con una solución detallada y ejemplos de código.

## Respuesta completa

El problema es un **retry storm**: cada 429 dispara inmediatamente otra llamada, que mantiene el rate limit activo. La solución es usar **reintentos limitados con espera exponencial y jitter**.

### Política recomendada

- Máximo **4–5 intentos totales**.
- Respetar el header `Retry-After` cuando exista.
- Si no existe, usar backoff exponencial: `1s, 2s, 4s, 8s…`.
- Añadir jitter aleatorio para evitar que varias peticiones reintenten simultáneamente.
- Reintentar solamente:
  - `429`
  - `408`
  - `500`, `502`, `503`, `504`
  - Errores temporales de red
- **No reintentar** `400`, `401`, `402`, `403`, etc.
- Limitar también la concurrencia global.

Ejemplo en JavaScript con `fetch`:

```js
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

function getRetryDelay(response, attempt) {
  const retryAfter = response.headers.get("retry-after");

  if (retryAfter) {
    // Retry-After puede ser una cantidad de segundos
    const seconds = Number(retryAfter);
    if (Number.isFinite(seconds)) {
      return seconds * 1000;
    }

    // O una fecha HTTP
    const date = Date.parse(retryAfter);
    if (!Number.isNaN(date)) {
      return Math.max(0, date - Date.now());
    }
  }

  // Backoff exponencial con jitter, limitado a 30 segundos
  const baseDelay = Math.min(1000 * (2 ** attempt), 30_000);
  return Math.floor(Math.random() * baseDelay);
}

async function callOpenRouter(messages, maxAttempts = 5) {
  for (let attempt = 0; attempt < maxAttempts; attempt++) {
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
          })
        }
      );
    } catch (error) {
      // Error de red: se puede reintentar, pero nunca indefinidamente
      if (attempt === maxAttempts - 1) {
        throw error;
      }

      const delay = Math.floor(
        Math.random() * Math.min(1000 * (2 ** attempt), 30_000)
      );

      console.warn(`Error de red. Retry en ${delay} ms`);
      await sleep(delay);
      continue;
    }

    if (response.ok) {
      return response.json();
    }

    const body = await response.text();

    const retryable =
      response.status === 408 ||
      response.status === 429 ||
      [500, 502, 503, 504].includes(response.status);

    if (!retryable || attempt === maxAttempts - 1) {
      throw new Error(
        `OpenRouter error ${response.status}: ${body}`
      );
    }

    const delay = getRetryDelay(response, attempt);

    console.warn(
      `OpenRouter devolvió ${response.status}. ` +
      `Intento ${attempt + 1}/${maxAttempts}; retry en ${delay} ms. ` +
      `Respuesta: ${body}`
    );

    await sleep(delay);
  }

  throw new Error("Se agotaron los reintentos");
}
```

También conviene:

1. **Detener temporalmente tu proceso** para dejar que expire la ventana del rate limit.
2. Registrar el cuerpo del 429, porque puede indicar límite del proveedor, límite de cuenta u otra causa.
3. Poner un límite de concurrencia, por ejemplo 2–5 llamadas simultáneas.
4. Evitar retries en streaming una vez que ya recibiste tokens: podrías generar o facturar una segunda respuesta.
5. Si tras agotar los intentos sigue fallando, devolver el error al caller o enviarlo a una cola para reintentar más tarde, nunca iniciar otro loop infinito.

La regla esencial es que todo loop de retry debe tener simultáneamente **máximo de intentos, espera y condición explícita de salida**.