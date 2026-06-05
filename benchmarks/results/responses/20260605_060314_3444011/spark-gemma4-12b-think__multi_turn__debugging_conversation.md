# Gemma 4 12B (Spark llama-server, reasoning) — multi_turn/debugging_conversation

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 54.884s | tokens_per_second: 25.7
- input_tokens: 342 | output_tokens: 1411
- judge_score: 5.0 | justificación: 

## Respuesta completa

Ese es el problema clásico: estás creando una **"Tormenta de Retries" (Retry Storm)**. Al recibir un 429, tu código intenta inmediatamente de nuevo, lo que satura el servidor y hace que el límite se mantenga activo, creando un bucle infinito de peticiones fallidas.

Para solucionar esto, debes implementar una estrategia de **Exponential Backoff con Jitter**. Aquí te explico cómo hacerlo correctamente:

### 1. El concepto clave: Exponential Backoff
En lugar de reintentar inmediatamente, debes esperar un tiempo que crece exponencialmente con cada fallo.
*   Fallo 1: Esperar 1 segundo.
*   Fallo 2: Esperar 2 segundos.
*   Fallo 3: Esperar 4 segundos.
*   Fallo 4: Esperar 8 segundos... y así sucesivamente.

### 2. El toque maestro: Jitter (Aleatoriedad)
Si tienes muchos procesos corriendo a la vez, todos esperarían exactamente 1, 2, 4 segundos. Esto haría que todos golpearan la API al mismo tiempo otra vez. El **Jitter** añade una pequeña variación aleatoria (ej. 1.2s, 2.4s, 4.1s) para dispersar las peticiones.

---

### Cómo implementarlo (Ejemplo en Python)

Si usas Python, la mejor forma de hacer esto de manera profesional es con la librería `tenacity`. Si no quieres usar librerías, te doy el ejemplo manual abajo.

#### Opción A: Usando `tenacity` (Recomendado)
Esta librería maneja todo automáticamente por ti.

```python
from tenacity import retry, stop_after_attempt, wait_random_exponential, retry_if_exception_type
import requests

# Definimos que reintente si recibe un error 429
# wait_random_exponential espera tiempos crecientes con aleatoriedad
@retry(
    wait=wait_random_exponential(min=1, max=60), 
    stop=stop_after_attempt(5), # Máximo 5 intentos
    reraise=True
)
def call_openrouter_api(payload):
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload)
    
    # Si es 429, lanzamos una excepción para que 'tenacity' capture el reintento
    if response.status_code == 429:
        raise Exception("Rate limit hit")
        
    return response.json()
```

#### Opción B: Implementación Manual (Si no quieres librerías)
Si prefieres escribir tu propia lógica, estructura tu bucle así:

```python
import time
import random
import requests

def call_with_retry(payload, max_retries=5):
    retries = 0
    while retries < max_retries:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload)
        
        if response.status_code == 200:
            return response.json()
            
        elif response.status_code == 429:
            retries += 1
            # Cálculo: 2^retries + un poco de aleatoriedad
            wait_time = (2 ** retries) + random.uniform(0, 1)
            print(f"Error 429. Reintentando en {wait_time:.2f} segundos... (Intento {retries}/{max_retries})")
            time.sleep(wait_time)
            
        else:
            # Para otros errores (400, 500, etc) no queremos reintentar infinitamente
            response.raise_for_status()

    raise Exception("Máximo de reintentos alcanzado")
```

### Resumen de reglas de oro para tu API:
1.  **Límite de intentos:** Nunca permitas un reintento infinito. Pon un tope (ej. 5 intentos).
2.  **Respeta el `Retry-After`:** Si el header de OpenRouter incluye `Retry-After`, usa ese valor exacto en lugar de tu propio cálculo.
3.  **Logueo:** Imprime siempre en consola cuántos reintentos lleva cada petición para que puedas monitorear si tu código está "luchando" demasiado con la API.

**¿En qué lenguaje estás programando?** Si me dices el lenguaje, puedo darte el código exacto para tu stack.