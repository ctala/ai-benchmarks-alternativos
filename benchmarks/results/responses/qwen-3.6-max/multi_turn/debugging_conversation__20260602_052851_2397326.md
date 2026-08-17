# Qwen 3.6 Max — multi_turn/debugging_conversation

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 6.9 | quality: 9.1
- latency_total: 93.366s | tokens_per_second: 39.7
- input_tokens: 340 | output_tokens: 3711
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y prácticamente útil, abordando el problema de manera exhaustiva y proporcionando soluciones detalladas con ejemplos de código.

## Respuesta completa

¡Excelente diagnóstico! Ese patrón es un clásico: un retry sin control convierte un 429 menor en un bloqueo total por "thundering herd". Vamos a arreglarlo con una estrategia de reintentos segura y production-ready.

### 🔑 Reglas de oro para retries en APIs
1. **Nunca retries infinitos**: máximo 3-5 intentos.
2. **Solo reintentar errores recuperables**: `429`, `5xx`, timeouts o fallos de red. **Nunca** `4xx` (excepto 429).
3. **Backoff exponencial + jitter**: `espera = base * (2^intento) + aleatorio`. Evita que todos los clientes reboten al mismo tiempo.
4. **Respetar headers del servidor**: si viene `Retry-After` o `x-ratelimit-*`, úsalos como fuente de verdad.
5. **Fail fast**: si se alcanza el máximo, lanza error claro y deja que tu app lo maneje.

---

### 🐍 Python (sin dependencias externas)
```python
import requests
import time
import random

def call_openrouter(url, headers, payload, max_retries=4):
    for attempt in range(max_retries):
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=30)
        except requests.exceptions.RequestException as e:
            print(f"🌐 Error de red: {e}")
            wait = (2 ** attempt) + random.uniform(0, 1)
            time.sleep(wait)
            continue

        if resp.status_code == 200:
            return resp.json()

        # ✅ 429: respetar Retry-After o backoff
        if resp.status_code == 429:
            retry_after = resp.headers.get("Retry-After")
            wait = int(retry_after) if retry_after else (2 ** attempt) + random.uniform(0, 1)
            print(f"⚠️ 429 Rate Limit. Esperando {wait:.1f}s (intento {attempt+1}/{max_retries})")
            time.sleep(wait)
            continue

        # ❌ Otros 4xx: no reintentar
        if 400 <= resp.status_code < 500:
            resp.raise_for_status()

        # 🔄 5xx o errores inesperados: backoff
        wait = (2 ** attempt) + random.uniform(0, 1)
        print(f"🔄 Error {resp.status_code}. Reintentando en {wait:.1f}s...")
        time.sleep(wait)

    raise RuntimeError("❌ Máximo de reintentos alcanzado. Verifica límites o estado de OpenRouter.")
```

---

### 🟨 JavaScript/Node.js (fetch nativo)
```js
async function callOpenRouter(url, headers, payload, maxRetries = 4) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    let resp;
    try {
      resp = await fetch(url, {
        method: "POST",
        headers,
        body: JSON.stringify(payload),
        signal: AbortSignal.timeout(30000)
      });
    } catch (err) {
      console.warn(`🌐 Error de red: ${err.message}`);
      await sleep((2 ** attempt) * 1000 + Math.random() * 1000);
      continue;
    }

    if (resp.ok) return await resp.json();

    if (resp.status === 429) {
      const retryAfter = resp.headers.get("Retry-After");
      const wait = retryAfter ? parseInt(retryAfter) * 1000 : (2 ** attempt) * 1000 + Math.random() * 1000;
      console.warn(`⚠️ 429 Rate Limit. Esperando ${(wait/1000).toFixed(1)}s (intento ${attempt+1}/${maxRetries})`);
      await sleep(wait);
      continue;
    }

    if (resp.status >= 400 && resp.status < 500) {
      const text = await resp.text();
      throw new Error(`❌ Error cliente ${resp.status}: ${text}`);
    }

    const wait = (2 ** attempt) * 1000 + Math.random() * 1000;
    console.warn(`🔄 Error ${resp.status}. Reintentando en ${(wait/1000).toFixed(1)}s...`);
    await sleep(wait);
  }
  throw new Error("❌ Máximo de reintentos alcanzado.");
}

const sleep = ms => new Promise(res => setTimeout(res, ms));
```

---

### 📊 Headers de OpenRouter que debes monitorear
OpenRouter devuelve estos headers en cada respuesta (incluyendo 429):
- `x-ratelimit-requests-limit`: tu límite por ventana
- `x-ratelimit-requests-remaining`: cuántos te quedan
- `x-ratelimit-requests-reset`: timestamp Unix cuando se reinicia la ventana
- `Retry-After`: segundos a esperar (si aplica)

💡 **Tip pro**: si `x-ratelimit-requests-remaining == 0`, calcula `wait = max(0, reset_timestamp - time.now())` y duerme ese tiempo antes de reintentar.

---

### 🛡️ Buenas prácticas adicionales
- ✅ Usa librerías probadas si prefieres no mantener el loop: `tenacity` (Python), `axios-retry` o `got` (JS), `httpx` con `AsyncHTTPTransport(retries=...)`.
- 🔍 Verifica que **ningún otro proceso/thread** esté usando la misma API key en paralelo.
- 📦 Si tu app hace muchas llamadas, considera una cola de trabajos (Celery, BullMQ, AWS SQS) con concurrencia controlada.
- 📈 Loggea `attempt`, `status_code`, `wait_time` y `x-ratelimit-*` para debug futuro.

---

¿En qué lenguaje/framework estás trabajando? Si me compartes un snippet de tu llamada actual, te lo adapto directamente con retry seguro y te ayudo a integrar los headers de rate limit.