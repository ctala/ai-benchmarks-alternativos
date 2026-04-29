# Gemma 4 31B (NIM) — multi_turn/debugging_conversation

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 7.9 | quality: 10.0
- latency_total: 38.954s | tokens_per_second: 24.3
- input_tokens: 356 | output_tokens: 946
- judge_score: 5.0 | justificación: 

## Respuesta completa

Ahí tienes el culpable. Has creado una **"tormenta de peticiones"** (retry storm). Al recibir el primer 429, tu código entra en pánico y bombardea el servidor, lo que hace que OpenRouter te bloquee por más tiempo, creando un círculo vicioso.

Para implementar retries de forma profesional, **nunca** uses un loop infinito o un retry inmediato. Debes implementar una estrategia de **Exponential Backoff con Jitter**.

Aquí tienes la guía paso a paso de cómo hacerlo:

### 1. El Concepto: Exponential Backoff + Jitter
*   **Exponential Backoff:** En lugar de reintentar cada 1 segundo, duplicas el tiempo de espera en cada fallo (1s, 2s, 4s, 8s...). Esto le da tiempo al servidor a "respirar".
*   **Jitter (Ruido):** Añades un número aleatorio pequeño al tiempo de espera. Si tienes 10 procesos fallando al mismo tiempo, el jitter evita que todos reintenten exactamente al mismo milisegundo, evitando nuevos picos de tráfico.

### 2. Implementación Recomendada (Python)

Si usas Python, no reinventes la rueda. Usa la librería `tenacity`, que es el estándar para esto:

```python
import random
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# Definimos una excepción personalizada para el 429
class RateLimitError(Exception):
    pass

# Configuración del Retry
@retry(
    # 1. Solo reintentar si es un error de Rate Limit (429)
    retry=retry_if_exception_type(RateLimitError), 
    # 2. Esperar exponencialmente: 2s, 4s, 8s... hasta un máximo de 60s
    wait=wait_exponential(multiplier=1, min=2, max=60), 
    # 3. Detenerse después de X intentos para no quedar en loop infinito
    stop=stop_after_attempt(5) 
)
def call_openrouter_api():
    response = make_api_request() # Tu función que hace el fetch/request
    
    if response.status_code == 429:
        print("Rate limit alcanzado. Reintentando con backoff...")
        raise RateLimitError("429 Too Many Requests")
    
    return response.json()
```

### 3. Si lo haces manualmente (Pseudocódigo/JS)

Si no quieres usar librerías, sigue esta lógica:

```javascript
async function fetchWithRetry(url, options, attempt = 0) {
    const MAX_ATTEMPTS = 5;
    const response = await fetch(url, options);

    if (response.status === 429 && attempt < MAX_ATTEMPTS) {
        // Cálculo: (2^attempt * 1000ms) + random jitter
        const backoff = Math.pow(2, attempt) * 1000;
        const jitter = Math.random() * 1000; 
        const delay = backoff + jitter;

        console.log(`Error 429. Reintentando en ${delay}ms...`);
        await new Promise(res => setTimeout(res, delay));
        
        return fetchWithRetry(url, options, attempt + 1);
    }
    return response;
}
```

### Resumen de Reglas de Oro para APIs:
1.  **Límite de Intentos:** Nunca pongas un `while(true)`. Pon un límite (ej. 5 intentos).
2.  **Espera Progresiva:** No reintentes inmediatamente.
3.  **Lee el Header `Retry-After`:** Algunas APIs (incluyendo OpenRouter a veces) envían un header llamado `Retry-After` que te dice exactamente cuántos segundos esperar. Si existe, prioriza ese valor sobre tu cálculo de backoff.

**Próximo paso:** Aplica esto, reinicia tu aplicación y espera unos 5-10 minutos antes de lanzar la primera petición para que el servidor de OpenRouter limpie tu "flag" de spam.