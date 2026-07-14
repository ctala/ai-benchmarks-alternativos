# Qwen 3.5 397B — multi_turn/debugging_conversation

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 14.994s | tokens_per_second: 57.4
- input_tokens: 340 | output_tokens: 860
- judge_score: 5 | justificación: La respuesta es precisa, relevante y proporciona una solución detallada al problema de manejo de errores 429 con implementaciones de backoff exponencial, incluyendo ejemplos de código en Python, lo que la hace altamente útil y clara.

## Respuesta completa

¡Excelente diagnóstico! Ese loop de retries es exactamente lo que está causando el problema. Cada 429 genera 100 requests más, creando una tormenta de peticiones.

Aquí tienes cómo implementar retries correctamente:

## ✅ Implementación Correcta con Backoff Exponencial

### Python (usando `tenacity` - recomendado)

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import openai

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="tu-api-key"
)

@retry(
    stop=stop_after_attempt(5),  # Máximo 5 intentos
    wait=wait_exponential(multiplier=1, min=2, max=30),  # Backoff: 2s, 4s, 8s, 16s, 30s
    retry=retry_if_exception_type(openai.RateLimitError)
)
def llamar_api():
    return client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324",
        messages=[{"role": "user", "content": "Hola"}]
    )
```

### Python (implementación manual)

```python
import time
import random
from openai import RateLimitError

def llamar_con_retry(max_retries=5):
    for intento in range(max_retries):
        try:
            return client.chat.completions.create(...)
        except RateLimitError as e:
            if intento == max_retries - 1:
                raise
            
            # Leer header Retry-After si está disponible
            retry_after = e.response.headers.get('Retry-After')
            if retry_after:
                wait_time = int(retry_after)
            else:
                # Backoff exponencial con jitter
                wait_time = (2 ** intento) + random.uniform(0, 1)
            
            print(f"Rate limit. Esperando {wait_time}s...")
            time.sleep(wait_time)
```

## 🔑 Puntos Clave

| Elemento | Valor Recomendado | Por qué |
|----------|-------------------|---------|
| Máximo retries | 3-5 | Evita loops infinitos |
| Wait inicial | 1-2 segundos | No saturar inmediatamente |
| Wait máximo | 30-60 segundos | Límite razonable |
| Jitter | ±20% aleatorio | Evita que múltiples clientes sincronicen |

## 🚫 Lo que NO debes hacer

```python
# ❌ MAL - Retry infinito
while True:
    try:
        llamar_api()
    except:
        continue  # Esto causó tu problema!

# ❌ MAL - Sin espera
for i in range(100):
    try:
        llamar_api()
    except:
        pass  # Sin time.sleep!
```

## 📊 Headers que debes monitorear

Cuando recibas un 429, revisa estos headers en la respuesta:

```
x-ratelimit-limit-requests: 300
x-ratelimit-remaining-requests: 0
x-ratelimit-reset-requests: 60s
Retry-After: 30
```

**¿Qué lenguaje estás usando?** Puedo darte el código específico para tu stack (Node.js, Python, etc.).