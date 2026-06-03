# Claude Sonnet 4.6 (suscripción) — multi_turn/debugging_conversation

- model_id: `claude-sonnet-4-6`
- success: True  | final: 7.59 | quality: 9.47
- latency_total: 15.871s | tokens_per_second: 60.0
- input_tokens: 3 | output_tokens: 953
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y profundiza en la solución al problema de rate limiting con un enfoque en exponential backoff con jitter, proporcionando un código detallado y alternativas de librería, lo cual es altamente útil y claro para un emprendedor.

## Respuesta completa

¡Ahí está el problema! Retry infinito es exactamente lo que satura el rate limit. La solución es **exponential backoff con jitter**:

## El patrón correcto

```python
import time
import random
import requests

def call_openrouter(payload, max_retries=5):
    base_delay = 1  # segundos
    
    for attempt in range(max_retries):
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json=payload
        )
        
        if response.status_code == 200:
            return response.json()
        
        if response.status_code == 429:
            if attempt == max_retries - 1:
                raise Exception(f"Rate limit después de {max_retries} intentos")
            
            # Leer el header Retry-After si existe
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                wait = float(retry_after)
            else:
                # Exponential backoff: 1s, 2s, 4s, 8s, 16s...
                wait = base_delay * (2 ** attempt)
            
            # Jitter: agrega hasta 1s aleatorio para evitar thundering herd
            wait += random.uniform(0, 1)
            
            print(f"429 recibido. Esperando {wait:.1f}s (intento {attempt + 1}/{max_retries})")
            time.sleep(wait)
            continue
        
        # Otros errores: NO reintentar
        response.raise_for_status()
```

## Los 3 principios clave

| Principio | Por qué |
|-----------|---------|
| **Máximo de reintentos** (ej: 5) | Evita el loop infinito |
| **Espera exponencial** (1s → 2s → 4s...) | Da tiempo al servidor para recuperarse |
| **Jitter aleatorio** (+0-1s) | Evita que múltiples workers hagan spike simultáneo |

## Lo que NO hacer

```python
# ❌ Esto es lo que tienes (mata tu rate limit)
while True:
    if response.status_code == 429:
        call_api()  # genera otros 100 requests

# ❌ Retry fijo sin espera
for i in range(10):
    if response.status_code == 429:
        call_api()  # 10 requests en milisegundos
```

## Si usas una librería (más simple)

Con `tenacity`:
```bash
pip install tenacity
```

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=1, max=60),
    retry=retry_if_exception(lambda e: "429" in str(e))
)
def call_openrouter(payload):
    # tu código aquí
```

---

**Resumen del fix**: agrega un límite de intentos + `time.sleep()` con espera creciente. El header `Retry-After` de OpenRouter te dice exactamente cuánto esperar — úsalo cuando esté disponible.

¿Quieres que revise tu código actual para ver dónde está el loop problemático?