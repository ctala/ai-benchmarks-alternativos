# Tencent Hy4 preview — multi_turn/debugging_conversation

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.36 | quality: 10.0
- latency_total: 85.794s | tokens_per_second: 64.3
- input_tokens: 371 | output_tokens: 5518

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

Ese loop infinito es exactamente el problema: un **429** significa “espera”, pero tu código volvía a llamar **inmediatamente**.Como el rate limit se mide en requests por minuto, cada reintorno consumía tu cuota y generaba más 429. Es el clásico **“retry storm”**.

La buena noticia: con $20 de saldo y DeepSeek V3 tienes límite de **300 RPM**, así que 5 requests/minuto no deberían dar 429 si los reintentos están bien hechos.

## Reglas para implementar retries correctamente

1. **Solo reintentar errores transitorios**
   - Sí: `429`, `500`, `502`, `503`, `504`, timeouts de red.
   - No: `400`, `401`, `403`, `404` (ahí el problema es la request, la API key o el modelo; reintentar no arregla nada).

2. **Número máximo de reintentos**
   - Usa entre **3 y 5**. Nunca `while True`.

3. **Backoff exponencial**
   - Espera `1s`, `2s`, `4s`, `8s`… hasta un máximo (ej. 30–60s).

4. **Jitter (aleatoriedad)**
   - Añade un pequeño random para que varios workers/clientes no reintentena la vez.

5. **Respetar el header `Retry-After`**
   - Si OpenRouter responde con `Retry-After: 20`, espera al menos esos segundos. Tiene prioridad sobre tu backoff.

6. **Fallar limpio**
   - Si se agotan los reintentos, lanza un error, loguea o mete el request en una cola. No sigas en loop.

7. **Cuidado con la concurrencia**
   - Si tienes múltiples hilos/workers reintentando al mismo tiempo, el total se multiplica. Limita también globalmente.

---

## Ejemplo en Python (requests)

```python
import requests
import time
import random

API_KEY = "sk-or-v1-..."
URL = "https://openrouter.ai/api/v1/chat/completions"

MAX_RETRIES = 5
BASE_DELAY = 1  # segundos

def call_openrouter(payload):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        # Recomendado por OpenRouter (opcional pero útil para rankings)
        "HTTP-Referer": "https://tu-sitio.com",
        "X-Title": "MiApp",
    }

    for attempt in range(MAX_RETRIES + 1):
        resp = requests.post(URL, json=payload, headers=headers, timeout=30)

        # Éxito
        if resp.status_code == 200:
            return resp.json()

        # Errores que NO se reintentan
        if resp.status_code in (400, 401, 403, 404):
            resp.raise_for_status()

        # Si llegamos al último intento, fallamos
        if attempt == MAX_RETRIES:
            resp.raise_for_status()

        # Calcular espera
        retry_after = resp.headers.get("Retry-After")
        if retry_after:
            delay = float(retry_after)
        else:
            delay = BASE_DELAY * (2 ** attempt)

        # Jitter +/- 20% y tope de 60s
        delay = delay * (1 + random.uniform(-0.2, 0.2))
        delay = min(max(delay, 0), 60)

        print(f"[{resp.status_code}] Reintentando en {delay:.1f}s (intento {attempt+1}/{MAX_RETRIES})")
        time.sleep(delay)
```

> Bonus: si usas el SDK de OpenAI apuntando a OpenRouter, ya trae reintentos con backoff. Solo configura `max_retries` y **no** lo envuelvas en tu propio loop infinito:
>
> ```python
> from openai import OpenAI
>
> client = OpenAI(
>     base_url="https://openrouter.ai/api/v1",
>     api_key=API_KEY,
>     max_retries=5,
>     timeout=30,
> )
> ```

---

## Ejemplo en JavaScript (fetch)

```js
const API_KEY = "sk-or-v1-...";

async function callOpenRouter(payload, maxRetries = 5) {
  const url = "https://openrouter.ai/api/v1/chat/completions";

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    const res = await fetch(url, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (res.ok) return await res.json();

    // No reintentar errores de cliente
    if ([400, 401, 403, 404].includes(res.status)) {
      throw new Error(`Error no reintentable: ${res.status}`);
    }

    if (attempt === maxRetries) {
      throw new Error(`Falló después de ${maxRetries} reintentos: ${res.status}`);
    }

    let delay = res.headers.get("Retry-After");
    delay = delay ? parseInt(delay, 10) * 1000 : 1000 * 2 ** attempt;

    // Jitter y tope
    delay = Math.min(delay, 60000);
    delay += Math.random() * 200 - 100;

    console.log(`[${res.status}] Reintentando en ${delay}ms`);
    await new Promise(r => setTimeout(r, delay));
  }
}
```

---

## Extra: ser proactivo con los headers de rate limit

OpenRouter devuelve headers tipo:

- `x-ratelimit-limit`
- `x-ratelimit-remaining`
- `x-ratelimit-reset`

Si `x-ratelimit-remaining` llega a `0`, puedes dormirte hasta `x-ratelimit-reset` **antes** de que te llegue el 429. Esto es opcional, pero hace tu cliente mucho más robusto si escalas el número de requests.

---

### Resumen
Tu bug no era la API ni el saldo: era el **loop de reintentos inmediatos**. Con **backoff exponencial + jitter + respetar `Retry-After` + un máximo de 3-5 reintentos**, deberías dejar de ver 429 por completo.

Si me dices en qué lenguaje/framework estás (Node, Python, n8n, etc.), te puedo dejar el snippet exacto para tu caso.