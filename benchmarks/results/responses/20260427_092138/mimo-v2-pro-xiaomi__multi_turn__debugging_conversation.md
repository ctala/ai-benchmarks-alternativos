# MiMo V2-Pro (Xiaomi direct) — multi_turn/debugging_conversation

- model_id: `mimo-v2-pro`
- success: True  | final: 7.56 | quality: 8.74
- latency_total: 13.407s | tokens_per_second: 48.3
- input_tokens: 357 | output_tokens: 647
- judge_score: 4.8 | justificación: 

## Respuesta completa

Perfecto, encontraste el problema. Aqui tienes una implementacion correcta de retries con exponential backoff:

```python
import time
import requests

def call_openrouter(messages, model="deepseek/deepseek-chat-v3", max_retries=5):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages
    }

    for attempt in range(max_retries):
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )

        # Exito
        if response.status_code == 200:
            return response.json()

        # Error 429 - rate limit
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 2 ** attempt))
            wait_time = min(retry_after, 60)  # max 60 segundos
            print(f"Rate limited. Esperando {wait_time}s (intento {attempt+1}/{max_retries})")
            time.sleep(wait_time)
            continue

        # Otros errores - no reintentar
        response.raise_for_status()

    raise Exception(f"Fallo despues de {max_retries} intentos")
```

3 claves:

- **Max retries fijo** (5) - no infinito
- **Exponential backoff** - 1s, 2s, 4s, 8s, 16s - le da tiempo al rate limit a "respirar"
- **Respeta Retry-After** - si OpenRouter te dice cuanto esperar, usalo

Tambien agrega esto para no saturar desde el origen:

```python
from collections import deque
import time

class RateLimiter:
    def __init__(self, max_per_minute=20):
        self.max = max_per_minute
        self.timestamps = deque()

    def wait(self):
        now = time.time()
        # Limpiar timestamps viejos
        while self.timestamps and now - self.timestamps[0] > 60:
            self.timestamps.popleft()

        if len(self.timestamps) >= self.max:
            wait = 60 - (now - self.timestamps[0])
            time.sleep(wait)

        self.timestamps.append(time.time())

# Uso
limiter = RateLimiter(max_per_minute=20)

def call_with_limit(messages):
    limiter.wait()
    return call_openrouter(messages)
```

Con el RateLimiter evitas generar 429s en primer lugar, y el retry es solo como red de seguridad. Con 5 req/min que haces, ponle `max_per_minute=20` y tendras margen de sobra.