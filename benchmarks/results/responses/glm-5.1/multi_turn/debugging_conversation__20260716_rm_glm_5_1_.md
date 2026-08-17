# GLM-5.1 — multi_turn/debugging_conversation

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.65 | quality: 10.0
- latency_total: 13.796s | tokens_per_second: 151.0
- input_tokens: 325 | output_tokens: 2083
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y prácticamente útil, abordando el problema de manera exhaustiva y proporcionando una solución detallada con un ejemplo de código.

## Respuesta completa

¡Excelente detective! Ese es exactamente el problema. Un loop de retry infinito ante un 429 crea un efecto de "tormenta de rayos" (thundering herd): la API te dice "espera", tu código la golpea más fuerte, ella te castiga con más 429s, y tu código la golpea aún más fuerte. 

Para arreglar esto de forma profesional, necesitas implementar un sistema de **Exponential Backoff con Jitter**. Aquí te explico los 4 principios básicos:

1. **Límite máximo (Max Retries):** Nunca hagas retries infinitos. Pon un tope (ej. 3 o 5 intentos).
2. **Backoff Exponencial:** Si falla, espera 1 segundo. Si falla de nuevo, espera 2. Luego 4, luego 8... así le das tiempo a la API para recuperarse.
3. **Jitter (Aleatoriedad):** Añadir un pequeño tiempo aleatorio al backoff evita que, si varias instancias de tu código fallan a la vez, todas reintenten exactamente al mismo segundo.
4. **Respetar el header `Retry-After`:** Muchas APIs (incluido OpenRouter) te dicen explícitamente cuánto tiempo debes esperar en el header de la respuesta.

Aquí tienes cómo implementarlo en Python usando la librería `requests`:

```python
import requests
import time
import random

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "tu-api-key"
MAX_RETRIES = 4

def call_api_with_retry(payload):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(API_URL, json=payload, headers=headers)
            
            # Si la petición es exitosa, devolvemos los datos
            if response.status_code == 200:
                return response.json()
            
            # Si es 429, calculamos el tiempo de espera
            if response.status_code == 429:
                # 1. Revisar si la API nos dice cuánto esperar
                retry_after = response.headers.get("Retry-After")
                if retry_after:
                    wait_time = int(retry_after)
                else:
                    # 2. Backoff exponencial con Jitter
                    # Intento 0: ~1s, Intento 1: ~2s, Intento 2: ~4s, Intento 3: ~8s
                    wait_time = (2 ** attempt) + random.uniform(0, 1)
                
                print(f"429 recibido. Reintentando en {wait_time:.2f} segundos (Intento {attempt + 1}/{MAX_RETRIES})...")
                time.sleep(wait_time)
                continue # Vuelve al inicio del loop
            
            # Si es otro error (ej. 401 Unauthorized, 400 Bad Request), no reintentar
            print(f"Error {response.status_code}: {response.text}")
            return None
            
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión: {e}")
            time.sleep(2 ** attempt) # Backoff básico para errores de red
            
    print("Se alcanzó el máximo de reintentos.")
    return None
```

### 💡 La alternativa "Modo Fácil" (Si usas el SDK de OpenAI)

Dado que OpenRouter es 100% compatible con el SDK de OpenAI para Python, la forma más fácil y robusta es usar su cliente oficial, que **ya tiene todo este sistema de reintentos programado por defecto**:

```python
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="tu-api-key",
  # El SDK de OpenAI ya hace backoff exponencial automático por defecto (max_retries=2)
  # Puedes subirlo si quieres:
  max_retries=3 
)

# Si recibe un 429, el SDK esperará y reintentará automáticamente sin que escribas nada extra
response = client.chat.completions.create(
  model="deepseek/deepseek-chat",
  messages=[{"role": "user", "content": "Hola"}]
)
```

**Resumen del paso a paso:**
1. Elimina el loop infinito de tu código actual.
2. Implementa el backoff exponencial manual (primer código) o cambia al SDK de OpenAI (segundo código).
3. Prueba de nuevo. Con 5 RPM reales y un backoff correcto, no deberías volver a ver el error 429.