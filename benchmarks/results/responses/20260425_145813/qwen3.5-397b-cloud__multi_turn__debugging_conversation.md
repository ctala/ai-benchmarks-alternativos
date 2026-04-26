# Qwen 3.5 397B (Ollama Cloud) — multi_turn/debugging_conversation

- model_id: `qwen3.5:397b-cloud`
- success: True  | final: 8.25 | quality: 10.0
- latency_total: 14.882s | tokens_per_second: 68.1
- input_tokens: 340 | output_tokens: 1013
- judge_score: 5.0 | justificación: 

## Respuesta completa

¡Excelente hallazgo! Ese es exactamente el problema. Un retry infinito sin control convierte un error temporal en un ataque DDoS contra tu propia API.

Aquí tienes la guía definitiva para implementar **retries inteligentes** que respeten los límites de OpenRouter:

### 1. La Estrategia Correcta: Backoff Exponencial con Jitter
No debes reintentar inmediatamente. Debes esperar un tiempo que aumenta exponencialmente y añadir aleatoriedad ("jitter") para evitar colisiones.

*   **Backoff Exponencial:** Espera 1s, luego 2s, 4s, 8s...
*   **Jitter:** Añade un poco de tiempo aleatorio para que los retries no se sincronicen.
*   **Límite Máximo:** Nunca más de 3 a 5 intentos. Si falla después de eso, el error es real y debes detenerte.
*   **Header `Retry-After`:** Si OpenRouter te dice exactamente cuánto esperar, obedece ese valor por encima del cálculo exponencial.

### 2. Implementación Recomendada (Python)
La forma más robusta es usar la librería `tenacity`, que maneja toda esta lógica por ti.

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

@retry(
    stop=stop_after_attempt(5),  # Máximo 5 intentos
    wait=wait_exponential(multiplier=1, min=2, max=60),  # Espera entre 2s y 60s
    retry=retry_if_exception_type(RateLimitError)  # Solo retry en errores específicos
)
def llamar_api(prompt):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {TU_API_KEY}"},
        json={"model": "deepseek/deepseek-chat", "messages": [{"role": "user", "content": prompt}]}
    )
    
    if response.status_code == 429:
        # Opcional: Leer header Retry-After si existe
        retry_after = response.headers.get('Retry-After')
        if retry_after:
            raise RateLimitError(f"Rate limit. Esperar {retry_after}s")
        raise RateLimitError("Rate limit excedido")
        
    response.raise_for_status()
    return response.json()
```

### 3. Solución Rápida (Sin librerías externas)
Si prefieres hacerlo manual en tu loop actual, implementa esta lógica básica:

```python
import time
import random

max_retries = 3
for intento in range(max_retries):
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        break # Éxito, salir del loop
        
    if response.status_code == 429:
        if intento == max_retries - 1:
            raise Exception("Límite de retries alcanzado")
        
        # Calcular espera: 2^intento + jitter aleatorio
        wait_time = (2 ** intento) + random.uniform(0, 1)
        print(f"Rate limit. Esperando {wait_time:.2f}s...")
        time.sleep(wait_time)
    else:
        raise Exception(f"Error no recuperable: {response.status_code}")
```

### 4. Verificación Final
1.  **Reinicia tu entorno:** Es posible que tu IP esté "caliente" temporalmente en el servidor de OpenRouter debido a la tormenta de requests anterior. Espera 5-10 minutos sin hacer llamadas antes de probar el nuevo código.
2.  **Logging:** Añade logs para cada retry. Te ayudará a ver si la estrategia está funcionando o si sigues recibiendo 429s constantes.
3.  **Circuit Breaker:** Si recibes 429s consecutivos incluso con los retries, detén tu aplicación por 1 minuto completo antes de reintentar.

Con esto, tus 5 requests por minuto deberían procesarse sin activar ninguna protección de rate limit.