# GLM 5 — multi_turn/debugging_conversation

- model_id: `z-ai/glm-5`
- success: True  | final: 8.65 | quality: 10.0
- latency_total: 15.487s | tokens_per_second: 42.7
- input_tokens: 322 | output_tokens: 661
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución detallada al problema de la API con errores 429, incluyendo un ejemplo de código en Python, lo que la hace altamente útil y clara.

## Respuesta completa

¡Esa es la causa! Un retry infinito con 429 crea un ciclo vicioso: el servidor te bloquea más y tú envías más requests.

Una implementación correcta de retries necesita:

**1. Límite máximo de reintentos** (3-5 es estándar)

**2. Exponential backoff** - esperar más tiempo entre cada retry:
- 1er retry: espera 1s
- 2do retry: espera 2s
- 3er retry: espera 4s
- etc.

**3. Jitter** - añadir aleatoriedad para evitar que todos los clientes se sincronicen

**4. Respetar el header `Retry-After`** si el servidor lo envía

---

Ejemplo en Python:

```python
import time
import random

def call_api_with_retry(api_func, max_retries=3):
    for attempt in range(max_retries + 1):
        response = api_func()
        
        if response.status_code == 200:
            return response
        
        if response.status_code == 429:
            if attempt == max_retries:
                raise Exception("Max retries exceeded")
            
            # Usar Retry-After del header, o calcular backoff
            retry_after = int(response.headers.get('Retry-After', 0))
            
            if retry_after > 0:
                wait_time = retry_after
            else:
                # Exponential backoff con jitter
                wait_time = (2 ** attempt) + random.uniform(0, 1)
            
            time.sleep(wait_time)
            continue
        
        # Otros errores: no reintentar
        raise Exception(f"API error: {response.status_code}")
```

¿Qué lenguaje estás usando? Te puedo dar el código específico o recomendarte una librería que maneje esto automáticamente.