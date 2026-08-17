# Ministral 14B — multi_turn/debugging_conversation

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 9.15 | quality: 10.0
- latency_total: 10.666s | tokens_per_second: 86.4
- input_tokens: 325 | output_tokens: 922
- judge_score: 5.0 | justificación: 

## Respuesta completa

Perfecto! **Los retries son la solución, pero deben manejarse con cuidado** para no empeorar el problema. Aquí tienes una implementación profesional usando un **exponential backoff** (retardo exponencial) y análisis de headers de rate limit:

---

### **Solución 1: Retry con Exponential Backoff (Python)**
```python
import time
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

# Función para realizar la petición con retry
@retry(
    stop=stop_after_attempt(5),  # Máximo 5 intentos
    wait=wait_exponential(multiplier=1, min=2, max=10),  # Retardo: 2s, 4s, 8s, etc.
    retry_error_callback=lambda _: True,  # Retry en cualquier error
)
def call_openrouter_prompt(prompt, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        json={"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]},
        headers=headers,
    )
    response.raise_for_status()  # Lanza error si falla
    return response.json()

# Ejemplo de uso
try:
    result = call_openrouter_prompt("Hola OpenRouter", "tuyo_api_key")
    print(result)
except Exception as e:
    print(f"Error tras retries: {e}")
```

---

### **Claves para un Retry seguro**:
1. **Exponential Backoff**:
   - Empieza con `2s` de espera, luego `4s`, `8s` (evita saturar la API).
   - La librería `tenacity` lo implementa automáticamente.

2. **Análisis de Headers**:
   - Si la respuesta 429 incluye `Retry-After: 30`, usa ese valor exacto:
     ```python
     if response.status_code == 429:
         retry_after = int(response.headers.get('Retry-After', 5))  # Valor mínimo 5s
         time.sleep(retry_after)
         return call_openrouter_prompt(prompt, api_key)  #Retry manual
     ```

3. **Límites por Modelo**:
   - DeepSeek es **100 RPM** (no 300). Si superas eso, los retries no servirán.
   - **Solución**: Aumenta el tiempo entre requests o reduce la carga.

---

### **Solución 2: Manejo Manual (para casos simples)**
```python
def retry_with_delay(prompt, api_key, max_retries=5):
    last_status = None
    for attempt in range(max_retries):
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                json={"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]},
                headers={"Authorization": f"Bearer {api_key}"}
            )
            if response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', 2 ** attempt))
                print(f"Rate limit hit. Retrying in {retry_after}s...")
                time.sleep(retry_after)
                continue
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
    raise Exception("All retries failed")
```

---

### **Recomendaciones Finales**:
- **Monitorea tu uso**: Usa un dashboard para ver si realmente excedes los 100 RPM de DeepSeek.
- **Diferencia `stop` y `wait`**: El backoff exponencial evita el "thundering herd" (muchos retries al mismo tiempo).
- **Prueba con 1 request cada 10 segundos** al principio para calibrar.

Si el problema persiste, revisa si hay un **bug en el código que dispara múltiples requests simultáneos** (ej: hilos/promesas mal manejados).