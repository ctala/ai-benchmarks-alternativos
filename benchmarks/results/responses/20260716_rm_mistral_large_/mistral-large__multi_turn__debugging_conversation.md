# Mistral Large — multi_turn/debugging_conversation

- model_id: `mistralai/mistral-large`
- success: True  | final: 8.48 | quality: 10.0
- latency_total: 16.548s | tokens_per_second: 68.0
- input_tokens: 325 | output_tokens: 1126
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución detallada al problema del error 429, con ejemplos de código claros y útiles, manteniendo la coherencia con el contexto de la conversación.

## Respuesta completa

¡Ah, ese es el problema clásico del "retry storm"! Vamos a implementar una solución robusta paso a paso:

### 1. **Estrategia de Retry Básica (Exponential Backoff)**
```python
import time
import random
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_session_with_retry():
    session = requests.Session()
    retries = Retry(
        total=3,  # Número máximo de intentos
        backoff_factor=1,  # Tiempo base para el backoff (1s, 2s, 4s...)
        status_forcelist=[429, 500, 502, 503, 504],  # Códigos para reintentar
        allowed_methods=["POST", "GET"]  # Métodos permitidos
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session
```

### 2. **Lógica de Retry Manual (Más Control)**
Si prefieres manejarlo manualmente:
```python
import time
import random

def call_api_with_retry(api_call, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = api_call()
            if response.status_code == 429:
                # Extraer el tiempo de espera del header (si existe)
                retry_after = int(response.headers.get("Retry-After", 2 ** attempt + random.uniform(0, 1)))
                print(f"Rate limited. Waiting {retry_after}s (attempt {attempt + 1}/{max_retries})")
                time.sleep(retry_after)
                continue
            response.raise_for_status()  # Lanza error para otros códigos
            return response
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise  # Re-lanza el error si se agotaron los intentos
            wait_time = 2 ** attempt + random.uniform(0, 1)  # Exponential backoff + jitter
            print(f"Error: {e}. Retrying in {wait_time:.2f}s...")
            time.sleep(wait_time)
```

### 3. **Cómo Usarlo**
```python
# Ejemplo con la librería requests
def make_api_call():
    return requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"model": "deepseek/deepseek-chat", "messages": [...]}
    )

# Opción 1: Usando la sesión con retry automático
session = create_session_with_retry()
response = session.post(...)  # Maneja retries automáticamente

# Opción 2: Usando la función manual
response = call_api_with_retry(make_api_call)
```

### 4. **Recomendaciones Clave**
- **Jitter**: Añade aleatoriedad (`random.uniform(0, 1)`) para evitar que múltiples clientes se sincronicen.
- **Headers**: Siempre revisa `Retry-After` en la respuesta 429 (OpenRouter lo incluye).
- **Límites**: No excedas 3-5 retries para evitar loops infinitos.
- **Logging**: Registra los intentos fallidos para debugging.

### 5. **Ejemplo Completo con OpenRouter**
```python
import requests
import time
import random

API_KEY = "tu_api_key"
MAX_RETRIES = 3

def call_openrouter(messages):
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {API_KEY}"},
                json={
                    "model": "deepseek/deepseek-chat",
                    "messages": messages
                }
            )
            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 2 ** attempt))
                print(f"Rate limited. Waiting {retry_after}s...")
                time.sleep(retry_after)
                continue
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt == MAX_RETRIES - 1:
                raise Exception(f"Failed after {MAX_RETRIES} attempts: {e}")
            wait_time = 2 ** attempt + random.uniform(0, 1)
            print(f"Attempt {attempt + 1} failed. Retrying in {wait_time:.2f}s...")
            time.sleep(wait_time)
```

### 6. **Verificación**
- **Prueba con 1 request**: Asegúrate de que funcione sin retries.
- **Simula un 429**: Usa un proxy como Charles para forzar un 429 y verifica que el retry funcione.
- **Monitorea logs**: Confirma que no se hagan más de 5-6 requests en total por llamada.

Con esto deberías resolver el problema sin saturar la API. ¿Necesitas ajustar algo para tu caso específico?