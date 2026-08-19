# Gemma 4 26B MoE (3.8B activos) — multi_turn/debugging_conversation

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 7.85 | quality: 9.72
- latency_total: 6.003s | tokens_per_second: 157.1
- input_tokens: 344 | output_tokens: 943
- judge_score: 4.8 | justificación: 

## Respuesta completa

¡Bingo! Acabas de encontrar el clásico problema de la **"Tormenta de Retries"** (Retry Storm). Al recibir un 429, tu código intenta desesperadamente reconectar, lo que satura la API, lo que genera más 429s, creando un bucle infinito que puede incluso hacer que OpenRouter te bloquee temporalmente por comportamiento abusivo.

Para arreglarlo profesionalmente, necesitas implementar una estrategia llamada **Exponential Backoff con Jitter**.

Aquí tienes los 3 pilares para solucionarlo:

### 1. Exponential Backoff (Retroceso Exponencial)
En lugar de reintentar inmediatamente o cada 1 segundo, debes aumentar el tiempo de espera exponencialmente entre cada intento.
*   Intento 1: esperar 1s
*   Intento 2: esperar 2s
*   Intento 3: esperar 4s
*   Intento 4: esperar 8s...

### 2. Jitter (Ruido aleatorio)
Si tienes varios procesos corriendo, todos reintentarán exactamente al mismo tiempo (ej. a los 2s, luego a los 4s). Esto crea "picos" de tráfico. El *Jitter* añade unos milisegundos aleatorios para esparcir las peticiones.
*   En lugar de 2s exactos, esperas `2s + random(0, 500ms)`.

### 3. Límite de reintentos (Max Retries)
**Nunca** uses un loop infinito. Debes definir un número máximo de intentos (ej. 5) y, si después de eso sigue fallando, lanzar una excepción o detener el proceso.

---

### Ejemplo de implementación (Python)

Si estás usando Python, no reinventes la rueda; usa la librería `tenacity`, que es el estándar de la industria para esto.

```python
import time
import random
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# Definimos una excepción personalizada para identificar errores de API
class RateLimitError(Exception):
    pass

# Configuración del decorador:
# - wait_exponential: Aplica el backoff (empezando en 1s, duplicando hasta un max de 60s)
# - stop_after_attempt: Deja de intentar tras 5 fallos (¡No más loops infinitos!)
# - retry_if_exception_type: Solo reintenta si es un error de Rate Limit
@retry(
    wait=wait_exponential(multiplier=1, min=2, max=60), 
    stop=stop_after_attempt(5),
    retry=retry_if_exception_type(RateLimitError)
)
def call_openrouter_api(payload):
    print(f"Intentando llamada a la API a las {time.strftime('%H:%M:%S')}...")
    
    # SIMULACIÓN DE TU LÓGICA ACTUAL
    response_status = simulate_api_call() # Aquí iría tu requests.post()
    
    if response_status == 429:
        print("¡Error 429 detectado! Aplicando backoff...")
        raise RateLimitError("Rate limit exceeded")
    
    return "Éxito"

def simulate_api_call():
    # Esto simula que la API te está dando error
    return 429 

# Ejecución
try:
    result = call_openrouter_api({"model": "deepseek/deepseek-chat"})
    print(result)
except Exception as e:
    print(f"El proceso falló definitivamente tras varios intentos: {e}")
```

### Resumen de tu Checklist de corrección:
1.  **Elimina el `while True`** o el loop sin condición de salida.
2.  **Agrega un contador de intentos** (`attempts < 5`).
3.  **Implementa el tiempo de espera variable** (si recibes 429, `sleep` antes de la siguiente vuelta).
4.  **Verifica el header `Retry-After`**: Algunas APIs te dicen exactamente cuántos segundos debes esperar en el header de la respuesta. Si OpenRouter te lo envía, ¡úsalo!