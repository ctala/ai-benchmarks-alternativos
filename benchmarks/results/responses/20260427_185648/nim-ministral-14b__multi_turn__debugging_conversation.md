# Ministral 14B (NIM) — multi_turn/debugging_conversation

- model_id: `mistralai/ministral-14b-instruct-2512`
- success: True  | final: 7.25 | quality: 8.99
- latency_total: 66.425s | tokens_per_second: 20.9
- input_tokens: 325 | output_tokens: 1391
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Perfecto que hayas identificado el problema! Para implementar los *retries* de manera inteligente sin saturar la API, sigue esta estrategia:

---

### **1. Implementación básica de retries con backoff exponencial**
Usa un algoritmo de *backoff exponencial* para manejar errores 429 (*Too Many Requests*) y otros errores temporales (como 5xx). Aquí un ejemplo en Python con `requests` y `time`:

```python
import time
import requests

def call_api_with_retry(url, headers, max_retries=5, initial_delay=1):
    retries = 0
    delay = initial_delay

    while retries < max_retries:
        try:
            response = requests.post(url, headers=headers)
            response.raise_for_status()  # Lanza error si no es 2xx
            return response.json()  # Asume que devolves JSON
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 429:  # Rate limit
                retry_after = int(err.response.headers.get('Retry-After', delay))
                print(f"Rate limit (429). Retrying after {retry_after} seconds...")
                time.sleep(retry_after)
            elif err.response.status_code in [500, 502, 503, 504]:  # Errores del servidor
                print(f"Server error ({err.response.status_code}). Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2  # Backoff exponencial
            else:  # Otros errores (ej: 401, 404)
                print(f"Error irreducible: {err}")
                return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

        retries += 1

    print("Se agotaron los retries.")
    return None
```

---

### **2. Claves para implementarlo correctamente**
#### **A. Respetar el `Retry-After` header**
- Si la respuesta 429 incluye el header `Retry-After` (en segundos), **usa ese valor exactamente**. Ejemplo:
  ```python
  retry_after = int(response.headers.get('Retry-After', 1))  # Valor mínimo: 1 segundo
  time.sleep(retry_after)
  ```
- Esto evita que tu código sature la API aún más.

#### **B. Límites de retries**
- Usa un `max_retries` bajo (ej: 3–5) para evitar loops infinitos.
- Para errores irreversibles (ej: 401, 404), **no intentes retry**.

#### **C. Backoff exponencial**
- Multiplica el delay por 2 cada retry (ej: 1s → 2s → 4s → 8s).
- Tiene un **límite máximo** (ej: 30 segundos) para no esperar horas.

#### **D. Manejo de bursts**
- Si estás usando un loop (ej: procesar un array de inputs), **no envíes todas las requests seguidas**. Usa `asyncio` o `concurrent.futures` con un *throttle* (ej: 1 request cada 2 segundos).

---

### **3. Ejemplo avanzado con `tenacity` (recomendado)**
La librería [`tenacity`](https://tenacity.readthedocs.io/) simplifica esto. Instálala:
```bash
pip install tenacity
```

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type, before_log
from requests.exceptions import HTTPError

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=1, max=30),
    retry=retry_if_exception_type(HTTPError),
    before=before_log(logger, logging.INFO),
)
def call_api(url, headers):
    response = requests.post(url, headers=headers)
    response.raise_for_status()  # Lanza HTTPError si no es 2xx
    return response.json()

# Uso:
result = call_api(url, headers)
```

---

### **4. Para tu caso específico (OpenRouter)**
- **Modelo DeepSeek V3**: Tiene un rate limit de **300 RPM** (según su docs). Si haces 5 requests/minuto, deberías estar bien, pero asegúrate de:
  - No tener múltiples instancias del cliente (ej: no crees un `openai.Client()` por cada request).
  - Verificar los headers de respuesta:
    ```python
    print(response.headers)  #Busca: x-ratelimit-limit, x-ratelimit-remaining, x-ratelimit-reset
    ```
  - Si usas `asyncio`, usa un semáforo para limitar concurrency:
    ```python
    import asyncio
    from openrouter import AsyncOpenAI

    semaphore = asyncio.Semaphore(10)  # Máximo 10 requests concurrentes

    async def call_model():
        async with semaphore:
            client = AsyncOpenAI()
            response = await client.chat.completions.create(...)
    ```

---

### **5. Debugging rápido**
Si aún falla, añade este logging para ver los headers de la respuesta 429:
```python
response = requests.post(url, headers=headers)
if response.status_code == 429:
    print("Headers:", response.headers)
    print("Body:", response.text)
```

---
### Resumen de pasos para arreglar:
1. **Elimina el retry infinito** y usa `max_retries`.
2. **Respetar `Retry-After`** si existe en el header 429.
3. **Añade backoff exponencial** (1s → 2s → 4s...).
4. **Límites de concurrency**: No envíes más de 300 requests/minuto (o el límite del modelo).
5. **Monitorea los headers** para ajustar el código.

Si después de esto sigue fallando, comparte:
- El código completo del retry.
- Un ejemplo de los headers de una respuesta 429.
- La cantidad exacta de requests que estas haciendo por minuto (usando `logging`).

¡Con esto deberías resolverlo!