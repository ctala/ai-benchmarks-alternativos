# GPT-5.6 Luna Pro — multi_turn/debugging_conversation

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.77 | quality: 10.0
- latency_total: 24.816s | tokens_per_second: 200.7
- input_tokens: 7182 | output_tokens: 4980

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

El problema principal es que el retry infinito convierte un 429 en una avalancha de solicitudes. Debes usar **reintentos limitados**, **backoff exponencial** y respetar `Retry-After`.

Una política razonable:

- Máximo: 3–5 reintentos.
- Espera creciente: 1 s, 2 s, 4 s, 8 s, etc.
- Añadir jitter aleatorio para evitar que varias instancias reintenten a la vez.
- Respetar siempre `Retry-After` si OpenRouter lo devuelve.
- No reintentar errores permanentes como `401`, `402`, `403` o `400`.
- Aplicar también un tiempo máximo total, por ejemplo 60 segundos.

### Ejemplo con `fetch` en JavaScript

```js
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

function getRetryAfterMs(response) {
  const value = response.headers.get("retry-after");

  if (!value) return null;

  // Normalmente Retry-After es un número de segundos
  const seconds = Number(value);
  if (Number.isFinite(seconds)) {
    return seconds * 1000;
  }

  // También puede ser una fecha HTTP
  const date = Date.parse(value);
  if (!Number.isNaN(date)) {
    return Math.max(0, date - Date.now());
  }

  return null;
}

async function callOpenRouter(payload, apiKey) {
  const maxRetries = 5;
  const baseDelayMs = 1000;
  const maxDelayMs = 30000;
  const deadline = Date.now() + 60000; // máximo 60 segundos

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${apiKey}`,
        "Content-Type": "application/json",
        "HTTP-Referer": "https://tu-dominio.example",
        "X-Title": "Tu aplicación"
      },
      body: JSON.stringify(payload)
    });

    if (response.ok) {
      return await response.json();
    }

    const body = await response.text();
    const status = response.status;

    // No reintentar errores permanentes
    const permanentError =
      status === 400 ||
      status === 401 ||
      status === 402 ||
      status === 403 ||
      status === 404;

    const retryableError =
      status === 408 ||
      status === 429 ||
      status >= 500;

    if (
      permanentError ||
      !retryableError ||
      attempt === maxRetries ||
      Date.now() >= deadline
    ) {
      throw new Error(
        `OpenRouter error ${status} después de ${attempt + 1} intento(s): ${body}`
      );
    }

    const retryAfterMs = getRetryAfterMs(response);

    // Backoff exponencial con jitter
    const exponentialMs = Math.min(
      maxDelayMs,
      baseDelayMs * 2 ** attempt
    );

    const jitterMs = Math.floor(Math.random() * 500);

    // Si el servidor indica un tiempo, respetarlo
    const delayMs = Math.min(
      Math.max(retryAfterMs ?? 0, exponentialMs + jitterMs),
      Math.max(0, deadline - Date.now())
    );

    console.warn(
      `OpenRouter devolvió ${status}. ` +
      `Reintento ${attempt + 1}/${maxRetries} en ${delayMs} ms`
    );

    await sleep(delayMs);
  }
}
```

Uso:

```js
const result = await callOpenRouter({
  model: "deepseek/deepseek-chat",
  messages: [
    { role: "user", content: "Hola" }
  ]
}, process.env.OPENROUTER_API_KEY);
```

### Importante en tu caso

Después de haber generado cientos de solicitudes, detén completamente el proceso y espera un poco antes de probar de nuevo. El saldo pagado no elimina necesariamente:

- Los límites de tu cuenta.
- Los límites del modelo o proveedor.
- Los límites de concurrencia.
- Los límites temporales provocados por el exceso reciente.

Revisa también estos headers de la respuesta:

```text
Retry-After
X-RateLimit-Limit
X-RateLimit-Remaining
X-RateLimit-Reset
```

No hagas reintentos concurrentes sin control. Por ejemplo, si procesas una cola, limita la concurrencia:

```js
// Evita lanzar 50 llamadas simultáneas.
// Empieza con 1–3 llamadas concurrentes.
```

Además, evita reintentar un error de saldo:

- `401`: API key inválida.
- `402`: saldo, créditos o facturación.
- `403`: acceso denegado.
- `429`: límite de solicitudes.
- `5xx`: error temporal del servidor o proveedor.

Para un `429`, la lógica correcta no es “reintentar inmediatamente”, sino:

```text
429
→ leer Retry-After
→ esperar
→ reintentar con backoff
→ detenerse después de N intentos
→ registrar el error y dejar que la aplicación lo gestione
```

Si sigues recibiendo 429 con una sola llamada cada varios segundos y después de esperar, entonces ya no parece un problema de tu loop: habría que revisar los headers, el modelo exacto utilizado y el estado de límites de tu cuenta en OpenRouter.