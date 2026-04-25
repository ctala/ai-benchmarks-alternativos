# Devstral 2 (Dic 2025) — multi_turn/debugging_conversation

- model_id: `mistralai/devstral-2512`
- success: True  | final: 7.5 | quality: 8.99
- latency_total: 8.663s | tokens_per_second: 65.8
- input_tokens: 325 | output_tokens: 570
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Ahí está el problema! Un retry infinito es peligroso. Vamos a implementar un sistema de retries inteligente con estas características:

### Solución recomendada (Python con `tenacity`):

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import openai  # o tu cliente de OpenRouter
import time

# Configuración de retries
@retry(
    stop=stop_after_attempt(3),  # Máximo 3 intentos
    wait=wait_exponential(multiplier=1, min=4, max=10),  # Espera exponencial: 4s, 8s, 16s...
    retry=retry_if_exception_type(openai.RateLimitError)  # Solo retry en 429
)
def call_openrouter(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )
        return response
    except openai.RateLimitError as e:
        print(f"Rate limit alcanzado. Retry en {e.retry_after} segundos...")
        time.sleep(e.retry_after)  # Usa el tiempo sugerido por la API
        raise  # Esto activa el retry de tenacity
```

### Alternativa sin librerías (backoff manual):

```python
import time
import random

def call_with_retry(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = openai.ChatCompletion.create(...)
            return response
        except openai.RateLimitError as e:
            if attempt == max_retries - 1:
                raise

            # Backoff exponencial con jitter
            wait_time = min(2 ** attempt + random.uniform(0, 1), 10)
            print(f"Retry {attempt + 1}/{max_retries}. Esperando {wait_time:.1f}s...")
            time.sleep(wait_time)
```

### Buenas prácticas:
1. **Límite de intentos**: Nunca más de 3-5 retries
2. **Backoff exponencial**: Espera más tiempo entre cada retry (4s → 8s → 16s)
3. **Jitter**: Añade aleatoriedad para evitar sincronización de requests
4. **Respetar headers**: Usa `Retry-After` si viene en la respuesta
5. **Logging**: Registra los retries para debugging

¿Quieres que adapte el código a tu lenguaje específico o que revise tu implementación actual?