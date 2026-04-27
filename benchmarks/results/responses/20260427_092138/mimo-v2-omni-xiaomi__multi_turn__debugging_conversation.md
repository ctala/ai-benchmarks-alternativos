# MiMo V2-Omni (Xiaomi direct) — multi_turn/debugging_conversation

- model_id: `mimo-v2-omni`
- success: True  | final: 7.75 | quality: 8.71
- latency_total: 14.398s | tokens_per_second: 136.4
- input_tokens: 357 | output_tokens: 1964
- judge_score: 4.4 | justificación: 

## Respuesta completa

El loop infinito es el problema principal. Aquí te muestro cómo implementar reintentos inteligentes con backoff exponencial:

## Solución con backoff exponencial

```python
import time
import requests
from typing import Optional

class OpenRouterClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://openrouter.ai/api/v1"
        
    def make_request(self, 
                    prompt: str, 
                    model: str = "deepseek/deepseek-chat",
                    max_retries: int = 3) -> Optional[dict]:
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        for attempt in range(max_retries + 1):
            try:
                response = requests.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=30
                )
                
                # Si es 429, esperar y reintentar
                if response.status_code == 429:
                    if attempt == max_retries:
                        print(f"Error 429 después de {max_retries} reintentos")
                        return None
                    
                    # Calcular tiempo de espera (backoff exponencial)
                    wait_time = (2 ** attempt) + 1  # 2, 5, 9 segundos
                    
                    # Si hay header Retry-After, usarlo
                    retry_after = response.headers.get('Retry-After')
                    if retry_after:
                        try:
                            wait_time = int(retry_after)
                        except ValueError:
                            pass
                    
                    print(f"Rate limit alcanzado. Esperando {wait_time} segundos...")
                    time.sleep(wait_time)
                    continue
                
                # Si es otro error, lanzar excepción
                response.raise_for_status()
                
                return response.json()
                
            except requests.exceptions.RequestException as e:
                if attempt == max_retries:
                    print(f"Error después de {max_retries} reintentos: {e}")
                    return None
                time.sleep(1)  # Espera mínima para otros errores
        
        return None
```

## Solución mejorada con `tenacity` (recomendada)

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

@retry(
    stop=stop_after_attempt(3),  # Máximo 3 intentos
    wait=wait_exponential(multiplier=1, min=2, max=10),  # Espera exponencial
    retry=retry_if_exception_type(requests.exceptions.HTTPError)
)
def make_api_call(prompt: str, api_key: str):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-chat",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    
    # Lanzar excepción para códigos 429 y 5xx
    if response.status_code == 429 or response.status_code >= 500:
        response.raise_for_status()
    
    return response.json()
```

## Para tu caso específico, revisa:

1. **Headers de rate limiting**: Añade esto para ver los límites:
```python
response = requests.post(...)
print(f"X-RateLimit-Limit: {response.headers.get('X-RateLimit-Limit')}")
print(f"X-RateLimit-Remaining: {response.headers.get('X-RateLimit-Remaining')}")
print(f"Retry-After: {response.headers.get('Retry-After')}")
```

2. **Si usas curl**, prueba con:
```bash
curl -X POST https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer TU_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek/deepseek-chat",
    "messages": [{"role": "user", "content": "Hola"}]
  }' -v
```

3. **Verifica en el dashboard** de OpenRouter:
   - Ve a https://openrouter.ai/keys
   - Revisa los logs de tu API key
   - Verifica que el modelo esté disponible

¿Puedes compartir el fragmento de código donde tienes el loop infinito? Así te ayudo a corregirlo específicamente.