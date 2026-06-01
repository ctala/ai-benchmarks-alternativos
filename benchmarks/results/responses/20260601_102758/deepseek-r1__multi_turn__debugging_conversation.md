# DeepSeek R1 (reasoning) — multi_turn/debugging_conversation

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 7.5 | quality: 9.55
- latency_total: 50.974s | tokens_per_second: 23.4
- input_tokens: 332 | output_tokens: 1193
- judge_score: 5.0 | justificación: 

## Respuesta completa

¡Ahí está el problema! Un retry infinito sin backoff está saturando la API y empeorando el error 429. Aquí te explico cómo implementar retries correctamente:

### Solución con Backoff Exponencial + Jitter (Recomendado)
```python
import requests
import time
import random

def make_request_with_retry(payload, max_retries=5):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer TU_API_KEY",
        "Content-Type": "application/json"
    }
    
    retries = 0
    base_delay = 1  # Segundos iniciales
    
    while retries <= max_retries:
        response = requests.post(url, json=payload, headers=headers)
        
        # Éxito
        if response.status_code == 200:
            return response.json()
        
        # Manejo específico de 429
        elif response.status_code == 429:
            # Intenta leer headers de rate limit (si existen)
            reset_time = response.headers.get('x-ratelimit-reset')
            retry_after = response.headers.get('retry-after')
            
            # Calcula delay inteligente
            if retry_after:
                delay = int(retry_after)
            elif reset_time:
                delay = max(0, int(reset_time) - time.time())
            else:
                delay = base_delay * (2 ** retries) + random.uniform(0, 1)  # Backoff exponencial + jitter
            
            print(f"Error 429. Reintentando en {delay:.2f}s...")
            time.sleep(delay)
            retries += 1
        
        # Otros errores (no reintentables)
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

    raise Exception("Máximo de reintentos alcanzado")
```

### Elementos clave:
1. **Límite máximo de reintentos**: Evita loops infinitos (`max_retries=5`)
2. **Backoff exponencial**: El tiempo de espera se duplica en cada intento (`1s → 2s → 4s → 8s`)
3. **Jitter**: Añade aleatoriedad (`random.uniform(0,1)`) para evitar el "efecto estampida"
4. **Headers de rate limit**: Prioriza información del servidor:
   - `retry-after`: Tiempo sugerido para reintento
   - `x-ratelimit-reset`: Timestamp de reinicio del contador

### Uso:
```python
payload = {
    "model": "deepseek-ai/deepseek-coder",
    "messages": [{"role": "user", "content": "Hola"}]
}

try:
    response = make_request_with_retry(payload)
    print(response)
except Exception as e:
    print(f"Error permanente: {str(e)}")
```

### Alternativa con bibliotecas (para producción):
Usa herramientas robustas como:
```python
# Instalar primero: pip install tenacity
from tenacity import retry, wait_exponential, stop_after_attempt

@retry(
    wait=wait_exponential(multiplier=1, min=1, max=60),
    stop=stop_after_attempt(5),
    retry=(lambda e: isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 429)
)
def make_request():
    response = requests.post(...)
    response.raise_for_status()
    return response
```

> **Importante**: Si usas múltiples instancias/hilos, implementa rate limiting global (ej. con Redis) para evitar exceder el límite en toda tu aplicación.