# DeepSeek V3 — multi_turn/debugging_conversation

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.99 | quality: 10.0
- latency_total: 12.508s | tokens_per_second: 47.3
- input_tokens: 333 | output_tokens: 592
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una implementación detallada con backoff exponencial, abordando el problema de manera efectiva y proporcionando insights útiles para un emprendedor.

## Respuesta completa

¡Eso explica todo! Un retry infinito sin backoff causa un "rate limit amplification". Te explico el patrón correcto:

## Implementación con backoff exponencial:

```python
import requests
import time
import random

def call_openrouter_with_retry(prompt, api_key, max_retries=3):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek/deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 429:
                # Rate limit exceeded
                if attempt == max_retries - 1:
                    return None, "Rate limit exceeded after retries"
                
                # Exponential backoff con jitter
                wait_time = (2 ** attempt) + random.uniform(0,通过网络)
                time.sleep(wait_time)
                continue
                
            elif response.status_code >= 500:
                # Error del servidor
                if attempt == max_retries - 1:
                    return None, f"Server error: {response.status_code}"
                
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                time.sleep(wait_time)
                continue
                
            elif response.status_code == 200:
                return response.json(), None
                
            else:
                # Otros errores (400, 401, etc)
                return None, f"Error {response.status_code}: {response.text}"
                
        except Exception as e:
            if attempt == max_retries - 1:
                return None, f"Network error: {str(e)}"
            time.sleep(1 * (attempt + 1))
    
    return None, "Max retries exceeded"
```

## Reglas clave:
1. **MAX_RETRIES**: Usa 3-5 máximo
2. **Exponential backoff**: `wait_time = (2^attempt) + random_jitter`
3. **Jitter**: Aleatoriedad para evitar "thundering herd"
4. **No retry en 400/401**: Solo en 429, 500-503, timeout
5. **Considera headers de rate limit** (si OpenRouter los provee):
```python
if 'Retry-After' in response.headers:
    time.sleep(int(response.headers['Retry-After']))
```

¿Quieres que adapte esto a tu framework específico (FastAPI, Node.js, etc)?