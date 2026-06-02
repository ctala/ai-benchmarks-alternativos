# Qwen 3.6 35B base (OpenRouter FP8) — multi_turn/debugging_conversation

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 7.72 | quality: 9.55
- latency_total: 15.845s | tokens_per_second: 153.5
- input_tokens: 340 | output_tokens: 2432
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y profundiza en el problema con una solución detallada y ejemplos de código, manteniendo claridad y utilidad práctica, y sigue perfectamente el contexto de la conversación.

## Respuesta completa

El problema es clásico: un `retry` sin control de tiempo ni límite de intentos convierte un rate limit puntual en una tormenta de peticiones. OpenRouter (y casi cualquier API moderna) espera que sigas el estándar **Exponential Backoff + Jitter + Retry-After**.

Aquí tienes cómo implementarlo correctamente:

### 🔑 Patrón recomendado para 429
1. **Lee `Retry-After`** si la respuesta lo incluye (OpenRouter suele enviarlo).
2. Si no existe, usa **backoff exponencial**: `delay = base * 2^intentos`.
3. Añade **jitter aleatorio** para evitar sincronización masiva: `delay += random.uniform(0, delay * 0.2)`.
4. **Capa máxima** de espera (ej. 30s) y **máximo de reintentos** (3-5).
5. **No reintentar** otros errores (4xx/5xx distintos a 429).

---

### 🐍 Ejemplo en Python (sin dependencias)
```python
import time
import random
import requests

def call_openrouter(url, headers, payload, max_retries=3):
    for attempt in range(max_retries):
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            return response.json()
            
        if response.status_code == 429:
            # 1. Priorizar header oficial
            retry_after = response.headers.get('Retry-After')
            if retry_after:
                delay = float(retry_after)
            else:
                # 2. Backoff exponencial + jitter
                base_delay = 1.0
                delay = min(base_delay * (2 ** attempt) + random.uniform(0, 1), 30.0)
            
            print(f"⚠️ 429 | Reintentando en {delay:.2f}s (intento {attempt+1}/{max_retries})")
            time.sleep(delay)
            continue
            
        # Otros errores: no reintentar automáticamente
        response.raise_for_status()
        
    raise Exception(f"❌ Se excedieron {max_retries} reintentos por rate limit")
```

---

### 📦 Alternativa profesional: `tenacity` (Python)
Si usas Python, `tenacity` maneja todo esto de forma declarativa y robusta:
```bash
pip install tenacity
```
```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=30) + wait_exponential(multiplier=0.5, max=2), # jitter implícito
    retry=retry_if_exception_type(requests.HTTPError) if False else None, # mejor manejar status manualmente
    reraise=True
)
def call_openrouter_tenacity(url, headers, payload):
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 429:
        retry_after = response.headers.get('Retry-After')
        delay = float(retry_after) if retry_after else None
        raise requests.HTTPError(response=response, delay=delay) # tenacity no lee headers nativamente, mejor el manual arriba
    response.raise_for_status()
    return response.json()
```
*(Nota: Para `tenacity` con `Retry-After` automático, usa la librería `httpx` + `tenacity` o el enfoque manual de arriba, que es más predecible con APIs que devuelven headers personalizados).*

---

### 🔍 Headers clave de OpenRouter que debes inspeccionar
Cuando reciba 429, OpenRouter suele incluir:
- `Retry-After`: segundos exactos a esperar
- `X-RateLimit-Requests-Remaining`: peticiones restantes en el window
- `X-RateLimit-Requests-Reset`: timestamp UNIX cuando se resetea el contador

**Consejo pro:** Guarda estos headers y úsalos para ajustar tu tasa de envío *antes* de llegar al límite.

---

### ✅ Checklist para arreglar tu código
1. Elimina el `while True` o `for _ in range(inf)` en el retry.
2. Limita a `max_retries = 3` o `4`.
3. Añade `time.sleep()` calculado como arriba.
4. Verifica que solo reintentes en `429`.
5. Añade logging de los headers `X-RateLimit-*` para monitoreo.

¿Estás usando Python, Node.js, Go o otro lenguaje? Te paso la implementación exacta para tu stack. También dime si usas `requests`, `httpx`, `axios`, etc., y te ajusto el código.