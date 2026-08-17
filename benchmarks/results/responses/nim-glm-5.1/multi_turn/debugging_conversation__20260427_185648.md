# GLM 5.1 (NIM) — multi_turn/debugging_conversation

- model_id: `z-ai/glm-5.1`
- success: True  | final: 7.4 | quality: 9.72
- latency_total: 129.099s | tokens_per_second: 6.6
- input_tokens: 328 | output_tokens: 851
- judge_score: 4.8 | justificación: 

## Respuesta completa

¡Excelente detective work! Ese es un problema clásico: el efecto avalancha. Cada 429 genera más 429s en un bucle infinito.

Para implementar retries correctamente necesitas dos cosas: **Exponential Backoff** y **Jitter**. Aquí te explico cómo:

### 1. Exponential Backoff
En lugar de reintentar inmediatamente, esperas un tiempo que se duplica después de cada fallo:
- Intento 1 falla → esperas 1 segundo
- Intento 2 falla → esperas 2 segundos
- Intento 3 falla → esperas 4 segundos
- Intento 4 falla → esperas 8 segundos

### 2. Jitter (Aleatoriedad)
Si varios procesos reintentan al mismo tiempo, volverán a colapsar la API al mismo tiempo. El jitter añade un pequeño tiempo aleatorio para dispersar los retries.

---

### Ejemplo de implementación en Python

Aquí tienes una función robusta para manejar esto:

```python
import time
import random
import requests

def call_openrouter_with_retry(url, headers, payload, max_retries=5):
    for attempt in range(max_retries):
        response = requests.post(url, headers=headers, json=payload)
        
        # Si la respuesta es exitosa, devolvemos los datos
        if response.status_code == 200:
            return response.json()
        
        # Si es un error 429 (Rate Limit) o 503 (Servidor ocupado), hacemos retry
        if response.status_code in [429, 503]:
            # Calcular el backoff base: 2^intento (1, 2, 4, 8, 16...)
            wait_time = 2 ** attempt
            
            # Añadir Jitter: random entre 0 y 1 segundo
            jitter = random.uniform(0, 1)
            
            # Si la API nos dio el header Retry-After, lo usamos en vez de nuestro cálculo
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                wait_time = int(retry_after)
            
            total_wait = wait_time + jitter
            
            print(f"Error {response.status_code}. Reintentando en {total_wait:.2f}s (Intento {attempt + 1}/{max_retries})")
            time.sleep(total_wait)
            continue
        
        # Si es otro error (400, 401, 403, 500), no reintentamos y lanzamos excepción
        response.raise_for_status()
    
    raise Exception(f"Máximo de retries alcanzado ({max_retries}). Último status code: {response.status_code}")

# Uso:
url = "https://openrouter.ai/api/v1/chat/completions"
headers = {"Authorization": f"Bearer TU_API_KEY"}
payload = {"model": "deepseek/deepseek-chat", "messages": [{"role": "user", "content": "Hola"}]}

resultado = call_openrouter_with_retry(url, headers, payload)
```

### Las reglas de oro para los retries:
1. **Nunca retries infinitamente**: Pon un tope (5 es un buen estándar).
2. **Nunca hagas retry instantáneo en 429**: La API te está diciendo "espera", no "intenta de nuevo ya".
3. **Respeta el header `Retry-After`**: OpenRouter suele devolver este header indicando cuántos segundos exactos debes esperar. Si está presente, úsalo.
4. **No hagas retry en errores 4xx (excepto 429)****: Un error 400 (Bad Request) o 401 (Unauthorized) no se va a arreglar repitiendo la llamada; es un error en tu código.

Prueba esta implementación. Si tu código no es en Python, dime en qué lenguaje estás trabajando y te doy el equivalente.