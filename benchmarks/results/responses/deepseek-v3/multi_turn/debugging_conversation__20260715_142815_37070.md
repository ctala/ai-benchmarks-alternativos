# DeepSeek V3.2 — multi_turn/debugging_conversation

- model_id: `deepseek/deepseek-chat`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 13.137s | tokens_per_second: 34.6
- input_tokens: 330 | output_tokens: 454
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución detallada y bien estructurada al problema de la API con errores 429, incluyendo técnicas de manejo de errores y backoff exponencial, lo que la hace altamente útil y clara.

## Respuesta completa

¡Ahí está el problema! Un retry infinito es peligroso con APIs. Te muestro una implementación robusta:

```python
import time
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),  # Máximo 3 intentos
    wait=wait_exponential(multiplier=1, min=4, max=10),  # Backoff exponencial
    retry=(lambda e: isinstance(e, (requests.exceptions.RequestException, 
                                  requests.exceptions.HTTPError)) 
           and e.response.status_code != 429)  # No reintentar en 429
)
def make_api_call(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=30  # Timeout para no quedarse colgado
    )
    
    if response.status_code == 429:
        retry_after = int(response.headers.get('Retry-After', 60))
        time.sleep(retry_after)
        raise Exception("Rate limit exceeded")  # Salir del retry decorator
    
    response.raise_for_status()  # Lanza excepción para otros errores HTTP
    return response.json()
```

Claves del diseño:
1. **Límite de reintentos** (3 es razonable)
2. **Backoff exponencial** para no saturar
3. **No reintentar automáticamente en 429** (espera el tiempo que diga el header)
4. **Timeout** para evitar requests colgados
5. **Retry-After** respeta el tiempo sugerido por la API

¿Necesitas adaptar esto a otro lenguaje?