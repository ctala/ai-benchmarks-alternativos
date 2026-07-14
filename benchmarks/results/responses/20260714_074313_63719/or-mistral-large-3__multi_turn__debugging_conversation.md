# Mistral Large 3 675B — multi_turn/debugging_conversation

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 16.061s | tokens_per_second: 67.0
- input_tokens: 325 | output_tokens: 1076
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución detallada y práctica para el problema de la API con errores 429, utilizando estrategias de reintentos avanzadas.

## Respuesta completa

¡Ahí está el problema! Un loop infinito de retries es peligroso. Vamos a implementar una estrategia de **exponential backoff con jitter** (reintentos con espera progresiva y aleatorización para evitar colisiones). Aquí te muestro cómo hacerlo correctamente en Python:

### Solución robusta (usando `tenacity`):
```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    RetryError
)
import requests
import time
from requests.exceptions import RequestException

# Configuración de retries
@retry(
    stop=stop_after_attempt(5),  # Máximo 5 intentos
    wait=wait_exponential(multiplier=1, min=4, max=10),  # Espera: 4s, 8s, 16s, etc (con max 10s)
    retry=retry_if_exception_type((RequestException, requests.HTTPError)),
    reraise=True  # Re-lanza la última excepción si falla
)
def call_openrouter_api(payload, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=30  # Timeout de 30 segundos
    )

    # Manejo específico de 429
    if response.status_code == 429:
        retry_after = int(response.headers.get("Retry-After", 5))  # Default 5s si no viene
        print(f"Rate limited. Retrying after {retry_after} seconds...")
        raise requests.HTTPError("429 Too Many Requests", response=response)

    response.raise_for_status()  # Lanza excepción para otros códigos de error
    return response.json()

# Uso:
try:
    result = call_openrouter_api(payload, "tu_api_key")
    print(result)
except RetryError as e:
    print(f"Fallo después de retries: {e.last_attempt.exception()}")
except Exception as e:
    print(f"Error inesperado: {e}")
```

---

### Alternativa manual (sin librerías):
```python
import requests
import time
import random

def call_openrouter_api(payload, api_key, max_retries=5):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    for attempt in range(max_retries):
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 2 ** attempt + random.uniform(0, 1)))
                print(f"Intento {attempt + 1}: Rate limited. Esperando {retry_after}s...")
                time.sleep(retry_after)
                continue

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise  # Re-lanza la última excepción
            wait_time = 2 ** attempt + random.uniform(0, 1)  # Exponential backoff + jitter
            print(f"Intento {attempt + 1} fallido. Esperando {wait_time:.2f}s...")
            time.sleep(wait_time)

# Uso:
try:
    result = call_openrouter_api(payload, "tu_api_key")
    print(result)
except Exception as e:
    print(f"Error: {e}")
```

---

### Claves del diseño:
1. **Exponential backoff**: La espera aumenta exponencialmente (1s, 2s, 4s, 8s...) para dar tiempo a que se libere el rate limit.
2. **Jitter**: Se añade un pequeño random (0-1s) para evitar que todos los clientes reintenten al mismo tiempo.
3. **Límite de intentos**: Máximo 5 retries (ajustable) para evitar loops infinitos.
4. **Manejo específico de 429**: Respeta el header `Retry-After` si está presente.
5. **Timeout**: Siempre usa timeouts para evitar bloqueos.

---

### Recomendaciones adicionales:
1. **Cachea respuestas**: Si haces requests idénticas, guarda el resultado para evitar repetirlas.
2. **Usa colas**: Para producción, considera usar una cola (como Celery o RabbitMQ) para manejar requests de forma asíncrona.
3. **Monitorea**: Implementa logging para trackear cuántos retries ocurren y detectar problemas temprano.

¿Necesitas adaptar esto a otro lenguaje o framework?