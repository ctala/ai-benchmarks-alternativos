# Gemma 4 31B (DGX Spark Q4_K_M) — multi_turn/debugging_conversation

- model_id: `gemma4:31b`
- success: True  | final: 7.1 | quality: 9.72
- latency_total: 181.335s | tokens_per_second: 9.3
- input_tokens: 342 | output_tokens: 1684
- judge_score: 4.8 | justificación: 

## Respuesta completa

Exacto, acabas de crear un "ataque de denegación de servicio" (DoS) contra tu propia cuenta. Cuando el servidor te dice "detente", tu código responde "¡hazlo más rápido!", lo que provoca que OpenRouter bloquee tu IP o tu Key por un periodo más largo.

Para arreglar esto, debes implementar una estrategia llamada **Exponential Backoff con Jitter**. 

### ¿Qué es el Exponential Backoff con Jitter?
1. **Exponential Backoff:** En lugar de reintentar inmediatamente, esperas un tiempo que crece exponencialmente (ej. 1s, 2s, 4s, 8s...).
2. **Jitter (Ruido):** Añades un pequeño tiempo aleatorio para evitar que, si tienes varios procesos, todos reintenten exactamente al mismo milisegundo.

Aquí tienes cómo implementarlo correctamente en Python. Tienes dos opciones: la manual y la profesional.

---

### Opción 1: Implementación Manual (Sin librerías externas)
Ideal si quieres entender la lógica o mantener el código ligero.

```python
import time
import random
import requests

def call_openrouter_with_retry(payload, max_retries=5):
    base_delay = 1  # Segundo inicial
    
    for attempt in range(max_retries):
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer YOUR_KEY"},
            json=payload
        )
        
        if response.status_code == 200:
            return response.json()
        
        # SOLO reintentamos si es 429 (Rate Limit) o 5xx (Error de servidor)
        if response.status_code == 429 or 500 <= response.status_code < 600:
            # Cálculo de espera: (2^attempt) + ruido aleatorio
            wait_time = (base_delay * (2 ** attempt)) + random.uniform(0, 1)
            print(f"Error {response.status_code}. Reintentando en {wait_time:.2f}s... (Intento {attempt+1}/{max_retries})")
            time.sleep(wait_time)
        else:
            # Si es 400, 401, 403, etc., NO reintentamos porque el error es nuestro
            print(f"Error crítico {response.status_code}: {response.text}")
            break
            
    raise Exception("Se alcanzó el máximo de reintentos o ocurrió un error irreparable.")
```

---

### Opción 2: La forma profesional (Usando la librería `tenacity`)
En entornos de producción, no escribimos el loop a mano; usamos `tenacity`. Es la librería estándar para manejar retries en Python.

**Instalación:** `pip install tenacity`

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

# Definimos una excepción personalizada para el Rate Limit
class RateLimitError(Exception):
    pass

def is_rate_limit_error(exception):
    # Solo reintentamos si es nuestra excepción de RateLimit
    return isinstance(exception, RateLimitError)

@retry(
    stop=stop_after_attempt(5), 
    wait=wait_exponential(multiplier=1, min=2, max=10), # Espera: 2s, 4s, 8s... hasta 10s
    retry=retry_if_exception_type(RateLimitError)
)
def call_api(payload):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer YOUR_KEY"},
        json=payload
    )
    
    if response.status_code == 429:
        raise RateLimitError("Too Many Requests")
    
    response.raise_for_status() # Lanza error para otros códigos (400, 500, etc)
    return response.json()
```

### Reglas de oro para tus Retries:

1. **No reintentes errores 400, 401 o 403:** Si el error es "Invalid API Key" (401) o "Bad Request" (400), reintentar un millón de veces no cambiará el resultado y solo gastarás recursos.
2. **Límite máximo (Stop condition):** Siempre pon un `max_retries`. Un loop infinito es la receta perfecta para que te baneen la cuenta.
3. **Lee el header `retry-after`:** Algunas APIs (incluyendo OpenRouter a veces) envían un header llamado `retry-after` que te dice exactamente cuántos segundos esperar. Si existe, es mejor usar ese valor que el cálculo exponencial.

**Consejo final:** Como ya provocaste muchos 429s, es posible que estés en una "lista negra" temporal. Si después de arreglar el código sigues recibiendo 429s inmediatos, espera 15 minutos sin hacer ninguna llamada para que el contador de OpenRouter se resetee.