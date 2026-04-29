# Kimi K2.5 (NIM) — multi_turn/debugging_conversation

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 7.22 | quality: 8.91
- latency_total: 109.018s | tokens_per_second: 15.7
- input_tokens: 391 | output_tokens: 1709
- judge_score: 4.6 | justificación: 

## Respuesta completa

 El problema es clásico: **thundering herd**. Cada 429 genera 100 requests más, lo que genera más 429s, y entras en un bucle de muerte que agota tus créditos y banea temporalmente tu IP.

Aquí tienes la implementación correcta de retries con **exponential backoff + jitter + límites**:

## 1. Reglas de oro para retries
- **Máximo 3-5 reintentos** (nunca infinito)
- **Solo retry en errores recuperables**: 429, 500, 502, 503, 504
- **NO retry en**: 400, 401, 403, 422 (eso es error de tu código)
- **Backoff exponencial**: 1s → 2s → 4s → 8s
- **Jitter aleatorio**: añade 0-1s aleatorio para evitar sincronización masiva

## 2. Implementación en Python (con `tenacity`)

```python
import random
import time
from tenacity import retry, stop_after_attempt, wait_exponential_jitter, retry_if_exception_type
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

def is_retryable_error(exception):
    """Solo retry en errores recuperables"""
    if isinstance(exception, HTTPError):
        status = exception.response.status_code
        # Solo 429 (rate limit) y errores de servidor
        return status in [429, 500, 502, 503, 504]
    return isinstance(exception, (ConnectionError, Timeout))

@retry(
    stop=stop_after_attempt(4),  # Máximo 4 intentos (1 original + 3 retries)
    wait=wait_exponential_jitter(initial=1, exp_base=2, jitter=1),  # 1s, 2s, 4s + jitter
    retry=retry_if_exception(is_retryable_error),
    before_sleep=lambda retry_state: print(f"Retry {retry_state.attempt_number}/4 tras error...")
)
def call_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://tusitio.com",  # Requerido por OpenRouter
        "X-Title": "Tu App"
    }
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json={
            "model": "deepseek/deepseek-chat",
            "messages": [{"role": "user", "content": prompt}]
        },
        timeout=30
    )
    
    # Manejo específico de 429
    if response.status_code == 429:
        # OpenRouter a veces manda Retry-After en headers
        retry_after = int(response.headers.get('Retry-After', 5))
        print(f"Rate limit hit. Esperando {retry_after}s...")
        time.sleep(retry_after)
        response.raise_for_status()  # Esto activará el retry
    
    response.raise_for_status()
    return response.json()
```

## 3. Implementación manual (sin librerías)

```python
import time
import random

def call_with_retry(prompt, max_retries=3):
    for attempt in range(max_retries + 1):
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {API_KEY}"},
                json={"model": "deepseek/deepseek-chat", "messages": [{"role": "user", "content": prompt}]},
                timeout=30
            )
            
            if response.status_code == 429:
                # Calcular espera exponencial + jitter
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                print(f"429 detectado. Esperando {wait_time:.1f}s (intento {attempt + 1}/{max_retries + 1})")
                time.sleep(wait_time)
                continue  # Intentar de nuevo
                
            if response.status_code >= 500:
                # Server error, también retry
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                time.sleep(wait_time)
                continue
                
            response.raise_for_status()
            return response.json()
            
        except (requests.Timeout, requests.ConnectionError) as e:
            if attempt == max_retries:
                raise
            time.sleep(2 ** attempt)
    
    raise Exception("Max retries exceeded")
```

## 4. Configuración específica para OpenRouter

Según la documentación actual de OpenRouter:
- **DeepSeek V3**: 300 RPM (requests por minuto)
- Si sigues viendo 429 con 5 req/min, verifica:
  1. No estés compartiendo la API key en otro servidor/script
  2. No tengas múltiples instancias de tu app corriendo
  3. Que no haya otro modelo en el historial de tu cuenta haciendo requests

## 5. Patrón adicional: Circuit Breaker

Si sigues teniendo problemas, implementa un **circuit breaker** simple:

```python
consecutive_errors = 0
MAX_CONSECUTIVE_ERRORS = 10

def safe_call(prompt):
    global consecutive_errors
    
    if consecutive_errors >= MAX_CONSECUTIVE_ERRORS:
        raise Exception("Circuit breaker activado - demasiados errores consecutivos")
    
    try:
        result = call_with_retry(prompt)
        consecutive_errors = 0  # Reset
        return result
    except Exception as e:
        consecutive_errors += 1
        raise
```

**Prueba primero con un solo request manual** para confirmar que tu API key funciona, luego implementa el retry con límites. ¿Necesitas ver el código en otro lenguaje (JavaScript, Go, etc.)?