# GLM 5.2 — multi_turn/debugging_conversation

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.27 | quality: 9.64
- latency_total: 26.54s | tokens_per_second: 72.7
- input_tokens: 331 | output_tokens: 1930
- judge_score: 4.8 | justificación: 

## Respuesta completa

¡Bingo! Ese es el problema. Un loop de retry infinito sin pausas crea un efecto "avalancha": la API te bloquea, tu código reintenta al instante, la API te bloquea más fuerte, y así sucesivamente hasta saturar todo.

Para arreglarlo, debes implementar **Exponential Backoff** (Retroceso exponencial) con un límite máximo de intentos. Aquí te explico cómo estructurarlo paso a paso:

### 1. Reglas de un buen sistema de Retries
*   **Límite máximo:** Nunca hagas retries infinitos. Un máximo de 3 a 5 intentos es lo estándar.
*   **Espera exponencial:** Si el primer intento falla, espera 1 segundo. Si el segundo falla, espera 2s, luego 4s, 8s... Esto le da tiempo a la API para recuperarse.
*   **Respeta el header `Retry-After`:** Muchas APIs devuelven este header en el error 429 indicando exactamente cuántos segundos debes esperar.
*   **No reintentes errores fatales:** Si te da un 401 (API key inválida) o 400 (Bad Request), reintentar no servirá de nada. Solo haz retry en 429 o errores 5xx (500, 502, 503).

### 2. Ejemplo de implementación en Python (usando `requests`)

Aquí tienes un patrón sólido y seguro para implementar:

```python
import time
import requests

def llamar_openrouter(prompt, max_retries=5):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer TU_API_KEY",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek/deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }

    for intento in range(max_retries):
        response = requests.post(url, headers=headers, json=payload)
        
        # Si todo va bien (200 OK)
        if response.status_code == 200:
            return response.json()
        
        # Si recibimos 429 (Rate Limit)
        if response.status_code == 429:
            # Intentamos leer el header 'Retry-After', si no existe, usamos retroceso exponencial (2^intento)
            retry_after = int(response.headers.get("Retry-After", 2 ** intento))
            print(f"Error 429. Esperando {retry_after} segundos antes del reintento {intento + 1}/{max_retries}...")
            time.sleep(retry_after)
            continue
            
        # Para errores 5xx (Server Error), también podemos reintentar
        if 500 <= response.status_code < 600:
            wait_time = 2 ** intento
            print(f"Error {response.status_code}. Reintentando en {wait_time} segundos...")
            time.sleep(wait_time)
            continue

        # Para cualquier otro error (400, 401, 403), lanzamos la excepción inmediatamente
        response.raise_for_status()

    # Si el loop termina y no hubo éxito
    raise Exception(f"Se superó el máximo de {max_retries} intentos. Última respuesta: {response.status_code}")

# Uso
try:
    resultado = llamar_openrouter("Hola, ¿cómo estás?")
    print(resultado['choices'][0]['message']['content'])
except Exception as e:
    print(e)
```

### 3. Alternativa más profesional (Librería `tenacity`)
Si no quieres escribir el loop a mano, en Python existe una librería excelente llamada `tenacity` que maneja esto de forma elegante:

```bash
pip install tenacity
```

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

# Configuramos el decorador
@retry(
    stop=stop_after_attempt(5), # Máximo 5 intentos
    wait=wait_exponential(multiplier=1, min=1, max=10), # Espera exponencial entre 1 y 10s
    retry=retry_if_exception_type(requests.exceptions.RequestException) # Solo reintenta en errores de red
)
def llamar_openrouter_tenacity(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": "Bearer TU_API_KEY"}
    payload = {"model": "deepseek/deepseek-chat", "messages": [{"role": "user", "content": prompt}]}
    
    response = requests.post(url, headers=headers, json=payload)
    
    # Si es 429 o 5xx, forzamos un error para que tenacity haga el retry
    if response.status_code == 429 or response.status_code >= 500:
        raise requests.exceptions.RequestException(f"Error {response.status_code}")
        
    response.raise_for_status() # Errores 4xx
    return response.json()
```

**Siguiente paso:** Reemplaza tu loop infinito actual con una de estas dos opciones. La avalancha de requests desaparecerá inmediatamente y el error 429 debería dejar de aparecer (a menos que genuinamente hagas 300 requests en un segundo, lo cual es difícil). 

¿En qué lenguaje estás programando o usas alguna librería específica para hacer las llamadas?