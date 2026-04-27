# MiMo V2.5 (Xiaomi) — multi_turn/debugging_conversation

- model_id: `mimo-v2.5`
- success: True  | final: 7.59 | quality: 8.54
- latency_total: 22.606s | tokens_per_second: 58.3
- input_tokens: 357 | output_tokens: 1318
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Exacto! Un retry infinito es peligroso. Vamos a implementar una estrategia adecuada. Aquí tienes un enfoque paso a paso:

## **Solución: Retry con backoff exponencial y jitter**

### **1. Código base corregido**
```python
import time
import random
import requests

def call_api_with_retry(max_retries=5, base_delay=1):
    for attempt in range(max_retries):
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {API_KEY}"},
                json={...}
            )
            
            # Si es 429, esperar y reintentar
            if response.status_code == 429:
                # Obtener tiempo de espera del header si existe
                retry_after = response.headers.get('Retry-After')
                
                if retry_after:
                    wait_time = float(retry_after)
                else:
                    # Backoff exponencial con jitter
                    wait_time = base_delay * (2 ** attempt) + random.uniform(0, 1)
                
                print(f"Rate limited. Esperando {wait_time:.1f}s (intento {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
                continue
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise
            print(f"Error: {e}. Reintentando...")
            time.sleep(base_delay * (2 ** attempt))
    
    raise Exception("Máximo de reintentos alcanzado")
```

### **2. Mejoras importantes**

**A. Usa los headers de rate limit de OpenRouter:**
```python
# Headers que deberías recibir en 429:
# x-ratelimit-limit-requests: 300
# x-ratelimit-remaining-requests: 0
# x-ratelimit-reset-requests: 1699999999
# x-ratelimit-limit-tokens: 200000
# x-ratelimit-remaining-tokens: 0
# x-ratelimit-reset-tokens: 1699999999

# Implementa un rate limiter local:
from ratelimit import limits, sleep_and_retry

@sleep_and_retry
@limits(calls=5, period=60)  # 5 llamadas por minuto
def call_api():
    return requests.post(...)
```

**B. Circuit breaker pattern (para fallos persistentes):**
```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, reset_timeout=60):
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.last_failure_time = None
        
    def record_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        
    def is_open(self):
        if self.failure_count >= self.failure_threshold:
            if time.time() - self.last_failure_time > self.reset_timeout:
                self.failure_count = 0
                return False
            return True
        return False
```

### **3. Estrategia recomendada para producción**

```python
import backoff

@backoff.on_exception(
    backoff.expo,
    (requests.exceptions.RequestException, ConnectionError),
    max_tries=5,
    max_time=30
)
def resilient_api_call():
    # Tu código de llamada aquí
    pass
```

### **4. Checklist inmediato:**

1. **Elimina** tu loop infinito actual
2. **Implementa** máximo 3-5 reintentos
3. **Añade** delays progresivos (1s, 2s, 4s, 8s...)
4. **Registra** los reintentos para debugging
5. **Monitorea** los headers `x-ratelimit-*` para ajustar tu rate

### **5. Para debuggear ahora mismo:**

```python
# Test rápido sin retry
import requests
response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={"Authorization": f"Bearer TU_KEY"},
    json={"model": "deepseek/deepseek-chat", "messages": [{"role": "user", "content": "test"}]}
)
print(response.status_code)
print(response.headers.get('x-ratelimit-remaining-requests'))
```

**¿Qué lenguaje/SDK estás usando?** Así puedo darte un ejemplo más específico. ¿Python, Node.js, u otro?