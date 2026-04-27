# MiMo-V2-Omni (multimodal) — multi_turn/debugging_conversation

- model_id: `xiaomi/mimo-v2-omni`
- success: True  | final: 7.0 | quality: 7.42
- latency_total: 12.762s | tokens_per_second: 114.5
- input_tokens: 357 | output_tokens: 1461
- judge_score: 3.8 | justificación: 

## Respuesta completa

Perfecto, ese es el problema clásico. Vamos a implementar retries inteligentes con **backoff exponencial y jitter**.

## Solución recomendada:

### 1. Usar `tenacity` (librería de Python)
```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import httpx

@retry(
    stop=stop_after_attempt(5),  # Max 5 intentos
    wait=wait_exponential(multiplier=1, min=2, max=30),  # Espera 2s, 4s, 8s, 16s...
    retry=retry_if_exception_type(httpx.HTTPStatusError)
)
async def call_openrouter(messages):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"model": "deepseek/deepseek-chat", "messages": messages}
        )
        
        # Lanza excepción para códigos 429/5xx
        response.raise_for_status()
        return response.json()
```

### 2. Implementación manual (sin librerías)
```python
import asyncio
import random

async def call_with_retry(messages, max_retries=5):
    for attempt in range(max_retries):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={"Authorization": f"Bearer {API_KEY}"},
                    json={"model": "deepseek/deepseek-chat", "messages": messages}
                )
                
                if response.status_code == 429:
                    # Leer header Retry-After si existe
                    retry_after = response.headers.get('Retry-After', 2 ** attempt)
                    wait_time = float(retry_after) + random.uniform(0.1, 1.0)  # Jitter
                    
                    print(f"Rate limit. Esperando {wait_time:.2f}s...")
                    await asyncio.sleep(wait_time)
                    continue
                    
                response.raise_for_status()
                return response.json()
                
        except httpx.HTTPStatusError as e:
            if e.response.status_code >= 500 and attempt < max_retries - 1:
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                await asyncio.sleep(wait_time)
                continue
            raise
    
    raise Exception("Max reintentos alcanzados")
```

### 3. Patrón avanzado con monitoreo de headers
```python
async def call_smart(messages):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"model": "deepseek/deepseek-chat", "messages": messages}
        )
        
        # Monitorear rate limits
        remaining = response.headers.get('x-ratelimit-remaining', 'unknown')
        reset = response.headers.get('x-ratelimit-reset', 'unknown')
        
        if int(remaining) < 5:  # Quedan pocas requests
            print(f"⚠️ Rate limit bajo. Quedan: {remaining}, reset: {reset}")
            await asyncio.sleep(1)  # Pausa preventiva
        
        if response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 60))
            print(f"⏸️ Rate limit. Esperando {retry_after}s")
            await asyncio.sleep(retry_after + 1)
            return await call_smart(messages)  # Reintento único
        
        return response.json()
```

## Consejos adicionales:

1. **Verifica los headers de OpenRouter**:
   ```python
   # Headers útiles que devuelve OpenRouter:
   # x-ratelimit-limit: 300
   # x-ratelimit-remaining: 298
   # x-ratelimit-reset: 1704067200
   # Retry-After: 60 (solo en 429)
   ```

2. **Implementa un circuit breaker**:
```python
from datetime import datetime, timedelta

class CircuitBreaker:
    def __init__(self, max_failures=5, reset_timeout=60):
        self.failures = 0
        self.last_failure = None
        self.max_failures = max_failures
        self.reset_timeout = reset_timeout
    
    def can_execute(self):
        if self.failures >= self.max_failures:
            if datetime.now() - self.last_failure > timedelta(seconds=self.reset_timeout):
                self.failures = 0  # Reset después del timeout
                return True
            return False
        return True
```

3. **Recomendación final**:
   - Usa `tenacity` si quieres algo robusto ya probado
   - Implementa monitoreo de los headers `x-ratelimit-*`
   - Considera agregar una cola de requests con límite de concurrencia

¿Quieres que profundice en alguna de estas implementaciones o prefieres una solución más específica para tu caso?