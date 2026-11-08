# Qwen 3.6 Plus — multi_turn/debugging_conversation

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 50.406s | tokens_per_second: 57.9
- input_tokens: 340 | output_tokens: 2920

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

Un **retry infinito sin backoff** es un clásico *retry storm*: cada error multiplica las llamadas, quema créditos rápidamente y puede hacer que OpenRouter bloquee tu API key por abuso. Vamos a arreglarlo con una estrategia de reintentos **segura, predecible y respetuosa con los límites**.

### 🔑 3 Reglas de Oro para Retries
1. **Nunca retries infinitamente**: Límite fijo (3-5 intentos).
2. **Backoff exponencial + jitter**: Espera `2^n` segundos + aleatoriedad para evitar colisiones.
3. **Respeta `Retry-After`**: OpenRouter lo devuelve en 429. Úsalo si existe.

---

### 🐍 Python (Recomendado: `tenacity`)
```python
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential_jitter, retry_if_exception_type
import random

def is_retryable_error(exception):
    if isinstance(exception, httpx.HTTPStatusError):
        return exception.response.status_code in (429, 500, 502, 503, 504)
    return False

@retry(
    stop=stop_after_attempt(3),  # Máximo 3 intentos
    wait=wait_exponential_jitter(initial=1, max=30),  # 1s, 2s, 4s + jitter
    retry=retry_if_exception_type((httpx.HTTPStatusError,)),
    before_sleep=lambda retry_state: print(f"⏳ Reintento {retry_state.attempt_number}...")
)
def call_openrouter(prompt: str, api_key: str):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {"model": "deepseek/deepseek-chat", "messages": [{"role": "user", "content": prompt}]}
    
    response = httpx.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=30)
    
    # Si es 429, extrae Retry-After si existe
    if response.status_code == 429:
        retry_after = response.headers.get("retry-after")
        if retry_after:
            # Tenacity lo manejará, pero puedes loguearlo
            print(f"📉 OpenRouter pide esperar {retry_after}s")
        response.raise_for_status()  # Lanza error para que tenacity reintente
        
    response.raise_for_status()
    return response.json()
```
📦 Instala: `pip install httpx tenacity`

---

### 🟨 JavaScript / Node.js (Nativo `fetch`)
```javascript
async function fetchWithRetry(url, options, maxRetries = 3) {
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      const res = await fetch(url, options);
      
      if (res.status === 429) {
        const retryAfter = res.headers.get('retry-after');
        const waitMs = retryAfter ? parseInt(retryAfter) * 1000 : (Math.pow(2, attempt) * 1000 + Math.random() * 500);
        console.warn(`⚠️ Rate limit 429. Esperando ${Math.round(waitMs/1000)}s...`);
        await new Promise(r => setTimeout(r, waitMs));
        continue;
      }
      
      if (!res.ok) throw new Error(`HTTP ${res.status}: ${res.statusText}`);
      return await res.json();
      
    } catch (err) {
      if (attempt === maxRetries) throw err;
      const delay = Math.pow(2, attempt) * 1000 + Math.random() * 500;
      console.warn(`❌ Error: ${err.message}. Reintento en ${Math.round(delay/1000)}s...`);
      await new Promise(r => setTimeout(r, delay));
    }
  }
}

// Uso:
// const data = await fetchWithRetry(
//   "https://openrouter.ai/api/v1/chat/completions",
//   { method: "POST", headers: { "Authorization": `Bearer ${KEY}`, "Content-Type": "application/json" }, body: JSON.stringify(payload) }
// );
```

---

### 🛡️ Protecciones Extra (Crítico para APIs de pago)
1. **Límite de gasto por minuto/hora**: Lleva un contador local. Si superas X req/min o $X, frena y alerta.
2. **Circuit Breaker**: Si recibes 5 errores seguidos en 1 min, pausa las llamadas 5-10 min. (Librerías: `pybreaker` en Python, `opossum` en JS).
3. **Log estructurado**: Registra `status`, `retry-after`, `model`, `tokens_used` para auditar consumo.
4. **Verifica en Dashboard**: Ve a [OpenRouter Dashboard](https://openrouter.ai/dashboard) → `Usage`. Confirma que no hay un límite de cuenta o modelo activado.

---

### ✅ Checklist Rápido
- [ ] Máximo 3-5 retries
- [ ] Backoff exponencial + jitter
- [ ] Leer `Retry-After` header si existe
- [ ] Solo reintentar 429 y 5xx (nunca 400, 401, 403)
- [ ] Límite de gasto local o en código
- [ ] Revisar logs de OpenRouter para confirmar que el 429 era por tu retry storm

¿En qué lenguaje/framework estás implementando esto? Te doy una versión ajustada a tu stack exacto y te ayudo a integrar un guard de presupuesto si lo necesitas.