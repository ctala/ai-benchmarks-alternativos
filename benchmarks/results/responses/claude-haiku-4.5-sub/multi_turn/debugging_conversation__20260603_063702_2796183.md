# Claude Haiku 4.5 (suscripción) — multi_turn/debugging_conversation

- model_id: `claude-haiku-4-5`
- success: True  | final: 8.02 | quality: 9.47
- latency_total: 8.981s | tokens_per_second: 107.7
- input_tokens: 10 | output_tokens: 967
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución detallada y práctica para el problema de rate limiting, con un enfoque en la implementación de exponential backoff con jitter, que es una estrategia avanzada y efectiva.

## Respuesta completa

Excelente diagnóstico. El loop de retry infinito es un clásico — cada 429 dispara más requests, creando una cascada. Voy a ayudarte implementar un sistema robusto. Primero necesito ver tu código:

**¿Me muestras dónde está ese loop de retry?** (archivo y líneas) 

Mientras tanto, te adelanto la solución correcta — implementar **exponential backoff con jitter**:

```python
import time
import random
from functools import wraps

def retry_with_backoff(max_retries=3, base_delay=1, max_delay=32):
    """
    Decorator para manejar rate limiting de forma segura.
    - max_retries: intentos totales antes de fallar
    - base_delay: segundos iniciales de espera (1s)
    - max_delay: techo máximo (32s)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # Si no es rate limit, propagar inmediatamente
                    if not is_rate_limit_error(e):
                        raise
                    
                    if attempt == max_retries - 1:
                        # Último intento fallido
                        raise
                    
                    # Exponential backoff: 1s, 2s, 4s, 8s...
                    delay = min(base_delay * (2 ** attempt), max_delay)
                    # Agregar jitter (random) para evitar thundering herd
                    jitter = random.uniform(0, delay * 0.1)
                    wait_time = delay + jitter
                    
                    print(f"Rate limited. Reintentando en {wait_time:.1f}s (intento {attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
            
        return wrapper
    return decorator

def is_rate_limit_error(error):
    """Detecta si el error es un 429 o similar"""
    error_str = str(error).lower()
    return "429" in error_str or "rate" in error_str or "too many requests" in error_str
```

**Uso:**
```python
@retry_with_backoff(max_retries=3)
def call_openrouter(prompt):
    # Tu llamada a OpenRouter aquí
    response = client.chat.completions.create(...)
    return response
```

**¿Cuál es tu situación?**

1. **Si usas `requests` o `httpx`**: puedo darte un adapter que respete los headers `retry-after` de OpenRouter
2. **Si usas `openai` SDK**: hay un built-in pero podemos mejorarlo
3. **Si es código custom**: necesito verlo para ajustar

Comparte el código y te doy la solución exacta. 👇