# Mistral Large 3 675B (NIM) — multi_turn/debugging_conversation

- model_id: `mistralai/mistral-large-3-675b-instruct-2512`
- success: True  | final: 7.09 | quality: 8.82
- latency_total: 102.722s | tokens_per_second: 6.9
- input_tokens: 331 | output_tokens: 704
- judge_score: 4.8 | justificación: 

## Respuesta completa

¡Ahí está el problema! Un retry infinito es peligroso con APIs que tienen rate limits. Vamos a implementar una estrategia robusta de retries paso a paso:

### Solución recomendada (Python con `requests`):

```python
import requests
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configuración de retry inteligente
retry_strategy = Retry(
    total=3,  # Máximo 3 intentos totales
    backoff_factor=1,  # Espera exponencial: 1s, 2s, 4s...
    status_forcelist=[429, 500, 502, 503, 504],  # Códigos para reintentar
    allowed_methods=["POST"]  # Solo reintentar POST (ajusta según tu caso)
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)

def call_openrouter(prompt):
    try:
        response = session.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "model": "deepseek/deepseek-chat",
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=30  # Timeout de 30 segundos
        )
        response.raise_for_status()  # Lanza excepción para códigos 4xx/5xx
        return response.json()

    except requests.exceptions.RetryError:
        print("Demasiados intentos fallidos")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error en la request: {e}")
        return None
```

### Reglas clave para evitar 429:
1. **Backoff exponencial**: Espera más tiempo entre cada intento (ej: 1s, 2s, 4s)
2. **Límite de intentos**: Máximo 3-5 reintentos por request
3. **Solo reintentar errores temporales**: 429, 5xx, pero no 400/401/403
4. **Timeout obligatorio**: Evita que requests colgadas consuman tu rate limit

### Alternativa con libreria `tenacity` (más limpio):
```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type(requests.exceptions.RequestException)
)
def call_openrouter(prompt):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"model": "deepseek/deepseek-chat", "messages": [{"role": "user", "content": prompt}]},
        timeout=30
    )
    response.raise_for_status()
    return response.json()
```

¿Quieres que adaptemos esta solución a tu lenguaje/framework específico?