# Qwen 3.7 Flash — multi_turn/debugging_conversation

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.28 | quality: 10.0
- latency_total: 18.847s | tokens_per_second: 107.4
- input_tokens: 340 | output_tokens: 2024

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

Exactamente ese es el problema. Un retry infinito sobre un `429` crea un bucle de retroalimentación: cada intento fallido genera más intentos, saturando los límites y haciendo que la API te bloquee aún más rápido.

Aquí tienes la estrategia estándar para implementar retries de forma segura y escalable:

### 🔑 Principios clave
1. **Límite máximo de reintentos**: 3 a 5 intentos como máximo.
2. **Backoff exponencial con jitter**: `delay = min(2^attempt + random_jitter, cap)`
3. **Respetar `Retry-After`**: Si la API lo envía, úsalo directamente.
4. **Solo reintentar errores transitorios**: `429`, `502`, `503`, `504`. No reintentes `400`, `401`, `403`.
5. **Cap máximo de espera**: Nunca dejes que el delay supere ~30 segundos.

---

### 📦 Ejemplo en Python (lista para producción)
```python
import time
import random
import requests

def call_openrouter(payload, api_key, max_retries=3):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "tu-dominio.com",  # Recomendado por OpenRouter
        "X-Title": "NombreDeTuApp"
    }

    for attempt in range(max_retries):
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=30)

            if resp.status_code == 200:
                return resp.json()

            if resp.status_code == 429:
                # Priorizar Retry-After si existe
                retry_after = resp.headers.get("Retry-After")
                if retry_after:
                    wait = float(retry_after)
                else:
                    wait = min(2 ** attempt + random.uniform(0.5, 2.0), 30)
                
                print(f"⏳ Rate limit. Reintento {attempt+1}/{max_retries} en {wait:.1f}s")
                time.sleep(wait)
                continue

            # Errores no retryables o inesperados
            resp.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"🌐 Error de red: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt + random.uniform(0.5, 2.0))
            else:
                raise

    raise Exception("❌ Máximo de reintentos alcanzado")
```

---

### 💡 Recomendaciones adicionales
| Práctica | Por qué importa |
|----------|----------------|
| **Usa librerías especializadas** | `tenacity` (Python) o `async-retry` (Node.js) manejan backoff, jitter, circuit breakers y logging automáticamente. |
| **Monitorea `x-ratelimit-remaining`** | OpenRouter lo devuelve en cada respuesta. Si llega a `0`, pausa tu flujo antes de hacer la siguiente request. |
| **No hagas requests en paralelo sin control** | Si usas `asyncio` o `ThreadPoolExecutor`, limita la concurrencia con semáforos o colas. |
| **Logging estructurado** | Guarda `status_code`, `attempt`, `delay`, y `x-ratelimit-reset` para debuggear picos futuros. |

---

¿En qué lenguaje/framework estás trabajando? Te paso una versión optimizada con librería nativa (`tenacity`, `axios-retry`, etc.) y te ayudo a integrarlo en tu código actual.