# Qwen 3.6 27B base (OpenRouter FP8) — multi_turn/debugging_conversation

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 47.043s | tokens_per_second: 46.7
- input_tokens: 340 | output_tokens: 2198

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

¡Excelente hallazgo! Un loop de retry infinito ante un `429` es una de las causas más comunes de bloqueo de API. OpenRouter (y la mayoría de proveedores) detectan esto como tráfico malicioso o mal configurado y pueden aplicar throttling temporal o incluso bloquear la key hasta que se estabilice.

Aquí tienes la guía paso a paso para implementar retries correctamente, adaptada a OpenRouter:

### 🔑 Principios de Retry Robusto
1. **Cap máximo de reintentos:** 3 a 5 intentos como máximo.
2. **Backoff exponencial:** `1s → 2s → 4s → 8s` (no lineal).
3. **Jitter:** Añadir ±20% de aleatoriedad para evitar el "thundering herd".
4. **Respetar `Retry-After`:** OpenRouter lo envía en el header del `429`. Úsalo como base.
5. **Retry selectivo:** Solo reintentar `429`, `5xx` y errores de red. **Nunca** `400`, `401`, `403` o `422`.

---

### 📦 Implementación (Ejemplos Product-Ready)

#### ✅ Python (`requests` o `httpx`)
```python
import time
import random
import requests

def call_openrouter_with_retry(url, headers, payload, max_retries=4):
    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=30)
            
            if resp.status_code == 429:
                # Respetar Retry-After si existe
                retry_after = int(resp.headers.get("Retry-After", 0))
                base_delay = max(retry_after, 2 ** attempt)
                jitter = random.uniform(0, base_delay * 0.2)
                wait = base_delay + jitter
                
                if attempt == max_retries:
                    raise Exception(f"Excedidos {max_retries} reintentos tras 429")
                print(f"429 recibido. Esperando {wait:.1f}s...")
                time.sleep(wait)
                continue
                
            resp.raise_for_status()
            return resp.json()
            
        except requests.exceptions.RequestException as e:
            if attempt == max_retries:
                raise Exception(f"Fallo tras {max_retries} intentos: {e}")
            time.sleep(2 ** attempt + random.uniform(0, 1))
            
    return None
```

#### ✅ JavaScript/Node (`fetch` + async/await)
```js
async function callOpenRouterWithRetry(url, options, maxRetries = 4) {
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      const res = await fetch(url, options);
      
      if (res.status === 429) {
        const retryAfter = parseInt(res.headers.get("Retry-After") || "0", 10);
        const baseDelay = Math.max(retryAfter, Math.pow(2, attempt));
        const jitter = Math.random() * baseDelay * 0.2;
        const wait = (baseDelay + jitter) * 1000; // a ms
        
        if (attempt === maxRetries) {
          throw new Error(`Excedidos ${maxRetries} reintentos tras 429`);
        }
        console.log(`429 recibido. Esperando ${(wait/1000).toFixed(1)}s...`);
        await new Promise(r => setTimeout(r, wait));
        continue;
      }
      
      if (!res.ok) throw new Error(`HTTP ${res.status}: ${res.statusText}`);
      return await res.json();
      
    } catch (err) {
      if (attempt === maxRetries) throw new Error(`Fallo tras ${maxRetries} intentos: ${err.message}`);
      await new Promise(r => setTimeout(r, Math.pow(2, attempt) * 1000));
    }
  }
}
```

---

### 🔍 Específico de OpenRouter
- Los headers de rate limit que envían:
  - `x-ratelimit-limit`: Límite de tokens/requests
  - `x-ratelimit-remaining`: Cuánto te queda
  - `x-ratelimit-reset`: Timestamp de reinicio
  - `Retry-After`: Segundos a esperar (prioriza este en 429)
- DeepSeek V3 en OpenRouter suele tener límites generosos (~300 RPM por modelo, ~60 RPM globales por key gratuita, pero tu key paga debería tener más). Si sigues viendo 429 tras arreglar el retry, revisa si estás haciendo llamadas concurrentes sin control.

---

### 🛠️ Siguientes pasos para diagnosticar
1. **Elimina el retry infinito** y prueba con el código de arriba.
2. **Agrega logging** de `x-ratelimit-*` y `Retry-After` para ver si OpenRouter está aplicando un límite global por key o por modelo.
3. Si usas **llamadas concurrentes**, añade un semáforo o cola (ej: `asyncio.Semaphore` en Python o `p-limit` en Node) para no superar ~10-15 req/s.
4. Verifica que no tengas **otro proceso/script** usando la misma key en segundo plano.

¿Qué lenguaje/framework estás usando? Te doy la implementación exacta adaptada a tu stack (FastAPI, Express, LangChain, etc.) y te ayudo a integrar métricas de consumo.