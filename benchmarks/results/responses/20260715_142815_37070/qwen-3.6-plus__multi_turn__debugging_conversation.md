# Qwen 3.6 Plus — multi_turn/debugging_conversation

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 43.001s | tokens_per_second: 54.0
- input_tokens: 340 | output_tokens: 2321
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución detallada y práctica al problema de la API con errores 429, incluyendo ejemplos de código y recomendaciones de librerías.

## Respuesta completa

Ese loop infinito es un clásico. Un `429` dispara el retry → el retry satura el límite → llega otro `429` → se repite hasta quemar créditos o bloquear la IP. 

Para solucionarlo de forma profesional, tu lógica de retry debe seguir **4 reglas de oro**:

### 🔑 Las 4 reglas de un retry seguro
1. **Límite máximo de intentos**: Nunca más de 3-5 retries. Si falla después de eso, falla.
2. **Exponential Backoff**: Espera cada vez más tiempo (`1s → 2s → 4s → 8s...`)
3. **Jitter (aleatoriedad)**: Añade un pequeño valor aleatorio para evitar que múltiples scripts colisionen en el mismo milisegundo.
4. **Respeta `Retry-After`**: Si la API te dice cuánto esperar, obedécelo. Es más preciso que tu backoff.

---

### 🛠️ Ejemplo práctico (Python)
```python
import time
import random
import requests

def call_openrouter(url, headers, payload, max_retries=3, base_delay=1.0):
    for attempt in range(max_retries + 1):
        try:
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 200:
                return response.json()
                
            elif response.status_code == 429:
                # 1️⃣ Prioridad: header Retry-After
                retry_after = response.headers.get("Retry-After")
                if retry_after:
                    wait = float(retry_after)
                else:
                    # 2️⃣ Backoff exponencial + jitter
                    wait = (base_delay * (2 ** attempt)) + random.uniform(0, 1)
                
                print(f"⏳ Rate limit. Esperando {wait:.1f}s (intento {attempt+1}/{max_retries})")
                time.sleep(wait)
                continue
                
            else:
                # Errores 4xx/5xx no retryables (excepto 429)
                response.raise_for_status()
                
        except requests.RequestException as e:
            print(f"🌐 Error de red: {e}")
            if attempt < max_retries:
                time.sleep(base_delay * (2 ** attempt))
                continue
            raise
            
    raise RuntimeError("❌ Máximo de retries excedido. La API sigue rechazando requests.")
```

---

### 📦 Alternativa recomendada (librerías)
No reinventes la rueda en producción. Usa librerías probadas:
- **Python**: `tenacity` o `backoff`
  ```python
  from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
  import requests

  @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
  def safe_call():
      r = requests.post(url, headers=headers, json=payload)
      r.raise_for_status()
      return r.json()
  ```
- **Node.js**: `axios-retry` o `p-retry`
- **Go**: `github.com/cenkalti/backoff/v4`

---

### 🔍 Tips específicos para OpenRouter
1. OpenRouter **sí devuelve `Retry-After`** en los `429`. Úsalo siempre.
2. Revisa estos headers en cada respuesta:
   - `x-ratelimit-limit`: Límite total del modelo/proveedor
   - `x-ratelimit-remaining`: Cuánto te queda
   - `x-ratelimit-reset`: Timestamp cuando se reinicia el contador
3. DeepSeek V3 suele tener límites de ~300 RPM / 30k TPM. Con 5 req/min no deberías tocar techo. El problema era 100% el loop infinito.
4. Si usas `stream: true`, cuenta cada chunk como parte de la misma request, no como requests separadas.

---

### ✅ Siguientes pasos
1. Implementa el backoff + `max_retries=3`
2. Loguea `x-ratelimit-remaining` para ver si realmente estás cerca del límite
3. Si sigues viendo `429` tras 1 intento limpio, comparte:
   - Tu lenguaje/framework
   - Si usas streaming o batch
   - El payload exacto (sin keys)

¿En qué stack estás trabajando? Te ajusto el código a tu lenguaje exacto.