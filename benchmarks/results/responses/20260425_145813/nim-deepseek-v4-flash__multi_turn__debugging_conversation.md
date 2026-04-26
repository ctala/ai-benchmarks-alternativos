# DeepSeek V4 Flash (NIM) — multi_turn/debugging_conversation

- model_id: `deepseek-ai/deepseek-v4-flash`
- success: True  | final: 7.29 | quality: 8.83
- latency_total: 12.391s | tokens_per_second: 38.0
- input_tokens: 333 | output_tokens: 471
- judge_score: 4.6 | justificación: 

## Respuesta completa

Problema clasico! El retry esta causando una tormenta de requests. Aqui tienes una implementacion robusta:

```python
import time
import random
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),  # Maximo 3 intentos
    wait=wait_exponential(multiplier=1, min=4, max=60),  # Espera exponencial: 4s, 8s, 16s...
    retry_error_callback=lambda retry_state: None  # No reintentar si no es error recuperable
)
def call_api():
    response = openrouter_request()  # Tu llamada
    
    if response.status_code == 429:
        retry_after = int(response.headers.get('Retry-After', 60))
        time.sleep(retry_after)
        raise Exception("Rate limited")
    
    return response
```

Puntos clave:
- **stop_after_attempt(3)**: Limita a 3 intentos maximo
- **wait_exponential**: Espera 4s, 8s, 16s... (no 0.1s como antes)
- **Respetar Retry-After**: Usa el header que te manda el servidor
- **Random jitter**: Agrega random.uniform(0, 1) al sleep para evitar que todos los clientes se sincronicen

Implementacion manual si no quieres usar tenacity:

```python
def call_with_retry(max_retries=3):
    for attempt in range(max_retries):
        response = openrouter_request()
        
        if response.status_code == 429:
            if attempt == max_retries - 1:
                raise Exception("Max retries exceeded")
            
            wait_time = (2 ** attempt) + random.uniform(0, 1)  # 2s, 4s, 8s...
            time.sleep(wait_time)
            continue
        
        return response
    return None
```

El error original era que no tenias limite de intentos ni backoff. Asi evitas el loop infinito.