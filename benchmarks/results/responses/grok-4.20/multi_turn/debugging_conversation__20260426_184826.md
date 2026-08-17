# Grok 4.20 — multi_turn/debugging_conversation

- model_id: `x-ai/grok-4.20`
- success: True  | final: 7.15 | quality: 8.99
- latency_total: 10.689s | tokens_per_second: 66.0
- input_tokens: 424 | output_tokens: 705
- judge_score: 4.6 | justificación: 

## Respuesta completa

**¡Ese es exactamente el problema!** Tienes un **retry storm** (tormenta de reintentos). El error 429 se convierte en cientos de requests, lo que hace que OpenRouter te bloquee más fuerte.

### ✅ Mejor forma de implementar retries con OpenRouter (2025)

Aquí te dejo una implementación recomendada usando **exponential backoff + jitter**:

### Python (recomendado)

```python
import time
import random
from openai import OpenAI
from openai import RateLimitError, APIError

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="tu-clave-aqui",
)

def call_openrouter_with_retry(messages, model="deepseek/deepseek-chat", max_retries=5):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                timeout=60
            )
            return response

        except RateLimitError as e:
            # Error 429 - Rate Limit
            wait_time = (2 ** attempt) * 1.5 + random.uniform(0, 1)  # Exponential backoff + jitter
            
            print(f"Rate limit alcanzado (intento {attempt+1}/{max_retries}). Esperando {wait_time:.2f} segundos...")
            time.sleep(wait_time)
            
        except APIError as e:
            # Otros errores del servidor
            if attempt == max_retries - 1:
                raise
            wait_time = (2 ** attempt) * 2
            print(f"Error del servidor. Reintentando en {wait_time}s...")
            time.sleep(wait_time)
            
        except Exception as e:
            print(f"Error inesperado: {e}")
            raise
    
    raise Exception("Se agotaron todos los reintentos")
```

### Mejores prácticas para OpenRouter:

1. **No uses retry infinito** (nunca).
2. **Máximo 5-6 reintentos**.
3. **Usa exponential backoff** (2^attempt).
4. **Agrega jitter** (random) para evitar el "thundering herd".
5. **Respeta los headers de rate limit** (mejor aún):

### Versión aún mejor (usando los headers):

```python
def call_with_smart_retry(messages, model="deepseek/deepseek-chat"):
    for attempt in range(6):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
            )
            return response

        except RateLimitError as e:
            # Intentar leer los headers de rate limit
            retry_after = int(e.response.headers.get("retry-after", 0))
            
            if retry_after > 0:
                wait = retry_after
            else:
                wait = (2 ** attempt) * 2 + random.uniform(0, 2)
                
            print(f"Rate limit. Esperando {wait:.1f} segundos...")
            time.sleep(wait)
            
    raise Exception("Rate limit persistente después de múltiples intentos")
```

---

**Pregunta rápida para ayudarte mejor:**

¿Estás usando `openai` library o `requests` directamente?

Y ¿quieres que te dé también una versión usando `tenacity` (la librería más limpia y recomendada actualmente)?